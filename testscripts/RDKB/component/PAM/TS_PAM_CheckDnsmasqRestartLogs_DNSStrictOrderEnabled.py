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
  <version>2</version>
  <name>TS_PAM_CheckDnsmasqRestartLogs_DNSStrictOrderEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the log "RFC DNSTRICT ORDER is not defined or Enabled" is not getting populated in the Consolelog.txt.0 during dnsmasq process restart when the DNS Strict Order RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is Enabled.</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_PAM_220</test_case_id>
    <test_objective>To check if the log "RFC DNSTRICT ORDER is not defined or Enabled" is not getting populated in the Consolelog.txt.0 during dnsmasq process restart when the DNS Strict Order RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is Enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable
PramValue : setValue
setValue : true
Type : bool</input_parameters>
    <automation_approch>1. Load the modules.
2. Get the initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable. If it is not true, set it to true.
3. Get the PID of dnsmasq process if it is running.
4. Get the initial number of log lines "RFC DNSTRICT ORDER is not defined or Enabled" present in Consolelog.txt.0
5. Kill the dnsmasq process and wait for the process to come up again.
6. Once the process comes up, check the final number of log lines "RFC DNSTRICT ORDER is not defined or Enabled" present in Consolelog.txt.0. It should be the same as the initial count and should not be incremented as DNSStrict is Enabled.
7. Revert to initial state if required.
8. Unload the modules.</automation_approch>
    <expected_output>The log "RFC DNSTRICT ORDER is not defined or Enabled" should not be populated in the Consolelog.txt.0 during dnsmasq process restart when the DNS Strict Order RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is Enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckDnsmasqRestartLogs_DNSStrictOrderEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getDNSStrict(pamobj, step):
    expectedresult = "SUCCESS";
    DNSStrict = " ";
    tdkTestObj = pamobj.createTestStep("pam_GetParameterValues");
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable" %(step);
    print "EXPECTED RESULT %d: Should successfully get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable" %(step);

    if expectedresult in actualresult:
        DNSStrict = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Parameter value retrieved successfully; Details : %s" %(step, DNSStrict);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Parameter value not retrieved successfully; Details : %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return actualresult,tdkTestObj,DNSStrict;

def setDNSStrict(pamobj, setValue, step):
    tdkTestObj = pamobj.createTestStep("pam_SetParameterValues");
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable");
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","bool");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable to %s" %(step, setValue);
    print "EXPECTED RESULT %d: Should successfully set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable to %s" %(step, setValue);

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Parameter value set successfully; Details : %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Parameter value set not successfully; Details : %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return actualresult,tdkTestObj;

def getLogFileTotalLinesCount(obj, step):
    logFile = "/rdklogs/logs/Consolelog.txt.0"
    search_string = "RFC DNSTRICT ORDER is not defined or Enabled";
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    cmd = "grep -ire " + "\"" + search_string + "\"  " + logFile + " | wc -l";
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "TEST STEP %d : Get the number of log lines currently present" %step;
    print "EXPECTED RESULT %d : Should get the number of log lines currently present" %step;
    print "Query : %s" %cmd;
    count = 0;

    if expectedresult in actualresult:
        count = int(tdkTestObj.getResultDetails().strip().replace("\\n", ""));
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Successfully captured the number of log lines present : %d" %(step, count);
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Failed to  capture the number of log lines present : %s" %(step, details);
        print "[TEST EXECUTION RESULT] : FAILURE";
    return count;

def checkDnsmasqPID(obj):
    #Get whether dnsmasq process is running, if so get the PID
    query="sh %s/tdk_platform_utility.sh checkProcess dnsmasq" %TDK_PATH
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
    return pid, actualresult, tdkTestObj;

def killDnsmasq_CheckLogs(obj, step):
    expectedresult = "SUCCESS";
    print "\nTEST STEP %d : Check if the DNSMASQ process is running and get the PID" %step;
    print "EXPECTED RESULT %d : DNSMASQ process should be running and PID retrieved" %step;

    initial_pid, actualresult, tdkTestObj = checkDnsmasqPID(obj);

    if expectedresult in actualresult and initial_pid.isdigit():
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: DNSMASQ process is running; PID of dnsmasq %s" %(step, initial_pid);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        print "\nGet the current number of log lines of \"RFC DNSTRICT ORDER is not defined or Enabled\"";
        step = step + 1;
        count = getLogFileTotalLinesCount(obj, step);

        #Kill DNSMASQ process
        step = step + 1;
        query="kill -9 " + initial_pid;
        print "query:%s" %query
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", query)
        tdkTestObj.executeTestCase("SUCCESS");
        actualresult = tdkTestObj.getResult();
        result = tdkTestObj.getResultDetails()

        print "\nTEST STEP %d : Kill the DNSMASQ process" %step;
        print "EXPECTED RESULT %d : Should kill the DNSMASQ process successfully" %step;

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: DNSMASQ process killed successfully" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the dnsmasq process is restarted every in 60s for 900s(as task_health_monitor.sh runs once in 15mins)
            step = step + 1;
            processfound = 0;

            print "\nTEST STEP %d : Check if the DNSMASQ process is restarted" %step;
            print "EXPECTED RESULT %d : DNSMASQ process should be restarted" %step;

            for iteration in range(1,16):
                print "Waiting for the DNSMASQ process to be restrated....\nIteration : %d" %iteration;
                new_pid, actualresult, tdkTestObj = checkDnsmasqPID(obj);

                if expectedresult in actualresult and new_pid.isdigit():
                    processfound = 1;
                    break;
                else:
                    sleep(60);
                    continue;

            if processfound == 1 and new_pid != initial_pid:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: DNSMASQ process restarted with PID : %s" %(step,new_pid);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "\nGet the current number of log lines of \"RFC DNSTRICT ORDER is not defined or Enabled\"";
                step = step + 1;
                final_count = getLogFileTotalLinesCount(obj, step);

                step = step + 1;
                print "\nTEST STEP %d : Check if the final number of log lines is the same and not incremented" %step;
                print "EXPECTED RESULT %d : The final number of log lines should be the same and not incremented" %step;
                print "Initial Count : %d" %count;
                print "Final Count : %d" %final_count;

                if final_count == count:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d:The final number of log lines is the same and not incremented" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d:The final number of log lines is not the same" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: DNSMASQ process is not restarted" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: DNSMASQ process is not killed successfully" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: DNSMASQ is not running" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return step;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckDnsmasqRestartLogs_DNSStrictOrderEnabled');
pamobj.configureTestCase(ip,port,'TS_PAM_CheckDnsmasqRestartLogs_DNSStrictOrderEnabled');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =pamobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    pamobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check the DNSStrict Enable status
    step = 1;
    actualresult,tdkTestObj,initial_DNSStrict = getDNSStrict(pamobj, step);

    if expectedresult in actualresult and initial_DNSStrict != " ":
        tdkTestObj.setResultStatus("SUCCESS");
        print "GET operation is success";

        if initial_DNSStrict == "true":
            print "The Initial value of DNSStrict ORDER is true, Toggle not required";
            #Kill the dnsmasq process if found running and check the logs on dnsmasq restart
            step = step + 1;
            step = killDnsmasq_CheckLogs(obj, step);
        else:
            print "The Initial value of DNSStrict ORDER is false, Toggle required";
            step = step + 1;
            setValue = "true";
            actualresult,tdkTestObj = setDNSStrict(pamobj, setValue, step);

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "Set operation is success";
                step = step + 1;
                actualresult,tdkTestObj,final_DNSStrict = getDNSStrict(pamobj, step);

                if expectedresult in actualresult and final_DNSStrict != " ":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Successfully fetched the DNSSStrict value after SET";

                    if final_DNSStrict == "true":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Set operation of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is reflected in Get";
                        #Kill the dnsmasq process if found running and check the logs on dnsmasq restart
                        step = step + 1;
                        step = killDnsmasq_CheckLogs(obj, step);

                        print "\nReverting to initial state....";
                        step = step + 1;
                        setValue = "false";
                        actualresult,tdkTestObj = setDNSStrict(pamobj, setValue, step);

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Revert operation is success";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Revert operation failed";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Set operation of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DNSStrictOrder.Enable is not reflected in Get";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Unable to fetch the DNSSStrict value after SET";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Set operation failed";
    else:
        tdkTestObj.setResultStatus("FAILED");
        print "GET operation failed";

    obj.unloadModule("sysutil");
    pamobj.unloadModule("pam");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    pamobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed"
