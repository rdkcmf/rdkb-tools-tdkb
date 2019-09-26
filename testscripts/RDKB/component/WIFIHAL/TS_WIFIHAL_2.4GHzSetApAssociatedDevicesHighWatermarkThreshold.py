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
  <name>TS_WIFIHAL_2.4GHzSetApAssociatedDevicesHighWatermarkThreshold</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the  ApAssociatedDevicesHighWatermarkThreshold for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_161</test_case_id>
    <test_objective>To set and get the ApAssociatedDevicesHighWatermarkThreshold for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDevicesHighWatermarkThreshold()
wifi_setApAssociatedDevicesHighWatermarkThreshold()</api_or_interface_used>
    <input_parameters>methodName : getApAssociatedDevicesHighWatermarkThreshold
methodName : setApAssociatedDevicesHighWatermarkThreshold
ApIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamUIntValue invoke wifi_getApAssociatedDevicesHighWatermarkThreshold() and save the get value
3. Choose a threshpold value less than maxAssociatedDevice and using  WIFIHAL_GetOrSetParamUIntValue invoke wifi_setApAssociatedDevicesHighWatermarkThreshold()
4. Invoke wifi_getApAssociatedDevicesHighWatermarkThreshold() to get the previously set value. 
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the WatermarkThreshold back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of WatermarkThreshold should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApAssociatedDevicesHighWatermarkThreshold</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApAssociatedDevicesHighWatermarkThreshold');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 0
    getMethod = "getApAssociatedDevicesHighWatermarkThreshold"
    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

    if expectedresult in actualresult:
	initThreshold = details.split(":")[1].strip()

	#The HighWatermarkThreshold value that is lesser than or equal to MaxAssociatedDevices
        getMethodToCheck = "getApMaxAssociatedDevices"
	apIndex = 0
	primitive = 'WIFIHAL_GetOrSetParamUIntValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethodToCheck)

        if expectedresult in actualresult:
            maxAssociatedDevice = details.split(":")[1].strip()

	    r = range(0,int(maxAssociatedDevice))
            setThreshold = random.choice(r)

            expectedresult="SUCCESS";
	    apIndex = 0
	    setMethod = "setApAssociatedDevicesHighWatermarkThreshold"
	    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setThreshold, setMethod)

	    if expectedresult in actualresult:
	        expectedresult="SUCCESS";
	        apIndex = 0
	        getMethod = "getApAssociatedDevicesHighWatermarkThreshold"
	        primitive = 'WIFIHAL_GetOrSetParamUIntValue'

	        #Calling the method from wifiUtility to execute test case and set result status for the test.
	        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

                if expectedresult in actualresult:
                    finalThreshold = details.split(":")[1].strip()
                    if int(finalThreshold) == setThreshold:
                        print "TEST STEP: Comparing set and get values of ApAssociatedDevicesHighWatermarkThreshold"
                        print "EXPECTED RESULT: Set and get values should be the same"
                        print "ACTUAL RESULT : Set and get values are the same"
                        print "Set value: %s"%setThreshold
                        print "Get value: %s"%finalThreshold
                        print "TEST EXECUTION RESULT :SUCCESS"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "TEST STEP: Comparing set and get values of ApAssociatedDevicesHighWatermarkThreshold"
                        print "EXPECTED RESULT: Set and get values should be the same"
                        print "ACTUAL RESULT : Set and get values are NOT the same"
                        print "Set value: %s"%setThreshold
                        print "Get value: %s"%finalThreshold
                        print "TEST EXECUTION RESULT :FAILURE"
                        tdkTestObj.setResultStatus("FAILURE");

                    #Revert back to initial value
                    setMethod = "setApAssociatedDevicesHighWatermarkThreshold"
                    primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                    setThreshold = int(initThreshold)
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setThreshold, setMethod)

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Successfully reverted back to inital value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to revert to initial value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "getApAssociatedDevicesHighWatermarkThreshold() function call failed after set operation"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "setApAssociatedDevicesHighWatermarkThreshold() function call failed"
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "getApMaxAssociatedDevices() function call failed"	
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "getApAssociatedDevicesHighWatermarkThreshold() function call failed"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
	 
