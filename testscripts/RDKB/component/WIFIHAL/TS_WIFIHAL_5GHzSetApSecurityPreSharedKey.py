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
  <version>6</version>
  <name>TS_WIFIHAL_5GHzSetApSecurityPreSharedKey</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the Access point Security preShared key values for 5GHz radio using wifi_setApSecurityPreSharedKey HAL API and validate the same using wifi_getApSecurityPreSharedKey HAL API.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_74</test_case_id>
    <test_objective>To set the Access point Security preShared key values for 5GHz radio using wifi_setApSecurityPreSharedKey HAL API and validate the same using wifi_getApSecurityPreSharedKey HAL API.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityPreSharedKey()
wifi_setApSecurityPreSharedKey()</api_or_interface_used>
    <input_parameters>methodName : getApSecurityPreSharedKey
methodName  : setApSecurityPreSharedKey
setKey : sharedkey123
apIndex    : 1</input_parameters>
    <automation_approch>1.Load the module
2.Get ApSecurityPreSharedKey using wifi_getApSecurityPreSharedKey HAL API.
3.Set ApSecurityPreSharedKey using wifi_setApSecurityPreSharedKey() HAL API.
4.Get the previously set value using wifi_getApSecurityPreSharedKey HAL API and check whether get and set values are same.
5.If set and get values are same return success,else failure.
6.Unload the module.</automation_approch>
    <except_output>Set the Access point Security preShared key values for 2.4GHz radio using wifi_setApSecurityPreSharedKey HAL API and validate the same using wifi_getApSecurityPreSharedKey HAL API.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApSecurityPreSharedKey</test_script>
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApSecurityPreSharedKey');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getApSecurityPreSharedKey"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
        preSharedKey = details.split(":")[1].strip()
        if (len(preSharedKey) >= 8 and len(preSharedKey) <= 64):
            print "getApSecurityPreSharedKey function successful,%s"%details
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Validate the wifi_getApSecurityPreSharedKey Function";
            print "EXPECTED RESULT 1: wifi_getApSecurityPreSharedKey should return a string";
            print "ACTUAL RESULT 1: Preshared key string Returned: %s"%preSharedKey;
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    expectedresult="SUCCESS";
	    apIndex = 1
	    setMethod = "setApSecurityPreSharedKey"
	    setKey = "123456789123456789123456789987654321ABCD123456789EF1234567891223"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setKey, setMethod)

	    if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Validate the wifi_setApSecurityPreSharedKey Function";
                print "EXPECTED RESULT 2: wifi_setApSecurityPreSharedKey should be success";
                print "ACTUAL RESULT 2: wifi_setApSecurityPreSharedKey() is success"
                print "[TEST EXECUTION RESULT] : SUCCESS";

	        expectedresult="SUCCESS";
	        apIndex = 1
	        getMethod = "getApSecurityPreSharedKey"
	        primitive = 'WIFIHAL_GetOrSetParamStringValue'
                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
		if expectedresult in actualresult:
		    finalKey = details.split(":")[1].strip()
		    if finalKey == setKey:
			print "TEST STEP 3: Compare set nad get preSharedKeys"
			print "EXPECTED RESULT 3: Set and get preSharedKeys should be the same"		
			print "ACTUAL RESULT 3: Set and get preSharedKeys are SAME"
			print "[TEST EXECUTION RESULT] : SUCCESS";
			tdkTestObj.setResultStatus("SUCCESS");

		    else:
			print "TEST STEP 3: Compare set nad get preSharedKeys"
			print "EXPECTED RESULT 3: Set and get preSharedKeys should be the same"		
			print "ACTUAL RESULT 3: Set and get preSharedKeys are NOT SAME"
			print "[TEST EXECUTION RESULT] : FAILURE";
			tdkTestObj.setResultStatus("FAILURE");

		    #Rvert to initial value
                    #Calling the method from wifiUtility to execute test case and set result status for the test.
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, preSharedKey, setMethod)
		    if expectedresult in actualresult:
			print "Successfully reverted to initial value"
			tdkTestObj.setResultStatus("SUCCESS");
		    else:
			print "Unable to revert to initial value"
			tdkTestObj.setResultStatus("FAILURE");
		else:
		    print "getApSecurityPreSharedKey() call failed after set operation"
		    tdkTestObj.setResultStatus("FAILURE");
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Validate the wifi_setApSecurityPreSharedKey Function";
                print "EXPECTED RESULT 2: wifi_setApSecurityPreSharedKey should be success";
                print "ACTUAL RESULT 2: wifi_setApSecurityPreSharedKey() failed"
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "getApSecurityPreSharedKey() Function failed: %s"%details
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Validate the wifi_getApSecurityPreSharedKey Function";
            print "EXPECTED RESULT 1: wifi_getApSecurityPreSharedKey should return a string";
            print "ACTUAL RESULT 1: Preshared key string Returned: %s"%preSharedKey;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	print "getApSecurityPreSharedKey() Function failed";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
