##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzSetInvalidRadioCountryCode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if a country code more than 64 char can be set to wifi_setRadioCountryCode api</synopsis>
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
    <test_case_id>TC_WIFIHAL_454</test_case_id>
    <test_objective>This test case is to check if a country code more than 64 char can be set to wifi_setRadioCountryCode api</test_objective>
    <test_type>Negative</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioCountryCode
wifi_getRadioCountryCode</api_or_interface_used>
    <input_parameters>radioindex
country code</input_parameters>
    <automation_approch>1.Load the module
2.Get the current country code
3.Set a invalid country code of characters greater than 64.
4.The test should return failure and appropriate result should be printed.
5.unload the module</automation_approch>
    <expected_output>The wifi_setRadioCountryCode api call should fail when a country code greater than 64  chars is set </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetInvalidRadioCountryCode</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetInvalidRadioCountryCode');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
countryCode = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
            expectedresult="SUCCESS";
            radioIndex = idx;
            getMethod = "getRadioCountryCode"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

            if expectedresult in actualresult:
                #Script to load the configuration file of the component
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                tdkTestObj.addParameter("methodName","setRadioCountryCode")
                #Radio index is 0 for 2.4GHz and 1 for 5GHz
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.addParameter("param", countryCode);
                expectedresult="FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    print "TEST STEP : Set a invalid country code like %s for wifi_setRadioCountryCode api" %countryCode;
                    print "EXPECTED RESULT : Set call with a invalid country code should fail";
                    print "ACTUAL RESULT 1: %s" %details;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "TEST STEP : Set a invalid country code like %s for wifi_setRadioCountryCode api" %countryCode;
                    print "EXPECTED RESULT : Set call with a invalid country code should fail";
                    print "ACTUAL RESULT 1: %s" %details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "getRadioCountryCode() call failed"
                tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
