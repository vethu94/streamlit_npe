*** Settings ***
Documentation   Debug Tests and General Keywords for various reasons
Library         ../Libs/tab_dev_info.py
Library         ../Libs/com_port.py
Library         ../Libs/win_navigation.py
Library         String
Library         Collections

*** Variables ***
${MESSAGE}       Hello!

*** Keywords ***

### Open Close Windows ###
Open Toolbox
    [Documentation]  Opens Toolbox
    ${status}  Run Keyword  start_toolbox

Close Toolbox
    [Documentation]  Closes Toolbox
    ${status}  Run Keyword  stop_toolbox

Open SMTool
    [Documentation]  Opens SMTool
    ${status}  Run Keyword  start_smtool

Close SMTool
    [Documentation]  Closes SMTool
    ${status}  Run Keyword  stop_smtool


### Tab Device Info ###
Read Device Info
    [Documentation]  Reads Device Information from a certain COM port
    [Arguments]  ${comport}
    ${status}  Select Com Port  ${comport}
    ${dev_info}  ${details}  run keyword if  "${status}"=="OK"  readdevinfo  ${comport}
    [Return]  ${dev_info}

Get Info from DeviceInfo
    [Documentation]  Gets data from Device Info tab
    ...             First argument is the comport
    ...             Second are the names of information needed separated with ;
    ...             List of avalable information: Unit Type, Serial, Vehicle ID, Firmware version, Build No, System Monitoring, Coordinates,
    ...             Accuracy, MAC Address, IP Address, UpTime, UTC Time, Network, Expiry Date, Device Error, GPIO Values,
    ...             VOLTAGE, RF, SysMon, Distance Driven)
    ...             Example:       Get Info from DeviceInfo  COM6  UTC Time;Network;Expiry Date
    [Arguments]  ${comport}  ${info_names}
    @{answers}  create dictionary
    ${dev_info}  Read Device Info  COM6
    @{infos_needed} = 	Split String 	${info_names}  ;
    :FOR  ${info}  IN  @{infos_needed}
    \  ${answer}  Get Lines Containing String  ${dev_info}  ${info}
    \  @{tuple} = 	Split String 	${answer}  :  1
    \  ${answer}  Strip String  @{tuple}[1]
    \  Append To List 	${answers} 	${answer}
    [Return]  @{answers}


### ComPort Related ###
Check Comport Active
    [Documentation]  Checks that given COM port is active
    [Arguments]  ${comport}
    ${status}  Run Keyword  check_port_is_active  ${comport}
    [Return]  ${status}

Select Com Port
    [Documentation]  Selects given COM port in SMTool
    [Arguments]  ${comport}
    ${status}  Run Keyword  select_port  ${comport}
    [Return]  ${status}


*** Test Cases ***

TEST_DEBUG
    [Documentation]  Debug test
    #Open Toolbox
    #Open SMTool
    #Select Com Port  COM6
    #Check Comport Active  COM6
    #${DEV_INFO}  Read Device Info  COM6
    ${answer1}  Get Info from DeviceInfo  COM6  Serial;Vehicle ID;Firmware version;Build No;System Monitoring;Coordinates;Device Error;Accuracy;MAC Address;IP Address;UpTime;
    ${answer3}  Get Info from DeviceInfo  COM6  UTC Time;Network;Expiry Date;Device Error;GPIO Values;VOLTAGE;RF;SysMon
    #Close SMTool
    #Close Toolbox
    # Log  ${DEV_INFO}
    # Get FW version
    # Get serial Number