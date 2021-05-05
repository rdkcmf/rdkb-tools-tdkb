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
  <name>TS_RBUS_TestApp_PartialPathObjectFailCount</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the RBUS functionalities against PartialPath object using Test App execution</synopsis>
  <groups_id/>
  <execution_time>45</execution_time>
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
    <test_case_id>TC_RBUS_72</test_case_id>
    <test_objective>To check the RBUS functionalities against PartialPath object using Test App execution</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil modules
2. Execute the pre requisite of RBUS and it should be success
3. Execute the Test Provider App (/usr/bin/rbusTestProvider)
4. Execute the Test consumer App (/usr/bin/rbusTestConsumer)
5. Wait 5 min for consumer App execution to complete
6. Grep through the consumer log file (/tmp/rbusTestConsumer1.log) to get the PASS and FAIL count on PartialPath object
7. If the FAIL count was zero then make the script success else failure
8. Execute the post process of RBUS and it should be success
9. Unload the modules</automation_approch>
    <expected_output>The Fail count value of PartialPath object from consumer app result should be zero</expected_output>
    <priority>High</priority>
    <test_stub_interface>RBUS</test_stub_interface>
    <test_script>TS_RBUS_TestApp_PartialPathObjectFailCount</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
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
sysobj.configureTestCase(ip,port,'TS_RBUS_TestApp_PartialPathObjectFailCount');
tr181obj.configureTestCase(ip,port,'TS_RBUS_TestApp_PartialPathObjectFailCount');
#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    pre_req_value = 0;
    revert_flag = 0;
    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
    #Execute the PreRequisite of RBUS
    rbus_set,revert_flag = rbus_PreRequisite(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj_Sys_ExeCmd);
    if rbus_set == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "TEST STEP 1: Execute the Pre Requisite for RBUS"
        print "EXPECTED RESULT 1: Pre Requisite of RBUS should be success"
        print "ACTUAL RESULT 1: PreRequisite of RBUS was Success"
        print "[TEST EXECUTION RESULT] 1: SUCCESS";
        #Execute the Test Provider Test App
        actualresult,details = doSysutilExecuteCommand(tdkTestObj_Sys_ExeCmd,"/usr/bin/rbusTestProvider > /tmp/rbusTestProvider1.log &");
        if expectedresult in actualresult:
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "TEST STEP 2: Execute the Test Provider Test App"
            print "EXPECTED RESULT 2: Test Provider Test App should be running"
            print "ACTUAL RESULT 2: Test Provider Test App Running successfully"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";
            sleep(3);
            #Execute the Test Consumer Test App for 180 seconds
            actualresult,details = doSysutilExecuteCommand(tdkTestObj_Sys_ExeCmd,"/usr/bin/rbusTestConsumer -a > /tmp/rbusTestConsumer1.log");
            if expectedresult in actualresult:
                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                print "TEST STEP 3: Execute the Test Consumer Test App "
                print "EXPECTED RESULT 3: Test Consumer Test App should be running"
                print "ACTUAL RESULT 3: Test Consumer Test App Running successfully"
                print "[TEST EXECUTION RESULT] 3: SUCCESS";
                #Wait 5 min to finish the consumer app execution
                sleep(300);
                cmd = "tail -1 /tmp/rbusTestConsumer1.log | head -1";
                tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
                tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
                actualresult = tdkTestObj_Sys_ExeCmd.getResult();
                details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");
                print "Test Name : PartialPath Fail count Result is:",details
                if expectedresult in actualresult and details != "":
                    print "TEST STEP 4: Get the PartialPath Test Result from consumer log file (/tmp/rbusTestConsumer1.log)"
                    print "EXPECTED RESULT 4: Should get PartialPath Test Result value from consumer log file (/tmp/rbusTestConsumer1.log)"
                    print "ACTUAL RESULT 4: Successfully got PartialPath Test Result value from consumer file (/tmp/rbusTestConsumer1.log)"
                    print "[TEST EXECUTION RESULT] 4: SUCCESS";
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                    testname = details.split("|")[0]
                    passcount = details.split("|")[1]
                    failcount1 = details.split("|")[2].strip().replace(" ","").split("#")[0];
                    failcount = int(failcount1);
                    print "Test Name: ",testname
                    print "Pass Count: ",passcount
                    print "Fail Count: ",failcount
                    if int(failcount) == 0:
                        print "TEST STEP 5: Get the Fail count value for Test name PartialPath"
                        print "EXPECTED RESULT 5: Fail count value for Test name PartialPath should be zero"
                        print "[ACTUAL RESULT 5: Failcount value for Test name PartialPath is Zero"
                        print "[TEST EXECUTION RESULT] 5: SUCCESS";
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                    else:
                        print "TEST STEP 5: Get the Fail count value for Test name PartialPath"
                        print "EXPECTED RESULT 5: Fail count value for Test name PartialPath should be zero"
                        print "[ACTUAL RESULT 5: Failcount value for Test name PartialPath is Zero"
                        print "[TEST EXECUTION RESULT] 5: FAILURE";
                        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                else:
                    print "TEST STEP 4: Get the PartialPath Test Result from consumer log (/tmp/rbusTestConsumer1.log)"
                    print "EXPECTED RESULT 4: Should get PartialPath Test Result value from consumer log file (/tmp/rbusTestConsumer1.log)"
                    print "ACTUAL RESULT 4: Failed to get PartialPath Test Result value from consumer file (/tmp/rbusTestConsumer1.log)"
                    print "[TEST EXECUTION RESULT] 4: FAILURE";
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            else:
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                print "TEST STEP 3: Execute the Test Consumer Test App "
                print "EXPECTED RESULT 3: Test Consumer Test App should be running"
                print "ACTUAL RESULT 3: ailed to run Test Consumer Test App"
                print "[TEST EXECUTION RESULT] 3: FAILURE";
        else:
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            print "TEST STEP 2: Execute the Test Provider Test App"
            print "EXPECTED RESULT 2: Test Provider Test App should be running"
            print "ACTUAL RESULT 2: Failed to run Test Provider Test App"
            print "[TEST EXECUTION RESULT] 2: FAILURE";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "TEST STEP 1: Execute the Pre Requisite for RBUS"
        print "EXPECTED RESULT 1: Pre Requisite of RBUS should be success"
        print "ACTUAL RESULT 1: PreRequisite of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] 1: FAILURE";
    post_process_value = rbus_PostProcess(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj_Sys_ExeCmd,revert_flag);
    if post_process_value == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "TEST STEP 6: Execute the Post process of RBUS"
        print "EXPECTED RESULT 6: Post process of RBUS should be success"
        print "ACTUAL RESULT 6: Post process of RBUS was Success"
        print "[TEST EXECUTION RESULT] 6: SUCCESS";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "TEST STEP 6: Execute the Post process for RBUS"
        print "EXPECTED RESULT 6: Post process of RBUS should be success"
        print "ACTUAL RESULT 6: Post process of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] 6: FAILURE";
    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
