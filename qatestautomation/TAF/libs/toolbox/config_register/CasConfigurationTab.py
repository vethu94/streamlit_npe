from libs.toolbox.UIBase import UIBase


class CasConfigurationTab(UIBase):
    def __init__(self, cr_window) -> None:
        self.cr = cr_window
        self.tab_name = "CAS Configuration"

        self.open_cas_configuration_tab()

        self.cas_config_tab = self._get_cas_config_tab_control()

    def open_cas_configuration_tab(self):
        self.cr.CasConfigurationTab.click_input()

    def _get_cas_config_tab_control(self):
        return self.cr.child_window(title=self.tab_name, control_type="Pane")

    def select_fw(self, fw):
        fw_item = self._find_item(fw, self.cr, ancestor_title="CAS Configuration",
                                  ancestor_ctrl_type="Pane", bestmatch_ctrl="FirmwarePane0",
                                  item_type="ListItem")
        fw_item.select()

    def get_fw_list(self, fw="SM4.81_6106_bcfdb51ad.fw_4.8.1"):
        """TODO Refactor once FW combo box has a unique automation ID
        Return a list of available FWs. The first item in list is current FW.
        Args:
            fw (str, optional): [description]. Defaults to "SM4.81_6106_bcfdb51ad.fw_4.8.1".
        """
        fw_item = self._find_item(fw, self.cr, ancestor_title="CAS Configuration",
                                  ancestor_ctrl_type="Pane", bestmatch_ctrl="FirmwarePane0",
                                  item_type="ListItem")
        available_fws = []
        # texts is a list of lists e.g.
        # [[' '], ['SM4.46_5833_fd3bb34e1.fw_4.4.6'], ['SM4.65_5980_225e7d558.fw_4.6.5']
        for f in fw_item.parent().texts():
            available_fws.append(f[0])

        # Move already selected item to the first position in list
        current_item = fw_item.parent().window_text()
        available_fws.pop(available_fws.index(current_item))
        available_fws.insert(0, current_item)

        return available_fws

    def get_current_fw(self, fw="SM4.81_6106_bcfdb51ad.fw_4.8.1"):
        """TODO Refactor once FW combo box has a unique automation ID

        Args:
            fw (str, optional): [description]. Defaults to "SM4.81_6106_bcfdb51ad.fw_4.8.1".
        """
        fw_item = self._find_item(fw, self.cr, ancestor_title="CAS Configuration",
                                  ancestor_ctrl_type="Pane", bestmatch_ctrl="FirmwarePane0",
                                  item_type="ListItem")
        return fw_item.parent().window_text()

    def press_save_button(self):
        self.cas_config_tab.SaveButton.click()
