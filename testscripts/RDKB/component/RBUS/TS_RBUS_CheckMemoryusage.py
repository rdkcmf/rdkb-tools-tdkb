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
  <name>TS_RBUS_CheckMemoryusage</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check Memory usage of RBUS is lesser than DBUS</synopsis>
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
    <test_case_id>TC_RBUS_10</test_case_id>
    <test_objective>To check Memory usage of RBUS is lesser than DBUS</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil modules
2. Get the initial value of RBUS enable status and store it
3. Get the Memory usage value from TOP and store it as RBUS_memory if RBUS is enabled else store it as DBUS_memory
4. Toggle the RBUS enable status
5. Get the Memory usage value from TOP and store it as DBUS_memory if RBUS is set to false in step 4 else store it as RBUS_memory
6. Compare DBUS_memory and RBUS_memory values, RBUS_memory value should be lesser than DBUS_memory value
7. Revert the value to the initial value
8. Unload the Modules</automation_approch>
    <expected_output>RBUS_memory value from top command should be lesser than DBUS_memory value</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_CheckMemoryusage</test_script>
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
sysobj.configureTestCase(ip,port,'TS_RBUS_CheckMemoryusage');
tr181obj.configureTestCase(ip,port,'TS_RBUS_CheckMemoryusage');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

def getMemUsageFromTOP(tdkTestObj_Sys_ExeCmd):
    actualresult,details = doSysutilExecuteCommand(tdkTestObj_Sys_ExeCmd,"top -n 1 |grep -i Mem |sed  's/^[^0-9]*//;s/[^0-9].*$//' ");
    return actualresult,details;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    revert_flag = 0;
    DBUS_memory = 0;
    RBUS_memory =0;

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');

    def_result, default_value = isRBUSEnabled(tdkTestObj_Tr181_Get);

    if expectedresult in def_result:
        tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Enable Status of RBUS"
        print "EXPECTED RESULT 1: Should Get the Enable Status of RBUS"
        print "ACTUAL RESULT 1: RBUS Enable Status retrieved successfully"
        print "[TEST EXECUTION RESULT] 1: SUCCESS";

        print "Initial RBUS Enabled Status is",default_value

        if default_value == "true":
            value_to_set = "false"
            current_mode = "RBUS"
        else:
            value_to_set = "true"
            current_mode = "DBUS"

        mem_result,mem_value1 = getMemUsageFromTOP(tdkTestObj_Sys_ExeCmd);

        if expectedresult in mem_result:
            tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Memory Usage value for ",current_mode
            print "EXPECTED RESULT 2: Should Get the Memory usage value of ",current_mode
            print "ACTUAL RESULT 2: Memory Usage value retrieved successfully"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";
            print "Memory Usage value of %s is %s"%(current_mode,mem_value1)

            rbus_set,revert_flag = doEnableDisableRBUS(value_to_set,sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
            if rbus_set == 1:
                tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                print "TEST STEP 3: Set the RBUS Enable status to ",value_to_set
                print "EXPECTED RESULT 3: Should set the RBUS Enable status to ",value_to_set
                print "ACTUAL RESULT 3: Set operation was successful"
                print "[TEST EXECUTION RESULT] 3: SUCCESS";

                #Set operation was Success, Change the current_mode
                if current_mode == "DBUS":
                    DBUS_memory = int(mem_value1);
                    current_mode = "RBUS"
                else:
                    RBUS_memory = int(mem_value1);
                    current_mode = "DBUS"

                mem_result1,mem_value2 = getMemUsageFromTOP(tdkTestObj_Sys_ExeCmd);

                if expectedresult in mem_result:
                    tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the Memory Usage value for ",current_mode
                    print "EXPECTED RESULT 4: Should Get the Memory usage value of ",current_mode
                    print "ACTUAL RESULT 4: Memory Usage value retrieved successfully"
                    print "[TEST EXECUTION RESULT] 4: SUCCESS";
                    print "Memory Usage value %s is %s"%(current_mode,mem_value2)

                    if current_mode == "DBUS":
                        DBUS_memory = int(mem_value2);
                    else:
                        RBUS_memory = int(mem_value2);

                else:
                    tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the Memory Usage value for ",current_mode
                    print "EXPECTED RESULT 4: Should Get the Memory usage value of ",current_mode
                    print "ACTUAL RESULT 4: Failed to get Memory Usage value "
                    print "[TEST EXECUTION RESULT] 4: FAILURE";
            else:
                tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                print "TEST STEP 3: Set the RBUS Enable status to ",value_to_set
                print "EXPECTED RESULT 3: Should set the RBUS Enable status to ",value_to_set
                print "ACTUAL RESULT 3: Set operation was FAILED"
                print "[TEST EXECUTION RESULT] 3: FAILURE";
        else:
            tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Memory Usage value for ",current_mode
            print "EXPECTED RESULT 2: Should Get the Memory usage value of ",current_mode
            print "ACTUAL RESULT 2: Failed to get Memory Usage value "
            print "[TEST EXECUTION RESULT] 2: FAILURE";
    else:
        tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Enable Status of RBUS"
        print "EXPECTED RESULT 1: Should Get the Enable Status of RBUS"
        print "ACTUAL RESULT 1: Failed to get RBUS Enable Status"
        print "[TEST EXECUTION RESULT] 1: FAILURE";


    if DBUS_memory > 0 and RBUS_memory > 0:
        if DBUS_memory >= RBUS_memory:
            tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
            print "TEST STEP 5: Compare the Memory Usage value of RBUS and DBUS"
            print "EXPECTED RESULT 5: RBUS Memory Usage should be less than DBUS"
            print "ACTUAL RESULT 5: RBUS Memory Usage is lesser the DBUS Memory Usage "
            print "[TEST EXECUTION RESULT] 5: SUCCESS";
        else:
            print "Memory and CPU usage in RBUS is GREATER than DBUS"
            tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
            print "TEST STEP 5: Compare the Memory Usage value of RBUS and DBUS"
            print "EXPECTED RESULT 5: RBUS Memory Usage should be less than DBUS"
            print "ACTUAL RESULT 5: RBUS Memory Usage is lesser the DBUS Memory Usage "
            print "[TEST EXECUTION RESULT] 5: FAILURE";
    else:
        print "Unable to get Memory usage value of RBUS and DBUS"
        tdkTestObj_Tr181_Set.setResultStatus("FAILURE");

    if revert_flag == 1:
        rbus_set,revert_flag = doEnableDisableRBUS(default_value,sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if rbus_set == 1:
            tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
            print "TEST STEP 6: Revert the RBUS enable status value"
            print "EXPECTED RESULT 6: Revert operation should be success"
            print "ACTUAL RESULT 6: Revert operation was successful "
            print "[TEST EXECUTION RESULT] 6: SUCCESS";
        else:
            tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
            print "TEST STEP 6: Revert the RBUS enable status value"
            print "EXPECTED RESULT 6: Revert operation should be success"
            print "ACTUAL RESULT 6: Revert operation was FAILED "
            print "[TEST EXECUTION RESULT] 6: FAILURE";
    else:
        print "Revert Flag was not set, No need for Revert operation"

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");