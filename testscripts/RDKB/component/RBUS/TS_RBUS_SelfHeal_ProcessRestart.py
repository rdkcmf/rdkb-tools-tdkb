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
  <version>14</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_SelfHeal_ProcessRestart</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate in RBUS mode, ccsp process getting restarted after killed</synopsis>
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
    <test_case_id>TC_RBUS_11</test_case_id>
    <test_objective>To validate in RBUS mode, ccsp process getting restarted after killed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable
</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil modules
2. Get the initial value of RBUS enable status and store it
3. Execute the Prerequisite of RBUS and it should be success
4. Get the PID of ccspwifissp process and kill the process
5. Check whether the ccspwifissp process is restarted successfully
6. Execute post process of RBUS and it should be success
7. Unload the Modules</automation_approch>
    <expected_output>The ccsp process should be restarted if its killed in RBUS mode</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_SelfHeal_ProcessRestart</test_script>
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
from tdkutility import *;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RBUS_SelfHeal_ProcessRestart');
tr181obj.configureTestCase(ip,port,'TS_RBUS_SelfHeal_ProcessRestart');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    revert_flag = 0;

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');

    print "TEST STEP 1: Execute the Pre Requisite for RBUS"
    print "EXPECTED RESULT 1: Pre Requisite of RBUS should be success"
    #Execute the PreRequisite of RBUS
    rbus_set,revert_flag = rbus_PreRequisite(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj_Sys_ExeCmd);

    if rbus_set == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

        print "ACTUAL RESULT 1: PreRequisite of RBUS was Success"
        print "[TEST EXECUTION RESULT] 1: SUCCESS";
        print "******************************************************************"

        actualresult,pid_value = getPID(tdkTestObj_Sys_ExeCmd,"CcspWifiSsp");

        if expectedresult in actualresult and pid_value != "":
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the PID value of CcspWifiSsp Process"
            print "EXPECTED RESULT 2: Should get the PID value of CcspWifiSsp process"
            print "ACTUAL RESULT 2: PID value retrieved successfully ",pid_value
            print "[TEST EXECUTION RESULT] 2: SUCCESS";
            print "******************************************************************"
            pid_value = int(pid_value);

            actualresult = killProcess(tdkTestObj_Sys_ExeCmd,pid_value,"");

            if expectedresult in actualresult:
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                print "TEST STEP 3: Kill the CcspWifiSsp Process"
                print "EXPECTED RESULT 3: CcspWifiSsp Process should be killed"
                print "ACTUAL RESULT 3: CcspWifiSsp process killed successfully"
                print "[TEST EXECUTION RESULT] 3: SUCCESS";
                print "******************************************************************"

                sleep(10);

                actualresult,pid_value = checkProcessRestarted(tdkTestObj_Sys_ExeCmd,"CcspWifiSsp");

                if expectedresult in actualresult and pid_value != "":
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Get the PID value of CcspWifiSsp Process to make sure process is restarted"
                    print "EXPECTED RESULT 5: Should get the PID value of CcspWifiSsp process"
                    print "ACTUAL RESULT 5: PID value retrieved successfully and Process is Running "
                    print "[TEST EXECUTION RESULT] 5: SUCCESS";
                else:
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                    print "TEST STEP 5: Get the PID value of CcspWifiSsp Process to make sure process is restarted"
                    print "EXPECTED RESULT 5: Should get the PID value of CcspWifiSsp process"
                    print "ACTUAL RESULT 5: Failed to get PID value,Process is not restarted"
                    print "[TEST EXECUTION RESULT] 5: FAILURE";

            else:
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                print "TEST STEP 3: Kill the CcspWifiSsp Process"
                print "EXPECTED RESULT 3: CcspWifiSsp Process should be killed"
                print "ACTUAL RESULT 3: Fail to kill the CcspWifiSsp process"
                print "[TEST EXECUTION RESULT] 3: FAILURE";
        else:
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the PID value of CcspWifiSsp Process"
            print "EXPECTED RESULT 2: Should get the PID value of CcspWifiSsp process"
            print "ACTUAL RESULT 2: Failed to get PID value "
            print "[TEST EXECUTION RESULT] 2: FAILURE";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: PreRequisite of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] 1: FAILURE";

    print "TEST STEP 6: Execute the Post process of RBUS"
    print "EXPECTED RESULT 6: Post process of RBUS should be success"

    post_process_value = rbus_PostProcess(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj_Sys_ExeCmd,revert_flag);
    if post_process_value == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 6: Post process of RBUS was Success"
        print "[TEST EXECUTION RESULT] 6: SUCCESS";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT 6: Post process of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] 6: FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
