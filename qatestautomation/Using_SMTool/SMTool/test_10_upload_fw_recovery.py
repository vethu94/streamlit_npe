"""
This script uploads a config file to a CAS unit.
DUT: SMTool

COM port has to preset in SMTool

"""


import autoit as ai
import time
import os
import repo
import smtool_init as init
from datetime import datetime

test_name = "\n\nTest#10_upload_fw_recovery "
time_and_date = str(datetime.now())
resolution = test_name + time_and_date

#Start the program
repo.start_program(init.test_dir,init.test_prog,init.title)

#Start SMTool
repo.start_tool_in_program(init.title,init.tool,init.tool_title)
time.sleep(1)

#Search for desired tab in SMTool
if repo.search_tab_with_text("Device Info"):
    resolution += "\nTab: PASS"
else:
    resolution += "\nTab: FAIL"
time.sleep(1)

for active_com in init.active_com_list:
    #Set COM port
    repo.set_com_port(init.tool_title, active_com)
    resolution = resolution + "\nCOM" + str(active_com) + ": OK"
    time.sleep(1)

    ai.control_click(init.tool_title, init.recovery_upload_button)
    ai.win_wait_active(init.search_win_title)
    time.sleep(1)

    ai.control_set_text(init.search_win_title, "[CLASS:Edit; INSTANCE:1]", init.fw_path)
    time.sleep(1)

    ai.control_click(init.search_win_title, "[CLASS:Button; INSTANCE:1]")
    resolution +="\nRecovery update started !"

    if repo.wait_while_not_in_text("Not enough space", init.popup_title, init.timeout_short):
        print("Not enough space on Device !")
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "Not enough space on Device ! Test Case: FAIL"

    
    if repo.wait_while_not_in_text("Successfully installed", init.popup_title, init.timeout_vlong):
        print("FW installation was successfull !")
        time.sleep(1)
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "\nFW installation was successfull ! Test Case: PASS"
    else:
        resolution += "\nFW installation was NOT successfull ! Test Case: FAIL"
        print("FW installation was NOT successfull ! Test Case: FAIL")
   

print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)