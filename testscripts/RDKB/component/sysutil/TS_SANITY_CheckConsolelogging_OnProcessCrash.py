##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_SANITY_CheckConsolelogging_OnProcessCrash</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the logging of "lsof: not found" is not happening in Consolelog.txt.0 when a process is killed.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_68</test_case_id>
    <test_objective>To check if the logging of "lsof: not found" is not happening in Consolelog.txt.0 when a process is killed.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the module
2. Check for Consolelog.txt.0 presence under /rdklogs/logs
3. Get the initial line count of "lsof: not found" in Consolelog.txt.0
4. Get the PID of webpa process
5. Kill the webpa process
6. Ensure that the process comes up by checking every 10s for 1 min duration
7. Check the final line count of "lsof: not found". The manual killing of webpa process should not cause the logging, so it should be the same as the initial count.
8. Unload the module</automation_approch>
    <expected_output>The logging of "lsof: not found" should not happen in Consolelog.txt.0 when a process is killed.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckConsolelogging_OnProcessCrash</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;
from tdkutility import *;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckConsolelogging_OnProcessCrash');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    #Check if Consolelog.txt.0 is present
    step = 1;
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/Consolelog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for Consolelog.txt.0 file presence" %step;
    print "EXPECTED RESULT %d: Consolelog.txt.0 should be present" %step;

    if details == "File exist" :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Consolelog.txt.0 is present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the initial line count of "lsof: not found"
        step = step + 1;
        file = "Consolelog.txt.0"
        print "\nGet the current number of log lines of \"lsof: not found\"";
        search_string = "lsof: not found"
        count_loglevel_initial = getLogFileTotalLinesCount(tdkTestObj, file, search_string, step);

        #Get the PID of webpa process
        step = step + 1;
        ps_name = "webpa"
        actualresult, initial_pid = getPID(tdkTestObj, ps_name);

        print "\nTEST STEP %d : Get the initial PID of Webpa process" %step;
        print "EXPECTED RESULT %d : Should successfully get the initial pidof Webpa process" %step;

        if expectedresult in actualresult and initial_pid.isdigit():
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : Initial PID obtained successfully : %s" %(step, initial_pid);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Kill the process
            step = step + 1;
            cmd = "kill -11 %s " %initial_pid;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d : Should successfully kill the process" %step;
            print "EXPECTED RESULT %d : The process should be killed successfully" %step;

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Process is killed" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the process is back up with a different PID every 10 seconds for 1 minute
                step = step + 1;
                processfound = 0;

                print "\nTEST STEP %d : Check if the Webpa process is restarted" %step;
                print "EXPECTED RESULT %d : Webpa process should be restarted" %step;

                for iteration in range(1,7):
                    print "Waiting for the webpa process to be restarted....\nIteration : %d" %iteration;
                    actualresult, new_pid = getPID(tdkTestObj, ps_name);

                    if expectedresult in actualresult and new_pid.isdigit():
                        processfound = 1;
                        break;
                    else:
                        sleep(10);
                        continue;

                if processfound == 1 and new_pid.isdigit() and new_pid != initial_pid:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Webpa process restarted with PID : %s" %(step, new_pid);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    print "\nGet the current number of log lines of \"lsof: not found\"";
                    step = step + 1;
                    count_loglevel_final = getLogFileTotalLinesCount(tdkTestObj, file, search_string, step);

                    #Check if no new instance of "lsof: not found" is found in the Console.log.txt.0
                    step = step + 1;
                    print "\nTEST STEP %d : Check if no new logging of \"lsof: not found\" is seen in Consolelog.txt.0" %step;
                    print "EXPECTED RESULT %d : No new logging of \"lsof: not found\" should be seen in Consolelog.txt.0" %step;
                    print "Initial Count : %d" %count_loglevel_initial;
                    print "Final Count : %d" %count_loglevel_final;

                    if count_loglevel_final == count_loglevel_initial:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: No new logging of \"lsof: not found\" is seen in Consolelog.txt.0" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: New logging of \"lsof: not found\" is seen in Consolelog.txt.0" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Webpa process restarted with PID : %s" %(step, new_pid);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Process is not killed" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : Initial PID not obtained successfully : %s" %(step, initial_pid);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Consolelog.txt.0 : %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
