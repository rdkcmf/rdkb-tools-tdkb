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
  <version>2</version>
  <name>TS_WIFIAGENT_5GHzCheckSecurityModeUpdate_OnWPA3PersonalTransitionDisable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the Security Mode enabled, Device.WiFi.AccessPoint.2.Security.ModeEnabled updates to WPA2-Personal from WPA3 Modes such as WPA3-Personal and WPA3-Personal-Transition whenever the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is disabled.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_181</test_case_id>
    <test_objective>Check if the Security Mode enabled, Device.WiFi.AccessPoint.2.Security.ModeEnabled updates to WPA2-Personal from WPA3 Modes such as WPA3-Personal and WPA3-Personal-Transition whenever the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is disabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.AccessPoint.2.Security.ModeEnabled
paramValue : security mode
paramType : string</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial security mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and store it.
3. Check if the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is enabled, else set it to true and validate with get.
4. Set Device.WiFi.AccessPoint.2.Security.ModeEnabled to WPA3-Personal mode
5. Toggle the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition to false, it should cause the security mode to update to WPA2-Personal.
6. Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition to true and then set Device.WiFi.AccessPoint.2.Security.ModeEnabled to WPA3-Personal-Transition.
7. Now disable the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition
8. Check if the security mode updates to WPA2-personal again.
9. the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable status if required
10. Revert Device.WiFi.AccessPoint.2.Security.ModeEnabled to initial mode.
11. Unload the module.</automation_approch>
    <expected_output>Device.WiFi.AccessPoint.2.Security.ModeEnabled should update to WPA2-Personal from WPA3 Modes such as WPA3-Personal and WPA3-Personal-Transition whenever the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable is disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzCheckSecurityModeUpdate_OnWPA3PersonalTransitionDisable</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def GetParameterValue(tdkTestObj, parameter):
    tdkTestObj.addParameter("paramName", parameter);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

def SetParameterValue(tdkTestObj, parameter, paramValue, paramType):
    tdkTestObj.addParameter("paramName", parameter);
    tdkTestObj.addParameter("paramValue", paramValue);
    tdkTestObj.addParameter("paramType", paramType);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzCheckSecurityModeUpdate_OnWPA3PersonalTransitionDisable');

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
            #Set Security Mode to WPA3 modes
            wpa3_modes = ["WPA3-Personal", "WPA3-Personal-Transition"]
            for mode in wpa3_modes:
                print "\n****************For Mode %s*******************" %mode;
                #Set the security mode
                step = step + 1;
                tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                actualresult, details = SetParameterValue(tdkTestObj, "Device.WiFi.AccessPoint.2.Security.ModeEnabled", mode, "string");

                print "\nTEST STEP %d : Set Device.WiFi.AccessPoint.2.Security.ModeEnabled to %s" %(step, mode);
                print "EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.2.Security.ModeEnabled to %s" %(step,mode);

                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                    print "TEST EXECUTION RESULT :SUCCESS";

                    #Verify the SET with GET
                    step = step + 1;
                    tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                    actualresult, details = GetParameterValue(tdkTestObj, "Device.WiFi.AccessPoint.2.Security.ModeEnabled");

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

                            #Disable the WPA3 RFC
                            step = step + 1;
                            tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                            actualresult, details = SetParameterValue(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable", "false", "boolean");

                            print "\nTEST STEP %d : Disable the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable" %(step);
                            print "EXPECTED RESULT %d : Should successfully disable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable" %(step);

                            if expectedresult in actualresult :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                                print "TEST EXECUTION RESULT :SUCCESS";

                                #Verify the SET with GET
                                step = step + 1;
                                tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                                actualresult, details = GetParameterValue(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable");

                                print "\nTEST STEP %d : Get the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and check if SET operation was success" %step;
                                print "EXPECTED RESULT %d : Should successfully get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and should reflect the enable SET" %step;

                                if expectedresult in actualresult:
                                    rfc_enable = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, rfc_enable);
                                    print "TEST EXECUTION RESULT :SUCCESS";

                                    print "Set RFC Enable : false";
                                    print "Get RFC Enable : ", rfc_enable;

                                    if rfc_enable == "false" :
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "WPA3 RFC is disabled successfully";

                                        #Check if the security mode changes to WPA2-Personal
                                        step = step + 1;
                                        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                                        actualresult, details = GetParameterValue(tdkTestObj, "Device.WiFi.AccessPoint.2.Security.ModeEnabled");

                                        print "\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.2.Security.ModeEnabled and check if the mode is changes to WPA2-Personal after WPA3 RDC Disable" %step;
                                        print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.2.Security.ModeEnabled and should be WPA2-Personal after WPA3 RFC Disable" %step;

                                        if expectedresult in actualresult:
                                            security_mode_rfcdisabled = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, security_mode_rfcdisabled);
                                            print "TEST EXECUTION RESULT :SUCCESS";

                                            print "\nExpected Security Mode after WPA3 RFC Disable : WPA2-Personal";
                                            print "Actual Security Mode after WPA3 RFC Disable : ", security_mode_rfcdisabled;

                                            if security_mode_rfcdisabled == "WPA2-Personal" :
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "Security Mode has been updated as expected after disabling the WPA3 RFC";
                                            else :
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "Security Mode has NOT been updated as expected after disabling the WPA3 RFC";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                                            print "TEST EXECUTION RESULT :FAILURE";

                                        #Enable WPA3 RFC
                                        step = step + 1;
                                        tdkTestObj = obj.createTestStep("WIFIAgent_Set");
                                        actualresult, details = SetParameterValue(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable", "true", "boolean");

                                        print "\nTEST STEP %d : Enable the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable" %(step);
                                        print "EXPECTED RESULT %d : Should successfully enable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable" %(step);

                                        if expectedresult in actualresult :
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                                            print "TEST EXECUTION RESULT :SUCCESS";

                                            #Verify the SET with GET
                                            step = step + 1;
                                            tdkTestObj = obj.createTestStep("WIFIAgent_Get");
                                            actualresult, details = GetParameterValue(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable");

                                            print "\nTEST STEP %d : Get the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and check if SET operation was success" %step;
                                            print "EXPECTED RESULT %d : Should successfully get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable and should reflect the enable SET" %step;

                                            if expectedresult in actualresult:
                                                rfc_enable = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, rfc_enable);
                                                print "TEST EXECUTION RESULT :SUCCESS";

                                                print "Set RFC Enable : true";
                                                print "Get RFC Enable : ", rfc_enable;

                                                if rfc_enable == "true" :
                                                    tdkTestObj.setResultStatus("SUCCESS");
                                                    print "WPA3 RFC is enabled successfully";
                                                else :
                                                    tdkTestObj.setResultStatus("FAILURE");
                                                    print "WPA3 RFC is NOT enabled successfully";
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                                                print "TEST EXECUTION RESULT :FAILURE";
                                        else :
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                                            print "TEST EXECUTION RESULT :FAILURE";
                                    else :
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "WPA3 RFC is NOT disabled successfully";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                                    print "TEST EXECUTION RESULT :FAILURE";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                                print "TEST EXECUTION RESULT :FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "SET is NOT reflected in GET";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                        print "TEST EXECUTION RESULT :FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
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
