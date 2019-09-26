##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>9</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzIfConfigUpOrDown</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_IfConfigUporDown</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the Ap status for 2.4GHz and invoke wifi_ifConfigDown() if the status is 'Up' or invoke wifi_ifConfigUp() if the status is 'Disable' and validate the same using wifi_getApStatus() api.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_261</test_case_id>
    <test_objective>To get the Ap status for 2.4GHz and invoke wifi_ifConfigDown() if the status is 'Up' or invoke wifi_ifConfigUp() if the status is 'Disable' and validate the same using wifi_getApStatus() api.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_ifConfigUp()
wifi_ifConfigDown()
wifi_getApStatus()</api_or_interface_used>
    <input_parameters>methodName : ifConfigUp
methodName : ifConfigDown
methodName : getApStatus
apIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Get the Ap status using wifi_getApStatus() api.
3a.If the status is 'Up',invoke wifi_ifConfigDown() api  and check whether the status is changed to 'Disable' by invoking wifi_getApStatus() api.
3b..Invoke wifi_ifConfigUp() api to change the status back to 'Up' and validate the same using wifi_getApStatus() api.
3c.If status is 'Up',return SUCCESS,else FAILURE.
4a.If the status is 'Disable',invoke wifi_ifConfigUp() api and check whether the status is changed to 'Up' by  invoking wifi_getApStatus() api.
4b.Invoke wifi_ifConfigDown() api to change the status back to 'Disable' and validate the same using wifi_getApStatus() api.
4c.If status is 'Disable',return SUCCESS,else FAILURE.
5.Unload the module.</automation_approch>
    <except_output>The Ap status should change to 'Up', if we invoke wifi_ifConfigUp() api and Ap status should change to 'Disable', if we invoke wifi_ifConfigDown() api for 2.4GHz</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzIfConfigUpOrDown</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzIfConfigUporDown');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
def GetApStatus():
    expectedresult="SUCCESS";
    apIndex = 0
    getMethod = "getApStatus"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        tdkTestObj.setResultStatus("FAILURE");
    return (tdkTestObj, actualresult, details);    

def IfConfigDown():
    #Primitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIHAL_IfConfigUporDown');
    #Giving the method name to invoke the api wifi_ifConfigDown()
    tdkTestObj.addParameter("methodName","ifConfigDown");
    #Ap index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("apIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print"TEST STEP:To invoke the wifi_ifConfigDown() api for 2.4GHz";
        print"EXPECTED RESULT:wifi_ifConfigDown() api should return SUCCESS for 2.4GHz";
        print"ACTUAL RESULT:%s"%details;
        print"[TEST EXECUTION RESULT]:SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print"TEST STEP:To invoke the wifi_ifConfigDown() api for 2.4GHz";
        print"EXPECTED RESULT:wifi_ifConfigDown() api should return SUCCESS for 2.4GHz";
        print"ACTUAL RESULT:%s"%details;
        print"[TEST EXECUTION RESULT]:FAILURE";
    return (tdkTestObj, actualresult, details);

def IfConfigUp():
    #Primitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIHAL_IfConfigUporDown');
    #Giving the method name to invoke the api wifi_ifConfigUp()
    tdkTestObj.addParameter("methodName","ifConfigUp");
    #Ap index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("apIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print"TEST STEP:To invoke the wifi_ifConfigUp() api for 2.4GHz";
        print"EXPECTED RESULT:wifi_ifConfigUp() api should return SUCCESS for 2.4GHz";
        print"ACTUAL RESULT:%s"%details;
        print"[TEST EXECUTION RESULT]:SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print"TEST STEP:To invoke the wifi_ifConfigUp() api for 2.4GHz";
        print"EXPECTED RESULT:wifi_ifConfigUp() api should return SUCCESS for 2.4GHz";
        print"ACTUAL RESULT:%s"%details;
        print"[TEST EXECUTION RESULT]:FAILURE";
    return (tdkTestObj, actualresult, details);
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj, actualresult, details =  GetApStatus();
    status_initial = details.split(":")[1].strip();
    if status_initial == 'Up':
        print"Calling the wifi_ifConfigDown() api";
        IfConfigDown();
        tdkTestObj, actualresult, details =  GetApStatus();
        status_down = details.split(":")[1].strip();
        if status_down == 'Disable':
            tdkTestObj.setResultStatus("SUCCESS");
            print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigDown() api";
            print"EXPECTED RESULT:Ap status should change to 'Disable' for 2.4GHz";
            print"ACTUAL RESULT:Ap staus changed to 'Disable' for 2.4GHz";
            print"[TEST EXECUTION RESULT]:SUCCESS";
            print"Calling the wifi_ifConfigUp() api for reverting the ApStatus back to initial value";
            IfConfigUp();
            tdkTestObj, actualresult, details =  GetApStatus();
            status_up = details.split(":")[1].strip();
            if status_up == 'Up':
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigUp() api for reverting the ApStatus back to initial value";
                print"EXPECTED RESULT:Ap status should change to 'Up' for 2.4GHz";
                print"ACTUAL RESULT:Ap staus changed to 'Up' for 2.4GHz";
                print"[TEST EXECUTION RESULT]:SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigUp() api for reverting the ApStatus back to initial value";
                print"EXPECTED RESULT:Ap status should change to 'Up' for 2.4GHz";
                print"ACTUAL RESULT:Ap staus is not changed to 'Up' for 2.4GHz";
                print"[TEST EXECUTION RESULT]:FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigDown() api";
            print"EXPECTED RESULT:Ap status should change to 'Disable' for 2.4GHz";
            print"ACTUAL RESULT:Ap staus is not changed to 'Disable' for 2.4GHz";
            print"[TEST EXECUTION RESULT]:FAILURE";
    elif status_initial == 'Disable':
        print"Calling the wifi_ifConfigUp() api";
        IfConfigUp();
        tdkTestObj, actualresult, details =  GetApStatus();
        status_up = details.split(":")[1].strip();
        if status_up == 'Up':
            tdkTestObj.setResultStatus("SUCCESS");
            print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigUp() api";
            print"EXPECTED RESULT:Ap status should change to 'Up' for 2.4GHz";
            print"ACTUAL RESULT:Ap staus changed to 'Up' for 2.4GHz";
            print"[TEST EXECUTION RESULT]:SUCCESS";
            print"Calling the wifi_ifConfigDown() api for reverting the ApStatus back to initial value";
            IfConfigDown();
            tdkTestObj, actualresult, details =  GetApStatus();
            status_down = details.split(":")[1].strip();
            if status_down == 'Disable':
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigDown() api for reverting the ApStatus back to initial value";
                print"EXPECTED RESULT:Ap status should change to 'Disable' for 2.4GHz";
                print"ACTUAL RESULT:Ap staus changed to 'Disable' for 2.4GHz";
                print"[TEST EXECUTION RESULT]:SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigDown() api for reverting the ApStatus back to initial value";
                print"EXPECTED RESULT:Ap status should change to 'Disable' for 2.4GHz";
                print"ACTUAL RESULT:Ap staus is not changed to 'Disable' for 2.4GHz";
                print"[TEST EXECUTION RESULT]:FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"TEST STEP:Get the Ap Status to validate whether the status has changed after invoking wifi_ifConfigUp() api";
            print"EXPECTED RESULT:Ap status should change to 'Up' for 2.4GHz";
            print"ACTUAL RESULT:Ap staus is not changed to 'Up' for 2.4GHz";
            print"[TEST EXECUTION RESULT]:FAILURE";
    else:
        print"Get Ap Status is not returning value from list of Ap Status ['Up', 'Disable']";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
