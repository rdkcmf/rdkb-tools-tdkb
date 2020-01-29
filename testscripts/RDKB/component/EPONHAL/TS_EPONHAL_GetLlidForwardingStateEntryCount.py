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
  <name>TS_EPONHAL_GetLlidForwardingStateEntryCount</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetParamUlongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the LlidForwardingState entry count using dpoe_LlidForwardingStateGetEntryCount() and check if it is greater than 0</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_EPONHAL_3</test_case_id>
    <test_objective>Get the LlidForwardingState entry count using dpoe_LlidForwardingStateGetEntryCount() and check if it is greater than 0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_LlidForwardingStateGetEntryCount()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load eponhal module
2. Invoke dpoe_LlidForwardingStateGetEntryCount() and get the LlidForwardingState entry count
3. Check if the LlidForwardingState entry count is greater than 0
3. Unload eponhal module</automation_approch>
    <expected_output>The LlidForwardingState entry count retrieved using dpoe_LlidForwardingStateGetEntryCount() should be  greater than 0</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetLlidForwardingStateEntryCount</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetLlidForwardingStateEntryCount');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep('EPONHAL_GetParamUlongValue');
    tdkTestObj.addParameter("paramName","LlidForwardingStateGetEntryCount");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    resultDetails = " ";
    resultDetails = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and resultDetails != " " and int(resultDetails) > 0 :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the LlidForwardingStateEntryCount";
        print "EXPECTED RESULT 1: Should get the LlidForwardingStateEntryCount value as greater than 0";
        print "ACTUAL RESULT 1: The LlidForwardingStateEntryCount is %s" %resultDetails;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the LlidForwardingStateEntryCount";
        print "EXPECTED RESULT 1: Should get the LlidForwardingStateEntryCount value as greater than 0";
        print "ACTUAL RESULT 1: Failed to get the LlidForwardingStateEntryCount, Details : %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
