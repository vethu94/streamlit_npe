import autoit as ai
import os
import time
import serial.tools.list_ports_windows
from datetime import datetime
import csv
import random
# import Using_SMTool.SMTool.smtool_init as init



def add_to_csv_file(csv_file_path, data):
    csv_file = open(os.path.join(csv_file_path, "CAS_Automation_Test.txt"), "a+")
    csv_file.write(data + "\n")
    csv_file.close()

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
    if int(ai.control_command(title, "[NAME:confFileBox]", "IsEnabled")) or int(
            ai.control_command(title, "[NAME:vehSearch]", "IsEnabled")):
        ai.control_click(title, "[NAME:confCheckBox]")
        print("Config disabled!")


def store_device_info(comport, csv_file_path, data):
    """
    Creates txt file with COM port device information
    :param comport:
    :param csv_file_path:
    :param data:
    :return:
    """
    file = open(os.path.join(csv_file_path, "Device_Info_%s.txt") % comport, "w+")
    file.write(data + "\n")
    file.close()