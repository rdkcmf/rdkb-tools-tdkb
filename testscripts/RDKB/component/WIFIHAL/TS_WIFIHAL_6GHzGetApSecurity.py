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
  <version>2</version>
  <name>TS_WIFIHAL_6GHzGetApSecurity</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApSecurity</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApSecurity() for 6G private AP and retrieve all the AP security details and verify if the values are valid.</synopsis>
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
    <test_case_id>TC_WIFIHAL_758</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApSecurity() for 6G private AP and retrieve all the AP security details and verify if the values are valid.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurity()</api_or_interface_used>
    <input_parameters>apIndex : 6G private AP index</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getApSecurity() for 6G private AP. Check if API invocation is success.
3. Retrieve the complete AP security detail values such as security mode, encryption method, WPA3-Transition enabled state, security key type, security key and others. Check if all the values are valid :
security modes should be from - {'1' : "None", '2' : "WEP-64", '4' : "WEP-128", '8' : "WPA-Personal", '16' : "WPA2-Personal", '32' : "WPA-WPA2-Personal", '64' : "WPA-Enterprise", '128' : "WPA2-Enterprise", '256' : "WPA-WPA2-Enterprise", '512' : "WPA3-Personal", '1024' : "WPA3-Personal-Transition", '2048' : "WPA3-Enterprise"};
mfp should be from - {"0" : "Disabled" , "1" : "Optional",  "2" : "Required"}
encryption method should be from - {'0' : "None", '1' : "TKIPEncryption", '2' : "AESEncryption", '3' : "TKIPandAESEncryption"}
security key type should be from - {'0' : "PSK", '1' : "Passphrase", '2' : "SAE", '3' : "PSK_SAE"}
security key should not be null
WPA3 Transition should not be null
Eapol retry and timeout should be integer values
Eap retries and timeouts should be integer values
4. Unload the modules.</automation_approch>
    <expected_output>Invocation of the HAL API wifi_getApSecurity() for 6G private AP should be success and all the AP security details retrieved should be valid.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApSecurity</test_script>
    <skipped>No</skipped>
    <release_version>M99</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApSecurity');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApSecurity');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    #Check if an invalid index is returned
    if apIndex == -1:
        print "Failed to get the 6G access point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        primitive = 'WIFIHAL_GetApSecurity';
        tdkTestObj = obj.createTestStep(primitive);
        tdkTestObj.addParameter("apIndex", apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getApSecurity() for 6G private AP";
        print "EXPECTED RESULT 1: Should successfully invoke wifi_getApSecurity()";

        if expectedresult in actualresult and "AP Security details" in details:
            print "ACTUAL RESULT 1: wifi_getApSecurity() invoked successfully";
            print "TEST EXECUTION RESULT 1: SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");

            #Get the access point security details
            security_mode_dict = {'0x0001' : "None", '0x0002' : "WEP-64", '0x0004' : "WEP-128", '0x0008' : "WPA-Personal", '0x0010' : "WPA2-Personal", '0x0020' : "WPA-WPA2-Personal", '0x0040' : "WPA-Enterprise", '0x0080' : "WPA2-Enterprise", '0x0100' : "WPA-WPA2-Enterprise", '0x0200' : "WPA3-Personal", '0x0400' : "WPA3-Personal-Transition", '0x0800' : "WPA3-Enterprise"};
            security_mode_hex = details.split("Security Mode : ")[1].split(",")[0];

            if security_mode_hex in security_mode_dict :
                security_mode = security_mode_dict[security_mode_hex];
            else :
                security_mode = "Invalid Security Mode";

            mfp = details.split("MFP : ")[1].split(",")[0];

            encryption_method_dict = {'0' : "None", '1' : "TKIPEncryption", '2' : "AESEncryption", '3' : "TKIPandAESEncryption"};
            encryption_method_int = details.split("Encrytion Method : ")[1].split(",")[0];

            if encryption_method_int in encryption_method_dict:
                encryption_method = encryption_method_dict[encryption_method_int];
            else :
                encryption_method = "Invalid Encryption Method";

            wpa3_transition = details.split("WPA3 Transition : ")[1].split(",")[0];
            rekey_interval = details.split("Rekey Interval : ")[1].split(",")[0];
            strict_rekey = details.split("Strict Rekey : ")[1].split(",")[0];
            eapol_key_timeout = details.split("Eapol Key Timeout : ")[1].split(",")[0];
            eapol_key_retries = details.split("Eapol Key Retries : ")[1].split(",")[0];
            eap_identity_timeout = details.split("Eap Identity Timeout : ")[1].split(",")[0];
            eap_identity_retries = details.split("Eap Identity Retries : ")[1].split(",")[0];
            eap_timeout = details.split("Eap Timeout : ")[1].split(",")[0];
            eap_retries = details.split("Eap Retries : ")[1].split(",")[0];
            pmksa_cashing = details.split("PMKSA Cashing : ")[1].split(",")[0];

            #The following AP security details such as security key type and security key will only be retrieved if security_mode is not None or any enterprise mode
            security_key_type = "";
            key = "";

            if security_mode == "WPA-Personal" or security_mode == "WPA2-Personal" or security_mode == "WPA3-Personal" or security_mode == "WPA3-Personal-Transition" or security_mode == "WPA-WPA2-Personal" :
                security_key_type_dict = {'0' : "PSK", '1' : "Passphrase", '2' : "SAE", '3' : "PSK_SAE"};
                security_key_type_int = details.split("Security Key Type : ")[1].split(",")[0];

                if security_key_type_int in security_key_type_dict:
                    security_key_type = security_key_type_dict[security_key_type_int];

                    if security_key_type == "PSK":
                        key = details.split("WPA PSK : ")[1].split(",")[0];
                    else :
                        key = details.split("WPA Passphrase : ")[1].split(",")[0];
                else :
                    security_key_type = "Invalid Security Key Type";
                    key = "Invalid Key";
            else :
                print "As Security Mode is %s, Security Key Type and Security Key are not retrieved" %security_mode;

            print "\nTEST STEP 2: Get the Access Point Security details and check if the values are valid";
            print "EXPECTED RESULT 2: Should get the Access Point Security details successfully and the values should be valid";

            #Print all applicable values
            print "Security Mode : ", security_mode;
            print "MFP : ", mfp;
            print "Encryption Method : ", encryption_method;
            print "WPA3 Transition : ", wpa3_transition;
            print "Rekey Interval : ", rekey_interval;
            print "Strict Rekey : ", strict_rekey;
            print "Eapol Key Timeout : ", eapol_key_timeout;
            print "Eapol Key Retries : ", eapol_key_retries;
            print "Eap Identity Timeout : ", eap_identity_timeout;
            print "Eap Identity Retries : ", eap_identity_retries;
            print "Eap Timeout : ", eap_timeout;
            print "Eap Retries : ", eap_retries;
            print "PMKSA Caching : ", pmksa_cashing;

            if security_mode == "WPA-Personal" or security_mode == "WPA2-Personal" or security_mode == "WPA3-Personal" or security_mode == "WPA3-Personal-Transition" or security_mode == "WPA-WPA2-Personal" :
                print "Security Key Type : ", security_key_type;
                print "Security Key : ", key;

            if "Invalid" not in security_mode and mfp.isdigit() and "Invalid" not in encryption_method and wpa3_transition != "" and rekey_interval.isdigit() and strict_rekey != "" and eapol_key_timeout.isdigit() and eapol_key_retries.isdigit() and eap_identity_timeout.isdigit() and eap_identity_retries.isdigit() and eap_timeout.isdigit() and eap_retries.isdigit() and pmksa_cashing != "" and "Invalid" not in security_key_type and "Invalid" not in key:
                print "ACTUAL RESULT 2: The Access Point Security details are retrieved and all values are valid";
                print "TEST EXECUTION RESULT 2: SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "ACTUAL RESULT 2: All Access Point Security details are not valid";
                print "TEST EXECUTION RESULT 2: FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "ACTUAL RESULT 1: wifi_getApSecurity() is not invoked successfully";
            print "TEST EXECUTION RESULT 1: FAILURE";
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

