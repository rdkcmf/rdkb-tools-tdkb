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
  <version>13</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_platform_stub_hal_GetHardwareVersionNullBuffer</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_GetHardwareVersion</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate HAL API platform_hal_GetHardwareVersion() by passing null buffer</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_HAL_Platform_47</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_GetHardwareVersion() by passing null buffer</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_GetHardwareVersion()</api_or_interface_used>
    <input_parameters>flag - to indicate negative scenario</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_hal_GetHardwareVersion by pasing null buffer
3. HAL API is expected to return failure status and the value should not be retreived because null buffer was passed as an argument
4. Unload platform module</automation_approch>
    <expected_output>Value should not retrieved from HAL.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetHardwareVersionNullBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>none</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#Library functions
import tdklib;
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetHardwareVersionNullBuffer');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetHardwareVersion");
        tdkTestObj.addParameter("flag", 1);

        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the Platform_GetHardwareVersion on passing Null  buffer";
            print "EXPECTED RESULT 1: Should not retrieve the Platform_GetHardwareVersion on passing Null buffer";
            print "ACTUAL RESULT 1 : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Retrieve the Platform_GetHardwareVersion";
            print "EXPECTED RESULT 1: Should not retrieve the Platform_GetHardwareVersion on passing Null buffer";
            print "ACTUAL RESULT 1 : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        obj.unloadModule("halplatform");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
