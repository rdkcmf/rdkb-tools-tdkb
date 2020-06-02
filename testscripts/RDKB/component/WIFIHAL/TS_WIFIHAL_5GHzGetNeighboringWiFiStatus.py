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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzGetNeighboringWiFiStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetNeighboringWiFiStatus</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>This scripts invokes wifi_getNeighboringWiFiStatus() api to get the neighbour access point informations</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_302</test_case_id>
    <test_objective>This scripts invokes wifi_getNeighboringWiFiStatus() api to get the neighbour access point informations</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getNeighboringWiFiStatus()
wifi_startNeighborScan()</api_or_interface_used>
    <input_parameters>radioIndex = 1</input_parameters>
    <automation_approch>1.Load the module
2. Invoke wifi_startNeighborScan() to do neighbouring WiFi scan
3. Wait for a few sceonds
4.Get the value of wifi_getNeighboringWiFiStatus()
5. Check if the api returns the neighboring wifi status
6.Unload the module.</automation_approch>
    <expected_output>The wifi_getNeighboringWiFiStatus() api should return the neighboring wifi status</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetNeighboringWiFiStatus</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import random;
import time;
from wifiUtility import *;
radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetNeighboringWiFiStatus');

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

	    #Prmitive test case which is associated to this Script
	    tdkTestObj = obj.createTestStep('WIFIHAL_StartNeighborScan');
	    tdkTestObj.addParameter("apIndex", idx);
	    #Scan mode '0' only active, so checking it alone 
	    tdkTestObj.addParameter("scan_mode", 1);
	    value = random.randrange(10,20);
	    tdkTestObj.addParameter("dwell_time", value);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();

	    if expectedresult in actualresult :
		print "TEST STEP : Successfully start the wifi_startNeighborScan"
		print "EXPECTED RESULT : Should successfully start the wifi_startNeighborScan"
		print "ACTUAL RESULT : Successfully started wifi_startNeighborScan"
		print "Output details: %s" %details;

		time.sleep(7)
		#Script to load the configuration file of the component
		tdkTestObj = obj.createTestStep("WIFIHAL_GetNeighboringWiFiStatus");
		tdkTestObj.addParameter("radioIndex",idx);
		expectedresult="SUCCESS";
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		details = tdkTestObj.getResultDetails();
		if expectedresult in actualresult:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 2: Get the neighboring wifi status for 5GHz";
		    print "EXPECTED RESULT 2: Should get the neighboring wifi status for 5GHz";
		    print "ACTUAL RESULT 2: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 2: Get the neighboring wifi status for 5GHz";
		    print "EXPECTED RESULT 2: Should get the neighboring wifi status for 5GHz";
		    print "ACTUAL RESULT 2: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : FAILURE";

	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP : Get the wifi_startNeighborScan"
		print "EXPECTED RESULT : Should successfully get the result of wifi_startNeighborScan"
		print "ACTUAL RESULT : Failed to get the result of wifi_startNeighborScan"
		print "Output details: %s" %details;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
