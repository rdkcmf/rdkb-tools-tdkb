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
  <version>19</version>
  <name>TS_PAM_CheckFirmwareUpgradeStartAndEndTime</name>
  <primitive_test_id/>
  <primitive_test_name>pam_Setparams</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the values Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeStartTime and Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeEndTime are valid integers and matches with the log value obtained from SelfHeal.txt.0 on factory reset.</synopsis>
  <groups_id/>
  <execution_time>35</execution_time>
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
    <test_case_id>TC_PAM_246</test_case_id>
    <test_objective>To check if the values Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeStartTime and Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeEndTime are valid integers and matches with the log value obtained from SelfHeal.txt.0 on factory reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeStartTime
ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeEndTime</input_parameters>
    <automation_approch>1. Load the modules
2. Initiate a factory reset
3. Once the device comes up, query Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeStartTime and Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeEndTime. Check if both are valid integers.
4. Check for the presence of SelfHeal.txt.0 under /rdklogs/logs
5. Check if "Firmware upgrade start time : " and "Firmware upgrade end time : " are populated in SelfHeal.txt.0. Fetch the start and end time log using them
6. Cross check if the start and end time from SelfHeal.txt.0 matches with the TR181 values.
7. Unload the modules</automation_approch>
    <expected_output>The values Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeStartTime and Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeEndTime should be valid integers and should match with the log value obtained from SelfHeal.txt.0 on factory reset.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckFirmwareUpgradeStartAndEndTime</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *;
from time import sleep;

#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_PAM_CheckFirmwareUpgradeStartAndEndTime');
sysobj.configureTestCase(ip,port,'TS_PAM_CheckFirmwareUpgradeStartAndEndTime');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Initiate a device FR
    pamobj.saveCurrentState();
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Initiate a factory reset";
    print "EXPECTED RESULT 1: Factory reset should be initiated successfully";

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Factory reset is initiated successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Restore the device state saved before reboot after a 600s wait time for RFC update
        sleep(600);
        print "Sleeping for 600s";
        pamobj.restorePreviousStateAfterReboot();

        #After the device comes up check the start and end times of firmware upgrade
        paramList = ["Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeStartTime", "Device.DeviceInfo.X_RDKCENTRAL-COM_MaintenanceWindow.FirmwareUpgradeEndTime"];

        actualresult = [];
        orgValue = [];
        status = 0;
        for index in range(len(paramList)):
            tdkTestObj = pamobj.createTestStep("pam_GetParameterValues");
            tdkTestObj.addParameter("ParamName",paramList[index])
            tdkTestObj.executeTestCase(expectedresult);
            actualresult.append(tdkTestObj.getResult())
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if expectedresult in actualresult[index] and details != "":
                orgValue.append(details);
            else :
                status = 1;
                break;

        print "\nTEST STEP 2: Get the Firmware Upgrade Start time and End time; Get the Values of the parameters : ", paramList;
        print "EXPECTED RESULT 2: The Firmware Upgrade Start time and End time should be obtained successfully";

        if status == 0 :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2 : The values of the parameters are : %s - %s and %s - %s" %(paramList[0], orgValue[0], paramList[1], orgValue[1]);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if orgValue[0].isdigit() and orgValue[1].isdigit() :
                tdkTestObj.setResultStatus("SUCCESS");
                print "\nThe Firmware Upgrade Start time and End time are valid numerical values";

                #Check for the presense of SelfHeal.txt.0
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "[ -f /rdklogs/logs/SelfHeal.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
                tdkTestObj.addParameter("command",cmd);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP 3: Check for SelfHeal.txt.0 file presence";
                print "EXPECTED RESULT 3: SelfHeal.txt.0 should be present";

                if details == "File exist" :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3 : SelfHeal.txt.0  is present";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the "Firmware upgrade start time : " and "Firmware upgrade end time : " logs are found in SelfHeal.txt.0 are present in SelfHeal
                    step = 3;
                    search_strings = ["Firmware upgrade start time : ", "Firmware upgrade end time : "];
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');

                    for iteration in range(0,2):
                        step = step + 1;
                        stringfound = 0;
                        cmd = "grep -ire \"" + search_strings[iteration] +  "\" /rdklogs/logs/SelfHeal.txt.0";
                        tdkTestObj.addParameter("command",cmd);

                        print "\nTEST STEP %d: Check if the log line \"%s\" is present in SelfHeal.txt.0" %(step, search_strings[iteration]);
                        print "EXPECTED RESULT %d: The required log line should be present in SelfHeal.txt.0" %step;

                        #Checking every 60s for 10 mins
                        for sub_iteration in range(1,11):
                            print "Waiting for the string to get populated in SelfHeal.txt.0....\nIteration : %d" %sub_iteration;
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                            if expectedresult in actualresult and search_strings[iteration] in details:
                                stringfound = 1;
                                break;
                            else:
                                sleep(60);
                                continue;

                        if stringfound == 1:
                            details = details.split(search_strings[iteration])[1];
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Required log line is present, Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Cross check the value obtained from SelfHeal.txt.0 with the TR181 parameter value
                            step = step + 1;
                            print "\nTEST STEP %d : Cross check the value of %s with the value from SelfHeal.txt.0" %(step, paramList[iteration]);
                            print "EXPECTED RESULT %d : Both the values should match" %(step);
                            print "%s : %s" %(paramList[iteration], orgValue[iteration]);
                            print "%s %s" %(search_strings[iteration], details);

                            if orgValue[iteration] == details :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: The values match" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: The values DO NOT match" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Required log line is not present, Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3 : SelfHeal.txt.0 is NOT present";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "\nThe Firmware Upgrade Start time and End time are NOT valid numerical values";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Get operation failed : ", orgValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Details : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
