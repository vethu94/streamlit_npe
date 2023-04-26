import time

from pywinauto.application import Application
from pywinauto.application import ProcessNotFoundError

from libs.config import config


class ToolboxLauncher:
    def __init__(self) -> None:
        try:
            self.app = Application(backend='uia').connect(path=config["TOOLBOX_LAUNCHER_PATH"])
        except ProcessNotFoundError:
            self.app = Application(backend='uia').start(config["TOOLBOX_LAUNCHER_PATH"])
        self.toolbox_launcher = self.app.window(title_re=".*HxGN MineProtect Toolbox*.",
                                                visible_only=False)
        self.toolbox_launcher.restore().set_focus()

    def open_sm_tool(self):
        self.toolbox_launcher.SMTool.click()

    def open_config_register(self):
        self.toolbox_launcher.ConfigRegister.click()
        self.cr = Application(backend='uia').connect(
            path=config["CONFIG_REGISTER_PATH"], timeout=5)
        self.cr.HxgnMineprotectConfigurationRegister.wait("enabled", timeout=25)
        # searchPanelView
        time.sleep(6)

        return self.cr


if __name__ == '__main__':
    tl = ToolboxLauncher()
    tl.open_config_register()
    tl.open_sm_tool()
