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
  <name>TS_WEBCONFIG_DisableRFC</name>
  <primitive_test_id/>
  <primitive_test_name>Webconfig_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To disable webconfig RFC and check WebConfig.log file to confirm the same</synopsis>
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
    <test_case_id>TC_WEBCONFIG_01</test_case_id>
    <test_objective>This test case is to disable webconfig RFC and check WebConfig.log file to confirm the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Webconfig distro should be enabled else enable with custom image</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.RfcEnable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current status of Webconfig RFC
3.Disable the Webconfig RFC
4.Check if "RFC disable"  is triggered in WebConfig.log file
5.Revert the RFC status to previous
6.Unload the module</automation_approch>
    <expected_output>The RFC should be disabled successfully and disabling triggered should be seen in WebConfig.log file</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_WEBCONFIG_DisableRFC</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
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
pamobj.configureTestCase(ip,port,'TS_WEBCONFIG_DisableRFC');
sysobj.configureTestCase(ip,port,'TS_WEBCONFIG_DisableRFC');
#Get the result of connection with test component and DUT
pamloadmodulestatus =pamobj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
revert = 0;
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

        tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WebConfig.RfcEnable");
        tdkTestObj.addParameter("ParamValue","false");
        tdkTestObj.addParameter("Type","boolean");
        expectedresult="SUCCESS";
        #Execute testcase on DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        result = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            revert =1;
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set Web Config Enable status to false";
            print "EXPECTED RESULT 2: Should set Web Config Enable status to false"
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            expectedresult="SUCCESS";
            cmd= "cat /rdklogs/logs/WebConfig.log  | grep -rn \"RFC disable\"";
            print cmd;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and details!= "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if RFC Disable is triggered in WebConfig.log file"
                print "ACTUAL RESULT 3:  RFC Disable should be triggered in WebConfig.log file" ;
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if RFC Disable is triggered in WebConfig.log file"
                print "ACTUAL RESULT 3:  RFC Disable should be triggered in WebConfig.log file" ;
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] :FAILURE";
        else:
            revert =0;
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set Web Config Enable status to false";
            print "EXPECTED RESULT 2: Should set Web Config Enable status to false"
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"

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
                print "TEST STEP 4: Revert the Web Config Enable status to previous"
                print "EXPECTED RESULT 4: Should revert Web Config status to previous"
                print "ACTUAL RESULT 4: %s" %result;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Revert Web Config Enable status to previous"
                print "EXPECTED RESULT 4: Should revert  Web Config Enable status to previous"
                print "ACTUAL RESULT 4: %s" %result;
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
