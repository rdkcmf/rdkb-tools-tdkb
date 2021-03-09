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
  <name>TS_WIFIHAL_5GHzGetSoftBlockWaitingTime</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To query wifi_getSoftBlockWaitingTime api and check whether expected Waiting time is received</synopsis>
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
    <test_case_id>TC_WIFIHAL_472</test_case_id>
    <test_objective>This test case is to query Soft Block Waiting Time and check whether  expected Waiting time is received</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSoftBlockWaitingTime</api_or_interface_used>
    <input_parameters>radioIndex</input_parameters>
    <automation_approch>1.Load wifihal module
2.Query the wifi_getSoftBlockWaitingTime check if the api call is success
3.Check if the Soft Block Waiting Time is a positive integer
4.Unload the module</automation_approch>
    <expected_output>wifi_getSoftBlockWaitingTime api call should be success and expected Soft Block Waiting Time has to be received</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetSoftBlockWaitingTime</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
radio = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetSoftBlockWaitingTime');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        getMethod = "getSoftBlockWaitingTime"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'

        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details =details.split(":")[1];
            details = int(details.replace("\\n", "").strip());
            if details >= 0 :
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 2: Check if the current Soft Block Waiting Time is a positive integer value "
               print "EXPECTED RESULT 2: Should get the Soft Block Waiting Time as a positive integer value"
               print "ACTUAL RESULT 2: The current Soft Block Waiting Time is :",details;
               print "TEST EXECUTION RESULT : SUCCESS";
            else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2: Check if the current Soft Block Waiting Time is a positive integer value "
               print "EXPECTED RESULT 2: Should get the Soft Block Waiting Time as a positive integer value"
               print "ACTUAL RESULT 2: The current Soft Block Waiting Time is :",details;
               print "TEST EXECUTION RESULT : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
