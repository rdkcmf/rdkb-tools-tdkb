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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_platform_stub_hal_SNMPOnboardReboot_InvalidInput</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_SetSNMPOnboardRebootEnable</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the SNMPOnboardRebootEnable with invalid argument and check its behaviour</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_HAL_PLATFORM_62</test_case_id>
    <test_objective>This test case is to set the SNMPOnboardRebootEnable with invalid argument and check its behaviour</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_stub_hal_SetSNMPOnboardRebootEnable</api_or_interface_used>
    <input_parameters>SNMPonboard</input_parameters>
    <automation_approch>1.Load the module
2. Call the platform_hal_SetSNMPOnboardRebootEnable api with the invalid input parameter
3.The api  is expected to fail and the result is displayed accordingly.
4.Unload the Module</automation_approch>
    <expected_output>platform_hal_SetSNMPOnboardRebootEnable api should fail with a invalid input parameter</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFORM</test_stub_interface>
    <test_script>TS_platform_stub_hal_SNMPOnboardReboot_InvalidInput</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SNMPOnboardReboot_InvalidInput');
#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();

if "SUCCESS" in result.upper():
   obj.setLoadModuleStatus("SUCCESS");
   #Prmitive test case which associated to this Script
   tdkTestObj = obj.createTestStep('platform_stub_hal_SetSNMPOnboardRebootEnable');
   expectedresult ="FAILURE"
   setValue ="Invalid"
   tdkTestObj.addParameter("SNMPonboard",setValue)
   #Execute the test case in DUT
   tdkTestObj.executeTestCase("expectedresult");
   #Get the result of execution
   actualresult = tdkTestObj.getResult();
   details = tdkTestObj.getResultDetails();
   if expectedresult in actualresult:
      print" TEST STEP 1: Set the SetSNMPOnboardRebootEnable with Invalid Value";
      print" EXPECTED  RESULT 1: Should not set the SetSNMPOnboardRebootEnable";
      print" ACTUAL RESULT 1: %s" %details
      print "[TEST EXECUTION RESULT] : SUCCESS";
      tdkTestObj.setResultStatus("SUCCESS");
   else:
       print" TEST STEP 1: Set the SetSNMPOnboardRebootEnable with Invalid Value";
       print" EXPECTED  RESULT 1: Should not set the SetSNMPOnboardRebootEnable";
       print" ACTUAL RESULT 1: %s" %details
       print "[TEST EXECUTION RESULT] : FAILURE";
       tdkTestObj.setResultStatus("FAILURE");
   obj.unloadModule("halplatform");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
