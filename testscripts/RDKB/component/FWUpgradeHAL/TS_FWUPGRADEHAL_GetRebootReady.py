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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_FWUPGRADEHAL_GetRebootReady</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>FWUPGRADEHAL_Reboot_Now</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke the HAL API fwupgrade_hal_reboot_ready(), retrieve the GetRebootReady and check if the value is in the expected list : [Ready, Not Ready]</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_FWUPGRADEHAL_05</test_case_id>
    <test_objective>Invoke the HAL API fwupgrade_hal_reboot_ready(), retrieve the GetRebootReady and check if the value is in the expected list : [Ready, Not Ready]</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>FWUPGRADEHAL_GetParamUlongValue</api_or_interface_used>
    <input_parameters>paramName : Reboot_Ready</input_parameters>
    <automation_approch>1. Load fwupgradehal module
2. Invoke the function FWUPGRADEHAL_GetParamUlongValue which will invoke the HAL API fwupgrade_hal_reboot_ready(), the Reboot Ready Status should be retrieved successfully and the value should be in expected list.
3. Unload fwupgradehal module</automation_approch>
    <expected_output>Invoke fwupgrade_hal_reboot_ready() HAL API and retrieve the Reboot ready status successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>fwupgradehal</test_stub_interface>
    <test_script>TS_FWUPGRADEHAL_GetRebootReady</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("fwupgradehal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_FWUPGRADEHAL_GetRebootReady');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("FWUPGRADEHAL_GetParamUlongValue");
    tdkTestObj.addParameter("paramName","Reboot_Ready");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    count = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Invoke the HAL API fwupgrade_hal_reboot_ready()";
        print "EXPECTED RESULT 1: Should successfully invoke fwupgrade_hal_reboot_ready()";
        print "ACTUAL RESULT 1: The API invocation is success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "Reboot Ready value : %s" %count;

        if count == "1":
            status="Ready";
        elif count == "2":
            status == "Not Ready";
        else:
            status = "Invalid Status";

        if count=="1" or count=="2":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Check if the GetRebootReady status in [Ready, Not Ready]";
            print "EXPECTED RESULT 2: The GetRebootReady status should be valid"
            print "ACTUAL RESULT 2: GetRebootReady status is  ",status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if the GetRebootReady status in [Ready, Not Ready]";
            print "EXPECTED RESULT 2: The GetRebootReady status should be valid"
            print "ACTUAL RESULT 2: GetRebootReady status is  ",status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Invoke the HAL API fwupgrade_hal_reboot_ready()";
        print "EXPECTED RESULT 1: Should successfully invoke fwupgrade_hal_reboot_ready()"
        print "ACTUAL RESULT 1: The API invocation is failure";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("fwupgradehal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
