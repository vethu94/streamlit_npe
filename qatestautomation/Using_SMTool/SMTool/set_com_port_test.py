import repo
import time
import os
import autoit as ai
import serial.tools.list_ports_windows

test_dir = r"C:\Program Files (x86)\Hexagon_Mining\SafetyToolbox"
test_prog = r"\ToolboxLauncher.exe"
title = "HxGN MineProtect Toolbox"
tool = "SMTool"
tool_title = "SMTool Generator Mateusz Lerch"
popup_title = "Progress"
search_win_title ="Open"
upload_config = 0
#COM = [28, 29, 31, 37, 38]  #this list has to represent actual state of available COM ports on the machine

active_com = 37


'''
COM_list = serial.tools.list_ports_windows.comports()
print(len(COM_list))
for i in range(len(COM_list)):
    COM_list[i] = int(COM_list[i].device[3:])
COM_list.sort()   

print(COM_list)
'''



timeout_vlong = 200
timeout_long = 60
timeout_short = 8

fw_path = r"C:\Users\lmate\Documents\SM_CAS\Firmware\FW4.2.1\SM4.21_5543_9991cd2.fw"
#fw_path = r"C:\Users\lmate\Documents\SM_CAS\Firmware\Testing\FW4.0.3_release_candiate_to_test\SM4.03_4820_82a84b4.fw"
config_path =r"C:\Users\lmate\Documents\SM_CAS\ini files\universal_TEST05.ini"

#Start the Toolbox program
repo.start_program(test_dir,test_prog,title)

#Start SMTool
repo.start_tool_in_program(title,tool,tool_title)
'''
for i in range(len(COM)):
    repo.set_com_port(tool_title,COM[i],COM)
    time.sleep(2)
'''
repo.set_com_port(tool_title,active_com)
