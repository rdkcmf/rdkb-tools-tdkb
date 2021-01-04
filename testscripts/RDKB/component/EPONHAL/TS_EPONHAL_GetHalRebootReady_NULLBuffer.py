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
  <name>TS_EPONHAL_GetHalRebootReady_NULLBuffer</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetParamUlongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke Hal Reboot Ready api with a NULL buffer as parameter and check if the api crashes</synopsis>
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
    <test_case_id>TC_EPONHAL_28</test_case_id>
    <test_objective>Invoke Hal Reboot Ready api with a NULL buffer as parameter and check if the api crashes</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_hal_Reboot_Ready</api_or_interface_used>
    <input_parameters>NULL</input_parameters>
    <automation_approch>1. Load eponhal module
2.invoke dpoe_hal_Reboot_Ready() by passing a NULL buffer
3.Check if dpoe_hal_Reboot_Ready() returns failure when NULL Buffer is passed or whether it crashes
4. Unload eponhal module</automation_approch>
    <expected_output>dpoe_hal_Reboot_Ready() api should not crash with a NULL buffer as parameter</expected_output>
    <priority>High</priority>
    <test_stub_interface>eponhal</test_stub_interface>
    <test_script>TS_EPONHAL_GetHalRebootReady_NULLBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetHalRebootReady_NULLBuffer');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep('EPONHAL_GetParamUlongValue');
        tdkTestObj.addParameter("paramName","hal_Reboot_Ready");
        tdkTestObj.addParameter("paramType","NULL")
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the hal_Reboot_Ready status with NULL Buffer";
            print "EXPECTED RESULT 1: Should not retrieve the hal_Reboot_Ready status with NULL Buffer";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Retrieve the hal_Reboot_Ready status with NULL Buffer";
            print "EXPECTED RESULT 1: Should not retrieve the hal_Reboot_Ready status with NULL Buffer";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        obj.unloadModule("eponhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
