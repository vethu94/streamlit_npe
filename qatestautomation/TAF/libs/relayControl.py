import libs.relay_ft245r
import time


class relayControl:
    def __init__(self, dev_index=0):
        """Choose device index from the list. By default, the first one is taken."""

        self.rb = libs.relay_ft245r.FT245R()
        self.dev_list = self.rb.list_dev()
        if len(self.dev_list) == 0:
            print("Not FT245 devices found!")
        else:
            print("Device list: ")
            for dev in self.dev_list:
                print(dev.serial_number)
            self.dev = self.dev_list[dev_index]
            self.rb.connect(self.dev)
            print("Using device with serial number " + self.dev.serial_number)

    def disconnentFromDevice(self):
        self.rb.disconnect()
        print("Disconnected from device " + self.dev.serial_number)

    def checkAllRelaysStatus(self):
        relay_status = []
        for relay_id in range(self.rb.RELAY_MAX):
            relay_num = relay_id + 1
            relay_status.append(self.rb.getstatus(relay_num))
            print("=============================")
            print("Relay {} status: {}".format(
                relay_num, relay_status[relay_id]))
        print("\n")
        return relay_status

    def checkRelayStatus(self, relay):
        relay_status = self.rb.getstatus(relay)
        print("Relay {} status: {}".format(relay, relay_status))
        return relay_status

    def turnOnRelay(self, relay):
        print("Turning ON relay {}".format(relay))
        self.rb.switchon(relay)
        time.sleep(.5)
        print("Realy {} status: {}".format(relay, self.rb.getstatus(relay)))

    def turnOffRelay(self, relay):
        print("Turning OFF relay {}".format(relay))
        self.rb.switchoff(relay)
        time.sleep(.5)
        print("Realy {} status: {}".format(relay, self.rb.getstatus(relay)))

    def resetRelay(self, relay, delay=1):
        """(relay_number, delay)"""
        print("Reseting relay {}".format(relay))
        self.turnOffRelay(relay)
        time.sleep(delay)
        self.turnOnRelay(relay)

    def turnOnAllRelays(self):
        print("Turning ON all relays")
        self.rb.relay_state = 0xFF
        self.rb.setstate()
        time.sleep(.5)

    def turnOffAllRelays(self):
        print("Turning ON all relays")
        self.rb.relay_state = 0x00
        self.rb.setstate()
        time.sleep(.5)

    def turnOffGivenRelays(self, relayList):
        print("Turning OFF relays: {}".format(relayList))
        currentRelayStatus = self.rb._getstatus_byte()
        relaysToBeTurnOff = 0
        for el in relayList:
            if el < 1 or el > 8:
                print("Wrong relay number: {}".format(el))
                print("Relay number range: 1 - 8")
                break
            relaysToBeTurnOff |= 1 << el-1
        self.rb.relay_state = currentRelayStatus & ~(relaysToBeTurnOff)
        self.rb.setstate()

    def turnOnGivenRelays(self, relayList):
        print("Turning ON relays: {}".format(relayList))
        currentRelayStatus = self.rb._getstatus_byte()
        relaysToBeTurnOn = 0
        for el in relayList:
            if el < 1 or el > 8:
                print("Wrong relay number: {}".format(el))
                print("Relay number range: 1 - 8")
                break
            relaysToBeTurnOn |= 1 << el-1
        self.rb.relay_state = currentRelayStatus | relaysToBeTurnOn
        self.rb.setstate()

    def resetRelayLong(self, relay, delay=5):
        """(relay_number, delay)"""
        print("Resting relay {}".format(relay))
        self.turnOffRelay(relay)
        time.sleep(delay)
        self.turnOnRelay(relay)

if __name__ == "__main__":
    rb1 = relayControl()
    r = [1, 2, 3, 4, 7, 8]
  #  rb1.resetRelay(6)
   # rb1.turnOnRelay(5)
   # rb1.turnOnRelay(6)
    rb1.turnOnRelay(8)
    rb1.checkAllRelaysStatus()
