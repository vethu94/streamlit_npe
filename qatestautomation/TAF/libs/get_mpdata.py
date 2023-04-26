import json
import requests
from requests.api import request
from requests.auth import HTTPBasicAuth
import urllib.parse
from casMPDataApiRequests import *

class restAPI(MPDataAPIRequests):
    def __init__(self, root_url="http://10.62.70.102/v2/", serial_CAS="all", serial_CAS10="all"):
        super().__init__(root_url, serial_CAS, serial_CAS10)
        # Setup variables 
        self.serial_CAS = serial_CAS
        self.serial_CAS10 = serial_CAS10
        self.root_url = root_url
        self.api_login = "Reporting"
        self.api_login_obst = "Configuration"
        self.api_password = "password"
        self.api_password_obst = "wah0eip2Faelooh"
        self.MPData_auth = HTTPBasicAuth(self.api_login, self.api_password)

        self.CAS_request_list = [
            self.CAS_Info,
            self.CAS_GPIO,
            self.CAS_UnitsAlarmEvents,
            self.CAS_UnitErrors,
            self.CAS_CasEncounters,
            self.CAS_CasAlarms,
            self.CAS_UnitPosition,
            self.CAS_UnitStatus,
            self.CAS_VisEventData,
            self.CAS_VisInterventionData,
            self.CAS_VisSituationData,
            self.CAS_PaEventData,
            self.CAS_PaTagInfo,
            self.CAS_ObstacleNames,
            self.CAS_UgPaEventData ]
        self.CAS10_request_list = [
            self.CAS10_AlarmEvents,
            self.CAS10_UnitsConfig,
            self.CAS10_UnitsErrors,
            self.CAS10_UnitsPosition ]

    def GETSuccessResponseTest(self):
        print("GET success reaponse test \n")
        for req in self.CAS_request_list + self.CAS10_request_list:
            if req == self.CAS_ObstacleNames:
                r = requests.get(req, auth=(self.api_login_obst, self.api_password_obst))
            else:
                r = requests.get(req, auth=self.MPData_auth)
            # jData = r.json()

            if r.status_code == 200:
                print("PASS")
                print(r.status_code)
                print(req + "\n")
            else:
                print("FAIL")
                print(r.status_code)
                print(req + "\n")

    def readAlarmEvents(self):
        r = requests.get(self.CAS10_AlarmEvents, auth=self.MPData_auth)
        print(r.json()["data"])

    def readConfig(self):
        r = requests.get(self.CAS10_UnitsConfig, auth=self.MPData_auth)
        print(r.json()["data"])

    def readErrors(self):
        r = requests.get(self.CAS10_UnitsErrors, auth=self.MPData_auth)
        print(r.json()["data"])

    def readPositon(self):
        r = requests.get(self.CAS10_UnitsPosition, auth=self.MPData_auth)
        print(r.json()["data"])

# main
if __name__ == "__main__":
    restAPI = restAPI()
    restAPI.readAlarmEvents()
    restAPI.readConfig()
    restAPI.readErrors()
    restAPI.readPositon()
    