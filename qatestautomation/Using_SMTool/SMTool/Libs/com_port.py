import autoit as ai
import time
import serial.tools.list_ports_windows
import config_param.config_param_gen as init


def select_port(comport):
    '''
    Checks that given comport is active
    COM is a list of COM ports used in test
    The order of the COM ports in the list should be from the lowest to the highest, starting from at COM[0]
    If COM is in active list, then returned status will be OK
    '''
    status = ""
    comportno = int(comport.strip("COM"))
    COM = serial.tools.list_ports_windows.comports()
    for i in range(len(COM)):
        COM[i] = int(COM[i].device[3:])
    COM.sort()
    ai.win_activate(init.title)
    ai.win_activate(init.tool_title)
    control = "[NAME:statusBar]"
    tool_pos = ai.win_get_pos(init.tool_title)
    control_pos = ai.control_get_pos(init.tool_title, control)
    #offset = -42
    for i in range(len(COM)):
        if comportno == COM[i]:
            ai.mouse_click(x = tool_pos[0] + control_pos[0] + 30,
                           y = tool_pos[1] + control_pos[1] + 40) # 954,845
            time.sleep(3)
            for j in range(0,i+2):
                ai.send("^{DOWN}")
            ai.send("{ENTER}")
            #text1 = ai.control_get_text(init.tool_title, control)
            #ai.mouse_click(x = tool_pos[0] + control_pos[0] + 30,
            #               y = tool_pos[1] + control_pos[1] + 20 + (len(COM)-3) * offset + 10)
            #                   #((len(COM)) - i) * offset) # 954, 805-* = 693
            status = "OK"
        else:
            status = "NOK"
    return status


def send_command(command):
    tool_pos = ai.win_get_pos(init.tool_title)
    control_pos = ai.control_get_pos(init.tool_title, "[CLASS:Edit; INSTANCE:1]")
    ai.control.control_set_text(init.tool_title, "[CLASS:Edit; INSTANCE:1]", command)
    time.sleep(1)
    ai.mouse_click(x = tool_pos[0] + 103, y = tool_pos[1] + 105)
    time.sleep(2)
    ai.send("{ENTER}")