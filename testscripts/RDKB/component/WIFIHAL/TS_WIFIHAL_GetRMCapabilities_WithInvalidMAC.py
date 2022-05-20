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
  <name>TS_WIFIHAL_GetRMCapabilities_WithInvalidMAC</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRMCapabilities</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRMCapabilities() with invalid client MAC address and check if the API returns failure.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_802</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRMCapabilities() with invalid client MAC address and check if the API returns failure.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRMCapabilities()</api_or_interface_used>
    <input_parameters>peer : randomly generated MAC address</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRMCapabilities() with an invalid client MAC address and check if the API invocation returns failure
3. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getRMCapabilities() should return failure when invoked with an invalid client MAC address </expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_GetRMCapabilities_WithInvalidMAC</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import randint;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetRMCapabilities_WithInvalidMAC');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="FAILURE";

    #Generate a random MAC address
    mac_partial = "7a:36:76:41:9a:";
    x = str(randint(10,99));
    mac = mac_partial + x;

    #Get the RM Capabilities details with invalid MAC
    tdkTestObj = obj.createTestStep('WIFIHAL_GetRMCapabilities');
    tdkTestObj.addParameter("peer", mac);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Invoke the HAL API wifi_getRMCapabilities() with the invalid client MAC Address : %s" %mac;
    print "EXPECTED RESULT 1: wifi_getRMCapabilities() should not be invoked successfully with invalid client MAC";

    if expectedresult in actualresult and "operation failed" in details :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 3 : wifi_getRMCapabilities() invocation failed with invalid client MAC";
        print "RM Capabilities details : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 3 : wifi_getRMCapabilities() invocation is successful with invalid MAC";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

        #Retrieve the Capabilities values
        capabilities_0 = details.split("capabilities[0] : ")[1].split(",")[0];
        capabilities_1 = details.split("capabilities[1] : ")[1].split(",")[0];
        capabilities_2 = details.split("capabilities[2] : ")[1].split(",")[0];
        capabilities_3 = details.split("capabilities[3] : ")[1].split(",")[0];
        capabilities_4 = details.split("capabilities[4] : ")[1];

        print "Capbilities[0] : ", capabilities_0;
        print "Capbilities[1] : ", capabilities_1;
        print "Capbilities[2] : ", capabilities_2;
        print "Capbilities[3] : ", capabilities_3;
        print "Capbilities[4] : ", capabilities_4;

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
