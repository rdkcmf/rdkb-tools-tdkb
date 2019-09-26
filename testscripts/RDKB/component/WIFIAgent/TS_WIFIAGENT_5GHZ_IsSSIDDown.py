##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_WIFIAGENT_5GHZ_IsSSIDDown</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check when 5GHZ ssid state is disabled, its status is "down"</synopsis>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_20</test_case_id>
    <test_objective>Check when 5GHZ ssid state is disabled, its status is "down"</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.2.Enable
Device.WiFi.SSID.2.Status</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Using WIFIAgent_Get, get and save Device.WiFi.SSID.2.Enable value
3. Using WIFIAgent_Set disable Device.WiFi.SSID.2.Enable
4. Using WIFIAgent_Get, get Device.WiFi.SSID.2.Status and check if its down
5.Using WIFIAgent_Set set Device.WiFi.SSID.2.Enable to its previous value
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.</automation_approch>
    <except_output>When ssid state is disabled, its status should be "down"</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHZ_IsSSIDDown</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHZ_IsSSIDDown');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.2.Enable")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the state of SSID2";
        print "EXPECTED RESULT 1: Should get the state of SSID2"
        orgState = details.split("VALUE:")[1].split(' ')[0];
        print "ACTUAL RESULT 1: State is %s %s" %(details,orgState);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Enable ssid2 to check its status
        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.2.Enable")
        tdkTestObj.addParameter("paramValue","false")
        tdkTestObj.addParameter("paramType","boolean")
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Disable SSID2";
            print "EXPECTED RESULT 1: Should disable SSID2"
            print "ACTUAL RESULT 1: State is %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            sleep(5);
            #check if ssid2 status is up or not
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.SSID.2.Status")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            status = details.split("VALUE:")[1].split(' ')[0];

            if expectedresult in actualresult and "Down" in status:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Check if SSID2 staus is Down";
                print "EXPECTED RESULT 1: SSID2 staus should be down";
                print "ACTUAL RESULT 1: Status is %s %s" %(details,status);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Check if SSID2 staus is down";
                print "EXPECTED RESULT 1: SSID2 staus should be down";
                print "ACTUAL RESULT 1: Status is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

           #change ssid state to previous one
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.WiFi.SSID.2.Enable")
            tdkTestObj.addParameter("paramValue",orgState)
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Restore Enable state of SSID2";
                print "EXPECTED RESULT 1: Should Restore Enable state of SSID2";
                print "ACTUAL RESULT 1: State is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Restore Enable state of SSID2";
                print "EXPECTED RESULT 1: Should Restore Enable state of SSID2";
                print "ACTUAL RESULT 1: State is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Disable SSID2";
            print "EXPECTED RESULT 1: Should disable SSID2"
            print "ACTUAL RESULT 1:  %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the state of SSID2"
        print "EXPECTED RESULT 1: Failure in getting the state of SSID2"
        print "ACTUAL RESULT 1: State is %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");

else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

