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
  <name>TS_WIFIHAL_5GHzGetLayer2TrafficInspectionFiltering</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the current Layer2TrafficInspectionFiltering enabled status for 5G using wifi_getLayer2TrafficInspectionFiltering()</synopsis>
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
    <test_case_id>TC_WIFIHAL_418</test_case_id>
    <test_objective>Get the current Layer2TrafficInspectionFiltering enabled status for 5G using wifi_getLayer2TrafficInspectionFiltering()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getLayer2TrafficInspectionFiltering</api_or_interface_used>
    <input_parameters>index:9</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getLayer2TrafficInspectionFiltering() and get the Layer2TrafficInspectionFiltering enabled status
3. Check if status is returned as either Enabled or Disabled
4.Unload wifihal module</automation_approch>
    <expected_output>wifi_getLayer2TrafficInspectionFiltering() should successfully return the current Layer2TrafficInspectionFiltering enabled status</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetLayer2TrafficInspectionFiltering</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetLayer2TrafficInspectionFiltering');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    passPoint_5G_Index = 9;
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
    tdkTestObj.addParameter("methodName","getLayer2TrafficInspectionFiltering");
    #Radio index stands for SSID index here.
    tdkTestObj.addParameter("radioIndex", passPoint_5G_Index);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and "Enabled" in details or "Disabled" in details:
	#Set the result status of execution
	tdkTestObj.setResultStatus("SUCCESS");
	print "TEST STEP 1: Get the Layer2TrafficInspectionFiltering enabled status  for 5GHz using wifi_getLayer2TrafficInspectionFiltering()";
        print "EXPECTED RESULT 1: Should get Layer2TrafficInspectionFiltering enabled status  for 5GHz using wifi_getLayer2TrafficInspectionFiltering()";
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
	#Set the result status of execution
	tdkTestObj.setResultStatus("FAILURE");
	print "TEST STEP 1: Get the Layer2TrafficInspectionFiltering enabled status  for 5GHz using wifi_getLayer2TrafficInspectionFiltering()";
	print "EXPECTED RESULT 1: Should get Layer2TrafficInspectionFiltering enabled status  for 5GHz using wifi_getLayer2TrafficInspectionFiltering()";
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
