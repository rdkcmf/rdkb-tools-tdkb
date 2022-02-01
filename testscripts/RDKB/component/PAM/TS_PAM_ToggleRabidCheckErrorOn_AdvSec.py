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
  <version>4</version>
  <name>TS_PAM_ToggleRabidCheckErrorOn_AdvSec</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check no error on Advance security cloud are seen on enabling cujo-agent</synopsis>
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
    <test_case_id>TC_PAM_214</test_case_id>
    <test_objective>This test case is to check no error on Advance security cloud are seen on enabling cujo-agent</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Check if fingerprint is enabled
3.If enabled check cujo-agent processes is running if running check for any adv_sec cloud related error messages popping in /rdklogs/logs/
4.In case fingerprint not enabled , enable it and check for cujo-agent process running
5.Then check for any adv_sec cloud related error messages popping in /rdklogs/logs/
6.Since cujo-agent process is running no such error messages should be seen
7.Unload the module</automation_approch>
    <expected_output>with cujo-agent process running no adv_sec cloud related error messages should pop in /rdklogs/logs/</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_ToggleRabidCheckErrorOn_AdvSec</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''

import tdklib;
import time;
from tdkbVariables import *;
MAX_RETRY = 10;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_ToggleRabidCheckErrorOn_AdvSec.py');
obj1.configureTestCase(ip,port,'TS_PAM_ToggleRabidCheckErrorOn_AdvSec.py');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the DeviceFingerPrint Enable status";
        print "EXPECTED RESULT 1: Should get the  DeviceFingerPrint Enable status"
        print "ACTUAL RESULT 1: DeviceFingerPrint Enable status :%s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        if orgValue == "true":
            #check whether the process is running or not
            query="sh %s/tdk_platform_utility.sh checkProcess cujo-agent" %TDK_PATH
            print "query:%s" %query
            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase("SUCCESS");
            actualresult = tdkTestObj.getResult();
            pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
            if expectedresult in actualresult and pid:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2:Check if cujo-agent process is running";
                print "EXPECTED RESUT 2: Should get the PID of cujo-agent if process is running";
                print "ACTUAL RESULT 2: PID of cujo-agent process %s" %pid;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj1.createTestStep('ExecuteCmd');
                cmd = "grep -rin \"can't remove '/tmp/advsec_cloud_ipv4':\" /rdklogs/logs/";
                tdkTestObj.addParameter("command",cmd);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and details =="":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3 : Check if log message regarding advsec_cloud is logged";
                    print "EXPECTED RESULT 3:log meessage regarding advsec_cloud should not be logged";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3 : Check if log message regarding advsec_cloud is logged";
                    print "EXPECTED RESULT 3:log meessage regarding advsec_cloud should not be logged";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Check if cujo-agent process is running";
                print "EXPECTED RESULT 2: cujo-agent process should be running";
                print "ACTUAL RESULT 2: cujo-agent process is not running";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #check whether the process is running or not
            query="sh %s/tdk_platform_utility.sh checkProcess cujo-agent" %TDK_PATH
            print "query:%s" %query
            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase("SUCCESS");
            actualresult = tdkTestObj.getResult();
            pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
            if expectedresult in actualresult and pid == "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2:Check if cujo-agent process is not running";
                print "EXPECTED RESULT 2: cujo-agent process should not be running";
                print "ACTUAL RESULT 2: cujo-agent process is not running";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
                tdkTestObj.addParameter("ParamValue","true");
                tdkTestObj.addParameter("Type","bool");
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Enable the DeviceFingerPrint";
                    print "EXPECTED RESULT 3: Should Enable the DeviceFingerPrint";
                    print "ACTUAL RESULT 3:%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    #check whether the process is running or not
                    query="sh %s/tdk_platform_utility.sh checkProcess cujo-agent" %TDK_PATH
                    print "query:%s" %query
                    tdkTestObj = obj1.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", query)
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase("SUCCESS");
                    actualresult = tdkTestObj.getResult();
                    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
                    print "Check for every 10 secs whether the process is up"
                    retryCount = 0;
                    while retryCount < MAX_RETRY:
                        tdkTestObj.executeTestCase("SUCCESS");
                        actualresult = tdkTestObj.getResult();
                        pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
                        if expectedresult in actualresult and pid:
                            break;
                        else:
                            time.sleep(10);
                            retryCount = retryCount + 1;
                    if expectedresult in actualresult and pid:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4:Check if cujo-agent process is running";
                        print "EXPECTED RESULT 4: cujo-agent process should be running";
                        print "ACTUAL RESULT4: cujo-agent process is running with PID:%s" %pid;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        tdkTestObj = obj1.createTestStep('ExecuteCmd');
                        cmd = "grep -rin \"can't remove '/tmp/advsec_cloud_ipv4':\" /rdklogs/logs/";
                        tdkTestObj.addParameter("command",cmd);
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                        if expectedresult in actualresult and details =="":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 5 : Check if log message regarding advsec_cloud is logged";
                            print "EXPECTED RESULT 5:log meessage regarding advsec_cloud should not be logged";
                            print "ACTUAL RESULT 5: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5 : Check if log message regarding advsec_cloud is logged";
                            print "EXPECTED RESULT 5:log meessage regarding advsec_cloud should not be logged";
                            print "ACTUAL RESULT 5: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4:Check if cujo-agent process is running";
                        print "EXPECTED RESULT 4: cujo-agent process should be running";
                        print "ACTUAL RESULT 4: cujo-agent process is not running";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Enable the DeviceFingerPrint";
                    print "EXPECTED RESULT 3:Should Enable the Device Finger Print ";
                    print "ACTUAL RESULT 3:%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Check if cujo-agent process is not running";
                print "EXPECTED RESULT 2: cujo-agent process shoul not be running";
                print "ACTUAL RESULT 2: cujo-agent process is running";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.Enable");
        tdkTestObj.addParameter("ParamValue",orgValue);
        tdkTestObj.addParameter("Type","bool");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 6:Revert the DeviceFingerPrint enable status";
            print "EXPECTED RESULT 6: Revert operation should be suceess";
            print "ACTUAL RESULT 6:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 6:Revert the DeviceFingerPrint enable status";
            print "EXPECTED RESULT 6: Revert operation should be suceess";
            print "ACTUAL RESULT8 6:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the DeviceFingerPrint Enable status";
        print "EXPECTEE RESULT 1: Should get the DeviceFingerPrint Enable status";
        print "ACTUAL RESULT 1: Failed to get DeviceFingerPrint Enable status";
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
    obj1.unloadModule("sysutil");

else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
