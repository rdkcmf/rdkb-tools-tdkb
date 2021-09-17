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
  <version>1</version>
  <name>TS_SANITY_NonEmpty_WiFiVendorLogFile</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify logging is happening for wifi vendor log file</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_SYSUTIL_57</test_case_id>
    <test_objective>To verify logging is happening for wifi vendor log file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Execute_Cmd</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module .
2.Check if wifi_vendor.log file is present
3.Get the current no of lines and perform set operation to simulate logs
4.Check if the current no of lines is greater then lines before simulation
5.Revert the set value
6.Unload the module</automation_approch>
    <expected_output>wifi_vendor.log file should not be empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_NonEmpty_WiFiVendorLogFile</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
from tdkbVariables import *;
from  tdkbTelemetry2_0Utility import *;
from time import sleep;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
tr181obj= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_NonEmpty_WiFiVendorLogFile');
tr181obj.configureTestCase(ip,port,'TS_SANITY_NonEmpty_WiFiVendorLogFile');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
tr181loadmodulestatus=tr181obj.getLoadModuleResult();

def getSSIDEnable(tdkTestObj,param_name):
    tdkTestObj.addParameter("ParamName",param_name);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details  = tdkTestObj.getResultDetails();
    return actualresult,details,tdkTestObj;

def setSSIDEnable(tdkTestObj,param_name,param_value):
    tdkTestObj.addParameter("ParamName",param_name);
    tdkTestObj.addParameter("ParamValue",param_value);
    tdkTestObj.addParameter("Type","boolean");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details,tdkTestObj;

if "SUCCESS" in (sysutilloadmodulestatus.upper() and tr181loadmodulestatus.upper()):
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_set = tr181obj .createTestStep('TDKB_TR181Stub_Set');

    #Check whether the file is present or not
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/wifi_vendor.log  ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check for existence of wifi_vendor.log ";
        print "EXPECTED RESULT 1: wifi_vendor.log  file should be present";
        print "ACTUAL RESULT 1:wifi_vendor.log  file is present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        cmd = "cat /rdklogs/logs/wifi_vendor.log | wc -l";
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        linecount = int(details);
        if expectedresult in actualresult:
            print "Initial Line count of  Log File is ",linecount
            disabled = 0;
            ssid1_res, ssid1_enable, tdkTestObj = getSSIDEnable(tdkTestObj_Tr181_Get,"Device.WiFi.SSID.1.Enable");
            if expectedresult in ssid1_res:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the SSID Enable status of SSID1";
                print "EXPECTED RESULT 2: Should get the SSID Enable status";
                print "ACTUAL RESULT 2: SSID Enable status Retrieved Successfully ";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                ssid_RevertFlag = 0;
                set_result1,set_details1, tdkTestObj = setSSIDEnable(tdkTestObj_Tr181_set,"Device.WiFi.SSID.1.Enable","false");
                if expectedresult in set_result1:
                    ssid_RevertFlag = 1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Set the SSID Enable Status to False";
                    print "EXPECTED RESULT 3: Should Set the SSID Enable to False";
                    print "ACTUAL RESULT 3: SSID Enable status Set was Successful ";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    sleep(30);
                    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                    cmd = "cat /rdklogs/logs/wifi_vendor.log | wc -l";
                    expectedresult="SUCCESS";
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    lineCountAfterSimu = int(details);
                    if expectedresult in actualresult and  int(lineCountAfterSimu) > int(linecount):
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Get the line count of wifi vendor log file and compare the value with linecount";
                        print "EXPECTED RESULT 4: Line count After Simulation should be greater than the linecount";
                        print "ACTUAL RESULT 4: Line count After Simulation is greater than the linecount";
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Get the line count of wifi vendor log file and compare the value with linecount";
                        print "EXPECTED RESULT 4: Line count After Simulation should be greater than the linecount";
                        print "ACTUAL RESULT 4: Line count After Simulation is not greater than the linecount";
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Set the SSID Enable Status to False";
                    print "EXPECTED RESULT 3: Should Set the SSID Enable to False";
                    print "ACTUAL RESULT 3: SSID Enable status Set was Failed ";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                if ssid_RevertFlag == 1:
                    set_result1,set_details1, tdkTestObj = setSSIDEnable(tdkTestObj_Tr181_set,"Device.WiFi.SSID.1.Enable",ssid1_enable);
                    if expectedresult in set_result1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Revert the SSID Enable";
                        print "EXPECTED RESULT 5: Should Revert the SSID Enable to original value";
                        print "ACTUAL RESULT 5: Revert operation was Successful ";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Revert the SSID Enable";
                        print "EXPECTED RESULT 5: Should Revert the SSID Enable to original value";
                        print "ACTUAL RESULT 5: Revert operation was Failed ";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "SSID Revert Flag was not SET, No need to set the SSID Enable status"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Get the SSID Enable status of SSID1";
                print "EXPECTED RESULT 2: Should get the SSID Enable status";
                print "ACTUAL RESULT 2: Failed to get SSID Enable Status ";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the initial Line count of Telemetry Log file";
            print "EXPECTED RESULT 2: Should get the initial line count of Telemetry Log file";
            print "ACTUAL RESULT 2: Failed to get the Line count";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 1: Check for existence of wifi_vendor.log ";
         print "EXPECTED RESULT 1: wifi_vendor.log  file should be present";
         print "ACTUAL RESULT 1:wifi_vendor.log  file is not present";
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";
    sysObj.unloadModule("sysutil");
    tr181obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     sysObj.setLoadModuleStatus("FAILURE");
     tr181obj.setLoadModuleStatus("FAILURE");
