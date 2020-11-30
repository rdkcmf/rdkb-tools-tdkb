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
  <version>1</version>
  <name>TS_WIFIHAL_5GHzPushApHotspotElement</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Toggle the current ApHotspotElement enabled status using wifi_pushApHotspotElement() and validate via wifi_getApHotspotElement()</synopsis>
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
    <test_case_id>TC_WIFIHAL_438</test_case_id>
    <test_objective>Toggle the current ApHotspotElement enabled status using wifi_pushApHotspotElement() and validate via wifi_getApHotspotElement()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApHotspotElement()
wifi_pushApHotspotElement()</api_or_interface_used>
    <input_parameters>index:9</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getApHotspotElement(), get and save the ApHotspotElement enabled status
3. Toggle the enable status using wifi_pushApHotspotElement
4. Using wifi_getApHotspotElement() check if set was operation was success or not
5. Revert back ApHotspotElement status to its initial value
6.Unload wifihal module</automation_approch>
    <expected_output>wifi_pushApHotspotElement() should successfully toggle the ApHotspotElement enabled status</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPushApHotspotElement</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPushApHotspotElement');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    passPoint_5G_Index = 9;
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
    tdkTestObj.addParameter("methodName","getApHotspotElement");
    #Radio index stands for SSID index here.
    tdkTestObj.addParameter("radioIndex", passPoint_5G_Index);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and "Enabled" in details or "Disabled" in details:
	#Set the result status of execution
	tdkTestObj.setResultStatus("SUCCESS");
	print "TEST STEP 1: Get the ApHotspotElement enabled status  for 5GHz using wifi_getApHotspotElement()";
        print "EXPECTED RESULT 1: Should get ApHotspotElement enabled status  for 5GHz using wifi_getApHotspotElement()";
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : SUCCESS";
	if "Enabled" in details:
	    oldEnable = 1;
	    newEnable = 0;
            expectedStatus = "Disabled"
	else:
	    oldEnable = 0;
	    newEnable = 1;
            expectedStatus = "Enabled"
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
	tdkTestObj.addParameter("methodName","pushApHotspotElement");
	tdkTestObj.addParameter("radioIndex",passPoint_5G_Index);
	tdkTestObj.addParameter("param",newEnable);
	expectedresult="SUCCESS";
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
	    #Set the result status of execution
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: Toggle the ApHotspotElement enabled status for 5GHz";
	    print "EXPECTED RESULT 2: Should toggle the ApHotspotElement enable status for 5GHz to ", expectedStatus ;
	    print "ACTUAL RESULT 2: %s" %details;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";

	    #Script to load the configuration file of the component
	    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
	    tdkTestObj.addParameter("methodName","getApHotspotElement")
	    tdkTestObj.addParameter("radioIndex",passPoint_5G_Index);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
	    if expectedresult in actualresult :
		newStatus = details.split(":")[1].strip();
		if newStatus == expectedStatus:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 3: Get the ApHotspotElement enabled status for 5GHz";
		    print "EXPECTED RESULT 3: Should get the ApHotspotElement enabled status same as the set value";
		    print "ACTUAL RESULT 3: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "ACTUAL RESULT 3: %s" %details;
		    print "FAILURE : ApHotspotElement enabled status not same as the set value";
	    else:
		#Set the result status of execution
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 3: Get the ApHotspotElement enabled status for 5GHz";
		print "EXPECTED RESULT 3: Should get the ApHotspotElement enabled status same as the set value";
		print "ACTUAL RESULT 3: %s" %details;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 2: Toggle the ApHotspotElement enabled status for 5GHz";
	    print "EXPECTED RESULT 2: Should toggle the ApHotspotElement enable status for 5GHz to ", expectedStatus ;
	    print "ACTUAL RESULT 2: %s" %details;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : FAILURE";

	#setting initial value to ApHotspotElement
	tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
	tdkTestObj.addParameter("methodName","pushApHotspotElement");
	tdkTestObj.addParameter("radioIndex",passPoint_5G_Index);
	tdkTestObj.addParameter("param",oldEnable);
	expectedresult="SUCCESS";
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
	    #Set the result status of execution
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP : Revert the ApHotspotElement enabled status for 5GHz";
	    print "EXPECTED RESULT : Should revert the ApHotspotElement enabled status for 5GHz";
	    print "ACTUAL RESULT : %s" %details;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";
	else:
	    #Set the result status of execution
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP : Revert the ApHotspotElement enabled status for 5GHz";
	    print "EXPECTED RESULT : Should revert the ApHotspotElement enabled status for 5GHz";
	    print "ACTUAL RESULT : %s" %details;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
	tdkTestObj.setResultStatus("FAILURE");
	print "TEST STEP 1: Get the ApHotspotElement enabled status  for 5GHz using wifi_getApHotspotElement()";
	print "EXPECTED RESULT 1: Should get ApHotspotElement enabled status  for 5GHz using wifi_getApHotspotElement()";
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
