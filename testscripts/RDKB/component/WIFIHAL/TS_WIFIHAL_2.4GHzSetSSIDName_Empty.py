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
  <name>TS_WIFIHAL_2.4GHzSetSSIDName_Empty</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>This is a negative scenario to set SSID Name to an empty value using wifi_setSSIDName() and try getting it with wifi_getSSIDName() for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_202</test_case_id>
    <test_objective>This is a negative scenario to set SSID Name to an empty value using wifi_setSSIDName() for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSSIDName()
wifi_setSSIDName()
</api_or_interface_used>
    <input_parameters>methodName : getSSIDName
methodName : setSSIDName
radioIndex : 0</input_parameters>
    <automation_approch>"1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getSSIDName() and save the initial SSIDName
3. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_setSSIDName() with parameter as empty
4.If the set operation is SUCCESS, return FAILURE, else return SUCCESS.
5. Revert the SSIDName back to initial value
6. Unload wifihal module"
</automation_approch>
    <except_output>Set operation of SSIDName with empty value should fail</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetSSIDName_Empty</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetSSIDName_Empty');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Checking for AP Index 0, Similar way we can check for other APs
    apIndex = 0
    getMethod = "getSSIDName"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    expectedresult="SUCCESS";

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
        initialName = details.split(":")[1].strip()

        expectedresult="FAILURE";
        apIndex = 0
        setMethod = "setSSIDName"
        setName = ""
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setName, setMethod)

        if expectedresult in actualresult:
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP: Trying to set an empty value as SSID Name"
            print "EXPECTED RESULT : Should not set the empty value"
            print "ACTUAL RESULT : Unable to set the SSIDName as empty value"
            print "TEST EXECUTION RESULT :SUCCESS"
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP: Trying to set an empty value as SSID Name"
            print "EXPECTED RESULT : Should not set the empty value"
            print "ACTUAL RESULT : Sets the SSIDName to empty value"
            print "TEST EXECUTION RESULT :FAILURE"
	
            #Revert the SSID NAme back o initial value
            apIndex = 0
            setMethod = "setSSIDName"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
	    expectedresult="SUCCESS";

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialName, setMethod)
	
            if expectedresult in actualresult:
                print "Successfully reverted back to initial value"
		tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "Unable to revert to initial value"
		tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getSSIDName function failed";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
