"""
This script performs the "Refresh" and "Reset" actions on given unit connected to particular COM port. 
DUT: SMTool
Action sequence: Refresh - Reset - Refresh
COM port has to preset in SMTool

"""


import autoit as ai
import time
import os
import repo



test_dir = r"C:\Program Files (x86)\Hexagon_Mining\SafetyToolbox"
test_prog = r"\ToolboxLauncher.exe"
title = "HxGN MineProtect Toolbox"
tool = "SMTool"
tool_title = "SMTool Generator Mateusz Lerch"
popup_title = "Progress"
timeout = 15


repo.start_program(test_dir,test_prog,title)
ai.control_click(title,tool)
ai.win_wait_active(tool_title)
repo.search_tab_with_text("Device Info")
time.sleep(1)
print("Refresh device information!")
ai.control_click(tool_title,"Refresh")
repo.wait_while_not_in_text("Unit Type:",tool_title, timeout)



time.sleep(1)
print("Reseting the device!")
ai.control_click(tool_title,"Reset Device")
ai.win_wait_active(popup_title)

repo.wait_while_not_in_text("Successfully restarted device", popup_title, timeout)
ai.control_click(popup_title,"Ok")
print("Reset succesful!")

print("Refresh device information!")
ai.control_click(tool_title,"Refresh")
repo.wait_while_not_in_text("Unit Type:",tool_title, timeout)

time.sleep(1)
print("Closing tool")
ai.win_close(tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(title)