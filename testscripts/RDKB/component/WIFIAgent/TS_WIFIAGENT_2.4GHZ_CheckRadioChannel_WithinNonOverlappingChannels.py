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
  <name>TS_WIFIAGENT_2.4GHZ_CheckRadioChannel_WithinNonOverlappingChannels</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if 2.4GHZ Wifi Radio channel value retrieved is within the Non-overlapping Channel list</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIAGENT_114</test_case_id>
    <test_objective>This test case is to check if 2.4GHZ Wifi Radio channel value retrieved is within the Non-overlapping Channel list</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.WiFi.Radio.1.Channel
</input_parameters>
    <automation_approch>1. Load  module
2.Get the current Channel for Wi-Fi 2.4GHz using  Device.WiFi.Radio.1.Channel
3.Check if the current Channel is one of the non-overlapping channel  1 or 6 or 11
4.Unload the module</automation_approch>
    <expected_output>The Channel should be one of the non-overlapping Channel</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHZ_CheckRadioChannel_WithinNonOverlappingChannels</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHZ_CheckRadioChannel_WithinNonOverlappingChannels');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #save the orginal value of AutoChannelEnable
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.WiFi.Radio.1.Channel")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current Channel"
        print "EXPECTED RESULT 1: Should get the current Channel"
        print "ACTUAL RESULT 1: Current Channel is %s " %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        nonOverlappingChannelsList = [1,6,11];
        checkStatus = 0;
        for channel in nonOverlappingChannelsList:
            if int (details) == channel :
               checkStatus =1;

        if checkStatus == 1:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Check if the Current Channel has one of %s non-overlapping Channel" %nonOverlappingChannelsList;
           print "EXPECTED RESULT 2: Should have one of the non-overlapping Channels";
           print "ACTUAL RESULT 2: The current Channel for 2.4GHz WiFi is a non-overlapping channel";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if the Current Channel has one of %s  non-overlapping Channel" %nonOverlappingChannelsList;
            print "EXPECTED RESULT 2: Should have one of the non-overlapping Channels";
            print "ACTUAL RESULT 2: The current Channel for 2.4GHz WiFi is not a non-overlapping channel";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current Channel"
        print "EXPECTED RESULT 1: Should get the current Channel"
        print "ACTUAL RESULT 1: Current Channel is %s " %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load tdkbtr181 module";
    obj.setLoadModuleStatus("FAILURE");
