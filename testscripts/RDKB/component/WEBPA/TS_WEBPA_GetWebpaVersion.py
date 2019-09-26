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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_WEBPA_GetWebpaVersion</name>
  <primitive_test_id/>
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the WEBPA version</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WEBPA_27</test_case_id>
    <test_objective>To get client WEBPA version details</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI, Emulator</test_setup>
    <pre_requisite>If SAT token is to be used, token should be created and made available in test manager. Also the config variables SAT_REQUIRED, SAT_TOKEN_FILE, SERVER_URI should be updated in webpaVariables.py</pre_requisite>
    <api_or_interface_used>webpaQuery
parseWebpaResponse</api_or_interface_used>
    <input_parameters>Device.X_RDKCENTRAL-COM_Webpa.Version</input_parameters>
    <automation_approch>1. Load sysutil module
2. Configure WEBPA server to send get request for Device.X_RDKCENTRAL-COM_Webpa.Version
3. Parse the WEBPA response and save the WEBPA version
4. Unload sysutil module</automation_approch>
    <except_output>Should get client WEBPA version</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_WEBPA_getWebpaVersion</test_script>
    <skipped>No</skipped>
    <release_version/>M66<release_version/>
    <remarks/><remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WEBPA_GetWebpaVersion');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:
	#get the current Webpa Version
	print "TEST STEP 1: Get and save the current Webpa Version "
	queryParam = {"name":"Device.X_RDKCENTRAL-COM_Webpa.Version"}
	queryResponse = webpaQuery(obj, queryParam)
	parsedResponse = parseWebpaResponse(queryResponse, 1)
	print "parsedResponse : %s" %parsedResponse;
	tdkTestObj = obj.createTestStep('ExecuteCmd');
	tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "" :
            tdkTestObj.setResultStatus("SUCCESS");
	    print "[TEST EXECUTION RESULT] : SUCCESS"
	    Value = parsedResponse[1];
	    print "Webpa Version: ",Value;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"
    obj.unloadModule("sysutil");
else:
    print "FAILURE to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
