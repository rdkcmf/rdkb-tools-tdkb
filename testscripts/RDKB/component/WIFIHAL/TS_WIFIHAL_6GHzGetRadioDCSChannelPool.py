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
  <version>1</version>
  <name>TS_WIFIHAL_6GHzGetRadioDCSChannelPool</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRadioDCSChannelPool() to retrieve the DCS channel pool</synopsis>
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
    <test_case_id>TC_WIFIHAL_682</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRadioDCSChannelPool() to retrieve the DCS channel pool</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDCSChannelPool()</api_or_interface_used>
    <input_parameters>methodname : getRadioDCSChannelPool
radioIndex : 6G radio index</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getRadioDCSChannelPool() for 6G radio and check if the length of the API output string is less that 256.
3. Unload the modules.</automation_approch>
    <expected_output>The HAL API wifi_getRadioDCSChannelPool() to retrieve the DCS channel pool should be invoked successfully and the API output string length should be less than 256.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioDCSChannelPool</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioDCSChannelPool');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamStringValue');
        tdkTestObj.addParameter("methodName","getRadioDCSChannelPool");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1 : Invoke the HAL API wifi_getRadioDCSChannelPool for 6G radio";
        print "EXPECTED RESULT 1 : The HAL API wifi_getRadioDCSChannelPool should be invoked successfully";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: wifi_getRadioDCSChannelPool invocation success, Details : %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
            dcsChannelNumber = details.split(":")[1].strip();

            #Check if the DCS Channel Pool has a maximum length of 256
            print "\nTEST STEP 2: Validate the output of wifi_getRadioDCSChannelPool API";
            print "EXPECTED RESULT 2: wifi_getRadioDCSChannelPool should return a string value of length less than 256";

            if len(dcsChannelNumber) <= 256:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: DCS channel Pool string received is of the expected length : %s"%dcsChannelNumber;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: DCS Channel Pool string received is not of the expected length : %s"%dcsChannelNumber;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: wifi_getRadioDCSChannelPool invocation failed, Details : %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
