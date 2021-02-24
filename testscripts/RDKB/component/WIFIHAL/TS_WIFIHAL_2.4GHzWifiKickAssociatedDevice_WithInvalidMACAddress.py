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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzWifiKickAssociatedDevice_WithInvalidMACAddress</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke wifi_kickAssociatedDevice() HAL api with an invalid MAC Address and check whether the API returns failure.</synopsis>
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
    <test_case_id>TC_WIFIHAL_511</test_case_id>
    <test_objective>To invoke wifi_kickAssociatedDevice() HAL api with an invalid MAC Address and check whether the API returns failure.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_kickAssociatedDevice</api_or_interface_used>
    <input_parameters>methodName : kickAssociatedDevice
ApIndex : 0
param : 00:aa:bb:cc:dd:ee</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_kickAssociatedDevice() api with an invalid MAC as input.
3. Check the return value of the api.The script will be SUCCESS if the return value is failure and FAILED if the return value is success
4. Unload wifihal module</automation_approch>
    <expected_output>Since we are passing invalid MAC address value, the API is expected to return failure</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzWifiKickAssociatedDevice_WithInvalidMACAddress</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio="2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzWifiKickAssociatedDevice_WithInvalidMACAddress');
loadmodulestatus = obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);

    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");

    else:
        #Caling the wifi_kickAssociatedDevice() to execute the functionality
        expectedresult = "FAILURE";
        radioIndex = idx
        Client_MAC = "00:aa:bb:cc:dd:ee"
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamStringValue');
        tdkTestObj.addParameter("radioIndex",radioIndex);
        tdkTestObj.addParameter("param",Client_MAC);
        tdkTestObj.addParameter("methodName","kickAssociatedDevice");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Calling the wifi api wifi_kickAssociatedDevice() with an invalid MAC address for 2.4GHz";
            print "EXPECTED RESULT 1: Should return failure since the MAC address is invalid";
            print "ACTUAL RESULT 1: API return status is",actualresult;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Calling the wifi api wifi_kickAssociatedDevice() with an invalid MAC address for 2.4GHz";
            print "EXPECTED RESULT 1: Should return failure since the MAC address is invalid";
            print "ACTUAL RESULT 1: API return status is",actualresult;
            print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
