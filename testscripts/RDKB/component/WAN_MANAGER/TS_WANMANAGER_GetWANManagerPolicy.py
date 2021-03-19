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
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_GetWANManagerPolicy</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get the Device.X_RDK_WanManager.Policy and  check the policy is one from
FIXED_MODE_ON_BOOTUP, FIXED_MODE, PRIMARY_PRIORITY, PRIMARY_PRIORITY_ON_BOOTUP, MULTIWAN_MODE</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WANMANAGER_08</test_case_id>
    <test_objective>Get the Device.X_RDK_WanManager.Policy and  check the policy is one from
FIXED_MODE_ON_BOOTUP, FIXED_MODE, PRIMARY_PRIORITY, PRIMARY_PRIORITY_ON_BOOTUP, MULTIWAN_MODE</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.Policy</input_parameters>
    <automation_approch>1] Load the module
2]Get the WANMANAGER Policy value
4]Check if the policy is one from
FIXED_MODE_ON_BOOTUP, FIXED_MODE, PRIMARY_PRIORITY, PRIMARY_PRIORITY_ON_BOOTUP, MULTIWAN_MODE
5]Unload the module</automation_approch>
    <expected_output>WANMANAGER policy is one from
FIXED_MODE_ON_BOOTUP, FIXED_MODE, PRIMARY_PRIORITY, PRIMARY_PRIORITY_ON_BOOTUP, MULTIWAN_MODE
</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_GetWANManagerPolicy_</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from WanManager_Utility import *;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_GetWANManagerPolicy');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.Policy");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    policy=details.strip().replace("\\n", "");
    if expectedresult in actualresult and policy != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 :Check the value of wanmanager policy ";
        print "EXPECTED RESULT 1: Should get wanmanager policy";
        print "ACTUAL RESULT 1: The value received is %s" %policy;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        if policy in ExpectedPolicyList:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 :Check  if the policy is one from:",ExpectedPolicyList;
            print "EXPECTED RESULT 2: policy value should be within the expected list";
            print "ACTUAL RESULT 2: policy value is within the expected list";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 :Check the check the policy is one from :",ExpectedPolicyList;
            print "EXPECTED RESULT 2: policy value should be within the expected list";
            print "ACTUAL RESULT 2: policy value is not within the expected list";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 :Check the value of wanmanager policy";
        print "EXPECTED RESULT 1: Should get wanmanager policy";
        print "ACTUAL RESULT 1: The value received is %s" %policy;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
