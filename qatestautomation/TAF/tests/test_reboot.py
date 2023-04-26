import time

def test_reboot(debug_port, wifi_manager, relay_control, config):
    
   # for i in range(2):
        debug_port.resetUnitwithRelay(relay_control)
        time.sleep(90)

    # if not connected then connect -> check if connected
    

        wifi_manager.connect(config["CAS10_HOTSPOT_SSID"],
                            config["CAS10_HOTSPOT_PASSWORD"], 90)
        
        assert True == wifi_manager.is_connected(config["CAS10_HOTSPOT_SSID"])        
        time.sleep(10)


        debug_port.breakStuff()
        time.sleep(5)
        debug_port.ping("192.168.200.233")
        debug_port.pingcheck()
    #    time.sleep(5)
    #    debug_port.ping("184.72.55.235")
