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
  <version>3</version>
  <name>TS_WIFIAGENT_SetLNF5GPassphrase_CheckRadiusServerIPAddrChange</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the Radius Server IP Address configuration for LNF SECURE 5G, Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr remains unchanged when the KeyPassphrase, Device.WiFi.AccessPoint.12.Security.KeyPassphrase is updated.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIAGENT_165</test_case_id>
    <test_objective>Check if the Radius Server IP Address configuration for LNF SECURE 5G, Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr remains unchanged when the KeyPassphrase, Device.WiFi.AccessPoint.12.Security.KeyPassphrase is updated.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr
paramName : Device.WiFi.AccessPoint.12.Security.KeyPassphrase
paramValue : randomly chosen key passphrase
paramType : string</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial Radius IP Address for LNF SECURE 5G using Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr and store it.
3. Get the initial KeyPassphrase Device.WiFi.AccessPoint.12.Security.KeyPassphrase and check if the value is exposed via TR181
4. Set Device.WiFi.AccessPoint.12.Security.KeyPassphrase to a new value successfully. Check if the GET operation does not expose the keypassphrase.
5. Check if the Radius Server IP configuration remains unchanged
6. Unload the modules</automation_approch>
    <expected_output>The Radius Server IP Address configuration for LNF SECURE 5G, Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr should remain unchanged when the KeyPassphrase, Device.WiFi.AccessPoint.12.Security.KeyPassphrase is updated.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetLNF5GPassphrase_CheckRadiusServerIPAddrChange</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

def SetValue(tdkTestObj, paramList):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("paramList",paramList);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

def GetValue(tdkTestObj, param):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("paramName",param);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from random import randint;

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_SetLNF5GPassphrase_CheckRadiusServerIPAddrChange');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper():
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Get the initial values for Radius Server IP Address
    step = 1;
    tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
    param = "Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr";
    actualresult, details = GetValue(tdkTestObj, param);

    print "\nTEST STEP %d : Get the initial Radius Server IP Address using Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr for LNF 5GHz" %step;
    print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr" %step;

    if expectedresult in actualresult:
        initial_IPAddr = details.split("VALUE:")[1].split(' ')[0].strip();
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details);
        print "Initial Radius Server IP Address : ", initial_IPAddr;
        print "TEST EXECUTION RESULT :SUCCESS";

        #Get the initial value of the LNF 5G KeyPassphrase
        step = step + 1;
        tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
        param = "Device.WiFi.AccessPoint.12.Security.KeyPassphrase";
        actualresult, details = GetValue(tdkTestObj, param);

        print "\nTEST STEP %d : Get the initial security KeyPassphrase using Device.WiFi.AccessPoint.12.Security.KeyPassphrase for LNF 5GHz" %step;
        print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.12.Security.KeyPassphrase" %step;

        if expectedresult in actualresult:
            initial_key = details.split("VALUE:")[1].split(' ')[0].strip();
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details);
            print "Initial KeyPassphrase : ", initial_key;
            print "TEST EXECUTION RESULT :SUCCESS";

            #Check if the KeyPassphrase is not exposed via DMCLI
            if initial_key == "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "The KeyPassphrase value is not exposed";

                #Set new Key Pass phrase randomly
                step = step + 1;
                key_new = "lnf-5G-wifi_" + str(randint(0,100));
                tdkTestObj = obj1.createTestStep("WIFIAgent_SetMultiple");
                paramList = "Device.WiFi.AccessPoint.12.Security.KeyPassphrase|"+ key_new + "|string|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool";
                actualresult, details = SetValue(tdkTestObj, paramList);

                print "\nTEST STEP %d : Set Device.WiFi.AccessPoint.12.Security.KeyPassphrase to %s" %(step, key_new);
                print "EXPECTED RESULT %d : Setting Device.WiFi.AccessPoint.12.Security.KeyPassphrase to %s should be success" %(step, key_new);

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the keypassphrase shows NULL value itself as the SET value should not be exposed via DMCLI
                    step = step + 1;
                    param = "Device.WiFi.AccessPoint.12.Security.KeyPassphrase";
                    tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
                    actualresult, details = GetValue(tdkTestObj, param);

                    print "\nTEST STEP %d : Get Device.WiFi.AccessPoint.12.Security.KeyPassphrase and check if value is not exposed" %(step);
                    print "EXPECTED RESULT %d : Device.WiFi.AccessPoint.12.Security.KeyPassphrase GET should not expose the value" %step;

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        details = details.split("VALUE:")[1].split(' ')[0].split(',');
                        details = details[0];
                        print "KeyPassphrase SET : ",key_new;
                        print "KeyPassphrase GET : ",details;

                        if details != key_new and details == "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "KeyPassphrase is not exposed";

                            #Check if the Radius Server IP configuration got changed due to the change in Key Pass phrase
                            step = step + 1;
                            param = "Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr";
                            tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
                            actualresult, details = GetValue(tdkTestObj, param);

                            print "\nTEST STEP %d : Get the current Radius Server IP Address using Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr for LNF 5GHz after KeyPassphrase change" %step;
                            print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.12.Security.RadiusServerIPAddr after KeyPassphrase change" %step;

                            if expectedresult in actualresult:
                                curr_IPAddr = details.split("VALUE:")[1].split(' ')[0].strip();
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details);
                                print "TEST EXECUTION RESULT :SUCCESS";

                                step = step + 1;
                                print "\nTEST STEP %d : Check if the current Radius Server IP address is the same as initial IP" %step;
                                print "EXPECTED RESULT %d : The current Radius Server IP address should be the same as initial IP" %step;
                                print "Initial Radius Server IP Address : ", initial_IPAddr;
                                print "Current Radius Server IP Address : ", curr_IPAddr;

                                if initial_IPAddr == curr_IPAddr:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: The Radius Server IP Address remains unchanged" %step;
                                    print "TEST EXECUTION RESULT :SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: The Radius Server IP Address changed" %step;
                                    print "TEST EXECUTION RESULT : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
                                print "TEST EXECUTION RESULT : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "KeyPassphrase is exposed";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "The KeyPassphrase value is exposed";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
            print "TEST EXECUTION RESULT :FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";

    obj1.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

