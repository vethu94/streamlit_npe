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

test_name = "\n\ntest#06_download_log_SMData "
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

#for active_com in init.active_com_list:
for i in range(5):
    '''
    #Set COM port
    repo.set_com_port(init.tool_title, active_com)
    resolution = resolution + "\nCOM" + str(active_com) + ": OK"
    
    '''

    #Set download direstory 
    ai.control_set_text(init.tool_title, init.download_dir_box_smdata ,init.download_path)
    time.sleep(1)

    #Refresh SMData log file list
    ai.control_click(init.tool_title, "[NAME:buttonRefresh]")
    
    #Select file to download. Chosen file is random. It is not possible to select desirend file.
    time.sleep(2)
    repo.select_file_to_download_smdata(init.tool_title)
    
    if int(ai.control_command(init.tool_title, init.download_button_smdata, "IsEnabled")):
        time.sleep(1)
        ai.control_click(init.tool_title, init.download_button_smdata)
        print("Downloading log file !")
    else:
        print("Download not enabled or file not chosen ! Choosing again !")
        repo.select_file_to_download_smdata(init.tool_title)

    #Wait for active Progress window
    ai.win_wait_active(init.download_title_smdata)

    if repo.wait_while_not_in_text("already exists", init.download_title_smdata, init.timeout_vshort):
        print("Overriding log file")
        resolution += "\nOverriding log file"
        time.sleep(1)
        ai.control_click(init.download_title_smdata, "[CLASS:Button; INSTANCE:1]")

    if repo.wait_while_not_in_text("Downloaded", init.download_title_smdata, init.timeout_vlong):
        print("Log file download was successfull !")
        time.sleep(1)
        ai.control_click(init.download_title_smdata, "[CLASS:Button; INSTANCE:1]")
        resolution += "\nLog file download was successfull ! Test Case: PASS"
    else:
        print("Log file download was NOT successfull ! Timeout!")
        resolution += "\nLog file download was NOT successfull ! Test Case: FAIL"

    
print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)