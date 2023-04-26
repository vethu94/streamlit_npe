from telnetlib import COM_PORT_OPTION
from libs import mansonlib
from libs.config import config
import time



class mansonPowerSupply:
    def __init__(self, com_port):
        self.com_port = com_port  # COM port needs to be a string, e.g. "COM8"
        self.hcs = mansonlib.HCS()

    def connectToDevice(self):
        print("Device connected: " + str(self.hcs.OpenPort(self.com_port)))
        time.sleep(2)

    def disconnectFromDevice(self):
        print("Device disconnected: " + str(self.hcs.Close()))

    def getModel(self):
        print("Power supply model: {}".format(self.hcs.GetModel()))
    
    def getPreset(self, index, option):
        # Options: "V", "C" or "A" 
        # Index: 0 - 2
        print("Power supply preset: {}".format(self.hcs.GetPreset(index, option)))

    def getOutputSettings(self, option):
        # Options: "V", "C" or "A" 
        print("Power supply output settings: {}".format(self.hcs.GetOutputSetting(option)))

    def setOutputVoltage(self, voltage):
        print("Setting output voltage: " + str(voltage) + "V")
        self.hcs.SetOutputVoltage(voltage)
        time.sleep(2)
    
    def readOutputCurrent(self):
        c1 = self.hcs.GetOutputCurrent()
        print("Actual output current = {} A".format(c1))
        return c1

    def readOutputVoltage(self):
        v1 = self.hcs.GetOutputVoltage()
        print("Actual output voltage = {} V".format(v1))
        return v1


    def resetOutput(self, timeout=5):
        self.hcs.OutOff()
        time.sleep(timeout)
        self.hcs.OutOn()
        print("Output reseted")

    def outputOff(self):
        self.hcs.OutputOff()
        print("Output turned OFF")
        time.sleep(2)

    def outputOn(self):
        self.hcs.OutputOn()
        print("Output turned ON")
        time.sleep(2)

    def readPowerConsumption(self, power_supply):
        v = power_supply.readOutputVoltage()
        c = power_supply.readOutputCurrent()
        p = v * c
        return p
        
if __name__ == "__main__":
    mps = mansonPowerSupply(config["DEBUG_PORT_COM_PS"])
    mps.connectToDevice()
    mps.getModel()
    mps.getOutputSettings("V")
    mps.getOutputSettings("C")
    mps.getOutputSettings("A")
    mps.getPreset(0, "V")
    mps.disconnectFromDevice()
    
