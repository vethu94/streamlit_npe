import autoit as ai
import time
import file_handling
import win_navigation
import config_param.config_param_gen as init


def readdevinfo(comport):
    """
    This function reads the device info of a CAS unit in a certain port.
    CAS should be connected to COM port
    """
    details = ""
    data = ""
    # Search for desired tab in SMTool
    if win_navigation.search_tab_with_text("Device Info"):
        ai.control_click(init.tool_title, init.refresh_button)
    if win_navigation.wait_while_not_in_text("Unit Type", init.tool_title):
        time.sleep(1)
    time.sleep(2)
    control = "[NAME:textBox]"
    data += ai.control_get_text(init.tool_title, control, buf_size=1024)
    while data.startswith("Wait for Refresh"):
        time.sleep(1)
        details += "Device info is not loaded yet!\n"
    file_handling.store_device_info(comport, init.device_info_path, data)
    details += "Successfully wrote Device info in txt file\n"
    return data, details