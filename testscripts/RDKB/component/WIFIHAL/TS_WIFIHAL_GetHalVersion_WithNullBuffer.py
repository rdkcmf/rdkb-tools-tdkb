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
  <version>3</version>
  <name>TS_WIFIHAL_GetHalVersion_WithNullBuffer</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether the null pointer handling is done for the api wifi_getHalVersion</synopsis>
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
    <test_case_id>TC_WIFIHAL_408</test_case_id>
    <test_objective>This test case is to check whether the null pointer handling is done for the api wifi_getHalVersion</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamStringValue</api_or_interface_used>
    <input_parameters>methodName
radioindex
paramType</input_parameters>
    <automation_approch>1.Load wifihal module
2.Query wifi_getHalVersion api with a NULL value
3.The test result is success if the api fails else its a failure case
4.Unload the Module</automation_approch>
    <expected_output>with a NULL value passed wifi_getHalVersion api should fail </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_GetHalVersion_WithNullBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio = ["2.4G","5G"]
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetHalVersion_WithNullBuffer');
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    for item in radio:
        tdkTestObjTemp, idx = getIndex(obj, item);

        if idx == -1:
           print "Failed to get radio index for radio %s\n" %radio;
           tdkTestObjTemp.setResultStatus("FAILURE");
        else:
            print"*************************************";
            print "Querying the api for apindex%d" %idx;
            print"**************************************";
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            tdkTestObj.addParameter("methodName","getHalVersion");
            tdkTestObj.addParameter("radioIndex",idx);
            tdkTestObj.addParameter("paramType","NULL");
            expectedresult="FAILURE";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 1: Query the wifi_getHalVersion api with Null Buffer";
               print "EXPECTED RESULT 1: API call should fail with Null Buffer";
               print "ACTUAL RESULT 1: %s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1:  Query the wifi_getHalVersion api with Null Buffer";
                print "EXPECTED RESULT 1: API call should fail with Null Buffer";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
