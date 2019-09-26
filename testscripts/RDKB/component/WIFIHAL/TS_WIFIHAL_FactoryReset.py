##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_FactoryReset</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_FactoryReset</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the wifi_factoryReset() api and check whether the values are being reset to factory values.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_285</test_case_id>
    <test_objective>To invoke the wifi_factoryReset() api and check whether the values are being reset to factory values.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsDevicePIN()
wifi_setApWpsDevicePIN()
wifi_getApSecurityKeyPassphrase()
wifi_setApSecurityKeyPassphrase()
wifi_factoryReset()</api_or_interface_used>
    <input_parameters>methodName : getApWpsDevicePIN
methodName : setApWpsDevicePIN
methoName : getApSecurityKeyPassphrase
methodName : setApSecurityKeyPassphrase
methodName : factoryReset
radioIndex : 0
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get the Device PIN and KeyPassphrase using  wifi_getApWpsDevicePIN() and wifi_getApSecurityKeyPassphrase() apis respectively for both 2.4GHz and 5GHz.
3.Set the Device PIN and Keypassphrase to different values using wifi_setApWpsDevicePIN() and wifi_setApSecurityKeyPassphrase() apis respectively for both 2.4GHz and 5GHz. 
4.Invoke the wifi_factoryReset().
5.Check whether set and get values after factory reset for Device PIN and KeyPassphrase are not same for both 2.4GHz and 5GHz.
5.If not same.return SUCCESS,else FAILURE.
6.Unload the module.</automation_approch>
    <except_output>The wifi_factoryReset() api should reset the values to factory values.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_FactoryReset</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_FactoryReset');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
def GetOperation_PIN(radioIndex):
    #get the ApWpsDevicePIN
    expectedresult="SUCCESS";
    getMethod = "getApWpsDevicePIN"
    primitive = 'WIFIHAL_GetOrSetParamULongValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    if expectedresult in actualresult:
	tdkTestObj.setResultStatus("SUCCESS");
	PIN = int(details.split(":")[1].strip());
	return PIN;
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print"getApWpsDevicePIN() operation failed for %d radioIndex"%radioIndex;

def SetOperation_PIN(radioIndex,setPIN):
    #set the ApWpsDevicePIN
    expectedresult="SUCCESS";
    setMethod = "setApWpsDevicePIN"
    primitive = 'WIFIHAL_GetOrSetParamULongValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setPIN, setMethod)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
	print"Successfully set the DevicePIN to ",setPIN;
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print"setApWpsDevicePIN() operation failed for %d radioIndex"%radioIndex;

def GetOperation_KeyPassphrase(radioIndex):
    #get the ApSecurityKeyPassphrase
    expectedresult="SUCCESS";
    getMethod = "getApSecurityKeyPassphrase"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
    if expectedresult in actualresult:
	tdkTestObj.setResultStatus("SUCCESS");
	KeyPassphrase = details.split(":")[1].strip();
	return KeyPassphrase;
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print"getApSecurityKeyPassphrase() operation failed for %d radioIndex"%radioIndex;

def SetOperation_KeyPassphrase(radioIndex,setKeyPassphrase):
    #set the ApSecurityKeyPassphrase
    expectedresult="SUCCESS";
    setMethod = "setApSecurityKeyPassphrase"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setKeyPassphrase, setMethod)
    if expectedresult in actualresult:
	tdkTestObj.setResultStatus("SUCCESS");
	print "Successfully set the KeyPassphrase to ",setKeyPassphrase;
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print"setApSecurityKeyPassphrase() operation failed for %d radioIndex"%radioIndex;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    DevicePIN0_initial =  GetOperation_PIN(0);
    print "DevicePIN initially for 2.4GHz = ",DevicePIN0_initial;
    DevicePIN1_initial =  GetOperation_PIN(1);
    print "DevicePIN initially for 5GHz = ",DevicePIN1_initial;
    KeyPassphrase0_initial = GetOperation_KeyPassphrase(0);
    print "KeyPassphrase initially for 2.4GHz = ",KeyPassphrase0_initial;
    KeyPassphrase1_initial = GetOperation_KeyPassphrase(1);
    print "KeyPassphrase initially for 5GHz = ",KeyPassphrase1_initial;
    setPIN = 23344556;
    SetOperation_PIN(0,setPIN);
    SetOperation_PIN(1,setPIN);
    setKeyPassphrase = "testpassword123";
    SetOperation_KeyPassphrase(0,setKeyPassphrase);
    SetOperation_KeyPassphrase(1,setKeyPassphrase);
    DevicePIN0_set =  GetOperation_PIN(0);
    print "DevicePIN after set for 2.4GHz = ",DevicePIN0_set;
    DevicePIN1_set =  GetOperation_PIN(1);
    print "DevicePIN after set for 5GHz = ",DevicePIN1_set;
    KeyPassphrase0_set = GetOperation_KeyPassphrase(0);
    print "KeyPassphrase after set for 2.4GHz = ",KeyPassphrase0_set;
    KeyPassphrase1_set = GetOperation_KeyPassphrase(1);
    print "KeyPassphrase after set for 5GHz = ",KeyPassphrase1_set;
    #call the factory reset api
    #Primitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIHAL_FactoryReset');
    #Giving the method name to invoke the api wifi_factoryReset()
    tdkTestObj.addParameter("methodName","factoryReset");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
	print"details",details;
	DevicePIN0_reset =  GetOperation_PIN(0);
	print "DevicePIN after factoryReset for 2.4GHz = ",DevicePIN0_reset;
	DevicePIN1_reset =  GetOperation_PIN(1);
	print "DevicePIN after factoryReset for 5GHz = ",DevicePIN1_reset;
	KeyPassphrase0_reset = GetOperation_KeyPassphrase(0);
	print "KeyPassphrase after factoryReset for 2.4GHz = ",KeyPassphrase0_reset;
	KeyPassphrase1_reset = GetOperation_KeyPassphrase(1);
	print "KeyPassphrase after factoryReset for 5GHz = ",KeyPassphrase1_reset;
	if KeyPassphrase0_reset != KeyPassphrase0_set and KeyPassphrase1_reset != KeyPassphrase1_set:
            tdkTestObj.setResultStatus("SUCCESS");
            print"TEST STEP:To invoke the wifi_factoryReset() api and check whether the KeyPassphrase is not equal to the set value";
            print"EXPECTED RESULT:The KeyPassphrase should not be equal to the set value after factory reset for both 2.4GHz and 5GHz";
            print"ACTUAL RESULT:The KeyPassphrase is changed after the factory reset for both 2.4GHz and 5GHz";
            print"[TEST EXECUTION RESULT]:SUCCESS";
            #Revert the KeyPassphrase to initial value
            print"[REVERTING THE KEYPASSPHRASE TO INITIAL VALUE...]";
            SetOperation_KeyPassphrase(0,KeyPassphrase0_initial);
            SetOperation_KeyPassphrase(1,KeyPassphrase1_initial);
            if DevicePIN0_reset != DevicePIN0_set and DevicePIN1_reset != DevicePIN1_set:
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP:To invoke the wifi_factoryReset() api and check whether the DevicePIN is not equal to the set value";
                print"EXPECTED RESULT:The DevicePIN should not be equal to the set value after factory reset for both 2.4GHz and 5GHz";
                print"ACTUAL RESULT:The DevicePIN is changed after the factory reset for both 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT]:SUCCESS";
                #Revert the DevicePIN to initial value
                print"[REVERTING THE DEVICEPIN TO INITIAL VALUE...]";
                SetOperation_PIN(0,DevicePIN0_initial);
                SetOperation_PIN(1,DevicePIN1_initial);
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP:To invoke the wifi_factoryReset() api and check whether the DevicePIN is not equal to the set value";
                print"EXPECTED RESULT:The DevicePIN should not be equal to the set value after factory reset for both 2.4GHz and 5GHz";
                print"ACTUAL RESULT:The DevicePIN is not changed after the factory reset for both 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT]:FAILURE";
                #Revert the DevicePIN to initial value
                print"[REVERTING THE DEVICEPIN TO INITIAL VALUE...]";
                SetOperation_PIN(0,DevicePIN0_initial);
                SetOperation_PIN(1,DevicePIN1_initial);
        else:
            tdkTestObj.setResultStatus("FAILURE");
	    print"TEST STEP:To invoke the wifi_factoryReset() api and check whether the KeyPassphrase is not equal to the set value";
            print"EXPECTED RESULT:The KeyPassphrase should not be equal to the set value after factory reset for both 2.4GHz and 5GHz";
            print"ACTUAL RESULT:The KeyPassphrase is not changed after the factory reset for both 2.4GHz and 5GHz";
            print"[TEST EXECUTION RESULT]:FAILURE";
            #Revert the KeyPassphrase to initial value
            print"[REVERTING THE KEYPASSPHRASE TO INITIAL VALUE...]";
            SetOperation_KeyPassphrase(0,KeyPassphrase0_initial);
            SetOperation_KeyPassphrase(1,KeyPassphrase1_initial);
            #Revert the DevicePIN to initial value
            print"[REVERTING THE DEVICEPIN TO INITIAL VALUE...]";
            SetOperation_PIN(0,DevicePIN0_initial);
            SetOperation_PIN(1,DevicePIN1_initial);
    else:
	tdkTestObj.setResultStatus("FAILURE");
	print"wifi_factoryReset() operation failed";
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
