##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WEBPA_SetFirewallLevel</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Using webpa, set the firewall level of gateway</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>25</execution_time>
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
    <test_case_id>TC_WEBPA_2</test_case_id>
    <test_objective>Using webpa, set the firewall level of gateway</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI, Emulator</test_setup>
    <pre_requisite>If SAT token is to be used, token should be created and made available in test manager. Also the config variables SAT_REQUIRED, SAT_TOKEN_FILE, SERVER_URI should be updated in webpaVariables.py</pre_requisite>
    <api_or_interface_used>webpaQuery
parseWebpaResponse</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_Security.Firewall.FirewallLevel</input_parameters>
    <automation_approch>1. Load sysutil module
2. Configure WEBPA server to send get request for Device.X_CISCO_COM_Security.Firewall.FirewallLevel
3. Parse the WEBPA response and save the firewall level
4.  Set a new firewall level using webpa set query
5. Get the new firewall level and compare that with the set value, both should be same
6. Revert the firewall level
7. Unload sysutil module</automation_approch>
    <except_output>Firewall set operation should be success</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_WEBPA_SetFirewallLevel</test_script>
    <skipped>No</skipped>
    <release_version>M58</release_version>
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
obj.configureTestCase(ip,port,'TS_WEBPA_SetFirewallLevel');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:

        firewallLevelList =  {"High", "Low", "Medium"}

        #get the current firewall level
        print "TEST STEP 1: Get and save the current firewall level"
        queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel"}
        queryResponse = webpaQuery(obj, queryParam)

        parsedResponse = parseWebpaResponse(queryResponse, 1)
        print "parsedResponse : %s" %parsedResponse;
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "" and parsedResponse[1] in firewallLevelList:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1 [TEST EXECUTION RESULT] : SUCCESS"

	    orgValue = parsedResponse[1];
	    print "original firewall level: ",orgValue

	    if orgValue == "Low":
	        newValue="Medium"
	    else:
	        newValue="Low"

	    #set the new firewall level
	    print "TEST STEP 2: Set the new firewall level value"
	    queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel","value":newValue,"dataType":0}
	    queryResponse = webpaQuery(obj, queryParam, "set")
	    parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
	    tdkTestObj.executeTestCase("SUCCESS");
            if "SUCCESS" in parsedResponse[0]:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2[TEST EXECUTION RESULT] : SUCCESS"

	        #get the current firewall level and check if its the same as the set value
	        print "TEST STEP 3: Get the new firewall level and check if its the same as the set value"
                queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel"}
                queryResponse = webpaQuery(obj, queryParam)
                parsedResponse = parseWebpaResponse(queryResponse, 1)
                tdkTestObj.executeTestCase("SUCCESS");
                if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
		    setValue = parsedResponse[1];
		    print "Firewall level after set is : ", setValue
		    if setValue == newValue:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3 [TEST EXECUTION RESULT] : SUCCESS"
		    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3 [TEST EXECUTION RESULT] : FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3[TEST EXECUTION RESULT] : FAILURE"

	        print "TEST STEP 4: Revert the firewall level"
	        queryParam = {"name":"Device.X_CISCO_COM_Security.Firewall.FirewallLevel","value":orgValue,"dataType":0}
                queryResponse = webpaQuery(obj, queryParam, "set")
                parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
                tdkTestObj.executeTestCase("SUCCESS");
                if "SUCCESS" in parsedResponse[0]:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4 [TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4[TEST EXECUTION RESULT] : FAILURE"
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2[TEST EXECUTION RESULT] : FAILURE"
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
