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
  <name>TS_WIFIAGENT_CheckTelemetryMarkerFor5GHzWiFiClientRxTxValue</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check for the telemetry marker WIFI_TXCLIENTS_2 and WIFI_RXCLIENTS_2 and it should be non empty values</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_96</test_case_id>
    <test_objective>Check for the telemetry marker WIFI_RXCLIENTS_2 and WIFI_TXCLIENTS_2 in log file /rdklogs/logs/wifihealth.txt for 5GHz WiFi client and it should be non empty values</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a WiFi cilent to 2.4Ghz private SSID of DUT</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module.
2. Check whether wifihelath.txt file is present or not
3.Grep "WIFI_RXCLIENT_2" and "WIFI_TXCLIENT_2" in wifihealth.txt file and get the values andd it should be non empty values
4.Unload module</automation_approch>
    <expected_output>Should get the telemetry marker of "WIFI_RX_CLIENT_2"and "WIFI_TXCLIENT_2" and it should be  non empty values</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerFor5GHzWiFiClientRxTxValue</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerFor5GHzWiFiClientRxTxValue');

#Get the result of connection with test component and DUT
loadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check for wifihealth log file presence";
        print "EXPECTED RESULT 1:wifihealth log file should be present";
        print "ACTUAL RESULT 1:wifihealth log file is present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	markerfound = 0;
        for i in range(1,15):
            if markerfound == 1:
                break;
            else:
		query="cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_RXCLIENTS_2:\""
		print "query:%s" %query
		tdkTestObj = sysObj.createTestStep('ExecuteCmd');
		tdkTestObj.addParameter("command", query)
		expectedresult="SUCCESS";
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		details = tdkTestObj.getResultDetails().strip().replace("\\n","");
        	print "Marker Detail Found fromLog file is: %s "%details;

       	        if (len(details) == 0) or details.endswith(":") or "WIFI_RXCLIENTS_2" not in details:
	    	    markerfound = 0;
                    sleep(60);
		else:
        	    telemetryRXClientValue = details.split("WIFI_RXCLIENTS_2:")[1].split(',')[0];
	    	    markerfound = 1;

	if expectedresult in actualresult and markerfound == 1:
            tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: WIFI_RXCLIENTS_2 Marker should be present";
	    print "EXPECTED RESULT 2: WIFI_RXCLIENTS_2 Marker should be present";
	    print "ACTUAL RESULT 2:WIFI_RXCLIENTS_2 Marker is %s" %telemetryRXClientValue
	    #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    query="cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_TXCLIENTS_2:\""
	    print "query:%s" %query
    	    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    	    tdkTestObj.addParameter("command", query)
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
            print "Marker Detail Found fromLog file is: %s "%details;

            if (len(details) == 0) or details.endswith(":") or "WIFI_TXCLIENTS_2" not in details:
	        markerfound = 0;
	    else:
                telemetryTXClientValue = details.split("WIFI_TXCLIENTS_2:")[1].split(',')[0];
	        markerfound = 1;

	    if expectedresult in actualresult and markerfound == 1:
                tdkTestObj.setResultStatus("SUCCESS");
	        print "TEST STEP 3: WIFI_TXCLIENTS_2 Marker should be present";
	        print "EXPECTED RESULT 3: WIFI_TXCLIENTS_2 Marker should be present";
	        print "ACTUAL RESULT 3:WIFI_TXCLIENTS_2 Marker is %s" %telemetryTXClientValue
	        #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
	        tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 3: WIFI_TXCLIENTS_2 Marker should be present";
	        print "EXPECTED RESULT 3: WIFI_TXCLIENTS_2 Marker should be present";
	        print "ACTUAL RESULT 3:WIFI_TXCLIENTS_2 Marker is  Not Present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 2: WIFI_RXCLIENTS_2 Marker should be present";
	    print "EXPECTED RESULT 2: WIFI_RXCLIENTS_2 Marker should be present";
	    print "ACTUAL RESULT 2:WIFI_RXCLIENTS_2 Marker is  Not Present";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check for wifihealth log file presence";
        print "EXPECTED RESULT 1:wifihealth log file should be present";
        print "ACTUAL RESULT 1:wifihealth log file is NOT present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load lmlite module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
