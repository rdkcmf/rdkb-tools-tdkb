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
  <name>TS_WIFIHAL_6GHzGetApWpsConfigurationState</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the access point WpsConfigurationState for 6GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_652</test_case_id>
    <test_objective>To get the access point WpsConfigurationState for 6GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsConfigurationState()</api_or_interface_used>
    <input_parameters>methodName : getApWpsConfigurationState</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getApWpsConfigurationState()
3. The string returned should be either "Configured" or "Not configured"
4. Depending upon the values returned SUCCESS else return FAILURE
5. Unload wifihal module</automation_approch>
    <expected_output>String output as 'Configured' or 'Not configured'</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApWpsConfigurationState</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApWpsConfigurationState');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApWpsConfigurationState');
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, idx = getApIndexfor6G(sysobj, TDK_PATH);

    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	    expectedresult="SUCCESS";
	    apIndex = idx
	    getMethod = "getApWpsConfigurationState"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'
	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
	    possibleConfigs = ["Configured","Not configured"];
	    if expectedresult in actualresult:
		configState = details.split(":")[1].strip()
		if configState in possibleConfigs:
		    print "EXPECTED OUTPUT: Output string should be either 'Configured' or 'Not configured'"
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "ApWpsConfigurationState: %s"%configState;
		    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
		    print "EXPECTED OUTPUT: Output string should be either 'Configured' or 'Not configured'"
		    tdkTestObj.setResultStatus("FAILURE");
		    print "ApWpsConfigurationState: %s"%configState;
		    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		print "wifi_getApWpsConfigurationState function call failed";
		tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");