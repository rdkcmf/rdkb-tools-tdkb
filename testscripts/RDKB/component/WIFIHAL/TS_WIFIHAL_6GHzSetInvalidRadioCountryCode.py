##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>2</version>
  <name>TS_WIFIHAL_6GHzSetInvalidRadioCountryCode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setRadioCountryCode() and check if setting an invalid value as the country code returns failure for 6G radio.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_719</test_case_id>
    <test_objective>Invoke the HAL API wifi_setRadioCountryCode() and check if setting an invalid value as the country code returns failure for 6G radio.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioCountryCode()
wifi_getRadioCountryCode() </api_or_interface_used>
    <input_parameters>methodname : getRadioCountryCode
radioIndex : 6G radio index
param : invalid_code - ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Invoke the HAL API wifi_getRadioCountryCode()  and retrieve the initial radio country code.
3. Set the radio country code to an invalid value using the HAL API wifi_setRadioCountryCode() and check if the set operation fails.
4. Get the current radio country code using wifi_getRadioCountryCode() and verify if it remains unchanged from the initial value.
5. In case the country code set returns success perform the revert operation.
6. Unload the module</automation_approch>
    <expected_output>Setting an invalid radio country code for 6G radio using the HAL API wifi_setRadioCountryCode() should fail and should not get reflected in the get API wifi_getRadioCountryCode().</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetInvalidRadioCountryCode</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetInvalidRadioCountryCode');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned

    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get initial radio country code
        expectedresult="SUCCESS";
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamStringValue');
        tdkTestObj.addParameter("methodName","getRadioCountryCode");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getRadioCountryCode()for 6G radio";
        print "EXPECTED RESULT 1 : The HAL API wifi_getRadioCountryCode() should be invoked successfully for 6G radio";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API invocation is success; Details : %s" %details;
            print "TEST EXECUTION RESULT : SUCCESS"
            countryCode = details.split(":")[1].strip()

            if countryCode != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "Country Code returned is non-empty : %s"%countryCode;

                #Set an invalid radio country code
                revert_flag = 0;
                invalid_code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
                expectedresult = "FAILURE";
                tdkTestObj.addParameter("methodName","setRadioCountryCode");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.executeTestCase(expectedresult);
                tdkTestObj.addParameter("param", invalid_code);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 2: Invoke the HAL API wifi_setRadioCountryCode() for 6G radio and set an invalid country code : %s" %invalid_code;
                print "EXPECTED RESULT 2 : The HAL API wifi_setRadioCountryCode() should return failure for invalid country code";

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 2: API returns failure for invalid country code; Details : %s" %details;
                    print "TEST EXECUTION RESULT : SUCCESS"
                else:
                    revert_flag = 1;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 2: API returns success for invalid country code; Details : %s" %details;
                    print "TEST EXECUTION RESULT : FAILURE"

                #Check if the country code remains unchanged with get operation
                expectedresult = "SUCCESS";
                tdkTestObj.addParameter("methodName","getRadioCountryCode");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 3: Check if the HAL API wifi_getRadioCountryCode() returns the initial country code after the invalid set operation";
                print "EXPECTED RESULT 3 : The HAL API wifi_getRadioCountryCode() should return country code unchanged from initial value";

                if expectedresult in actualresult :
                    curr_countryCode = details.split(":")[1].strip();
                    print "Current country code : %s" %curr_countryCode;
                    print "Initial country code : %s" %countryCode;

                    if curr_countryCode == countryCode:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3: Country code remains unchanged; Details : %s" %details;
                        print "TEST EXECUTION RESULT : SUCCESS"
                    else:
                        revert_flag = 1;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3: Country code does not remain unchanged; Details : %s" %details;
                        print "TEST EXECUTION RESULT : FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: API invocation failed; Details : %s" %details;
                    print "TEST EXECUTION RESULT : FAILURE"

                #Revert operation
                if revert_flag == 1:
                    expectedresult = "SUCCESS";
                    tdkTestObj.addParameter("methodName","setRadioCountryCode");
                    tdkTestObj.addParameter("radioIndex",idx);
                    tdkTestObj.executeTestCase(expectedresult);
                    tdkTestObj.addParameter("param", countryCode);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Revert operation was successful";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "revert operation was not successful";
                else :
                    print "Revert operation not required";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Country Code returned is empty : %s"%countryCode;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            print "TEST EXECUTION RESULT : FAILURE"
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
