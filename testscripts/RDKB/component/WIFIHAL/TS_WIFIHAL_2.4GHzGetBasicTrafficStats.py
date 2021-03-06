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
  <version>10</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzGetBasicTrafficStats</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetBasicTrafficStats</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get and check the BasicTrafficStats data using wifi_getBasicTrafficStats()</synopsis>
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
    <test_case_id>TC_WIFIHAL_283</test_case_id>
    <test_objective>Get and check the BasicTrafficStats data using wifi_getBasicTrafficStats()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.DUT should be connected with a WiFi client
2. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
3.TDK Agent should be in running state or invoke it through StartTdk.sh scrip</pre_requisite>
    <api_or_interface_used>wifi_getBasicTrafficStats()</api_or_interface_used>
    <input_parameters>ApIndex</input_parameters>
    <automation_approch>1. Load wifihal module
2.Invoke wifi_getApNumDevicesAssociated() to check the no: of associated devices
3. No: of associated devices should be greater than 0
3. Invoke wifi_getBasicTrafficStats() for 2.4G.
4. Check if the basic traffic stats values returned are greater than 0
5. Check if the associated device count returned in basic traffic stats is same as the value from wifi_getApNumDevicesAssociated() api
6. Unload wifihal module</automation_approch>
    <expected_output>Basic traffic stats values returned should be greater than 0</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetBasicTrafficStats</test_script>
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

radio = "2.4"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetBasicTrafficStats');

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
	getMethod = "getApNumDevicesAssociated"
	primitive = 'WIFIHAL_GetOrSetParamULongValue'
	tdkTestObj = obj.createTestStep(primitive);
	tdkTestObj.addParameter("radioIndex",radioIndex);
        tdkTestObj.addParameter("methodName",getMethod);
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
	    ApNumDevices = details.split(":")[1].strip();
	    if  ApNumDevices != "" and int(ApNumDevices) > 0:
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP 1: Get the number of Ap Associated Devices"
		print "EXPECTED RESULT 1: Should get the number of Ap Associated Devices as greater than 0"
		print "ACTUAL RESULT 1: Received the number of Ap Associated Devices as greater than 0"
		print "ApNumDevicesAssociated : %s"%ApNumDevices
		print "TEST EXECUTION RESULT 1: SUCCESS"

	        primitive = 'WIFIHAL_GetBasicTrafficStats'
	        tdkTestObj = obj.createTestStep(primitive);
	        tdkTestObj.addParameter("apIndex",radioIndex);
	        tdkTestObj.executeTestCase(expectedresult);
	        actualresult = tdkTestObj.getResult();
	        details = tdkTestObj.getResultDetails();
	        if expectedresult in actualresult:
                    trafficStats =  details.rstrip('\n').split('-')[1]
                    bytesSent = trafficStats.split(',')[0].split(' ')[2]
                    bytesReceived = trafficStats.split(',')[1].split(' ')[2]
                    packetsSent = trafficStats.split(',')[2].split(' ')[2]
                    packetsReceived = trafficStats.split(',')[3].split(' ')[2]
                    associations = trafficStats.split(',')[4].split(' ')[2].replace("\\n", "")

	            tdkTestObj.setResultStatus("SUCCESS");
	            print "TEST STEP 2: Get the Basic Traffic statistics for 2.4GHz";
	            print "EXPECTED RESULT 2: wifi_getBasicTrafficStats should return the basic traffic statistics for 2.4GHz";
	            print "ACTUAL RESULT 2: wifi_getBasicTrafficStats operation returned SUCCESS";
	            print "Actual result is :",details;
	            print "[TEST EXECUTION RESULT] 2: SUCCESS";

                    print "TEST STEP 3: Check if the Basic Traffic statistics values for 2.4GHz are greater than 0";
                    print "EXPECTED RESULT 3: Basic Traffic statistics values for 2.4GHz should be greater than 0";
                    if int(ApNumDevices) == int(associations) and int(bytesSent) >0 and int(bytesReceived) >0 and int(packetsSent) >0 and int(packetsReceived) >0 :
                        print "ACTUAL RESULT 3: Basic Traffic statistics values for 2.4GHz are greater than 0";
                        print "[TEST EXECUTION RESULT] 3: SUCCESS";
                    else:
                        print "ACTUAL RESULT 3: Basic Traffic statistics values for 2.4GHz are not greater than 0";
                        print "[TEST EXECUTION RESULT] 3: FAILURE";
	        else:
		    tdkTestObj.setResultStatus("FAILURE");
  		    print "TEST STEP 2: Get the Basic Traffic statistics for 2.4GHz";
		    print "EXPECTED RESULT 2: wifi_getBasicTrafficStats should return the basic traffic statistics for 2.4GHz";
		    print "ACTUAL RESULT 2: Failed to get the Basic Traffic statistics values for 2.4GHz";
		    print "Actual result is :",details;
		    print "[TEST EXECUTION RESULT] 2: FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 1: Get the number of Ap Associated Devices"
		print "EXPECTED RESULT 1: Should get the number of Ap Associated Devices as greater than 0"
		print "ACTUAL RESULT 1: Received number of Ap Associated Devices is not greater than 0"
		print "ApNumDevicesAssociated : %s"%ApNumDevices
		print "TEST EXECUTION RESULT 1: FAILURE"
	else:
            tdkTestObj.setResultStatus("FAILURE");
	    print "getApNumDevicesAssociated() call failed"
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
