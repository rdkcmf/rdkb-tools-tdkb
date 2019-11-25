##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_PAM_CheckRabidProcess</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To enable rabid framework and check if rabid process is running</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>3</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_156</test_case_id>
    <test_objective>To enable rabid framework and check if rabid process is running</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable</input_parameters>
    <automation_approch>1.Load module
2.Enable rabid framework
3.Check if rabid process is running</automation_approch>
    <expected_output>After enabling rabid framework rabid process should be running</expected_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_PAM_CheckRabidProcess</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
import time;
from tdkbVariables import *;


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","RDKB");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckRabidProcess');
obj1.configureTestCase(ip,port,'TS_PAM_CheckRabidProcess');


#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;



if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the RabidFramework Enable status";
        print "ACTUAL RESULT 1: RabidFramework Enable status :%s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
        tdkTestObj.addParameter("ParamValue","true");
        tdkTestObj.addParameter("Type","bool");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Enable the rabid framework";
            print "ACTUAL RESULT 2:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            time.sleep(30);
            #check whether the process is running or not
            query="sh %s/tdk_platform_utility.sh checkProcess rabid" %TDK_PATH
            print "query:%s" %query
            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase("SUCCESS");
            actualresult = tdkTestObj.getResult();
            pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
            if expectedresult in actualresult and pid:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if rabid process is running";
                print "ACTUAL RESULT 3: PID of Rabid process %s" %pid;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Check if rabid process is running";
                print "ACTUAL RESULT 3: Rabid process is not running";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj = obj.createTestStep('pam_SetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
            tdkTestObj.addParameter("ParamValue",orgValue);
            tdkTestObj.addParameter("Type","bool");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP :Revert the rabid framework enable status";
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP :Revert the rabid framework enable status";
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Enable the rabid framework";
            print "ACTUAL RESULT 2:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the RabidFramework Enable status";
        print "ACTUAL RESULT 1: Failed to get RabidFramework Enable status";
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
    obj1.unloadModule("sysutil");
    
else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

