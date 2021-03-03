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
  <name>TS_WEBCONFIG_DisableRFC_QuerySyncParams</name>
  <primitive_test_id/>
  <primitive_test_name>Webconfig_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To disable the Webconfig RFC and check if a get operation on Force Sync parameters logs DB failure in  WebConfig.log file</synopsis>
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
    <test_case_id>TC_WEBCONFIG_02</test_case_id>
    <test_objective>This test is case is to disable the RFC and check if a get operation on Force Sync parameters logs DB failure in  WebConfig.log file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Webconfig distro should be enabled else enable with custom image</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.RfcEnable
Device.X_RDK_WebConfig.ConfigFile.1.ForceSyncCheck
Device.X_RDK_WebConfig.ConfigFile.1.SyncCheckOK"</input_parameters>
    <automation_approch>1.Load the module
2.Get the current webconfig RFC enable status and disable the RFC
3.Do a get operation on Force Sync check and Force Sync Check Ok parameters
4.Check if DB failed message specific to the parameter is logged in WebConfig.log File
5.Revert the RFC status to previous
6.Unload the module</automation_approch>
    <expected_output>When webconfig RFC is disabled and get operation done on Force Sync parameters should log Db failed message specific to the parameter in webConfig.log file</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_WEBCONFIG_DisableRFC_QuerySyncParams</test_script>
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
from time import sleep;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_WEBCONFIG_DisableRFC_QuerySyncParams');
sysobj.configureTestCase(ip,port,'TS_WEBCONFIG_DisableRFC_QuerySyncParams');
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
        print "[TEST EXECUTION RESULT] : SUCCESS";

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
            print "EXPECTED RESULT 2: Should set Web Config Enable status to false";
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            paramlist = ["Device.X_RDK_WebConfig.ConfigFile.1.ForceSyncCheck","Device.X_RDK_WebConfig.ConfigFile.1.SyncCheckOK"];
            logMsgs = ["ForceSyncCheck GET from DB failed","SyncCheckOK GET from DB failed"];
            i=0;
            for item in  paramlist:
                tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
                tdkTestObj.addParameter("ParamName",item);
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip();
                if expectedresult in actualresult:
                    print "Querying %s parameter is sucessfull" %item;
                    print "Check if DB failed message is seen on querying this specific parameter";
                    sleep(5);
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    expectedresult="SUCCESS";
                    cmd= "cat /rdklogs/logs/WebConfig.log  | grep -rn \"%s\" " %logMsgs[i];
                    print cmd;
                    expectedresult="SUCCESS";
                    tdkTestObj.addParameter("command", cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    i= i+1;
                    if expectedresult in actualresult and details:
                       tdkTestObj.setResultStatus("SUCCESS");
                       print"%s" %details;
                       print"The expected log message is present when Queried";
                       print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "The expected log message is not present: %s" %logMsgs[i];
                        print "[TEST EXECUTION RESULT] : FAILURE";
                        break;
        else:
            revert =0;
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set Web Config Enable status to false";
            print "EXPECTED RESULT 2: Should set Web Config Enable status to false";
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        if revert ==1 :
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
                print "TEST STEP 3: Revert the Web Config Enable status to previous"
                print "EXPECTED RESULT 3: Should revert Web Config status to previous"
                print "ACTUAL RESULT 3: %s" %result;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Revert Web Config Enable status to previous"
                print "EXPECTED RESULT 3: Should revert  Web Config Enable status to previous"
                print "ACTUAL RESULT 3: %s" %result;
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
