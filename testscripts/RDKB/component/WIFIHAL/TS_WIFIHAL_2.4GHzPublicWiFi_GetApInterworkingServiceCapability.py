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
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_GetApInterworkingServiceCapability</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the HAL API wifi_getApInterworkingServiceCapability for 2.4GHz Public WiFi  and check if the Interworking Service Capability is enabled.</synopsis>
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
    <test_case_id>TC_WIFIHAL_557</test_case_id>
    <test_objective>To invoke the HAL API wifi_getApInterworkingServiceCapability  for 2.4GHz Public WiFi and check if the Interworking Service Capability is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamBoolValue</api_or_interface_used>
    <input_parameters>methodname : getApInterworkingServiceCapability
apIndex : 8</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Invoke the HAL API wifi_getApInterworkingServiceCapability() for 2.4GHz Public WiFi. If it is enabled return Success else return Failure.
3. Validation of  the result is done within the python script and send the result status to Test Manager.
4. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from the WIFIHAL Stub.
5. Unload the module</automation_approch>
    <expected_output>wifi_getApInterworkingServiceCapability() HAL API should return the Interworking Service Capability as Enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_GetApInterworkingServiceCapability</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
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
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_GetApInterworkingServiceCapability');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    print "2.4GHz Public WiFi index : %s" %apIndex_2G_Public_Wifi;
    apIndex = apIndex_2G_Public_Wifi;

    print "TEST STEP 1: Invoke the wifi_getApInterworkingServiceCapability api for 2.4GHz Public WiFi";
    print "EXPECTED RESULT 1:Invocation of wifi_getApInterworkingServiceCapability should be success";
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
    tdkTestObj.addParameter("methodName","getApInterworkingServiceCapability")
    tdkTestObj.addParameter("radioIndex", apIndex)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Invocation of wifi_getApInterworkingServiceCapability was success.";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "TEST STEP 2: Check if value returned by wifi_getApInterworkingServiceCapability api is Enabled";
        print "EXPECTED RESULT 2 : The value returned by wifi_getApInterworkingServiceEnable api should be Enabled";
        enable= details.split(":")[1].strip()

        if "Enabled" in enable :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: ApInterworkingServiceCapability = %s" %enable;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: ApInterworkingServiceCapability = %s" %enable;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

