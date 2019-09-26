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
  <name>TS_ETHWAN_CheckWEBPA</name>
  <primitive_test_id/>
  <primitive_test_name>EthWAN_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>WEBPA support must be available in ETHWAN Mode</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_ETHWAN_06</test_case_id>
    <test_objective>WEBPA support must be available in ETHWAN Mode</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. The broadband device should be in ETHWAN setup
2. The EthWAN mode should be enabled
3. TDK Agent must be up and running</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled</input_parameters>
    <automation_approch>1. Load module
2. Get the ethwan mode and check if it true or not
3. If ethwan is enabled,  check if webpa is working or not.
4. Unload module</automation_approch>
    <except_output>WEBPA should be working in ethwan mode</except_output>
    <priority>High</priority>
    <test_stub_interface>ETHWAN</test_stub_interface>
    <test_script>TS_ETHWAN_CheckWEBPA</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from webpaUtility import *

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHWAN_CheckWEBPA');
obj1.configureTestCase(ip,port,'TS_ETHWAN_CheckWEBPA');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    ethwanEnable = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the enable status of Ethwan";
        print "EXPECTED RESULT 1: Should get the enable status of Ethwan";
        print "ACTUAL RESULT 1: Ethwan Enable status is %s" %ethwanEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	if "true" == ethwanEnable:
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "The device is in ethwan mode."

	    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    	    if "SUCCESS" in preRequisiteStatus:

    	        queryParam = {"name":"Device.DeviceInfo.ManufacturerOUI"}
    	        queryResponse = webpaQuery(obj, queryParam)

    	        parsedResponse = parseWebpaResponse(queryResponse, 1)
    	        tdkTestObj = obj.createTestStep('ExecuteCmd');
    	        tdkTestObj.executeTestCase("SUCCESS");
    	        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
    	            getStatus = parsedResponse[1];
    	            if getStatus:
    	                tdkTestObj.setResultStatus("SUCCESS");
    	                print "ManufacturerOUI:",getStatus
    	                print "[TEST EXECUTION RESULT] : SUCCESS"
    	            else:
    	                tdkTestObj.setResultStatus("FAILURE");
    	                print "[TEST EXECUTION RESULT] : FAILURE, invalid status received"
    	        else:
    	            tdkTestObj.setResultStatus("FAILURE");
    	            print "[TEST EXECUTION RESULT] : FAILURE"
    	    else:
    	        tdkTestObj.setResultStatus("FAILURE");
    	        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"

	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "The device is not in ethwan mode. Please check the device setup"
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the enable status of Ethwan";
        print "EXPECTED RESULT 1: Should get the enable status of Ethwan";
        print "ACTUAL RESULT 1: Ethwan Enable status is %s" %ethwanEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj1.unloadModule("tdkbtr181");
    obj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
