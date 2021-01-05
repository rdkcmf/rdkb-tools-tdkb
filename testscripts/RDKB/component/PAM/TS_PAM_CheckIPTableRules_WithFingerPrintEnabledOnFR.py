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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_PAM_CheckIPTableRules_WithFingerPrintEnabledOnFR</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if finger print is enabled and finger print specific iptable rules are present on a Factory reset</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_PAM_200</test_case_id>
    <test_objective>This test case is to check if finger print is enabled and finger print specific iptable rules are present on a Factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues
ExecuteCmd</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset
Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Perform factory reset on the device
3.Check if  Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable is enabled by default
4.Check if all the finger print enable related iptable rules are present
5.Unload the module</automation_approch>
    <expected_output>On FR all the iptable rules related to finger print should be present and also finger print should be enabled by default</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckIPTableRules_WithFingerPrintEnabledOnFR</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_PAM_CheckIPTableRules_WithFingerPrintEnabledOnFR');
sysobj.configureTestCase(ip,port,'TS_PAM_CheckIPTableRules_WithFingerPrintEnabledOnFR');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus ;

def verify_iptable_rules(tdkTestObj):
    rulesFound = 0;
    cmd = "sh %s/tdk_utility.sh parseConfigFile FINGER_PRINT_IPTABLE_RULES  | tr \"\n\" \"  \"" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult  and details!= "":
       iptable_list = details.split(",");
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP : Execute the command";
       print "EXPECTED RESULT : Should execute the command successfully";
       print "ACTUAL RESULT : Details: %s" %details;
       print "[TEST EXECUTION RESULT] : SUCCESS";

       for list in iptable_list:
           cmd = "iptables-save | grep  -ire \"%s\"" %list;
           tdkTestObj.addParameter("command",cmd);
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
           if expectedresult in actualresult and details == list:
              rulesFound = 1;
           else:
               rulesFound = 0;
               print "Iptable Rule %s is NOT present"%list
               break;
    return rulesFound,actualresult;

if "SUCCESS" in (loadmodulestatus.upper() and sysutilloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    obj.saveCurrentState();
    #Initiate Factory reset before checking the default value
    tdkTestObj = obj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();

        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        initial_value = tdkTestObj.getResultDetails().strip();

        if expectedresult in actualresult and initial_value == "true":
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Get current value of Device FingerPrint Enable"
           print "EXPECTED RESULT 2: Should get current value of Device FingerPrint Enable"
           print "ACTUAL RESULT 2: current value is %s" %initial_value;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS"

           tdkTestObj = sysobj.createTestStep('ExecuteCmd');
           result,actualresult= verify_iptable_rules(tdkTestObj);

           if result == 1 and expectedresult in actualresult:
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Verify iptables rules for  Device FingerPrint Enable"
              print "EXPECTED RESULT 3: The iptables rules specific to Device FingerPrint Enable should be present"
              print "ACTUAL TEST 3: Verification on the iptables rules specific to Device FingerPrint Enable is success"
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS"
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Verify iptables rules for  Device FingerPrint Enable"
               print "EXPECTED RESULT 3: The iptables rules specific to Device FingerPrint Enable should be present"
               print "ACTUAL TEST 3: Verification on the iptables rules specific to Device FingerPrint Enable Failed";
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get current value of Device FingerPrint Enable"
            print "EXPECTED RESULT 2: Should get current value of Device FingerPrint Enable"
            print "ACTUAL RESULT 2: current value is %s" %initial_value;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
