def test_connect_to_hotspot(wifi_manager, config):
    if wifi_manager.is_connected(config["CAS10_HOTSPOT_SSID"]):
        wifi_manager.disconnect()

    wifi_manager.connect(config["CAS10_HOTSPOT_SSID"],
                         config["CAS10_HOTSPOT_PASSWORD"])
    assert True == wifi_manager.is_connected(config["CAS10_HOTSPOT_SSID"])
