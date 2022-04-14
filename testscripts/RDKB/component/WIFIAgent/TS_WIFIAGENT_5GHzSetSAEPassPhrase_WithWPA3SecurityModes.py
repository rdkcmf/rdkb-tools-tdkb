##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>8</version>
  <name>TS_WIFIAGENT_5GHzSetSAEPassPhrase_WithWPA3SecurityModes</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if setting Device.WiFi.AccessPoint.2.Security.SAEPassphrase to valid Passphrase is success when the Access Point Security Mode Enabled Device.WiFi.AccessPoint.2.Security.ModeEnabled is set to WPA3-Personal and WPA3-Personal-Transition after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_179</test_case_id>
    <test_objective>Check if setting Device.WiFi.AccessPoint.2.Security.SAEPassphrase to valid Passphrase is success when the Access Point Security Mode Enabled Device.WiFi.AccessPoint.2.Security.ModeEnabled is set to WPA3-Personal and WPA3-Personal-Transition after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
paramName : Device.WiFi.AccessPoint.2.Security.ModeEnabled
paramValue : security mode
paramType : string
paramName : Device.WiFi.AccessPoint.2.Security.SAEPassphrase
paramValue : Passphrase generated dynamically
paramType : string</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial security mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and store it.
3. Check if the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, else set it to true and validate with get.
4. Get the initial SAE Passphrase using Device.WiFi.AccessPoint.2.Security.SAEPassphrase and store it.
5. Set the Device.WiFi.AccessPoint.2.Security.ModeEnabled wo WPA3-Personal and validate with get.
6. Check if the SET operation of Device.WiFi.AccessPoint.2.Security.SAEPassphrase to a valid new value returns success and validate with get.
7. Set the Device.WiFi.AccessPoint.2.Security.ModeEnabled wo WPA3-Personal-Transition and validate with get.
8. Check if the SET operation of Device.WiFi.AccessPoint.2.Security.SAEPassphrase to a valid new value returns success and validate with get.
9. Revert Device.WiFi.AccessPoint.2.Security.SAEPassphrase to initial value
10. Revert the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable status if required
11. Revert Device.WiFi.AccessPoint.2.Security.ModeEnabled to initial mode.
12. Unload the module.</automation_approch>
    <expected_output>Setting Device.WiFi.AccessPoint.2.Security.SAEPassphrase should be successful in WPA3-Personal and WPA3-Personal-Transition modes when the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzSetSAEPassPhrase_WithWPA3SecurityModes</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;
from random import randint;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzSetSAEPassPhrase_WithWPA3SecurityModes');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the initial security mode
    step = 1;
    tdkTestObj = obj.createTestStep("WIFIAgent_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled" %step;
    print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.ModeEnabled" %step;

    if expectedresult in actualresult:
        initial_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, initial_mode);
        print "TEST EXECUTION RESULT :SUCCESS";

        #Check the Pre-requisites - WPA3_Personal_Transition RFC should be enabled
        step = step + 1;
        pre_req_set, tdkTestObj, step, revert_flag, initial_value = CheckWPA3Pre_requiste(obj, step);

        if pre_req_set == 1:
            print "\n*************RFC Pre-requisite set for the DUT*****************";
            #Get the initial SAEPassphrase
            step = step + 1;
            tdkTestObj = obj.createTestStep("WIFIAgent_Get");
            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.SAEPassphrase");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d : Get the initial SAEPassphrase using Device.WiFi.AccessPoint.2.Security.SAEPassphrase" %step;
            print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.SAEPassphrase" %step;

            if expectedresult in actualresult:
                initial_sae = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, initial_sae);
                print "TEST EXECUTION RESULT :SUCCESS";

                #Set SAEPassphrase for each of the WPA3 modes
                wpa3_modes = ["WPA3-Personal", "WPA3-Personal-Transition"]
                for mode in wpa3_modes:
                    print "\n****************For Mode %s*******************" %mode;
                    #Set the security mode
                    step = step + 1;
                    tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
                    tdkTestObj.addParameter("paramValue",mode);
                    tdkTestObj.addParameter("paramType","string");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP %d : Set Device.WiFi.AccessPoint.2.Security.ModeEnabled to %s" %(step, mode);
                    print "EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.2.Security.ModeEnabled to %s" %(step,mode);

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                        print "TEST EXECUTION RESULT :SUCCESS";

                        #Verify the SET with GET
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print "\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and check if SET operation was success" %step;
                        print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.ModeEnabled and should reflect the SET Mode" %step;

                        if expectedresult in actualresult:
                            final_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, final_mode);
                            print "TEST EXECUTION RESULT :SUCCESS";

                            print "Set Mode : ", mode;
                            print "Get Mode : ", final_mode;

                            if final_mode == mode:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "SET is reflected in GET";

                                #Set the SAEPassphrase to a new value
                                step = step + 1;
                                saePassphrase = "test_password_" + str(randint(0, 100));
                                tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.SAEPassphrase");
                                tdkTestObj.addParameter("paramValue",saePassphrase);
                                tdkTestObj.addParameter("paramType","string");
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                print "\nTEST STEP %d : Set Device.WiFi.AccessPoint.2.Security.SAEPassphrase to %s" %(step, saePassphrase);
                                print "EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.2.Security.SAEPassphrase to %s" %(step,saePassphrase);

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                                    print "TEST EXECUTION RESULT :SUCCESS";

                                    #Verify SET with GET
                                    step = step + 1;
                                    tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.SAEPassphrase");
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    details = tdkTestObj.getResultDetails();

                                    print "\nTEST STEP %d : Get the SAEPassphrase using Device.WiFi.AccessPoint.2.Security.SAEPassphrase after the SET operation" %step;
                                    print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.SAEPassphrase" %step;

                                    if expectedresult in actualresult:
                                        final_sae = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, final_sae);
                                        print "TEST EXECUTION RESULT :SUCCESS";

                                        print "Set SAEPassphrase : ", saePassphrase;
                                        print "Get SAEPassphrase : ", final_sae;

                                        if saePassphrase == final_sae:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "SET is reflected in GET";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "SET is not reflected in GET";
                                    else:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                                        print "TEST EXECUTION RESULT :SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                                    print "TEST EXECUTION RESULT :FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "SET is NOT reflected in GET";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                            print "TEST EXECUTION RESULT : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                        print "TEST EXECUTION RESULT :FAILURE";

                #Revert operation
                print "\nReverting to initial SAEPassPhrase..."
                step = step + 1;
                tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.SAEPassphrase");
                tdkTestObj.addParameter("paramValue", initial_sae);
                tdkTestObj.addParameter("paramType","string");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "TEST STEP %d : Revert Device.WiFi.AccessPoint.2.Security.SAEPassphrase to %s" %(step, initial_sae);
                print "EXPECTED RESULT %d : Should successfully revert Device.WiFi.AccessPoint.2.Security.SAEPassphrase to %s" %(step, initial_sae);

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                    print "TEST EXECUTION RESULT :SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                    print "TEST EXECUTION RESULT :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
                print "TEST EXECUTION RESULT :FAILURE";

            #Revert the pre-requisites set
            if revert_flag == 1:
                step = step + 1;
                status = RevertWPA3Pre_requisite(obj, initial_value);

                print "\nTEST STEP %d : Revert the pre-requisite to initial value" %step;
                print "EXPECTED RESULT %d : Pre-requisites set should be reverted successfully" %step;

                if status == 1:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Revert operation was success" %step;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Revert operation failed" %step;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Reverting pre-requisites not required";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Pre-Requisite is not set successfully";

        #Revert operation of security mode
        print "Reverting to initial Security Mode..."
        step = step + 1;
        tdkTestObj = obj.createTestStep("WIFIAgent_Set");
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.Security.ModeEnabled");
        tdkTestObj.addParameter("paramValue",initial_mode);
        tdkTestObj.addParameter("paramType","string");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d : Revert Device.WiFi.AccessPoint.2.Security.ModeEnabled to initial mode : %s" %(step, initial_mode);
        print "EXPECTED RESULT %d : Reverting to initial security mode should be success" %step;

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : Reverting Mode to initial value was successful; Details : %s" %(step, details);
            print "TEST EXECUTION RESULT : SUCCESS";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : Reverting Mode to initial value was NOT successful; Details : %s" %(step, details);
            print "TEST EXECUTION RESULT : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
