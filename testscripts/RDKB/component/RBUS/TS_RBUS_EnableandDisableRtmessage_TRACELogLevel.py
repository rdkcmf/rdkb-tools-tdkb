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
  <version>3</version>
  <name>TS_RBUS_EnableandDisableRtmessage_TRACELogLevel</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if setting rtmessage to TRACE log level is success and the required log lines are seen in the rtrouted.log file for any two randomly selected TRACE levels in the range 1-9. The resetting of log level from TRACE level should also be success and the corresponding log lines should be present in rtrouted.log file.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_RBUS_88</test_case_id>
    <test_objective>To check if setting rtmessage to TRACE log level is success and the required log lines are seen in the rtrouted.log file for any two randomly selected TRACE levels in the range 1-9. The resetting of log level from TRACE level should also be success and the corresponding log lines should be present in rtrouted.log file.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the modules
2. Check if the device is in RBUS mode using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable and if not, enable this parameter and reboot the device and check if the device comes up in RBUS mode.
3. Check if the file rtrouted.log is present under /rdklogs/logs
4. Chose any two TRACE levels randomly from the applicable range of 1 to 9
5. Check the initial line count of Set TRACE loglevel log lines and Reset TRACE loglevel log lines in rtrouted.log and store it
6. Set the rtmessage log level to TRACE using the command "rdklogctrl rtrouted LOG.RDK.RTMESSAGE TRACE"
7. Wait for 2 minutes and then check for the presence of set TRACE log level log lines are verify if it is incremented by 1 after the set operation.
8. Disable/Reset the TRACE log level using the command "rdklogctrl rtrouted LOG.RDK.RTMESSAGE ~TRACE"
9. Wait for 2 minutes and then check if the disable TRACE log level line is incremented by 1 after the disable operation.
10. Revert to initial state if required
11. Unload the modules</automation_approch>
    <expected_output>The rtmessage TRACE log levels should be enabled and disabled successfully and the corresponding log lines should be present in rtrouted.log file.</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_EnableandDisableRtmessage_TRACELogLevel</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbRBUS_Utility import *;
from tdkutility import *;
from time import sleep;
from random import randint;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RBUS_EnableandDisableRtmessage_TRACELogLevel');
tr181obj.configureTestCase(ip,port,'TS_RBUS_EnableandDisableRtmessage_TRACELogLevel');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    revert_flag = 0;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
    print "\nTEST STEP 1: Execute the Pre Requisite for RBUS"
    print "EXPECTED RESULT 1: Pre Requisite of RBUS should be success"
    #Execute the PreRequisite of RBUS
    rbus_set,revert_flag = rbus_PreRequisite(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj);

    if rbus_set == 1:
        print "ACTUAL RESULT 1: PreRequisite of RBUS was Success"
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "\n******************************************************************"

        #Check if rtrouted.log file is present or not
        file = "/rdklogs/logs/rtrouted.log";
        cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
        print "\nCommand : ", cmd;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "TEST STEP 2: Check for %s file presence" %(file);
        print "EXPECTED RESULT 2: %s file should be present" %(file);

        if expectedresult in actualresult and details == "File exist":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: %s file is present" %(file);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            step = 2;
            #Considering any 2 TRACE levels randomly
            for iteration in range(0,2):
                #Get a TRACE level randomly in the available range of 1-9
                traceLevel = randint(1,9);
                print "\n*****************For TRACE LEVEL : %d*******************" %traceLevel;

                #Get the set log line count
                print "\nGet the current number of log lines of \"rdk_dyn_log_validateComponentName(): Set TRACE%d loglevel for the component LOG.RDK.RTMESSAGE of the process rtrouted\"" %traceLevel;
                step = step + 1;
                search_string_loglevelSet = "rdk_dyn_log_validateComponentName(): Set TRACE" + str(traceLevel) + " loglevel for the component LOG.RDK.RTMESSAGE of the process rtrouted";
                count_loglevelSet_initial = getLogFileTotalLinesCount(tdkTestObj, file, search_string_loglevelSet, step);

                #Get the disable log line count
                print "\nGet the current number of log lines of \"rdk_dyn_log_validateComponentName(): Set !TRACE%d loglevel for the component LOG.RDK.RTMESSAGE of the process rtrouted\"" %traceLevel;
                step = step + 1;
                search_string_loglevelReset = "rdk_dyn_log_validateComponentName(): Set !TRACE" + str(traceLevel) + " loglevel for the component LOG.RDK.RTMESSAGE of the process rtrouted"
                count_loglevelReset_initial = getLogFileTotalLinesCount(tdkTestObj, file, search_string_loglevelReset, step);

                #Execute the set rtmessage log level command
                step = step + 1;
                cmd = "rdklogctrl rtrouted LOG.RDK.RTMESSAGE TRACE" + str(traceLevel);
                print "\nCommand : %s" %cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip();
                print "TEST STEP %d: Set the rtmessage log level to TRACE%d" %(step, traceLevel);
                print "EXPECTED RESULT %d: Should successfully set the rtmessage log level to TRACE%d" %(step, traceLevel);

                if expectedresult in actualresult and "Sent message to update log level of LOG.RDK.RTMESSAGE for rtrouted process" in details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: The rtmessage log level is set to TRACE%d successfully; Details : %s" %(step, traceLevel, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Wait for 120s before checking the rtrouted.log
                    sleep(120);
                    #Check the final log lines of log level set in rtrouted.log
                    print "\nGet the final number of log lines of \"rdk_dyn_log_validateComponentName(): Set TRACE%d loglevel for the component LOG.RDK.RTMESSAGE of the process rtrouted\"" %traceLevel;
                    step = step + 1;
                    count_loglevelSet_final = getLogFileTotalLinesCount(tdkTestObj, file, search_string_loglevelSet, step);

                    #Check if the final log line number is incremented by 1
                    step = step + 1;
                    print "\nTEST STEP %d : Check if the final number of log lines is incremented by 1" %step;
                    print "EXPECTED RESULT %d : The final number of log lines should be incremented by 1" %step;
                    print "Initial Count : %d" %count_loglevelSet_initial;
                    print "Final Count : %d" %count_loglevelSet_final;

                    if count_loglevelSet_final == (count_loglevelSet_initial + 1):
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d:The final number of log lines is incremented by 1" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d:The final number of log lines is not incremented by 1" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Execute the disable rtmessage log level command
                    step = step + 1;
                    cmd = "rdklogctrl rtrouted LOG.RDK.RTMESSAGE ~TRACE" + str(traceLevel);
                    print "\nCommand : %s" %cmd;
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip();
                    print "TEST STEP %d: Reset the rtmessage log level from TRACE%d" %(step, traceLevel);
                    print "EXPECTED RESULT %d: Should successfully Disable the rtmessage log level from TRACE%d" %(step, traceLevel);

                    if expectedresult in actualresult and "Sent message to update log level of LOG.RDK.RTMESSAGE for rtrouted process" in details:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: The rtmessage log level TRACE%d is disabled successfully; Details : %s" %(step, traceLevel, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Wait for 120s before checking the rtrouted.log
                        sleep(120);
                        #Get the reset log line count
                        print "\nGet the final number of log lines of \"rdk_dyn_log_validateComponentName(): Set !TRACE%d loglevel for the component LOG.RDK.RTMESSAGE of the process rtrouted\"" %traceLevel;
                        step = step + 1;
                        count_loglevelReset_final = getLogFileTotalLinesCount(tdkTestObj, file, search_string_loglevelReset, step);

                        #Check if the final log line number is incremented by 1
                        step = step + 1;
                        print "\nTEST STEP %d : Check if the final number of log lines is incremented by 1" %step;
                        print "EXPECTED RESULT %d : The final number of log lines should be incremented by 1" %step;
                        print "Initial Count : %d" %count_loglevelReset_initial
                        print "Final Count : %d" %count_loglevelReset_final;

                        if count_loglevelReset_final == (count_loglevelReset_initial + 1):
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d:The final number of log lines is incremented by 1" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d:The final number of log lines is not incremented by 1" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: The rtmessage log level TRACE%d is not disabled successfully; Details : %s" %(step, traceLevel, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: The rtmessage log level is not set to TRACE%d successfully; Details : %s" %(step, traceLevel, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: %s file is not present" %(file);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: PreRequisite of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] : FAILURE";

    print "\n******************************************************************";
    step = step + 1;
    print "\nTEST STEP %d: Execute the Post process of RBUS" %step;
    print "EXPECTED RESULT %d: Post process of RBUS should be success" %step;
    post_process_value = rbus_PostProcess(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj,revert_flag);

    if post_process_value == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Post process of RBUS was Success" %step;
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Post process of RBUS was FAILED" %step;
        print "[TEST EXECUTION RESULT] : FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
