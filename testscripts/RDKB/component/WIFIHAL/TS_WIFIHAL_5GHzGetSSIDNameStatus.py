##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WIFIHAL_5GHzGetSSIDNameStatus</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the SSIDNameStatus for 5GHz radio using  wifi_getSSIDNameStatus HAL API to read the runtime ssid name and validate the same.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_297</test_case_id>
    <test_objective>To get the SSIDNameStatus for 5GHz radio using  wifi_getSSIDNameStatus HAL API to read the runtime ssid name and validate the same.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSSIDNameStatus
</api_or_interface_used>
    <input_parameters>methodName : getSSIDNameStatus
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module
2.Using WIFIHAL_GetOrSetParamStringValue, call wifi_getSSIDNameStatus() API
3. Check if the api call is success
4. Check if the api returns the SSID name of 5GHz
5.Unload the module.</automation_approch>
    <except_output>The wifi_getSSIDNameStatus() api should return the 5GHz SSID name</except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetSSIDNameStatus</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetSSIDNameStatus');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else: 

	    expectedresult="SUCCESS";

	    #Checking for AP Index 0, Similar way we can check for other APs
	    apIndex = idx
	    getMethod = "getSSIDName"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

	    if expectedresult in actualresult:
		ssidName = details.split(":")[1].strip()
		if len(ssidName) <= 32:
		    print "Wifi_getSSIDName() function called successfully and %s"%details
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 1: Get the SSID name from wifi hal api";
		    print "EXPECTED RESULT 1: wifigetSSIDName should return a string value of SSID";
		    print "ACTUAL RESULT 1: SSID string received: %s"%ssidName;
		    print "[TEST EXECUTION RESULT] : SUCCESS";

		    apIndex = idx
		    getMethod = "getSSIDNameStatus"
		    primitive = 'WIFIHAL_GetOrSetParamStringValue'

		    #Calling the method from wifiUtility to execute test case and set result status for the test.
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

		    if expectedresult in actualresult:
			ssidNameStatus = details.split(":")[1].strip()
			if ssidNameStatus == ssidName:
			    print "Wifi_getSSIDNameStatus() function called successfully and %s"%details
			    tdkTestObj.setResultStatus("SUCCESS");
			    print "TEST STEP 2: Validate the wifi_getSSIDNameStatus Function";
			    print "EXPECTED RESULT 2: wifigetSSIDNameStatus should return a string value of SSID";
			    print "ACTUAL RESULT 2: SSID string received: %s"%ssidName;
			    print "[TEST EXECUTION RESULT] : SUCCESS";
			else:
			    print "wifi_getSSIDName function failed, %s"%details
			    tdkTestObj.setResultStatus("FAILURE");
			    print "TEST STEP 2: Validate the wifi_getSSIDName Function";
			    print "EXPECTED RESULT 2: wifigetSSIDName should return a string value of SSID";
			    print "ACTUAL RESULT 2:Failed to receive SSID string: %s"%ssidName;
			    print "[TEST EXECUTION RESULT] : FAILURE";
		else:
		    print "wifi_getSSIDName function failed, %s"%details
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 1: Get the SSID name from wifi hal api";
		    print "EXPECTED RESULT 1: wifigetSSIDName should return a string value of SSID";
		    print "ACTUAL RESULT 1:Failed to receive SSID string: %s"%ssidName;
		    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		print "wifi_getSSIDNameStatus function failed";
		tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
