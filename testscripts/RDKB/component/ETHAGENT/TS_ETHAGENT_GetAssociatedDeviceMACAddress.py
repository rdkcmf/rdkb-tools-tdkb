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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>3</version>
  <name>TS_ETHAGENT_GetAssociatedDeviceMACAddress</name>
  <primitive_test_id/>
  <primitive_test_name>ETHAgent_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if AssociatedDeviceMACAddress is returned for LAN client connected interface</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_ETHAGENT_06</test_case_id>
    <test_objective>To check if AssociatedDeviceMACAddress is returned for LAN client connected interface</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.LAN Client should be connected</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.{i}.MACAddress</input_parameters>
    <automation_approch>1. Load module
2. Get the MAC Address of client via Device.Hosts.Host.
3. Check which interface Associated device MAC Address equals to MAC address retrived via Device.Hosts.Host.{i}.PhysAddress
4. Check that interface's AssociatedDeviceMACAddress is returned for LAN client connected interface
5. Unload module</automation_approch>
    <except_output>AssociatedDeviceMACAddress value should be returned for LAN client connected interface</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_ETHAGENT_GetAssociatedDeviceMACAddress</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
retryCount =0;
MAX_RETRY=4;
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_GetAssociatedDeviceMACAddress');
obj1.configureTestCase(ip,port,'TS_ETHAGENT_GetAssociatedDeviceMACAddress');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

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
                  print "EXPECTED RESULT 2: Should get the connected LAN client as active";
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
           for i in range (1,5):
               tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
               tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress"%i);
               #Execute the test case in DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               associatedMACAddress = tdkTestObj.getResultDetails().strip().replace("\\n", "");
               if expectedresult in actualresult and associatedMACAddress == mac:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 3: Get the MAC address of the Ethernet interface";
                  print "EXPECTED RESULT 3: Should get the MAC address of the Ethernet interface"
                  print "ACTUAL RESULT 3:Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress is %s" %(i,associatedMACAddress);
                  print "LAN client interafce connected at :%s" %i
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";
                  interface = i;
                  print "AssociatedDeviceMACAddress is %s" %associatedMACAddress
                  break;
               else:
                    retryCount = retryCount + 1;
       if retryCount == MAX_RETRY:
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 2: Get the active LAN client MAC"
          print "EXPECTED RESULT 2: Should get the active LAN client MAC"
          print "ACTUAL RESULT 2:Failed to get active LAN client MAC";
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
        print "ACTUAL RESULT 1:No clients associated with DUT %s" %NoofHost
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
