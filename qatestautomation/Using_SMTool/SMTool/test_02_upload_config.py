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

test_name = "\n\nTest#02_upload_config "
time_and_date = str(datetime.now())
resolution = test_name + time_and_date 



#Start the program
repo.start_program(init.test_dir,init.test_prog,init.title)

#Start SMTool
repo.start_tool_in_program(init.title,init.tool,init.tool_title)

#Search for desired tab in SMTool
if repo.search_tab_with_text("Device Configuration"):
    resolution += "\nTab: PASS"
else:
    resolution += "\nTab: FAIL"
time.sleep(1)

for active_com in init.active_com_list:
    #Set COM port
    repo.set_com_port(init.tool_title, active_com)
    resolution = resolution + "\nCOM" + str(active_com) + ": OK"
    time.sleep(2)

    #Disable all options
    repo.disable_all_config_options(init.tool_title)
    time.sleep(1)

    #check the desired option
    if int(ai.control_command(init.tool_title, init.control_file_box["conf"], "IsEnabled")):
        print("Option already checked!")
    else:
        ai.control_click(init.tool_title, init.control_check_box["conf"])
        time.sleep(1)

    time.sleep(1)
    ai.control_click(init.tool_title, init.control_file_point)

    #enter path to config file 
    ai.control_set_text(init.tool_title, init.control_file_box["conf"], init.config_path)
    time.sleep(1)


    #upload the config file
    ai.control_click(init.tool_title, init.upload_button)
    resolution = resolution + "\nUploading FW: " + str(init.config_path)
    time.sleep(1)

    ai.win_wait_active(init.popup_title) 

    if repo.wait_while_not_in_text("Warning", init.popup_title, init.timeout_short):
        ai.control_click(init.popup_title, init.ok_button)
        #print("OK")
    if repo.wait_while_not_in_text("Not enough space", init.popup_title, init.timeout_short):
        print("Not enough space on Device !")
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "Not enough space on Device ! Test Case: FAIL"
    time.sleep(3)

    if repo.wait_while_not_in_text("File already on Device", init.popup_title, init.timeout_short):
        print("Configuration file already installed on the device !")
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "\nConfiguration file already installed on the device !"
    elif repo.wait_while_not_in_text("Successfull installation", init.popup_title, init.timeout_long):
        print("Config upload was successfull !")
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "\nConfig upload was successfull ! Test Case: PASS"
    else:
        print("Config update NOT successfull !") 
        resolution += "\nConfig update NOT successfull ! Test Case: FAIL"


print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)