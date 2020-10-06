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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHz_SetApScanFiltermode_First</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_SetApScanFilter</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the filter  mode WIFI_SCANFILTER_MODE_FIRST using WiFi HAL API wifi_setApScanFilter for 5GHz AccessPoint</synopsis>
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
    <test_case_id>TC_WIFIHAL_414</test_case_id>
    <test_objective>To validate the filter  mode WIFI_SCANFILTER_MODE_FIRST using WiFi HAL API wifi_setApScanFilter for 5GHz AccessPoint</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.DUT should have some neighboring APs with valid SSID names
2. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
3.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApScanFilter</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the ssid name of a neighboring AP using wifi_getNeighboringWiFiDiagnosticResult2() to use in filter setting
3. Check if SSID name is valid
4. Set filter Ap filter mode as WIFI_SCANFILTER_MODE_ENABLED, with the above SSID name.
5. Invoke wifi_getNeighboringWiFiDiagnosticResult2() again and check if the SSID set in filter is returned
6.Unload wifihal module
</automation_approch>
    <expected_output>On setting filter  mode as WIFI_SCANFILTER_MODE_FIRST, the SSID name set in filter should come up as first entry in further neighbor Ap scan result</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHz_SetApScanFiltermode_First</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHz_SetApScanFiltermode_First');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Prmitive test case which associated to this Script
	tdkTestObj = obj.createTestStep('WIFIHAL_GetNeighboringWiFiDiagnosticResult2');
	tdkTestObj.addParameter("radioIndex", idx);
	expectedresult="SUCCESS";
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult :
	    details = details.split(":ap_")[1].strip();
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 1 : Get the NeighboringWiFiDiagnosticResult"
	    print "EXPECTED RESULT 1 : Should successfully get the NeighboringWiFiDiagnosticResult"
	    print "ACTUAL RESULT 1 : Successfully gets the NeighboringWiFiDiagnosticResult"
	    print "Details: "
	    detailList = details.split(",")
	    org_ssidname = details.split(",")[0].split("=")[1].strip()
	    detailApList = details.split(",ap_")
	    for i in range(0,17):
	        print detailApList[i]
	    org_output_array_size = detailList[-1].split('=')[1];
	    print "Identified %s neighboring access points"%org_output_array_size
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] 1: SUCCESS";
            if org_ssidname != "" and org_ssidname != "OutOfService" and len(org_ssidname) <= 32:
	        tdkTestObj.setResultStatus("SUCCESS");
	        print "TEST STEP 2 : Get a valid neighboring AP"
		print "EXPECTED RESULT 2 : Should get a valid neighboring AP"
		print "ACTUAL RESULT 2 : Successfully got a valid neighboring AP"
	        print "ssid Name: ",org_ssidname;
	        #Get the result of execution
		print "[TEST EXECUTION RESULT] 2: SUCCESS";
	        #Prmitive test case which is associated to this Script
                tdkTestObj = obj.createTestStep('WIFIHAL_SetApScanFilter');
	        tdkTestObj.addParameter("apIndex", idx);
                tdkTestObj.addParameter("methodName", "setApScanFilter");
                tdkTestObj.addParameter("mode", 2);
                tdkTestObj.addParameter("essid", org_ssidname);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
	        if expectedresult in actualresult :
	            tdkTestObj.setResultStatus("SUCCESS");
	            print "TEST STEP 3: Set AccessPoint scan filter mode as WIFI_SCANFILTER_MODE_FIRST"
                    print "EXPECTED RESULT 3: wifi_setapscanfilter api call should be SUCCESS"
                    print "ACTUAL RESULT 3: Successfully called wifi_setapscanfilter "
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] 3 : SUCCESS";

		    tdkTestObj = obj.createTestStep('WIFIHAL_GetNeighboringWiFiDiagnosticResult2');
	            tdkTestObj.addParameter("radioIndex", idx);
	            expectedresult="SUCCESS";
	            tdkTestObj.executeTestCase(expectedresult);
	            actualresult = tdkTestObj.getResult();
	            details = tdkTestObj.getResultDetails();
	            if expectedresult in actualresult and details !="No neighbouring Accesspoints found by wifi_getNeighboringWiFiDiagnosticResult2"  :
	                tdkTestObj.setResultStatus("SUCCESS");
	                print "TEST STEP 4: Get the details of neighboring AP after calling wifi_setapscanfilter"
	                print "EXPECTED RESULT 4: Should successfully get the details of neighboring AP"
	                print "ACTUAL RESULT 4: neighboring AP found"
			print "Details: "
			details = details.split(":ap_")[1].strip();
	                detailList = details.split(",")
	                ssidname = details.split(",")[0].split("=")[1].strip()
	                detailApList = details.split(",ap_")
	                for i in range(0,17):
	                    print detailApList[i]
	                output_array_size = int(detailList[-1].split('=')[1]);
	                print "ssid Name: ",ssidname;
		        print "output_array_size : ",output_array_size;
		        #Get the result of execution
	                print "[TEST EXECUTION RESULT] 4: SUCCESS";
                        if ssidname == org_ssidname:
		            tdkTestObj.setResultStatus("SUCCESS");
	                    print "TEST STEP 5: Check whether WIFI_SCANFILTER_MODE_FIRST filter mode  is working"
		            print "EXPECTED RESULT 5: WIFI_SCANFILTER_MODE_FIRST filter mode should SUCCESS"
		            print" ACTUAL RESULT 5: WIFI_SCANFILTER_MODE_FIRST filter mode applied Successfully "
		            #Get the result of execution
	                    print "[TEST EXECUTION RESULT] 5: SUCCESS";
		        else:
		            tdkTestObj.setResultStatus("FAILURE");
	                    print "TEST STEP 5: Check whether WIFI_SCANFILTER_MODE_FIRST filter mode  is working "
		            print "EXPECTED RESULT 5: WIFI_SCANFILTER_MODE_FIRST filter mode should SUCCESS"
		            print" ACTUAL RESULT 5: WIFI_SCANFILTER_MODE_FIRST filter mode FAILED "
		            #Get the result of execution
	                    print "[TEST EXECUTION RESULT] 5: FAILURE";
		    else:
		        tdkTestObj.setResultStatus("FAILURE");
	                print "TEST STEP 4: Get the NeighboringWiFiDiagnosticResult after calling wifi_setapscanfilter"
	                print "EXPECTED RESULT 4: Should successfully get the NeighboringWiFiDiagnosticResult"
	                print "ACTUAL RESULT 4: No neighboring AP found"
	                print "Details: %s"%details
	                #Get the result of execution
	                print "[TEST EXECUTION RESULT] 4: FAILURE";
	        else:
	            tdkTestObj.setResultStatus("FAILURE");
	            print "TEST STEP 3: Set AccessPoint scan filter mode as WIFI_SCANFILTER_MODE_FIRST"
                    print "EXPECTED RESULT 3: wifi_setapscanfilter api call should be SUCCESS"
                    print "ACTUAL RESULT 3: Failed to call wifi_setapscanfilter with WIFI_SCANFILTER_MODE_FIRST mode"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] 3: FAILURE";
	    else:
	        tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 2 : Get a valid neighboring AP"
		print "EXPECTED RESULT 2 : Should get a valid neighboring AP"
		print "ACTUAL RESULT 2 : Failed to get a valid neighboring AP"
	        print "ssid Name: ",org_ssidname;
	        #Get the result of execution
		print "[TEST EXECUTION RESULT] 2: FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 1: Get the NeighboringWiFiDiagnosticResult"
	    print "EXPECTED RESULT 1: Should successfully get the NeighboringWiFiDiagnosticResult"
	    print "ACTUAL RESULT 1: Failed to get the NeighboringWiFiDiagnosticResult"
	    print "Details: %s"%details
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] 1: FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
