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
  <version>3</version>
  <name>TS_WANMANAGER_WithEqualPriority_SetPrimaryWanType</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Primary Wan Type can be set to both the interfaces when Wan Priorities are equal</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WANMANAGER_44</test_case_id>
    <test_objective>This test case is to check  if Primary Wan Type can be set to both the interfaces when Wan Priorities are equal</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.CPEInterface.1.Wan.Type
Device.X_RDK_WanManager.CPEInterface.2.Wan.Type
Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority
Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority</input_parameters>
    <automation_approch>1.Load the module
2.Get the priority of WANOE and DSL and check if  equal if not make them equal
3.Try setting the Wan Type for DSL and WANOE as Primary and is expected to fail
4.Revert the priorities if changed
5.Unload the module</automation_approch>
    <expected_output>When a equal priority is given for both interfaces then setting a similar Wan Type i,e primary should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_WithEqualPriority_SetPrimaryWanType</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>none</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
from WanManager_Utility import *;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_WithEqualPriority_SetPrimaryWanType');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult= "SUCCESS";
    revertpriority = 0;
    print "TEST STEP 1 :Checking if the priorites of WANOE and DSL are equal and making them equal if not";
    tdkTestObj_Set = obj.createTestStep('TDKB_TR181Stub_Set');
    tdkTestObj_Get = obj.createTestStep('TDKB_TR181Stub_Get');
    revertpriority,defPriority,actualresult = MakePriorityEqual(tdkTestObj_Get,tdkTestObj_Set);
    if expectedresult in actualresult:
        print "ACTUAL RESUTL 1 : The  priorites of WANOE and DSL are  now equal ";
        print "TEST EXECUTION RESULT :SUCCESS";

        setValue ="Primary";
        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
        tdkTestObj.addParameter("paramList","Device.X_RDK_WanManager.CPEInterface.1.Wan.Type|%s|string|Device.X_RDK_WanManager.CPEInterface.2.Wan.Type|%s|string" %(setValue,setValue));
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Setting Wan Type as Primary for DSL and WANOE";
            print "EXPECTED RESULT 2 : The set operation is expected to fail";
            print "ACTUAL RESULT 2: %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Setting Wan Type as Primary for DSL and WANOE";
            print "EXPECTED RESULT 2 : The set operation is expected to fail";
            print "ACTUAL RESULT 2: %s" %details;
            print "TEST EXECUTION RESULT :FAILURE";

    else:
        tdkTestObj_Set.setResultStatus("FAILURE");
        print "ACTUAL RESUTL 1 :Failed to make priorites of WANOE and DSL equal ";
        print "TEST EXECUTION RESULT :FAILURE";

    if revertpriority == 1:
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority");
        tdkTestObj.addParameter("ParamValue",defPriority[1]);
        tdkTestObj.addParameter("Type","int");
        expectedresult= "SUCCESS";
        #Execute testcase on DUT
        tdkTestObj.executeTestCase(expectedresult);
        result = tdkTestObj.getResult();
        Setresult = tdkTestObj.getResultDetails();
        if expectedresult in result:
            print "Reverted the priority changed";
            tdkTestObj.setResultStatus("SUCCESS");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "failed to revert the changed priority";
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
