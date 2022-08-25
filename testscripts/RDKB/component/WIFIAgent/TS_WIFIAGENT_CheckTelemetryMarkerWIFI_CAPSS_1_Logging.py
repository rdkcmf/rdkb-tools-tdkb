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
  <version>5</version>
  <name>TS_WIFIAGENT_CheckTelemetryMarkerWIFI_CAPSS_1_Logging</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Client capability spatial streams parameter Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr returns a valid value in the range (0, 8] and the telemetry marker "WIFI_CAPSS_1" is populated in wifihealth.txt within the logging interval with valid marker value when a 2.4G client is connected to the DUT.</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_WIFIAGENT_211</test_case_id>
    <test_objective>To check if the Client capability spatial streams parameter Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr returns a valid value in the range (0, 8] and the telemetry marker "WIFI_CAPSS_1" is populated in wifihealth.txt within the logging interval with valid marker value when a 2.4G client is connected to the DUT.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Connect a wifi client to 2.4G radio private access point</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr
paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
paramValue : logging interval
paramType : int</input_parameters>
    <automation_approch>1. Load the modules
2. Check if wifihealth.txt is present under /rdklogs/logs/
3. Retrieve the client capability spatial streams using Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr.
4. Check if the value retrieved is in the range (0, 8].
5. Get the value of telemetry log interval using Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval.
6. Set to a new value (300 or 360s) if the initial log interval is different and validate the set with get.
7. Get the initial count of "WIFI_CAPSS_1" markers in wifihealth.txt.
8. Sleep for a duration set by Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval + 60s (polling interval of log interval)
9. After the sleep time, get the final count of the marker "WIFI_CAPSS_1"
10. Compute the difference between the number of markers before and after the sleep duration and check if it is greater than or equal to 1.
11. Check if the marker value has two components of the form &lt;client capability/number of spatial streams&gt;.
12. Check if both the client capability and spatial streams value in the marker is greater than 0.
13. Then check if the client spatial stream component of the marker is equal to TR181 value retrieved using Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr.
14. Also, the number of spatial streams component of the marker should have a value less than the client capability.
15. Revert Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval to initial value.
16. Unload the modules.</automation_approch>
    <expected_output>Client capability spatial streams parameter Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr should return a valid value in the range (0, 8] and the telemetry marker "WIFI_CAPSS_1" should be populated in wifihealth.txt within the logging interval with valid marker value when a 2.4G client is connected to the DUT.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerWIFI_CAPSS_1_Logging</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerWIFI_CAPSS_1_Logging');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerWIFI_CAPSS_1_Logging');

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

        #Get the value of the spatial streams client capability Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr
        step = step + 1;
        paramName = "Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr";
        actualresult, details = getParameter(obj, paramName);

        print "\nTEST STEP %d: Get the spatial streams client capability using Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr" %step;
        print "EXPECTED RESULT %d: Should get the spatial streams client capability using Device.WiFi.AccessPoint.1.AssociatedDevice.1.X_RDK_CapSpaStr" %step;

        if expectedresult in actualresult and details != "":
            capss = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Client Capbility Spatial Streams : %s" %(step, capss);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if capss.isdigit() and int(capss) > 0 and int(capss) <= 8:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Client Capability Spatial Streams value is a valid value greater than 0 and less than or equal to 8";

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

                            print "\nGet the number of log lines \"WIFI_CAPSS_1\" in /rdklogs/logs/wifihealth.txt";
                            step = step + 1;
                            tdkTestObj1 = sysObj.createTestStep('ExecuteCmd');
                            log = "WIFI_CAPSS_1";
                            file = "/rdklogs/logs/wifihealth.txt"
                            no_of_lines_initial = getLogFileTotalLinesCount(tdkTestObj1, file, log, step);
                            print "The initial number of log lines \"WIFI_CAPSS_1\" in wifihealth.txt is : %d" %no_of_lines_initial;

                            #Sleeping for initial telemetry interval newlogInt + 60 (as the polling of Log Interval happens every 60s)
                            sleep_time = 60 + int(newlogInt);
                            print "\nSleeping for duration : %d to check if the logging is happening according to the new log interval set" %sleep_time;
                            sleep(sleep_time);
                            print "\nGet the final number of log lines \"WIFI_CAPSS_1\" in /rdklogs/logs/wifihealth.txt";
                            step = step + 1;
                            no_of_lines_final = getLogFileTotalLinesCount(tdkTestObj1, file, log, step);
                            print "The final number of log lines \"WIFI_CAPSS_1\" in wifihealth.txt is : %d" %no_of_lines_final;

                            #Check if the difference between the final and initial number of Markers is >= 1
                            step = step + 1;
                            difference = no_of_lines_final - no_of_lines_initial;
                            print "\nThe WIFI_CAPSS_1 markers can be >= 1, after accounting for the polling interval and the new log interval set";
                            print "TEST STEP %d: Should get WIFI_CAPSS_1 markers count greater than or equal to 1" %step;
                            print "EXPECTED RESULT %d: The WIFI_CAPSS_1 markers count should be greater than or equal to 1" %step;

                            if difference >= 1:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Number of new WIFI_CAPSS_1 markers are : %d" %(step, difference);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Check if the marker value of WIFI_CAPSS_1 is valid and is of the form <client capability/number of spatial streams>
                                step = step + 1;
                                cmd= "cat /rdklogs/logs/wifihealth.txt | grep \"WIFI_CAPSS_1:\"";
                                print "\nCommand : ", cmd;
                                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                                actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                print "\nTEST STEP %d : Check if the marker value of WIFI_CAPSS_1 is valid" %(step);
                                print "EXPECTED RESULT %d : The marker value of WIFI_CAPSS_1 should be valid" %(step);

                                if expectedresult in actualresult and details != "":
                                    marker_val = details.strip().split("WIFI_CAPSS_1:")[1].split(",")[0];
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: The marker value is : %s" %(step, marker_val);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    client_cap = marker_val.split("/")[0];
                                    spatial_str = marker_val.split("/")[1];
                                    print "Client capability : %s" %client_cap;
                                    print "Number of spatial streams : %s" %spatial_str;

                                    if client_cap.isdigit() and spatial_str.isdigit() and int(client_cap) > 0 and int(spatial_str) > 0:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "The marker values are valid";

                                        #Check if the client capability and spatial streams values are valid
                                        flag = 0;
                                        step = step + 1;
                                        print "\nTEST STEP %d : Check if the client capability from the marker is same as the TR181 value and the number of spatial streams supported is less than or equal to the client capability" %step;
                                        print "EXPECTED RESULT %d : The client capability from the marker should be the same as the TR181 value and the number of spatial streams supported should be less than or equal to the client capability" %step;

                                        if int(client_cap) == int(capss):
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "The client capability marker value : %s is same as the TR181 value : %s" %(client_cap, capss);

                                            if int(spatial_str) <= int(client_cap):
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "The number of spatial streams supported : %s is less than or equal to the client capability : %s" %(spatial_str, client_cap);
                                            else:
                                                flag = 1;
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "The number of spatial streams supported : %s is NOT less than or equal to the client capability : %s" %(spatial_str, client_cap);
                                        else:
                                            flag = 1;
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "The client capability marker value : %s is NOT same as the TR181 value : %s" %(client_cap, capss);

                                        if flag == 0:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "ACTUAL RESULT %d: The client capability or spatial streams value is as expected" %step;
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : SUCCESS";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: The client capability or spatial streams value is NOT as expected" %step;
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : FAILURE";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "The marker values are NOT valid";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: The marker value is : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Number of new WIFI_CAPSS_1 markers are : %d" %(step, difference);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

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
                            print "ACTUAL RESULT %d: Set operation failed" %(step);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] :FAILURE";

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
                print "Client Capability Spatial Streams value is NOT a valid value greater than 0 and less than or equal to 8";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Client Capbility Spatial Streams : %s" %(step, details);
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
