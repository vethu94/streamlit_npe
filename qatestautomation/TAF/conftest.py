from libs.config import get_config
from libs.networkManager.NetworkManager import WiFiManager
# from libs.networkManager.NetworkManager import NetworkManager
from libs.mansonControl import mansonPowerSupply
import pytest
from libs.ssh import Ssh
from libs.toolbox.config_register.ConfigRegister import ConfigRegister
from libs.serialControlCas10 import Debugport
from libs.relayControl import relayControl
import subprocess
import re

#from libs.config import config

def pytest_addoption(parser):
    parser.addoption("--user", action="store", default="hxm")
    parser.addoption("--ip", action="store", default="10.62.70.102")
    parser.addoption("--key", action="store",
                     default=r"C:\Users\lmate\.ssh\id_rsa")
    parser.addoption("--debug_port_com_cas", action="store")
    parser.addoption("--search_keyword", action="store")


@pytest.fixture
def host(request):
    return request.config.getoption("--ip")


@pytest.fixture
def user(request):
    return request.config.getoption("--user")


@pytest.fixture
def key(request):
    return request.config.getoption("--key")


@pytest.fixture
def minion_server(host, user, key):
    return Ssh(host, user, None, key)


@pytest.fixture
def config_register():
    return ConfigRegister()


@pytest.fixture
def wifi_manager():
    return WiFiManager()


# @pytest.fixture
# def network_manager():
#     return NetworkManager()


@pytest.fixture
def config():
    return get_config()


@pytest.fixture                                  
def debug_port_com_cas(request):
    return request.config.getoption("--debug_port_com_cas")


@pytest.fixture(scope = "session")                                     
def debug_port():
    return Debugport()


@pytest.fixture                                  
def search_keyword(request):
    return request.config.getoption("--search_keyword")


@pytest.fixture                                     
def keyword(search_keyword):
    ky = search_keyword
    return ky


@pytest.fixture(scope = "session")
def relay_control():
    return relayControl()


@pytest.hookimpl()
def pytest_sessionfinish():
    print("session finish test")

    fwversion = ""
    nwsubversion = ""

    infoTxtFile = open("..//cassysteminfo.txt", "r")
    data = infoTxtFile.read()

    if "fw" in data:
        fwversionlist = re.findall(r"fw: ([\d.]*\d+)", data)

    for element in fwversionlist:
        fwversion += element

    if "nwsub" in data:
        nwsubversionlist = re.findall(r"nwsub: ([\d.]*\d+)", data)

    for element in nwsubversionlist:
        nwsubversion += element

    item = subprocess.Popen(["..\\tests\\testrail_config.bat", str(fwversion), str(nwsubversion)], 
            shell=True, stdout=subprocess.PIPE)
    for line in item.stdout:
        print(line)
  
