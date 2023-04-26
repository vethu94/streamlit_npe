import autoit as ai
import smtool_init as init
import time
import os
from datetime import datetime
import repo
#import smtool_init as init 
from smtool_init import *
import colored
from colored import stylize

#Start the Toolbox program
repo.start_program(init.test_dir, init.test_prog, init.title)

#Start SMTool
repo.start_tool_in_program(init.title,init.tool, init.tool_title)
time.sleep(7)

print(ai.win_exists("Not supported version exception"))

if ai.win_exists("Not supported version exception"):
    ai.control_click("Not supported version exception", "[CLASS:Button; INSTANCE:1]")
   



