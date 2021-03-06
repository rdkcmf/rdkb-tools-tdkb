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
  <name>TS_PAM_EnableRFCWebConfig_CheckPersistence_OnReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if URL and Supported Docs are populated when Web-Config is enabled persists on reboot</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_205</test_case_id>
    <test_objective>This test case is to check if URL and Supported Docs are populated when Web-Config is enabled persists on reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.RfcEnable
Device.X_RDK_WebConfig.URL
Device.X_RDK_WebConfig.SupportedDocs</input_parameters>
    <automation_approch>1.Load the module
2.Get the current status of Web config RFC
3.Enable the Web config RFC
4.Reboot the DUT
5.Check if the expected URL and supported Docs are present even after reboot
6.Revert the set value
7.Unload the module</automation_approch>
    <expected_output>The expected URL and supported Docs are present even after reboot with Web config enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_EnableRFCWebConfig_CheckPersistence_OnReboot</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import tdkutility
from tdkutility import *
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_PAM_EnableRFCWebConfig_CheckPersistence_OnReboot');
sysobj.configureTestCase(ip,port,'TS_PAM_EnableRFCWebConfig_CheckPersistence_OnReboot');
#Get the result of connection with test component and DUT
pamloadmodulestatus =pamobj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
revert =0;
if  "SUCCESS" in pamloadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_RDK_WebConfig.RfcEnable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    initial_value = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get current value of Web Config Enable"
        print "EXPECTED RESULT 1: Should get current value of Web Config Enable"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        setValue = "true";
        if initial_value != "true":
            tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.X_RDK_WebConfig.RfcEnable");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","boolean");
            expectedresult="SUCCESS";
            #Execute testcase on DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            result = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                revert =1;
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set Web Config Enable status to true"
                print "EXPECTED RESULT 2: Should set Web Config Enable status to true"
                print "ACTUAL RESULT 2: %s" %result;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set Web Config Enable status to true"
                print "EXPECTED RESULT 2: Should set Web Config Enable status to true"
                print "ACTUAL RESULT 2: %s" %result;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
                setValue ="failed";
        if "true" == setValue:
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            expectedresult="SUCCESS";
            cmd= "sh %s/tdk_utility.sh parseConfigFile WEB_CONFIG_PARAMS" %TDK_PATH;
            print cmd;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and details!= "":
                URL= details.split(",")[0];
                SupDocs=details.split(".net,")[1];
                expectedValues  = [URL,SupDocs];
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Should get the configured WEB_CONFIG parameters"
                print "ACTUAL RESULT 3: WEB_CONFIG parameters value received succesfully" ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                sysobj.initiateReboot();
                sleep(300);

                paramList=["Device.X_RDK_WebConfig.URL","Device.X_RDK_WebConfig.SupportedDocs"];
                i=0;
                for item  in  paramList:
                    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
                    tdkTestObj.addParameter("ParamName",item);
                    expectedresult="SUCCESS";
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase("expectedresult");
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip();
                    if expectedresult in actualresult and expectedValues[i] in details:
                        print "The value received is %s and  equal to expected value" %details;
                        i=i+1;
                    else:
                        actualresult ="FAILURE";
                        print "%s is expected to have %s but has %s" %(item,expectedValues[i],details);
                        break;
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Should get the WEB_CONFIG parameters after enabling WEB CONFIG ";
                    print "EXPECTED RESULT 4: Should get the WEB_CONFIG parameters equal to the one configured after enabling";
                    print "ACTUAL RESULT 4:WEB_CONFIG parameters are equal to the one configured after enabling";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Should get the WEB_CONFIG parameters after enabling WEB CONFIG ";
                    print "EXPECTED RESULT 4: Should get the WEB_CONFIG parameters equal to the one configured after enabling";
                    print "ACTUAL RESULT 4:WEB_CONFIG parameters are not equal to the one configured after enabling";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Should get the configured WEB_CONFIG parameters"
                print "ACTUAL RESULT 3: WEB_CONFIG parameter values from properties file:%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert the value
            if revert ==1:
                tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WebConfig.RfcEnable");
                tdkTestObj.addParameter("ParamValue",initial_value);
                tdkTestObj.addParameter("Type","boolean");
                expectedresult="SUCCESS";
                #Execute testcase on DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                result = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Revert the Web Config Enable status to previous"
                    print "EXPECTED RESULT 5: Should revert Web Config status to previous"
                    print "ACTUAL RESULT 5: %s" %result;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Revert Web Config Enable status to previous"
                    print "EXPECTED RESULT 5: Should revert  Web Config Enable status to previous"
                    print "ACTUAL RESULT 5: %s" %result;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get current value of Web Config Enable"
        print "EXPECTED RESULT 1: Should get current value of Web Config Enable"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
