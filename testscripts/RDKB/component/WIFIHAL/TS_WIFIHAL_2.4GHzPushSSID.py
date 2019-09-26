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
  <name>TS_WIFIHAL_2.4GHzPushSSID</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To push the ssid name to the hardware for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_270</test_case_id>
    <test_objective>To push the ssid name to the hardware for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_pushSSID()
wifi_getSSIDName()</api_or_interface_used>
    <input_parameters>methodName : pushSSID
methodName : getSSIDName
radioIndex : 0</input_parameters>
    <automation_approch>1.Load the module
2.Using WIFIHAL_GetOrSetParamStringValue call wifi_getSSIDName() and get the initial SSID Name
3. Using WIFIHAL_GetOrSetParamStringValue, call wifi_pushSSID() API and pus ha new value of SSID name to hardware
4. Call wifi_getSSIDName() and see if the ssid name has chnaged to new value
5. If the set and get values are same, return SUCCESS else return FAILURE
6.Unload the module.</automation_approch>
    <except_output>Set value through wifi_pushSSID() and get value through wifi_getSSIDName() should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPushSSID</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPushSSID');

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
	tdkTestObj.setResultStatus("SUCCESS");
        initialName = details.split(":")[1].strip()

        expectedresult="SUCCESS";
        apIndex = 0
        setMethod = "pushSSID"
        setName = "ssid_0_name"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setName, setMethod)

        if expectedresult in actualresult:
	    tdkTestObj.setResultStatus("SUCCESS");
            apIndex = 0
            getMethod = "getSSIDName"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
            finalName = details.split(":")[1].strip()

            if expectedresult in actualresult:
                if finalName == setName:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Compare the pushSSID value and get values of SSID Name"
                    print "EXPECTED RESULT : Value pushed to hardware and get value of SSID Name should be the same"
                    print "ACTUAl RESULT : Value pushed to hardware and get value of SSID Name are the same"
                    print "pushSSIDName = ",setName
                    print "getSSIDName = ",finalName
                    print "TEST EXECUTION RESULT :SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP : Compare the pushSSID value and get values of SSID Name"
                    print "EXPECTED RESULT : Value pushed to hardware and get value of SSID Name should be the same"
                    print "ACTUAl RESULT : Value pushed to hardware and get value of SSID Name are NOT the same"
                    print "setSSIDName = ",setName
                    print "getSSIDName = ",finalName
                    print "TEST EXECUTION RESULT :FAILURE"

                #Revert the SSID NAme back o initial value
                apIndex = 0
                setMethod = "pushSSID"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'
                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialName, setMethod)

                if expectedresult in actualresult:
                    print "Successfully reverted back to initial value"
		    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "Unable to revert to initial value"
 		    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "wifi_getSSIDName() function failed"
 		tdkTestObj.setResultStatus("FAILURE");
        else:
            print "wifi_pushSSID function failed";
 	    tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getSSIDName function failed";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

