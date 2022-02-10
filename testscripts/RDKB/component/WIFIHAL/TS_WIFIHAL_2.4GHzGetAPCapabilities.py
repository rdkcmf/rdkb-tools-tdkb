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
  <version>7</version>
  <name>TS_WIFIHAL_2.4GHzGetAPCapabilities</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetAPCapabilities</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getAPCapabilities() to retrieve the AP Capabilities such as RTS threshold support, Security modes supported, Onboarding methods supported, WMM support, UAPSD support, Interworking service support and BSS transition support for 2.4G Private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_744</test_case_id>
    <test_objective>Invoke the HAL API wifi_getAPCapabilities() to retrieve the AP Capabilities such as RTS threshold support, Security modes supported, Onboarding methods supported, WMM support, UAPSD support, Interworking service support and BSS transition support for 2.4G Private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getAPCapabilities()</api_or_interface_used>
    <input_parameters>apIndex : 2.4G private AP index</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getAPCapabilities() for 2.4G private AP and check if the API invocation is success.
3. Retrieve the AP Capabilities structures values such as RTS threshold support, Security modes supported, Onboarding methods supported, WMM support, UAPSD support, Interworking service support and BSS transition support and ensure that values are not empty.
4. Unload the module</automation_approch>
    <expected_output>Invocation of  the HAL API wifi_getAPCapabilities() to retrieve the AP Capabilities such as RTS threshold support, Security modes supported, Onboarding methods supported, WMM support, UAPSD support, Interworking service support and BSS transition support should be success for 2.4G Private AP and values retrieved should be non-empty.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetAPCapabilities</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetAPCapabilities');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep("WIFIHAL_GetAPCapabilities");
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getAPCapabilities() to retrieve the 2.4G Private AP Capabilities";
        print "EXPECTED RESULT 1: Should invoke the HAL API wifi_getAPCapabilities() successfully";

        if expectedresult in actualresult and "Details" in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API was invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Retrieve the AP Capabilities structure values
            rts_threshold = details.split("RTS Threshold Supported = ")[1].split(",")[0];
            security_modes = details.split("Security Modes Supported = ")[1].split(",")[0];
            onboarding_methods = details.split("Onboarding Methods Supported = ")[1].split(",")[0];
            wmm_support = details.split("WMM Supported = ")[1].split(",")[0];
            uapsd_support = details.split("UAPSD Supported = ")[1].split(",")[0];
            interworking_service = details.split("Interworking Service Supported = ")[1].split(",")[0];
            bss_transition = details.split("BSS Transition Implemented = ")[1].split(",")[0].strip("\\n");

            #Print all AP Capabilities values
            print "RTS Threshold Supported = %s" %rts_threshold;
            print "Security Modes Supported = %s" %security_modes;
            print "Onboarding Methods Supported = %s" %onboarding_methods;
            print "WMM Supported = %s" %wmm_support;
            print "UAPSD Supported = %s" %uapsd_support;
            print "Interworking Service Supported = %s" %interworking_service;
            print "BSS Transition Implemented = %s" %bss_transition;

            print "\nTEST STEP 2 : Check if the AP Capabilities structure values are non-empty";
            print "EXPECTED RESULT 2 : AP Capabilities structure values should be non-empty";

            if rts_threshold != "" and security_modes != "" and onboarding_methods != "" and wmm_support != "" and uapsd_support != "" and interworking_service != "" and bss_transition != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: AP Capabilities structure values are non-empty";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Not all AP Capabilities structure values are non-empty";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
