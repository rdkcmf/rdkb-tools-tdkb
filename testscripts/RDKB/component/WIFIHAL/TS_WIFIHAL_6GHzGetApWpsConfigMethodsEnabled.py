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
  <name>TS_WIFIHAL_6GHzGetApWpsConfigMethodsEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the WPS configMethod Enabled values for 6GHz radio using wifi_getApWpsConfigMethodsEnabled HAL API and validate the same.</synopsis>
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
    <test_case_id>TC_WIFIHAL_658</test_case_id>
    <test_objective>To get the WPS configMethod Enabled values for 6GHz radio using wifi_getApWpsConfigMethodsEnabled HAL API and validate the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsConfigMethodsEnabled()</api_or_interface_used>
    <input_parameters>methodName   :   getApWpsConfigMethodsEnabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the  config method  enabled using wifi_getApWpsConfigMethodsEnabled
3.Get the config methods supported using wifi_getApWpsConfigMethodsSupported
4.Check if the method enabled is one among the supported methods
4.Unload the module</automation_approch>
    <expected_output>WPS Config method enable ,should be one among the supported config methods</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApWpsConfigMethodsEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
radio = "6G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApWpsConfigMethodsEnabled');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApWpsConfigMethodsEnabled');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()) :
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, idx = getApIndexfor6G(sysobj, TDK_PATH);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	    expectedresult="SUCCESS";
	    apIndex = idx
	    getMethod = "getApWpsConfigMethodsEnabled"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
	    print "\n";
	    #Calling the method from wifiUtility to execute test case and set result status for the test. Fetching the WPS Config Mode Supported.
	    tdkTestObj1, actualresult1, details1 = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", "getApWpsConfigMethodsSupported")
	    print "\n";
	    if expectedresult in actualresult and expectedresult in actualresult1:
		supportedWpsConfigModes = details1.split(":")[1].strip()
		actualSupportedModes = details.split(":")[1].strip()
		for item in list(actualSupportedModes.split(",")):
		    if item in list(supportedWpsConfigModes.split(",")):
			print "\ngetApWpsConfigMethodsEnabled function successful  %s"%details
			tdkTestObj.setResultStatus("SUCCESS");
			print "\nTEST STEP 1: Validate the wifi_getApWpsConfigMethodsEnabled Function";
			print "EXPECTED RESULT 1: wifi_getApWpsConfigMethodsEnabled should return a string comma separated list of the enabled WPS config methods";
			print "ACTUAL RESULT 1: APWPS config methods string received %s"%item;
			print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
			print "\ngetApWpsConfigMethodsEnabled() failed %s"%details
			tdkTestObj.setResultStatus("FAILURE");
			print "\nTEST STEP 1: Validate the wifi_getApWpsConfigMethodsEnabled Function";
			print "EXPECTED RESULT 1: wifi_getApWpsConfigMethodsEnabled should return a string comma separated list of the enabled WPS config methods";
			print "ACTUAL RESULT 1: Failed to receive ApWpsconfigMethod string %s"%item;
			print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		print "getApWpsConfigMethodsEnabled() failed"
		tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
