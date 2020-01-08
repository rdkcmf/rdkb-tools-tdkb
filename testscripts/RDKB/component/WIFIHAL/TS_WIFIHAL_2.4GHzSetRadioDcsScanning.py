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
  <name>TS_WIFIHAL_2.4GHzSetRadioDcsScanning</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>This api is used to enable or disable Radio DCS scanning</synopsis>
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
    <test_case_id>TC_WIFIHAL_307</test_case_id>
    <test_objective>This api is used to enable or disable Radio DCS scanning</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDcsScanning()
wifi_setRadioDcsScanning()
</api_or_interface_used>
    <input_parameters>methodName = "getRadioDcsScanning" and "etRadioDcsScanning"
RadioIndex = 0
param = 0</input_parameters>
    <automation_approch>1.Load the module
2.Get the value of radio dcs scanning state  and save
3. Toggle the radio dcs scanning state  set api and validate
4. Revert the value
5.Unload the module.</automation_approch>
    <except_output>The radio dcs scanning state should change with the hal api</except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioDcsScanning</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioDcsScanning');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:

	    #Script to load the configuration file of the component
	    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
	    tdkTestObj.addParameter("methodName","getRadioDcsScanning");
	    tdkTestObj.addParameter("radioIndex",idx);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
	    if expectedresult in actualresult:
		#Set the result status of execution
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP 1: Get the current enable state of Radio DCS scanning";
		print "EXPECTED RESULT 1: Should get current enable state of Radio DCS scanning";
		print "ACTUAL RESULT 1: %s" %details;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";

		currState = details.split(":")[1]
		if "Enabled" in currState:
		    newValue= 0;
		    newState = "Disabled"
		else:
		    newValue = 1;
		    newState = "Enabled"
		tdkTestObj.addParameter("methodName","setRadioDcsScanning");
		tdkTestObj.addParameter("radioIndex",idx);
		tdkTestObj.addParameter("param",newValue);
		expectedresult="SUCCESS";
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		details = tdkTestObj.getResultDetails();
		if expectedresult in actualresult:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 2: Set the Radio DCS scanning state";
		    print "EXPECTED RESULT 2: Should toggle the state of Radio DCS Scanning"
		    print "ACTUAL RESULT 2: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : SUCCESS"

		    tdkTestObj.addParameter("methodName","getRadioDcsScanning");
		    tdkTestObj.addParameter("radioIndex",idx);
		    expectedresult="SUCCESS";
		    tdkTestObj.executeTestCase(expectedresult);
		    actualresult = tdkTestObj.getResult();
		    details = tdkTestObj.getResultDetails();
		    if expectedresult in actualresult and newState in details:
			#Set the result status of execution
			tdkTestObj.setResultStatus("SUCCESS");
			print "TEST STEP 3: Validate set function using get function"
			print "EXPECTED RESULT 3: Should get the enable status for 5GHz";
			print "ACTUAL RESULT 3: %s" %details;
			#Get the result of execution
			print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
			#Set the result status of execution
			tdkTestObj.setResultStatus("FAILURE");
			print "TEST STEP 3: Validate set function using get function"
			print "EXPECTED RESULT 3: Should get the enable status for 5GHz";
			print "ACTUAL RESULT 3: %s" %details;
			#Get the result of execution
			print "[TEST EXECUTION RESULT] : FAILURE";
		    #Revert the value
		    tdkTestObj.addParameter("methodName","setRadioDcsScanning");
		    tdkTestObj.addParameter("radioIndex",idx);
		    tdkTestObj.addParameter("param",newValue);
		    expectedresult="SUCCESS";
		    tdkTestObj.executeTestCase(expectedresult);
		    actualresult = tdkTestObj.getResult();
		    details = tdkTestObj.getResultDetails();
		    if expectedresult in actualresult:
			#Set the result status of execution
			tdkTestObj.setResultStatus("SUCCESS");
			print "TEST STEP : Set the Radio DCS scanning state";
			print "EXPECTED RESULT : Should toggle the state of Radio DCS Scanning"
			print "ACTUAL RESULT : %s" %details;
			#Get the result of execution
			print "[TEST EXECUTION RESULT] : SUCCESS"
		    else:
			#Set the result status of execution
			tdkTestObj.setResultStatus("FAILURE");
			print "TEST STEP : Set the Radio DCS scanning state";
			print "EXPECTED RESULT : Should toggle the state of Radio DCS Scanning"
			print "ACTUAL RESULT : %s" %details;
			#Get the result of execution
			print "[TEST EXECUTION RESULT] : FAILURE"

		else:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 2: Set the Radio DCS scanning state";
		    print "EXPECTED RESULT 2: Should toggle the state of Radio DCS Scanning"
		    print "ACTUAL RESULT 2: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : FAILURE"
	    else:
		#Set the result status of execution
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 1: Get the current enable state of Radio DCS scanning";
		print "EXPECTED RESULT 1: Should get current enable state of Radio DCS scanning";
		print "ACTUAL RESULT 1: %s" %details;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
