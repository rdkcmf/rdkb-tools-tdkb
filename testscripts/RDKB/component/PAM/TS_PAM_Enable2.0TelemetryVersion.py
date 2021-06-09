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
  <name>TS_PAM_Enable2.0TelemetryVersion</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To enable 2.0 telemetry and check if telemetry2_0 is running</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_PAM_164</test_case_id>
    <test_objective>This test case is to enable 2.0 telemetry and check if telemetry2_0 is running</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable</input_parameters>
    <automation_approch>1.Load the module
2. Get the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable status if disabled ,enable it.
3.Get the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version and should be 2.0.1 on enabling telemetry version.
4.set the Config URL using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL
5Initiate a Reboot
6.Check if telemetry2_0.txt.0 file is present
7.Check the  pidof telemetry2_0 and should be running.
8.Revert the  set parameters to previous.
9.Unload the module</automation_approch>
    <expected_output>On Enabling telemetry and after a successful reboot   telemetry2_0 should be running</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_Enable2.0TelemetryVersion</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_Enable2.0TelemetryVersion');
obj1.configureTestCase(ip,port,'TS_PAM_Enable2.0TelemetryVersion');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();
setflag = 1;
revertflag =0;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Telemetry Enable status";
       print "EXPECTED RESULT 1: Should get the Telemetry Enable status";
       print "ACTUAL RESULT 1: Telemetry Enable status is:",default
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       if default != "true":
          tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable");
          tdkTestObj.addParameter("ParamValue","true");
          tdkTestObj.addParameter("Type","bool");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();

          if expectedresult in actualresult:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Set the Telemetry Enable status to true";
             print "EXPECTED RESULT 2: Should set the Telemetry Enable status to true";
             print "ACTUAL RESULT 2: Telemetry Enable status is:",details
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
             revertflag =1;
          else:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Set the Telemetry Enable status to true";
             print "EXPECTED RESULT 2: Should set the Telemetry Enable status to true";
             print "ACTUAL RESULT 2: Telemetry Enable status is:",details
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
             setflag =0;

       if setflag ==1:
          tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          telver = tdkTestObj.getResultDetails();
          if expectedresult in actualresult and telver == "2.0.1":
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the current Telemetry version in the DUT after Telemetry Enable ";
             print "EXPECTED RESULT 3: Should get the current Telemetry version as 2.0.1 in the DUT"
             print "ACTUAL RESULT 3: ",telver;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
             tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL");
             expectedresult="SUCCESS";
             #Execute the test case in DUT
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             defURL = tdkTestObj.getResultDetails();
             if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Get the current Telemetry ConfigURL";
                print "EXPECTED RESULT 4: Should get the current Telemetry ConfigURL";
                print "ACTUAL RESULT 4: ",defURL;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL");
                tdkTestObj.addParameter("ParamValue",TEL_CONFIG_URL);
                tdkTestObj.addParameter("Type","string");
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 5: Set the Telemetry ConfigURL";
                   print "EXPECTED RESULT 5: Should set the Telemetry ConfigURL";
                   print "ACTUAL RESULT 5: ",details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                   print "***************************************************"
                   print "Initiating Reboot Please wait till the device comes up";
                   print"*******************************************************"
                   obj.initiateReboot();
                   sleep(300);
                   tdkTestObj = obj.createTestStep('ExecuteCmd');
                   cmd= "[ -f /rdklogs/logs/telemetry2_0.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
                   expectedresult="SUCCESS";
                   tdkTestObj.addParameter("command",cmd);
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                   if details == "File exist" :
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 6: Check for telemetry2_0.txt.0  log file presence";
                      print "EXPECTED RESULT 6: telemetry2_0.txt.0 log file should be present";
                      print "ACTUAL RESULT 6: telemetry2_0.txt.0 file is present";
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      tdkTestObj = obj.createTestStep('ExecuteCmd');
                      cmd = "pidof telemetry2_0";
                      expectedresult="SUCCESS";
                      tdkTestObj.addParameter("command",cmd);
                      tdkTestObj.executeTestCase(expectedresult);
                      actualresult = tdkTestObj.getResult();
                      details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                      if expectedresult in actualresult and details != "":
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 7: Check if telemetry2_0 process is running";
                         print "EXPECTED RESULT 7:telemetry2_0  process should be running";
                         print "ACTUAL RESULT 7: pid of telemetry2_0",details;
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 7: Check if telemetry2_0 process is running";
                          print "EXPECTED RESULT 7:telemetry2_0  process should be running";
                          print "ACTUAL RESULT78: pid of telemetry2_0",details;
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 6: Check for telemetry2_0.txt.0  log file presence";
                       print "EXPECTED RESULT 6: telemetry2_0.txt.0 log file should be present";
                       print "ACTUAL RESULT 6: telemetry2_0.txt.0 file is not present";
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                   #Revert the URL
                   tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
                   tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL");
                   tdkTestObj.addParameter("ParamValue",defURL);
                   tdkTestObj.addParameter("Type","string");
                   expectedresult="SUCCESS";
                   #Execute the test case in DUT
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();

                   if expectedresult in actualresult:
                      #Set the result status of execution
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 8: Revert the Telemetry ConfigURL to previous";
                      print "EXPECTED RESULT 8: Should revert the Telemetry ConfigURL";
                      print "ACTUAL RESULT 8: ",details;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                   else:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 8: Revert the Telemetry ConfigURL to previous";
                       print "EXPECTED RESULT 8: Should revert the Telemetry ConfigURL";
                       print "ACTUAL RESULT 8: ",details;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Set the Telemetry ConfigURL";
                    print "EXPECTED RESULT 5: Should set the Telemetry ConfigURL";
                    print "ACTUAL RESULT 5: ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Get the current Telemetry ConfigURL";
                 print "EXPECTED RESULT 4: Should get the current Telemetry ConfigURL";
                 print "ACTUAL RESULT 4: ",defURL;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Get the current Telemetry version in the DUT after Telemetry Enable";
              print "EXPECTED RESULT 3: Should get the current Telemetry version in the DUT"
              print "ACTUAL RESULT 3: ",telver;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "telemetry was disabled and failed on enabling";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Telemetry Enable status";
        print "EXPECTED RESULT 1: Should get the Telemetry Enable status";
        print "ACTUAL RESULT 1: Telemetry Enable status is:",default
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    if revertflag ==1:
       tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable");
       tdkTestObj.addParameter("ParamValue",default);
       tdkTestObj.addParameter("Type","bool");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();

       if expectedresult in actualresult:
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 9:Revert the telemetry enable status to previous";
          print "EXPECTED RESULT 9: Should revert the telemetry enable status to previous";
          print "ACTUAL RESULT 9: Revertion was successful";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version")
          expectedresult= "SUCCESS";
          #Execute testcase on DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();
          if expectedresult in actualresult and int(details) == 1:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 10:Check if the Telemetry version is 1.0  after disabling Telemetry";
             print "EXPECTED RESULT 10: Telemetry version should be 1.0  after disabling Telemetry";
             print "ACTUAL RESULT 10:",details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 10:Check if the Telemetry version is 1.0  after disabling Telemetry";
              print "EXPECTED RESULT 10: Telemetry version should be 1.0  after disabling Telemetry";
              print "ACTUAL RESULT 10: ",details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 9:Revert the telemetry enable status to previous";
          print "EXPECTED RESULT 9: Should revert the telemetry enable status to previous";
          print "ACTUAL RESULT 9: Revertion failed";
          print "[TEST EXECUTION RESULT] : FAILURE";
    obj1.unloadModule("tdkbtr181");
    obj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
