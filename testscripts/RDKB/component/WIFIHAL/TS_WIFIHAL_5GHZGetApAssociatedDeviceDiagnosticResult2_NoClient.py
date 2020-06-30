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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHZGetApAssociatedDeviceDiagnosticResult2_NoClient</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceDiagnosticResult2</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if wifi_getApAssociatedDeviceDiagnosticResult2() is returning success and empty buffer for 5GHZ when there are no associated devices</synopsis>
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
    <test_case_id>TC_WIFIHAL_374</test_case_id>
    <test_objective>Check if wifi_getApAssociatedDeviceDiagnosticResult2() is returning success and empty buffer for 5GHZ when there are no associated devices</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. 5GHZ WiFi client should not be connected to the DUT</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceDiagnosticResult2()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module
2. Invoke wifi_getApAssociatedDeviceDiagnosticResult2() and check its return values
3. Api return status should be true and it should return an empty data buffer
4. Unload WIFI hal module</automation_approch>
    <expected_output>wifi_getApAssociatedDeviceDiagnosticResult2() should return success and empty buffer when there are no associated devices</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHZGetApAssociatedDeviceDiagnosticResult2_NoClient</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio5 = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHZGetApAssociatedDeviceDiagnosticResult2_NoClient');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Validate wifi_getApAssociatedDeviceDiagnosticResult2() for 5GHZ
    tdkTestObjTemp, idx = getIndex(obj, radio5);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio5;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1:Invoke GetApAssociatedDeviceDiagnosticResult2 for 5GHZ"
        print "EXPECTED RESULT 1: GetApAssociatedDeviceDiagnosticResult2 for 5GHZ should return success status and empty buffer"
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult2');

        #TDK stub function for the hal api wifi_getApAssociatedDeviceDiagnosticResult2, will return failure when this api returns success and an empty buffer when no client is connected. Hence making the expected result as failure.
        expectedresult="FAILURE";
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        resultDetails = tdkTestObj.getResultDetails();
        print "resultDetails:",resultDetails;

        if expectedresult in actualresult and resultDetails == "wifi_getApAssociatedDeviceDiagnosticResult2 returned empty buffer":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: GetApAssociatedDeviceDiagnosticResult2 for 5GHZ returned success status and empty buffer"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1 : GetApAssociatedDeviceDiagnosticResult2 for 5GHZ returned failure"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
