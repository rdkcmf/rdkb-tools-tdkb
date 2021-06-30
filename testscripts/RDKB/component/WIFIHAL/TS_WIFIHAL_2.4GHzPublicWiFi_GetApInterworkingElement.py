##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_GetApInterworkingElement</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetApInterworkingElement</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To invoke wifi_getApInterworkingElement() HAL API successfully and fetch the Interworking element details.</synopsis>
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
    <test_case_id>TC_WIFIHAL_555</test_case_id>
    <test_objective>To invoke wifi_getApInterworkingElement() HAL API successfully for 2.4GHz Public WiFi and fetch the Interworking element details.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetApInterworkingElement</api_or_interface_used>
    <input_parameters>apIndex : 8</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Invoke wifi_getApInterworkingElement() for 2.4GHz Public WiFi and get the element details.
3. The GET operation should be success
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from the WIFIHAL Stub.
6. Unload the module</automation_approch>
    <expected_output>wifi_getApInterworkingElement() HAL API is invoked for 2.4GHz Public WiFi and  Interworking element details are fetched successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_GetApInterworkingElement</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_GetApInterworkingElement');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    print "2.4GHz Public WiFi index : %s" %apIndex_2G_Public_Wifi;
    apIndex = apIndex_2G_Public_Wifi;

    primitive = 'WIFIHAL_GetApInterworkingElement'
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex",apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        print "TEST STEP 1: Invoke the wifi api wifi_getApInterworkingElement()";
        print "EXPECTED RESULT 1: Should succeesully invoke wifi_getApInterworkingElement()";
        print "ACTUAL RESULT 1: wifi_getApInterworkingElement() invoked successfully";
        print "TEST EXECUTION RESULT 1: SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        if details != " ":
            print "TEST STEP 2: Get the 2.4GHz Public WiFi Access Point InterworkingElement details";
            print "EXPECTED RESULT 2: Should get the Access Point InterworkingElement details successfully";
            print "ACTUAL RESULT 2: The Access Point InterworkingElement details are : %s"%details;
            print "TEST EXECUTION RESULT 2: SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 2: Get the 2.4GHz Public WiFi Access Point InterworkingElement details";
            print "EXPECTED RESULT 2: Should get the Access Point InterworkingElement details successfully";
            print "ACTUAL RESULT 2: The Access Point InterworkingElement details are not obtained :%s"%details;
            print "TEST EXECUTION RESULT 2: FAILURE";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1: Invoke the wifi api wifi_getApInterworkingElement()";
        print "EXPECTED RESULT 1: Should succeesully invoke wifi_getApInterworkingElement()";
        print "ACTUAL RESULT 1: wifi_getApInterworkingElement() is not invoked successfully";
        print "TEST EXECUTION RESULT 1: FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

