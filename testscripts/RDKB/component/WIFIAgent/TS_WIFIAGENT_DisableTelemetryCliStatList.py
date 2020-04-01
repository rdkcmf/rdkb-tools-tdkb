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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>7</version>
  <name>TS_WIFIAGENT_DisableTelemetryCliStatList</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Disable cli stats telemetry markers for all available Virtual access points</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIAGENT_97</test_case_id>
    <test_objective>Disable cli stats telemetry markers for all available Virtual access points</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.CliStatList</input_parameters>
    <automation_approch>1. Load the Module
2. Get the current clistat value and save it
3. Disable the WiFi Telemetry Clistat list using the parameter Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.CliStatList
4. Get the clistatValue and check if its disabled or not
5. Revert back the clistat original value
6. Unload the Module</automation_approch>
    <expected_output>Cli stats telemetry markers should be disabled for all available Virtual access points</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_DisableTelemetryCliStatList</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_DisableWiFiTelemetryClistatlist');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.CliStatList")
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    orgCliStatList = details.split("VALUE:")[1].split(' ')[0];

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current telemetry Clistat List";
        print "EXPECTED RESULT 1: Should get the current  telemetry Clistat List";
	print "ACTUAL RESULT 1: Current  telemetry Clistat List is  %s" %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.CliStatList")
	tdkTestObj.addParameter("paramValue","")
	tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails()

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set Telemetry Clistat List";
            print "EXPECTED RESULT 2: Should set new Telemetry Clistat List";
            print "ACTUAL RESULT 2: Details:  %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    #check if Clistat List is set
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.CliStatList")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            cliStatValue = details.split("VALUE:")[1].split(' ')[0];

	    if expectedresult in actualresult  and cliStatValue == "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if  telemetry Clistat List is set to new value"
                print "EXPECTED RESULT 3:  Telemetry Clistat List should be set as new value"
                print "ACTUAL RESULT 3: Details is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.CliStatList")
	        tdkTestObj.addParameter("paramValue",orgCliStatList);
	        tdkTestObj.addParameter("paramType","string");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Revert the Telemetry Clistat List";
                    print "EXPECTED RESULT 4: Should set the original Telemetry Clistat List";
                    print "ACTUAL RESULT 4: Details:  %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Revert the Telemetry Clistat List";
                    print "EXPECTED RESULT 4: Should set the original Telemetry Clistat List";
                    print "ACTUAL RESULT 4: Details:  %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if  telemetry Clistat List is set to new value"
                print "EXPECTED RESULT 3:  Telemetry Clistat List should be set as new value"
                print "ACTUAL RESULT 3: Details is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set Telemetry Clistat List";
            print "EXPECTED RESULT 2: Should set new Telemetry Clistat List";
            print "ACTUAL RESULT 2: Details:  %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current  telemetry Clistat List";
        print "EXPECTED RESULT 1: Should get the current  telemetry Clistat List";
        print "ACTUAL RESULT 1: Details is %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
