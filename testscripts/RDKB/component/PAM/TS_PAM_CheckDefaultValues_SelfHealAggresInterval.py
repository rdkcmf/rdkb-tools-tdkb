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
  <version>1</version>
  <name>TS_PAM_CheckDefaultValues_SelfHealAggresInterval</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the default value of Self heal aggressive on Factory reset</synopsis>
  <groups_id/>
  <execution_time>220</execution_time>
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
    <test_case_id>TC_PAM_189</test_case_id>
    <test_objective>This test case is to check the default value of Self heal aggressive on Factory reset </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval
Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow</input_parameters>
    <automation_approch>1.Load the module
2.Perform Factory reset on the device
3.Get the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval
Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow
4.Check if SelfHealAggressive.txt file is present
5.Toggle the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval and check if the same is logged in SelfHealAggressive.txt
6.Revert the set value
7.Unload the module</automation_approch>
    <expected_output>the parameter should have the expected default value</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckDefaultValues_SelfHealAggresInterval</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
obj1 = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
obj2= tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckDefaultValues_SelfHealAggresInterval');
obj1.configureTestCase(ip,port,'TS_PAM_CheckDefaultValues_SelfHealAggresInterval');
obj2.configureTestCase(ip,port,'TS_PAM_CheckDefaultValues_SelfHealAggresInterval');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 =obj2.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    #save device's current state before it goes for reboot
    tdkTestObj = obj1.createTestStep('WIFIAgent_Set');
    obj1.saveCurrentState();
    #Initiate Factory reset before checking the default value
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("paramType","string");
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
       sleep(180);

       paramList = ["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow"];
       expectedValue = ["5","15"];
       i=0;
       result =[];
       for item in paramList:
           tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
           tdkTestObj.addParameter("ParamName",item);
           expectedresult="SUCCESS";
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails();
           details = details.strip().replace("\\n", "");
           result.append(actualresult);
           if expectedresult in actualresult and details == expectedValue[i]:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP : Query %s and should be equal to %s" %(item,expectedValue[i]);
               print "ACTUAL RESULT : Should get %s received %s after Factory Reset" %(expectedValue[i],details);
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP : Query %s and should be equal to %s" %(item,expectedValue[i]);
               print "ACTUAL RESULT :  Should get %s received %s after Factory Reset" %(expectedValue[i],details);
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
           i =i+1;

       print result;
       if  "FAILURE" not in result:
           tdkTestObj = obj2.createTestStep('ExecuteCmd');
           cmd = "[ -f /rdklogs/logs/SelfHealAggressive.txt ] && echo \"File exist\" || echo \"File does not exist\"";
           tdkTestObj.addParameter("command",cmd);
           expectedresult="SUCCESS";
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
           if details == "File exist":
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Check for SelfHealAggressive log file presence";
              print "EXPECTED RESULT 3:SelfHealAggressive log file should be present";
              print "ACTUAL RESULT 3:SelfHealAggressive log file is present";
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";

              tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
              tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval")
              tdkTestObj.addParameter("ParamValue","6");
              tdkTestObj.addParameter("Type","unsignedint");
              expectedresult= "SUCCESS";

              #Execute testcase on DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              Setresult = tdkTestObj.getResultDetails();
              if expectedresult in actualresult:
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 4: Set SelfHealAggressive Interval to 6 min";
                  print "EXPECTED RESULT 4: Should set SelfHealAggressive Interval to 6 min";
                  print "ACTUAL RESULT 4 : %s" %Setresult;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";
                  #Wait for 2 sec for logging to take place
                  sleep(2);

                  tdkTestObj = obj2.createTestStep('ExecuteCmd');
                  cmd = "grep -i \"INTERVAL is: 6\" /rdklogs/logs/SelfHealAggressive.txt";
                  tdkTestObj.addParameter("command",cmd);
                  expectedresult="SUCCESS";
                  tdkTestObj.executeTestCase(expectedresult);
                  actualresult = tdkTestObj.getResult();
                  details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                  if expectedresult in actualresult :
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 5: Check for Self Heal Aggressive Interval logged in log file";
                      print "EXPECTED RESULT 5:Self Heal Aggressive Interval should be logged in log file";
                      print "ACTUAL RESULT 5: Search for the log was success";
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      if "INTERVAL is: 6"  in details:
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 6: Check for Self Heal Aggressive Interval logged with the interval set i,e 6";
                          print "EXPECTED RESULT 6:Self Heal Aggressive Interval should be logged in log file with the interval set i,e 6";
                          print "ACTUAL RESULT 6: %s" %details;
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 6: Check for Self Heal Aggressive Interval logged with the interval set i,e 6";
                          print "EXPECTED RESULT 6:Self Heal Aggressive Interval should be logged in log file with the interval set i,e 6";
                          print "ACTUAL RESULT 6: Failed to log the expected log message";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                  else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print "TEST STEP 5: Check for Self Heal Aggressive Interval logged in log file";
                      print "EXPECTED RESULT 5:Self Heal Aggressive Interval should be logged in log file";
                      print "ACTUAL RESULT 5:Failed to log the expected to set log interval" ;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : FAILURE";

                  #Revert to previous
                  tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                  tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval")
                  #5 is known default value
                  tdkTestObj.addParameter("ParamValue","5");
                  tdkTestObj.addParameter("Type","unsignedint");
                  expectedresult= "SUCCESS";
                  #Execute testcase on DUT
                  tdkTestObj.executeTestCase(expectedresult);
                  actualresult = tdkTestObj.getResult();
                  Setresult = tdkTestObj.getResultDetails();
                  if expectedresult in actualresult:
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 7: Revert the SelfHealAggressive Interval to default";
                      print "EXPECTED RESULT 7: Should revert SelfHealAggressive Interval to 5  min";
                      print "ACTUAL RESULT 5 : %s" %Setresult;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                  else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print "TEST STEP 7: Revert the SelfHealAggressive Interval to default";
                      print "EXPECTED RESULT 7: Should revert SelfHealAggressive Interval to 5  min";
                      print "ACTUAL RESULT 7 : %s" %Setresult;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : FAILURE";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4: Set SelfHealAggressive Interval to 6 min";
                  print "EXPECTED RESULT 4: Should set SelfHealAggressive Interval to 6 min";
                  print "ACTUAL RESULT 4 : %s" %Setresult;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Check for SelfHealAggressive log file presence";
               print "EXPECTED RESULT 3:SelfHealAggressive log file should be present";
               print "ACTUAL RESULT 3:SelfHealAggressive log file is not present";
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("wifiagent");
    obj2.unloadModule("sysutil");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
     obj1.setLoadModuleStatus("FAILURE");
     obj2.setLoadModuleStatus("FAILURE");
