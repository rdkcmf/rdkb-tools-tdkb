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
  <name>TS_WIFIHAL_6GHzIsApIsolationEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if Accesspoint isolation is enabled or not using wifi_getApIsolationEnable HAL API.</synopsis>
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
    <test_case_id>TC_WIFIHAL_660</test_case_id>
    <test_objective>Check if Accesspoint isolation is enabled or not using wifi_getApIsolationEnable HAL API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApIsolationEnable()</api_or_interface_used>
    <input_parameters>methodName : getApIsolationEnable
methodName : setApIsolationEnable</input_parameters>
    <automation_approch>1.Load the module
2.Get the Ap Isolation enable status using wifi_getApIsolationEnable
3.Toggle the value using wifi_setApIsolationEnable
4.Verify if set reflected using wifi_getApIsolationEnable
5.Revert the set value
6.Unload the module</automation_approch>
    <expected_output>wifi_getApIsolationEnable and wifi_setApIsolationEnable operations are expected to be suceesful</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzIsApIsolationEnabled</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzIsApIsolationEnabled');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzIsApIsolationEnabled');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in loadmodulestatus.upper():
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
	    getMethod = "getApIsolationEnable"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

	    if expectedresult in actualresult :
		tdkTestObj.setResultStatus("SUCCESS");
		enable = details.split(":")[1].strip()
		if "Enabled" in enable:
		    print "Access point Isolation is Enabled"
		    oldEnable = 1
		    newEnable = 0
		else:
		    print "Access point Isolation is Disabled"
		    oldEnable = 0
		    newEnable = 1

		setMethod = "setApIsolationEnable"
		#Toggle the enable status using set
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, newEnable, setMethod)

		if expectedresult in actualresult :
		    print "Enable state toggled using set"
		    # Get the New enable status
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

		    if expectedresult in actualresult and enable not in details.split(":")[1].strip():
			print "getApIsolationEnable Success, verified along with setApIsolationEnable() api"
			#Revert back to original Enable status
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, oldEnable, setMethod)

			if expectedresult in actualresult :
			    print "Enable status reverted back";
			else:
			    print "Couldn't revert enable status"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
			print "getApIsolationEnable() failed after set function"
			tdkTestObj.setResultStatus("FAILURE");
		else:
		    print "setApIsolationEnable() failed"
		    tdkTestObj.setResultStatus("FAILURE");
	    else:
		print "getApIsolationEnable() failed"
		tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
