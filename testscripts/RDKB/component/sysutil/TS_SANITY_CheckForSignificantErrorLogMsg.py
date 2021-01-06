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
  <name>TS_SANITY_CheckForSignificantErrorLogMsg</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if any significant Log Messages are seen in /rdklogs/logs</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_36</test_case_id>
    <test_objective>This test case is to check if any significant Log Messages are seen in /rdklogs/logs</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband ,RPI,EMU</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module
2. Reboot the DUT
3.wait for device to come up  after reboot
4.Search for "command not found" , "No such file or directory"," syscfg_get failed" ,"404 Not Found" ,"syntax error","System Not Ready","Unknown Msg" ,"Invalid argument" ,"unary operator expected","nonexistent directory" ,"not found"  in /rdklogs/logs
5.Display the Log message if the above mentioned Log messages are present and mark the script as failure
6.Unload the module
</automation_approch>
    <expected_output>When searched for these log messages the messages should not be present in /rdklogs/logs/ file</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckForSignificantErrorLogMsg</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckForSignificantErrorLogMsg');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    obj.initiateReboot();
    sleep(300);

    logFile = "/rdklogs/logs/";
    logMsg = ["command not found" ,"No such file or directory","syscfg_get failed" ,"404 Not Found" ,"syntax error","System Not Ready","Unknown Msg" ,"Invalid argument" ,"unary operator expected","nonexistent directory" ,"not found","Failed to get parameter value","received message error","Event length more than expected","violation","integer expression expected","No Matching Profiles"];

    print "***************************************************";
    print "TEST STEP 1: Checking if the following Log Messages are present in /rdklogs/logs/";
    print "%s" %logMsg;
    markerfound =0;
    result = [];
    for item in logMsg:
        print "\n*** Checking if %s  message is present in Log Files***" %item;
        query="grep -rin \"%s\" \"%s\"" %(item,logFile);
        print "query:%s" %query
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", query)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n","");
        print "Search Result :%s "%details;
        if (len(details) != 0)  and  item in details:
           result.append(details);
           markerfound =1;

    if markerfound == 0:
       tdkTestObj.setResultStatus("SUCCESS");
       print "ACTUAL RESULT : The Above listed Log Messgaes were not present in /rdklogs/logs/";
       print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT : The following Log Messages were present :%s" %result;
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "***************************************************";
    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
