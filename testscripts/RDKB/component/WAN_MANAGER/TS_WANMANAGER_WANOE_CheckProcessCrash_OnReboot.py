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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_WANOE_CheckProcessCrash_OnReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check if any process crahsed when WAN Manager is enabled on reboot</synopsis>
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
    <test_case_id>TC_WANMANAGER_20</test_case_id>
    <test_objective>This test case is to check if any process crahsed when WAN Manager is enabled on reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Check if WANOE interface is present and enabled
3.reboot the DUT
4.Once the device comes up after reboot check no process crashed
5.Unload the module</automation_approch>
    <expected_output>In a wan manager enabled image no process is expected to crash on boot up</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_WANOE_CheckProcessCrash_OnReboot</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
import time;
from WanManager_Utility import *;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
tadobj = tdklib.TDKScriptingLibrary("tad","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_WANMANAGER_WANOE_CheckProcessCrash_OnReboot');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_WANOE_CheckProcessCrash_OnReboot');
tadobj.configureTestCase(ip,port,'TS_WANMANAGER_WANOE_CheckProcessCrash_OnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 = tadobj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper()and loadmodulestatus3.upper()):
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tadobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile DEVICETYPE" %TDK_PATH;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    devicetype = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and devicetype != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the DEVICE TYPE"
        print "EXPECTED RESULT 1: Should get the device type";
        print "ACTUAL RESULT 1:Device type  %s" %devicetype;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if devicetype == "RPI":
            i =1;
        else:
            i=2;
        tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%s.Wan.Enable" %i);
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details == "true":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 :Check if WANOE is enabled";
            print "EXPECTED RESULT 2: Should get the status of WANOE";
            print "ACTUAL RESULT 2: The value received is :",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", "grep -rin \"RDKB_PROCESS_CRASHED\" /rdklogs/logs/");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace(" ",",");
            if expectedresult in actualresult and "RDKB_PROCESS_CRASHED" not in details:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if any process crashed before reboot ";
                print "ACTUAL RESULT 3: Log files does not have any process crashed logs";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                sysObj.initiateReboot();
                time.sleep(300);

                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", "grep -rin \"RDKB_PROCESS_CRASHED\" /rdklogs/logs/");
                expectedresult="SUCCESS";

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace(" ",",");
                if expectedresult in actualresult and "RDKB_PROCESS_CRASHED" not in details:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Check if any process crashed after reboot"
                    print "ACTUAL RESULT 4: Log files does not have any process crashed logs";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Check if any process crashed after reboot";
                    print "ACTUAL RESULT 4: %s"%details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if any process crashed before reboot ";
                print "ACTUAL RESULT 3: Log files  have process crashed logs :%s "%details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 :Check if WANOE is enabled";
            print "EXPECTED RESULT 2: Should get the status of WANOE enabled";
            print "ACTUAL RESULT 2: The value received is :",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the DEVICE TYPE"
        print "EXPECTED RESULT 1: Should get the device type";
        print "ACTUAL RESULT 1:Device type  %s" %devicetype;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
    tadobj.unloadModule("tad");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
