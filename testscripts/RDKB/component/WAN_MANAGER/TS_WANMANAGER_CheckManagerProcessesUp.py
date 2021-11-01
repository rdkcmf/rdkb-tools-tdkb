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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_CheckManagerProcessesUp</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if manager processes are running in WAN_MANAGER Enabled build.</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WANMANGER_113</test_case_id>
    <test_objective>This test case is to check if manager processes are running in WAN_MANAGER Enabled build</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN Manager should be enabled</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module
2.Get the list of  manager process
3.Loop through the list and check if the processes are up and running
4.Unload the module
</automation_approch>
    <expected_output>All the manager process are expected to be active and running</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckManagerProcessesUp</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import time;
from time import sleep;
from xfinityWiFiLib import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_CheckManagerProcessesUp');
#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    CcspProcess= "sh %s/tdk_utility.sh parseConfigFile WAN_PROCESSES" %TDK_PATH;
    print CcspProcess;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", CcspProcess);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    WanProcessList = tdkTestObj.getResultDetails().strip();
    WanProcessList = WanProcessList.replace("\\n", "");
    if "Invalid Argument passed" not in WanProcessList:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of WAN_MANAGER rocesses ";
        print "EXPECTED RESULT 1: Should get the list of WAN_MANAGER processes";
        print "ACTUAL RESULT 1: %s" %WanProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        WanProcessList = WanProcessList.split(",");

        for item in WanProcessList:
            command1 = "pidof %s" %item
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", command1);
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
        print "TEST STEP 1: Get the list of ccsp processes ";
        print "EXPECTED RESULT 1: Should get the list of ccsp processes";
        print "ACTUAL RESULT 1: %s" %WanProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");
else:
     print "Failed to load sysutil module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
