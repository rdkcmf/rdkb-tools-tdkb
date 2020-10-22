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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_CheckStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_CheckStatus</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the RBUS2.0 API rbus_checkstatus and compare the value with TR181 enable status value</synopsis>
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
    <test_case_id>TC_RBUS_17</test_case_id>
    <test_objective>To validate the RBUS2.0 API rbus_checkstatus and compare the value with TR181 enable status value</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_checkstatus</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable</input_parameters>
    <automation_approch>1. Load the rbus and tr181 module
2. Get the RBUS status using rbus_checkstatus API
3. Get the RBUS enable status value from TR181 parameter
4. Compare the values of API and TR181 parameter, the values should be matching
5. Unload the modules</automation_approch>
    <expected_output>The RBUS enable status value of API and TR181 parameter should be matching
</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_CheckStatus</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbRBUS_Utility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RBUS_CheckStatus');
tr181obj.configureTestCase(ip,port,'TS_RBUS_CheckStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =tr181obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('RBUS_CheckStatus');
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Detail is ",details

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Retrieve the RBUS status via HAL api";
        print "EXPECTED RESULT 1: Should retrieve the RBUS status via HAL api";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "RBUS status is %s" %details;

        if int(details) == 0 :
            rbus_status = "RBUS_ENABLED"
        elif int(details) == 1 :
            rbus_status = "RBUS_ENABLE_PENDING"
        elif int(details) == 2 :
            rbus_status = "RBUS_DISABLE_PENDING"
        else:
            rbus_status = "RBUS_DISABLED"

        tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
        def_result, default_value = isRBUSEnabled(tdkTestObj_Tr181_Get);

        if expectedresult in def_result:
            tdkTestObj_Tr181_Get.executeTestCase("SUCCESS");
            print "TEST STEP 2: Get the Enable Status of RBUS"
            print "EXPECTED RESULT 2: Should Get the Enable Status of RBUS"
            print "ACTUAL RESULT 2: RBUS Enable Status retrieved successfully"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";

            if default_value == "true" and (rbus_status == "RBUS_ENABLED" or rbus_status == "RBUS_DISABLE_PENDING"):
                print "RBUS is Enabled and RBUS Status is ",rbus_status
                tdkTestObj.setResultStatus("SUCCESS");
            elif default_value == "false" and (rbus_status == "RBUS_DISABLED" or rbus_status == "RBUS_ENABLE_PENDING"):
                print "RBUS is Disabled and RBUS Status is ",rbus_status
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "RBUS Enable status from TR181 and HAL is not matching"
                print "TR181 RBUS enable value is ",default_value
                print "HAL API RBUS enable value is ",rbus_status
                tdkTestObj.setResultStatus("FAILURE");
        else:
            tdkTestObj_Tr181_Get.executeTestCase("FAILURE");
            print "TEST STEP 2: Get the Enable Status of RBUS"
            print "EXPECTED RESULT 2: Should Get the Enable Status of RBUS"
            print "ACTUAL RESULT 2: Failed to get RBUS Enable Status"
            print "[TEST EXECUTION RESULT] 2: FAILURE";

    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Retrieve the RBUS status via HAL api";
        print "EXPECTED RESULT 1: Should retrieve the RBUS status via HAL api";
        print "[TEST EXECUTION RESULT] : FAILURE" ;
        print "Failure details: %s" %details

    obj.unloadModule("rbus");
    tr181obj.unloadModule("tdkbtr181");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";