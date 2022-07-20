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
  <version>4</version>
  <name>TS_WIFIAGENT_CheckMFPConfig_WithWPA3-Personal-TransitionSecurityMode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the MFP Configuration retrieved using Device.WiFi.AccessPoint.{i}.Security.MFPConfig for the applicable radio's private AP is [2.4G - Optional, 5G - Optional] when the security mode enabled, Device.WiFi.AccessPoint.{i}.Security.ModeEnabled is "WPA3-Personal-Transition".</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIAGENT_206</test_case_id>
    <test_objective>To check if the MFP Configuration retrieved using Device.WiFi.AccessPoint.{i}.Security.MFPConfig for the applicable radio's private AP is [2.4G - Optional, 5G - Optional] when the security mode enabled, Device.WiFi.AccessPoint.{i}.Security.ModeEnabled is "WPA3-Personal-Transition".</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.{i}.Security.ModeEnabled
paramValue : security mode
paramType : string
paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.AccessPoint.{i}.Security.MFPConfig</input_parameters>
    <automation_approch>1. Load the modules
2. Get the security mode enabled for the access points using Device.WiFi.AccessPoint.{i}.Security.ModeEnabled and store them.
3. Enable the WPA3 RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable if not already enabled
4. Set the security mode enabled to "WPA3-Personal-Transition" if not already in that mode. Validate the set operation.
5. Check the MFP Config using Device.WiFi.AccessPoint.{i}.Security.MFPConfig
6. Validate if the MFP Config are : for 2.4G - Optional, 5G - Optional.
7. Revert the WPA3 RFC if required.
8. Revert the security modes if required.
9. Unload the modules.</automation_approch>
    <expected_output>The MFP Configuration retrieved using Device.WiFi.AccessPoint.{i}.Security.MFPConfig for the applicable radio's private AP should be [2.4G - Optional, 5G - Optional] when the security mode enabled, Device.WiFi.AccessPoint.{i}.Security.ModeEnabled is "WPA3-Personal-Transition".</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckMFPConfig_WithWPA3-Personal-TransitionSecurityMode</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

def getParams(obj, ap_indices, param):
    Value = [];
    status = 0;
    expectedresult = "SUCCESS";

    for index in range(0, len(ap_indices)):
        paramName = "Device.WiFi.AccessPoint." + str(ap_indices[index]) + ".Security." + param;
        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
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
            break;
    return status, Value, tdkTestObj;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckMFPConfig_WithWPA3-Personal-TransitionSecurityMode');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    ap_indices = [1,2];
    #Get the initial security mode for all the applicable VAPs
    step = 1;
    print "\nTEST STEP %d : Retrieve the initial security mode enabled using Device.WiFi.AccessPoint.{i}.Security.ModeEnabled" %step;
    print "EXPECTED RESULT %d : The initial security modes enabled should be retrieved successfully" %step;

    param = "ModeEnabled";
    status, initial_mode, tdkTestObj = getParams(obj, ap_indices, param);

    if status == 0:
        tdkTestObj.setResultStatus("SUCCESS");
        print "\nACTUAL RESULT %d: Initial security Modes enabled retrieved successfully" %step;
        #Get the result of execution
        print "TEST EXECUTION RESULT :SUCCESS";

        #Check the Pre-requisites - WPA3_Personal_Transition RFC should be enabled
        step = step + 1;
        pre_req_set, tdkTestObj, step, revert_flag, initial_value = CheckWPA3Pre_requiste(obj, step);

        if pre_req_set == 1:
            print "\n*************RFC Pre-requisite set for the DUT*****************";

            #Set the security mode to WPA3-Personal-Transition if the initial security mode is different
            step = step + 1;
            mode = "WPA3-Personal-Transition";
            status = 0;
            revert = [];

            for index in range(0, len(ap_indices)):
                param = "Device.WiFi.AccessPoint." + str(ap_indices[index]) + ".Security.ModeEnabled";
                if initial_mode[index] != mode:
                    tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get");
                    tdkTestObj.addParameter("paramName",param)
                    tdkTestObj.addParameter("paramValue",mode);
                    tdkTestObj.addParameter("paramType","string");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "\n%s set successfully to %s" %(param, mode);
                        revert.append(1);
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        status = 1;
                        print "\n%s NOT set successfully to %s" %(param, mode);
                        revert.append(0);
                else:
                    print "\n%s is already set to %s" %(param, mode);
                    revert.append(0);

            print "\nTEST STEP %d : Set the security mode enabled using Device.WiFi.AccessPoint.{i}.Security.ModeEnabled to WPA3-Personal-Transition" %step;
            print "EXPECTED RESULT %d : The security modes should be set to WPA3-Personal-Transition mode successfully" %step;

            if status == 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Security Modes are set to WPA3-Personal-Transition successfully" %step;
                #Get the result of execution
                print "TEST EXECUTION RESULT :SUCCESS";

                #Get the MFP Configuration values when the security mode enabled is WPA3-Personal-Transition mode
                step = step + 1;
                print "\nTEST STEP %d : Get the MFP Configurations using Device.WiFi.AccessPoint.{i}.Security.MFPConfig" %step;
                print "EXPECTED RESULT %d : The MFP Configurations should be retrieved successfully" %step;

                param = "MFPConfig";
                status, actual_mfp, tdkTestObj = getParams(obj, ap_indices, param);

                if status == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "\nACTUAL RESULT %d: MFP Configurations are retrieved successfully" %step;
                    #Get the result of execution
                    print "TEST EXECUTION RESULT :SUCCESS";

                    #Check if the MFP Config values are as expected
                    #For VAPs 1, 2 MFP Config = Optional, VAP 17 MFP Config = Required when WPA3-Personal-Transition is the security mode enabled
                    step = step + 1;
                    expected_mfp = ["Optional", "Optional"];
                    status = 0;

                    print "\nTEST STEP %d : Check if the MFP Configurations are as expected for the applicable VAPs when the security mode enabled in WPA3-Personal-Transition" %step;
                    print "EXPECTED RESULT %d : The MFP Configurations should be as expected for the applicable VAPs when the security mode enabled in WPA3-Personal-Transition" %step;

                    for index in range(0, len(ap_indices)):
                        print "\nFor VAP %d, expected MFPConfig : %s, actual MFPConfig : %s" %(ap_indices[index], expected_mfp[index], actual_mfp[index]);
                        if expected_mfp[index] == actual_mfp[index]:
                            tdkTestObj.setResultStatus("SUCCESS");
                            continue;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            status = 1;

                    if status == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "\nACTUAL RESULT %d: MFP Configurations are as expected when the security mode enabled is WPA3-Personal-Transition" %step;
                        #Get the result of execution
                        print "TEST EXECUTION RESULT :SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: MFP Configurations are NOT as expected when the security mode enabled is WPA3-Personal-Transition" %step;
                        #Get the result of execution
                        print "TEST EXECUTION RESULT :FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: MFP Configurations are NOT retrieved successfully" %step;
                    #Get the result of execution
                    print "TEST EXECUTION RESULT :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Security Modes are NOT set to WPA3-Personal-Transition successfully" %step;
                #Get the result of execution
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
        step = step + 1;
        status = 0;
        print "\nTEST STEP %d : Revert current security mode enabled to initial mode" %(step);
        print "EXPECTED RESULT %d : Should revert to initial security mode successfully" %step;

        for index in range(0, len(ap_indices)):
            paramName = "Device.WiFi.AccessPoint." + str(ap_indices[index]) + ".Security.ModeEnabled";
            if revert[index] == 1:
                tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get");
                tdkTestObj.addParameter("paramName",paramName)
                tdkTestObj.addParameter("paramValue",initial_mode[index]);
                tdkTestObj.addParameter("paramType","string");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s is reverted to initial security mode" %paramName;
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    status = 1;
                    print "%s is NOT reverted to initial security mode" %paramName;
            else:
                print "%s revert is not required" %paramName;

        if status == 0:
            tdkTestObj.setResultStatus("SUCCESS");
            print "\nACTUAL RESULT %d : Revert operation was success" %(step);
            print "TEST EXECUTION RESULT : SUCCESS";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : Revert operation failed" %(step);
            print "TEST EXECUTION RESULT : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Get operation failed" %(step);
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

