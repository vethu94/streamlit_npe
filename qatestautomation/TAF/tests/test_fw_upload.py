def test_publish_fw_to_cas(config_register, config):
    config_register.select_from_vehicle_tree(config["CAS_UNIT"])
    config_register.open_cas_configuration_tab()

    available_fws = config_register.cas_config.get_fw_list()
    # Select the last FW from the list, unless it is already selected.
    # In this case choose second to last FW.
    config_register.cas_config.select_fw(available_fws[-1])
    config_register.cas_config.press_save_button()
    config_register.publish()
    # TODO Add verification on mongo side


def test_publish_display_fw_to_cas10(config_register, config):
    config_register.select_from_vehicle_tree(config["CAS10_UNIT"])
    config_register.open_cas10_configuration_tab()

    available_fws = config_register.cas10_config.get_display_fw_list()
    # Select the last FW from the list, unless it is already selected.
    # In this case choose second to last FW.
    config_register.cas10_config.select_fw(available_fws[-1])
    config_register.cas10_config.press_save_button()
    config_register.publish()
    # TODO Add verification on mongo side
