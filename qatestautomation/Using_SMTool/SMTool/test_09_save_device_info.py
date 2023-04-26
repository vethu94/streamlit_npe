"""
This script reads the device info of a CAS unit.
DUT: SMTool

COM port has to preset in SMTool

"""


import autoit as ai
import time
import os
import repo
import smtool_init as init
from datetime import datetime 

test_name = "\n\nTest#09_save_device_info "
time_and_date = str(datetime.now())
resolution = test_name + time_and_date
device_info = resolution + "\n\n"

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
    time.sleep(4)
    resolution = resolution + "\nCOM" + str(active_com) + ": OK"

    #press the refresh button 
    ai.control_click(init.tool_title, init.refresh_button)
    time.sleep(1)  
    if  repo.wait_while_not_in_text("Unit Type", init.tool_title):
        device_info += ai.win_get_text(init.tool_title, buf_size=1024)
        resolution += "\nTest Case: PASS"
    else:
        resolution += "\nTest Case: FAIL"
    time.sleep(2)

print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
repo.store_device_info(init.device_info_path, device_info)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)