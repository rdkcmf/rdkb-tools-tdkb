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
  <version>3</version>
  <name>TS_WIFIHAL_6GHzGetSSIDTrafficStats2</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetSSIDTrafficStats2</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To retrieve the SSID traffic statistics info for 6GHz radio with the HAL API wifi_getSSIDTrafficStats2().</synopsis>
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
    <test_case_id>TC_WIFIHAL_637</test_case_id>
    <test_objective>To retrieve the SSID traffic statistics info for 6GHz radio with the HAL API wifi_getSSIDTrafficStats2().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSSIDTrafficStats2()</api_or_interface_used>
    <input_parameters>apIndex : fetched from the platform property file
</input_parameters>
    <automation_approch>1.Load the module
2.Get the 6GHz access point index from the platform properties file.
3.Using primitive test WIFIHAL_GetSSIDTrafficStats2 call the api wifi_getSSIDTrafficStats2()
4.Parse the return values and check if they are all non empty
5. If the api call fails, return FAILURE, else return SUCESS
6.Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_getSSIDTrafficStats2() should retrieve the SSID Traffic Statistics for 6GHz successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetSSIDTrafficStats2</test_script>
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
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetSSIDTrafficStats2');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetSSIDTrafficStats2');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS";
    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        primitive = 'WIFIHAL_GetSSIDTrafficStats2'
        tdkTestObj = obj.createTestStep(primitive);
        tdkTestObj.addParameter("radioIndex",apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2: Get the SSID traffic statistics info for 6GHz";
        print "EXPECTED RESULT 2: wifi_getSSIDTrafficStats2 should return the SSID traffic statistics for 6GHz";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: wifi_getSSIDTrafficStats2 operation returned SUCCESS";
            print "SSID Traffic Stats Info : ";
            detailList = details.split(",")
            for i in detailList:
                print i;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: wifi_getSSIDTrafficStats2 operation returned FAILURE";
            print "SSID Traffic Stats Info : ",details;
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

