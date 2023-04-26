import time
from libs.mansonControl import mansonPowerSupply

# Test should check if PS3 and PS2 is deactivated after changing from Parked to Forward in Medium Battery State

def test_battery_medium_parked_to_forward(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to medium then engaging timeout for PS3 and wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(23)
    debug_port.timeOutPS3(5000)
    time.sleep(10)

    debug_port.changeMovemode("parked")  # 5 = Parked Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("forward")  # 2 = Forward Mode

    is_rf_power_save_off = False
    is_gnss_power_save_off = False
    is_reduce_gnss_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_RF_OFF"] in line:
            print("Found: ", config["POWER_SAVING_RF_OFF"])
            is_rf_power_save_off = True

        elif config["POWER_SAVING_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_GNSS_OFF"])
            is_gnss_power_save_off = True

        elif config["POWER_SAVING_REDUCE_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_OFF"])
            is_reduce_gnss_power_save_off = True
        # break out of loop as soon as keywords are found
        if is_rf_power_save_off and is_gnss_power_save_off and is_reduce_gnss_power_save_off:
            print("Found all!!")
            break

    # if keywords not found -> test failed
    if is_rf_power_save_off is False or is_gnss_power_save_off is False or is_reduce_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_rf_power_save_off and is_gnss_power_save_off and is_reduce_gnss_power_save_off
