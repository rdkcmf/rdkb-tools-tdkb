##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_5GHzGetRadioTrafficStats2</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioTrafficStats2</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the details of Radio traffic statistics info for 5 GHz </synopsis>
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
    <test_case_id>TC_WIFIHAL_264</test_case_id>
    <test_objective>To get the details of Radio traffic statistics</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioTrafficStats2()
</api_or_interface_used>
    <input_parameters>methodName : wifi_getRadioTrafficStats2
</input_parameters>
    <automation_approch>1. Load wifihal module
3. Using WIFIHAL_GetRadioTrafficStats2 invoke wifi_getRadioTrafficStats2() to see if the Radio traffic statistics info is getting or not . If available return SUCCESS and else exit the script with FAILURE.
4. Unload wifihal module</automation_approch>
    <except_output>Get the details of Radio traffic statistics info </except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioTrafficStats2</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioTrafficStats2');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Getting the Radio Traffic state Info
    expectedresult="SUCCESS";
    radioIndex = 1;
    primitive = 'WIFIHAL_GetRadioTrafficStats2'
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex",radioIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the RadioTrafficStats for 5GHz";
        print "EXPECTED RESULT 1: wifi_getRadioTrafficStats2 should return the Radio traffic statistics for 5GHz";
        print "ACTUAL RESULT 1: wifi_getRadioTrafficStats2 operation returned SUCCESS";
        print "Actual result is :",details;
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the RadioTrafficStats for 5GHz";
        print "EXPECTED RESULT 1: wifi_getRadioTrafficStats2 should return the Radio traffic statistics for 5GHz";
        print "ACTUAL RESULT 1: Failed to get the values for 5GHz";
        print "Actual result is :",details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");


