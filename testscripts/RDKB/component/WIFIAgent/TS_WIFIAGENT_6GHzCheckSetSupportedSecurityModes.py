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
  <version>2</version>
  <name>TS_WIFIAGENT_6GHzCheckSetSupportedSecurityModes</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if setting security mode enabled other than WPA3-Personal to 6GHz private access point index returns failure.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_227</test_case_id>
    <test_objective>Check if setting security mode enabled other than WPA3-Personal to 6GHz private access point index returns failure.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName/ParamName : Device.WiFi.AccessPoint.i.Security.ModeEnabled
ParamValue : security mode
Type : string</input_parameters>
    <automation_approch>1. Load the module
2. Get the 6ghz private access point index from platform property file
3. Get the initial security mode enabled using Device.WiFi.AccessPoint.i.Security.ModeEnabled.
4. Check if that is WPA3-Personal
5. Enable the WPA3 RFC if not enabled already.
6. Set the security modes None, WPA2-Personal, WPA3-Personal-Transition and check if the set operation returns failure.
7. Revert to initial security mode if required
8. Unload the module
 </automation_approch>
    <expected_output>Setting security mode enabled other than WPA3-Personal to 6GHz private access point index should return failure.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_6GHzCheckSetSupportedSecurityModes</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_6GHzCheckSetSupportedSecurityModes');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_6GHzCheckSetSupportedSecurityModes');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the PRIVATE_6G_AP_INDEX
    step = 1;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    cmd = "sh %s/tdk_utility.sh parseConfigFile PRIVATE_6G_AP_INDEX" %TDK_PATH;
    print "\nCommand : ", cmd;
    tdkTestObj.addParameter("command", cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    vap = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Get the 6GHz private access point index from platform property file" %step;
    print "EXPECTED RESULT %d: Should successfully get the 6GHz private access point index from platform property file" %step;

    if expectedresult in actualresult and vap != "" :
        #Access Point index = vap + 1
        apIndex = int(vap) + 1;
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: 6GHz private access point index : %d" %(step, apIndex);
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the initial security mode
        step = step + 1;
        mode_enabled_param = "Device.WiFi.AccessPoint." + str(apIndex) + ".Security.ModeEnabled";
        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName",mode_enabled_param);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d : Get the Security Mode using %s" %(step, mode_enabled_param);
        print "EXPECTED RESULT %d : Should successfully get %s" %(step, mode_enabled_param);

        if expectedresult in actualresult:
            initial_mode = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, initial_mode);
            print "TEST EXECUTION RESULT :SUCCESS";

            #Check if it is WPA3-Personal
            step = step + 1;
            print "\nTEST STEP %d : Check if the security mode enabled in 6Ghz private access point is WPA3-Personal" %step;
            print "EXPECTED RESULT %d: The security mode enabled in 6Ghz private access point should be WPA3-Personal" %step;

            if initial_mode == "WPA3-Personal":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: The security mode enabled in 6Ghz private access point is WPA3-Personal" %(step);
                print "TEST EXECUTION RESULT :SUCCESS";

                #Check the Pre-requisites - WPA3_Personal_Transition RFC should be enabled
                step = step + 1;
                pre_req_set, tdkTestObj, step, revert_flag, initial_value = CheckWPA3Pre_requiste(obj, step);

                if pre_req_set == 1:
                    print "\n*************RFC Pre-requisite set for the DUT*****************";
                    #Set all modes to the 6G private access point when the WPA3 RFC is in enabled state
                    #Set operation should fail for all modes other than WPA3-Personal
                    set_modes = ["None", "WPA2-Personal", "WPA3-Personal-Transition"]
                    revert_mode = 0;

                    for mode in set_modes:
                        print "\n****************For Mode %s*******************" %mode;
                        expectedresult = "FAILURE"
                        #Set the security mode
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get");
                        tdkTestObj.addParameter("paramName",mode_enabled_param);
                        tdkTestObj.addParameter("paramValue",mode);
                        tdkTestObj.addParameter("paramType","string");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print "\nTEST STEP %d : Set %s to %s" %(step, mode_enabled_param, mode);
                        print "EXPECTED RESULT %d : Should not SET %s to %s" %(step, mode_enabled_param, mode);

                        if expectedresult in actualresult :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                            print "TEST EXECUTION RESULT :SUCCESS";
                        else :
                            revert_mode = 1;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                            print "TEST EXECUTION RESULT :FAILURE";
                            break;

                    #Revert to WPA3-Personal if revert flag is set
                    if revert_mode == 1:
                        step = step + 1;
                        mode = "WPA3-Personal";
                        expectedresult = "SUCCESS";
                        tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get");
                        tdkTestObj.addParameter("paramName",mode_enabled_param);
                        tdkTestObj.addParameter("paramValue",mode);
                        tdkTestObj.addParameter("paramType","string");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print "\nTEST STEP %d : Revert %s to %s" %(step, mode_enabled_param, mode);
                        print "EXPECTED RESULT %d : Should revert %s to %s" %(step, mode_enabled_param, mode);

                        if expectedresult in actualresult :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
                            print "TEST EXECUTION RESULT :SUCCESS";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
                            print "TEST EXECUTION RESULT :FAILURE";
                    else:
                        print "Security Mode enable revert operation not required";

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
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: The security mode enabled in 6Ghz private access point is NOT WPA3-Personal" %(step);
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
            print "TEST EXECUTION RESULT :FAILURE";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: 6GHz private access point index not retrieved" %(step);
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
