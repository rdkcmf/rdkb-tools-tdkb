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
  <name>TS_WANMANAGER_CheckLANStatusAndProvappProcess</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if lan status is started and check the provapp  process is running</synopsis>
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
    <test_case_id>TC_WANMANAGER_04</test_case_id>
    <test_objective>This test case is to check if lan status is started and check the provapp  process is running</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>sysevent get lan-status</input_parameters>
    <automation_approch>1] Load the module
2]Get the lan-status using "sysevent get lan-status"
3]Check if the lan status is started
4]if started check if provapp process running
5]Unload the module</automation_approch>
    <expected_output>provapp process is expected to be up and running if the lan-status is started</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckLANStatusAndProvappProcess</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_CheckLANStatusAndProvappProcess');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult ="SUCCESS";
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    command = "sysevent get lan-status"
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip();
    status = details.replace("\\n", "");
    if expectedresult in actualresult and details != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check the lan status";
        print "EXPECTED RESULT 1: Should Get the lan status";
        print "ACTUAL RESULT 1: lan status is ",status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        if status == "started":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Check if the lan status is started";
            print "EXPECTED RESULT 2: Should Get the lan status as started";
            print "ACTUAL RESULT 2: lan status is ",status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            command = "ps | grep -rn \"provapp\"| grep -v \"grep\"";
            tdkTestObj.addParameter("command", command);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();
            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if the provapp process is running";
                print "EXPECTED RESULT 3:provapp process should be running";
                print "ACTUAL RESULT 3: provapp process  details is: ",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if the provapp process is running";
                print "EXPECTED RESULT 3:provapp process should be running";
                print "ACTUAL RESULT 3: provapp process  details is: ",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if the lan status is started";
            print "EXPECTED RESULT 2: Should Get the lan status as started";
            print "ACTUAL RESULT 2: lan status is ",status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check the lan status";
        print "EXPECTED RESULT 1: Should Get the lan status";
        print "ACTUAL RESULT 1: lan status is ",status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
