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
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ETHWAN_GetCurAndLastOperMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>EthWAN_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check the Current operational mode and Last operational mode based on the status of Wan Enabled .</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_ETHWAN_22</test_case_id>
    <test_objective>This test case is to check the Current operational mode and Last operational  mode by checking on the status of WAN Enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled
Device.X_RDKCENTRAL-COM_EthernetWAN.CurrentOperationalMode</input_parameters>
    <automation_approch>1.Load Module
2.Check the status of WAN Enabled using Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled
3.If WAN Enabled then the operational mode is expected to be ETHERNET else DOCSIS.
4.Get the Current operational mode using Device.X_RDKCENTRAL-COM_EthernetWAN.CurrentOperationalMode and check if the value sync's based on WAN Enabled status.
5.Get the last knowm operational mode using Device.X_RDKCENTRAL-COM_EthernetWAN.LastKnownOperationalMode and check if the value sync's based on WAN Enabled status.
6.Unload the Module</automation_approch>
    <expected_output>if WAN Enabled status is enabled then Current and Last known operational Mode should be ETHERNET else DOCSIS.</expected_output>
    <priority>High</priority>
    <test_stub_interface>ETHWAN</test_stub_interface>
    <test_script>TS_ETHWAN_GetCurAndLastOperMode</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHWAN_GetCurAndLastOperMode');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    WanEnabled = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the status of WAN Enabled";
       print "EXPECTED RESULT 1: Should get the WAN Enabled";
       print "ACTUAL RESULT 1: Wan enabled status is :",WanEnabled;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       if WanEnabled == "true":
            Mode = "ETHERNET";
       else:
            Mode = "DOCSIS";

       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
       tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_EthernetWAN.CurrentOperationalMode");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details  = tdkTestObj.getResultDetails();

       if expectedresult in actualresult and details == Mode:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the Current Operational Mode";
          print "EXPECTED RESULT 2: Should get Current operationl mode as ",details,"if Wan status is ",WanEnabled;
          print "ACTUAL RESULT 2: Cuurent Operational mode is :",details;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
          tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_EthernetWAN.LastKnownOperationalMode");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details  = tdkTestObj.getResultDetails();

          if expectedresult in actualresult and details == Mode:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the Last Known Operational Mode";
             print "EXPECTED RESULT 3: Should get the  Last Known operationl mode as ",details,"if Wan status is ",WanEnabled;
             print "ACTUAL RESULT 3: Last Known Operational mode is :",details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Get the Last Known Operational Mode";
              print "EXPECTED RESULT 3: Should get the  Last Known operationl mode as ",details,"if Wan status is ",WanEnabled;
              print "ACTUAL RESULT 3: Last Known Operational mode is :",details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the Current Operational Mode";
           print "EXPECTED RESULT 2: Should get Current operationl mode as ",details,"if Wan status is ",WanEnabled;
           print "ACTUAL RESULT 2:Cuurent Operational mode is:",details;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the status of WAN Enabled";
        print "EXPECTED RESULT 1: Should get the WAN Enabled";
        print "ACTUAL RESULT 1: Wan enabled status is :",WanEnabled;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
