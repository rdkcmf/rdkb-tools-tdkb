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
  <name>TS_mso_mgmt_hal_SetPodSeed_NullBuffer</name>
  <primitive_test_id/>
  <primitive_test_name>mso_mgmt_hal_SetMsoPodSeed</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the mso mgmt HAL API mso_set_pod_Seed by passing the NULL value for Pod Seed</synopsis>
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
    <test_case_id>TC_mso_mgmt_hal_7</test_case_id>
    <test_objective>To validate the Pod Seed using mso_set_pod_seed() by passing a NULL Value</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Braodband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mso_set_pod_seed</api_or_interface_used>
    <input_parameters>paramValue -password to be set
paramType - indicates whether to execute a positive or negative scenario.</input_parameters>
    <automation_approch>1.Load mso_mgmt_hal module
2.Pass the NULL value as ParamType to mso_set_pod_seed
3.Set should fail for the NULL value param
4.Unload mso_mgmt_hal module</automation_approch>
    <expected_output>Set function should fail when NULL value is passed as a parameter.</expected_output>
    <priority>High</priority>
    <test_stub_interface>MSO_MGMT_HAL</test_stub_interface>
    <test_script>TS_mso_mgmt_hal_SetPodSeed_NullBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mso_mgmt_hal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_mso_mgmt_hal_SetPodSeed_NullBuffer');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep("mso_mgmt_hal_SetMsoPodSeed");
    tdkTestObj.addParameter("paramType","NULL");
    expectedresult="FAILURE";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Status = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Set the Null POD Seed";
        print "EXPECTED RESULT 1: Should  not set the NULL Pod Seed";
        print "ACTUAL RESULT 1: Status of POD seed  validation is %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Set the POD Seed";
        print "EXPECTED RESULT 1:Should  not set the NULL POD Seed";
        print "ACTUAL RESULT 1: Status of POD Seed validation is %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("mso_mgmt_hal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

