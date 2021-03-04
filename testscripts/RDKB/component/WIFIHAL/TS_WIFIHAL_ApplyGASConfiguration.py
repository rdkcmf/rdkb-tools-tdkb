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
  <name>TS_WIFIHAL_ApplyGASConfiguration</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_ApplyGASConfiguration</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Should be able to set GAS configurations in the expected ranges successfully using wifi_applyGASConfiguration() HAL api.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_509</test_case_id>
    <test_objective>Should be able to set GAS configurations in the expected ranges successfully using wifi_applyGASConfiguration() HAL api.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_applyGASConfiguration</api_or_interface_used>
    <input_parameters>AdvertisementID : 0-255
PauseForServerResponse : 0/1
ResponseTimeout : 1000-65535
ComeBackDelay : 0-65535
ResponseBufferingTime : 0-65535
QueryResponseLengthLimit : 1-127</input_parameters>
    <automation_approch>1. Load wifihal module
2. Set the GAS configurations using wifi_applyGASConfiguration() HAL api
3. Set operation should return SUCCESS
4. Unload the module</automation_approch>
    <expected_output>Set GAS configurations in the expected ranges successfully using wifi_applyGASConfiguration() HAL api.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_ApplyGASConfiguration</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_ApplyGASConfiguration');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_ApplyGASConfiguration");
    advertisementID = random.randint(0,255);
    pauseForServerResponse = random.randint(0,1);
    responseTimeout = random.randint(1000,65535);
    comeBackDelay = random.randint(0,65535);
    responseBufferingTime = random.randint(0,65535);
    queryResponseLengthLimit = random.randint(1,127);
    tdkTestObj.addParameter("advertisementID",advertisementID);
    tdkTestObj.addParameter("pauseForServerResponse",pauseForServerResponse);
    tdkTestObj.addParameter("responseTimeout",responseTimeout);
    tdkTestObj.addParameter("comeBackDelay",comeBackDelay);
    tdkTestObj.addParameter("responseBufferingTime",responseBufferingTime);
    tdkTestObj.addParameter("queryResponseLengthLimit",queryResponseLengthLimit);
    print "Setting the GAS configurations with the following values:\nadvertisementID=%d\npauseForServerResponse=%d\nresponseTimeout=%d\ncomeBackDelay=%d\nresponseBufferingTime=%d\nqueryResponseLengthLimit=%d\n"%(advertisementID,pauseForServerResponse,responseTimeout,comeBackDelay,responseBufferingTime,queryResponseLengthLimit);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Set the GAS configurations using wifi_applyGASConfiguration";
        print "EXPECTED RESULT 1: Should be able to set GAS configurations using wifi_applyGASConfiguration successfully";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:  Set the GAS configurations using wifi_applyGASConfiguration";
        print "EXPECTED RESULT 1: Should be able to set GAS configurations using wifi_applyGASConfiguration successfully";
        print "ACTUAL RESULT 1: API returned Failure status. %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
