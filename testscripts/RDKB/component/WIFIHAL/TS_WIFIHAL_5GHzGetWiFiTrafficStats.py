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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzGetWiFiTrafficStats</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetWifiTrafficStats</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get and check the WiFiTrafficStats data using wifi_getWifiTrafficStats()</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_286</test_case_id>
    <test_objective>Get and check the WiFiTrafficStats data using wifi_getWifiTrafficStats()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI, Emulator</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getWifiTrafficStats()</api_or_interface_used>
    <input_parameters>ApIndex</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getWifiTrafficStats() for 2.4G.
3. Check if wifi_getWifiTrafficStats() returns status as success
4. Check if the wifi traffic stats values returned are greater than or equal to 0
5. Unload wifihal module</automation_approch>
    <expected_output>wifi traffic stats values returned should be greater than or equal to 0</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetWiFiTrafficStats</test_script>
    <skipped>No</skipped>
    <release_version>M80</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetWiFiTrafficStats');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	radioIndex = idx
	primitive = 'WIFIHAL_GetWifiTrafficStats'
	tdkTestObj = obj.createTestStep(primitive);
	tdkTestObj.addParameter("apIndex",radioIndex);
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
            trafficStats =  details.rstrip('\n').split('-')[1]
            wifi_ErrorsSent = trafficStats.split(',')[0].split(' ')[2]
            wifi_ErrorsReceived = trafficStats.split(',')[1].split(' ')[2]
            wifi_UnicastPacketsSent = trafficStats.split(',')[2].split(' ')[2]
            wifi_UnicastPacketsReceived = trafficStats.split(',')[3].split(' ')[2]
            wifi_DiscardedPacketsSent= trafficStats.split(',')[4].split(' ')[2]
            wifi_DiscardedPacketsReceived = trafficStats.split(',')[5].split(' ')[2]
            wifi_MulticastPacketsSent = trafficStats.split(',')[6].split(' ')[2]
            wifi_MulticastPacketsReceived = trafficStats.split(',')[7].split(' ')[2].replace("\\n", "")

	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 1: Get the Wifi Traffic statistics for 5GHz";
	    print "EXPECTED RESULT 1: wifi_getWifiTrafficStats should return the wifi traffic statistics for 5GHz";
	    print "ACTUAL RESULT 1: wifi_getWifiTrafficStats operation returned SUCCESS";
	    print "Actual result is :",details;
	    print "[TEST EXECUTION RESULT] 1: SUCCESS";

            print "TEST STEP 2: Check if the Wifi Traffic statistics values for 5GHz are greater than or equal to 0";
            print "EXPECTED RESULT 2: Wifi Traffic statistics values for 5GHz should be greater than or equal to 0";
            if int(wifi_ErrorsSent) >= 0 and int(wifi_ErrorsReceived) >=0 and int(wifi_UnicastPacketsSent) >=0 and int(wifi_UnicastPacketsReceived) >=0 and int(wifi_DiscardedPacketsSent) >=0 and int(wifi_DiscardedPacketsReceived) >=0 and int(wifi_MulticastPacketsSent) >=0 and int(wifi_MulticastPacketsReceived) >=0:
                print "ACTUAL RESULT 2: Wifi Traffic statistics values for 5GHz are greater than or equal to 0";
                print "[TEST EXECUTION RESULT] 2: SUCCESS";
            else:
                print "ACTUAL RESULT 2: Wifi Traffic statistics values for 5GHz are not greater than or equal to 0";
                print "[TEST EXECUTION RESULT] 2: FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
  	    print "TEST STEP 1: Get the Wifi Traffic statistics for 5GHz";
	    print "EXPECTED RESULT 1: wifi_getWifiTrafficStats should return the Wifi traffic statistics for 5GHz";
	    print "ACTUAL RESULT 1: Failed to get the Wifi Traffic statistics values for 5GHz";
	    print "Actual result is :",details;
	    print "[TEST EXECUTION RESULT] 1: FAILURE";
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
