##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SNMP_ResetRouterOnly</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>GetCommString</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>This test case will reset the router through SNMP and check whether specific logs are logged in the PAM module log.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_SNMP_PA_18</test_case_id>
    <test_objective>This test case will reset the router through SNMP and check whether specific logs are logged in the PAM module log.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>snmpMethod : snmpset
snmpVersion : -v 2c
OID :1.3.6.1.4.1.17270.50.2.1.1.1003.0</input_parameters>
    <automation_approch>1.Function which needs to be tested will be configured in Test Manager GUI.
2.Python Script will be generated by Test Manager with provided arguments in configure page. 
3.TM will load the snmp_pa library via Test agent
4.From python script, invoke SnmpExecuteCmd function in snmplib to get the value of given OID 
5.GetCommString function in the SNMP_PA stub will be called from snmplib to get the community string. 
6.Send a SNMP query to reset the router and check whether reset logs are logged in the PAM module log
7.Validation of  the result is done within the python script and send the result status to Test Manager.
8.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.</automation_approch>
    <except_output>CheckPoint 1:
  Response of snmp command should be logged in the script log

CheckPoint 2:
Stub and lib function result should be success and should see corresponding log in the script log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>SNMP_PA_Stub</test_stub_interface>
    <test_script>TS_SNMP_RebootDUT</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;
from time import sleep;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SNMP_ResetRouterOnly');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    
    #Get the Community String
    commGetStr = snmplib.getCommunityString(obj,"snmpget");
    commSetStr = snmplib.getCommunityString(obj,"snmpset");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj);
    ########## Script to Execute the snmp command ###########
    actResponse =snmplib.SnmpExecuteCmd("snmpget", commGetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.1.1.1003.0", ipaddress);
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.executeTestCase("SUCCESS");
    
    act_value=actResponse.rsplit(None, 1)[-1];

    if "=" in actResponse and act_value == "0":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: snmpget request to get Reboot status";
        print "EXPECTED RESULT 1: Command should return Reboot status as false";
        print "ACTUAL RESULT 1: %s" %actResponse;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        
	#Get the RDKB Logger path
	getLogPath = "sh %s/tdk_utility.sh parseConfigFile RDKB_LOGGER_PATH" %TDK_PATH;
        print getLogPath;
        expectedresult="SUCCESS";
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", getLogPath);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        logPath = tdkTestObj.getResultDetails().strip();
        logPath = logPath.replace("\\n", "");
	if "Invalid Argument passed" not in logPath:
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: Get the log path of log file ";
            print "EXPECTED RESULT 2: Should get the log path of log file";
            print "ACTUAL RESULT 2: %s" %logPath;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            #Get the log path for creating temporary log file during runtime
            getRuntimeLogPath = "sh %s/tdk_utility.sh parseConfigFile RUNTIME_LOG_PATH" %TDK_PATH;
            print getRuntimeLogPath;
            expectedresult="SUCCESS";
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", getRuntimeLogPath);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            runtimeLogPath = tdkTestObj.getResultDetails().strip();
            runtimeLogPath = runtimeLogPath.replace("\\n", "");
            if "Invalid Argument passed" not in runtimeLogPath:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the log path for runtime log file creation ";
                print "EXPECTED RESULT 3: Should get the log path for runtime log file creation";
                print "ACTUAL RESULT 3: %s" %runtimeLogPath;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                #Tail the log file and redirect it to a local log file to handle the content loss during log rotation
                tailCommand = "tail -f "+logPath+"/PAMlog.txt.0 >> "+runtimeLogPath+"/log.txt & echo $!";
                tailCommand = tailCommand.replace("\\n", "");
                print tailCommand;
                tdkTestObj = obj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", tailCommand);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                tailpid = tdkTestObj.getResultDetails().strip();
                tailpid = tailpid.replace("\\n", "");
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Tail the log file and redirect the logs to a local log file";
                    print "EXPECTED RESULT 4: Log file should redirect the logs to a local log file";
                    print "ACTUAL RESULT 4: %s" %tailpid;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    #Wait for 100 secs for the router to reset after executing the SNMP query to reset the router.
                    #This delay is required to ensure the agent and test manager communication is not broken due to router reset
                    actResponse =snmplib.SnmpExecuteCmd("snmpset", commSetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.1.1.1003.0 i 2", ipaddress);
                    if "INTEGER: 2" in actResponse:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Send SNMP query to reset router";
                        print "EXPECTED RESULT 5: Router should reset";
                        print "ACTUAL RESULT 5: %s" %actResponse;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                        sleep(100);

                        # Kill the process
                        tdkTestObj = obj.createTestStep('ExecuteCmd');
                        killCmd = "kill -9 "+tailpid+"";
                        print "Kill tail process: %s" %killCmd
                        tdkTestObj.addParameter("command", killCmd)
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase("SUCCESS");
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip();
                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Kill the tail command running in background";
                            print "EXPECTED RESULT 6: tail process should be killed";
                            print "ACTUAL RESULT 6: %s" %actualresult;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS"
                            #Grep the log file for the expected logs
                            tdkTestObj = obj.createTestStep('ExecuteCmd');
                            string = "Router is going to reboot"
                            command = "grep -inr \"Router is going to reboot\" "+runtimeLogPath+"/log.txt;";
                            print command;
                            tdkTestObj.addParameter("command", command);
                            expectedresult="SUCCESS";
                            #Execute the test case in DUT
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails().strip();
                            print "grep details: %s" %details
                            if expectedresult in actualresult and string in details:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7: Check log whether erouter is reset";
                                print "EXPECTED RESULT 7: Log file should have the erouter reset log";
                                print "ACTUAL RESULT 7: %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS"
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 7: Check log whether erouter is reset";
                                print "EXPECTED RESULT 7: Log file should have the erouter reset log";
                                print "ACTUAL RESULT 7: %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE"
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Kill the tail command running in background";
                            print "EXPECTED RESULT 6: tail process should be killed";
                            print "ACTUAL RESULT 6: %s" %actualresult;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE"
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Send SNMP query to reset router";
                        print "EXPECTED RESULT 5: Router should reset";
                        print "ACTUAL RESULT 5: %s" %actResponse;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Tail the log file and redirect the logs to a local log file";
                    print "EXPECTED RESULT 4: Log file should redirect the logs to a local log file";
                    print "ACTUAL RESULT 4: %s" %tailpid;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the log path for runtime log file creation";
                print "EXPECTED RESULT 3: Should get the log path for runtime log file creation";
                print "ACTUAL RESULT 3: %s" %runtimeLogPath;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the log path of log file";
            print "EXPECTED RESULT 2: Should get the log path of log file";
            print "ACTUAL RESULT 2: %s" %logPath;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: snmpget request to get Reboot status";
        print "EXPECTED RESULT 1: Command should return Reboot status as false";
        print "ACTUAL RESULT 1: %s" %actResponse;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    #Remove the temporary log file created for testing purpose
    cleanupCmd = "rm -rf "+runtimeLogPath+"/log.txt;";
    print "Remove the local log file created: %s" %cleanupCmd;
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", cleanupCmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    print "Log Cleanup Status: %s" %actualresult;

    obj.unloadModule("sysutil");
else:
        print "FAILURE to load SNMP_PA module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";
