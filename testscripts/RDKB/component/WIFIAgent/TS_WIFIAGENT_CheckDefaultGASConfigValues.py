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
  <name>TS_WIFIAGENT_CheckDefaultGASConfigValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if Generic Advertising Service Configurations have default value after factory reset</synopsis>
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
    <test_case_id>TC_WIFIAGENT_123</test_case_id>
    <test_objective>This test case is to check if Generic Advertising Service Configurations have default value after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_GASConfiguration</input_parameters>
    <automation_approch>1.Load the module
2. Initiate a Factory reset on the device.
3.Query the Device.WiFi.X_RDKCENTRAL-COM_GASConfiguration
4.Check if the GAS Configuration have their default values on FR
Advertisement Identifier -  default = 0.
Pause for Server response -  default = true
Response Timeout - default = 5000
Comeback Delay - default = 1000.
Response Buffering Time -  default = 1000.
Query Response Length Limit - default = 127.
5.Unload the module
</automation_approch>
    <expected_output>GAS configurations should have the expected default value once the device comes up after a Factory Reset</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckDefaultGASConfigValues</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckDefaultGASConfigValues');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
flag =1;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    #save device's current state before it goes for reboot
    obj.saveCurrentState();
    expectedresult ="SUCCESS";
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
       print "TEST STEP 1: Initiate factory reset ";
       print "EXPECTED RESULT 1: Should inititate factory reset";
       print "ACTUAL RESULT 1: %s" %details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       #Restore the device state saved before reboot
       obj.restorePreviousStateAfterReboot();

       tdkTestObj = obj.createTestStep('WIFIAgent_Get');
       tdkTestObj.addParameter("paramName","Device.WiFi.X_RDKCENTRAL-COM_GASConfiguration");
       expectedresult="SUCCESS";

       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();

       if expectedresult in actualresult and details:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the GAS Configuration";
          print "EXPECTED RESULT 2: Should get GAS Configuration";
          print "ACTUAL RESULT 2: GAS Configuration retreived successful";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          advertId = int(details.split("advertId")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
          print "advertId:",advertId;
          pauseForServerResp = details.split("pauseForServerResp")[1].split(":")[1].split(",")[0].strip().replace("\\n", "");
          print "pauseForServerResp:",pauseForServerResp;
          respTimeout = int(details.split("respTimeout")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
          print "respTimeout:",respTimeout
          comebackDelay = int(details.split("comebackDelay")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
          print "comebackDelay:" ,comebackDelay
          respBufferTime = int(details.split("respBufferTime")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
          print "respBufferTime:",respBufferTime;
          queryRespLengthLimit=int(details.split("queryRespLengthLimit")[1].split(":")[1].split("}")[0].strip().replace("\\n", ""));
          print "queryRespLengthLimit:",queryRespLengthLimit;

          print "*** Checking if the GAS Configurations have default Value***";
          if advertId == 0:
             print "advertId has a default value as 0";
          else:
              flag = 0;
              print "advertId doesnot have a default value";

          if pauseForServerResp == "true":
             print "pauseForServerResp should have a default value as true";
          else:
              flag = 0;
              print "pauseForServerResp doesnot hold a default value";

          if respTimeout == 5000:
             print "respTimeout has a default value as 5000";
          else:
              flag = 0;
              print "respTimeout doesnot have a default value";

          if comebackDelay ==1000:
             print "comebackDelay has a default value as 1000";
          else:
              flag = 0;
              print "comebackDelay doesnot have a default value";

          if respBufferTime == 1000 :
             print"respBufferTime has a default value as 1000";
          else:
              flag = 0;
              print "respBufferTime doesnot have a default value";

          if queryRespLengthLimit == 127:
             print "queryRespLengthLimit has a default value as 127";
          else:
              flag = 0;
              print "queryRespLengthLimit doesnot have a default value";

          if flag == 1:
             tdkTestObj.setResultStatus("SUCCESS");
             print "****The GAS configs have the default value on factory reset****";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "*****The GAS configs donot have the default value on factory reset****";
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the GAS Configuration";
           print "EXPECTED RESULT 2: Should get GAS Configuration";
           print "ACTUAL RESULT 2: Failed to retrieve GAS Configuration";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
