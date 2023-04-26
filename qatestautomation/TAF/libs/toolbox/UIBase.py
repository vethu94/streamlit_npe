import sys
import locale
import six

from pywinauto import findbestmatch


class UIBase():
    def _find_item(self,
                   item_value,
                   root_ctrl,
                   item_type=None,
                   ancestor_title=None,
                   ancestor_auto_id=None,
                   ancestor_ctrl_type=None,
                   bestmatch_ctrl=None):
        """Traverse a tree of currently visible elements and select one that matches given value. 
        Starting point of the traverse might be a root control or an ancestor node if its name, 
        automation ID and/or control type are given. This will make the search more efficient.

        bestmatch_ctrl is "temporary" solution to getting an ancestor if given information is not
        enough to identify it. In this case we can try to search for its parent and then get it with
        pywinauto's best match algorithm.

        Args:
            item_value ([string]): item's value, note it is not the same as item's name
            root_ctrl ([control]): the root of UI elements tree where the search will be done.
            return item's control if found, otherwise False.
        """
        if ancestor_title is not None and ancestor_auto_id is not None and \
                ancestor_ctrl_type is not None:
            window = root_ctrl
        else:
            window = root_ctrl.child_window(auto_id=ancestor_auto_id, title=ancestor_title,
                                            control_type=ancestor_ctrl_type)
        return get_control_identifier(item_value,
                                      window,
                                      item_type,
                                      bestmatch_ctrl=bestmatch_ctrl)


def get_control_identifier(item_value, ctrl,
                           item_type=None, depth=None,
                           bestmatch_ctrl=None,
                           verbose=False):
    """
    Get the control of identifier or one of its nodes
    ctrl - limit seach to a given control and its children
    bestmatch_ctrl = node of ctrl - if node does not have a sensible unique name or automationId, 
    best_match can by used but first a list of possible matches needs to be build (name_ctrl_id_map)
    For building bestmatch list a parent node is needed, at least in this implementation 
    criteria - default criteria from pywinauto
    TODO to be revisited
    """
    if depth is None:
        depth = sys.maxsize

    def prepare_ctrls(ctrl, already_resolved=False):
        this_ctrl = ctrl if already_resolved else ctrl._WindowSpecification__resolve_control(
            ctrl.criteria)[-1]

        # Create a list of this control and all its descendants
        all_ctrls = [this_ctrl, ] + this_ctrl.descendants()

        # Create a list of all visible text controls
        txt_ctrls = [ctrl for ctrl in all_ctrls if ctrl.can_be_label and ctrl.is_visible() and
                     ctrl.window_text()]

        # Build a dictionary of disambiguated list of control names
        name_ctrl_id_map = findbestmatch.UniqueDict()
        for index, ctrl in enumerate(all_ctrls):
            ctrl_names = findbestmatch.get_control_names(
                ctrl, all_ctrls, txt_ctrls)
            for name in ctrl_names:
                name_ctrl_id_map[name] = index

        # Swap it around so that we are mapped off the control indices
        ctrl_id_name_map = {}
        for name, index in name_ctrl_id_map.items():
            ctrl_id_name_map.setdefault(index, []).append(name)

        return this_ctrl, all_ctrls, ctrl_id_name_map, name_ctrl_id_map

    this_ctrl, all_ctrls, ctrl_id_name_map, name_ctrl_id_map = prepare_ctrls(ctrl)
    if bestmatch_ctrl:
        this_ctrl = all_ctrls[name_ctrl_id_map[bestmatch_ctrl]]
        _, all_ctrls, ctrl_id_name_map, _ = prepare_ctrls(ctrl)

    def traverse_tree(ctrls, item_value, current_depth=1, found=False,
                      verbose=verbose):
        """Recursively traverse ctrls tree until ctrl with item_value value is found"""
        if found:
            return found
        if len(ctrls) == 0 or current_depth > depth:
            return False
        found = False
        indent = (current_depth - 1) * u"   | "
        for ctrl in ctrls:
            if found:
                return found
            try:
                ctrl_id = all_ctrls.index(ctrl)
            except ValueError:
                continue

            if hasattr(ctrl.element_info, 'control_type'):
                control_type = ctrl.element_info.control_type
            else:
                control_type = None

            try:
                ctrl_value = ctrl.legacy_properties()['Value'].lower().strip()
                searched_value = item_value.lower().strip()
                if verbose:
                    print(f"{searched_value} vs {ctrl_value}: ({ctrl_value == searched_value})")
                if ctrl_value == item_value.lower().strip() and \
                        (item_type is None or item_type == control_type):
                    found = ctrl

                    if verbose:
                        # get more info on found control
                        print_control_info(ctrl)
            except:
                pass
            finally:
                if verbose:
                    print_control_tree_nodes(ctrl, indent, ctrl_id_name_map, ctrl_id)

            if not found:
                found = traverse_tree(
                    ctrl.children(), item_value, current_depth + 1, found)
            else:
                return found
        return found

    return traverse_tree([this_ctrl, ], item_value)


def print_control_info(ctrl):
    print(f"Value: {ctrl.legacy_properties()['Value']}")
    print(dir(ctrl))


def print_control_tree_nodes(ctrl, indent, ctrl_id_name_map, ctrl_id):
    ctrl_text = ctrl.window_text()
    if ctrl_text:
        # transform multi-line text to one liner
        ctrl_text = ctrl_text.replace(
            '\n', r'\n').replace('\r', r'\r')

    output = indent + u'\n'
    output += indent + u"{class_name} - '{text}'    {rect}\n"\
        "".format(class_name=ctrl.friendly_class_name(),
                  text=ctrl_text,
                  rect=ctrl.rectangle())
    output += indent + u'{}'.format(ctrl_id_name_map[ctrl_id])

    title = ctrl_text
    class_name = ctrl.class_name()
    auto_id = None
    control_type = None
    if hasattr(ctrl.element_info, 'automation_id'):
        auto_id = ctrl.element_info.automation_id
    if control_type:
        class_name = None  # no need for class_name if control_type exists
    else:
        control_type = None  # if control_type is empty, still use class_name instead
    criteria_texts = []
    if title:
        criteria_texts.append(u'title="{}"'.format(title))
    if class_name:
        criteria_texts.append(
            u'class_name="{}"'.format(class_name))
    if auto_id:
        criteria_texts.append(u'auto_id="{}"'.format(auto_id))
    if control_type:
        criteria_texts.append(
            u'control_type="{}"'.format(control_type))
    if title or class_name or auto_id:
        output += u'\n' + indent + \
            u'child_window(' + u', '.join(criteria_texts) + u')'
    if six.PY3:
        print(output)
    else:
        print(output.encode(
            locale.getpreferredencoding(), errors='backslashreplace'))
