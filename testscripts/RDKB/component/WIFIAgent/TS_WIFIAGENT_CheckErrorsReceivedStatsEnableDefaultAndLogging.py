##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################
'''
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>7</version>
  <name>TS_WIFIAGENT_CheckErrorsReceivedStatsEnableDefaultAndLogging</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable is false and Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable is true for private and hotspot vAPs and is false for others. Check if setting the disabled Associated Devices Errors Received Stats Enable to true is logged as expected in WiFilog.txt.0</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_208</test_case_id>
    <test_objective>To check if the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable is false and Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable is true for private and hotspot vAPs and is false for others. Check if setting the disabled Associated Devices Errors Received Stats Enable to true is logged as expected in WiFilog.txt.0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.FactoryReset
paramValue : Router,Wifi,VoIP,Dect,MoCA
paramType : string
paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable
paramValue : true/false
paramType : boolean</input_parameters>
    <automation_approch>1. Load the modules
2. Initiate a device factory reset
3. Once the DUT comes up, get the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable and check if it is disabled.
4. Get the default values of Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable. It should be enabled for i = 1,2,5,6,9,10 and disabled for 3,4,7,8 vAPs.
5. Enable the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable and validate the set.
6. Set Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable to true for 3,4,7,8 vAPs and validate the set.
7. Check if the log "AccessPoint_SetParamBoolValue: RxRetryList 1,2,3,4,5,6,7,8,9,10" is present under /rdklogs/logs/WiFilog.txt.0 after the set operation.
8. Revert Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable for vAPS 3,4,7,8 if required.
9. Revert the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable if required.
10. Unload the modules</automation_approch>
    <expected_output>The default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable should be false and Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable should true for private and hotspot vAPs and  false for others. The setting of disabled Associated Devices Errors Received Stats Enable to true should be logged as expected in WiFilog.txt.0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckErrorsReceivedStatsEnableDefaultAndLogging</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def setParameter(obj, param, setValue, type):
    expectedresult = "SUCCESS";
    status = 0;
    tdkTestObj = obj.createTestStep('WIFIAgent_Set_Get');
    tdkTestObj.addParameter("paramName",param);
    tdkTestObj.addParameter("paramValue",setValue);
    tdkTestObj.addParameter("paramType",type);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult not in actualresult:
        status = 1;
        print "%s SET operation failed" %param;
    return status;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *;
from time import sleep;

#Test component to be tested
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckErrorsReceivedStatsEnableDefaultAndLogging');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckErrorsReceivedStatsEnableDefaultAndLogging');

#Get the result of connection with test component and DUT
wifiloadmodulestatus=wifiobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in wifiloadmodulestatus.upper():
    #Set the result status of execution
    wifiobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Initiate a device FR
    wifiobj.saveCurrentState();
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("paramType","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Initiate a factory reset";
    print "EXPECTED RESULT 1: Factory reset should be initiated successfully";

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Factory reset is initiated successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #Restore the device state saved before reboot
        wifiobj.restorePreviousStateAfterReboot();
        #Sleep for 60s
        sleep(60);

        #Check if the RFC DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable is disabled
        tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2: Get the default value of the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable";
        print "EXPECTED RESULT 2: Should get the default value of Errors Received Enable RFC as false";

        if expectedresult in actualresult and details != "":
            rfc_enable = details.split("VALUE:")[1].split(" ")[0].strip();
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable : %s" %rfc_enable;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            if rfc_enable == "false":
                tdkTestObj.setResultStatus("SUCCESS");
                print "Errors Received Enable RFC is disabled by default";

                #Check the default values of Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable for APs 1,2,3,4,5,6,7,8,9,10
                #It should be enabled for APs 1,2,5,6,9,10 and disabled for 3,4,7,8
                Value = [];
                status = 0;

                print "\nTEST STEP 3 : Get the default values of Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable for APs 1,2,3,4,5,6,7,8,9,10";
                print "EXPECTED RESULT 3 : The default values should be retrieved successfully";

                for index in range(0, 10):
                    paramName = "Device.WiFi.AccessPoint." + str(index + 1) + ".X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable";
                    tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
                    tdkTestObj.addParameter("paramName",paramName)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        details = details.split("VALUE:")[1].split(" ")[0].strip();
                        Value.append(details);
                        print "\n%s : %s" %(paramName, Value[index]);
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        status = 1;
                        print "\n%s : %s" %(paramName, details);

                if status == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: The default values of Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable are retrieved successfully";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    #Check if the default values are as expected
                    def_status = 0;
                    expected_def = ["true", "true", "false", "false", "true", "true", "false", "false", "true", "true"];
                    print "\nTEST STEP 4 : Check if the Associated Devices Errors Received Stats Enable have the expected default values";
                    print "EXPECTED RESULT 4 : Associated Devices Errors Received Stats Enable should have the expected default values : For Private and HotSpot SSIDS, it should be enabled and disabled for all others";

                    for index in range(0, 10):
                        print "For SSID %d, expected : %s, actual : %s" %(index + 1, expected_def[index], Value[index]);

                        if Value[index] == expected_def[index]:
                            tdkTestObj.setResultStatus("SUCCESS");
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            def_status = 1;

                    if def_status == 0 :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: Associated Devices Errors Received Stats Enable have the expected default values";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"

                        #Enable the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable
                        status = setParameter(wifiobj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable", "true", "boolean");

                        print "\nTEST STEP 5 : Enable the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable";
                        print "EXPECTED RESULT 5 : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable should be enabled successfully";

                        if status == 0:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: Errors Received Enable RFC is set successfully; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS"

                            #Enable the Associated Devices Errors Received Stats Enable for the SSIDs 3,4,7,8
                            enable_set = 0;
                            revert_flag = [];
                            paramList = ["Device.WiFi.AccessPoint.3.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable", "Device.WiFi.AccessPoint.4.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable", "Device.WiFi.AccessPoint.7.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable", "Device.WiFi.AccessPoint.8.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable"];
                            print "\nTEST STEP 6 : Enable Associated Devices Errors Received Stats Enable for the SSIDs 3,4,7,8";
                            print "EXPECTED RESULT 6 : Should successfully set Associated Devices Errors Received Stats Enable for the SSIDs 3,4,7,8";

                            for iteration in range(0, 4):
                                status = setParameter(wifiobj, paramList[iteration], "true", "boolean");

                                if status == 0:
                                    revert_flag.append(1);
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "%s is set successfully to true" %(paramList[iteration]);
                                else:
                                    enable_set = 1;
                                    revert_flag.append(0);
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "%s is NOT set successfully to true" %(paramList[iteration]);

                            if enable_set == 0:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 6: Associated Devices Errors Received Stats Enable for the SSIDs 3,4,7,8 are enabled" ;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Check for the presence of of the logs "AccessPoint_SetParamBoolValue: RxRetryList 1,2,3,4,5,6,7,8,9,10"
                                sleep(10);
                                print "\nTEST STEP 7 : Check if the log \"AccessPoint_SetParamBoolValue: RxRetryList 1,2,3,4,5,6,7,8,9,10\" is present in WiFilog.txt.0";
                                print "EXPECTED RESULT 7 : The required log should be present in WiFilog.txt.0";

                                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                cmd = "cat /rdklogs/logs/WiFilog.txt.0 | grep -i \"AccessPoint_SetParamBoolValue: RxRetryList 1,2,3,4,5,6,7,8,9,10\"";
                                tdkTestObj.addParameter("command",cmd);
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                                if expectedresult in actualresult and "RxRetryList" in details:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 7: Log is present; Details : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 7: Log is NOT present; Details : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 6: Associated Devices Errors Received Stats Enable are NOT set to true for all of the SSIDs 3,4,7,8" ;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

                            #Revert of Associated Devices Errors Received Stats Enable
                            revert_complete = 0;
                            print "\nTEST STEP 8 : Revert the Associated Devices Errors Received Stats Enable if required";
                            print "EXPECTED RESULT 8 : Associated Devices Errors Received Stats Enable revert operation should be success";

                            for iteration in range(0,4):
                                if revert_flag[iteration] == 0:
                                    print "Revert of %s not required" %paramList[iteration];
                                else:
                                    status = setParameter(wifiobj, paramList[iteration], "false", "boolean");

                                    if status == 0:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "%s is successfully reverted" %(paramList[iteration]);
                                    else:
                                        revert_complete = 1;
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "%s is NOT successfully reverted" %(paramList[iteration]);

                            if revert_complete == 0:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 8: Associated Devices Errors Received Stats Enable for the SSIDs 3,4,7,8 are reverted" ;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 8: Associated Devices Errors Received Stats Enable for the SSIDs 3,4,7,8 are NOT reverted" ;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

                            #Revert the RFC
                            status = setParameter(wifiobj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable", "false", "boolean");

                            print "\nTEST STEP 9 : Revert the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable";
                            print "EXPECTED RESULT 9 : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable should be reverted successfully";

                            if status == 0:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 9: Errors Received Enable RFC is reverted successfully";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS"
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 9: Errors Received Enable RFC is NOT reverted successfully";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE"
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: Errors Received Enable RFC is NOT set successfully; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE"
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: Associated Devices Errors Received Stats Enable does NOT have the expected default values";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: The default values of Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable are NOT retrieved successfully";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Errors Received Enable RFC is NOT disabled by default";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Factory reset is not initiated successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    wifiobj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    wifiobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
