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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_WIFIHAL_6GHzGetRadioChannelStats</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioChannelStats</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To retrieve the radio channel stats info using the HAL API wifi_getRadioChannelStats() for 6GHz radio.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_636</test_case_id>
    <test_objective>To retrieve the radio channel stats info using the HAL API wifi_getRadioChannelStats() for 6GHz radio.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioChannelStats()</api_or_interface_used>
    <input_parameters>radioIndex : index corresponding to 6G radio</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the radio channel stats for 6G radio using the HAL API wifi_getRadioChannelStats().
3. Unload wifihal module</automation_approch>
    <expected_output>The Radio Channel Stats details should be retrieved successfully using the HAL API wifi_getRadioChannelStats() for 6GHz.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioChannelStats</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioChannelStats');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned

    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        primitive = 'WIFIHAL_GetRadioChannelStats'
        tdkTestObj = obj.createTestStep(primitive);
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "TEST STEP 1: Get the Radio channel statistics info for 6GHz";
        print "EXPECTED RESULT 1: wifi_getRadioChannelStats should return the radio channel statistics for 6GHz";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: wifi_getRadioChannelStats operation returned SUCCESS";
            print "Radio Channel Stats Info : ",details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: wifi_getRadioChannelStats operation returned FAILURE";
            print "Radio Channel Stats Info : ",details;
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");

