##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_SetWiFiTelemetryTxRxRateList</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Enable TxRxRate telemetry markers for private APs</synopsis>
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
    <test_case_id>TC_WIFIAGENT_101</test_case_id>
    <test_objective>Enable TxRxRate Telemetry markers for private APs </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList</input_parameters>
    <automation_approch>1. Load the module
2. Get the current TxRx Rate List value
3. Set the TxRx RateList with private AP's and it should be sucess
4. Revert back the original value
5. Unload the module</automation_approch>
    <expected_output>Should be able to enable TxRxRate telemetry marker for Private WiFi APs</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetWiFiTelemetryTxRxRateList</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetWiFiTelemetryTxRxRateList');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    orgTxRxvalue = details.split("VALUE:")[1].split(' ')[0];

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current TxRxRateList value";
        print "EXPECTED RESULT 1: Should get the current TxRxRateList value";
        print "ACTUAL RESULT 1: Current TxRxRateList value is  %s" %orgTxRxvalue
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        newTxRxRateListTobeset = "1,2"
        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList");
        tdkTestObj.addParameter("paramValue",newTxRxRateListTobeset);
        tdkTestObj.addParameter("paramType","string");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set TxRxRateList as Private WiFi AP List (1,2)";
            print "EXPECTED RESULT 2: Should  set a value as Prviate WiFi AP's (1,2)";
            print "ACTUAL RESULT 2: Details:  %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            sleep(5);
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            newTxRxvalue = details.split("VALUE:")[1].split(' ')[0];

            if expectedresult in actualresult and newTxRxvalue == newTxRxRateListTobeset:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the TxRxRateList value after set";
                print "ACTUAL RESULT 3: TxRxRateList value after set is %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the TxRxRateList value after set";
                print "ACTUAL RESULT 3: Failed to get TxRxRateList value after set";
                print "[TEST EXECUTION RESULT] : FAILURE";

	    #change TxRxValue state to previous one
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.TxRxRateList");
            tdkTestObj.addParameter("paramValue",orgTxRxvalue);
            tdkTestObj.addParameter("paramType","string");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Restore initial TxRxRateList value";
                print "EXPECTED RESULT 4: Should Set initial TxRxRateList value";
                print "ACTUAL RESULT 4: Details is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Restore initial TxRxRateList value";
                print "EXPECTED RESULT 4: Should Set initial TxRxRateList value";
                print "ACTUAL RESULT 4: Details is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set TxRxRateList value as Private WiFi AP's (1,2)";
            print "EXPECTED RESULT 2: Should  set a value as private WiFi AP's (1,2)";
            print "ACTUAL RESULT 2: Details:  %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current TxRxRateList Value"
        print "EXPECTED RESULT 1: Failure in getting the current TxRxRateList value"
        print "ACTUAL RESULT 1: Details is %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
else:
    print "Failed to load wifiagent module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
