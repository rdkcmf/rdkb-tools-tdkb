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
  <version>4</version>
  <name>TS_EPONHAL_GetOnuId</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetOnuId</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the ONU id using dpoe_getOnuId() and check if it returns a non-empty onu id</synopsis>
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
    <test_case_id>TC_EPONHAL_6</test_case_id>
    <test_objective>Get the ONU id using dpoe_getOnuId() and check if it returns a valid MAC address</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_getOnuId()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load eponhal module
2. Invoke dpoe_getOnuId() and get the ONU Id
3. Check if the ONU id is a valid MAC address
3. Unload eponhal module</automation_approch>
    <expected_output>dpoe_getOnuId() should return a valid MAC address as ONU id</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetOnuId</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetOnuId');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep('EPONHAL_GetOnuId');
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    resultDetails = " ";
    resultDetails = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult and re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", resultDetails.lower()) :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the ONU Id";
        print "EXPECTED RESULT 1: Should get the onu id as a valid MAC";
        print "ACTUAL RESULT 1: The ONU Id is %s" %resultDetails;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the ONU Id";
        print "EXPECTED RESULT 1: Should get the onu id as a valid MAC";
        print "ACTUAL RESULT 1: Failed to get the ONU Id, Details : %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
