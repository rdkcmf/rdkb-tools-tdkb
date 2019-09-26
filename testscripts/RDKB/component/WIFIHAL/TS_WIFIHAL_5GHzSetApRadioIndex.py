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
  <name>TS_WIFIHAL_5GHzSetApRadioIndex</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the radioIndex of an odd number of access point to 0</synopsis>
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
    <test_case_id>TC_WIFIHAL_257</test_case_id>
    <test_objective>To set the radioIndex of an odd number of access point to 0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApRadioIndex()
wifi_setApRadioIndex()</api_or_interface_used>
    <input_parameters>methodName : getApRadioIndex
methodName : setApRadioIndex
apIndex : 11</input_parameters>
    <automation_approch>1.Load the module.
2.Using WIFIHAL_GetOrSetParamIntValue invoke wifi_getApRadioIndex for Ap 11.
3. Invoke  wifi_setApRadioIndex and set the radioIndex to 0
4. Again invoke wifi_getApRadioIndex  to get the previously set index value.
5. If set and get values are the same, return SUCCESS,else return FAILURE.
6.Unload module.</automation_approch>
    <except_output>Set and get values should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApRadioIndex</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApRadioIndex');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Checking for apIndex 1, Similary can be check for other APs 1,3,5,7,9,11,13,15
    expectedresult="SUCCESS";
    apIndex = 11
    getMethod = "getApRadioIndex"
    primitive = 'WIFIHAL_GetOrSetParamIntValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

    if expectedresult in actualresult:
        initRadioIndex = details.split(":")[1].strip()
        expectedresult="SUCCESS";
        apIndex = 11
        setMethod = "setApRadioIndex"
        setRadioIndex = 0
        primitive = 'WIFIHAL_GetOrSetParamIntValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setRadioIndex, setMethod)

        if expectedresult in actualresult:
            expectedresult="SUCCESS";
            apIndex = 11
            getMethod = "getApRadioIndex"
            primitive = 'WIFIHAL_GetOrSetParamIntValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

            if expectedresult in actualresult:
                finalRadioIndex = details.split(":")[1].strip()
                if int(finalRadioIndex) == setRadioIndex:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP: Compare the set and get radio index for the access point %s"%apIndex
                    print "EXPECTED RESULT: Set and get radio index should be the same"
                    print "ACTUAL RESULT: Set and get radio index are the SAME for access point %s"%apIndex
                    print "Set RadioIndex = %s"%setRadioIndex
                    print "Get RadioIndex = %s"%finalRadioIndex
                    print "TEST EXECUTION RESULT: SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP: Compare the set and get radio index for the access point %s"%apIndex
                    print "EXPECTED RESULT: Set and get radio index should be the same"
                    print "ACTUAL RESULT: Set and get radio index are NOT SAME for access point %s"%apIndex
                    print "Set RadioIndex = %s"%setRadioIndex
                    print "Get RadioIndex = %s"%finalRadioIndex
                    print "TEST EXECUTION RESULT: FAILURE"
            else:
                print "getApRadioIndex() call failed after set operation"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "setApRadioIndex() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "getApRadioIndex() call failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

