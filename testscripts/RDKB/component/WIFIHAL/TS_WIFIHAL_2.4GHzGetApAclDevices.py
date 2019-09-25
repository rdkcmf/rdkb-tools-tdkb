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
  <version>7</version>
  <name>TS_WIFIHAL_2.4GHzGetApAclDevices</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAclDevices</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get List of Acl Devices associated with particular apIndex value and the number of devices in that list at radioIndex 2.4GHz.</synopsis>
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
    <test_case_id>TS_WIFIHAL_338</test_case_id>
    <test_objective>get the list of acl devices associated with DUT.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAclDevices()</api_or_interface_used>
    <input_parameters>methodName : getApAclDevices
apIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Get the list of ApAcl devices and  using the wifi_getApAclDevices() API.
3.Store the mac address in a array variable.
4.Unload the module.</automation_approch>
    <except_output>should get the mac addresses of the acl devices</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAclDevices</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>nil</remarks>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAclDevices');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    #Calling the method to execute wifi_getApAclDevices()
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
    tdkTestObj.addParameter("apIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Execution Details: ",details;
    if expectedresult in actualresult:
        macAddress= [];
        macAddress = details.split(";")[1].split("n")
        for i in range(len(macAddress)):
            macAddress[i] =  macAddress[i].replace("\\", '')
        if '' in macAddress:
            macAddress.remove('')
        print "TEST STEP: Get the Acl Devices"
        print "EXPECTED RESULT: Should get the list of acl devices"
        print "List of Acl Devices MAC Address:",macAddress
        print "TEST EXECUTION RESULT :SUCCESS"
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "TEST STEP: Get the Acl Devices List"
        print "EXPECTED RESULT: Should get the total list of associated devices"
        print "ACTUAL RESULT : wifi_getApAclDevices call failed"
        print "TEST EXECUTION RESULT :FAILURE"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
