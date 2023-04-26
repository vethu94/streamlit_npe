import autoit as ai
import os
import time
import serial.tools.list_ports_windows
from datetime import datetime
import csv
import random
import config_param.config_param_gen as init


def start_toolbox():
    "This function Starts the HxGN Mine Protect Toolbox window"
    path = init.test_dir + init.test_prog
    ai.run(path)
    time.sleep(4)
    if ai.win_exists(init.title):
        print(init.test_prog + " has started!")
    if not (8 & ai.win_get_state(init.title)):
        print("Program window not active. Activating!")
        ai.win_activate(init.title)
    ai.win_wait_active(init.title)  # wait until window with given title become active


def start_smtool(many_inst=0):
    "This function opens the SMTool"
    if not (many_inst):
        if ai.win_exists(init.tool_title):
            print("in here")
            ai.win_activate(init.tool_title)
            print("activated tool_title")
            ai.win_close(init.tool_title)
            print("closed active tool title")
    ai.control_click(init.title, init.tool)
    print("trying to click on control")
    ai.win_wait_active(init.tool_title)


def stop_toolbox():
    " This function Stops the HxGN Mine Protect Toolbox window"
    path = init.test_dir + init.test_prog
    ai.run(path)
    time.sleep(4)
    if ai.win_exists(init.title):
        ai.win_close(init.title)
        print(init.test_prog + " has closed!")
    #if not (8 & ai.win_get_state(init.title)):
    #    print("Program window not active. Activating!")
    #    ai.win_activate(init.title)
    #    ai.win_close(init.title)
    #ai.win_wait_active(init.title)  # wait until window with given title become active


def stop_smtool(many_inst=0):
    " This function Stops the SMTool window"
    # Stop SMTool
    if not (many_inst):
        if ai.win_exists(init.tool_title):
            ai.win_activate(init.tool_title)
            ai.win_close(init.tool_title)
    #else:
    #    ai.control_click(init.title, init.tool)
    #    ai.win_close(init.tool_title)


def search_tab_with_text(searched_tab, sleep=2, timeout=30):
    print("Searching for tab with " + searched_tab)
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


def go_to_tab(tab_number, sleep=1):
    time.sleep(sleep)
    ai.send("^" + str(tab_number))
    print("Switching tab!")


def wait_while_not_in_text(expected_expr, title, timeout=10):
    timer = 0
    while expected_expr not in ai.win_get_text(title, 1024):
        # print(ai.win_get_text(title, 1024))
        time.sleep(1)
        if timer == timeout:
            print("Timeout!")
            return 0

        # print(timer)
        timer += 1
    return 1

