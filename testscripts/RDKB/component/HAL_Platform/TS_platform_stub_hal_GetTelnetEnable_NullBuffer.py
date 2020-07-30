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
  <version>2</version>
  <name>TS_platform_stub_hal_GetTelnetEnable_NullBuffer</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_GetTelnetEnable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate Platform HAL API platform_hal_GetTelnetEnable() by passing a Null Buffer</synopsis>
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
    <test_case_id>TC_HAL_Platform_57</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_GetTelnetEnable() by passing a Null Buffer</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_GetTelnetEnable()</api_or_interface_used>
    <input_parameters>NullBuffer</input_parameters>
    <automation_approch>1.Load halplatform module
2. Invoke the HAL api platform_hal_GetTelnetEnable() by passing a null buffer
3. HAL API is expected to return failure status and the value should not be retrieved because null buffer was passed as an argument
4. UnLoad halplatform module</automation_approch>
    <expected_output>Call to platform_hal_GetTelnetEnable api should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>halplatform</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetTelnetEnable_NullBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetTelnetEnable_NullBuffer');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetTelnetEnable");
        expectedresult="FAILURE";
        tdkTestObj.addParameter("flag",1);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 1: Retrieve the Platform_GetTelnetEnable with NULL buffer";
           print "EXPECTED RESULT 1: Should not retrieve the Platform_GetTelnetEnable  with NULL buffer";
           print "ACTUAL RESULT 1: Platform_GetTelnetEnable api call failed";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Retrieve the Platform_GetTelnetEnable with NULL buffer";
            print "EXPECTED RESULT 1: Should not retrieve the Platform_GetTelnetEnable  with NULL buffer";
            print "ACTUAL RESULT 1: Platform_GetTelnetEnable api call success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        obj.unloadModule("halplatform");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
