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
  <name>TS_WIFIHAL_2.4GHzSetRadioCountryCode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the RadioCountryCode for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_245</test_case_id>
    <test_objective>To set and get the RadioCountryCode for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioCountryCode()
wifi_setRadioCountryCode()</api_or_interface_used>
    <input_parameters>methodName : getRadioCountryCode
methodName : setRadioCountryCode
radioIndex : 0</input_parameters>
    <automation_approch>1.Load the module
2.Get the Radio Country Code using wifi_getRadioCountryCode() API.
3.Set the Radio Country Code to another value using wifi_setRadioCountryCode() API.
4.Get the value and check whether getting the previously set value.
5.If get and set values are same,return SUCCESS else FAILURE.
6.Unload the module.</automation_approch>
    <except_output>Get and set values for RadioCountryCode should be same.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioCountryCode</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioCountryCode');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getRadioCountryCode"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

    if expectedresult in actualresult:
        countryCode = details.split(":")[1].strip()

        expectedresult="SUCCESS";
        radioIndex = 0
        setMethod = "setRadioCountryCode"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, countryCode, setMethod)

        if expectedresult in actualresult:
            expectedresult="SUCCESS";
            radioIndex = 0
            getMethod = "getRadioCountryCode"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

            if expectedresult in actualresult:
                setCode = details.split(":")[1].strip()
                if setCode == countryCode:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP: Compare the set and get Radio Country Codes for 2.4GHz"
                    print "EXPECTED RESULT: Set and get Country Codes should be the same"
                    print "ACTUAL RESULT: Set ang get Country Codes are the SAME"
                    print "Initial Country Code is %s"%countryCode
                    print "Newly set Country Code is %s"%setCode
                    print "TEST EXECUTION RESULT : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP: Compare the set and get Radio Country Codes for 2.4GHz"
                    print "EXPECTED RESULT: Set and get Country Codes should be the same"
                    print "ACTUAL RESULT: Set ang get Country Codes are NOT SAME"
                    print "Initial Country Code is %s"%countryCode
                    print "Newly set Country Code is %s"%setCode
                    print "TEST EXECUTION RESULT : FAILURE"
            else:
                print "getRadioCountryCode() call failed after set operation"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "setRadioCountryCode() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "getRadioCountryCode() call failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

