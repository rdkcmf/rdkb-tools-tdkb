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
  <version>14</version>
  <name>TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Logging</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the channel utilization marker CHUTIL_1  logging is happening according to the log interval set with Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval.</synopsis>
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
    <test_case_id>TC-WIFIAGENT_147</test_case_id>
    <test_objective>To check if the channel utilization marker CHUTIL_1  logging is happening according to the log interval set with Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval
ParamValue : 30 or 60
Type : int
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval.
3. If the initial value is 30, set it to 60 else set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval to 30.
4. Check if the log file wifihealth.txt is present under /rdklogs/logs.
5. Get the initial count of the telemetry marker CHUTIL_1 and store it.
6. Sleep for a wait time of sum of  initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval and the new value set.
7. After the wait time, check the final count of the telemetry marker CHUTIL_1 and compute the difference with the initial value.
8. The difference should be greater than or equal to 2.
9. Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval to initial value.
10. Unload the modules.</automation_approch>
    <expected_output>The channel utilization marker CHUTIL_1  logging should happen according to the log interval set with Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Logging</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getLogFileTotalLinesCount(tdkTestObj, string, step):
    cmd = "grep -ire " + "\"" + string + "\"  " + "/rdklogs/logs/wifihealth.txt | wc -l";
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\n*********************************************";
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
    print "*********************************************\n";
    return count,step;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Logging');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Logging');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    step = 1;
    #Check whether the wifihealth.txt file is present or not
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for wifihealth log file presence" %step;
    print "EXPECTED RESULT %d:wifihealth log file should be present" %step;

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d:wifihealth log file is present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        step = step + 1;
        #Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval
        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initial_value = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d: Get the TELEMETRY Channel Utility LogInterval from Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval" %step;
        print "EXPECTED RESULT %d: Should get the TELEMETRY Channel Utility LogInterval from Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval" %step;

        if expectedresult in actualresult and initial_value != "":
            DeflogInt = int(initial_value);
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: TELEMETRY Channel Utility LogInterval: %d" %(step,DeflogInt);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if DeflogInt == 30:
                newlogInt = "60";
            else:
                newlogInt = "30";

            #Set the LogInterval to newlogInt, the set is cross checked with get
            step = step + 1;
            tdkTestObj = obj.createTestStep('pam_SetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval");
            tdkTestObj.addParameter("ParamValue",newlogInt);
            tdkTestObj.addParameter("Type","int");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Set the TELEMETRY Channel Utility LogInterval to %ss" %(step, newlogInt);
            print "EXPECTED RESULT %d: Should set the TELEMETRY Channel Utility LogInterval to %ss" %(step, newlogInt);

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: TELEMETRY Channel Utility LogInterval: %s" %(step,details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "\nGet the number of log lines \"CHUTIL_1\" in /rdklogs/logs/wifihealth.txt";
                step = step + 1;
                tdkTestObj1 = sysObj.createTestStep('ExecuteCmd');
                log = "CHUTIL_1";
                no_of_lines_initial,step = getLogFileTotalLinesCount(tdkTestObj1, log, step);
                print "The initial number of log lines \"CHUTIL_1\" in wifihealth.txt is : %d" %no_of_lines_initial;

                #Sleeping for initial telemetry interval DeflogInt + newlogInt
                sleep_time = DeflogInt + int(newlogInt);
                print "\nSleeping for duration : %d to check if the logging is happening according to the new log interval set" %sleep_time;
                sleep(sleep_time);

                print "\nGet the final number of log lines \"CHUTIL_1\" in /rdklogs/logs/wifihealth.txt";
                step = step + 1;
                tdkTestObj1 = sysObj.createTestStep('ExecuteCmd');
                log = "CHUTIL_1";
                no_of_lines_final,step = getLogFileTotalLinesCount(tdkTestObj1, log, step);
                print "The initial number of log lines \"CHUTIL_1\" in wifihealth.txt is : %d" %no_of_lines_final;

                step = step + 1;
                difference = no_of_lines_final - no_of_lines_initial;
                print "\nThe CHUTIL_1 log lines can be >= 2, after accounting for the initial log interval and the new log interval set";

                print "TEST STEP %d: Should get CHUTIL_1 markers count greater than or equal to 2" %step;
                print "EXPECTED RESULT %d: The CHUTIL_1 markers count should be greater than or equal to 2" %step;

                if difference >= 2:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Number of new CHUTIL_1 markers are : %d" %(step, difference);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Number of new CHUTIL_1 markers are : %d" %(step, difference);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Set operation failed" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] :FAILURE";

            #Revert the Value
            step = step + 1;
            tdkTestObj = obj.createTestStep('pam_SetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.ChUtilityLogInterval");
            tdkTestObj.addParameter("ParamValue",initial_value);
            tdkTestObj.addParameter("Type","int");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Revert the TELEMETRY Channel Utility LogInterval to initial value" %step;
            print "EXPECTED RESULT %d: Should revert the TELEMETRY Channel Utility LogInterval to initial value" %step;

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Revert successful" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Revertion failed" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: TELEMETRY Channel Utility LogInterval: %s" %(step,details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d:wifihealth log file is not present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam")
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

