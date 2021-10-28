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
  <name>TS_WIFIHAL_6GHzGetApAclDevices</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAclDevices</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the list of ApAcl devices associated with the device for 6GHz radio using the HAL API wifi_getApAclDevices().</synopsis>
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
    <test_case_id>TC_WIFIHAL_648</test_case_id>
    <test_objective>To get the list of ApAcl devices associated with the device for 6GHz radio using the HAL API wifi_getApAclDevices().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAclDevices()</api_or_interface_used>
    <input_parameters>methodName : getApAclDevices
apIndex : fetched from platform property file</input_parameters>
    <automation_approch>1.Load the module.
2.Get the 6GHz access point index from the platform property file of the device.
3.Invoke the HAL API wifi_getApAclDevices() and retrieve the ApAclDevices.
4.Store the mac address in a array variable.
5.Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_getApAclDevices() should successfully retrieve the MAC Addresses of the acl devices for 6GHz access point.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApAclDevices</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApAclDevices');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApAclDevices');

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
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
        tdkTestObj.addParameter("apIndex",apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "\nDetails: ",details;
        print "\nTEST STEP 2 : Get the Acl Devices using the HAL API wifi_getApAclDevices"
        print "EXPECTED RESULT 2: Should get the list of acl devices successfully"

        if expectedresult in actualresult:
            macAddress= [];
            macAddress = details.split(";")[1].split("n")

            for i in range(len(macAddress)):
                macAddress[i] =  macAddress[i].replace("\\", '')

            if '' in macAddress:
                macAddress.remove('')
            print "ACTUAL RESULT 2: List of Acl Devices MAC Address:",macAddress
            print "TEST EXECUTION RESULT :SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");
        else:
            print "ACTUAL RESULT 2: wifi_getApAclDevices call failed"
            print "TEST EXECUTION RESULT :FAILURE"
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

