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
  <name>TS_ETHAGENT_CheckAssociatedDeviceNumberOfEntries</name>
  <primitive_test_id/>
  <primitive_test_name>ETHAgent_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if lan client connected interface AssociatedDeviceNumberOfEntries
should return the number of  client connected to that ethernet port</synopsis>
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
    <test_case_id>TC_ETHAGENT_05</test_case_id>
    <test_objective>To check if lan client connected interface AssociatedDeviceNumberOfEntries
should return the number of  client connected to that ethernet port</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.LAN Client should be connected</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries</input_parameters>
    <automation_approch>1. Load module
2. Get the MAC Address of client via arp -a
3. Check which interface Associated device MAC Address equals to MAC address retrived via arp -a
4. Check that interface's AssociatedDeviceNumberOfEntries return the number of  client connected to that ethernet port
5. Unload module</automation_approch>
    <except_output>lan client connected interface AssociatedDeviceNumberOfEntries
should return the number of  client connected to that ethernet port</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_ETHAGENT_CheckAssociatedDeviceNumberOfEntries</test_script>
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


#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_CheckAssociatedDeviceNumberOfEntries');
obj1.configureTestCase(ip,port,'TS_ETHAGENT_CheckAssociatedDeviceNumberOfEntries');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    command= "arp -a | grep brlan0 |cut -d \' \' -f 4";
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    macAddress = tdkTestObj.getResultDetails().strip().replace("\\n","").upper();
    if expectedresult in actualresult and macAddress != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the MAC Address of client via arp -a"
        print "EXPECTED RESULT 1: Should get the MAC Address of client";
        print "ACTUAL RESULT 1:MAC Address of client:  %s" %macAddress;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        retryCount=0;
        MAX_RETRY=4;
        for i in range (1,5):
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDevice.%s.MACAddress"%(i,i));

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            associatedMACAddress = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and associatedMACAddress == macAddress:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the lan client connected interface";
                print "EXPECTED RESULT 2: Should get the lan client connected interface"
                print "ACTUAL RESULT 2:LAN client connected interface:%s" %i
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                interface = i;

                tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries"%interface);

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult1 = tdkTestObj.getResult();
                associatedNumberOfEntries = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                tdkTestObj = obj.createTestStep('ExecuteCmd');
                command= "arp -a | grep brlan0 |wc -l";
                expectedresult="SUCCESS";
                tdkTestObj.addParameter("command", command);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult2 = tdkTestObj.getResult();
                connectedDevice = tdkTestObj.getResultDetails().strip().replace("\\n","");
                if expectedresult in (actualresult1 and actualresult2) and associatedNumberOfEntries == connectedDevice:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Check if AssociatedDeviceNumberOfEntries and number of clients connected to ethernet port are same";
                    print "EXPECTED RESULT 3:AssociatedDeviceNumberOfEntries and number of clients connected to ethernet port should be same"
                    print "ACTUAL RESULT 3:AssociatedDeviceNumberOfEntries and number of clients connected to ethernet port are same"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    break;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Check if AssociatedDeviceNumberOfEntries and number of clients connected to ethernet port are same";
                    print "EXPECTED RESULT 3:AssociatedDeviceNumberOfEntries and number of clients connected to ethernet port should be same"
                    print "ACTUAL RESULT 3:AssociatedDeviceNumberOfEntries and number of clients connected to ethernet port are not same"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    break;
            else:
                retryCount = retryCount + 1;
        if retryCount == MAX_RETRY:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the lan client connected interface"
            print "EXPECTED RESULT 2: Should get the lan client connected interface"
            print "ACTUAL RESULT 2:Failed to get lan client connected interface";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the MAC Address of client via arp -a "
        print "EXPECTED RESULT 1: Should get the MAC Address of client";
        print "ACTUAL RESULT 1:No LAN client is connected";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

