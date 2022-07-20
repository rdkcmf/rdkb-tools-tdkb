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
  <name>TS_WIFIAGENT_CheckACSDLogging_WithRadiosDisabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the log "Radio's disabled, Skipping ACSD check" is populated under /rdklogs/logs/SelfHeal.txt.0 when both the radios Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable are disabled.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_210</test_case_id>
    <test_objective>Check if the log "Radio's disabled, Skipping ACSD check" is populated under /rdklogs/logs/SelfHeal.txt.0 when both the radios Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable are disabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.Radio.1.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.Radio.2.Enable
paramValue : true/false
paramType : boolean</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial radio enable status using Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable.
3. Disable both radios if not already disabled. Validate with GET operation.
4. Check if SelfHeal.txt.0  is found under /rdklogs/logs
5. Check if the log "Radio's disabled, Skipping ACSD check" is logged in SelfHeal.txt.0 within a duration of 15mins (during task health monitor script runs).
6. Revert the radio enable statuses to initial values if required.
7. Unload the modules</automation_approch>
    <expected_output>The log "Radio's disabled, Skipping ACSD check" should be populated under /rdklogs/logs/SelfHeal.txt.0 when both the radios Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable are disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckACSDLogging_WithRadiosDisabled</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getParam(wifiobj, paramName):
    expectedresult = "SUCCESS";
    value = "";
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName",paramName);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details != "":
        value = details.split("VALUE:")[1].split(" ")[0].strip();
        print "%s : %s" %(paramName, value);
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "%s is not retrieved successfully" %paramName;
        tdkTestObj.setResultStatus("FAILURE");
    return actualresult, tdkTestObj, value;

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
    return status, tdkTestObj;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *;
from time import sleep;

#Test component to be tested
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckACSDLogging_WithRadiosDisabled');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckACSDLogging_WithRadiosDisabled');

#Get the result of connection with test component and DUT
wifiloadmodulestatus=wifiobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in wifiloadmodulestatus.upper():
    #Set the result status of execution
    wifiobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Get the radio enabled status for 2.4G and 5G
    paramList = ["Device.WiFi.Radio.1.Enable", "Device.WiFi.Radio.2.Enable"];
    radio_enable_initial = [0, 0];

    print "\nTEST STEP 1 : Get the initial values of ", paramList;
    print "EXPECTED RESULT 1 : The Radio enable values should be retrieved successfully";
    actualresult1, tdkTestObj, radio_enable_initial[0] = getParam(wifiobj, paramList[0]);
    actualresult2, tdkTestObj, radio_enable_initial[1] = getParam(wifiobj, paramList[1]);

    if actualresult1 in expectedresult and  actualresult2 in expectedresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: The radio enable values are retrieved successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Disable the radio enable if not already in disabled state
        radio_disabled = [0, 0];
        print "\nTEST STEP 2 : Disable the radios if not already in disabled state";
        print "EXPECTED RESULT 2 : The Radios should be disabled successfully";

        for index in range(0,2):
            if radio_enable_initial[index] != "false":
                status, tdkTestObj = setParameter(wifiobj, paramList[index], "false", "boolean");
                if status == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s disabled successfully" %paramList[index];
                else:
                    radio_disabled[index] = 1;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "%s NOT disabled successfully" %paramList[index];
            else:
                print "%s is already in disabled state...SET not required" %paramList[index];

        if radio_disabled[0] == 0 and radio_disabled[1] == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: The radios are disabled successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if SelfHeal.txt.0 is present under /rdklogs/logs
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "[ -f /rdklogs/logs/SelfHeal.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
            tdkTestObj.addParameter("command",cmd);
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

                #Check if the log "Radio's disabled, Skipping ACSD check" is present in SelfHeal.txt.0 logs
                #As the task health monitor script runs once in every 15mins, check for the logs with a gap of 60s for a 15mins duration
                string_found = 0;
                print "\nTEST STEP 4 : Check if the log \"Radio's disabled, Skipping ACSD check\" is found in SelfHeal.txt.0";
                print "EXPECTED RESULT 4 : The log \"Radio's disabled, Skipping ACSD check\" should be found in SelfHeal.txt.0"

                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "cat /rdklogs/logs/SelfHeal.txt.0 | grep -i \"Radio's disabled, Skipping ACSD check\"";
                tdkTestObj.addParameter("command",cmd);

                for iteration in range(1, 16):
                    print "Iteration %d..." %iteration;
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and details != "":
                        string_found = 1;
                        break;
                    else:
                        sleep(60);
                        continue;

                if string_found == 1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4 : Log Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4 : Required log not found";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3 : SelfHeal.txt.0  is NOT present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: The radios are NOT disabled successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Revert operation
        radio_revert = [0, 0];
        print "\nTEST STEP 5 : Revert the radio enable statuses if required";
        print "EXPECTED RESULT 5 : Radio enable statuses should be reverted if required";

        for index in range(0,2):
            if radio_enable_initial[index] != "false":
                status, tdkTestObj = setParameter(wifiobj, paramList[index], "true", "boolean");
                if status == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "%s reverted successfully" %paramList[index];
                else:
                    radio_revert[index] = 1;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "%s NOT reverted successfully" %paramList[index];
            else:
                print "%s revert not required" %paramList[index];

        if radio_revert[0] == 0 and radio_revert[1] == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 5: The radios are reverted successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 5: The radios are NOT reverted successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: The radio enable values are NOT retrived successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    wifiobj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    wifiobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
