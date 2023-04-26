
class MPDataAPIRequests:
    def __init__(self, root_url, serial_CAS, serial_CAS10):
        # Setup variables 
        self.serial_CAS = serial_CAS
        self.serial_CAS10 = serial_CAS10
        self.root_url = root_url

        # CAS10_Misc
        self.CAS10_AlarmEvents = root_url + "cas2/{}/alarm/events".format(serial_CAS10)

        # CAS10_Unit
        self.CAS10_UnitsConfig = root_url + "cas2/{}/unit/configuration".format(serial_CAS10)
        self.CAS10_UnitsErrors = root_url + "cas2/{}/unit/error/events".format(serial_CAS10)
        self.CAS10_UnitsPosition = root_url + "cas2/{}/unit/position".format(serial_CAS10)

        # CAS_Unit
        self.CAS_Info = root_url + "cas/units/{}/info".format(serial_CAS)
        self.CAS_UnitErrors = root_url + "cas/units/{}/errors".format(serial_CAS)
        self.CAS_UnitPosition = root_url + "cas/units/{}/position".format(serial_CAS)
        self.CAS_UnitStatus = root_url + "cas/units/{}/status".format(serial_CAS)


        # CAS_Misc
        self.CAS_GPIO = root_url + "cas/{}/gpio".format(serial_CAS)
        self.CAS_UnitsAlarmEvents = root_url + "cas/{}/alarm/events".format(serial_CAS)
        self.CAS_CasAlarms = root_url + "cas/{}/alarms".format(serial_CAS)
        self.CAS_CasEncounters = root_url + "cas/{}/encounters".format(serial_CAS)

        # CAS_VIS
        self.CAS_VisEventData = root_url + "cas/{}/vis/events".format(serial_CAS)
        self.CAS_VisInterventionData = root_url + "cas/{}/vis/interventions".format(serial_CAS)
        self.CAS_VisSituationData = root_url + "cas/{}/vis/situations".format(serial_CAS)

        # CAS_PA
        self.CAS_PaEventData = root_url + "cas/{}/pa/events".format(serial_CAS)
        self.CAS_PaTagInfo = root_url + "cas/{}/pa/tag/all/info".format(serial_CAS)

        # CAS_Obstacle
        self.CAS_ObstacleNames = root_url + "cas/obstacles/{}/name".format(serial_CAS)

        # CAS_UG
        self.CAS_UgPaEventData = root_url + "cas-ug/{}/pa/events".format(serial_CAS)
