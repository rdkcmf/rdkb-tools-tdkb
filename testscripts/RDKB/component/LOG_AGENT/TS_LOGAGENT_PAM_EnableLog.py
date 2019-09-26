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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_LOGAGENT_PAM_EnableLog</name>
  <primitive_test_id/>
  <primitive_test_name>LogAgent_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable logging of PAM module and check if the logs are getting updated in PAMlog.txt.0</synopsis>
  <groups_id/>
  <execution_time>40</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_LOGAGENT_3</test_case_id>
    <test_objective>Enable logging of PAM module and check if the logs are getting updated in PAMlog.txt.0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>TDK Agent should be in running state.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.LogAgent.X_RDKCENTRAL-COM_LoggerEnable : True
Device.LogAgent.X_RDKCENTRAL-COM_PAM_LoggerEnable : True</input_parameters>
    <automation_approch>1. Load LogAgent module
2. Get and save the values of log enable status
3. Set true to PAM log enable status
4. Check if the PandM process is up and running in device
5. When the process is up, get and save the timestamp of PAMlog.txt.0
6. Get the values of PAM related parameters and check if the timestamp in log file is changed or not.
7. Revert the values
8. Unload module</automation_approch>
    <except_output>The logs should get updated in PAMlog.txt.0</except_output>
    <priority>High</priority>
    <test_stub_interface>LOG_AGENT</test_stub_interface>
    <test_script>TS_LOGAGENT_PAM_EnableLog</test_script>
    <skipped>No</skipped>
    <release_version>M65</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbVariables import *;

MAX_RETRY = 6;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LOGAGENT_PAM_EnableLog');
sysobj.configureTestCase(ip,port,'TS_LOGAGENT_PAM_EnableLog');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.LogAgent.X_RDKCENTRAL-COM_LoggerEnable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    LogStatus = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the enable status of Logging";
        print "EXPECTED RESULT 1: Should get the enable status of logging";
        print "ACTUAL RESULT 1: Enable status is %s" %LogStatus;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj.addParameter("ParamName","Device.LogAgent.X_RDKCENTRAL-COM_PAM_LoggerEnable");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        PamLogStatus = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the enable status of PAM Logging";
            print "EXPECTED RESULT 2: Should get the enable status of PAM logging";
            print "ACTUAL RESULT 2: Enable status is %s" %PamLogStatus;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Set true to both namespaces
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.LogAgent.X_RDKCENTRAL-COM_LoggerEnable|true|bool|Device.LogAgent.X_RDKCENTRAL-COM_PAM_LoggerEnable|true|bool");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Enable logging of PAM module"
                print "EXPECTED RESULT 3: Should enable PAM logging"
                print "ACTUAL RESULT 3: %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";
                #Check the timestamp of PAMlog.txt.0
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "tail -1 /rdklogs/logs/PAMlog.txt.0"
                tdkTestObj.addParameter("command", cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                lastLineofLog = tdkTestObj.getResultDetails().strip();
                if lastLineofLog:
                    oldTimeStamp = lastLineofLog.split(" ")[0]
                    print "Current timestamp in PAMlog.txt.0 is %s" %oldTimeStamp
                #If log file is empty
                else:
                    oldTimeStamp = " "

                #check whether the process is restarted automatically
                query="sh %s/tdk_platform_utility.sh checkProcess CcspPandMSsp" %TDK_PATH
                print "query:%s" %query
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";

                print "Check for every 10 secs whether the process is up"
                retryCount = 0;
                while retryCount < MAX_RETRY:
                    tdkTestObj.executeTestCase("SUCCESS");
                    actualresult = tdkTestObj.getResult();
                    pid = tdkTestObj.getResultDetails().strip();
                    if expectedresult in actualresult and pid:
                        break;
                    else:
                        sleep(10);
                        retryCount = retryCount + 1;

                if not pid:
                    print "Retry Again: Check for every 5 mins whether the process is up"
                    retryCount = 0;
                    while retryCount < MAX_RETRY:
                        tdkTestObj.executeTestCase("SUCCESS");
                        actualresult = tdkTestObj.getResult();
                        pid = tdkTestObj.getResultDetails().strip();
                        if expectedresult in actualresult and pid:
                            break;
                        else:
                            sleep(300);
                            retryCount = retryCount + 1;

                #Get the values of PAM parameters
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.1.Enable");
                expectedresult="SUCCESS";

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails()
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the value of PAM parameters";
                    print "EXPECTED RESULT 4: Should get the value of PAM parameters";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Get and compare the new timestamp of PAMlog.txt.0
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    lastLineofLog = tdkTestObj.getResultDetails().strip();
                    if lastLineofLog:
                        newTimeStamp = lastLineofLog.split(" ")[0]
                        print "New timestamp in PAMlog.txt.0 is %s" %newTimeStamp
                        if newTimeStamp == oldTimeStamp:
                            print "FAILURE:The logs are not updated in the log file"
                            tdkTestObj.setResultStatus("FAILURE");
                        else:
                            print "SUCCESS:The logs are updated in log file"
                            tdkTestObj.setResultStatus("SUCCESS");
                    #If log file is empty
                    else:
                        newTimeStamp = " "
                        print "FAILURE:The Logs are not updated in the file"
			tdkTestObj.setResultStatus("FAILURE");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the value of PAM parameters";
                    print "EXPECTED RESULT 4: Should get the value of PAM parameters";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert the log enable status
                tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
                tdkTestObj.addParameter("paramList","Device.LogAgent.X_RDKCENTRAL-COM_LoggerEnable|%s|bool|Device.LogAgent.X_RDKCENTRAL-COM_PAM_LoggerEnable|%s|bool" %(LogStatus,PamLogStatus));
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Revert the logging status"
                    print "EXPECTED RESULT : Should revert the logging status"
                    print "ACTUAL RESULT : %s" %details;
                    print "TEST EXECUTION RESULT :SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP : Revert the logging status"
                    print "EXPECTED RESULT : Should revert the logging status"
                    print "ACTUAL RESULT : %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Enable logging of PAM module"
                print "EXPECTED RESULT 3: Should enable PAM logging"
                print "ACTUAL RESULT 3: %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the enable status of PAM Logging";
            print "EXPECTED RESULT 2: Should get the enable status of PAM logging";
            print "ACTUAL RESULT 2: Enable status is %s" %PamLogStatus;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the enable status of Logging";
        print "EXPECTED RESULT 1: Should get the enable status of logging";
        print "ACTUAL RESULT 1: Enable status is %s" %LogStatus;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
