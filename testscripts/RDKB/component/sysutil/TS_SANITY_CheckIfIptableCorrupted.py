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
  <name>TS_SANITY_CheckIfIptableCorrupted</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if  any iptables corrupted log messages are present ,if so check if firewall restart took place</synopsis>
  <groups_id/>
  <execution_time>25</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>  
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_49</test_case_id>
    <test_objective>To check if  any iptables corrupted log messages are present ,if so check if firewall restart took place</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module
2.Check if any log message iptable corrupted is present  and should not be present ,if present check if firewall restart took place
3. Based on the above result script is marked as SUCCESS else FAILURE
4.Unload the module</automation_approch>
    <expected_output>iptable corrupted log message is not expected to be present if present firewall restart has to take place </expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckIfIptableCorrupted</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
import time;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckIfIptableCorrupted');
count = 0;
#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", "grep -rin \"iptable corrupted\" /rdklogs/logs/");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and details!= "":
        #Set the result status of execution
        print "TEST STEP 1: Check if log files have log message for iptables corrupted"
        print "EXPECTED RESULT 1: Log files should not have log message for iptables corrupted";
	print "ACTUAL RESULT 1: log message found :",details;

   	tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", "grep -rin \"restarting firewall\" /rdklogs/logs/");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult and details!= "":
	    tdkTestObj.setResultStatus("SUCCESS");
            #Set the result status of execution
            print "TEST STEP 2: Check if firewall restarted as iptable was corrupted"
            print "EXPECTED RESULT 2: firewall should restart as iptable was corrupted";
	    print "ACTUAL RESULT 2: Search result is :",details;
	    print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if firewall restarted as iptable was corrupted"
            print "EXPECTED RESULT 2: firewall should restart as iptable was corrupted";
            print "ACTUAL RESULT 2: search result is :",details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
	tdkTestObj.setResultStatus("SUCCESS");
        #Set the result status of execution
        print "TEST STEP 1: Check if log files have log message for iptables corrupted"
        print "EXPECTED RESULT 1: Log files should not have log message for iptables corrupted";
	print "ACTUAL RESULT 1: log message not found:",details;
	print "[TEST EXECUTION RESULT] : SUCCESS";
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
