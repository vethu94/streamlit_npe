"""
This script uploads a config file to a CAS unit.
DUT: SMTool

COM port has to preset in SMTool

"""

import autoit as ai
import time
import os
import datetime
import repo
import smtool_init as init 
from datetime import datetime

test_name = "\n\nTest#01_upload_fw "
time_and_date = str(datetime.now())
resolution = test_name + time_and_date


#Start the Toolbox program
repo.start_program(init.test_dir, init.test_prog, init.title)

#Start SMTool
repo.start_tool_in_program(init.title,init.tool, init.tool_title)

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

    #disable all option
    repo.disable_all_config_options(init.tool_title)


    #start of upload
    #check the desired option
    if int(ai.control_command(init.tool_title, init.control_file_box["fw"], "IsEnabled")):
        print("Option already checked!")
    else:
        ai.control_click(init.tool_title, init.control_check_box["fw"])
        time.sleep(1)

    #enter path to fw file
    #ai.control_set_text(init.tool_title, init.control_file_box["fw"], init.fw_path)
    repo.paste_cas_fw_path(init.fw_path)
    time.sleep(6)
        
    if ai.win_exists("Not supported version exception"):
        ai.control_click("Not supported version exception", "[CLASS:Button; INSTANCE:1]")
        resolution += "\nDevice NOT supported for this FW version ! Test case: FAIL"
        print("Device NOT supported be this FW version !")
       
    else: 



        #check the desired option
        print(ai.control_command(init.tool_title, init.control_check_box["conf"], "IsChecked"))
        if int(ai.control_command(init.tool_title, init.control_check_box["conf"], "IsChecked")):
            print("Option already checked - checkbox!")
        else:
            ai.control_click(init.tool_title, init.control_check_box["conf"])
            time.sleep(1)

        if int(ai.control_command(init.tool_title, init.control_file_point, "IsChecked")):
            print("Option already checked - radio!")
        else:
            ai.control_click(init.tool_title, init.control_file_point)
            time.sleep(1)

        
            
        ai.control_set_text(init.tool_title, init.control_file_box["conf"], init.config_path)
        time.sleep(1)




        #upload the file(s)
        ai.control_click(init.tool_title, init.upload_button)
        resolution = resolution + "\nUploading FW: " + str(init.fw_path)
        time.sleep(1)



        ai.win_wait_active(init.popup_title, timeout=5)
        time.sleep(1)

        if init.upload_config:
            if repo.wait_while_not_in_text("Warning", init.popup_title, init.timeout_short):
                print("OK")
                ai.control_click(init.popup_title, init.ok_button)
                time.sleep(1)


        
        if repo.wait_while_not_in_text("Warning", init.popup_title, init.timeout_short):
            print("FW version downgrade !")
            ai.control_click(init.popup_title, init.ok_button)
            resolution += "\nFW version downgrade !"
        elif repo.wait_while_not_in_text("Not enough space", init.popup_title, init.timeout_short):
            print("Not enough space on Device !")
            ai.control_click(init.popup_title, init.ok_button)
            resolution += "Not enough space on Device ! Test Case: FAIL"
        
        
        if repo.wait_while_not_in_text("already installed", init.popup_title, init.timeout_short):
            resolution += "\nFW version already installed !"
            print("FW version already installed !")
            ai.control_click(init.popup_title, init.ok_button)
            resolution += "FW version already installed !"
        elif repo.wait_while_not_in_text("Successfull installation", init.popup_title, init.timeout_vlong):
            print("FW installation was successfull !")
            time.sleep(1)
            ai.control_click(init.popup_title, init.ok_button)
            resolution += "\nFW installation was successfull ! Test Case: PASS"
        elif repo.wait_while_not_in_text("Installation failed", init.popup_title, init.timeout_vlong):
            print("FW installation was NOT successfull !")
            time.sleep(1)
            ai.control_click(init.popup_title, init.ok_button)
            resolution += "\nFW installation was NOT successfull ! FW version does not mach ! Test Case: FAIL"
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
