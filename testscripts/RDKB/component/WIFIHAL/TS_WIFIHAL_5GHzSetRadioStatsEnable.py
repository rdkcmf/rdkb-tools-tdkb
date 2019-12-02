##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WIFIHAL_5GHzSetRadioStatsEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test to enable/disable radio enable status using wifi_setRadioStatsEnable() api and verify using wifi_getRadioStatsEnable() for 5GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_300</test_case_id>
    <test_objective>Test to enable/disable radio enable status using wifi_setRadioStatsEnable() api and verify using wifi_getRadioStatsEnable() for 5GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioStatsEnable()
wifi_getRadioStatsEnable()</api_or_interface_used>
    <input_parameters>methodName="getRadioStatsEnable"/"setRadioStatsEnable"
radioIndex = 1
</input_parameters>
    <automation_approch>1.Load the module
2.Using WIFIHAL_GetOrSetParamStringValue, call wifi_getRadioStatsEnable()() API
3. Toggle the radio status using wifi_setRadioStatsEnable()
4. Check if the set function is success with get function
5.Unload the module.</automation_approch>
    <except_output>The radio enable status should be toggled </except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioStatsEnable</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioStatsEnable');

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
	    radioIndex = idx;
	    getMethod = "getRadioStatsEnable"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

	    if expectedresult in actualresult :
		enable = details.split(":")[1].strip()
		tdkTestObj.setResultStatus("SUCCESS");

		if "Enabled" in enable:
		    oldEnable = 1
		    newEnable = 0
		else:
		    oldEnable = 0
		    newEnable = 1

		setMethod = "setRadioStatsEnable"
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, setMethod)

		if expectedresult in actualresult :
		    print "Enable state toggled using set"

		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

		    if expectedresult in actualresult and enable not in details.split(":")[1].strip():
			print "SetEnable Success, verified with getEnable() api"
		    else:
			print "SetEnable is failed while verifying using getEnable()"
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, oldEnable, setMethod)

		    if expectedresult in actualresult :
			print "Reverted the radio enable status";
		    else:
			print "Failed to revert the enable status";

		else:
		    print "Failed to toggle the enable status";
	    else:
		print "Failed to get the radio enable status"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
