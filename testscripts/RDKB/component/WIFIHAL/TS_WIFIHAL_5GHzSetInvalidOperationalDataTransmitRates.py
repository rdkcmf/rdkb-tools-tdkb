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
  <name>TS_WIFIHAL_5GHzSetInvalidOperationalDataTransmitRates</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set an invalid operational data transmit rate ie, a value not present in supported transmit rate for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_199</test_case_id>
    <test_objective>To set an invalid operational data transmit rate ie, a value not present in supported transmit rate for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioSupportedDataTransmitRates()
wifi_getRadioOperationalDataTransmitRates()
wifi_setRadioOperationalDataTransmitRates()</api_or_interface_used>
    <input_parameters>methodName : getRadioSupportedDataTransmitRates
methodName : getRadioOperationalDataTransmitRates
methodName : setRadioOperationalDataTransmitRates
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getRadioSupportedDataTransmitRates() to get the supported transmit rates. 
3. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getRadioOperationalDataTransmitRates()
4. Using WIFIHAL_GetOrSetParamStringValue 
 invoke wifi_setRadioOperationalDataTransmitRates and set a value that is not present in supported range
5. If the set operation is SUCCESS, return FAILURE else return SUCCESS
6.. Unload wifihal module</automation_approch>
    <except_output>Set operation should not be SUCCESS with out of range values</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetInvalidOperationalDataTransmitRates</test_script>
    <skipped>No</skipped>
    <release_version/>
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
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetInvalidOperationalDataTransmitRates');

#Get the result of connection with test component and DUT
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

    if expectedresult in actualresult :
        supportedRates = details.split(":")[1].strip().split(",")

        expectedresult="SUCCESS";
        radioIndex = 1
        getMethod = "getOperationalDataTransmitRates"
        #Invoke the api wifi_getRadioOperationalDataTransmitRates() using wifiUtility function
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        if expectedresult in actualresult :
            initOperRates = details.split(":")[1].strip()

            r = range(1,100);
            for setOperRate in r:
                if str(setOperRate) not in supportedRates:
                    expectedresult="FAILURE";
                    radioIndex = 1
                    setMethod = "setOperationalDataTransmitRates"
                    print "Set OperationalDataTransmitRate = %s"%setOperRate
                    #Invoke the api wifi_setRadioOperationalDataTransmitRates() using wifiUtility function
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, str(setOperRate), setMethod)
                    if expectedresult in actualresult :
                        print "TEST STEP: To set a data transmit rate not present in SupportedDataTransmitRates list"
                        print "EXPECTED RESULT: Should not set the invalid value"
                        print "ACTUAL RESULT : Unable to set Invalid OperationalDataTransmitRates with value %s"%setOperRate
                        print "TEST EXECUTION RESULT: SUCCESS"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "TEST STEP: To set a data transmit rate not present in SupportedDataTransmitRates list"
                        print "EXPECTED RESULT: Should not set the invalid value"
                        print "ACTUAL RESULT : Sets the Invalid OperationalDataTransmitRates with value %s"%setOperRate
                        print "TEST EXECUTION RESULT: FAILURE"
                        tdkTestObj.setResultStatus("FAILURE");

                        #Revert the data transmit rate to initial value
                        expectedresult="SUCCESS";
                        radioIndex = 1
                        setMethod = "setOperationalDataTransmitRates"
                        #Invoke the api wifi_setRadioOperationalDataTransmitRates() using wifiUtility function
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initOperRates, setMethod)
                        if expectedresult in actualresult :
                            print "Successfully reverted to initial value"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Unable to revert to initial value"
                            tdkTestObj.setResultStatus("FAILURE");
                    break;
                else:
                    continue;
        else:
            print "wifi_getRadioOperationalDataTransmitRates() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getRadioSupportedDataTransmitRates() call failed"
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

