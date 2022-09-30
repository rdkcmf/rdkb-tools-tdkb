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
  <version>3</version>
  <name>TS_WIFIAGENT_CheckStatusAndLogging_WithRadioDisabledAndSSIDEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if disabling the Radios Device.WiFi.Radio.1.Enable, Device.WiFi.Radio.2.Enable and enabling the SSIDs Device.WiFi.SSID.1.Enable, Device.WiFi.SSID.2.Enable updates the status parameters of Radios and SSIDs as "Down" and the expected logs "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state" and "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state", "Both 2G Radio(Radio 1) and 2G Private SSID are in DOWN state" are populated in SelfHeal.txt.0 within 15mins.</synopsis>
  <groups_id/>
  <execution_time>40</execution_time>
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
    <test_case_id>TC_WIFIAGENT_216</test_case_id>
    <test_objective>To check if disabling the Radios Device.WiFi.Radio.1.Enable, Device.WiFi.Radio.2.Enable and enabling the SSIDs Device.WiFi.SSID.1.Enable, Device.WiFi.SSID.2.Enable updates the status parameters of Radios and SSIDs as "Down" and the expected logs "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state" and "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state", "Both 2G Radio(Radio 1) and 2G Private SSID are in DOWN state" are populated in SelfHeal.txt.0 within 15mins.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.Radio.1.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.Radio.2.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.SSID.1.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.SSID.2.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.Radio.1.Status
paramName : Device.WiFi.Radio.2.Status
paramName : Device.WiFi.SSID.1.Status
paramName : Device.WiFi.SSID.2.Status</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial enable states of Radios Device.WiFi.Radio.1.Enable, Device.WiFi.Radio.2.Enable and SSIDs Device.WiFi.SSID.1.Enable, Device.WiFi.SSID.2.Enable and store them.
3. As pre-requisite enable all radios and SSIDs if not already enabled. Validate the SET with corresponding GET.
4. Disable the radios and validate with GET.
5. Sleep for 20s
6. Check the status of Radios and SSIDs using Device.WiFi.Radio.1.Status, Device.WiFi.Radio.2.Status, Device.WiFi.SSID.1.Status and Device.WiFi.SSID.2.Status.
7. The status of all the above parameters should be "Down".
8. Check if SelfHeal.txt.0 is present under /rdklogs/logs/.
9. Within a 15min duration comprising of 60s iterations, check if the logs "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state" and "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state", "Both 2G Radio(Radio 1) and 2G Private SSID are in DOWN state" are populated in SelfHeal.txt.0 within 15mins.
10. Enable the Radios and then check if revert operations for SSIDs are required. If so, revert the SSIDs and validate with GET.
11. Finally revert the radios if required.
12. Unload the modules.</automation_approch>
    <expected_output>After disabling Device.WiFi.Radio.1.Enable, Device.WiFi.Radio.2.Enable and enabling the SSIDs Device.WiFi.SSID.1.Enable, Device.WiFi.SSID.2.Enable the status parameters of Radios and SSIDs should be updated to "Down" and the expected logs "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state", "Both 2G Radio(Radio 1) and 2G Private SSID are in DOWN state" should be  populated in SelfHeal.txt.0 within 15mins.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckStatusAndLogging_WithRadioDisabledAndSSIDEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

def getValues(obj, paramList):
    Values = [];
    status = 0;
    expectedresult = "SUCCESS";

    for param in paramList:
        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName",param)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        if expectedresult in actualresult and details != "":
            enable = details.split("VALUE:")[1].split(" ")[0].strip();
            Values.append(enable);
            print "\n%s : %s" %(param, enable);

            if enable != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                continue;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                status = 1;
                break;
        else :
            status = 1;
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "%s : %s" %(param, details);
            break;
    return tdkTestObj, status, Values;

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

    if expectedresult not in actualresult:
        status = 1;
        print "%s SET operation failed" %param;
    return status;

def preRequisite(obj, paramList, values):
    retVal = 0;
    revertFlag = [0, 0, 0, 0];
    #Check if Radios and SSIDs are enabled
    for index in range(0, 4) :
        if values[index] == "false":
            status = setParameter(obj, paramList[index], "true", "boolean");

            if status == 0:
                revertFlag[index] = 1;
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "%s is set to enabled successfully" %paramList[index];
            else:
                retVal = 1;
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "%s is NOT set to enabled successfully" %paramList[index];
                break;
        else:
            print "%s is enabled initially, set operation not required" %paramList[index];
    return retVal, revertFlag;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from random import randint;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckStatusAndLogging_WithRadioDisabledAndSSIDEnabled');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckStatusAndLogging_WithRadioDisabledAndSSIDEnabled');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Get the initial Radio and SSID enable values
    paramList = ["Device.WiFi.Radio.1.Enable", "Device.WiFi.Radio.2.Enable", "Device.WiFi.SSID.1.Enable", "Device.WiFi.SSID.2.Enable"];
    print "\nTEST STEP 1: Get the initial Radios and SSID enable state - ", paramList;
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    tdkTestObj, status, initial_values = getValues(obj, paramList);

    if status == 0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: The values retrieved are respectively : %s, %s, %s, %s" %(initial_values[0], initial_values[1], initial_values[2], initial_values[3]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if the pre-requisites are set else set them
        print "\n**********Pre-Requisites Start**********";
        print "\nTEST STEP 2 : Check if the Radios and SSIDs are enabled initially else enable them as pre-requisites";
        print "EXPECTED RESULT 2 : Radios and SSIDs should be enabled as pre-requisites";

        preReq = 0;
        #Check if Radios and SSIDs are enabled
        for index in range(0, 4) :
            if initial_values[index] == "false":
                preReq = setParameter(obj, paramList[index], "true", "boolean");
                if preReq == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s is set to enabled successfully" %paramList[index];
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "%s is NOT set to enabled successfully" %paramList[index];
                    break;
            else:
                print "%s is enabled initially, set operation not required" %paramList[index];

        if preReq == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Radios and SSIDs are enabled as pre-requisite";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "\n**********Pre-Requistes Complete**********"

            #Disable the radios
            paramList_radio = ["Device.WiFi.Radio.1.Enable", "Device.WiFi.Radio.2.Enable"];
            setvalues = ["false", "false"];
            print "\nTEST STEP 3: Set the Radio enable parameters to disabled values - ", paramList_radio;
            print "EXPECTED RESULT 3 : The Radio enable parameters should be set to disabled successfully";

            for index in range(0, 2):
                status = setParameter(obj, paramList_radio[index], "false", "boolean");
                if status == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s is set successfully to %s" %(paramList_radio[index], setvalues[index]);
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "%s is NOT set successfully to %s" %(paramList_radio[index], setvalues[index]);
                    break;

            if status == 0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Radios are disabled successfully keeping the SSIDs enabled" ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the Radio and SSID statuses after a 20s sleep time for changes to reflect
                sleep(20);
                paramList_status = ["Device.WiFi.Radio.1.Status", "Device.WiFi.Radio.2.Status", "Device.WiFi.SSID.1.Status", "Device.WiFi.SSID.2.Status"];

                print "\nTEST STEP 4: Get the current Radio and SSID status - ", paramList_status;
                print "EXPECTED RESULT 4 : The values should be retrieved successfully";
                tdkTestObj, status, values = getValues(obj, paramList_status);

                if status == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: The values retrieved are respectively : %s, %s, %s, %s" %(values[0], values[1], values[2], values[3]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the Radio statuses and SSID statuses are Down
                    print "\nTEST STEP 5: Check if the Radio and SSID statuses are Down";
                    print "EXPECTED RESULT 5 : The Radio statuses and SSID statuses should be Down";

                    if values[0] == "Down" and values[1] == "Down" and values[2] == "Down" and values[3] == "Down":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5 : The Radio and SSID statuses are as expected";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check for the presense of SelfHeal.txt.0
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        cmd = "[ -f /rdklogs/logs/SelfHeal.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                        print "\nTEST STEP 6: Check for SelfHeal.txt.0 file presence";
                        print "EXPECTED RESULT 6: SelfHeal.txt.0 should be present";

                        if details == "File exist" :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6 : SelfHeal.txt.0 is present";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Check if the "Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state" and "Both 2G Radio(Radio 1) and 2G Private SSID are in DOWN state" logs are found in SelfHeal.txt.0
                            step = 6;
                            search_strings = ["Both 5G Radio(Radio 2) and 5G Private SSID are in DOWN state", "Both 2G Radio(Radio 1) and 2G Private SSID are in DOWN state"];
                            tdkTestObj = sysobj.createTestStep('ExecuteCmd');

                            for iteration in range(0,2):
                                stringfound = 0;
                                step = step + 1;
                                cmd = "grep -ire \"" + search_strings[iteration] +  "\" /rdklogs/logs/SelfHeal.txt.0";
                                tdkTestObj.addParameter("command",cmd);

                                print "\nTEST STEP %d: Check if the log line \"%s\" is present in SelfHeal.txt.0" %(step, search_strings[iteration]);
                                print "EXPECTED RESULT %d: The required log line should be present in SelfHeal.txt.0" %step;

                                #Checking every 60s for 15 mins
                                for sub_iteration in range(1,17):
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
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Required log line is present, Details : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Required log line is NOT present, Details : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6 : SelfHeal.txt.0 is not present";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5 : The Radio and SSID statuses are NOT as expected";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: The values are NOT retrieved successfully" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Enable the radios before reverting the SSID enable
                status = 0;
                print "\nTEST STEP 9 : Enable the radios before reverting the SSID enable";
                print "EXPECTED RESULT 9 : Enabling radios should be success";

                for index in range(0, 2):
                    setvalue = "true";
                    status = setParameter(obj, paramList[index], setvalue, "boolean");
                    if status == 0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "%s is set successfully to %s" %(paramList[index], setvalue);
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "%s is NOT set successfully to %s" %(paramList[index], setvalue);
                        break;

                if status == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 9: Radios enabled successfully" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Revert the SSID enable if required
                    status = 0;
                    print "\nTEST STEP 10 : Revert the SSID Enable if required";
                    print "EXPECTED RESULT 10 : Revert operation should be success wherever required";

                    for index in range(2, 4):
                        if initial_values[index] != "true":
                            status = setParameter(obj, paramList[index], initial_values[index], "boolean");
                            if status == 0:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "%s is reverted successfully to %s" %(paramList[index], initial_values[index]);
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "%s is NOT reverted successfully to %s" %(paramList[index], initial_values[index]);
                                break;
                        else:
                            print "%s revert operation is not required" %paramList[index];

                    if status == 0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 10: SSID enable revert operations completed" ;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 10: SSID enable revert operations NOT completed" ;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 9: Radios NOT enabled successfully" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: SSIDs are NOT disabled successfully keeping the radios enabled" ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert the Radio enable states if required
            status = 0;
            print "\nTEST STEP 11 : Revert the Radio Enable if required";
            print "EXPECTED RESULT 11 : Revert operation should be success wherever required";

            for index in range(0, 2):
                if initial_values[index] != "true":
                    status = setParameter(obj, paramList[index], initial_values[index], "boolean");
                    if status == 0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "%s is reverted successfully to %s" %(paramList[index], initial_values[index]);
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "%s is NOT reverted successfully to %s" %(paramList[index], initial_values[index]);
                        break;
                else:
                    print "%s revert operation is not required" %paramList[index];

            if status == 0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 11: Radio enable revert operations completed" ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 11: Radio enable revert operations NOT completed" ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Radios and SSIDs are NOT enabled as pre-requisite";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: The values are NOT retrieved successfully" ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
