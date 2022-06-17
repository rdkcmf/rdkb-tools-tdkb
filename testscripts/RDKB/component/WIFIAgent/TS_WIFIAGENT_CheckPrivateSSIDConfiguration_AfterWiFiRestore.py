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
  <version>13</version>
  <name>TS_WIFIAGENT_CheckPrivateSSIDConfiguration_AfterWiFiRestore</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Private SSID Configuration (AP 1, AP 2) is getting restored when Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp is set to "1,2;1,2".</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIAGENT_196</test_case_id>
    <test_objective>To check if the Private SSID Configuration (AP 1, AP 2) is getting restored when Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp is set to "1,2;1,2".</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.SSID.1.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.SSID.2.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.SSID.1.SSID
paramValue : dynamically generated
paramType : string
paramName : Device.WiFi.SSID.2.SSID
paramValue : dynamically generated
paramType : string
paramName : Device.WiFi.AccessPoint.1.Security.KeyPassphrase
paramValue : dynamically generated
paramType : string
paramName : Device.WiFi.AccessPoint.2.Security.KeyPassphrase
paramValue : dynamically generated
paramType : string
paramName : Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp
paramValue : 1,2;1,2
paramType : string
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial values of Device.WiFi.SSID.1.Enable and Device.WiFi.SSID.2.Enable and set to enabled if not already in enabled state.
3. Get the initial values of Device.WiFi.SSID.1.SSID, Device.WiFi.SSID.2.SSID, Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase.
4. Set all the 4 above mentioned parameters to new dynamically generated values and verify with GET.
5. Perform WiFi restore of APs 1,2 with Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp
6. Sleep for 100s for the WiFi restore operation to take effect.
7. Check the values of Device.WiFi.SSID.1.SSID, Device.WiFi.SSID.2.SSID, Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase after WiFi restore. It should be different from the values before WiFi restore operation.
8. Revert to initial Private SSID configuration and SSID Enable status if required.
9. Unload the modules
</automation_approch>
    <expected_output>The Private SSID Configuration (AP 1, AP 2) should get restored when Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp is set to "1,2;1,2".</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckPrivateSSIDConfiguration_AfterWiFiRestore</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def setParameter(obj1, param, setValue, type):
    expectedresult = "SUCCESS";
    status = 0;
    tdkTestObj = obj1.createTestStep('WIFIAgent_Set_Get');
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
from tdkutility import *
from random import randint;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPrivateSSIDConfiguration_AfterWiFiRestore');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPrivateSIDConfiguration_AfterWiFiRestore');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    paramList_enable=["Device.WiFi.SSID.1.Enable", "Device.WiFi.SSID.2.Enable"];
    tdkTestObj,status,enableValue = getMultipleParameterValues(obj,paramList_enable)

    print "\nTEST STEP 1: Get the values of Private SSID enable status - ", paramList_enable;
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and enableValue[0] != "" and enableValue[1] != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Private SSID enable statuses are respectively : %s, %s" %(enableValue[0],enableValue[1]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Enable the SSIDs if not enabled already
        step = 2;
        print "\nTEST STEP 2 : Check if the SSIDs are enabled and enable them if required";
        print "EXPECTED RESULT 2 : The SSIDs should be enabled";
        ssid_enable_flag = 0;
        revert_flag = [0, 0];

        for index in range(0, 2):
            if enableValue[index] != "true":
                status = setParameter(obj1, paramList_enable[index], "true", "boolean");
                if status == 0:
                    revert_flag[index] = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s is enabled successfully" %paramList_enable[index];
                else:
                    ssid_enable_flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "%s is NOT enabled successfully" %paramList_enable[index];
            else :
                print "%s is enabled, SET operation not required" %paramList_enable[index];

        if ssid_enable_flag == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: SSIDs are enabled";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the initial Private SSID and KeyPassphrase
            step = 3;
            paramList_ssid_config = ["Device.WiFi.SSID.1.SSID", "Device.WiFi.AccessPoint.1.Security.KeyPassphrase", "Device.WiFi.SSID.2.SSID", "Device.WiFi.AccessPoint.2.Security.KeyPassphrase"];
            tdkTestObj,status,orgSSIDConfig = getMultipleParameterValues(obj,paramList_ssid_config)

            print "\nTEST STEP 3: Get the Private SSID configuration parameter values - ", paramList_ssid_config;
            print "EXPECTED RESULT 3 : The values should be retrieved successfully";

            if expectedresult in status and orgSSIDConfig[0] != "" and orgSSIDConfig[1] != "" and orgSSIDConfig[2] != "" and orgSSIDConfig[3] != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Private SSID Configuration are respectively : %s, %s, %s, %s" %(orgSSIDConfig[0],orgSSIDConfig[1],orgSSIDConfig[2],orgSSIDConfig[3]) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Set to new configuration
                step = 4;
                ssid1 = "Private-SSID-" + str(randint(0, 99));
                key1 = "Private-Key-" + str(randint(0, 99));
                ssid2 = "Private-SSID-" + str(randint(100, 199));
                key2 = "Private-Key-" + str(randint(100, 199));
                setvalues = [ssid1, key1, ssid2, key2];

                print "\nTEST STEP 4 : Set new Private SSID Configuration using : ", paramList_ssid_config;
                print "EXPECTED RESULT 4 : New Private SSID Configuration should be set successfully";
                ssid_config_flag = 0;

                for index in range(0, 4):
                    status = setParameter(obj1, paramList_ssid_config[index], setvalues[index], "string");
                    if status == 0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "%s is set successfully to %s" %(paramList_ssid_config[index], setvalues[index]);
                    else:
                        ssid_config_flag = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "%s is NOT set successfully to %s" %(paramList_ssid_config[index], setvalues[index]);

                if ssid_config_flag == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: New Private SSID Configuration is set successfully" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Perform WiFi restore if the SSID configuration is set properly
                    step = 5;
                    tdkTestObj = obj1.createTestStep("WIFIAgent_Set");
                    tdkTestObj.addParameter("paramName","Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp");
                    tdkTestObj.addParameter("paramValue","1,2;1,2");
                    tdkTestObj.addParameter("paramType","string");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    print "\nTEST STEP 5 : Perform WiFi Restore operation using Device.WiFi.X_CISCO_COM_FactoryResetRadioAndAp";
                    print "EXPECTED RESULT 5 : The WiFi restore operation should be successful";

                    if expectedresult in actualresult and details != "" :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5 : WiFi radio reset operation was success; Details : %s" %(details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Sleep for 100s for restore settings to take effect
                        print "Sleeping 100s for WiFi restore settings to take effect";
                        sleep(100);

                        #Check if the Private SSID configuration is changed to default values
                        step = 6;
                        tdkTestObj,status,finalSSIDConfig = getMultipleParameterValues(obj,paramList_ssid_config)

                        print "\nTEST STEP 6: Get the Private SSID configuration parameter values - ", paramList_ssid_config;
                        print "EXPECTED RESULT 6 : The values should be retrieved successfully";

                        if expectedresult in status and finalSSIDConfig[0] != "" and finalSSIDConfig[1] != "" and finalSSIDConfig[2] != "" and finalSSIDConfig[3] != "":
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6: Private SSID Configuration are respectively : %s, %s, %s, %s" %(finalSSIDConfig[0],finalSSIDConfig[1],finalSSIDConfig[2],finalSSIDConfig[3]) ;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Check if the final SSID config value is different from the setvalues
                            step = 7;
                            print "\nTEST STEP 7: Check if the SSID configuration after WiFi Restore is different from values set";
                            print "EXPECTED RESULT 7 : The SSID configuration after WiFi Restore should be different from values set";

                            restore_check = 0;
                            for index in range(0, 4):
                                print "%s before restore : %s, after restore : %s" %(paramList_ssid_config[index], setvalues[index], finalSSIDConfig[index]);
                                if finalSSIDConfig[index] == setvalues[index]:
                                    restore_check = 1;
                                else:
                                    continue;

                            if restore_check == 0:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 7: The SSID configuration after WiFi Restore is different from values set" ;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 7: The SSID configuration after WiFi Restore is NOT different from values set" ;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

                            #Revert to initial SSID configuration
                            if finalSSIDConfig[0] == orgSSIDConfig[0] and finalSSIDConfig[1] == orgSSIDConfig[1] and finalSSIDConfig[2] == orgSSIDConfig[2] and finalSSIDConfig[3] == orgSSIDConfig[3]:
                                print "Reverting the SSID configuration not required...";
                            else :
                                step = 8;
                                print "\nTEST STEP 8 : Revert to initial Private SSID Configuration";
                                print "EXPECTED RESULT 8 : Revert to initial Private SSID Configuration should be successful";

                                status1 = 0;
                                status2 = 0;
                                status3 = 0;
                                status4 = 0;
                                status5 = 0;
                                status6 = 0;
                                if finalSSIDConfig[0] != orgSSIDConfig[0] or finalSSIDConfig[1] != orgSSIDConfig[1]:
                                    #Enable the SSID
                                    status1 = setParameter(obj1, paramList_enable[0], "true", "boolean");

                                    if status1 == 0:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "%s is enabled successfully" %paramList_enable[0];

                                        #Revert SSID
                                        if finalSSIDConfig[0] != orgSSIDConfig[0] :
                                            status2 = setParameter(obj1, paramList_ssid_config[0], orgSSIDConfig[0], "string");

                                        #Revert KeyPassphrase
                                        if finalSSIDConfig[1] != orgSSIDConfig[1]:
                                            status3 = setParameter(obj1, paramList_ssid_config[1], orgSSIDConfig[1], "string");
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "%s is NOT enabled successfully" %paramList_enable[0];

                                if finalSSIDConfig[2] != orgSSIDConfig[2] or finalSSIDConfig[3] != orgSSIDConfig[3]:
                                    #Enable the SSID
                                    status4 = setParameter(obj1, paramList_enable[1], "true", "boolean");

                                    if status4 == 0:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "%s is enabled successfully" %paramList_enable[1];

                                        #Revert SSID
                                        if finalSSIDConfig[2] != orgSSIDConfig[2] :
                                            status5 = setParameter(obj1, paramList_ssid_config[2], orgSSIDConfig[2], "string");

                                        #Revert KeyPassphrase
                                        if finalSSIDConfig[3] != orgSSIDConfig[3]:
                                            status6 = setParameter(obj1, paramList_ssid_config[3], orgSSIDConfig[3], "string");
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "%s is NOT enabled successfully" %paramList_enable[0];

                                #Check the status of revert operation
                                if status1 == 0 and status2 == 0 and status3 == 0 and status4 == 0 and status5 == 0 and status6 == 0:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 8: The revert operation was success" ;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 8: The revert operation was failed" ;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                        else :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6: Private SSID Configuration is NOT retrieved";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5 : WiFi radio reset operation was failed; Details : %s" %(details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: New Private SSID Configuration is NOT set successfully" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Private SSID Configuration is NOT retrieved";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: SSIDs are NOT enabled";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Revert the SSID enable status
        step = step + 1;
        print "\nTEST STEP %d : Revert the SSID Enable Status if required" %step;
        print "EXPECTED RESULT %d : The revert operation if required should be success" %step;
        revert_success = 0;

        for index in range(0, 2):
            if revert_flag[index] == 1:
                status = setParameter(obj1, paramList_enable[index], enableValue[index], "boolean");
                if status == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s is reverted successfully" %paramList_enable[index];
                else:
                    revert_success = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "%s is NOT reverted successfully" %paramList_enable[index];
            else :
                print "%s revert operation not required" %paramList_enable[index];

        if revert_success == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Checked if SSID Enable revert is required; Revert operation is success in required cases" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Checked if SSID Enable revert is required; Revert operation is failed in required cases" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Private SSID enable statuses are NOT retrieved";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("wifiagent");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
