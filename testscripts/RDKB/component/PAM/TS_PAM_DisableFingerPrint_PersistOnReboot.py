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
  <version>3</version>
  <name>TS_PAM_DisableFingerPrint_PersistOnReboot</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To disable finger print status and check if it persists on reboot</synopsis>
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
    <test_case_id>TC_PAM_203</test_case_id>
    <test_objective>To disable finger print status and check if it persists on reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable</input_parameters>
    <automation_approch>1.Load the module
2.get the current status of Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable
3.Disable the Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable
4.Reboot the device
5.Check if Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable value persists and no iptable rules related to it are present
6.Revert the set value to previous
7.Unload the module</automation_approch>
    <expected_output>The set value and iptable rules should persist across reboot when disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_DisableFingerPrint_PersistOnReboot</test_script>
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
obj.configureTestCase(ip,port,'TS_PAM_DisableFingerPrint_PersistOnReboot');
sysobj.configureTestCase(ip,port,'TS_PAM_DisableFingerPrint_PersistOnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus ;
revert =0;
def verify_iptable_rules(tdkTestObj):
       rulesFound =1;
       cmd = "iptables-save | grep -rn \"FINGER\"";
       print cmd;
       tdkTestObj.addParameter("command",cmd);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if expectedresult in actualresult and details == "":
          pass;
       else:
           rulesFound = 0;
           print "Iptable Rule %s is  present"%details
       return rulesFound;

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

        setValue = "false";
        if initial_value != "false":
           tdkTestObj = obj.createTestStep('pam_SetParameterValues');
           actualresult,result=setFunction(tdkTestObj,setValue);
           if expectedresult in actualresult:
              revert = 1;
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 2: Set Device FingerPrint Enable status to false"
              print "EXPECTED RESULT 2: Should set Device FingerPrint Enable status to false"
              print "ACTUAL RESULT 2: %s" %result;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS"
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2: Set Device FingerPrint Enable status to false"
               print "EXPECTED RESULT 2: Should set Device FingerPrint Enable status to false"
               print "ACTUAL RESULT 2: %s" %result;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
               setValue = "failed";

        if "false" == setValue:
           sleep(60);
           tdkTestObj = sysobj.createTestStep('ExecuteCmd');
           result= verify_iptable_rules(tdkTestObj);

           if result == 1:
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Verify iptables rules for  Device FingerPrint Enable when disabled"
              print "EXPECTED RESULT 3: The iptables rules specific to Device FingerPrint when Disabled should not be present"
              print "ACTUAL TEST 3: Verification on the iptables rules specific to Device FingerPrint Disable is success"
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS"

              obj.initiateReboot();
              sleep(300);

              tdkTestObj = obj.createTestStep('pam_GetParameterValues');
              tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
              expectedresult="SUCCESS";

              #Execute the test case in DUT
              tdkTestObj.executeTestCase("expectedresult");
              actualresult = tdkTestObj.getResult();
              valueOnReboot = tdkTestObj.getResultDetails().strip();
              if expectedresult in actualresult and valueOnReboot == setValue:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 4: Get current value of Device FingerPrint Enable after reboot"
                 print "EXPECTED RESULT 4: Should get current value of Device FingerPrint Enable after reboot should be equal to set value";
                 print "ACTUAL RESULT 4: current value is %s and setValues is %s" %(valueOnReboot,setValue);
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS"

                 tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                 result= verify_iptable_rules(tdkTestObj);

                 if result == 1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Verify iptables rules for  Device FingerPrint Disable after reboot"
                    print "EXPECTED RESULT 5: The iptables rules specific to Device FingerPrint after reboot should not be present"
                    print "ACTUAL TEST 5: Verification on the iptables rules specific to Device FingerPrint after reboot is success"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                 else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 5: Verify iptables rules for  Device FingerPrint Disable after reboot"
                     print "EXPECTED RESULT 5: The iptables rules specific to Device FingerPrint when after reboot should not be present"
                     print "ACTUAL TEST 5: Verification on the iptables rules specific to Device FingerPrint after reboot is failed"
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE"
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4: Get current value of Device FingerPrint Enable after reboot"
                  print "EXPECTED RESULT 4: Should get current value of Device FingerPrint Enable after reboot should be equal to set value"
                  print "ACTUAL RESULT 4: current value is %s and setValue is %s" %(valueOnReboot,setValue);
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE"
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Verify iptables rules for  Device FingerPrint Enable when disabled"
               print "EXPECTED RESULT 3: The iptables rules specific to Device FingerPrint when Disabled should not be present"
               print "ACTUAL TEST 3: Verification on the iptables rules specific to Device FingerPrint Disable failed"
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";

           #Revert the value
           if revert == 1:
              tdkTestObj = obj.createTestStep('pam_SetParameterValues');
              actualresult,result=setFunction(tdkTestObj,initial_value);
              if expectedresult in actualresult:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 6: Revert the Device FingerPrint Enable status to previous"
                  print "EXPECTED RESULT 6: Should revert  Device FingerPrint Enable status to %s" %initial_value
                  print "ACTUAL RESULT 6: %s" %result;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS"
                  sleep(60);
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 6: Revert the Device FingerPrint Enable status to previous"
                  print "EXPECTED RESULT 6: Should revert  Device FingerPrint Enable status to %s" %initial_value
                  print "ACTUAL RESULT 6: %s" %result;
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
