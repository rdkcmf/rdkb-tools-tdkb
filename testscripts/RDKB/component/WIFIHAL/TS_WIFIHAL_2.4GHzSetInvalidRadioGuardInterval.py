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
  <name>TS_WIFIHAL_2.4GHzSetInvalidRadioGuardInterval</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set radio guard interval to a value that is not in possible guard interval list and check whether it is set for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_221</test_case_id>
    <test_objective>To set radio guard interval to a value that is not in possible guard interval list and check whether it is set for 2.4GHz</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioGuardInterval
wifi_setRadioGuardInterval</api_or_interface_used>
    <input_parameters>methodName: getRadioGuardInterval
methodName: setRadioGuardInterval
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using getRadioGuardInterval get and save current GuardInterval
3.Set the GuardInterval using setRadioGuardInterval()
4.Get the above set value using getRadioGuardInterval
5. Verify whether the set and get values are the same.
6. Revert back to the initial GuardInterval
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of the guard interval should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL
</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetInvalidRadioGuardInterval</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetInvalidRadioGuardInterval');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    possibleGuardInt = ["400nsec", "800nsec", "Auto"];
    setGuardIntInvalid = "100nsec"

    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getRadioGuardInterval"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method to execute wifi_getRadioGuardInterval()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
    initialGuardInt = details.split(":")[1].strip()
    if expectedresult in actualresult and initialGuardInt in possibleGuardInt:
        tdkTestObj.setResultStatus("SUCCESS");
        setMethod = "setRadioGuardInterval"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'
	#Calling the method to execute wifi_setRadioGuardInterval()
	tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setGuardIntInvalid, setMethod)
        expectedresult = "FAILURE";
        radioIndex = 0
	if expectedresult in actualresult:
	    print "TEST STEP1: Set the RadioGuardInterval to a value not in possible guardinterval list"
            print "SET VALUE IS:",setGuardIntInvalid
            print "EXPECTED RESULT: Set operation should not be happen"
	    print "ACTUAL RESULT: Set operation returns FAILURE"
	    print "TEST EXECUTION RESULT : SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");
        else:
	    print "TEST STEP1: Set the RadioGuardInterval to a value not in possible guardinterval list"
            print "SET VALUE IS:",setGuardIntInvalid
            print "EXPECTED RESULT: Set operation should not be happen"
	    print "ACTUAL RESULT: Set operation returns SUCCESS"
	    print "TEST EXECUTION RESULT : FAILURE"
            tdkTestObj.setResultStatus("FAILURE");

            #Calling the method to execute wifi_getRadioGuardInterval()to check whether set has done
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
            getGuardInt = details.split(":")[1].strip()
            if getGuardInt == setGuardIntInvalid:

	        #Revert the guard interval back to initial value
	        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initialGuardInt, setMethod)
                expectedresult = "SUCCESS";
	        if expectedresult in actualresult:
                    print "Successfully reverted back to initial value"
		    tdkTestObj.setResultStatus("SUCCESS");
	        else:
                    print "Unable to revert to initial value"
                    tdkTestObj.setResultStatus("FAILURE");
	    else:
                print "HAL API setRadioGuardInterval() returns false SUCCESS"
	        tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getRadioGuardInterval() call failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

