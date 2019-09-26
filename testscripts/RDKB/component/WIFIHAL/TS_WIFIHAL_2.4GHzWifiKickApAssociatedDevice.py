##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzWifiKickApAssociatedDevice</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To take the action to remove the existing wifi client connection for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_286</test_case_id>
    <test_objective>To take the action to remove the existing wifi client connection for 2.4GHz</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.As this is a functional scenario and have limitation to validate via HAL APIs, we are validating this API by passing an dummy/invalid client MAC address and expecting the API to return failure
2.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
3.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>>wifi_kickApAssociatedDevice()</api_or_interface_used>
    <input_parameters>methodName : kickApAssociatedDevice
ApIndex : 0
param : 00:aa:bb:cc:dd:ee</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_kickApAssociatedDevice() api
3. Check the return value of the api.The script will SUCCESS if the return value is failure and FAILED if the return value is success
4. Unload wifihal module</automation_approch>
    <except_output>Since we are passing the invalid MAC address value, the API is expected to return failure</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzWifiKickApAssociatedDevice</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzWifiKickApAssociatedDevice');
loadmodulestatus = obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Caling the wifi_kickApAssociatedDevice() to execute the functionality
    expectedresult = "FAILURE";
    radioIndex = 0
    Client_MAC = "00:aa:bb:cc:dd:ee"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex",radioIndex);
    tdkTestObj.addParameter("param",Client_MAC);
    tdkTestObj.addParameter("methodName","kickApAssociatedDevice");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Calling the wifi api wifi_kickApAssociatedDevice() to remove the connected wifi client for 2.4GHz";
    	print "EXPECTED RESULT 1: Should return failure since the MAC address is invalid";
	print "ACTUAL RESULT 1: API return status is",actualresult;
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Calling the wifi api wifi_kickApAssociatedDevice() to remove the connected wifi client for 2.4GHz";
        print "EXPECTED RESULT 1: Should return failure since the MAC address is invalid";
        print "ACTUAL RESULT 1: API return status is",actualresult;
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
    