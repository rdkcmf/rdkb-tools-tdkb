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
  <name>TS_WIFIHAL_5GHzSetApWpsEnrolleePin</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the ApWpsEnrolleePin for 5GHz</synopsis>
  <groups_id/>
  <execution_time>4</execution_time>
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
    <test_case_id>TC_WIFIHAL_193</test_case_id>
    <test_objective>To set the ApWpsEnrolleePin for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApWpsEnrolleePin()</api_or_interface_used>
    <input_parameters>methodName : setApWpsEnrolleePin
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_setApWpsEnrolleePin() and set a pin
3. Depending upon the return status, return SUCCESS or FAILURE
4. Unload wifihal module</automation_approch>
    <except_output>wifi_setApWpsEnrolleePin should return SUCCESS</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApWpsEnrolleePin</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApWpsEnrolleePin');

def setEnrolleepin(radioIndex):
    expectedresult = "SUCCESS"

    setMethod = "setApWpsEnrolleePin"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    setPIN = "12345670"

    print "Invoke setApWpsEnrolleePin to set the enrollee pin 12345670 for WPS"
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setPIN, setMethod)

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Set the ApWpsEnrolleePin as 12345670"
        print "EXPECTED RESULT : Set operation should return SUCCESS"
        print "ACTUAL RESULT : Set operation returned SUCCESS"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Set the ApWpsEnrolleePin"
        print "EXPECTED RESULT : Set operation should return SUCCESS"
        print "ACTUAL RESULT : Set operation returned FAILURE"

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
	    apIndex = idx;
	    getMethod = "getApWpsEnable"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

	    if expectedresult in actualresult :
		tdkTestObj.setResultStatus("SUCCESS");
		enable = details.split(":")[1].strip()
		if "Enabled" in enable:
		    print "Access point WPS is enabled"
		    setEnrolleepin(apIndex);
		else:
		    print "Access point WPS is Disabled"
		    oldEnable = 0
		    newEnable = 1
		    setMethod = "setApWpsEnable"
		    print "Invoke setApWpsEnable() to enable WPS"
		    #Toggle the enable status using set
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, newEnable, setMethod)

		    if expectedresult in actualresult :
			tdkTestObj.setResultStatus("SUCCESS");
			print "Access point WPS is enabled"
			time.sleep(20);
			getMethod = "getApWpsEnable"
			primitive = 'WIFIHAL_GetOrSetParamBoolValue'
			print "Invoke getApWpsEnable() to get WPS"
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

			if expectedresult in actualresult :
			    tdkTestObj.setResultStatus("SUCCESS");
			    enable = details.split(":")[1].strip()
			    print "AP WPS Status:",enable;
			    if "Enabled" in enable:
				print "Access point WPS is enabled"
				setEnrolleepin(apIndex);
			    else:
				print "setApWpsEnable has returned false success"
				tdkTestObj.setResultStatus("FAILURE");
			else:
			    print "getApWpsEnable operation failed"
			    tdkTestObj.setResultStatus("FAILURE");
			#revert the WPS to initial value
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, oldEnable, setMethod)
			if expectedresult in actualresult :
			    print "WPS is reverted back to initial value"
			    tdkTestObj.setResultStatus("SUCCESS");
			else:
			    print "Unable to revert WPS to initial value"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "Unable to enable WPS"
	    else:
		print "getApWpsEnable operation failed"
		tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";



