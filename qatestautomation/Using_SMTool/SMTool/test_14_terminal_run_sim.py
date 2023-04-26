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
        
    
    repo.send_command("$pflac,r,sim")
    time.sleep(2)
    print(ai.win_get_text(init.tool_title, 1024))
    if "$PFLAC,A,SIM,1" in ai.win_get_text(init.tool_title, 1024):
        repo.send_command("$sim,scen,6")
    else:
        print("Simulation is not activated !")

    time.sleep(2)
    




   

print("Saving results")   
repo.add_to_csv_file(init.log_file_path, resolution)
time.sleep(3)
print("Closing tool")
ai.win_close(init.tool_title)
time.sleep(1)
print("Closing program")
ai.win_close(init.title)