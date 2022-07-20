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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckTelemetryMarkerUP_RetransCount_2_Logging</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the telemetry for WiFi Packet Retries in the uplink direction for 5G "UP_RetransCount_2" is getting logged properly in wifihealth.txt within the specified Log Interval after the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable and Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable are enabled.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_202</test_case_id>
    <test_objective>Check if the telemetry for WiFi Packet Retries in the uplink direction for 5G "UP_RetransCount_2" is getting logged properly in wifihealth.txt within the specified Log Interval after the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable and Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable are enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Connect a wifi client to 5G radio private access point</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable
paramValue : true/false
paramType : boolean
paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
paramValue : 300 or 360
paramType : int</input_parameters>
    <automation_approch>1. Load the modules
2. Check if wifihealth.txt is present under /rdklogs/logs
3. Get the initial enable status of the RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable
4. If the RFC is not enabled, set to true and validate the set
5. Get the initial value of Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable
6. If the enable parameter for 5G private AP is  not enabled, set to true and validate the set.
7. Get the current telemetry log interval using Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
8. Set Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to a valid interval (300s or 360s) and validate the set
9. Get the initial marker count of "UP_RetransCount_2" in wifihealth.txt for the connected client.
10. Sleep for a duration set by the log interval and 60s to include the telemetry log interval polling time.
11. Get the final marker count of "UP_RetransCount_2" in wifihealth.txt for the connected client.
12. The difference between the final and initial number of "UP_RetransCount_2" markers in wifihealth.txt should be greater than or equal to 1.
13. Check if the marker value is a valid integer greater than 0.
14. Revert the telemetry log interval to initial value
15. Revert Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable if required.
16. Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable if required.
17. Unload the modules</automation_approch>
    <expected_output>The telemetry for WiFi Packet Retries in the uplink direction for 5G "UP_RetransCount_2" should get logged properly in wifihealth.txt within the specified Log Interval after the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable and Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable are enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerUP_RetransCount_2_Logging</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def getParameter(obj, param):
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName", param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

def setParameter(obj, param, setValue, type):
    expectedresult = "SUCCESS";
    status = 0;
    tdkTestObj = obj.createTestStep('WIFIAgent_Set_Get');
    tdkTestObj.addParameter("paramName",param);
    tdkTestObj.addParameter("paramValue",setValue);
    tdkTestObj.addParameter("paramType",type);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;
from tdkutility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerUP_RetransCount_2_Logging');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerUP_RetransCount_2_Logging');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check whether the wifihealth.txt file is present or not
    step = 1;
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for wifihealth log file presence under /rdklogs/logs" %step;
    print "EXPECTED RESULT %d:wifihealth log file should be present under /rdklogs/logs" %step;

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d:wifihealth log file is present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the value of the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable
        step = step + 1;
        paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable";
        actualresult, details = getParameter(obj, paramName);

        print "\nTEST STEP %d: Get the enable state of the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable" %step;
        print "EXPECTED RESULT %d: Should get the enable state of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable" %step;

        if expectedresult in actualresult and details != "":
            rfc_initial = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Errors Received Enable is : %s" %(step,rfc_initial);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #If RFC not enabled, enable it and validate the set operation
            proceed_flag = 0;
            revert_flag_rfc = 0;
            if rfc_initial != "true":
                step = step + 1;
                actualresult, details = setParameter(obj, paramName, "true", "boolean");

                print "\nTEST STEP %d: Set the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable to true" %step;
                print "EXPECTED RESULT %d: Should set the enable state of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable to true" %step;

                if expectedresult in actualresult and details != "":
                    proceed_flag = 1;
                    revert_flag_rfc = 1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: RFC value is set successfully; Details : %s" %(step,details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: RFC value is NOT set successfully; Details : %s" %(step,details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                proceed_flag = 1;
                print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable is already enabled, SET operation not required";

            if proceed_flag == 1:
                #Check if Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable for the AP 1 is enabled
                step = step + 1;
                paramName = "Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable";
                actualresult, details = getParameter(obj, paramName);

                print "\nTEST STEP %d: Get the enable state of Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable" %step;
                print "EXPECTED RESULT %d: Should get the enable state of Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable" %step;

                if expectedresult in actualresult and details != "":
                    error_stats_initial = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Associated Devices Errors Received Stats Enable is : %s" %(step, error_stats_initial);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #If not enabled, enable it and validate the set operation
                    proceed_flag = 0;
                    revert_flag_stats = 0;

                    if error_stats_initial != "true":
                        step = step + 1;
                        actualresult, details = setParameter(obj, paramName, "true", "boolean");

                        print "\nTEST STEP %d: Set Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable to true" %step;
                        print "EXPECTED RESULT %d: Should set the enable state of Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable to true" %step;

                        if expectedresult in actualresult and details != "":
                            proceed_flag = 1;
                            revert_flag_stats = 1;
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Associated Devices Errors Received Stats Enable is SET; Details : %s" %(step,details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Associated Devices Errors Received Stats Enable value is NOT set successfully; Details : %s" %(step,details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        proceed_flag = 1;
                        print "Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable is already enabled, SET operation not required";

                    if proceed_flag == 1:
                        #Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
                        step = step + 1;
                        paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval";
                        actualresult, details = getParameter(obj, paramName);

                        print "\nTEST STEP %d: Get the TELEMETRY LogInterval from Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval" %step;
                        print "EXPECTED RESULT %d: Should get the TELEMETRY LogInterval from Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval" %step;

                        if expectedresult in actualresult and details != "":
                            DeflogInt = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: TELEMETRY LogInterval: %s" %(step,DeflogInt);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if DeflogInt.isdigit():

                                if DeflogInt != "300":
                                    newlogInt = "300";
                                else:
                                    newlogInt = "360";

                                #Set the LogInterval to newlogInt, the set is cross checked with get
                                step = step + 1;
                                actualresult, details = setParameter(obj, paramName, newlogInt, "int");

                                print "\nTEST STEP %d: Set the TELEMETRY LogInterval to %ss" %(step, newlogInt);
                                print "EXPECTED RESULT %d: Should set the TELEMETRY LogInterval to %ss" %(step, newlogInt);

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: TELEMETRY LogInterval: %s" %(step,details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    print "\nGet the number of log lines \"UP_RetransCount_2\" in /rdklogs/logs/wifihealth.txt";
                                    step = step + 1;
                                    tdkTestObj1 = sysObj.createTestStep('ExecuteCmd');
                                    log = "UP_RetransCount_2";
                                    file = "/rdklogs/logs/wifihealth.txt"
                                    no_of_lines_initial = getLogFileTotalLinesCount(tdkTestObj1, file, log, step);
                                    print "The initial number of log lines \"UP_RetransCount_2\" in wifihealth.txt is : %d" %no_of_lines_initial;

                                    #Sleeping for initial telemetry interval newlogInt + 60 (as the polling of Log Interval happens every 60s)
                                    sleep_time = 60 + int(newlogInt);
                                    print "\nSleeping for duration : %d to check if the logging is happening according to the new log interval set" %sleep_time;
                                    sleep(sleep_time);

                                    print "\nGet the final number of log lines \"UP_RetransCount_2\" in /rdklogs/logs/wifihealth.txt";
                                    step = step + 1;
                                    no_of_lines_final = getLogFileTotalLinesCount(tdkTestObj1, file, log, step);
                                    print "The final number of log lines \"UP_RetransCount_2\" in wifihealth.txt is : %d" %no_of_lines_final;

                                    #Check if the difference between the final and initial number of Markers is >= 1
                                    step = step + 1;
                                    difference = no_of_lines_final - no_of_lines_initial;
                                    print "\nThe UP_RetransCount_2 markers can be >= 1, after accounting for the polling interval and the new log interval set";

                                    print "TEST STEP %d: Should get UP_RetransCount_2 markers count greater than or equal to 1" %step;
                                    print "EXPECTED RESULT %d: The UP_RetransCount_2 markers count should be greater than or equal to 1" %step;

                                    if difference >= 1:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: Number of new UP_RetransCount_2 markers are : %d" %(step, difference);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";

                                        #Check if the marker value of UP_RetransCount_2 >= 0
                                        step = step + 1;
                                        cmd= "cat /rdklogs/logs/wifihealth.txt | grep \"UP_RetransCount_2:\"";
                                        print "\nCommand : ", cmd;
                                        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                                        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                        print "\nTEST STEP %d : Check if the marker value of UP_RetransCount_2 is greater than or equal to 0" %(step);
                                        print "EXPECTED RESULT %d : The marker value of UP_RetransCount_2 should be greater than or equal to 0" %(step);

                                        if expectedresult in actualresult and details != "":
                                            marker_val = details.strip().split("UP_RetransCount_2:")[1].split(",")[0];
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "ACTUAL RESULT %d: The marker value is : %s" %(step, marker_val);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : SUCCESS";

                                            if marker_val.isdigit() and int(marker_val) >= 0:
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "Marker value is valid and greater than or equal to 0";
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "Marker value is NOT valid or NOT greater than or equal to 0";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: The marker value is : %s" %(step, details);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : FAILURE";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: Number of new UP_RetransCount_2 markers are : %d" %(step, difference);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Set operation failed" %(step);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] :FAILURE";

                                #Revert the Log Interval value
                                step = step + 1;
                                actualresult, details = setParameter(obj, paramName, DeflogInt, "int");

                                print "\nTEST STEP %d: Revert the TELEMETRY LogInterval to initial value" %step;
                                print "EXPECTED RESULT %d: Should revert the TELEMETRY LogInterval to initial value" %step;

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Revert of TELEMETRY LogInterval is successful" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Revertion of TELEMETRY LogInterval failed" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TELEMETRY LogInterval not a valid value" %step;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: TELEMETRY LogInterval: %s" %(step,details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to enable Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable, cannot proceed..";

                    #Revert the Associated Devices Errors Received Stats Enable
                    if revert_flag_stats == 1:
                        step = step + 1;
                        paramName = "Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable"
                        actualresult, details = setParameter(obj, paramName, error_stats_initial, "boolean");

                        print "\nTEST STEP %d: Revert Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable to initial value" %step;
                        print "EXPECTED RESULT %d: Should revert the enable state of Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable to initial value" %step;

                        if expectedresult in actualresult and details != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Associated Devices Errors Received Stats Enable is reverted; Details : %s" %(step,details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Associated Devices Errors Received Stats Enable value is NOT reverted; Details : %s" %(step,details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "Revert of Device.WiFi.AccessPoint.2.X_COMCAST-COM_AssociatedDevicesErrorsReceivedStatsEnable not required";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Associated Devices Errors Received Stats Enable is : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable
                if revert_flag_rfc == 1:
                    step = step + 1;
                    paramName = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable"
                    actualresult, details = setParameter(obj, paramName, rfc_initial, "boolean");

                    print "\nTEST STEP %d: Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable to initial value" %step;
                    print "EXPECTED RESULT %d: Should revert the enable state of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable to initial value" %step;

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: RFC Enable is reverted; Details : %s" %(step,details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: RFC Enable value is NOT reverted; Details : %s" %(step,details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Revert of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable not required";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Unable to enable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ErrorsReceived.Enable, cannot proceed..";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Errors Received Enable is : %s" %(step,details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d:wifihealth log file is not present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent")
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
