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
2. Get the MAC Address of client via arp -a
3. Check which interface Associated device MAC Address equals to MAC address retrived via arp -a
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
                tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%s.MaxBitRate"%interface);

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                maxBitRate = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and maxBitRate != "" and  maxBitRate != "0":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Check if Interface Max Bit Rate is not 0";
                    print "EXPECTED RESULT 3:Interface Max Bit Rate should not be 0"
                    print "ACTUAL RESULT 3:Interface Max Bit Rate is not 0"
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
                        print "TEST STEP 4: Check if Interface current Bit Rate is not 0";
                        print "EXPECTED RESULT 4:Interface current Bit Rate should not be 0"
                        print "ACTUAL RESULT 4:Interface current Bit Rate is not 0"
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
                            print "TEST STEP 5: Check if Interface duplexMode is  full";
                            print "EXPECTED RESULT 5:Interface duplexMode should be full"
                            print "ACTUAL RESULT 5:Interface duplexMode is full"
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            break;
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Check if Interface duplexMode is full";
                            print "EXPECTED RESULT 5:Interface duplexMode should be full"
                            print "ACTUAL RESULT 5:Interface duplexMode is not full"
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                            break;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Check if Interface current Bit Rate is not 0";
                        print "EXPECTED RESULT 4:Interface current Bit Rate should not be 0"
                        print "ACTUAL RESULT 4:Interface current Bit Rate is  0"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Check if Interface Max Bit Rate is not 0";
                    print "EXPECTED RESULT 3:Interface Max Bit Rate should not be 0"
                    print "ACTUAL RESULT 3:Interface Max Bit Rate is  0"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
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

