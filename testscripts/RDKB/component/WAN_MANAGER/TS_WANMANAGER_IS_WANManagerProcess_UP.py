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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_IS_WANManagerProcess_UP</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>This test case is to check if  WANMANAGER is up and running</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WANMANAGER_07</test_case_id>
    <test_objective>This test case is to check if  WANMANAGER is up and running</test_objective>
    <test_type>Positive</test_type>
    <test_setup> Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>pidof wanmanager</input_parameters>
    <automation_approch>1] Load the module
2]Get the wanmanger pid using "pidof wanmanager"
3]check if wanmanager is up and  process running
4]Unload the module</automation_approch>
    <expected_output> wanmanager is up and  process running</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_IS_WANManagerProcess_UP</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_IS_WANManagerProcess_UP');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    wanmanagerProcess= "sh %s/tdk_utility.sh parseConfigFile WANMANAGER_PROCESS" %TDK_PATH;
    print wanmanagerProcess;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", wanmanagerProcess);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    wanmanagerProcessList = tdkTestObj.getResultDetails().strip();
    wanmanagerProcessList = wanmanagerProcessList.replace("\\n", "");
    if "Invalid Argument passed" not in wanmanagerProcessList:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of wanmanager process";
        print "EXPECTED RESULT 1: Should Get the list of wanmanager process";
        print "ACTUAL RESULT 1: wanmanager process: %s" %wanmanagerProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        wanmanagerProcessList = wanmanagerProcessList.split(",");
        for item in wanmanagerProcessList:
            command = "pidof %s" %item
            tdkTestObj.addParameter("command", command);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();
            details = details.replace("\\n", "");
            if expectedresult in actualresult and "" != details:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Process Name : %s" %item;
                print "PID : %s" %details;
                print "%s with process ID %s is running" %(item,details)
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Process Name : %s" %item
                print "%s is not running" %item
                print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the list of wanmanager process";
        print "EXPECTED RESULT 1: Should Get the list of wanmanager Process";
        print "ACTUAL RESULT 1: wanmanager process: %s" %wanmanagerProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");
else:
        print "Failed to load sysutil module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed"
