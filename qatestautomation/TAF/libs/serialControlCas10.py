from os import device_encoding
from platform import java_ver
import serial
import time
from libs.config import config



class Debugport:     
        def __init__(self, com_port=config["DEBUG_PORT_COM_CAS"], baudrate=115200):
                
                self.connect()

        def connect(self, com_port=config["DEBUG_PORT_COM_CAS"], baudrate=115200):
                
                self.com_port = com_port
                self.baudrate = baudrate

                self.serial_port = serial.Serial(self.com_port, self.baudrate, timeout=20)
                print("COM connection status: {}".format(self.serial_port.isOpen()))
                print("Connected to {} at {}".format(self.serial_port.name, self.serial_port.baudrate))   

        def disconnect(self):
                self.serial_port.flush()
                self.serial_port.close()
                print("COM connection status: {}".format(self.serial_port.isOpen()))
                if not self.serial_port.isOpen():
                        print("Disconnected from {}".format(self.serial_port.name))
                else:
                        print("Connection to {} still open!".format(self.serial_port.name))

        def deleteLogFile(self, file_name):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$file,rm,/LOGS/{}".format(file_name))
                        print("File {} has been removed".format(file_name))
                else:
                        print(self.serial_port.name + " has not been opened")

        def breakStuff(self):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("LETSBREAKTHINGS")
                        print("Command for entering debug mode sent!")
                        time.sleep(1)
                else:
                        print(self.serial_port.name + " has not been opened")

        def backToBusiness(self):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$backtobusiness")
                        print("Command for exiting debug mode sent!")
                        time.sleep(1)
                else:
                        print(self.serial_port.name + " has not been opened")

        def writeDataToCom(self, cmd):
                if self.serial_port.is_open == True:
                        msg = cmd + "\r\n"
                        self.serial_port.reset_input_buffer()
                        self.serial_port.write(msg.encode("ascii"))
                        time.sleep(0.01)
                else:
                        print(self.serial_port.name + " has not been opened")
                
        def resetUnit(self):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$sys,reset")
                        print("Device has been reset")
                else:
                        print(self.serial_port.name + " has not been opened")

        def resetUnitwithRelay(self, rc1):
                rc1.turnOffRelay(config["POWER_SWITCH_RELAY"])
                time.sleep(3)
                rc1.turnOnRelay(config["POWER_SWITCH_RELAY"])

        def sysInfo(self):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$sys,info")
                        print("System info sent to the device")
                else:
                        print(self.serial_port.name + " has not been opened")

        def timeOutPS3(self, settimeout, max_retries=5):
                if self.serial_port.is_open == True:
                        
                        cmd = "$power,setps3timeout,{}".format(settimeout)

                        for i in range(max_retries):
                                
                                self.writeDataToCom(cmd)
                                print("Command for PS3 Timeout in {} ms sent".format(settimeout))
                                
                                if self.checkAcknowledgementFromLog(i, cmd, max_retries):
                                        break
                else:
                        print(self.serial_port.name + " has not been opened")

        def timeOutDP(self, settimeout, max_retries=5):
                if self.serial_port.is_open == True:
                        
                        cmd = "$power,setdptimeout,{}".format(settimeout)

                        for i in range(max_retries):
                        
                                self.writeDataToCom(cmd)
                                print("Command for DP Timeout in {} ms sent".format(settimeout))
                                
                                if self.checkAcknowledgementFromLog(i, cmd, max_retries):
                                        break
                else:
                        print(self.serial_port.name + " has not been opened")

        def checkAcknowledgementFromLog(self, i, keyword, max_retries):
        
                is_found = self.findDebugCommandAckLog(keyword)

                if is_found:
                        print("Command received and Confirmed!")
                        return True
                else:
                        print("No confirmation received! Command will be sent again if Max amount not reached!! Number of tries: {} out of {}".format(i+1, max_retries))
                        
                        if i+1 == max_retries:
                                print("Max Number of tries reached, CAS wont acknowledge Command")
                                return False                       
        
        def findDebugCommandAckLog(self, cmd):
                # line in log expected to be read is: e.g. "DBGPORT, INFO: $EGO,SETMOVEMODE,A" 
                splitline = cmd.split(",")
                LINE_ELEMENT_1 = splitline[0]
                LINE_ELEMENT_2 = splitline[1]
                ack_line = "DBGPORT, INFO: {},{},A".format(LINE_ELEMENT_1, LINE_ELEMENT_2)
                return self.findLineinDebugOutput(ack_line)

        def findLineinDebugOutput(self, ack_line, maxlinetoread=5):

                for i in range(maxlinetoread):                                              
                        
                        line_from_debug_output = self.readSingleLineFromSerial()
                        if ack_line.lower() in line_from_debug_output.lower():            
                                return True                                               
                return False
                
        def changeHeading(self, heading):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$ego,setheading,1,{}".format(heading))
                        print("Heading has been set to {}".format(heading))
                else:
                        print(self.serial_port.name + " has not been opened")

        def releaseHeading(self):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$ego,setheading,0,0")
                        print("Heading has been released!")
                else:
                        print(self.serial_port.name + " has not been opened")

        def setEgoState(self, lat, lon, elevation, speed, heading, moveMode, fwdGear, revGear, hAcc, headingMode):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$ego,setegostate,1,{},{},{},{},{},{},{},{},{},{}".format(lat, lon, elevation, speed, heading, moveMode, fwdGear, revGear, hAcc, headingMode))
                        print("Ego state has been set to {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(lat, lon, elevation, speed, heading, moveMode, fwdGear, revGear, hAcc, headingMode))
                else:
                        print(self.serial_port.name + " has not been opened")

        def changeLatitude(self, lat):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$ego,setlat,1,{}".format(lat))
                        print("Heading has been set to {}".format(lat))
                else:
                        print(self.serial_port.name + " has not been opened")

        def changeMovemode(self, movemode, max_retries=5):
                if self.serial_port.is_open == True:

                        if movemode == "forward":
                                movemodenumber = "2"
                        elif movemode == "reverse":
                                movemodenumber = "3"
                        elif movemode == "standstill":
                                movemodenumber = "4"
                        elif movemode == "parked":
                                movemodenumber = "5"

                        for i in range(max_retries):

                                        cmd = "$ego,setmovemode,1,{}".format(movemodenumber) 
                                        self.writeDataToCom(cmd)
                                        print("Following Movemode Command was sent: " + movemodenumber + " ({})".format(movemode))

                                        if self.checkAcknowledgementFromLog(i, cmd, max_retries):
                                                break
                else:
                        print(self.serial_port.name + " has not been opened")

        def sendDebugCommand(self, cmd, max_retries=5):

                if self.serial_port.is_open == True:

                        for i in range(max_retries):

                                self.writeDataToCom(cmd)
                                print("Following Command was sent: {}".format(cmd))

                                if self.findDebugCommandAckLog(cmd):
                                        print("Command received and Confirmed!")
                                        return True
                                else:
                                        print("No confirmation received! Command will be sent again if Max amount not reached!! Number of tries: {} out of {}".format(i+1, max_retries))

                                        if i+1 == max_retries:
                                                print("Max Number of tries reached, CAS wont acknowledge Command!")
                                                return False

        def changeSpeed(self, speed):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$ego,setspeed,1,{}".format(speed))
                        print("Heading has been set to {}".format(speed))
                else:
                        print(self.serial_port.name + " has not been opened")

        def readLinesFromSerial(self,file_name="Data1.txt", lines=20):   
                data_file = open(file_name,"a+")
                print(file_name +" opened")
                print("Reading data from " + self.serial_port.name)

                for i in range(0,lines):
                        # print("reading line {}".format(i+1))
                        data = self.serial_port.readline().decode(encoding="utf-8")
                        data_file.write(data)
                        
                data_file.close()
                print(file_name +" closed")

        def readSingleLineFromSerial(self):
                return self.serial_port.readline().decode("utf-8", errors='backslashreplace')

        def rotateHeading(self):
                heading = [*range(1, 361, 7)]

                self.releaseHeading(self.serial_port)
                time.sleep(3)
                while True:
                        for h in heading:
                                self.changeHeading(self.serial_port, h)
                                time.sleep(.2)

        def linearMovement(self):
                self.changeHeading(self.serial_port, 0)
                self.changeMovemode(self.serial_port, 2)
                
                step_m = 2
                step_t = .15
                speed = step_m/step_t
                self.changeSpeed(self.serial_port, speed)
                loops = 10
                meters = 100 * step_m
                step = 0.00001 * step_m
                lat = 47.1810742 - step*(int(meters/2))

                for l in range(loops):
                        for i in range(1, meters+1):
                                lat_mod = lat + step * i
                                self.changeLatitude(self.serial_port, lat_mod)
                                time.sleep(step_t)

                self.changeMovemode(self.serial_port, 4)
                self.changeSpeed(self.serial_port, 0)

        def initializeSerialComAndDebugmode(self, rc1, max_retries=5):

                rc1.turnOffGivenRelays(config["DEBUG_PORT_RELAY"])

                for i in range(max_retries):

                        self.breakStuff()
                        
                        if self.findLineinDebugOutput("DBGPORT, INFO: Debug port activated"):
                                print("Command received and Confirmed!")
                                break                                
                        else:
                                print("No confirmation received! Command will be sent again if Max amount not reached!! Number of tries: {} out of {}".format(i+1, max_retries))
                                self.backToBusiness()

                                if i+1 == max_retries:
                                        print("Max Number of tries reached, CAS wont acknowledge Command")
                    
        def finalizeSerialComAndDebugmode(self, rc1, max_retries=5):
                
                is_debugmode_closed = False

                for i in range(max_retries):

                        self.backToBusiness()

                        if self.findLineinDebugOutput("command received: backtobusiness"):
                                print("Command received and Confirmed!")
                                break                                
                        else:
                                print("No confirmation received! Command will be sent again if Max amount not reached!! Number of tries: {} out of {}".format(i+1, max_retries))
                                self.breakStuff()

                                if i+1 == max_retries:
                                        print("Max Number of tries reached, CAS wont acknowledge Command")

                rc1.turnOnGivenRelays(config["DEBUG_PORT_RELAY"])
                time.sleep(2)
                return is_debugmode_closed

        def ping(self, host):
                if self.serial_port.is_open == True:
                        self.writeDataToCom("$NETWORK,PING,{}".format(host))
                        print("Ping sent")
                else:
                        print(self.serial_port.name + " has not been opened")
        
        def pingcheck(self, maxlinetoread=20):

                ack_line = "10 packets transmitted"

                for i in range(maxlinetoread):
                        line = self.readSingleLineFromSerial()
                        print(line)

                        if ack_line in line:
                                print("found")
                                break


                # line = "10 packets transmitted,"

                # for i in range(maxlinetoread):
                        
                #         line_from_debug_output = self.readSingleLineFromSerial()
                #         print(line_from_debug_output)
                #         if line in line_from_debug_output():
                #                 return True
                # return False


if __name__ == "__main__":
        device_1 = Debugport(config["DEBUG_PORT_COM_CAS"], 115200)
        device_1.resetUnit()
        # device_1.breakStuff()
        # device_1.sysInfo()
        # device_1.readLinesFromSerial(lines=10)
        # device_1.backToBusiness()
        # device_1.disconnect()
