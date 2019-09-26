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
  <name>TS_WIFIHAL_5GHzSetApMaxAssociatedDevices</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get and set the ApMax Associated Devices value for 5GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_244</test_case_id>
    <test_objective>To get and set the ApMax Associated Devices value for 5GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApMaxAssociatedDevices()
wifi_setApMaxAssociatedDevices()</api_or_interface_used>
    <input_parameters>methodName : getApMaxAssociatedDevices
methodName : setApMaxAssociatedDevices
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get Ap Max Associated Devices using wifi_getApMaxAssociatedDevices() API.
3.Set Ap Max Associated Devices to a new value using wifi_setApMaxAssociatedDevices() API.
4.Get the previously set value.
5.If get and set values are same,return SUCCESS else FAILURE.
6.Revert the Ap Max Associated Devices value to initial value.
7.Unload the module.</automation_approch>
    <except_output>Set and get values should be same.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApMaxAssociatedDevices</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApMaxAssociatedDevices');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getApMaxAssociatedDevices"
    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    initialApMaxAssociatedDevices = int(details.split(":")[1])

    if expectedresult in actualresult:
	expectedresult="SUCCESS";
	radioIndex = 1
	primitive = 'WIFIHAL_GetOrSetParamUIntValue'
	setMethod = "setApMaxAssociatedDevices"
	setApMaxAssociatedDevicesValue  = random.randint(1,200)
	print "setApMaxAssociatedDevicesValue = ",setApMaxAssociatedDevicesValue

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setApMaxAssociatedDevicesValue, setMethod)

	if expectedresult in actualresult:
	    expectedresult="SUCCESS";
	    radioIndex = 1
	    getMethod = "getApMaxAssociatedDevices"
	    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	    getApMaxAssociatedDevicesValue = int(details.split(":")[1])

	    if expectedresult in actualresult:
		if getApMaxAssociatedDevicesValue == setApMaxAssociatedDevicesValue:
		    print "TEST STEP : Comparing the set and get values of ApMax Associated Devices"
		    print "EXPECTED RESULT : Set and get values should be the same"
		    print "ACTUAL RESULT : Set and get values are the same"
		    print "TEST EXECUTION RESULT : SUCCESS"
		    tdkTestObj.setResultStatus("SUCCESS");

	        else:
		    print "TEST STEP : Comparing the set and get values of ApMax Associated Devices"
		    print "EXPECTED RESULT : Set and get values should be the same"
		    print "ACTUAL RESULT : Set and get values are NOT the same"
		    print "TEST EXECUTION RESULT : FAILURE"
		    tdkTestObj.setResultStatus("FAILURE");
		#Revert back the ApMax Associated Devices to initial value
	        expectedresult="SUCCESS";
	        radioIndex = 1
	        setMethod = "setApMaxAssociatedDevices"
	        primitive = 'WIFIHAL_GetOrSetParamUIntValue'

                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initialApMaxAssociatedDevices, setMethod)

		if expectedresult in actualresult:
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "Successfully reverted back to default value"
		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print" Unable to revert to default value"

	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "getApMaxAssociatedDevices function failed";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "setApMaxAssociatedDevices function failed";

    else:
        print "getApMaxAssociatedDevices function failed";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
