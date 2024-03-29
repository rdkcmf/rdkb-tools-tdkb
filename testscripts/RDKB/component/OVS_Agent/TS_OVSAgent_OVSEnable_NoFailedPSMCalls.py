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
  <version>2</version>
  <name>TS_OVSAgent_OVSEnable_NoFailedPSMCalls</name>
  <primitive_test_id/>
  <primitive_test_name>OVS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To ensure no psm failures observed with OVS Enabled</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_OVSAGENT_08</test_case_id>
    <test_objective>This test case is to ensure no psm failures observed with OVS Enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.CodeBigFirst.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Disable code big and enable mesh as pre-requisite
3.Enable ovs and reboot the device
4.Check if any psm errors are seen after enabling
5.Revert the set values
6.Unload the module
</automation_approch>
    <expected_output>With OVS Enabled no psm errors should be logged after device comes up on reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>OVS_AGENT</test_stub_interface>
    <test_script>TS_OVSAgent_OVSEnable_NoFailedPSMCalls</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_OVSAgent_OVSEnable_NoFailedPSMCalls');
tr181obj.configureTestCase(ip,port,'TS_OVSAgent_OVSEnable_NoFailedPSMCalls');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();
revert_flag=0;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');

    result,default = ovs_PreRequisite(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);

    if expectedresult in result:
        print "TEST STEP 1:  Get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "EXPECTED RESULT 1: Should get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "ACTUAL RESULT 1 : The Code Big and Mesh status are as expected";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

        print "\n\n";
        print "TEST STEP 2: Get the OVS status"
        print "EXPECTED RESULT 2: OVS Status should enabled else enable it "

        ovs_set,revert_flag = doEnableDisableOVS("true",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if ovs_set == 1:
            ovs_enabled = 1;
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: OVS Enable status set to false"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";

            query="grep -rin \"ret code 102\" /rdklogs/logs/bridgeUtils.log";
            print "query:%s" %query
            tdkTestObj = tdkTestObj_Sys_ExeCmd;
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            ovs = tdkTestObj.getResultDetails().strip().replace("\\n","");

            if expectedresult in actualresult1 and "ret code 102" not in ovs:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 : Check for PSM failures in in bridgeUtils.log";
                print "EXPECTED RESULT 3: Should not get PSM failures in in bridgeUtils.log";
                print "ACTUAL RESULT 3:Log message received is :%s"%ovs;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 : Check for PSM failures in in bridgeUtils.log";
                print "EXPECTED RESULT 3: Should not get PSM failures in in bridgeUtils.log";
                print "ACTUAL RESULT 3:Log message received is :%s"%ovs;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
             ovs_enabled = 0
             print "ACTUAL RESULT 2: OVS status enable operation failed";
             print "[TEST EXECUTION RESULT] 2: FAILURE";
             tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

        actualresult = ovs_PostProcess(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,default);
        if expectedresult in actualresult:
            print "TEST STEP 4: Set Code Big and Mesh Enable Status value to initial value",;
            print "EXPECTED RESULT 4: Revert operation should be success";
            print "ACTUAL RESULT 4: REvert operation was success";
            print "[TEST EXECUTION RESULT] 7: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 4: Set Code Big and Mesh Enable Status value to initial value",;
            print "EXPECTED RESULT 4: Revert operation should be success";
            print "ACTUAL RESULT 4: REvert operation was Failed";
            print "[TEST EXECUTION RESULT] 5: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1:  Get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "EXPECTED RESULT 1: Should get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "ACTUAL RESULT 1 : The Code Big and Mesh status are as expected";
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    #Revert Flag will set to 1 only when initial value was false, so disable the OVS using doEnableDisableOVS function
    if revert_flag == 1:
        ovs_set,revert_flag = doEnableDisableOVS("false",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if ovs_set == 1:
            print "TEST STEP 5: Set the OVS enable status to False"
            print "EXPECTED RESULT 5: Should Set the OVS Enable Status of False"
            print "ACTUAL RESULT 5: OVS Enable Status set to False"
            print "[TEST EXECUTION RESULT] 1: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 5: Set the OVS enable status to False"
            print "EXPECTED RESULT 5: Should Set the OVS Enable Status of False"
            print "ACTUAL RESULT 5: Failed to set OVS Enable Status to False"
            print "[TEST EXECUTION RESULT] 1: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
