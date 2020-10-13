##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_ETHAGENT_CheckBitRateAndDuplexMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ETHAgent_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if lan client connected interface maxbit rate,current bit rate  is not 0 and duplex mode is  full</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <test_case_id>TC_ETHAGENT_03</test_case_id>
    <test_objective>To check if lan client connected interface maxbit rate,current bit rate  is not 0 and duplex mode is full</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.LAN Client should be connected</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.Interface.{i}.MaxBitRate,Device.Ethernet.Interface.{i}.CurrentBitRate , Device.Ethernet.Interface.{i}.DuplexMode</input_parameters>
    <automation_approch>1. Load module
2. Get the MAC Address of client via Device.Hosts.Host.
3. Check which interface Associated device MAC Address equals to MAC address retrived via Device.Hosts.Host.{i}.PhysAddress
4. Check that interface's max bit rate and current bit rate is not zero
5. Check that interface's duplex mode is full
6. Unload module</automation_approch>
    <except_output>LAN connected interface's  maxbit rate,current bit rate  is not 0 and duplex mode is full</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_ETHAGENT_CheckBitRateAndDuplexMode</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_CheckBitRateAndDuplexMode');
obj1.configureTestCase(ip,port,'TS_ETHAGENT_CheckBitRateAndDuplexMode');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Hosts.HostNumberOfEntries");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoofHost=tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and int(NoofHost) >0:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the no of LAN clients connected";
       print "EXPECTED RESULT 1: Should get the no of LAN clients connected"
       print "ACTUAL RESULT 1:%s" %NoofHost
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       Ethclientfound = 0;

       for i in range (1,int(NoofHost)+1):
           expectedresult="SUCCESS";
           tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
           tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Layer1Interface"%(i));
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
           print "Device.Hosts.Host.%s.Layer1Interface value is %s" %(i,details);
           if expectedresult in actualresult and details == "Ethernet":
              tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
              tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Active"%(i));
              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
              print "Device.Hosts.Host.%s.Active value is %s" %(i,details);
              if  expectedresult in actualresult and details == "true":
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 2: Check if the connected LAN client is active";
                  print "EXPECTED RESULT 2: Should get the connected LAN client  active";
                  print "ACTUAL RESULT 2:%s" %details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";

                  Ethclientfound = 1;
                  tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                  tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.PhysAddress"%(i));

                  #Execute the test case in DUT
                  tdkTestObj.executeTestCase(expectedresult);
                  actualresult = tdkTestObj.getResult();
                  macAddress = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                  if expectedresult in actualresult :
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 3: Get the lan client mac";
                     print "EXPECTED RESULT 3: Should get the lan client mac"
                     print "ACTUAL RESULT 3:LAN client connected mac is:%s" %macAddress
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                     mac = macAddress.upper();
                     break;

       if  Ethclientfound == 1:
           retryCount=0;
           MAX_RETRY=4;
           for i in range (1,5):
               tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
               tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.%s.MACAddress"%(i,i));
               #Execute the test case in DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               associatedMACAddress = tdkTestObj.getResultDetails().strip().replace("\\n", "");
               if expectedresult in actualresult and associatedMACAddress == mac:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 3: Get the MAC address of the Ethernet interface";
                  print "EXPECTED RESULT 3: Should get the MAC address of the Ethernet interface"
                  print "ACTUAL RESULT 3:Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.%s.MACAddress is %s" %(i,i,associatedMACAddress);
                  print "LAN client interafce connected at :%s" %i
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";
                  interface = i;
                  break;
               else:
                   retryCount = retryCount + 1;

           tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
           tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.MaxBitRate"%interface);
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           maxBitRate = tdkTestObj.getResultDetails().strip().replace("\\n", "");
           if expectedresult in actualresult and maxBitRate != "" and  maxBitRate != "0":
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 5: Check if Interface Max Bit Rate is not 0";
              print "EXPECTED RESULT 5:Interface Max Bit Rate should not be 0"
              print "ACTUAL RESULT 5:Interface Max Bit Rate is %s"%maxBitRate
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";
              tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
              tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.CurrentBitRate"%interface);
              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              currentBitRate = tdkTestObj.getResultDetails().strip().replace("\\n", "");
              if expectedresult in actualresult and currentBitRate != "" and  currentBitRate != "0":
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 6: Check if Interface current Bit Rate is not 0";
                 print "EXPECTED RESULT 6:Interface current Bit Rate should not be 0"
                 print "ACTUAL RESULT 6:Interface current Bit Rate is %s"%currentBitRate
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
                 tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                 tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.DuplexMode"%interface);
                 #Execute the test case in DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 duplexMode = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                 if expectedresult in actualresult and duplexMode != "" and  duplexMode == "Full":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 7: Check if Interface duplexMode is  full";
                    print "EXPECTED RESULT 7:Interface duplexMode should be full"
                    print "ACTUAL RESULT 7:Interface duplexMode is %s" %duplexMode
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                 else:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 7: Check if Interface duplexMode is full";
                     print "EXPECTED RESULT 7:Interface duplexMode should be full"
                     print "ACTUAL RESULT 7:Interface duplexMode is %s" %duplexMode
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 6: Check if Interface current Bit Rate is not 0";
                  print "EXPECTED RESULT 6:Interface current Bit Rate should not be 0"
                  print "ACTUAL RESULT 6:Interface current Bit Rate is  %s"%currentBitRate
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 5: Check if Interface Max Bit Rate is not 0";
               print "EXPECTED RESULT 5:Interface Max Bit Rate should not be 0"
               print "ACTUAL RESULT 5:Interface Max Bit Rate is  %s"%maxBitRate
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";

       if retryCount == MAX_RETRY:
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 3: Get the active LAN client MAC"
          print "EXPECTED RESULT 3: Should get the active LAN client MAC"
          print "ACTUAL RESULT 3:Failed to get active LAN client MAC";
          print "[TEST EXECUTION RESULT] : FAILURE";

       if Ethclientfound == 0:
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 2: Get the active lan client connected interface"
          print "EXPECTED RESULT 2: Should get the active lan client connected interface"
          print "ACTUAL RESULT 2:No Ethernet client connected to DUT";
          print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the no of LAN clients connected";
        print "EXPECTED RESULT 1: Should get the no of LAN clients connected"
        print "ACTUAL RESULT 1:No of LAN clients associated with DUT %s" %NoofHost
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
