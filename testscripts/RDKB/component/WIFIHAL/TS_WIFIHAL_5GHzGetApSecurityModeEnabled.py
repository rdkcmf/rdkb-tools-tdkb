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
  <version>4</version>
  <name>TS_WIFIHAL_5GHzGetApSecurityModeEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the access point Security mode enabled for 5GHz radio using  wifi_getApSecurityModeEnabled HAL API and validate the same using wifi_getApSecurityModesSupported  HAL API</synopsis>
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
    <test_case_id>TC_WIFIHAL_72</test_case_id>
    <test_objective>To check if Access point Security mode enabled for 5GHz radio using  wifi_getApSecurityModeEnabled HAL API and validate the same using wifi_getApSecurityModesSupported HAL API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityModeEnabled()
wifi_getApSecurityModesSupported()</api_or_interface_used>
    <input_parameters>methodName :  getApSecurityModeEnabled
methodName :  getApSecurityModesSupported
apIndex    :   1</input_parameters>
    <automation_approch>1. Load the module.
2. Get the Ap Security Modes Supported by invoking wifi_getApSecurityModesSupported() api.
3. Get the current Ap SecurityMode Enabled by invoking wifi_getApSecurityModeEnabled() api.
4. The Ap SecurityMode Enabled retrieved should be the list of Ap Security Modes Supported.
5. If yes, return SUCCESS, else FAILURE.
6. Unload the module.</automation_approch>
    <except_output>Access point Security mode enabled for 5GHz radio should be from the list of Ap Security Modes Supported.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetApSecurityModeEnabled</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApSecurityModeEnabled');

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
	    apIndex = idx
	    getMethod = "getApSecurityModesSupported"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
	    if expectedresult in actualresult:
		SupportedModes = list(details.split(":")[1].strip().split(","));
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP 1: Validate the wifi_getApSecurityModesSupported Function";
		print "EXPECTED RESULT 1: wifi_getApSecurityModesSupported should return a set of strings";
		print "ACTUAL RESULT 1: ApSecurityModesSupported list : ",SupportedModes;
		print "[TEST EXECUTION RESULT] : SUCCESS";

		getMethod = "getApSecurityModeEnabled"
		primitive = 'WIFIHAL_GetOrSetParamStringValue'

		#Calling the method from wifiUtility to execute test case and set result status for the test.
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

		if expectedresult in actualresult:
		    mode = details.split(":")[1].strip()
		    if mode in SupportedModes:
			print "Security mode is in valid supported security modes %s"%details
			tdkTestObj.setResultStatus("SUCCESS");
			print "TEST STEP 2: Validate the Security mode Enabled";
			print "EXPECTED RESULT 2: Security modes should be from : ",SupportedModes;
			print "ACTUAL RESULT 2: Security mode received is: %s"%mode;
			print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
			print "Security mode is NOT in valid supported security modes %s"%details
			tdkTestObj.setResultStatus("FAILURE");
			print "TEST STEP 2: Validate the Security mode Enabled";
			print "EXPECTED RESULT 2: Security modes should be from : ",SupportedModes;
			print "ACTUAL RESULT 2: Security mode received is: %s"%mode;
			print "[TEST EXECUTION RESULT] : FAILURE";
		else:
		    print "getApSecurityModeEnabled() failed";
		    print details;
		    tdkTestObj.setResultStatus("FAILURE");
	    else :
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 1: Validate the wifi_getApSecurityModesSupported Function";
		print "EXPECTED RESULT 1: wifi_getApSecurityModesSupported should return a set of strings";
		print "ACTUAL RESULT 1: wifi_getApSecurityModesSupported call failed";
		print details;
		print "[TEST EXECUTION RESULT] : SUCCESS";
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
