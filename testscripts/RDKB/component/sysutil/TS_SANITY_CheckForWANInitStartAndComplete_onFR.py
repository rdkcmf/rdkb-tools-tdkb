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
  <version>2</version>
  <name>TS_SANITY_CheckForWANInitStartAndComplete_onFR</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To  check if Wan init and complete log messages are populated on FR when DUT boots and comes up</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_SYSUTIL_47</test_case_id>
    <test_objective>To  check if Wan init and complete log messages are populated on FR when DUT boots and comes up.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module
2.Perform FR on DUT .
3.Once the DUT Boots Up check for "Wan_init_start" and "Wan_init_complete" in /rdklogs/logs/
4.The script is marked as SUCCESS if log messages are present else marked as FAILURE
5.Unload the module</automation_approch>
    <expected_output>The log message "Wan_init_start" and "Wan_init_complete" are expected to be present.</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckForWANInitStartAndComplete_onFR</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
obj1 = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckForWANInitStartAndComplete_onFR');
obj1.configureTestCase(ip,port,'TS_SANITY_CheckForWANInitStartAndComplete_onFR');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('WIFIAgent_Set');
    obj1.saveCurrentState();
    #Initiate Factory reset before checking the default value
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
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();
        sleep(200);
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        cmd = "grep -rin \"Wan_init_start\" /rdklogs/logs/";
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult and details !="":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 : Check if log message Wan init start is logged";
            print "EXPECTED RESULT 2: Wan init start log message should be logged";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "grep -rin \"Wan_init_complete\" /rdklogs/logs/";
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and details !="":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 : Check if log message Wan init complete is logged";
                print "EXPECTED RESULT 3: Wan init complete log message should be logged";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 : Check if log message Wan init complete is logged";
                print "EXPECTED RESULT 3: Wan init complete log message should be logged";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if log message Wan init start is logged";
            print "EXPECTED RESULT 2: Wan init start log message should be logged";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] :FAILURE";
    obj.unloadModule("sysutil");
    obj1.unloadModule("wifiagent");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
     obj1.setLoadModuleStatus("FAILURE");
