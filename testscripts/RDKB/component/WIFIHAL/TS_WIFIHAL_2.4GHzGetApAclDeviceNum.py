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
  <name>TS_WIFIHAL_2.4GHzGetApAclDeviceNum</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the number of devices in the filter list for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_253</test_case_id>
    <test_objective>To get the number of devices in the filter list for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAclDeviceNum()</api_or_interface_used>
    <input_parameters>methodName : getApAclDeviceNum
radioIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Get the ApAclDeviceNum using wifi_getApAclDeviceNum() API.
3.Return SUCCESS for non empty value,else FAILURE.
4.Unload module.</automation_approch>
    <except_output>Get the number of devices in the filter list for 2.4GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAclDeviceNum</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAclDeviceNum');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS"
    radioIndex = 0
    getMethod = "getApAclDeviceNum"
    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult:
	deviceNum = details.split(":")[1].strip();
	if deviceNum != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Get the number of devices in the filter list"
            print "EXPECTED RESULT : Should get the number of devices as a non empty value"
            print "ACTUAL RESULT : Received the number of devices as a NON EMPTY value"
	    print "Device number : %s"%deviceNum
	    print "TEST EXECUTION RESULT: SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the number of devices in the filter list"
            print "EXPECTED RESULT : Should get the number of devices as a non empty value"
            print "ACTUAL RESULT : Received the number of devices as an EMPTY value"
	    print "Device number : %s"%deviceNum
	    print "TEST EXECUTION RESULT: FAILURE"
    else:
	tdkTestObj.setResultStatus("FAILURE");
	print "getApAclDeviceNum() call failed"
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

