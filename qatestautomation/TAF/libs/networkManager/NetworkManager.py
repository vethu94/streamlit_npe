import os
import time
from subprocess import Popen, PIPE


class NetworkManager():
    def __init__(self) -> None:
        self.wifi = WiFiManager()

    @staticmethod
    def get_ip_by_mac(mac):
        pid = Popen(["arp", "-a"], stdout=PIPE)
        output = pid.communicate()[0].decode('utf-8')
        # Expected output from arp command:
        # Interface: 192.168.0.192 --- 0xa
        # Internet Address      Physical Address      Type
        # 192.168.0.1           90-5c-44-24-b7-1b     dynamic
        # 192.168.0.255         ff-ff-ff-ff-ff-ff     static
        # ...
        for line in output.splitlines():
            if mac in line.lower():
                print("Found " + line)
                ip = line.strip().split()[0]
                return ip
        return None


class WiFiManager():
    @staticmethod
    def create_network_profile(ssid, password, connection_mode="manual"):
        """
        Args:
            connection_mode (str, optional): Either manual or auto. Defaults to "manual".
        """

        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>"""+ssid+"""</name>
        <SSIDConfig>
            <SSID>
                <name>"""+ssid+"""</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>"""+connection_mode+"""</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>"""+password+"""</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        command = "netsh wlan add profile filename=\""+ssid+".xml\""+" interface=Wi-Fi"
        with open(ssid+".xml", 'w') as file:
            file.write(config)
        WiFiManager._execute(command)
        os.remove(ssid+".xml")

    @staticmethod
    def connect(ssid, password=None, timeout=10):
        if password:
            if not WiFiManager.is_already_known(ssid):
                WiFiManager.create_network_profile(ssid, password)
        command = "netsh wlan connect name=\""+ssid+"\" ssid=\""+ssid+"\" interface=Wi-Fi"
        WiFiManager._execute(command)
        for _ in range(timeout):
            if WiFiManager.is_connected(ssid):
                break
            time.sleep(1)
        else:
            raise TimeoutError(f"Could not connect to {ssid} within {timeout} sec")

    @staticmethod
    def disconnect():
        command = f"netsh wlan disconnect"
        WiFiManager._execute(command)

    @staticmethod
    def display_available_networks():
        command = "netsh wlan show networks interface=Wi-Fi"
        output, errors, _ = WiFiManager._execute(command)
        if errors:
            print(f"ERROR when running displayAvailableNetworks: {errors}")
        else:
            print(output.decode())

    @staticmethod
    def is_already_known(ssid):
        """Check if a profile for a given ssid is already known. 
        """
        command = f"netsh wlan show profile {ssid}"
        _, _, return_code = WiFiManager._execute(command)

        return True if not return_code else False

    @staticmethod
    def is_connected(ssid):
        command = f"netsh wlan show interfaces"
        output, errors, _ = WiFiManager._execute(command)
        if errors:
            print(f"ERROR when running {command}: {errors}")
        else:
            ssid_line = [x for x in output.decode().split("\n") if 'SSID' in x and 'BSSID' not in x]
            # expected ssid_line similar to: "['    SSID                   : MF283V-BBB301\r']"
            if ssid_line and ssid == ssid_line[0].split()[-1].strip():
                return True
        return False

    @staticmethod
    def _execute(command):
        p = Popen(command, shell=True, stderr=PIPE, stdout=PIPE)
        output, errors = p.communicate()
        return output, errors, p.returncode


if __name__ == "__main__":
    ssid = "CHANGE ME"
    nm = NetworkManager()

    print(f"IS CONNECTED {nm.wifi.is_connected(ssid)}")
    nm.wifi.connect(ssid)
    print(f"IS CONNECTED {nm.wifi.is_connected(ssid)}")
    time.sleep(5)
    nm.wifi.disconnect()
    print(f"IS CONNECTED {nm.wifi.is_connected(ssid)}")

    # wifi_manager.create_network_profile("test", "test123456", "auto")
