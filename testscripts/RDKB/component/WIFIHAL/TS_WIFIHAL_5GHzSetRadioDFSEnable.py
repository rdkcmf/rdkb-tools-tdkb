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
  <version>5</version>
  <name>TS_WIFIHAL_5GHzSetRadioDFSEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check DFS support for 5GHZ using wifi_getRadioDfsSupport  (), set DFS status using wifi_setRadioDfsEnable() and verify with wifi_getRadioDfsEnable()</synopsis>
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
    <test_case_id>TC_WIFIHAL_12</test_case_id>
    <test_objective>Check DFS support using wifi_getRadioDfsSupport  (), set DFS status using wifi_setRadioDfsEnable() and verify with wifi_getRadioDfsEnable()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDfsSupport
wifi_setRadioDfsEnable()
wifi_getRadioDfEnable()</api_or_interface_used>
    <input_parameters>methodName   :   getRadioDfsEnable
methodName   :   setRadioDfsEnable
radioIndex        :    1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Check if DFS is supported using wifi_getRadioDfsSupport()
3. If supported, then using getRadioDfsEnable() get and save current DFS enable state. Else, exit the script
4.Toggle DFS enable state using setRadioDfsEnable()
5. Verify whether the set was success by getting the DFS enable state using getRadioDfsEnable()
6. Revert back to the initial DFS enable state
7. Unload wifihal module</automation_approch>
    <expected_output>If DFS is supported, setting DFS enable state using  setRadioDfsEnable() should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioDFSEnable</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioDFSEnable');

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
        getMethod = "getRadioDFSSupported"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

        if expectedresult in actualresult and "Enabled" in details.split(":")[1].strip():
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the device's 5GHZ DFS Support";
            print "EXPECTED RESULT 1: Should get the device's 5GHZ DFS Support";
            print "ACTUAL RESULT 1: DFS is supported by this device for 5GHZ";
            print "[TEST EXECUTION RESULT] 1: SUCCESS";

	    getMethod = "getRadioDFSEnable"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

	    if expectedresult in actualresult :
		enable = details.split(":")[1].strip()
		if "Enabled" in enable:
		    oldEnable = 1
		    newEnable = 0
		else:
		    oldEnable = 0
		    newEnable = 1

		setMethod = "setRadioDfsEnable"
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, setMethod)

		if expectedresult in actualresult :
		    print "Enable state toggled using set"
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

		    if expectedresult in actualresult and enable not in details.split(":")[1].strip():
			print "SetEnable Success, verified with getEnable() api"
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, oldEnable, setMethod)

			if expectedresult in actualresult :
			    print "Enable status reverted back";
			else:
			    print "Couldn't revert enable status"
		    else:
			print "Set validation with get api failed"
			tdkTestObj.setResultStatus("FAILURE");
		else:
		    print "wifi_setRadioDfsEnable() call failed"
		    tdkTestObj.setResultStatus("FAILURE");
	    else:
		print "wifi_getRadioDFSEnable() call failed"
		tdkTestObj.setResultStatus("FAILURE");

        elif expectedresult in actualresult and "Disabled" in details.split(":")[1].strip():
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the device's 5GHZ DFS Support";
            print "EXPECTED RESULT 1: Should get the device's 5GHZ DFS Support";
            print "ACTUAL RESULT 1: DFS is not supported by this device for 5GHZ";
            print "[TEST EXECUTION RESULT] 1: SUCCESS";

        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the device's 5GHZ DFS Support";
            print "EXPECTED RESULT 1: Should get the device's 5GHZ DFS Support";
            print "ACTUAL RESULT 1: Failed to get device's 5GHZ DFS Support status";
            print "[TEST EXECUTION RESULT] 1: FAILURE";

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
