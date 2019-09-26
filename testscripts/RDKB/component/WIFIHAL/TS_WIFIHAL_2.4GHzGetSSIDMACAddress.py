##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzGetSSIDMACAddress</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the SSID Mac Address and verify using BSSID</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_124</test_case_id>
    <test_objective>To get the SSID Mac Address and verify using BSSID for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator ,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSSIDMACAddress()
wifi_getBaseBSSID()</api_or_interface_used>
    <input_parameters>methodName : getSSIDMACAddress
methodName : getBaseBSSID
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getSSIDMACAddress() and save the get value
3. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getBaseBSSID() 
4. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
5. Unload wifihal module</automation_approch>
    <except_output>Return values of  wifi_getSSIDMACAddress() and wifi_getBaseBSSID() should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetSSIDMACAddress</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetSSIDMACAddress');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getSSIDMACAddress"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
    MacAddress = details.split(" :")[1].rstrip('\\n');

    if expectedresult in actualresult:
        expectedresult="SUCCESS";
        radioIndex = 0
        getMethod = "getBaseBSSID"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        BSSID = details.split(" :")[1].rstrip('\\n');

	if expectedresult in actualresult:
    	    if BSSID == MacAddress:
		print "TEST STEP: Comparing the values of SSID Mac Address and BSSID"
		print "EXECUTION RESULT : SSID Mac Address and BSSID values should be the same"
		print "ACTUAL RESULT : SSID Mac Address and BSSID values are the same"
	        print "SSID Mac Address is :%s"%MacAddress;
		tdkTestObj.setResultStatus("SUCCESS");
	    else:
		print "TEST STEP: Comparing the values of SSID Mac Address and BSSID"
		print "EXECUTION RESULT : SSID Mac Address and BSSID values should be the same"
		print "ACTUAL RESULT : SSID Mac Address and BSSID values are NOT the same"
	        print "SSID Mac Address is :%s"%MacAddress;
		tdkTestObj.setResultStatus("FAILURE");
	else:
	    print "getBaseBSSID call failed"
    else:
	print "getSSIDMACAddress call failed"

    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

