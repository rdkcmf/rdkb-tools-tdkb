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
  <name>TS_FWUPGRADEHAL_Reboot_Now</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>FWUPGRADEHAL_Reboot_Now</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To reboot the device by invoking the HAL API fwupgrade_hal_download_reboot_now() and check if the uptime before reboot is greater than uptime after reboot.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <test_case_id>TC_FWUPGRADEHAL_07</test_case_id>
    <test_objective>To reboot the device by invoking the HAL API fwupgrade_hal_download_reboot_now() and check if the uptime before reboot is greater than uptime after reboot.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>FWUPGRADEHAL_Reboot_Now
pam_GetParameterValues</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.UpTime</input_parameters>
    <automation_approch>1. Load the fwupgradehal module
2. Invoke the function pam_GetParameterValues with input Device.DeviceInfo.UpTime and get the current device uptime.
3. Invoke the function FWUPGRADEHAL_Reboot_Now which will in turn invoke the HAL API fwupgrade_hal_download_reboot_now() to reboot the device. The device should be rebooted successfully.
4. Invoke the function pam_GetParameterValues with input Device.DeviceInfo.UpTime and get the device uptime. This value should be lesser than the previous uptime before reboot.
5. Unload the module</automation_approch>
    <expected_output>fwupgrade_hal_download_reboot_now() invocation should be success and the uptime before reboot is greater than uptime after reboot.</expected_output>
    <priority>High</priority>
    <test_stub_interface>fwupgradehal</test_stub_interface>
    <test_script>TS_FWUPGARDEHAL_Reboot_Now</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("fwupgradehal","1");
obj1 = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_FWUPGRADEHAL_Reboot_Now');
obj1.configureTestCase(ip,port,'TS_FWUPGRADEHAL_Reboot_Now');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    beforedetails = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 :Get the uptime with Device.DeviceInfo.UpTime";
        print "EXPECTED RESULT 1: Should return the uptime successfully";
        print "ACTUAL RESULT 1:UpTime before reboot is %s" %beforedetails;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #save device's current state before it goes for reboot
        obj1.saveCurrentState();
        tdkTestObj = obj.createTestStep("FWUPGRADEHAL_Reboot_Now");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        rebootdetails = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Start the reboot by invoking the HAL API fwupgrade_hal_download_reboot_now()";
            print "EXPECTED RESULT 2: Should start the reboot successfully";
            print "ACTUAL RESULT 2: %s" %rebootdetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #Restore the device state saved before reboot
            obj1.restorePreviousStateAfterReboot();

            #checking the uptime after reboot
            tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            afterdetails = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 :Get the uptime with Device.DeviceInfo.UpTime";
                print "EXPECTED RESULT 3: Should return the uptime successfully";
                print "ACTUAL RESULT 3:UpTime before reboot is %s" %afterdetails;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if int(beforedetails) >= int(afterdetails):
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Compare the uptime before and after reboot";
                    print "EXPECTED RESULT 4: Uptime before reboot should be greater than uptime after reboot";
                    print "ACTUAL RESULT 4: Uptime after reboot is %s" %afterdetails;
                    print "Successfully updated the uptime after reboot";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Compare the uptime before and after reboot";
                    print "EXPECTED RESULT 4: Uptime before reboot should be greater than uptime after reboot";
                    print "ACTUAL RESULT 4: UpTime after reboot is %s" %afterdetails;
                    print "Failed to update the uptime after reboot"
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 :Get the uptime with Device.DeviceInfo.UpTime";
                print "EXPECTED RESULT 3: Should return the uptime successfully";
                print "ACTUAL RESULT 3:UpTime before reboot is %s" %afterdetails;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Start the reboot by invoking the HAL API fwupgrade_hal_download_reboot_now()";
            print "EXPECTED RESULT 2: Should start the reboot successfully";
            print "ACTUAL RESULT 2: %s" %rebootdetails;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the UpTime with Device.DeviceInfo.UpTime";
        print "EXPECTED RESULT 1: Should return the uptime successfully";
        print "ACTUAL RESULT 1: Failed to get the uptime before reboot %s" %beforedetails;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("fwupgradehal");
    obj1.unloadModule("pam");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading Failed";

