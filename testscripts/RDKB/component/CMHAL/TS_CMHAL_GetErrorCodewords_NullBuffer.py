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
  <name>TS_CMHAL_GetErrorCodewords_NullBuffer</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetErrorCodeWords</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the api call to docsis_GetErrorCodewords fails when a null buffer is passed</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TS_CMHAL_88</test_case_id>
    <test_objective>This test case is to check if the api call to docsis_GetErrorCodewords fails when a null buffer is passed</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CMHAL_GetErrorCodeWords</api_or_interface_used>
    <input_parameters>paramType -NULL</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Call the docsis_GetErrorCodewords api  with NULL buffer
3. The test should return FAILURE on passing NULL buffer.
4. Unload cmhal module</automation_approch>
    <expected_output>The api  call should fail when a Null buffer is passed
</expected_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_GetErrorCodewords_NullBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetErrorCodewords_NullBuffer');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetErrorCodeWords");
    tdkTestObj.addParameter("flag",1);
    expectedresult="FAILURE";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the GetErrorCodewords with null buffer";
        print "EXPECTED RESULT 1: Should not get the GetErrorCodewords with null buffer";
        print "ACTUAL RESULT 1: api call failed ";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the GetErrorCodewords with null buffer";
        print "EXPECTED RESULT 1: Should not get the GetErrorCodewords with null buffer"
        print "ACTUAL RESULT 1 : api call success";
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cmhal");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
