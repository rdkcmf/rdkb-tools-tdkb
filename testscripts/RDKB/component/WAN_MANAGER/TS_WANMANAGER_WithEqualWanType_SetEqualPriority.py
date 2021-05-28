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
  <name>TS_WANMANAGER_WithEqualWanType_SetEqualPriority</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if similar priority can be set if Wan Types are equal</synopsis>
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
    <test_case_id>TC_WANMANAGER_46</test_case_id>
    <test_objective>This test case is to check if similar priority can be set if Wan Types are equal</test_objective>
    <test_type>Positive</test_type>
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
2.Check if Wan Types are equal and  if not make them equal
3.Set the similar priority for WANOE and DSL and is expected to be success
4.revert the set values
5.Unload the module</automation_approch>
    <expected_output>With similar Wan Type setting  equal Wan priority should be successful</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_WithEqualWanType_SetEqualPriority</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_WithEqualWanType_SetEqualPriority');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

def MakeWanTypeEqual(tdkTestObj_Get,tdkTestObj_Set):
    paramList =["Device.X_RDK_WanManager.CPEInterface.1.Wan.Type","Device.X_RDK_WanManager.CPEInterface.2.Wan.Type"];
    revertflag = 0;
    default = [];

    for item in paramList:
        tdkTestObj = tdkTestObj_Get;
        tdkTestObj.addParameter("ParamName",item);
        expectedresult= "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult:
            default.append(details);
        else:
            break;

    print "Default WAN Values are :",default;
    if expectedresult in actualresult:
        if default [0] != default [1]:
            revertflag =1;
            default[0] = str(default[0]);
            print "The Wan Type are unequal and changing the type for 2nd interface";
            tdkTestObj = tdkTestObj_Set;
            tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Type");
            tdkTestObj.addParameter("ParamValue",(default[0]));
            tdkTestObj.addParameter("Type","string");
            expectedresult= "SUCCESS";
            #Execute testcase on DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Setresult = tdkTestObj.getResultDetails();
        else:
            print "The Wan Type are equal and no change is required";

    return revertflag,default,actualresult;

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult= "SUCCESS";
    revertWanType = 0;
    print "TEST STEP 1 :Checking if the WAN Type of WANOE and DSL are equal and making them equal if not";
    tdkTestObj_Set = obj.createTestStep('TDKB_TR181Stub_Set');
    tdkTestObj_Get = obj.createTestStep('TDKB_TR181Stub_Get');
    revertWanType,defWanType,actualresult = MakeWanTypeEqual(tdkTestObj_Get,tdkTestObj_Set);
    if expectedresult in actualresult:
        print "ACTUAL RESUTL 1 : The  Wan Type of WANOE and DSL are  now equal ";
        print "TEST EXECUTION RESULT :SUCCESS";

        paramList =["Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority","Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority"];
        revertPriority = 0;
        default = [];
        flag =0;
        for item in paramList:
            tdkTestObj = tdkTestObj_Get;
            tdkTestObj.addParameter("ParamName",item);
            expectedresult= "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult:
               default.append(details);
            else:
                flag =1;

        if flag == 0:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the default priority value for DSL and WANOE";
            print "EXPECTED RESULT 2 : Get operation is expected to be success";
            print "ACTUAL RESULT 2: %s" %default;
            print "TEST EXECUTION RESULT :SUCCESS";

            setValue ="1";
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority|%s|int|Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority|%s|int" %(setValue,setValue));
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                revertPriority = 1;
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Setting priority as 1 for DSL and WANOE";
                print "EXPECTED RESULT 3 : The set operation is expected to be success";
                print "ACTUAL RESULT 3: %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Setting priority as 1 for DSL and WANOE";
                print "EXPECTED RESULT 3 : The set operation is expected to success";
                print "ACTUAL RESULT 3: %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the default priority value for DSL and WANOE";
            print "EXPECTED RESULT 2 : Get operation is expected to be success";
            print "ACTUAL RESULT 2: %s" %default;
            print "TEST EXECUTION RESULT :FAILURE";
    else:
        tdkTestObj_Set.setResultStatus("FAILURE");
        print "ACTUAL RESUTL 1 :Failed to make Wan Type of WANOE and DSL equal ";
        print "TEST EXECUTION RESULT :FAILURE";

    if revertWanType == 1:
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Type");
        tdkTestObj.addParameter("ParamValue",defWanType[1]);
        tdkTestObj.addParameter("Type","string");
        expectedresult= "SUCCESS";
        #Execute testcase on DUT
        tdkTestObj.executeTestCase(expectedresult);
        result = tdkTestObj.getResult();
        Setresult = tdkTestObj.getResultDetails();
        if expectedresult in result:
            print "Reverted the Wan Type changed";
            tdkTestObj.setResultStatus("SUCCESS");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "failed to revert the changed Wan Type";

    if revertPriority ==1:
        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
        tdkTestObj.addParameter("paramList","Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority|%s|int|Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority|%s|int" %(default[0],default[1]));
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 4: Reverting the priority  for DSL and WANOE";
            print "EXPECTED RESULT 4 : The set operation is expected to be success";
            print "ACTUAL RESULT 4: %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Reverting the priority  for DSL and WANOE";
            print "EXPECTED RESULT 4 : The set operation is expected to be success";
            print "ACTUAL RESULT 4: %s" %details;
            print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
