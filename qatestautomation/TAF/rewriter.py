import re

def configrewrite(cmd):

    #userentry = input("Enter TestStand and Unit: ")
    userentry = cmd

    match userentry:
        case "teststand1unit1":

            file = open("teststandinfo.txt").readlines()

            for lines in file:
                if "teststand1unit1" in lines:
                    cas10unit = re.findall('CAS10_UNIT:(.*?);', str(lines))                                 #change from findall to finditer
                    cas10hotspotssid = re.findall('CAS10_HOTSPOT_SSID:(.*?);', str(lines))
                    cas10hotspotpassword = re.findall('CAS10_HOTSPOT_PASSWORD:(.*?);', str(lines))
                    casunit = re.findall('CAS_UNIT:(.*?);', str(lines))
                    display5ip = re.findall('DISPLAY5_IP:(.*?);', str(lines))
                    debugportcomcas = re.findall('DEBUG_PORT_COM_CAS:(.*?);', str(lines))
                    powersupplycom = re.findall('POWER_SUPPLY_COM:(.*?);', str(lines))

                    print(cas10unit)
                    print(cas10hotspotssid)
                    print(cas10hotspotpassword)
                    print(casunit)
                    print(display5ip)
                    print(debugportcomcas)
                    print(powersupplycom)

            #search_text = '"DISPLAY5_IP":'

            with open('config.json','r+') as f:

                file = f.read()
                #file = re.sub(fr"(?<={search_text} ).*", cas10unit[0]+",", file)
                file = re.sub(r'(?<="CAS10_UNIT": ).*', cas10unit[0]+",", file)                             #once re.findall is changed adjust from list to string
                file = re.sub(r'(?<="CAS10_HOTSPOT_SSID": ).*', cas10hotspotssid[0]+",", file)
                file = re.sub(r'(?<="CAS10_HOTSPOT_PASSWORD": ).*', cas10hotspotpassword[0]+",", file)
                file = re.sub(r'(?<="CAS_UNIT": ).*', casunit[0]+",", file)
                file = re.sub(r'(?<="DISPLAY5_IP": ).*', display5ip[0]+",", file)
                file = re.sub(r'(?<="DEBUG_PORT_COM_CAS": ).*', debugportcomcas[0]+",", file)
                file = re.sub(r'(?<="POWER_SUPPLY_COM": ).*', powersupplycom[0]+",", file)
                f.seek(0)
                f.write(file)
                f.truncate()

            return "Text replaced"



        case "teststand1unit2":

            file = open("teststandinfo.txt").readlines()

            for lines in file:
                if "teststand1unit2" in lines:
                    cas10unit = re.findall('CAS10_UNIT:(.*?);', str(lines))                                 #change from findall to finditer
                    cas10hotspotssid = re.findall('CAS10_HOTSPOT_SSID:(.*?);', str(lines))
                    cas10hotspotpassword = re.findall('CAS10_HOTSPOT_PASSWORD:(.*?);', str(lines))
                    casunit = re.findall('CAS_UNIT:(.*?);', str(lines))
                    display5ip = re.findall('DISPLAY5_IP:(.*?);', str(lines))
                    debugportcomcas = re.findall('DEBUG_PORT_COM_CAS:(.*?);', str(lines))
                    powersupplycom = re.findall('POWER_SUPPLY_COM:(.*?);', str(lines))

                    print(cas10unit)
                    print(cas10hotspotssid)
                    print(cas10hotspotpassword)
                    print(casunit)
                    print(display5ip)
                    print(debugportcomcas)
                    print(powersupplycom)

            #search_text = '"DISPLAY5_IP":'

            with open('config.json','r+') as f:

                file = f.read()
                #file = re.sub(fr"(?<={search_text} ).*", cas10unit[0]+",", file)
                file = re.sub(r'(?<="CAS10_UNIT": ).*', cas10unit[0]+",", file)                             #once re.findall is changed adjust from list to string
                file = re.sub(r'(?<="CAS10_HOTSPOT_SSID": ).*', cas10hotspotssid[0]+",", file)
                file = re.sub(r'(?<="CAS10_HOTSPOT_PASSWORD": ).*', cas10hotspotpassword[0]+",", file)
                file = re.sub(r'(?<="CAS_UNIT": ).*', casunit[0]+",", file)
                file = re.sub(r'(?<="DISPLAY5_IP": ).*', display5ip[0]+",", file)
                file = re.sub(r'(?<="DEBUG_PORT_COM_CAS": ).*', debugportcomcas[0]+",", file)
                file = re.sub(r'(?<="POWER_SUPPLY_COM": ).*', powersupplycom[0]+",", file)
                f.seek(0)
                f.write(file)
                f.truncate()

            return "Text replaced"




        case "teststand2unit1":

            file = open("teststandinfo.txt").readlines()

            for lines in file:
                if "teststand2unit1" in lines:
                    cas10unit = re.findall('CAS10_UNIT:(.*?);', str(lines))
                    cas10hotspotssid = re.findall('CAS10_HOTSPOT_SSID:(.*?);', str(lines))
                    cas10hotspotpassword = re.findall('CAS10_HOTSPOT_PASSWORD:(.*?);', str(lines))
                    casunit = re.findall('CAS_UNIT:(.*?);', str(lines))
                    display5ip = re.findall('DISPLAY5_IP:(.*?);', str(lines))
                    debugportcomcas = re.findall('DEBUG_PORT_COM_CAS:(.*?);', str(lines))
                    powersupplycom = re.findall('POWER_SUPPLY_COM:(.*?);', str(lines))

                    print(cas10unit)
                    print(cas10hotspotssid)
                    print(cas10hotspotpassword)
                    print(casunit)
                    print(display5ip)
                    print(debugportcomcas)
                    print(powersupplycom)

            #search_text = '"DISPLAY5_IP":'

            with open('config.json','r+') as f:

                file = f.read()
                #file = re.sub(fr"(?<={search_text} ).*", cas10unit[0]+",", file)
                file = re.sub(r'(?<="CAS10_UNIT": ).*', cas10unit[0]+",", file)
                file = re.sub(r'(?<="CAS10_HOTSPOT_SSID": ).*', cas10hotspotssid[0]+",", file)
                file = re.sub(r'(?<="CAS10_HOTSPOT_PASSWORD": ).*', cas10hotspotpassword[0]+",", file)
                file = re.sub(r'(?<="CAS_UNIT": ).*', casunit[0]+",", file)
                file = re.sub(r'(?<="DISPLAY5_IP": ).*', display5ip[0]+",", file)
                file = re.sub(r'(?<="DEBUG_PORT_COM_CAS": ).*', debugportcomcas[0]+",", file)
                file = re.sub(r'(?<="POWER_SUPPLY_COM": ).*', powersupplycom[0]+",", file)
                f.seek(0)
                f.write(file)
                f.truncate()

            return "Text replaced"

    #print(configrewrite(search_text,replace_text))

#configrewrite()








# import re
# import os




# def configrewrite():
#     print("Program Start")

#     search_text = '"DISPLAY5_IP": "192.168.200.233",'
#     replace_text = "replaced"


#     display5ip_read = ""
#     display5ip_write = ""
#     nwsubversion = ""

#     configFileToWrite = open("config2.json", "r")
#     datawrite = configFileToWrite.read()

#     configFileToRead = open("teststandinfo.txt", "r")
#     dataread = configFileToRead.read()


#     str = 'Python is a programming language.'
#     #search using regex
#     x = re.findall('^Python.*', str)

#     print(x)


#     lang = input("Enter TestStand")

#     match lang:
#         case "1":
#             with open('config.json','r+') as f:

#                 file = f.read()
#                 file = re.sub(search_text, replace_text, file)
#                 f.seek(0)
#                 f.write(file)
#                 f.truncate()

#             return "Text replaced"


#         #print(replacetext(search_text,replace_text))


#         case "2":
#             print("TestStand 1 selected")
#             display5ip_read = re.findall(r"teststand1: ([\d.]*\d+)", dataread)
#             print (display5ip_read)

#             display5ip_write = re.findall(r"\"DISPLAY5_IP\".*", datawrite)
#             print (display5ip_write)


#     print(configrewrite(search_text,replace_text))

# configrewrite()