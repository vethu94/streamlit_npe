from tkinter import E
from libs.mansonControl import mansonPowerSupply
from libs.serialControlCas10 import Debugport

import time


# Normal P = 3.7179 W (no QD1400 connected)
# DP P = 0.572 W (no QD1400 connected)
# ratio ~6.5


def test_battery_low_DP(config, debug_port, relay_control):
    device = mansonPowerSupply(config["DEBUG_PORT_COM_PS"]) 
    rc1 = relay_control
    
    debug_port.changeMovemode(5)

    device.connectToDevice()
    device.setOutputVoltage(14)

    debug_port.initializeSerialCom(rc1)
    debug_port.timeOut()
    debug_port.finalizeSerialCom(rc1)

    medium_voltage_threshold = 9     # voltage threshold to set on the power supply
    # voltage diff between power supply and MFA measurement
    offset = 0.2
    # it is common to get a false reading at the first time
    v1 = device.readOutputVoltage()
    v1 = device.readOutputVoltage()     # that's why it's done twice
    c1 = device.readOutputCurrent()
    p1 = v1 * c1                        # power consumption calculation before going to DP
    device.setOutputVoltage(medium_voltage_threshold + offset)
    time.sleep(40)
    v2 = device.readOutputVoltage()
    c2 = device.readOutputCurrent()
    p2 = v2 * c2                        # power consumption calculation while in DP
    device.disconnectFromDevice()
    assert p1/p2 > 6


def test_12V_ps_normal(config, debug_port):
    device = mansonPowerSupply(config["DEBUG_PORT_COM_PS"]) 
    
    
    debug_port.changeMovemode(5)
    
    medium_voltage_threshold = 13.7     # voltage threshold to set on the power supply
    # voltage diff between power supply and MFA measurement
    offset = 0.2
    device.connectToDevice()
    v = device.readOutputVoltage()
    c = device.readOutputCurrent()
    p1 = v * c                          # power consumption calculation while in DP
    device.setOutputVoltage(medium_voltage_threshold + offset)
    time.sleep(40)
    v = device.readOutputVoltage()
    c = device.readOutputCurrent()
    p2 = v * c                          # power consumption calculation when back to normal
    device.disconnectFromDevice()
    assert p2/p1 > 6
