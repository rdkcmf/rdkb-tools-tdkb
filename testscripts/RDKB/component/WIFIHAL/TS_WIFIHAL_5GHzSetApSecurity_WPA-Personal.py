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
  <name>TS_WIFIHAL_5GHzSetApSecurity_WPA-Personal</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_SetApSecurity</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setApSecurity() to set the security parameters when the security mode is set to "WPA-Personal" and check if the SET operation of the mfp, encryption mode, key type and key passphrase is success and is getting reflected when the GET  API wifi_getApSecurity() is invoked for 5GHz private AP.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_762</test_case_id>
    <test_objective>Invoke the HAL API wifi_setApSecurity() to set the security parameters when the security mode is set to "WPA-Personal" and check if the SET operation of the mfp, encryption mode, key type and key passphrase is success and is getting reflected when the GET  API wifi_getApSecurity() is invoked for 5GHz private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurity()
wifi_setApSecurity()</api_or_interface_used>
    <input_parameters>apIndex : 5G private AP index
mode : security modes - {'1' : "None", '2' : "WEP-64", '4' : "WEP-128", '8' : "WPA-Personal", '16' : "WPA2-Personal", '32' : "WPA-WPA2-Personal", '64' : "WPA-Enterprise", '128' : "WPA2-Enterprise", '256' : "WPA-WPA2-Enterprise", '512' : "WPA3-Personal", '1024' : "WPA3-Personal-Transition", '2048' : "WPA3-Enterprise"};
mfp : {"0" : "Disabled" , "1" : "Optional",  "2" : "Required"}
encr : encryption method - {'0' : "None", '1' : "TKIPEncryption", '2' : "AESEncryption", '3' : "TKIPandAESEncryption"}
key_type : security key type - {'0' : "PSK", '1' : "Passphrase", '2' : "SAE", '3' : "PSK_SAE"}
key : security key
</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getApSecurity() for 2.4G private AP and retrieve the initial values of the  security parameters and store them. Key Type and KeyPassphrase will be retrieved only if the initial security mode is not None or any of the enterprise modes.
3. Invoke the HAL API wifi_setApSecurity() to set security parameter values in the security mode : "WPA-Personal". Set mfp : 2, encryption mode : AESEncyption, key type : passphrase and key : testpassword123. Check if the GET API returns success.
4. Invoke the HAL API wifi_getApSecurity() to check if the security mode, mfp, encryption mode, key type and key values are the same as the values set.
5. Restore to initial state
6. Unload the modules</automation_approch>
    <expected_output>The HAL API wifi_setApSecurity() should successfully set the security parameters such as mfp, encryption type, key type and key passphrase to valid values when the security mode is set to WPA-Personal and the SET values should be reflected by the GET API wifi_getApSecurity() for 5G Private AP.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApSecurity_WPA-Personal</test_script>
    <skipped>No</skipped>
    <release_version>M99</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def getAPSecurity(obj, apIndex):
    expectedresult = "SUCCESS";
    primitive = 'WIFIHAL_GetApSecurity';
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("apIndex", apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details, tdkTestObj;

def setAPSecurity(obj, apIndex, setvalues):
    expectedresult = "SUCCESS";
    primitive = 'WIFIHAL_SetApSecurity'
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("apIndex", apIndex);
    tdkTestObj.addParameter("mode", setvalues[0]);
    tdkTestObj.addParameter("mfp", setvalues[1]);

    #Additional parameters can be set only if security mode is not None or enterprise
    if setvalues[0] not in [1,2,64,128,256,2048]:
        tdkTestObj.addParameter("encr", setvalues[2]);
        tdkTestObj.addParameter("key_type", setvalues[3]);
        tdkTestObj.addParameter("key", setvalues[4]);

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details, tdkTestObj;


def getAPSecurityDetails(details):
    #values[] to keep track of the AP Security parameters in string format
    values = [];
    #map_to_enum_values[] to keep track of AP Security parameters in enumeration format
    map_to_enum_values = [];

    #Security Mode
    security_mode_dict = {'0x0001' : "None", '0x0002' : "WEP-64", '0x0004' : "WEP-128", '0x0008' : "WPA-Personal", '0x0010' : "WPA2-Personal", '0x0020' : "WPA-WPA2-Personal", '0x0040' : "WPA-Enterprise", '0x0080' : "WPA2-Enterprise", '0x0100' : "WPA-WPA2-Enterprise", '0x0200' : "WPA3-Personal", '0x0400' : "WPA3-Personal-Transition", '0x0800' : "WPA3-Enterprise"};
    security_mode_hex = details.split("Security Mode : ")[1].split(",")[0];

    if security_mode_hex in security_mode_dict :
        security_mode = security_mode_dict[security_mode_hex];
    else :
        security_mode = "Invalid Security Mode";

    values.append(security_mode);
    security_mode_int = int(security_mode_hex, 16);
    map_to_enum_values.append(security_mode_int);

    #MFP
    mfp = details.split("MFP : ")[1].split(",")[0];
    values.append(mfp);
    if mfp.isdigit():
        mfp_int = int(mfp);
        map_to_enum_values.append(mfp_int);

    #Encryption Method
    encryption_method_dict = {'0' : "None", '1' : "TKIPEncryption", '2' : "AESEncryption", '3' : "TKIPandAESEncryption"};
    encryption_method_int = details.split("Encrytion Method : ")[1].split(",")[0];

    if encryption_method_int in encryption_method_dict:
        encryption_method = encryption_method_dict[encryption_method_int];
    else :
        encryption_method = "Invalid Encryption Method";

    values.append(encryption_method);
    encr_method = int(encryption_method_int);
    map_to_enum_values.append(encr_method);

    #Other parameters to be read
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

            values.append(security_key_type);
            security_key_type_int = int(security_key_type_int);
            map_to_enum_values.append(security_key_type_int);

            values.append(key);
            map_to_enum_values.append(key);
        else :
            security_key_type = "Invalid Security Key Type";
            key = "Invalid Key";
    else :
        print "As Security Mode is %s, Security Key Type and Security Key are not retrieved" %security_mode;

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
        status = "SUCCESS";
    else:
        status = "FAILED";
    return status, values, map_to_enum_values;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApSecurity_WPA-Personal');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Invoke the Get AP Security API
        actualresult, details, tdkTestObj = getAPSecurity(obj, idx);
        print "\nTEST STEP 1: Invoke the HAL API wifi_getApSecurity() for 5G private AP";
        print "EXPECTED RESULT 1: Should successfully invoke wifi_getApSecurity()";

        if expectedresult in actualresult and "AP Security details" in details:
            print "ACTUAL RESULT 1: wifi_getApSecurity() invoked successfully";
            print "TEST EXECUTION RESULT 1: SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");

            #Get the access point security details
            status, initial_values, map_to_enum_values_initial = getAPSecurityDetails(details);
            print "\nTEST STEP 2: Get the Access Point Security details and check if the initial values are valid";
            print "EXPECTED RESULT 2: Should get the Access Point Security details successfully and the initial values should be valid";

            if status == "SUCCESS":
                print "ACTUAL RESULT 2: The Access Point Security details are retrieved and all initial values are valid";
                print "TEST EXECUTION RESULT 2: SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");

                #Set AP Security
                #New Security Mode = WPA-Personal, which has the decimal value 8 corresponding to the Hex value 0x00000008
                new_security_mode = 8;
                #New MFP = 1
                new_mfp = 1;
                #New Encruption Method = AESEncryption, which has the value 2
                new_encryption_method = 2;
                #New Key Type = Passphrase, which has the value 1
                new_key_type = 1;
                #New Key = "testpassword123";
                new_key = "testpassword123";
                set_values = ["WPA-Personal", "1", "AESEncryption", "Passphrase", "testpassword123"];
                new_values = [new_security_mode, new_mfp, new_encryption_method, new_key_type, new_key];

                actualresult, details, tdkTestObj = setAPSecurity(obj, idx, new_values);
                print "\nTEST STEP 3 : Invoke the HAL API wifi_setApSecurity() for 5G private AP with Security Mode : %s, MFP : %s, Encryption Mode : %s, Key Type : %s and Key : %s" %(set_values[0], set_values[1], set_values[2], set_values[3], set_values[4]);
                print "EXPECTED RESULT 3 : The HAL API should be invoked successfully";

                if expectedresult in actualresult:
                    print "ACTUAL RESULT 3: The SET API returned success; Details : %s" %details;
                    print "TEST EXECUTION RESULT 3: SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");

                    #Cross check the SET with GET
                    actualresult, details, tdkTestObj = getAPSecurity(obj, idx)
                    print "\nTEST STEP 4: Invoke the HAL API wifi_getApSecurity() for 5G private AP after the SET operation";
                    print "EXPECTED RESULT 4: Should successfully invoke wifi_getApSecurity()";

                    if expectedresult in actualresult and "AP Security details" in details:
                        print "ACTUAL RESULT 4: wifi_getApSecurity() invoked successfully";
                        print "TEST EXECUTION RESULT 1: SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Get the access point security details and check if the values SET are GET
                        status, final_values, map_to_enum_values_final = getAPSecurityDetails(details);
                        print "\nTEST STEP 5: Get the Access Point Security details and check if the retrieved values are valid";
                        print "EXPECTED RESULT 5: Should get the Access Point Security details successfully and the retrieved values should be valid";

                        if status == "SUCCESS":
                            print "ACTUAL RESULT 5: The Access Point Security details are retrieved and all retrieved values are valid";
                            print "TEST EXECUTION RESULT 5: SUCCESS";
                            tdkTestObj.setResultStatus("SUCCESS");

                            print "Security Mode SET : %s" %set_values[0];
                            print "Security Mode GET : %s" %final_values[0];
                            print "MFP SET : %s" %set_values[1];
                            print "MFP GET : %s" %final_values[1];
                            print "Encryption Method SET : %s" %set_values[2];
                            print "Encryption Method GET : %s" %final_values[2];
                            print "Key Type SET : %s" %set_values[3];
                            print "Key Type GET : %s" %final_values[3];
                            print "Key SET : %s" %set_values[4];
                            print "Key GET : %s" %final_values[4];

                            if (set_values[0] == final_values[0]) and (set_values[1] == final_values[1]) and (set_values[2] == final_values[2]) and (set_values[3] == final_values[3]) and (set_values[4] == final_values[4]):
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "The GET values match with the SET values";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "The GET values do not match with the SET values";
                        else:
                            print "ACTUAL RESULT 5: The Access Point Security details are retrieved and all retrieved values are not valid";
                            print "TEST EXECUTION RESULT 5: FAILURE";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "ACTUAL RESULT 4: wifi_getApSecurity() not invoked successfully";
                        print "TEST EXECUTION RESULT 4: FAILURE";
                        tdkTestObj.setResultStatus("FAILURE");

                    #Revert operation
                    actualresult, details, tdkTestObj = setAPSecurity(obj, idx, map_to_enum_values_initial);
                    print "\nTEST STEP 6 : Revert to initial AP Security state";
                    print "EXPECTED RESULT 6 : Revert operation should be success";

                    if expectedresult in actualresult:
                        print "ACTUAL RESULT 6: The SET API returned success; Details : %s" %details;
                        print "TEST EXECUTION RESULT 6: SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "ACTUAL RESULT 6: The SET API returned failure; Details : %s" %details;
                        print "TEST EXECUTION RESULT 6: FAILURE";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "ACTUAL RESULT 3: The SET API returned failure; Details : %s" %details;
                    print "TEST EXECUTION RESULT 3: FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "ACTUAL RESULT 2: All Access Point Security details are not valid";
                print "TEST EXECUTION RESULT 2: FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "ACTUAL RESULT 1: wifi_getApSecurity() is not invoked successfully";
            print "TEST EXECUTION RESULT 1: FAILURE";
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
