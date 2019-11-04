##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WEBPA_SetBandSteeringCapability</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if setting Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to false returns failure</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WEBPA_36</test_case_id>
    <test_objective>To check if setting Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to false returns failure</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>If SAT token is to be used, token should be created and made available in test manager. Also the config variables SAT_REQUIRED, SAT_TOKEN_FILE, SERVER_URI should be updated in webpaVariables.py</pre_requisite>
    <api_or_interface_used>webpaQuery
parseWebpaResponse</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability</input_parameters>
    <automation_approch>1. Load sysutil module
2. Configure WEBPA server to send get request for Device.X_RDKCENTRAL-COM_Webpa.Version
3. Parse the WEBPA response and save the WEBPA version
4.Get the value of Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability
5.Set Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to false and check if it returns failure
6. Unload sysutil module</automation_approch>
    <expected_output>Setting Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to false should return failure</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_WEBPA_SetBandSteeringCapability</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from webpaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBPA_SetBandSteeringCapability');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:


        print "TEST STEP 1: Get and save the current BandSteering capability"
        queryParam = {"name":"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability"}
        queryResponse = webpaQuery(obj, queryParam)

        parsedResponse = parseWebpaResponse(queryResponse, 1)
        print "parsedResponse : %s" %parsedResponse;
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0]:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1 [TEST EXECUTION RESULT] : SUCCESS"

            orgValue = parsedResponse[1];
            print "BandSteering Capability: ",orgValue

            newValue = "false"

            print "TEST STEP 2: Set the BandSteering Capability as false"
            queryParam = {"name":"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability","value":newValue,"dataType":3}
            queryResponse = webpaQuery(obj, queryParam, "set")
            parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
            tdkTestObj.executeTestCase("SUCCESS");
            if "FAILURE" in parsedResponse[0] and "520" in queryResponse:
                tdkTestObj.setResultStatus("SUCCESS");
                print "EXPECTED RESULT 2: BandSteering Capability should not be set to false";
                print "ACTUAL RESULT 2: BandSteering Capability is not set to false";                
                print "TEST STEP 2[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "EXPECTED RESULT 2: BandSteering Capability should not be set to false";
                print "ACTUAL RESULT 2: BandSteering Capability is set to false";
                print "TEST STEP 2[TEST EXECUTION RESULT] : FAILURE"
                print "TEST STEP 3:Revert the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to original value "
                queryParam = {"name":"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability","value":orgValue,"dataType":3}
                queryResponse = webpaQuery(obj, queryParam, "set")
                parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
                tdkTestObj.executeTestCase("SUCCESS");
                if "SUCCESS" in parsedResponse[0]:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3 [TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3:Revert the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Capability to original value: FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"

    obj.unloadModule("sysutil");

else:
    print "FAILURE to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";


