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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_ModeChanges_OnlyAfterReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check whether RBUS mode changes take effects only after reboot</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>45</execution_time>
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
    <test_case_id>TC_RBUS_8</test_case_id>
    <test_objective>To check whether RBUS mode changes take effects only after reboot </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil Modules
2. Get the RBUS enable status value and store it
3. If the RBUS was enabled initially, Set the RBUS enable status to False
4. Get the RBUS Enable status, the value should be false and rbus process should be running since DUT was not rebooted
5. Reboot the DUT and check the RBUS Enable status, now the value should be false and RBUS process should not be running
6. If the RBUS was disabled initially, Set the RBUS enable status to True
7. Get the RBUS Enable status, the value should be false and RBUS process should not be running since DUT was not rebooted
8. Reboot the DUT and check the RBUS Enable status, now the value should be True and RBUS process should be running
9. Revert the value of RBUS Enable status to its initial value
10. Unload the modules</automation_approch>
    <expected_output>RBUS enable status changes should take effect only after the reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_ModeChanges_OnlyAfterReboot</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbRBUS_Utility import *;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RBUS_ModeChanges_OnlyAfterReboot');
tr181obj.configureTestCase(ip,port,'TS_RBUS_ModeChanges_OnlyAfterReboot');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    rbus_enabled = 0;
    revertFlag = 0;
    parameter_Name = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable";

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');

    #Check RBUS is Enabled / Disabled
    def_result, default_value = isRBUSEnabled(tdkTestObj_Tr181_Get);

    if expectedresult in def_result:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Enable Status of RBUS"
        print "EXPECTED RESULT 1: Should Get the Enable Status of RBUS"
        print "ACTUAL RESULT 1: RBUS Enable Status retrieved successfully"
        print "[TEST EXECUTION RESULT] 1: SUCCESS";

        print "Initial RBUS Enabled Status is",default_value

        if default_value == "true":
            set_result, set_details = setTR181Value(tdkTestObj_Tr181_Set,parameter_Name,"false","bool");
            if expectedresult  in set_result:
                revertFlag = 1	;
                print "TEST STEP 2: Set RBUS Enable Status value to false",;
                print "EXPECTED RESULT 2:  Set Operation should be success";
                print "ACTUAL RESULT 2: Set operation was success";
                print "[TEST EXECUTION RESULT] 2: SUCCESS";
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

                get_result,get_details = getTR181Value(tdkTestObj_Tr181_Get,parameter_Name);
                print "Value of RBUS enable status is ",get_details

                if expectedresult  in get_result and get_details == default_value:
                    print "TEST STEP 3: Get the Enable Status of RBUS ";
                    print "EXPECTED RESULT 3: Enable Status value should be equal to default_value";
                    print "ACTUAL RESULT 3: RBUS Enable status is still showing default value"
                    print "[TEST EXECUTION RESULT] 3: SUCCESS";
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

                    actualresult,pid_value = getPID(tdkTestObj_Sys_ExeCmd,"rbus_session_mgr");
                    if expectedresult  in actualresult and pid_value != "":
                        print "TEST STEP 4: Get the PID of RBUS";
                        print "EXPECTED RESULT 4:  Should get the PID value of RBUS";
                        print "ACTUAL RESULT 4: Successfully got the PID value, PID:",pid_value;
                        print "[TEST EXECUTION RESULT] 4: SUCCESS";
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");

                        #Reboot the DUT
                        doRebootDUT(sysobj);
                        get_result,get_details = getTR181Value(tdkTestObj_Tr181_Get,parameter_Name);
                        print "Value of RBUS enable status After Reboot is ",get_details

                        if expectedresult  in get_result and get_details == "false":
                            print "TEST STEP 5: Get the Enable Status of RBUS ";
                            print "EXPECTED RESULT 5: Enable Status value should be changed to new value";
                            print "ACTUAL RESULT 5: RBUS Enable status is changed to new value"
                            print "[TEST EXECUTION RESULT] 5: SUCCESS";
                            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

                            actualresult,pid_value = getPID(tdkTestObj_Sys_ExeCmd,"rbus_session_mgr");
                            if expectedresult  in actualresult and pid_value == "":
                                print "TEST STEP 6: Get the PID of RBUS to check RBUS is Running or NOT";
                                print "EXPECTED RESULT 6: RBUS process should not be running";
                                print "ACTUAL RESULT 6: RBUS is not Running after Reboot"
                                print "[TEST EXECUTION RESULT] 6: SUCCESS";
                                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                            else:
                                print "TEST STEP 6: Get the PID of RBUS to check RBUS is Running or NOT";
                                print "EXPECTED RESULT 6: RBUS process should not be running";
                                print "ACTUAL RESULT 6: RBUS is Running after Reboot"
                                print "[TEST EXECUTION RESULT] 6: FAILURE";
                                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                        else:
                            print "TEST STEP 5: Get the Enable Status of RBUS ";
                            print "EXPECTED RESULT 5: Enable Status value should be changed to new value";
                            print "ACTUAL RESULT 5: RBUS Enable status is NOT changed to new value"
                            print "[TEST EXECUTION RESULT] 5: FAILURE";
                            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                    else:
                        print "TEST STEP 4: Get the PID of RBUS";
                        print "EXPECTED RESULT 4:  Should get the PID value of RBUS";
                        print "ACTUAL RESULT 4: Failed to get the PID value"
                        print "[TEST EXECUTION RESULT] 4: FAILURE";
                        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                else:
                    print "TEST STEP 3: Get the Enable Status of RBUS ";
                    print "EXPECTED RESULT 3: Enable Status value should be equal to default_value";
                    print "ACTUAL RESULT 3: RBUS Enable status is changed to new value"
                    print "[TEST EXECUTION RESULT] 3: FAILURE";
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            else:
                print "TEST STEP 2: Set RBUS Enable Status value to false",;
                print "EXPECTED RESULT 2:  Set Operation should be success";
                print "ACTUAL RESULT 2: Set operation was Failed";
                print "[TEST EXECUTION RESULT] 2: FAILURE";
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        else:
            set_result, set_details = setTR181Value(tdkTestObj_Tr181_Set,parameter_Name,"true","bool");
            if expectedresult  in set_result:
                print "TEST STEP 2: Set RBUS Enable Status value to True",;
                print "EXPECTED RESULT 2:  Set Operation should be success";
                print "ACTUAL RESULT 2: Set operation was success";
                print "[TEST EXECUTION RESULT] 2: SUCCESS";
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

                get_result,get_details = getTR181Value(tdkTestObj_Tr181_Get,parameter_Name);
                print "Value of RBUS enable status is ",get_details

                if expectedresult  in get_result and get_details == default_value:
                    print "TEST STEP 3: Get the Enable Status of RBUS ";
                    print "EXPECTED RESULT 3: Enable Status value should be equal to default_value";
                    print "ACTUAL RESULT 3: RBUS Enable status is still showing default value"
                    print "[TEST EXECUTION RESULT] 3: SUCCESS";
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

                    actualresult,pid_value = getPID(tdkTestObj_Sys_ExeCmd,"rbus_session_mgr");
                    if expectedresult  in actualresult and pid_value == "":
                        print "TEST STEP 4: Get the PID of RBUS to check RBUS is not running";
                        print "EXPECTED RESULT 4: RBUS should not be running";
                        print "ACTUAL RESULT 4: RBUS process is not running";
                        print "[TEST EXECUTION RESULT] 4: SUCCESS";
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");

                        #Reboot the DUT
                        doRebootDUT(sysobj);
                        get_result,get_details = getTR181Value(tdkTestObj_Tr181_Get,parameter_Name);
                        print "Value of RBUS enable status After Reboot is ",get_details

                        if expectedresult  in get_result and get_details == "true":
                            print "TEST STEP 5: Get the Enable Status of RBUS ";
                            print "EXPECTED RESULT 5: Enable Status value should be changed to new value";
                            print "ACTUAL RESULT 5: RBUS Enable status is changed to new value"
                            print "[TEST EXECUTION RESULT] 5: SUCCESS";
                            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

                            actualresult,pid_value = getPID(tdkTestObj_Sys_ExeCmd,"rbus_session_mgr");
                            if expectedresult  in actualresult and pid_value != "":
                                print "TEST STEP 6: Get the PID of RBUS to check RBUS is Running or NOT";
                                print "EXPECTED RESULT 6: RBUS process should be running";
                                print "ACTUAL RESULT 6: Successfully got the PID value, PID:",pid_value;
                                print "[TEST EXECUTION RESULT] 6: SUCCESS";
                                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                            else:
                                print "TEST STEP 6: Get the PID of RBUS to check RBUS is Running or NOT";
                                print "EXPECTED RESULT 6: RBUS process should not be running";
                                print "ACTUAL RESULT 6: RBUS is not Running after Reboot"
                                print "[TEST EXECUTION RESULT] 6: FAILURE";
                                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                        else:
                            print "TEST STEP 5: Get the Enable Status of RBUS ";
                            print "EXPECTED RESULT 5: Enable Status value should be changed to new value";
                            print "ACTUAL RESULT 5: RBUS Enable status is NOT changed to new value"
                            print "[TEST EXECUTION RESULT] 5: FAILURE";
                            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                    else:
                        print "TEST STEP 4: Get the PID of RBUS";
                        print "EXPECTED RESULT 4:  Should get the PID value of RBUS";
                        print "ACTUAL RESULT 4: Failed to get the PID value"
                        print "[TEST EXECUTION RESULT] 4: FAILURE";
                        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                else:
                    print "TEST STEP 3: Get the Enable Status of RBUS ";
                    print "EXPECTED RESULT 3: Enable Status value should be equal to default_value";
                    print "ACTUAL RESULT 3: RBUS Enable status is changed to new value"
                    print "[TEST EXECUTION RESULT] 3: FAILURE";
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            else:
                print "TEST STEP 2: Set RBUS Enable Status value to false",;
                print "EXPECTED RESULT 2:  Set Operation should be success";
                print "ACTUAL RESULT 2: Set operation was Failed";
                print "[TEST EXECUTION RESULT] 2: FAILURE";
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Enable Status of RBUS"
        print "EXPECTED RESULT 1: Should Get the Enable Status of RBUS"
        print "ACTUAL RESULT 1: Failed to get RBUS Enable Status"
        print "[TEST EXECUTION RESULT] 1: FAILURE";

    if revertFlag == 1:
        set_result, set_details = setTR181Value(tdkTestObj_Tr181_Set,parameter_Name,"false","bool");
        if expectedresult  in set_result:
            print "TEST STEP 7 Set RBUS Enable Status value to initial value",;
            print "EXPECTED RESULT 7: Revert operation should be success";
            print "ACTUAL RESULT 7: REvert operation was success";
            print "[TEST EXECUTION RESULT] 7: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 7 Set RBUS Enable Status value to initial value",;
            print "EXPECTED RESULT 7: Revert operation should be success";
            print "ACTUAL RESULT 7: REvert operation was Failed";
            print "[TEST EXECUTION RESULT] 7: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
