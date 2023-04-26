import autoit as ai
import os
import time
import serial.tools.list_ports_windows
from datetime import datetime
import csv
import random
import smtool_init as init


def start_program(prog_directory, prog_name, title=""):
    path = prog_directory + prog_name
    ai.run(path)
    time.sleep(4)
    if ai.win_exists(title):
        print(prog_name +" has started!")
    if not(8 & ai.win_get_state(title)):
        print("Program window not active. Activating!")
        ai.win_activate(title)
    ai.win_wait_active(title) #wait until window with given title become active 
    
def start_tool_in_program(program_name, tool_name, tool_title, many_inst = 0 ):
    #Start SMTool
    if not(many_inst):
        if ai.win_exists(tool_title):
            ai.win_activate(tool_title)
            ai.win_close(tool_title)
    ai.control_click(program_name,tool_name)
    ai.win_wait_active(tool_title)
    

def search_tab_with_text(searched_tab,sleep=2, timeout = 30):
    print("Searching for tab with "+searched_tab)
    time_colapse = 0
    for i in range(12): 
        time.sleep(sleep)
        time_colapse += sleep
        windows_text = ai.win_get_text("[ACTIVE]")  

        if searched_tab in windows_text:
            print("Found it!")
            return 1
        elif time_colapse == timeout:
            print("Text find timeout !")
            return 0
        else:
            ai.send("^{TAB}")
            print("Not yet...")  

def go_to_tab(tab_number,sleep=1):
    time.sleep(sleep)
    ai.send("^"+str(tab_number))
    print("Switching tab!")

def wait_while_not_in_text(expected_expr, title, timeout=10):
    timer = 0
    while expected_expr not in ai.win_get_text(title, 1024):
        #print(ai.win_get_text(title, 1024))
        time.sleep(1)
        if timer == timeout:
            print("Timeout!")
            return 0
            
        #print(timer)    
        timer += 1
    return 1

def set_com_port(title, active_com):
    '''
    COM is a list of COM ports unsed in test
    The order of the COM ports in the list should be from the lowest to the highest, starting from at COM[0] 
    '''
    
    COM = serial.tools.list_ports_windows.comports()
    #print(len(COM))
    for i in range(len(COM)):
        COM[i] = int(COM[i].device[3:])
    COM.sort()  

    control = "[NAME:statusBar]"
    tool_pos = ai.win_get_pos(title)
    control_pos = ai.control_get_pos(title, control)
    offset = -22
    #print(tool_pos)
    #print(control_pos)

    for i in range(len(COM)):
        if active_com == COM[i]:  
            ai.mouse_click(x = tool_pos[0] + control_pos[0] + 30, y = tool_pos[1] + control_pos[1] + 40)
            time.sleep(3)
            ai.mouse_click(x = tool_pos[0] + control_pos[0] + 30, y = tool_pos[1] + control_pos[1] + 20 + (len(COM)-i-1)*offset)
            print("COM"+str(COM[i])+" available and selected!")        

    
def disable_all_config_options(title):
    if int(ai.control_command(title, "[NAME:fwFileBox]", "IsEnabled")):
        ai.control_click(title, "[NAME:fwCheckBox]")
        print("Firmware disabled!")
    if int(ai.control_command(title, "[NAME:obstFileBox]", "IsEnabled")):
        ai.control_click(title, "[NAME:obstCheckBox]")
        print("Obstacle disabled!")
    if int(ai.control_command(title, "[NAME:voiceFileBox]", "IsEnabled")):
        ai.control_click(title, "[NAME:voiceCheckBox]")
        print("Voice disabled!")
    if int(ai.control_command(title, "[NAME:masterFileBox]", "IsEnabled")):
        ai.control_click(title, "[NAME:masterCheckBox]")
        print("Master file disabled!")
    if int(ai.control_command(title, "[NAME:fwSyncFileBox]", "IsEnabled")):
        ai.control_click(title, "[NAME:fwSyncCheckBox]")
        print("Sync Firmware disabled!")
    if int(ai.control_command(title, "[NAME:confFileBox]", "IsEnabled")) or int(ai.control_command(title, "[NAME:vehSearch]", "IsEnabled")):
        ai.control_click(title, "[NAME:confCheckBox]")
        print("Config disabled!")

def add_to_csv_file(csv_file_path, data):
    csv_file = open(os.path.join(csv_file_path, "CAS_Automation_Test.txt"), "a+")
    csv_file.write(data + "\n")
    #csv_file = open(os.path.join(csv_file_path, "CAS_{}_{}.csv".format(test_name, datetime.now())), "wt", newline=' ')
    #csv_writer = csv.writer(csv_file, delimiter=' ')
    #csv_writer.writerow(data)
    
    csv_file.close()

def store_device_info(csv_file_path, data):
    file = open(os.path.join(csv_file_path, "Device_Info.txt"), "w+")
    file.write(data + "\n")
    #csv_file = open(os.path.join(csv_file_path, "CAS_{}_{}.csv".format(test_name, datetime.now())), "wt", newline=' ')
    #csv_writer = csv.writer(csv_file, delimiter=' ')
    #csv_writer.writerow(data)
    
    file.close()

def select_file_to_download(win_title):
    win_pos = ai.win_get_pos(win_title)
    ai.mouse_click(x = win_pos[0] + 40, y = win_pos[1] + 220)

def select_file_to_download_smdata(win_title):

    win_pos = ai.win_get_pos(win_title)
    random_num = random.randint(-50, 50)
    print(random_num)
    ai.mouse_click(x = win_pos[0] + 60, y = win_pos[1] + 350 + 2*random_num) 

def paste_cas_fw_path(path):
    ai.control_click("SMTool Support Mateusz Lerch","[NAME:fwBrowseButton]") 
    ai.win_wait_active("Open")
    time.sleep(1)
    ai.control_set_text("Open","[CLASS:Edit; INSTANCE:1]", path)
    time.sleep(1)
    ai.control_click("Open", "[CLASS:Button; INSTANCE:1]")

def send_command(command):
    tool_pos = ai.win_get_pos(init.tool_title)
    control_pos = ai.control_get_pos(init.tool_title, "[CLASS:Edit; INSTANCE:1]")

    ai.control.control_set_text(init.tool_title, "[CLASS:Edit; INSTANCE:1]", command)
    time.sleep(1)

    ai.mouse_click(x = tool_pos[0] + 103, y = tool_pos[1] + 105)
    time.sleep(2)
    ai.send("{ENTER}")