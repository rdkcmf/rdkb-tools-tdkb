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
  <version>1</version>
  <name>TS_WIFIHAL_5GHzSetInvalidRadioBasicDataTransmitRates</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the basic data transmit rate with a value not in the supported data transmit rates and check whether the set operation is failing for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_224</test_case_id>
    <test_objective>To set the basic data transmit rate with a value not in the supported data transmit rates and check whether the set operation is failing.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioBasicDataTransmitRates()
wifi_getRadioSupportedDataTransmitRates()
wifi_setRadioBasicDataTransmitRates()</api_or_interface_used>
    <input_parameters>methodName : getSupportedDataTransmitRates
methodName : getRadioBasicDataTransmitRates
methodName : setRadioBasicDataTransmitRates
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2.Get the supported transmit rate using wifi_getRadioSupportedDataTransmitRates()
3. Invoke wifi_getRadiobasicDataTransmitRates()  to get the current data transmit rate
4.Set the basic transmit rate not in the list of supported data transmit rates using wifi_setRadioBasicDataTransmitRates()
5.Set operation should fail as we are trying to set the value not in the list of supported data transmit rates.
6.Unload the wifi module.</automation_approch>
    <except_output>Set operation should fail as we are trying to set the value not in the list of supported data transmit rates.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetInvalidRadioBasicDataTransmitRates</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetInvalidRadioBasicDataTransmitRates');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getSupportedDataTransmitRates"
    primitive = "WIFIHAL_GetOrSetParamStringValue"
    #Invoke the api wifi_getRadioSupportedDataTransmitRates() using wifiUtility function
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
    supportedRatesList = details.split(":")
    if expectedresult in actualresult :
        expectedresult="SUCCESS";
        radioIndex = 1
        getMethod = "getRadioBasicDataTransmitRates"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'
        #Invoke the api wifi_getRadioBasicDataTransmitRates() using wifiUtility function
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        basicRates = details.split(":")[1].strip()
        for x in range(1):
            z = random.randint(1,500);
            setbasicRate = str(z);
        if expectedresult in actualresult:

            if setbasicRate not in supportedRatesList:
                expectedresult="FAILURE";
                radioIndex = 1
                setMethod = "setRadioBasicDataTransmitRates"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'
                print "setbasicRate",setbasicRate

                #Calling the method to execute wifi_setRadioBasicDataTransmitRates()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setbasicRate, setMethod)
                if expectedresult in actualresult:
                    print "TEST STEP: Set the radio basic data transmit rates out of supported data transmit rates"
                    print "EXPECTED RESULT : Set operation should fail"
                    print "ACTUAL RESULT : Set operation should fail"
                    print "TEST EXECUTION RESULT : SUCCESS"
                    print "setbasicRate:",setbasicRate
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "TEST STEP:Set the radio basic data transmit rates out of supported data transmit rates "
                    print "EXPECTED RESULT : Set operation should fail "
                    print "ACTUAL RESULT : Set operation is success"
                    print "TEST EXECUTION RESULT : FAILURE"
                    tdkTestObj.setResultStatus("FAILURE");
                    #Revert the radio basic data transmit rates back to initial value
                    expectedresult = "SUCCESS";
                    setMethod = "setRadioBasicDataTransmitRates"

                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, basicRates , setMethod)
                    if expectedresult in actualresult:
                        print "Successfully reverted radio basic data transmit rates to initial value"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Unable to revert the radio basic data transmit rates"
                        tdkTestObj.setResultStatus("FAILURE");
        else:
            print "wifi_getRadioBasicDataTransmitRates() failed";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getSupportedDataTransmitRates() failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

