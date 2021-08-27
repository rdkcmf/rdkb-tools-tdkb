##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_WIFIAGENT_SubscribeNonExistingSession</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Subscribe a Non Existing Session</synopsis>
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
    <test_case_id>TC_WIFIAGENT_136</test_case_id>
    <test_objective>This test case is to check if Subscribing a Non Existing Session is possible</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
ExecuteCmd</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDK_CSI.
wifi_events_consumer -e 7 -s 1</input_parameters>
    <automation_approch>1.Load the module
2.Check if there are no subscribers under Device.WiFi.X_RDK_CSI. as NO client is connected to device
3.Try to query a non existing session an error is expected to pop-up
4.Unload the module</automation_approch>
    <expected_output>with no subscribers querying an non-existing session should throw a error</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_SubscribeNonExistingSession</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
#import  tdklib library,which provides a wrapper for tdk testcase scripti
import tdklib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SubscribeNonExistingSession');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_SubscribeNonExistingSession');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysObj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDK_CSI.");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanmodeInitial = tdkTestObj.getResultDetails();

    if expectedresult not  in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Verify CSI Table is empty";
        print "EXPECTED RESULT 1: With no client and subsciberts table should be empty";
        print "ACTUAL RESULT 1: No entries found";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", "wifi_events_consumer -e 7 -s 1");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details!= "" and "consumer: exit"  in details:
            tdkTestObj.setResultStatus("SUCCESS");
            #Set the result status of execution
            print "TEST STEP 2: Subscribe CSI data for session 1"
            print "EXPECTED RESULT 2: CSI data should not be retreived for non-existing session";
            print "ACTUAL RESULT 2: ",details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Subscribe CSI data for session 1"
            print "EXPECTED RESULT 2: CSI data should not be retreived for non-existing session";
            print "ACTUAL RESULT 2: ",details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Verify CSI Table is empty";
        print "EXPECTED RESULT 1: With no client and subsciberts table should be empty";
        print "ACTUAL RESULT 1: Subscriber entries are found in the table disconnect the subscribers and execute script";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
