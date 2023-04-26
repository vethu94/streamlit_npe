from libs.toolbox.UIBase import UIBase


class FwManagerTab(UIBase):
    def __init__(self, cr_window) -> None:
        self.cr = cr_window
        self.tab_name = "Manage Firmware"
        self.open_fw_manager_tab()
        self.fw_manager_tab = self._get_fw_manager_tab_control()

    def open_fw_manager_tab(self):
        self.cr.ManageFirmwareTab.click_input()

    def _get_fw_manager_tab_control(self):
        return self.cr.child_window(title=self.tab_name, control_type="Pane")

    def is_fw_added(self, fw):
        fw_item = self._find_item(
            fw, self.fw_manager_tab, ancestor_title="Data Panel")
        return fw_item
