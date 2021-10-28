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
  <version>13</version>
  <name>TS_SANITY_CheckLogLocation_PreserveLogsON</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the tar ball of Bootup Logs is moved to preserveLogs folder when        Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold is set to the default value 3 and
Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync is set to True by checking for the string "preserve this log for further analysis" in Consolelog.txt.0</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_SANITY_61</test_case_id>
    <test_objective>To check if the tar ball of Bootup Logs is moved to preserveLogs folder when        Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold is set to the default value 3 and
Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync is set to True by checking for the string "preserve this log for further analysis" in Consolelog.txt.0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold
Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync
</input_parameters>
    <automation_approch>1. Load the modules.
2. Get the values of Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold and Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync.
3. Set the values to 3 and true respectively and validate the Set operation with a Get.
4. Reboot the device
5. Once the device comes up, as the Preserve Logs RFC parameters are enabled, the tar ball of the bootup logs should come under preserveLogs folder in nvram2. This can be validated by checking if the string "preserve this log for further analysis" under Consolelog.txt.0.
6. Unload the modules.</automation_approch>
    <expected_output>The  log message "preserve this log for further analysis" should be present under Consolelog.txt.0 on Bootup of the device when Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold is set to the default value 3 and
Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync is set to True and rebooted.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckLogLocation_PreserveLogsON</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def checkLogs(obj2, step):
    #Check if the string "preserve this log for further analysis" is present in Consolelog.txt.0
    status = 1;
    string_to_check = "preserve this log for further analysis";
    tdkTestObj = obj2.createTestStep('ExecuteCmd');
    cmd = "grep -ire \"" + string_to_check + "\" /rdklogs/logs/Consolelog.txt.0";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for the presence of the string \"%s\"" %(step, string_to_check);
    print "EXPECTED RESULT %d: The string should be present in Consolelog.txt.0" %step;

    if string_to_check in details :
        status = 0;
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Required string is found; Details : %s" %(step,details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Required string is not found; Details : %s" %(step,details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2 = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckLogLocation_PreserveLogsON');
obj1.configureTestCase(ip,port,'TS_SANITY_CheckLogLocation_PreserveLogsON');
obj2.configureTestCase(ip,port,'TS_SANITY_CheckLogLocation_PreserveLogsON');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =obj2.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    tdkTestObj = obj.createTestStep('TADstub_Get');
    paramList=["Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold", "Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync"]
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)

    print "\nTEST STEP 1: Get the values of Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold and Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync";
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold is : %s and Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync is : %s" %(orgValue[0],orgValue[1]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        set_threshold = "3";
        set_sync = "true";
        #Check the GET values, if they match reboot the device directly else SET the values and reboot
        if orgValue[0] == "3" and orgValue[1] == "true":
            print "\nSet operation for Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold and Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync is not required";
            print "****DUT is going for a reboot and will be up after 360 seconds*****";
            obj.initiateReboot();
            sleep(360);

            #Check if the required logs are present in the Consolelog.txt.0
            step = 2;
            status = checkLogs(obj2, step);
            if status == 0:
                print "The required logs are present under Consolelog.txt.0"
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "The required logs are not present under Consolelog.txt.0"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList", "Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold|%s|unsignedint|Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync|%s|boolean"%(set_threshold,set_sync));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 2 : Set Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold to %s and Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync to %s" %(set_threshold,set_sync);
            print "EXPECTED RESULT 2 : SET operations should be success";

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Set operation success; Details : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";

                #Validate the SET with GET
                tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)

                print "\nTEST STEP 3: Get the values of Device.SelfHeal.X_RDKCENTRAL-COM_LogBackupThreshold and Device.SelfHeal.X_RDKCENTRAL-COM_NoWaitLogSync";
                print "EXPECTED RESULT 3: The values should be retrieved successfully and should be the same as set values";

                if expectedresult in status and setValue[0] == set_threshold and setValue[1] == set_sync :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Values after the GET are same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    print "\n****DUT is going for a reboot and will be up after 360 seconds*****";
                    obj.initiateReboot();
                    sleep(360);

                    #Check if the required logs are present under Consolelog.txt.0
                    step = 4;
                    status = checkLogs(obj2, step);
                    if status == 0:
                        print "The required logs are present under Consolelog.txt.0"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "The required logs are not present under Consolelog.txt.0"
                        tdkTestObj.setResultStatus("FAILURE");
                    print "Revert operation is not required as Preserve Logs parameters are RFC";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Values after the GET are not same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:Set operation failed; Details : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: GET operation failed; Details : %s" %details;
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

