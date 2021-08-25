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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_CheckSetFailure_ForInvalidValue</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if set operation of Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC with invalid value returns Execution error as expected when the device is in RBUS mode.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_RBUS_59</test_case_id>
    <test_objective>To check if set operation of Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC with invalid value returns Execution error as expected when the device is in RBUS mode.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC
ParamValue : test
Type : unsignedint</input_parameters>
    <automation_approch>1. Load the modules
2. Check whether the device is in RBUS mode. If it is not, then Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable and reboot the device.
3. After the DUT comes up, set Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC of unsigned int type to an invalid value "test". The set operation should fail.
4. Revert to the initial RBUS enable state if the revert flag is set.</automation_approch>
    <expected_output>Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC when set to an invalid value should return error in RBUS mode.</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_CheckSetFailure_ForInvalidValue</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbRBUS_Utility import *;
from tdkutility import *;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RBUS_CheckSetFailure_ForInvalidValue');
tr181obj.configureTestCase(ip,port,'TS_RBUS_CheckSetFailure_ForInvalidValue');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    revert_flag = 0;

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
    print "\nTEST STEP 1: Execute the Pre Requisite for RBUS"
    print "EXPECTED RESULT 1: Pre Requisite of RBUS should be success"
    #Execute the PreRequisite of RBUS
    rbus_set,revert_flag = rbus_PreRequisite(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj);

    if rbus_set == 1:
        print "ACTUAL RESULT 1: PreRequisite of RBUS was Success"
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "\n******************************************************************"

        #Set operation with invalid value; Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC is of unsigned int type
        tdkTestObj_Tr181_Set.addParameter("ParamName","Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC");
        #Set to Invalid value
        value = "test";
        tdkTestObj_Tr181_Set.addParameter("ParamValue",value);
        tdkTestObj_Tr181_Set.addParameter("Type","unsignedint");
        expectedresult="FAILURE";
        #Execute the test case in DUT
        tdkTestObj_Tr181_Set.executeTestCase(expectedresult);
        actualresult = tdkTestObj_Tr181_Set.getResult();
        details = tdkTestObj_Tr181_Set.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set DDevice.DeviceInfo.Webpa.X_COMCAST-COM_CMC to an invalid value : %s" %value;
            print "EXPECTED RESULT 2: The set operation should fail with invalid value";
            print "ACTUAL RESULT 2: Details : %s" %details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
            print "TEST STEP 2: Set Device.DeviceInfo.Webpa.X_COMCAST-COM_CMC to an invalid value : %s" %value;
            print "EXPECTED RESULT 2: The set operation should fail with invalid value";
            print "ACTUAL RESULT 2: Details : %s" %details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    print "\n******************************************************************";

    print "\nTEST STEP 3: Execute the Post process of RBUS"
    print "EXPECTED RESULT 3: Post process of RBUS should be success"
    post_process_value = rbus_PostProcess(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj,revert_flag);

    if post_process_value == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 3: Post process of RBUS was Success"
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT 3: Post process of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] : FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");

