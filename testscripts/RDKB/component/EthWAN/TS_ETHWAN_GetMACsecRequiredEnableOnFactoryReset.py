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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ETHWAN_GetMACsecRequiredEnableOnFactoryReset</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>EthWAN_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if  Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable goes to a default value on factory reset</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_ETHWAN_17</test_case_id>
    <test_objective>This test case will check if the MAc sec is enabled on Factory reset which is the default value  in ethwan device</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.The device should be in ETHWAN mode</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues</api_or_interface_used>
    <input_parameters>Name of the Parameter
Type of the value to be get/set
parameter value to be set/get</input_parameters>
    <automation_approch>1.Function which needs to be tested will be configured in Test Manager GUI.
2.Python Script will be generated by Test Manager with provided arguments in configure page.
3.TM will load the PAM  and TAD library via Test agent
4.Check if  Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled is true
and  Device.DeviceInfo.X_RDKCENTRAL-COM_EthernetWAN.CurrentOperationalMode is Ethernet
5.Get the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable required state and store it in a variable.
6.Now disable the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable required status
7.Initiate a  Factory reset operation
8.Now get the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable status and the value should go to default on Factory reset
9.Revert the value to initial.
10.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.
11.unload the loaded modules</automation_approch>
    <expected_output>The value should be a default value that is enabled by default on Factory reset</expected_output>
    <priority>High</priority>
    <test_stub_interface>ETHWAN</test_stub_interface>
    <test_script>TS_ETHWAN_GetMACsecRequiredEnableOnFactoryReset</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkutility;
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","1");
obj1 = tdklib.TDKScriptingLibrary("tad","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHWAN_GetMACsecRequiredEnableOnFactoryReset');
obj1.configureTestCase(ip,port,'TS_ETHWAN_GetMACsecRequiredEnableOnFactoryReset');
#Get the result of connection with test component and DUT
loadmodulestatus  = obj.getLoadModuleResult();
loadmodulestatus1  = obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('TADstub_Get');
    paramList=["Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled","Device.DeviceInfo.X_RDKCENTRAL-COM_EthernetWAN.CurrentOperationalMode"]
    tdkTestObj,status,Value = getMultipleParameterValues(obj1,paramList)

    if expectedresult in status  and Value[1] == "Ethernet" and Value[0] == "true":
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the WAN Enabled Mode and Operational Mode";
       print "EXPECTED RESULT 1: Should get the WAN Enabled Mode as true and Operational Mode as Ethernet";
       print "ACTUAL RESULT 1: WAN Enabled  Mode is  %s and  Operational Mode is %s" %(Value[0],Value[1]);
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       print "*******************************************"
       print "The Device is in EthWan Mode"
       print "*******************************************"

       tdkTestObj = obj.createTestStep('pam_GetParameterValues');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable");
       expectedresult="SUCCESS";

       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       InitMACsecStatus = tdkTestObj.getResultDetails();

       if expectedresult in actualresult:
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the Initial Mac Sec status";
          print "EXPECTED RESULT 2: Should get the Initial Mac Sec status";
          print "ACTUAL RESULT 2: Got the Initial Mac Sec status",InitMACsecStatus;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          if  InitMACsecStatus == "true" :
              print "TEST STEP 3: Get Mac Sec status";
              print "EXPECTED RESULT 3: Should get the Mac Sec status as true";
              print "ACTUAL RESULT 3: Got the Mac Sec status as ",InitMACsecStatus;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";
              tdkTestObj.setResultStatus("SUCCESS");

              tdkTestObj = obj.createTestStep('pam_SetParameterValues');
              tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable");
              tdkTestObj.addParameter("ParamValue","false");
              tdkTestObj.addParameter("Type","bool");
              expectedresult="SUCCESS";

              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details = tdkTestObj.getResultDetails();

              if expectedresult in actualresult:
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 4: Toggle the Mac Sec status";
                 print "EXPECTED RESULT 4: Should Toggle the Mac Sec status";
                 print "ACTUAL RESULT 4: The Mac Sec status is : ",details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";

                 tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                 tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable");
                 expectedresult="SUCCESS";

                 #Execute the test case in DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 GetMACsecStatus = tdkTestObj.getResultDetails();

                 if expectedresult in actualresult and GetMACsecStatus == "false":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Get the Mac Sec status";
                    print "EXPECTED RESULT 5: Get and  set Mac Sec status should be equal";
                    print "ACTUAL RESULT 5: Got the Mac Sec status",GetMACsecStatus;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

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
                       print "TEST STEP 6: Initiate factory reset ";
                       print "ACTUAL RESULT 6: %s" %details;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : SUCCESS";
                       #Restore the device state saved before reboot
                       obj.restorePreviousStateAfterReboot();

                       tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable");
                       expectedresult="SUCCESS";

                       #Execute the test case in DUT
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       MACsecStatus = tdkTestObj.getResultDetails();

                       if expectedresult in actualresult and MACsecStatus == "true":
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 7: Get the Mac Sec status";
                          print "EXPECTED RESULT 7:  Mac Sec status should go to default state after Factory reset";
                          print "ACTUAL RESULT 7: Mac Sec status is ",MACsecStatus;
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";
                       else:
                           tdkTestObj.setResultStatus("FAILURE");
                           print "TEST STEP 7: Get the Mac Sec status";
                           print "EXPECTED RESULT 7: Mac Sec status should go to default state after Factory reset";
                           print "ACTUAL RESULT 7: Mac Sec status is ",MACsecStatus;
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : FAILURE";

                           #Revert the value
                           tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                           tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.MACsecRequired.Enable");
                           tdkTestObj.addParameter("ParamValue",InitMACsecStatus);
                           tdkTestObj.addParameter("Type","bool");
                           expectedresult="SUCCESS";

                           #Execute the test case in DUT
                           tdkTestObj.executeTestCase(expectedresult);
                           actualresult = tdkTestObj.getResult();
                           details = tdkTestObj.getResultDetails();

                           if expectedresult in actualresult:
                              tdkTestObj.setResultStatus("SUCCESS");
                              print "TEST STEP 8: Revert the Mac Sec status";
                              print "EXPECTED RESULT 8: Should revert the Mac Sec status";
                              print "ACTUAL RESULT 8: The Mac Sec status reverted to ",InitMACsecStatus;
                              #Get the result of execution
                              print "[TEST EXECUTION RESULT] : SUCCESS";
                           else:
                               tdkTestObj.setResultStatus("FAILURE");
                               print "TEST STEP 8: Revert the Mac Sec status";
                               print "EXPECTED RESULT 8: Should revert the Mac Sec status";
                               print "ACTUAL RESULT 8: The Mac Sec status reverted to ",InitMACsecStatus;
                               #Get the result of execution
                               print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: Initiate factory reset ";
                        print "ACTUAL RESULT 6: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                 else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 5: Get the Mac Sec status";
                     print "EXPECTED RESULT 5: Get and set Mac Sec status should be equal";
                     print "ACTUAL RESULT 5: Got the Mac Sec status",GetMACsecStatus;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4: Toggle the Mac Sec status";
                  print "EXPECTED RESULT 4: Should Toggle the Mac Sec status";
                  print "ACTUAL RESULT 4: The Mac Sec status is : ",details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";

          else:
               print "TEST STEP 3: Get Mac Sec status";
               print "EXPECTED RESULT 3: Should get the Mac Sec status as true";
               print "ACTUAL RESULT 3: Got the Mac Sec status as ",InitMACsecStatus;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
               tdkTestObj.setResultStatus("FAILURE");
       else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Initial Mac Sec status";
            print "EXPECTED RESULT 2: Should get the Initial Mac Sec status";
            print "ACTUAL RESULT 2: Got the Initial Mac Sec status",InitMACsecStatus;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the WAN Enabled Mode and Operational Mode";
        print "EXPECTED RESULT 1: Should get the WAN Enabled Mode as true and Operational Mode as Ethernet";
        print "ACTUAL RESULT 1: WAN Enabled  Mode is  %s and  Operational Mode is %s" %(Value[0],Value[1]);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

        print "*************************************************************"
        print "The Device is not in EthWan mode Please check the Device Setup"
        print "**************************************************************"

    obj.unloadModule("pam");
    obj1.unloadModule("tad");
else:
    print "Failed to load pam  module";
    obj.setLoadModuleStatus("FAILURE");