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
  <version>3</version>
  <name>TS_platform_stub_hal_SetLowPowerModeState_InvalidState</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_SetLowPowerModeState</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke platform_hal_SetLowPowerModeState() with invalid state and check if the API returns failure as expected.</synopsis>
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
    <test_case_id>TC_HAL_Platform_88</test_case_id>
    <test_objective>To invoke platform_hal_SetLowPowerModeState() with invalid state and check if the API returns failure as expected.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetLowPowerModeState()</api_or_interface_used>
    <input_parameters>method : platform_stub_hal_SetLowPowerModeState</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_hal_SetLowPowerModeState() by passing the state value as an invalid value
3. The Set operation should be failed
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>On invoking platform_hal_SetLowPowerModeState() with invalid state, the API should return failure as expected.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetLowPowerModeState_InvalidState</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from random import randint;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetLowPowerModeState_InvalidState');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    # Generate invalid state(>5)
    x = randint(5,100);
    tdkTestObj = obj.createTestStep("platform_stub_hal_SetLowPowerModeState");
    #Invalid state is passed
    tdkTestObj.addParameter("state", x);
    expectedresult="FAILURE";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and details:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Set Low Power Mode state by invoking the HAL API platform_hal_SetLowPowerModeState with Invalid State";
        print "EXPECTED RESULT 1: platform_hal_SetLowPowerModeState not invoked successfully";
        print "ACTUAL RESULT 1: %s"%details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Set Low Power Mode state by invoking the HAL API platform_hal_SetLowPowerModeState with Invalid State";
        print "EXPECTED RESULT 1: platform_hal_SetLowPowerModeState not invoked successfully";
        print "ACTUAL RESULT 1: %s"%details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("halplatform");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

