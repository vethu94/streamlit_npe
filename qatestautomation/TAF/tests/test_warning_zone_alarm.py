import time

"""
set device position (latitude, longitude)
check if alarm occurs on display
"""

HIGH_LAT = 0.5
HIGH_LON = 0.5
MEDIUM_LAT = 1.5
MEDIUM_LON = 1.5
LOW_LAT = 7.5
LOW_LON = 7.5
NONE_LAT = 11.5
NONE_LON = 11.5
NONE_EDGE_LAT = 20
NONE_EDGE_LON = 20
FIFTEEN_METERS = 0.00015
OUTSIDE_LAT = 22
OUTSIDE_LON = 22
ELEVATION = 300
SPEED = 10
HEADING = 3.1428
MOVEMODE = 2
FWDGEAR = 0
REVGEAR = 0
HACC = 2
HEADINGMODE = 1


def test_activate_high_warning_zone_alarm(config, debug_port):
    debug_port.breakStuff()
    is_found = False

    print("Move antenna into high severity warning zone")
    debug_port.setEgoState(HIGH_LAT, HIGH_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["HIGH_WARNING_ZONE"] in line1:
            print("Found: ", config["HIGH_WARNING_ZONE"])
            is_found = True
            break

    assert is_found
    time.sleep(10)


def test_activate_medium_warning_zone_alarm(config, debug_port):
    debug_port.breakStuff()
    is_found = False

    print("Move antenna into medium severity warning zone")
    debug_port.setEgoState(MEDIUM_LAT, MEDIUM_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["MEDIUM_WARNING_ZONE"] in line1:
            print("Found: ", config["MEDIUM_WARNING_ZONE"])
            is_found = True
            break

    assert is_found
    time.sleep(10)


def test_activate_low_warning_zone_alarm(config, debug_port):
    debug_port.breakStuff()
    is_found = False

    print("Move antenna into low severity warning zone")
    debug_port.setEgoState(LOW_LAT, LOW_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["LOW_WARNING_ZONE"] in line1:
            print("Found: ", config["LOW_WARNING_ZONE"])
            is_found = True
            break

    assert is_found
    time.sleep(10)


def test_activate_none_warning_zone_alarm(config, debug_port):
    debug_port.breakStuff()
    is_found = False

    print("Move antenna into none severity warning zone")
    debug_port.setEgoState(NONE_LAT, NONE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["NONE_WARNING_ZONE"] in line1:
            print("Found: ", config["NONE_WARNING_ZONE"])
            is_found = True
            break

    assert is_found
    time.sleep(10)


def test_jump_between_zones(config, debug_port):
    debug_port.breakStuff()
    not_found_outside1 = False
    is_found_in_none = False
    not_found_outside2 = False

    print("Move antenna outside each zone")
    debug_port.setEgoState(OUTSIDE_LAT, OUTSIDE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if not config["NONE_WARNING_ZONE"] in line1:
            print("Not found any alarm")
            not_found_outside1 = True
            break

    time.sleep(10)

    print("Move antenna into none severity warning zone")
    debug_port.setEgoState(NONE_LAT, NONE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["NONE_WARNING_ZONE"] in line1:
            print("Found: ", config["NONE_WARNING_ZONE"])
            is_found_in_none = True
            break

    time.sleep(10)

    print("Move antenna back outside each zone")
    debug_port.setEgoState(OUTSIDE_LAT, OUTSIDE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if not config["NONE_WARNING_ZONE"] in line1:
            print("Not found any alarm")
            not_found_outside2 = True
            break

    assert not_found_outside1 & is_found_in_none & not_found_outside2
    time.sleep(10)


def test_if_hysteresis_applied(config, debug_port):
    debug_port.breakStuff()
    not_found_outside1 = False
    not_found_on_edge = False
    is_found_inside = False
    is_found_on_edge = False
    not_found_outside2 = False

    print("Move antenna outside each zone")
    debug_port.setEgoState(OUTSIDE_LAT, OUTSIDE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if not config["NONE_WARNING_ZONE"] in line1:
            print("Not found any alarm")
            not_found_outside1 = True
            break

    time.sleep(10)

    print("Move antenna from outside zone to edge of the none warning zone")
    debug_port.setEgoState(NONE_EDGE_LAT, NONE_EDGE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if not config["NONE_WARNING_ZONE"] in line1:
            print("Not found any alarm")
            not_found_on_edge = True
            break

    time.sleep(10)

    print("Move antenna from the edge of the none warning zone to inside the zone")
    debug_port.setEgoState(NONE_EDGE_LAT-FIFTEEN_METERS, NONE_EDGE_LON-FIFTEEN_METERS, ELEVATION, SPEED, HEADING,
                           MOVEMODE, FWDGEAR, REVGEAR, HACC, HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["NONE_WARNING_ZONE"] in line1:
            print("Found: ", config["NONE_WARNING_ZONE"])
            is_found_inside = True
            break

    time.sleep(10)

    print("Move antenna from inside the zone to the edge of the none warning zone")
    debug_port.setEgoState(NONE_EDGE_LAT, NONE_EDGE_LON, ELEVATION, SPEED, HEADING, MOVEMODE, FWDGEAR, REVGEAR, HACC,
                           HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if config["NONE_WARNING_ZONE"] in line1:
            print("Found: ", config["NONE_WARNING_ZONE"])
            is_found_on_edge = True
            break

    time.sleep(10)

    print("Move antenna from the edge of the none warning zone to outside zone")
    debug_port.setEgoState(NONE_EDGE_LAT+FIFTEEN_METERS, NONE_EDGE_LON+FIFTEEN_METERS, ELEVATION, SPEED, HEADING,
                           MOVEMODE, FWDGEAR, REVGEAR, HACC, HEADINGMODE)

    for i in range(30):
        line1 = debug_port.readSingleLineFromSerial()
        if not config["NONE_WARNING_ZONE"] in line1:
            print("Not found any alarm")
            not_found_outside2 = True
            break

    assert not_found_outside1 & not_found_on_edge & is_found_inside & is_found_on_edge & not_found_outside2
