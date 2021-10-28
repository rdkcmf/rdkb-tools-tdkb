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
  <name>TS_WIFIHAL_6GHzGetApAclDeviceNum</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the number of devices in the filter list for 6GHz radio using the HAL API wifi_getApAclDeviceNum().</synopsis>
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
    <test_case_id>TC_WIFIHAL_647</test_case_id>
    <test_objective>To get the number of devices in the filter list for 6GHz radio using the HAL API wifi_getApAclDeviceNum().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAclDeviceNum()</api_or_interface_used>
    <input_parameters>methodName : getApAclDeviceNum
apIndex : fetched from the platform property file</input_parameters>
    <automation_approch>1.Load the module.
2.Get the 6GHz access point index from the platform property file.
2.Get the ApAclDeviceNum using wifi_getApAclDeviceNum() API.
3.Return SUCCESS for non empty value, else FAILURE.
4.Unload module.</automation_approch>
    <expected_output>The number of devices connected to the access point should be retrieved successfully using the HAL API wifi_getApAclDeviceNum() for 6GHz.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApAclDeviceNum</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApAclDeviceNum');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApAclDeviceNum');

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
        getMethod = "getApAclDeviceNum"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

        if expectedresult in actualresult:
            deviceNum = details.split(":")[1].strip();
            print "\nTEST STEP 2: Get the number of devices in the filter list"
            print "EXPECTED RESULT 2: Should get the number of devices as a non empty value"

            if deviceNum != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Received the number of devices as a NON EMPTY value"
                print "Device number : %s"%deviceNum
                print "TEST EXECUTION RESULT: SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Received the number of devices as an EMPTY value"
                print "Device number : %s"%deviceNum
                print "TEST EXECUTION RESULT: FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "getApAclDeviceNum() call failed"

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

