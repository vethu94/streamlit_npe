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

command = "$wifi,reset"
number_of_resets = 50   #total number of resets 
reset_freq = 60  #time between reserts in s 

#Start the program
repo.start_program(init.test_dir,init.test_prog,init.title)

#Start SMTool
repo.start_tool_in_program(init.title,init.tool,init.tool_title)
time.sleep(1)

#Search for desired tab in SMTool
if repo.search_tab_with_text("Terminal"):
    resolution += "\nTab: PASS"
else:
    resolution += "\nTab: FAIL"
time.sleep(1)

for active_com in init.active_com_list:
    #Set COM port
    repo.set_com_port(init.tool_title, active_com)
    resolution = resolution + "\nCOM" + str(active_com) + ": OK"
    time.sleep(5)

    if ("Disconnect" in ai.win_get_text(init.tool_title, 1024)):
        print("Device connected to the terminal!")

    else: 
        ai.control_click(init.tool_title, "[NAME:connectionButton]")
        print("Device not connected to the terminal! Connecting... ")
        
    if "Start recording to File" in ai.win_get_text(init.tool_title, 1024):
        ai.control_click(init.tool_title, "[NAME:recordButton]")
        print("Logging terminal output to file...")
    else:
        print("Logging to file already started !")

    time.sleep(2)
    repo.send_command("$debug_out,RS232-0,net,all")
    time.sleep(2)
       
    resolution += "\nNumber of wifi module resets: "
    resolution += str(number_of_resets)
  
    for res in range(number_of_resets):
        repo.send_command(command)
        time.sleep(reset_freq)
        if res == number_of_resets:
            resolution += "\nTest case: PASS"

    time.sleep(2)            
    ai.control_click(init.tool_title, "[NAME:recordButton]")              
    time.sleep(2)
    




   

print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)