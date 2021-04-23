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
  <name>TS_WANMANAGER_SetInterfaceWithExistingWantype</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the wan type to interface which already exist for another interface</synopsis>
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
    <test_case_id>TC_WANMANAGER_16</test_case_id>
    <test_objective>This test case is to set the wan type to interface which already exist for another interface</test_objective>
    <test_type>Neagtive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Get the WAN type for a interface
3.set the same WAN type to another interface and is expected to fail
4.Unload the module</automation_approch>
    <expected_output>We should not be able to set a WAN type which is already configured for another interface</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_SetInterfaceWithExistingWantype</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
import tdkutility
from tdkutility import *

obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_SetInterfaceWithExistingWantype');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

def MakePriorityEqual (tdkTestObj_Get,tdkTestObj_Set):
    paramList =["Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority","Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority"];
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

    print "Default priority Values are :",default;

    if default [0] != default [1]:
        revertflag =1;
        default[0] = str(default[0]);
        print "The priorities are unequal and changing the priority for 2nd interface";
        tdkTestObj = tdkTestObj_Set;
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority");
        tdkTestObj.addParameter("ParamValue",(default[0]));
        tdkTestObj.addParameter("Type","int");
        expectedresult= "SUCCESS";
        #Execute testcase on DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Setresult = tdkTestObj.getResultDetails();
    else:
        print "The priorities are equal and no change is required";

    return revertflag,default,actualresult;

if "SUCCESS" in loadmodulestatus.upper():
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

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Type");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        wanType=details.strip().replace("\\n", "");
        if expectedresult in actualresult and wanType != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 :Get the WAN Type of interface no. 2";
            print "EXPECTED RESULT 2: Should get WAN Type of interface no. 2";
            print "ACTUAL RESULT 2: The value received is %s" %wanType;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.1.Wan.Type");
            tdkTestObj.addParameter("ParamValue",wanType);
            tdkTestObj.addParameter("Type","string");
            expectedresult= "FAILURE";
            #Execute testcase on DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Setresult = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 :Set the Wan WAN Type of interface no. 1 with same as interface no. 2";
                print "EXPECTED RESULT 3: Should not set interface no. 1 with same as interface no. 2";
                print "ACTUAL RESULT 3: ",Setresult;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 :Set the Wan WAN Type of interface no. 1 with same as interface no. 2";
                print "EXPECTED RESULT 3: Should not set interface no. 1 with same as interface no. 2";
                print "ACTUAL RESULT 3: ",Setresult;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 :Get the Wan WAN Type of interface no. 2";
            print "EXPECTED RESULT 2: Should get Wan WAN Type of interface no. 2";
            print "ACTUAL RESULT 2: The value received is %s" %wanType;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        if revertpriority ==1:
            paramList =["Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority","Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority"];
            index =0;
            for item in paramList:
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                tdkTestObj.addParameter("ParamName",item)
                tdkTestObj.addParameter("ParamValue",defPriority[index]);
                tdkTestObj.addParameter("Type","int");
                expectedresult= "SUCCESS";
                #Execute testcase on DUT
                tdkTestObj.executeTestCase(expectedresult);
                result = tdkTestObj.getResult();
                Setresult = tdkTestObj.getResultDetails();
                index =index +1;
                if expectedresult in result:
                    print "Reverted the unequal  priority";
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "failed to revert the changed priority";
    else:
        print "ACTUAL RESUTL 1 : failed to make priorites of WANOE and DSL equal ";
        print "TEST EXECUTION RESULT :FAILURE";
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
