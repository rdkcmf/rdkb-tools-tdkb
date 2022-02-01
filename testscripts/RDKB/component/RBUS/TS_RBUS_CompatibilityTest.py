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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_CompatibilityTest</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check RBUS Compatibility Test is success using Test applications</synopsis>
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
    <test_case_id>TC_RBUS_9</test_case_id>
    <test_objective>To check RBUS Compatibility Test is success using Test applications</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil modules
2. Execute the pre requisite of RBUS and it should be success
3. Execute the Table Provider Test App with 200 as an argument ( 200 - number of seconds Test Provider will run)
4. Execute the Table consumer Test App with 180 as an argument ( 180 - number of seconds Test consumer app will run)
5. Above two apps will set up a following data model parameters with its pre-configured values which can be accessed through dmcli for next 180 seconds.
    - TR181 parameter name is Device.Tables1.T1.1.T2.1.Data  and its default value is "The color red"
	- TR181 parameter name is Device.Tables1.T1.1.T2.[green].Data and its default value is "The color green"
	- TR181 parameter name is Device.Tables1.T1.2.T2.1.Data and its default value is "The shape circle"
	- TR181 parameter name is Device.Tables1.T1.2.T2.[square].Data and its default value is "The shape square"
6. Get the above TR181 values and all get operation should be success
7. Validate the values against the provided default values and both values should be matching
8. Execute the post process of RBUS and it should be success
9. Unload the modules</automation_approch>
    <expected_output>Should be able to query all the Data model parameter from the Test apps and value should match with default values provided</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_CompatibilityTest</test_script>
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
sysobj.configureTestCase(ip,port,'TS_RBUS_CompatibilityTest');
tr181obj.configureTestCase(ip,port,'TS_RBUS_CompatibilityTest');

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

        #Execute the Table Provider Test App for 200 seconds and Table Consumer App for 180 seconds
        tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmdReboot');
        cmd = "/usr/bin/rbusTableProvider 200 > /tmp/plog & sleep 3 && /usr/bin/rbusTableConsumer 180 > /tmp/clog &"
        tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
        tdkTestObj_Sys_ExeCmd.executeTestCase("SUCCESS");
        actualresult = tdkTestObj_Sys_ExeCmd.getResult();

        if expectedresult in actualresult:
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "TEST STEP 2: Execute the Table Provider Test App for 200 seconds and Table Consumer Test App for 180 seconds"
            print "EXPECTED RESULT 2: Table Provider Test App and Table Consumer Test App should be running"
            print "ACTUAL RESULT 2: Table Provider and Table Consumer Test App Running successfully"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";
            sleep(10);

            t1_data1,t1_value1 = getTR181Value(tdkTestObj_Tr181_Get,"Device.Tables1.T1.1.T2.1.Data");
            print "Tables1.T1.1.T2.1.Data Result is %s and Value is %s" %(t1_data1,t1_value1)

            t1_data2,t1_value2 = getTR181Value(tdkTestObj_Tr181_Get,"Device.Tables1.T1.1.T2.[green].Data");
            print "Tables1.T1.1.T2.[green].Data Result is %s and Value is %s" %(t1_data2,t1_value2)

            t2_data1,t2_value1 = getTR181Value(tdkTestObj_Tr181_Get,"Device.Tables1.T1.2.T2.1.Data");
            print "Tables1.T1.2.T2.1.Data Result is %s and Value is %s" %(t2_data1,t2_value1)

            t2_data2,t2_value2 = getTR181Value(tdkTestObj_Tr181_Get,"Device.Tables1.T1.2.T2.[square].Data");
            print "Tables1.T1.2.T2.[square].Data Result is %s and Value is %s" %(t2_data2,t2_value2)

            if expectedresult in (t1_data1 and 	t1_data2 and t2_data1 and t2_data2):
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the TR181 values from the Table"
                print "EXPECTED RESULT 3: Should get the TR181 values"
                print "ACTUAL RESULT 3: Get operation on RBUS compatibility Test was successful"
                print "[TEST EXECUTION RESULT] 3: SUCCESS";

                if t1_value1 == "The color red" and t1_value2 == "The color green" and t2_value1 == "The shape circle" and t2_value2 == "The shape square":
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Validate the Values from Table"
                    print "EXPECTED RESULT 4: Values retrieved from table should be matching with the value given"
                    print "ACTUAL RESULT 4: Values retrieved from tables are Proper"
                    print "[TEST EXECUTION RESULT] 4: SUCCESS";
                else:
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                    print "TEST STEP 4: Validate the Values from Table"
                    print "EXPECTED RESULT 4: Values retrieved from table should be matching with the value given"
                    print "ACTUAL RESULT 4: Values retrieved from tables are NOT Proper"
                    print "[TEST EXECUTION RESULT] 4: FAILURE";
            else:
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the TR181 values from the Table"
                print "EXPECTED RESULT 3: Should get the TR181 values"
                print "ACTUAL RESULT 3: Get operation on RBUS compatibility Test was Failed"
                print "[TEST EXECUTION RESULT] 3: FAILURE";
        else:
            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
            print "TEST STEP 2: Execute the Table Provider Test App for 200 seconds and Table Consumer Test App for 180 seconds"
            print "EXPECTED RESULT 2: Table Provider Test App and Table Consumer Test App should be running"
            print "ACTUAL RESULT 2: Failed to RUN Table Provider and Table Consumer Test App"
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
        print "TEST STEP 5: Execute the Post process of RBUS"
        print "EXPECTED RESULT 5: Post process of RBUS should be success"
        print "ACTUAL RESULT 5: Post process of RBUS was Success"
        print "[TEST EXECUTION RESULT] 5: SUCCESS";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "TEST STEP 5: Execute the Post process for RBUS"
        print "EXPECTED RESULT 5: Post process of RBUS should be success"
        print "ACTUAL RESULT 5: Post process of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] 5: FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
