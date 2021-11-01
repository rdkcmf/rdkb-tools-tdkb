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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_WANOE_PriorityChange_CheckInternetConnectivity</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To change the WAN priority of the WANOE Interface (interface 2) and check internet connectivity when DUT comes up after reboot.</synopsis>
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
    <test_case_id>TC_WANMANAGER_27</test_case_id>
    <test_objective>This test case is to change the WAN priority of the WANOE Interface (interface 2) and check internet connectivity when DUT comes up after reboot.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority</input_parameters>
    <automation_approch>1.Load the module
2.Get the current WAN priority for interface no 2
3.Change the wan priority to a number like 2 which will not be taken by other interfaces
4.reboot the device to apply priority settings
5.ping to a outside network and check no packet loss takes place
6.revert the priority to previous
7.Unload the module</automation_approch>
    <expected_output>With change in priority internet should be available with no packet loss </expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_WANOE_PriorityChange_CheckInternetConnectivity</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
import time;
from tdkbVariables import *;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_WANMANAGER_WANOE_PriorityChange_CheckInternetConnectivity');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_WANOE_PriorityChange_CheckInternetConnectivity');

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper()):
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
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
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%d.Wan.Priority"%i);
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        default = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the current WAN Priority for WANoE interface";
            print "EXPECTED RESULT 2: Should get the current WAN Priority for WANoE interface";
            print "ACTUAL RESULT 2: " ,default;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%d.Wan.Priority"%i);
            tdkTestObj.addParameter("ParamValue","2");
            tdkTestObj.addParameter("Type","int");
            #Execute testcase on DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Setresult = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Change the Priority for WANoE interface";
                print "EXPECTED RESULT 3: Should change the priority for WANoE interface"
                print "ACTUAL RESULT 3: ",Setresult;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                sysObj.initiateReboot();
                time.sleep(300);

                query ="ping -c 2 google.com |  grep -i \"100% packet loss\"";
                print "query:%s" %query;
                tdkTestObj.addParameter("command",query);
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip();
                if expectedresult in actualresult and details == "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Do a ping operation and check for internet connectivity";
                    print "EXPECTED RESULT 4: ping operation should be success with no 100% packet loss";
                    print "ACTUAL RESULT 4: ping operation is success and internet is available";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Do a ping operation and check for internet connectivity";
                    print "EXPECTED RESULT 4: ping operation should be success with no 100% packet loss";
                    print "ACTUAL RESULT 4: %s"%details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert the priority to previous
                tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%d.Wan.Priority"%i);
                tdkTestObj.addParameter("ParamValue",default);
                tdkTestObj.addParameter("Type","int");
                #Execute testcase on DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                Setresult = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Revert the Priority for WANoE interface";
                    print "EXPECTED RESULT 5: Should revert the priority for WANoE interface";
                    print "ACTUAL RESULT 5: ",Setresult;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Revert the Priority for WANoE interface to previous";
                    print "EXPECTED RESULT 5: Should revert the priority for WANoE interface";
                    print "ACTUAL RESULT 5: ",Setresult;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Change the Priority for WANoE interface";
                print "EXPECTED RESULT 3: Should change the priority for WANoE interface "
                print "ACTUAL RESULT 3: ",Setresult;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the current WAN Priority for WANoE interface number";
            print "EXPECTED RESULT 2: Should get the current WAN Priority for WANoE interface";
            print "ACTUAL RESULT 2: " ,default;
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
    obj1.unloadModule("tdkbtr181");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj1.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
