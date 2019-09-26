##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzKickApAclAssociatedDevices</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test to remove all the existing connection from the associated device by using wifi_kickApAclAssociatedDevices () api by checking whether the return status is SUCCESS for 2.4 GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_265</test_case_id>
    <test_objective>Test to remove all the existing connection from the associated device by using wifi_kickApAclAssociatedDevices () api by checking whether the return status is SUCCESS for 2.4 GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.We need to check the Disassociation log to check whether all existing connections are removed. But this disassociation log is not consistent across platforms, we have restricted our validation to check only the return status of the API
    2.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
3.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_kickApAclAssociatedDevices()</api_or_interface_used>
    <input_parameters>methodName : kickApAclAssociatedDevices
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
4. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_kickApAclAssociatedDevices() and enable the kick for devices on acl black list
5.Check the return status of the api and pass the script if the status is SUCCESS and fail if the return status is FAILED.
6. Unload wifihal module</automation_approch>
    <except_output></except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzKickApAclAssociatedDevices</test_script>
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzKickApAclAssociatedDevices');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Calling primitive WIFIHAL_GetOrSetParamBoolValue that in turn will call wifi_kickApAclAssociatedDevices() and remove all existing connection. 
    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "kickApAclAssociatedDevices"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    newEnable = 1
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, getMethod)

    if expectedresult in actualresult :
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Remove the all existing wifi connection associated with this device for 2.4GHz"
       print "EXPECTED RESULT 1: The api wifi_kickApAclAssociatedDevices() should return SUCCESS for 2.4 GHz"
       print "ACTUAL RESULT 1: The api wifi_kickApAclAssociatedDevices() returned  SUCCESS for 2.4 GHz"
       print "TEST EXECUTION RESULT : SUCCESS"
       print "Details is",details
    else:
       tdkTestObj.setResultStatus("FAILURE");
       print "TEST STEP 1: Remove the all existing wifi connection associated with this device for 2.4GHz"
       print "EXPECTED RESULT 1: The api wifi_kickApAclAssociatedDevices() should return SUCCESS for 2.4 GHz"
       print "ACTUAL RESULT 1: The api wifi_kickApAclAssociatedDevices() returned  FAILURE for 2.4 GHz"
       print "TEST EXECUTION RESULT : FAILURE"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");


