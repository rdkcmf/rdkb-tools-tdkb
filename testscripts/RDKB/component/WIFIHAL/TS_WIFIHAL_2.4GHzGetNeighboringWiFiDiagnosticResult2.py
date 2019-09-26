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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzGetNeighboringWiFiDiagnosticResult2</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetNeighboringWiFiDiagnosticResult2</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To start the wifi scan and get the result for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_294</test_case_id>
    <test_objective>To start the wifi scan and get the result for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getNeighboringWiFiDiagnosticResult2()</api_or_interface_used>
    <input_parameters>radioIndex: 0</input_parameters>
    <automation_approch>1.Load the module
2.Using WIFIHAL_GetNeighboringWiFiDiagnosticResult2 call wifi_getNeighboringWiFiDiagnosticResult2() and get the scan result
3.Print the number of access points identified
4.Unload the module.</automation_approch>
    <except_output>Should detect and return the neighboring access points and the corresponding parameters</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetNeighboringWiFiDiagnosticResult2</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetNeighboringWiFiDiagnosticResult2');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIHAL_GetNeighboringWiFiDiagnosticResult2');
    tdkTestObj.addParameter("radioIndex", 0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
	details = details.split(":ap_")[1].strip();
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Get the NeighboringWiFiDiagnosticResult"
        print "EXPECTED RESULT : Should successfully get the NeighboringWiFiDiagnosticResult"
        print "ACTUAL RESULT : Successfully gets the NeighboringWiFiDiagnosticResult"
        print "Details: "
        detailList = details.split(",")
        detailApList = details.split(",ap_")
        for i in range(0,17):
	    print detailApList[i]
	output_array_size = detailList[-1].split('=')[1];
	print "output_array_size=",output_array_size
	print "Identified %s neighboring access points"%output_array_size
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Get the NeighboringWiFiDiagnosticResult"
        print "EXPECTED RESULT : Should successfully get the NeighboringWiFiDiagnosticResult"
        print "ACTUAL RESULT : Failed to get the NeighboringWiFiDiagnosticResult"
        print "Details: %s"%details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

