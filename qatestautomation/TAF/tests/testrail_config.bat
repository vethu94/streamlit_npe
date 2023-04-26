@echo off
set arg1=%1
set arg2=%2
trcli -y -h https://hexagonmining.testrail.io/ --project "HxM CAS New Generation (Stromboli) - QC1000, QD1400 - CAS10" --username nattan.mueller@hexagon.com --password "1E1FE92E9F400B05F6D424B41783D5B9" parse_junit --suite-id 813 --title "SS%arg1%_NS%arg2%_D5_Powermanagement" -f junit-report.xml