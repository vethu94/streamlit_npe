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

test_name = "\n\ntest#05_download_log_serial "
time_and_date = str(datetime.now())
resolution = test_name + time_and_date

#Start the program
repo.start_program(init.test_dir,init.test_prog,init.title)

#Start SMTool
repo.start_tool_in_program(init.title,init.tool,init.tool_title)
time.sleep(1)

#Search for desired tab in SMTool
if repo.search_tab_with_text("Download"):
    resolution += "\nTab: PASS"
else:
    resolution += "\nTab: FAIL"
time.sleep(1)

for active_com in init.active_com_list:
    #Set COM port
    repo.set_com_port(init.tool_title, active_com)
    resolution = resolution + "\nCOM" + str(active_com) + ": OK"

   


    #Set download direstory 
    ai.control_set_text(init.tool_title, init.download_dir_box ,init.download_path)

    #Click download to PC button
    ai.control_click(init.tool_title, init.download_to_PC_button)

    #Wait for active download window
    ai.win.win_wait_active(init.download_title)

    #Select file to download. Chosen file is random. It is not possible to select desirend file.
    repo.select_file_to_download(init.download_title)

    #Click download button
    ai.control_click(init.download_title, init.download_button)

    #Wait for active Progress window
    ai.win_wait_active(init.popup_title)

    if repo.wait_while_not_in_text("Do you want to overide", init.popup_title, init.timeout_short):
        print("Overriding log file")
        ai.control_click(init.popup_title, init.ok_button)

    if repo.wait_while_not_in_text("Successfully downloaded", init.popup_title, init.timeout_vlong):
        print("Log file download was successfull !")
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "\nLog file download was successfull ! Test Case: PASS"
    else:
        print("Log file download was NOT successfull ! Timeout!")
        ai.control_click(init.popup_title, init.ok_button)
        resolution += "\nLog file download was NOT successfull ! Test Case: FAIL"



print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)