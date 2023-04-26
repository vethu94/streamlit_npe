### PATHS ###
test_dir = r"C:\Program Files (x86)\Hexagon_Mining\SafetyToolbox"
test_prog = r"\ToolboxLauncher.exe"

fw_path = r"C:\GitRepos\qatestautomation\Using_SMTool\test_data\fw\FW4.4.0_RC\SM4.312_5778_050dad9"
config_path =r"C:\GitRepos\qatestautomation\Using_SMTool\test_data\ini\universal_sim_on.ini"
#config_name_reg = r"hfab"
config_name_reg = r"ht"
obst_path = r"C:\GitRepos\qatestautomation\Using_SMTool\test_data\obst\obst_1.ini"
voice_path = r"C:\GitRepos\qatestautomation\Using_SMTool\test_data\voice\dummy.voc"
log_file_path = r"C:\GitRepos\qatestautomation\Using_SMTool\SMTool\logs"
device_info_path = r"C:\GitRepos\qatestautomation\Using_SMTool\SMTool\logs"
download_path = r"C:\Temp"

### TITLES ###
name_surname = "Marifay Bratsaki"  # User should change this according to the name of the SMTool licence in the given PC
kind_of_licence = "Support"
tool_title = "SMTool " + str(kind_of_licence) + " " + str(name_surname)
#tool_title = "SMTool Support Marifay Bratsaki"
title = "HxGN MineProtect Toolbox"
tool = "SMTool"
popup_title = "Progress"
search_win_title ="Open"
download_title = "List of Files"
download_title_smdata = "CAS Log Download"

### BOXES & BUTTONS ###
control_file_box = {"conf": "[NAME:confFileBox]", "obst": "[NAME:obstFileBox]", "fw": "[NAME:fwFileBox]", "voice": "[NAME:voiceFileBox]"}
control_check_box = {"conf": "[NAME:confCheckBox]", "obst": "[NAME:obstCheckBox]", "fw": "[NAME:fwCheckBox]", "voice": "[NAME:voiceCheckBox]"}
upload_button = "[NAME:uploadButton]"
ok_button = "[NAME:okButton]"
refresh_button = "[NAME:refreshButton]"
compare_conf_button = "[NAME:compareConfButton]"
control_file_point = "[NAME:radioButtonConfigFile]"
control_config_veh_reg_point = "[NAME:radioButtonVehRegister]"
control_config_reg_point = "[NAME:radioButtonConfigRegisterConfig]"
download_dir_box = "[NAME:dirBox]"
download_dir_box_smdata = "[NAME:textBoxDownloadTarget]"
download_to_PC_button = "[NAME:downloadButton]"
download_button = "[NAME:goButton]"
download_button_smdata = "[NAME:buttonDownloadLogSmData]"
recovery_upload_button = "[NAME:recoverFWButton]"

fw_check = {"FW3": "3.0.5","FW4": "4.0.3", "FW4.2": "4.2.1", "FW4.4": "4.3.12"}

test_status = "FAIL"
upload_config = False  # True or False
timeout_vlong = 360
timeout_long = 60
timeout_short = 5
timeout_vshort = 3

active_com_list = [6]
#active_com_list = [9, 10, 12]   #QC23x units
#active_com_list = [6, 7, 8, 9, 10, 11, 12, 13, 14]  #COM13 is QC241 - do NOT upload FW3.0.5 !!!!!
#active_com_list = [6, 7, 8, 9, 10, 11, 12, 13]
#active_com_list = [10, 12]