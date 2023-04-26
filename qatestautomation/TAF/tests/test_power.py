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



# Test should check if PS3 is deactivated after changing from Parked to Standstill in Medium Battery State

def test_battery_medium_parked_to_standstill(config, debug_port, relay_control, max_retries=20):

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

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode

    is_rf_power_save_off = False
    is_gnss_power_save_off = False

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
        # break out of loop as soon as keywords are found
        if is_rf_power_save_off and is_gnss_power_save_off:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_rf_power_save_off is False or is_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_rf_power_save_off and is_gnss_power_save_off



# Test should check if PS2 is deactivated after changing from Standstill to Forward in Medium Battery State

def test_battery_medium_standstill_to_forward(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to medium then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(23)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("forward")  # 2 = Forward Mode

    is_reduce_gnss_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_REDUCE_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_OFF"])
            is_reduce_gnss_power_save_off = True
        # break out of loop as soon as keyword is found
        if is_reduce_gnss_power_save_off:
            print("Found!!")
            break

    # if keyword not found -> test failed
    if is_reduce_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_reduce_gnss_power_save_off



# Test should check if PS3 is activated after changing from Standstill to Parked in Medium Battery State

def test_battery_medium_standstill_to_parked(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to medium then engaging timeout for PS3 and wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(23)
    debug_port.timeOutPS3(5000)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("parked")  # 5 = Parked Mode

    is_rf_power_save_on = False
    is_gnss_power_save_on = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_RF_ON"] in line:
            print("Found: ", config["POWER_SAVING_RF_ON"])
            is_rf_power_save_on = True

        elif config["POWER_SAVING_GNSS_ON"] in line:
            print("Found: ", config["POWER_SAVING_GNSS_ON"])
            is_gnss_power_save_on = True
        # break out of loop as soon as keywords are found
        if is_rf_power_save_on and is_gnss_power_save_on:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_rf_power_save_on is False or is_gnss_power_save_on is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_rf_power_save_on and is_gnss_power_save_on



# Test should check if PS2 is deactivated after changing from Standstill to Reverse in Medium Battery State

def test_battery_medium_standstill_to_reverse(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to medium then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(23)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("reverse")  # 3 = Reverse Mode

    is_reduce_gnss_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_REDUCE_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_OFF"])
            is_reduce_gnss_power_save_off = True
        # break out of loop as soon as keyword is found
        if is_reduce_gnss_power_save_off:
            print("Found!!")
            break

    # if keyword not found -> test failed
    if is_reduce_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_reduce_gnss_power_save_off



# Test should check if PS1 and PS2 is deactivated after changing from Parked to Forward in Normal Battery State

def test_battery_normal_parked_to_forward(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("parked")  # 5 = Parked Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("forward")  # 2 = Forward Mode

    is_uwb_power_save_off = False
    is_reduce_gnss_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_OFF"] in line:
            print("Found: ", config["POWER_SAVING_UWB_OFF"])
            is_uwb_power_save_off = True

        elif config["POWER_SAVING_REDUCE_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_OFF"])
            is_reduce_gnss_power_save_off = True
        # break out of loop as soon as keywords are found
        if is_uwb_power_save_off and is_reduce_gnss_power_save_off:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_uwb_power_save_off is False or is_reduce_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_off and is_reduce_gnss_power_save_off



# Test should check if PS1 and PS2 is deactivated after changing from Parked to Reverse in Normal Battery State

def test_battery_normal_parked_to_reverse(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("parked")  # 5 = Parked Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("reverse")  # 3 = Reverse Mode

    is_uwb_power_save_off = False
    is_reduce_gnss_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_OFF"] in line:
            print("Found: ", config["POWER_SAVING_UWB_OFF"])
            is_uwb_power_save_off = True

        elif config["POWER_SAVING_REDUCE_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_OFF"])
            is_reduce_gnss_power_save_off = True
        # break out of loop as soon as keywords are found
        if is_uwb_power_save_off and is_reduce_gnss_power_save_off:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_uwb_power_save_off is False or is_reduce_gnss_power_save_off is False:
        print(f"Search Failed!! is_uwb_power_save_off={is_uwb_power_save_off}; " +
              f"is_reduce_gnss_power_save_off={is_reduce_gnss_power_save_off}")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_off and is_reduce_gnss_power_save_off



# Test should check if PS1 and PS2 is deactivated after changing from Parked to Standstill in Normal Battery State

def test_battery_normal_parked_to_standstill(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("parked")  # 5 = Parked Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode

    is_uwb_power_save_off = False
    is_reduce_gnss_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_OFF"] in line:
            print("Found: ", config["POWER_SAVING_UWB_OFF"])
            is_uwb_power_save_off = True

        elif config["POWER_SAVING_REDUCE_GNSS_OFF"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_OFF"])
            is_reduce_gnss_power_save_off = True
        # break out of loop as soon as keywords are found
        if is_uwb_power_save_off and is_reduce_gnss_power_save_off:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_uwb_power_save_off is False or is_reduce_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_off and is_reduce_gnss_power_save_off



# Test should check if PS1 and PS2 is activated after changing from Standstill to Parked in Normal Battery State

def test_battery_normal_standstill_to_parked(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("parked")  # 5 = Parked Mode

    is_uwb_power_save_on = False
    is_reduce_gnss_power_save_on = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_ON"] in line:
            print("Found: ", config["POWER_SAVING_UWB_ON"])
            is_uwb_power_save_on = True

        elif config["POWER_SAVING_REDUCE_GNSS_ON"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_ON"])
            is_reduce_gnss_power_save_on = True
        # break out of loop as soon as keywords are found
        if is_uwb_power_save_on and is_reduce_gnss_power_save_on:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_uwb_power_save_on is False or is_reduce_gnss_power_save_on is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_on and is_reduce_gnss_power_save_on



# Test should check if any modes are activated or deactivated after changing -
# from Standstill to Forward in Normal Battery State

def test_battery_normal_standstill_to_forward(config, debug_port, relay_control, max_retries=10):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("forward")  # 2 = Forward Mode

    keyword_list = [
            config["POWER_SAVING_UWB_OFF"], config["POWER_SAVING_UWB_ON"],
            config["POWER_SAVING_REDUCE_GNSS_OFF"], config["POWER_SAVING_REDUCE_GNSS_ON"],
            config["POWER_SAVING_RF_OFF"], config["POWER_SAVING_RF_ON"],
            config["POWER_SAVING_GNSS_OFF"], config["POWER_SAVING_GNSS_ON"]
             ]

    nothing_found = True

    # iterate through 10 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        is_sentence_found = any(keyword in line for keyword in keyword_list)

        if is_sentence_found:
            print("Search Failed!! Keyword found from line: {}".format(line))
            nothing_found = False
            break

    if nothing_found is True:
        print("Search Successful, nothing found!!")

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert nothing_found



# Test should check if any modes are activated or deactivated after changing -
# from Standstill to Reverse in Normal Battery State

def test_battery_normal_standstill_to_reverse(config, debug_port, relay_control, max_retries=10):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    debug_port.changeMovemode("reverse")  # 3 = Reverse Mode

    keyword_list = [
            config["POWER_SAVING_UWB_OFF"], config["POWER_SAVING_UWB_ON"],
            config["POWER_SAVING_REDUCE_GNSS_OFF"], config["POWER_SAVING_REDUCE_GNSS_ON"],
            config["POWER_SAVING_RF_OFF"], config["POWER_SAVING_RF_ON"],
            config["POWER_SAVING_GNSS_OFF"], config["POWER_SAVING_GNSS_ON"]
             ]

    nothing_found = True

    # iterate through 10 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        is_sentence_found = any(keyword in line for keyword in keyword_list)

        if is_sentence_found:
            print("Search Failed!! Keyword found from line: {}".format(line))
            nothing_found = False
            break

    if nothing_found is True:
        print("Search Successful, nothing found!!")

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert nothing_found



# Test should check if PS1 is deactivated after changing from Medium to Normal Battery State in Forward mode

def test_battery_medium_to_normal_forward(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to medium then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(23)
    time.sleep(10)

    debug_port.changeMovemode("forward")  # 2 = Forward Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    power_supply.setOutputVoltage(24)  # set voltage to normal

    is_uwb_power_save_off = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_OFF"] in line:
            print("Found: ", config["POWER_SAVING_UWB_OFF"])
            is_uwb_power_save_off = True
        # break out of loop as soon as keyword is found
        if is_uwb_power_save_off:
            print("Found!!")
            break

    # if keyword not found -> test failed
    if is_uwb_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_off



# Test should check if PS3 is deactivated after changing from Medium to Normal Battery State in Parked mode

def test_battery_medium_to_normal_parked(config, debug_port, relay_control, max_retries=20):

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

    power_supply.setOutputVoltage(24)  # set voltage to normal

    is_rf_power_save_off = False
    is_gnss_power_save_off = False

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
        # break out of loop as soon as keywords are found
        if is_rf_power_save_off and is_gnss_power_save_off:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_rf_power_save_off is False or is_gnss_power_save_off is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_rf_power_save_off and is_gnss_power_save_off



# Test should check if PS1 is activated after changing from Normal to Medium Battery State in Forward mode

def test_battery_normal_to_medium_forward(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("forward")  # 2 = Forward Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    power_supply.setOutputVoltage(23)  # set voltage to medium

    is_uwb_power_save_on = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_ON"] in line:
            print("Found: ", config["POWER_SAVING_UWB_ON"])
            is_uwb_power_save_on = True
        # break out of loop as soon as keyword is found
        if is_uwb_power_save_on:
            print("Found!!")
            break

    # if keyword not found -> test failed
    if is_uwb_power_save_on is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_on



# Test should check if PS3 is activated after changing from Normal to Medium Battery State in Parked mode

def test_battery_normal_to_medium_parked(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    # set voltage to normal then engaging timeout for PS3 and wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    debug_port.timeOutPS3(5000)
    time.sleep(10)

    debug_port.changeMovemode("parked")  # 5 = Parked Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    power_supply.setOutputVoltage(23)  # set voltage to medium

    is_rf_power_save_on = False
    is_gnss_power_save_on = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_RF_ON"] in line:
            print("Found: ", config["POWER_SAVING_RF_ON"])
            is_rf_power_save_on = True

        elif config["POWER_SAVING_GNSS_ON"] in line:
            print("Found: ", config["POWER_SAVING_GNSS_ON"])
            is_gnss_power_save_on = True
        # break out of loop as soon as keywords are found
        if is_rf_power_save_on and is_gnss_power_save_on:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_rf_power_save_on is False or is_gnss_power_save_on is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_rf_power_save_on and is_gnss_power_save_on



# Test should check if PS1 and PS2 is activated after changing from Normal to Medium Battery State in Standstill mode

def test_battery_normal_to_medium_standstill(config, debug_port, relay_control, max_retries=20):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)

    # set voltage to normal then wait to make sure power mode is changed and set
    power_supply.setOutputVoltage(24)
    time.sleep(10)

    debug_port.changeMovemode("standstill")  # 4 = Standstill Mode
    time.sleep(10)  # wait to make sure changes are set before changing movemode again

    power_supply.setOutputVoltage(23)  # set voltage to medium

    is_uwb_power_save_on = False
    is_reduce_gnss_power_save_on = False

    # iterate through 20 lines in search of the keywords
    for _ in range(max_retries):

        line = debug_port.readSingleLineFromSerial()
        # if keyword is in the line then turn boolean to true
        if config["POWER_SAVING_UWB_ON"] in line:
            print("Found: ", config["POWER_SAVING_UWB_ON"])
            is_uwb_power_save_on = True

        elif config["POWER_SAVING_REDUCE_GNSS_ON"] in line:
            print("Found: ", config["POWER_SAVING_REDUCE_GNSS_ON"])
            is_reduce_gnss_power_save_on = True
        # break out of loop as soon as keywords are found
        if is_uwb_power_save_on and is_reduce_gnss_power_save_on:
            print("Found both!!")
            break

    # if keywords not found -> test failed
    if is_uwb_power_save_on is False or is_reduce_gnss_power_save_on is False:
        print("Search Failed!!")

    # turn on relay comms between CAS and Display5 and exits debugmode

    debug_port.finalizeSerialComAndDebugmode(relay_control)
    power_supply.disconnectFromDevice()
    assert is_uwb_power_save_on and is_reduce_gnss_power_save_on



# Test shuold show if the power consumption between LowDP (Drain Protect) -
# and Normal Battery mode is greater than 6 times

# Normal P = 3.7179 W (no QD1400 connected)
# DP P = 0.572 W (no QD1400 connected)
# ratio ~6.5

def test_battery_low_DP_to_normal(config, debug_port, relay_control):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    debug_port.timeOutDP(5000)  # timeout for Drain Protect
    # turn on relay comms between CAS and Display5 and exits debugmode
    debug_port.finalizeSerialComAndDebugmode(relay_control)

    power_supply.setOutputVoltage(9)
    time.sleep(40)  # wait for Display5 to turn off completly

    medium_voltage_threshold = 13.7  # voltage threshold to set on the power supply
    offset = 0.2  # voltage diff between power supply and MFA measurement
    p1 = power_supply.readPowerConsumption(power_supply)  # power consumption calculation while in DP
    power_supply.setOutputVoltage(medium_voltage_threshold + offset)
    time.sleep(40)  # wait for devices to turn back on
    p2 = power_supply.readPowerConsumption(power_supply)  # power consumption calculation when back to normal
    power_supply.disconnectFromDevice()
    relay_control.turnOffGivenRelays(config["DEBUG_PORT_RELAY"])
    assert p2/p1 > 6



# Test shuold show if the power consumption between Normal and LowDP (Drain Protect) -
# Battery mode is greater than 6 times

# Normal P = 3.7179 W (no QD1400 connected)
# DP P = 0.572 W (no QD1400 connected)
# ratio ~6.5

def test_battery_normal_to_low_DP(config, debug_port, relay_control):

    power_supply = mansonPowerSupply(config["POWER_SUPPLY_COM"])
    power_supply.connectToDevice()
    power_supply.setOutputVoltage(14)  # set voltage to normal

    # turn off relay comms between CAS and Display5 and starts debugmode
    debug_port.initializeSerialComAndDebugmode(relay_control)
    debug_port.timeOutDP(5000)  # timeout for Drain Protect
    # turn on relay comms between CAS and Display5 and exits debugmode
    debug_port.finalizeSerialComAndDebugmode(relay_control)

    medium_voltage_threshold = 9  # voltage threshold to set on the power supply
    offset = 0.2  # voltage diff between power supply and MFA measurement
    p1 = power_supply.readPowerConsumption(power_supply)  # power consumption calculation before DP
    power_supply.setOutputVoltage(medium_voltage_threshold + offset)  # set voltage to low
    time.sleep(40)  # wait for Display5 to turn off completly
    p2 = power_supply.readPowerConsumption(power_supply)  # power consumption calculation while in DP
    power_supply.setOutputVoltage(14)  # set voltage back to normal
    power_supply.disconnectFromDevice()
    assert p1/p2 > 6
