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

test_name = "\n\nTest#04_read_device_info "
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
    time.sleep(5)

    ai.control_click(init.tool_title, "[NAME:resetButton]")
    ai.win_wait_active(init.popup_title)
    print("Waiting for restart...")
    time.sleep(3)

    if  repo.wait_while_not_in_text("Successfully restarted device", init.popup_title, 60): 
        resolution += "\nDevice restart successful! Test case: PASS"
        print("Device restart successful!")
    else:
        resolution += "\nDevice restart NOT successful! Test case: FAIL"
        print("Device restart failed :(")
    time.sleep(1)

    ai.control_click(init.popup_title, "[NAME:okButton]")
    time.sleep(2)

print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)