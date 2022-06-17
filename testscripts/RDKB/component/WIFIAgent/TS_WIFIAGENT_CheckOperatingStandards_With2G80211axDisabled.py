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
  <name>TS_WIFIAGENT_CheckOperatingStandards_With2G80211axDisabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the operating standards retrieved using Device.WiFi.Radio.1.OperatingStandards is "g,n" when the parameter Device.WiFi.2G80211axEnable is in disabled state.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIAGENT_190</test_case_id>
    <test_objective>Check if the operating standards retrieved using Device.WiFi.Radio.1.OperatingStandards is "g,n" when the parameter Device.WiFi.2G80211axEnable is in disabled state.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.2G80211axEnable
paramName : Device.WiFi.Radio.1.OperatingStandards</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial enable status of Device.WiFi.2G80211axEnable
3. If it not initially false, set to false and cross check with GET
4. Get the operating standards using Device.WiFi.Radio.1.OperatingStandards. When the 2G80211axEnable is in disabled state, the operating standards should be "g,n"
5. Revert Device.WiFi.2G80211axEnable to initial value if required.
6. Unload the module.</automation_approch>
    <expected_output>The operating standards retrieved using Device.WiFi.Radio.1.OperatingStandards should be "g,n" when the parameter Device.WiFi.2G80211axEnable is in disabled state.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckOperatingStandards_With2G80211axDisabled</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckOperatingStandards_With2G80211axDisabled');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the initial 2G80211axEnable Enable Status
    step = 1;
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.2G80211axEnable");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    initial_enable = tdkTestObj.getResultDetails().strip();
    initial_enable = initial_enable.split("VALUE:")[1].split(" ")[0].strip();

    print "\nTEST STEP %d: Get the initial value of Device.WiFi.2G80211axEnable" %step;
    print "EXPECTED RESULT %d: Should get the initial Device.WiFi.2G80211axEnable successfully" %step;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: GET operation success; 2G80211axEnable is : %s" %(step, initial_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set to false if initially the enable status is not false
        revert_flag = 0;
        proceed_flag = 0;

        if initial_enable == "true":
            step = step + 1;
            setValue = "false";

            #Change the 2G80211axEnable enable status
            tdkTestObj = obj.createTestStep('WIFIAgent_Set_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.2G80211axEnable");
            tdkTestObj.addParameter("paramValue",setValue);
            tdkTestObj.addParameter("paramType","boolean");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Toggle the enable mode of Device.WiFi.2G80211axEnable to %s" %(step, setValue);
            print "EXPECTED RESULT %d: Should set the Device.WiFi.2G80211axEnable to %s successfully" %(step, setValue);

            if expectedresult in actualresult:
                revert_flag = 1;
                proceed_flag = 1;
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Device.WiFi.2G80211axEnable set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Device.WiFi.2G80211axEnable not set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            proceed_flag = 1;
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "Device.WiFi.2G80211axEnable is in disabled state initially";

        if  proceed_flag == 1:
            #Check the Operating Standards
            step = step + 1;
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.OperatingStandards");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();
            operating_standards = details.split("VALUE:")[1].split(" ")[0].strip();

            print "\nTEST STEP %d: Get the Operating Standards using Device.WiFi.Radio.1.OperatingStandards" %step;
            print "EXPECTED RESULT %d: Should get the Device.WiFi.Radio.1.OperatingStandards successfully" %(step);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: GET operation success; Operating Standards are : %s" %(step, operating_standards);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the operating standards are "g,n" when 2G80211axEnable is in disabled state
                step = step + 1;

                print "\nTEST STEP %d: Check if the Device.WiFi.Radio.1.OperatingStandards gives g,n as operating standards when 2G80211axEnable is in disabled state" %step;
                print "EXPECTED RESULT %d: Device.WiFi.Radio.1.OperatingStandards should give g,n as operating standards when 2G80211axEnable is in disabled state" %(step);
                print "Expected Operating Standards : g,n";
                print "Actual Operating Standards : %s" %operating_standards;

                if "g,n" == operating_standards:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: The operating standards are as expected" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: The operating standards are NOT as expected" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Details : %s" %(step, operating_standards);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Device.WiFi.2G80211axEnable could not be disabled";

        #Revert operation
        if revert_flag == 1:
            step = step + 1;
            tdkTestObj = obj.createTestStep('WIFIAgent_Set_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.2G80211axEnable");
            tdkTestObj.addParameter("paramValue",initial_enable);
            tdkTestObj.addParameter("paramType","boolean");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Revert Device.WiFi.2G80211axEnable to %s" %(step, initial_enable);
            print "EXPECTED RESULT %d: Should set the Device.WiFi.2G80211axEnable to %s successfully" %(step, initial_enable);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: 2G80211axEnable set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: 2G80211axEnable not set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Revert operation not required";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Details : %s" %(step, initial_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
