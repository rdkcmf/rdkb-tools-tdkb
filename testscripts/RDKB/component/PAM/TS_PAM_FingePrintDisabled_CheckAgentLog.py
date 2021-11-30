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
  <version>1</version>
  <name>TS_PAM_FingePrintDisabled_CheckAgentLog</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To disable finger print and check if expected  messages are logged in.</synopsis>
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
    <test_case_id>TC_PAM_229</test_case_id>
    <test_objective>To disable finger print and check if expected  messages are logged in</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current finger print enable status
3.Disable the finger print and check if expected messaged are logged
4.Mark the script as success if expected log messages are present else mark the script as failure
5.Revert the set value
6.Unload the module</automation_approch>
    <expected_output>expected log messages should be logged when finger print is disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_FingePrintDisabled_CheckAgentLog</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_FingePrintDisabled_CheckAgentLog');
sysobj.configureTestCase(ip,port,'TS_PAM_FingePrintDisabled_CheckAgentLog');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus ;

def setFunction(tdkTestObj,set_value):
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
    tdkTestObj.addParameter("ParamValue",set_value);
    tdkTestObj.addParameter("Type","boolean");
    expectedresult="SUCCESS";
    #Execute testcase on DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    result = tdkTestObj.getResultDetails();
    return actualresult, result;

if "SUCCESS" in (loadmodulestatus.upper() and sysutilloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    initial_value = tdkTestObj.getResultDetails().strip();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get current value of Device FingerPrint Enable"
        print "EXPECTED RESULT 1: Should get current value of Device FingerPrint Enable"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
        actualresult,result=setFunction(tdkTestObj,"false");
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set Device FingerPrint Enable status to false"
            print "EXPECTED RESULT 2: Should set Device FingerPrint Enable status to false"
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            sleep(60);
            logMsgs =["ignoring cloud's attempt to enable fingerprint","ADVANCED_SECURITY_CLOUD_SECURITY_ASSOC_SUCCESS"];

            print "TEST STER 3 : The following log msgs are expected to be present on Disabling finger print ";
            print "\n%s \n" %logMsgs;
            print "EXPECTED RESULT 3 : The above listed log message should be logged in agent.txt";
            flag =1;
            for item in logMsgs:
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "cat /rdklogs/logs/agent.txt | grep -rn \"%s\""%item;
                print cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and details !="":
                   print "\nACTUAL RESULT :  log message found : %s" %details;
                else:
                     print "\n ACTUAL RESULT : log message %s not found" %item;
                     flag  =0;
            if flag == 1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set Device FingerPrint Enable status to false"
            print "EXPECTED RESULT 2: Should set Device FingerPrint Enable status to false"
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #revert the value
        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
        actualresult,result=setFunction(tdkTestObj,initial_value);
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 4: Revert the Device FingerPrint Enable status to previous"
            print "EXPECTED RESULT 4: Should revert  Device FingerPrint Enable status to %s" %initial_value
            print "ACTUAL RESULT 4: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            sleep(60);
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Revert the Device FingerPrint Enable status to previous"
            print "EXPECTED RESULT 4: Should revert  Device FingerPrint Enable status to %s" %initial_value
            print "ACTUAL RESULT 4: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get current value of Device FingerPrint Enable"
        print "EXPECTED RESULT 1: Should get current value of Device FingerPrint Enable"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
