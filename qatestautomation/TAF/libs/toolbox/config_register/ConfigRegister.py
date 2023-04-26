import time

from pywinauto.application import ProcessNotFoundError
from pywinauto.application import Application

from libs.toolbox.ToolboxLauncher import ToolboxLauncher
from libs.config import config
from libs.toolbox.config_register.FwManagerTab import FwManagerTab
from libs.toolbox.config_register.CasConfigurationTab import CasConfigurationTab
from libs.toolbox.config_register.Cas10ConfigurationTab import Cas10ConfigurationTab
from libs.toolbox.UIBase import UIBase


class ConfigRegister(UIBase):
    def __init__(self) -> None:
        self.cr = self.open_app()

        # wait for connecting to backend
        self.cr.child_window(auto_id='searchPanelView').wait("enabled", timeout=25)

        self.focus_window()

        # Controls to known windows
        self.cas_config = None
        self.cas10_config = None
        self.fw_manager = None

    def open_app(self):
        try:
            self.app = Application(backend='uia').connect(
                path=config["CONFIG_REGISTER_PATH"])
        except ProcessNotFoundError:
            # if CR not open yet, start it via Toolbox launcher
            self.app = ToolboxLauncher().open_config_register()

        return self.app.window(title_re=".*Configuration Register*.", visible_only=False)

    def focus_window(self):
        self.cr.restore().set_focus()

    def select_from_vehicle_tree(self, item):
        self.search_in_vehicle_tree(item)
        self.click_in_vehicle_tree(item)

    def search_in_vehicle_tree(self, item):
        """Type in search box of vehicle tree. This should give a small list of items,
        ideally all of them should fit into the shown tree and no need for scrolling is needed.
        Args:
            item ([string]): item name from vehicle tree
        """
        self.cr.child_window(auto_id='textBoxSearch').set_edit_text(item)

    def click_in_vehicle_tree(self, item):
        item_ctrl = self._find_item(
            item, self.cr, ancestor_auto_id="vehiclesTabPage")
        item_ctrl.click_input()

    def clear_vehicle_search(self):
        self.cr.child_window(
            auto_id='textBoxSearch').set_edit_text(u'')  # clean-up

    def open_cas_configuration_tab(self):
        self.cas_config = CasConfigurationTab(self.cr)

    def open_cas10_configuration_tab(self):
        self.cas10_config = Cas10ConfigurationTab(self.cr)

    def open_fw_manager_tab(self):
        self.fw_manager = FwManagerTab(self.cr)

    def publish(self):
        """ Click publish button and close popup window - It will only work if publish is 
        successfull. 
        """
        self.press_publish_button()
        self.confirm_publish_popup()

    def press_publish_button(self, unit=None):
        if unit:
            self.select_from_vehicle_tree(unit)
        self.cr.PublishButton.click_input()

    def confirm_publish_popup(self, unit=None):
        self.cr.child_window(auto_id="PublishConfigView").OkButton.click()
        self.cr.child_window(title="Config published",
                             control_type="Window").OkButton.click()


if __name__ == '__main__':
    start = time.time()
    cr = ConfigRegister()
    cr.select_from_vehicle_tree("lds1")
    cr.open_cas_configuration_tab()
    cr.clear_vehicle_search()
    cr.cas_config.get_fw_list()
    cr.cas_config.get_current_fw()
    cr.cas_config.select_fw("sm4.81_6106_bcfdb51ad.fw_4.8.1")
    try:  # it will fail if given FW already selected
        cr.cas_config.press_save_button()
        cr.publish()
    except:
        pass

    cr.select_from_vehicle_tree("TestLTE4")
    cr.open_cas10_configuration_tab()
    cr.cas10_config.get_display_fw_list()
    cr.cas10_config.select_fw("Etna_image_10.1.99.fwp_10.1.99")
    try:  # it will fail if given FW already selected
        cr.cas10_config.press_save_button()
        cr.publish()
    except:
        pass

    cr.open_fw_manager_tab()
    cr.fw_manager.is_fw_added("Etna_image_10.1.101.fwp")

    duration = time.time() - start
    print(f"ConfigRegister main executed in {duration}")
