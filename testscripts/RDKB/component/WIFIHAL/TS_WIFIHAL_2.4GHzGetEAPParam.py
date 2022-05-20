##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzGetEAPParam</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetEAPParam</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getEAP_Param() for 2.4G private AP index and retrieve the values for EAPOL Key Timeout and Retries, EAP Identity Request Timeout and Retries, EAP Request Timeout and Retries.</synopsis>
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
    <test_case_id>TC_WIFIHAL_793</test_case_id>
    <test_objective>Invoke the HAL API wifi_getEAP_Param() for 2.4G private AP index and retrieve the values for EAPOL Key Timeout and Retries, EAP Identity Request Timeout and Retries, EAP Request Timeout and Retries.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getEAP_Param()</api_or_interface_used>
    <input_parameters>apIndex : 2.4G private AP index</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getEAP_Param() for 2.4G private AP.
3. If the invocation is success retrieve EAPOL Key Timeout and Retries, EAP Identity Request Timeout and Retries, EAP Request Timeout and Retries and check if all the values are valid integers.
4. Unload the module</automation_approch>
    <expected_output>The the HAL API wifi_getEAP_Param() for 2.4G private AP index should be invoked successfully and the values for EAPOL Key Timeout and Retries, EAP Identity Request Timeout and Retries, EAP Request Timeout and Retries should be retrieved as valid integer values.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetEAPParam</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetEAPParam');

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
        tdkTestObj = obj.createTestStep("WIFIHAL_GetEAPParam");
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getEAP_Param() to retrieve the 2.4G EAP Param values";
        print "EXPECTED RESULT 1: Should invoke the HAL API wifi_getEAP_Param() successfully";

        if expectedresult in actualresult and "EAP Congiguration" in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Retrieve the EAP Param structure values
            eapol_key_timeout = details.split("EAPOL Key Timeout: ")[1].split(",")[0];
            eapol_key_retries = details.split("EAPOL Key Retries: ")[1].split(",")[0];
            eap_identity_timeout = details.split("EAP Identity Request Timeout: ")[1].split(",")[0];
            eap_identity_retries = details.split("EAP Identity Request Retries: ")[1].split(",")[0];
            eap_req_timeout = details.split("EAP Request Timeout: ")[1].split(",")[0];
            eap_req_reties = details.split("EAP Request Retries: ")[1].split(",")[0];

            #Print all EAP Param values
            print "EAPOL Key Timeout = %s" %eapol_key_timeout;
            print "EAPOL Key Retries = %s" %eapol_key_retries;
            print "EAP Identity Request Timeout = %s" %eap_identity_timeout;
            print "EAP Identity Request Retries = %s" %eap_identity_retries;
            print "EAP Request Timeout = %s" %eap_req_timeout;
            print "EAP Request Retries = %s" %eap_req_reties;

            print "\nTEST STEP 2 : Check if the EAP Param structure values are valid integer values";
            print "EXPECTED RESULT 2 : EAP Param structure values should be valid integer values";

            if eapol_key_timeout.isdigit() and eapol_key_retries.isdigit() and eap_identity_timeout.isdigit() and eap_identity_retries.isdigit() and eap_req_timeout.isdigit() and eap_req_reties.isdigit():
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: EAP Param structure values are valid";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Not all EAP Param structure values are valid";
                #Get the result of execution
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
