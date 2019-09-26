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
  <name>TS_WIFIHAL_2.4GHzSet4DigitApWpsDevicePIN</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the ApWpsDevicePIN to a 4 digit value and check whether it is allow to set for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_219</test_case_id>
    <test_objective>To set the  WpsDevicePIN to a 4 digit value and check whether it is set for 2.4GHz</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsDevicePIN()
wifi_setApWpsDevicePIN()</api_or_interface_used>
    <input_parameters>methodName : getApWpsDevicePIN
methodName : setApWpsDevicePIN
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_getApWpsDevicePIN() and save the initial value
3. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_setApWpsDevicePIN() and set a value with 4 digit.
4. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_getApWpsDevicePIN() and get the previously set value
5. If the set and get values are the same, return FAILURE, else return SUCCESS
6. Revert to initial value if set operation is success
7. Unload wifihal module</automation_approch>
    <except_output>Set operation should not be happen since it is a invalid number of digits</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSet4DigitApWpsDevicePIN</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSet4DigitApWpsDevicePIN');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #get the ApWpsDevicePIN
    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getApWpsDevicePIN"
    primitive = 'WIFIHAL_GetOrSetParamULongValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult :
        initPIN = int(details.split(":")[1].strip())
        #set the ApWpsDevicePIN
        expectedresult="FAILURE";
        radioIndex = 0
        setMethod = "setApWpsDevicePIN"
        setPIN = 1234
        primitive = 'WIFIHAL_GetOrSetParamULongValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setPIN, setMethod)
        if expectedresult in actualresult :
	    print "TEST STEP 1: Set the DevicePIN to a 4 digit Value"
            print "SET VALUE IS :",setPIN
            print "EXPECTED RESULT : DevicePIN set operation should not happen"
            print "ACTUAL RESULT :Set operation returns FAILURE"
	    print "TEST EXECUTION RESULT: SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");

        else:
            print "TEST STEP 2: Set the DevicePIN to a 4 Digit value"
            print "SET VALUE IS :",setPIN
            print "EXPECTED RESULT : DevicePIN set operation should not happen"
            print "ACTUAL RESULT :Set operation returns SUCCESS"
            print "TEST EXECUTION RESULT: FAILURE"
            tdkTestObj.setResultStatus("FAILURE");

            #check whether "setApWpsDevicePIN" not returns false success
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
            getPIN = int(details.split(":")[1].strip())

            if getPIN == setPIN:
                #Revert the pin to initial value
                expectedresult = "SUCCESS";
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initPIN, setMethod)
                if expectedresult in actualresult :
                    print "Successfully reverted to initial pin"
                    tdkTestObj.setResultStatus("SUCCESS");

                else:
                    print "Unable to revert to initial value"
                    tdkTestObj.setResultStatus("FAILURE");

            else:
                print "HAL API setApWpsDevicePIN() returns false success"
                tdkTestObj.setResultStatus("FAILURE");
    else:
        print "getApWpsDevicePIN() call failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

