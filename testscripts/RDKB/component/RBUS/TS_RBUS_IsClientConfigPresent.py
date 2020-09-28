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
  <name>TS_RBUS_IsClientConfigPresent</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check RBUS client config file (/etc/rbus_client.conf) is present when RBUS is enabled</synopsis>
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
    <test_case_id>TC_RBUS_4</test_case_id>
    <test_objective>To check RBUS client config file (/etc/rbus_client.conf) is present when RBUS is enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil Modules
2. Check the RBUS is enabled or not using isRBUSEnabled function and store the initial value
3. If RBUS is disabled then enable the RBUS using doEnableDisableRBUS function
4. Check whether RBUS client config file (/etc/rbus_client.conf) is present or not
5. Make the script success when client config file present else failure
6. Revert the value of RBUS is its changed in step 3
7. Unload the modules</automation_approch>
    <expected_output>The RBUS client config file (/etc/rbus_client.conf) should be present</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_IsClientConfigPresent</test_script>
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
sysobj.configureTestCase(ip,port,'TS_RBUS_IsClientConfigPresent');
tr181obj.configureTestCase(ip,port,'TS_RBUS_IsClientConfigPresent');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    rbus_enabled = 0;
    revert_flag = 0;

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
            rbus_enabled = 1;
        else:
            #RBUS is not enabled, Enable RBUS using doEnableDisableRBUS function, which will enable RBUS and Do a reboot to take effect
            rbus_set,revert_flag = doEnableDisableRBUS("true",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
            if rbus_set == 1:
                rbus_enabled = 1;
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                print "TEST STEP 2: Enable the RBUS status to TRUE"
                print "EXPECTED RESULT 2: Should Enable RBUS Status of TRUE"
                print "ACTUAL RESULT 2: RBUS Enable status set to TRUE"
                print "[TEST EXECUTION RESULT] 2: SUCCESS";
            else:
                rbus_enabled = 0
                print "TEST STEP 2: Enable the RBUS status to TRUE"
                print "EXPECTED RESULT 2: Should Enable RBUS Status of TRUE"
                print "ACTUAL RESULT 2: Failed to Enable RBUS status to TRUE"
                print "[TEST EXECUTION RESULT] 2: FAILURE";
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

        if rbus_enabled == 1:
            actualresult,details = isFilePresent(tdkTestObj_Sys_ExeCmd,"/etc/rbus_client.conf")
            if 	expectedresult in actualresult and details != "":
                print "TEST STEP 3: Check whether RBUS client Config file(/etc/rbus_client.conf) is present"
                print "EXPECTED RESULT 3: RBUS client config file(/etc/rbus_client.conf) should be present under etc"
                print "ACTUAL RESULT 3: RBUS client config file (/etc/rbus_client.conf) is present"
                print "[TEST EXECUTION RESULT] 3: SUCCESS";
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
            else:
                print "TEST STEP 3: Check whether RBUS client Config file(/etc/rbus_client.conf)  is present"
                print "EXPECTED RESULT 3: RBUS client config file(/etc/rbus_client.conf)  should be present under etc"
                print "ACTUAL RESULT 3: RBUS client config file(/etc/rbus_client.conf) is NOT present"
                print "[TEST EXECUTION RESULT] 3: FAILURE";
                tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        else:
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            print "RBUS is NOT enabled to TRUE"
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Enable Status of RBUS"
        print "EXPECTED RESULT 1: Should Get the Enable Status of RBUS"
        print "ACTUAL RESULT 1: Failed to get the RBUS enable status"
        print "[TEST EXECUTION RESULT] 1: FAILURE";

    #Revert Flag will set to 1 only when initial value was false, so disable the RBUS using doEnableDisableRBUS function
    if revert_flag == 1:
        rbus_set,revert_flag = doEnableDisableRBUS("false",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if rbus_set == 1:
            print "TEST STEP 7: Set the RBUS enable status to False"
            print "EXPECTED RESULT 7: Should Set the RBUS Enable Status of False"
            print "ACTUAL RESULT 7: RBUS Enable Status set to False"
            print "[TEST EXECUTION RESULT] 1: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 7: Set the RBUS enable status to False"
            print "EXPECTED RESULT 7: Should Set the RBUS Enable Status of False"
            print "ACTUAL RESULT 7: Failed to set RBUS Enable Status to False"
            print "[TEST EXECUTION RESULT] 1: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");