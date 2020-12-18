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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_ForceDisable_CheckRadioEnable_AfterFR</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To enable WIFI Force Disable and check if to goes to default on Factory Reset.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <test_case_id>TC_WIFIAGENT_127</test_case_id>
    <test_objective>This test case is to enable WIFI Force Disable and check if to goes to default on Factory Reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get
WIFIAgent_Set</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
Device.WiFi.Radio.1.Enable
Device.WiFi.Radio.2.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Get the Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
3.Enable Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
4.Check if  Device.WiFi.Radio.1.Enable
Device.WiFi.Radio.2.Enable are disabled
5.Initiate a Factory reset on the DUT
6.Check if Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is disabled and Device.WiFi.Radio.1.Enable,Device.WiFi.Radio.2.Enable are enabled by default
7.Unload the module</automation_approch>
    <expected_output>On factory reset and Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable should go to default value and the same should be reflected in Device.WiFi.Radio.1.Enable,Device.WiFi.Radio.2.Enable</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_ForceDisable_CheckRadioEnable_AfterFR</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_WIFIAGENT_ForceDisable_CheckRadioEnable_AfterFR');

#result of connection with test component and DUT
result =obj.getLoadModuleResult();

loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
       #Set the result status of execution
       obj.setLoadModuleStatus("SUCCESS")
       expectedresult = "SUCCESS";
       tdkTestObj = obj.createTestStep('WIFIAgent_Set');
       tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
       tdkTestObj.addParameter("paramValue", "true");
       tdkTestObj.addParameter("paramType","boolean")
       tdkTestObj.executeTestCase("expectedresult");
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();

       if expectedresult in actualresult:
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 1: Enable the WiFi Force Disable";
          print "EXPECTED RESULT 1: Should enable Force Disable state";
          print "ACTUAL RESULT 1: %s" %details;
          print "[TEST EXECUTION RESULT] : SUCCESS";

          tdkTestObj = obj.createTestStep('WIFIAgent_Get');
          tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable")
          tdkTestObj.executeTestCase("expectedresult");
          actualresult = tdkTestObj.getResult();
          Radio1 = tdkTestObj.getResultDetails();
          if expectedresult in actualresult and "false" in Radio1:
             Radio1 = Radio1.split("VALUE:")[1].split(" ")[0].strip();
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Get the Radio Enable status for 2.4GHz as false";
             print "EXPECTED RESULT 2: Should get the Radio Enable status for 2.4GHz as false";
             print "ACTUAL RESULT 2: Radio Enable status for 2.4GHz state is %s" %Radio1;
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = obj.createTestStep('WIFIAgent_Get');
             tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Enable")
             tdkTestObj.executeTestCase("expectedresult");
             actualresult = tdkTestObj.getResult();
             Radio2 = tdkTestObj.getResultDetails();
             if expectedresult in actualresult and "false" in Radio2:
                Radio2 = Radio2.split("VALUE:")[1].split(" ")[0].strip();
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the Radio Enable status for 5GHz as false";
                print "EXPECTED RESULT 3: Should get the Radio Enable status for 5GHz as false";
                print "ACTUAL RESULT 3: Radio Enable status for 5GHz state is %s" %Radio2;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #save device's current state before it goes for reboot
                obj.saveCurrentState();

                #Initiate Factory reset before checking the default value
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
                tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
                tdkTestObj.addParameter("paramType","string");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 4: Initiate factory reset ";
                   print "ACTUAL RESULT 4: %s" %details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                   #Restore the device state saved before reboot
                   obj.restorePreviousStateAfterReboot();
                   #waiting for device to restore state  after reboot
                   print "Waiting for device to restore previous state after reboot";
                   sleep(180);

                   tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                   tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
                   tdkTestObj.executeTestCase("expectedresult");
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();
                   if expectedresult in actualresult and "false" in details:
                      details = details.split("VALUE:")[1].split(" ")[0].strip();
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 5: Check if  WiFi Force Disable is false after Factory Reset";
                      print "EXPECTED RESULT 5: Should get WiFi Force Disable  as false";
                      print "ACTUAL RESULT 5: %s" %details;
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                      tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable")
                      tdkTestObj.executeTestCase("expectedresult");
                      actualresult = tdkTestObj.getResult();
                      details = tdkTestObj.getResultDetails();
                      if expectedresult in actualresult and "true" in details:
                         details = details.split("VALUE:")[1].split(" ")[0].strip();
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 6: Check if Radio enable status for 2.4GHz is true after Factory reset";
                         print "EXPECTED RESULT 6: Radio enable status for 2.4GHz should be true after Factory reset";
                         print "ACTUAL RESULT 6: default value is :%s" %details
                         print "[TEST EXECUTION RESULT] : SUCCESS";

                         tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                         tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Enable")
                         tdkTestObj.executeTestCase("expectedresult");
                         actualresult = tdkTestObj.getResult();
                         details = tdkTestObj.getResultDetails();
                         if expectedresult in actualresult and  "true" in details:
                            details = details.split("VALUE:")[1].split(" ")[0].strip();
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 7: Check if Radio enable status for 5GHz is true after Factory reset";
                            print "EXPECTED RESULT 7: Radio enable status for 5GHz should be true after Factory reset";
                            print "ACTUAL RESULT 7: default value is : %s" %details
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                         else:
                             tdkTestObj.setResultStatus("FAILURE");
                             print "TEST STEP 7: Check if Radio enable status for 5GHz is true after Factory reset";
                             print "EXPECTED RESULT 7: Radio enable status for 5GHz should be true after Factory reset";
                             print "ACTUAL RESULT 7: default value is :%s" %details
                             print "[TEST EXECUTION RESULT] : FAILURE";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 6: Check if Radio enable status for 2.4GHz is true after Factory reset";
                          print "EXPECTED RESULT 6: Radio enable status for 2.4GHz should be true after Factory reset";
                          print "ACTUAL RESULT 6: default value is :%s" %details
                          print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 5: Check if  WiFi Force Disable is false after Factory Reset";
                       print "EXPECTED RESULT 5: Should get WiFi Force Disable  as false";
                       print "ACTUAL RESULT 5: %s" %details;
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Initiate factory reset ";
                    print "ACTUAL RESULT 4: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Get the Radio Enable status for 5GHz as false";
                 print "EXPECTED RESULT 3: Should get the Radio Enable status for 5GHz as false";
                 print "ACTUAL RESULT 3: Radio Enable status for 5GHz state is %s" %Radio2;
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Get the Radio Enable status for 2.4GHz as false";
              print "EXPECTED RESULT 2: Should get the Radio Enable status for 2.4GHz as false";
              print "ACTUAL RESULT 2: Radio Enable status for 2.4GHz state is %s" %Radio1;
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 1: Enable the WiFi Force Disable";
           print "EXPECTED RESULT 1: Should enable Force Disable state";
           print "ACTUAL RESULT 1: %s" %details;
           print "[TEST EXECUTION RESULT] : FAILURE";
       obj.unloadModule("wifiagent")
else:
    print "Failed to load wifiagent module";
    obj.setLoadModuleStatus("FAILURE");
