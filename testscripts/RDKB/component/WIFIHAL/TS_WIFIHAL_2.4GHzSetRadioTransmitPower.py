########################################################################
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
  <name>TS_WIFIHAL_2.4GHzSetRadioTransmitPower</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the RadioTransmitPower for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_WIFIHAL_211</test_case_id>
    <test_objective>To get the supported transmit power for 2.4GHz and try to set a valid transmit power. </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioTransmitPowerSupported()
wifi_getRadioTransmitPower()
wifi_setRadioTransmitPower()</api_or_interface_used>
    <input_parameters>methodName: getRadioTransmitPowerSupported
methodName: getRadioTransmitPower
methodName: setRadioTransmitPower
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getRadioTransmitPowerSupported() and save the supported transmit powers.
3. Using  WIFIHAL_GetOrSetParamULongValue invoke wifi_getRadioTransmitPower()
4. Using WIFIHAL_GetOrSetParamULongValue
 invoke wifi_setRadioTransmitPower and set a valid value from the supported list
5. Invoke wifi_getRadioTransmitPower() to get the previously set value.
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the transmit power back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>The set and get values of transmit powers should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioTransmitPower</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioTransmitPower');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    getMethod = "getRadioTransmitPowerSupported"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    radioIndex = 0
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

    if expectedresult in actualresult:
        supportedTransmitPower = details.split(":")[1].strip()
	supportedTransmitPower = [int(x) for x in details.split(":")[1].split(",")];
	print "Supported Transmit Power: %s"%supportedTransmitPower
        tdkTestObj.setResultStatus("SUCCESS");

        getMethod = "getRadioTransmitPower"
        primitive = 'WIFIHAL_GetOrSetParamULongValue'
        radioIndex = 0
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

        if expectedresult in actualresult:
            initGetValue = details.split(":")[1].strip()
            tdkTestObj.setResultStatus("SUCCESS");
            setMethod = "setRadioTransmitPower"
            radioIndex = 0
            primitive = 'WIFIHAL_GetOrSetParamULongValue'
	    for setValue in supportedTransmitPower:
		if setValue == int(initGetValue) or setValue == 0:
		    continue;
		else:
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)
		    time.sleep(60);

                    if expectedresult in actualresult:
                        getMethod = "getRadioTransmitPower"
                        radioIndex = 0
                        primitive = 'WIFIHAL_GetOrSetParamULongValue'
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            finalGetValue = details.split(":")[1].strip()
                            if setValue == int(finalGetValue):
                                print "TEST STEP: Comparing set and get values of TransmitPower"
                                print "EXPECTED RESULT: Set and get values should be the same"
                                print "ACTUAL RESULT : Set and get values are the same"
                                print "Set value: %s"%setValue
                                print "Get value: %s"%finalGetValue
                                print "TEST EXECUTION RESULT :SUCCESS"
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "TEST STEP: Comparing set and get values of TransmitPower"
                                print "EXPECTED RESULT: Set and get values should be the same"
                                print "ACTUAL RESULT : Set and get values are NOT the same"
                                print "Set value: %s"%setValue
                                print "Get value: %s"%finalGetValue
                                print "TEST EXECUTION RESULT :FAILURE"
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "getRadioTransmitPower() call failed after set operation"

                        #Revert back to initial value
                        setMethod = "setRadioTransmitPower"
                        primitive = 'WIFIHAL_GetOrSetParamULongValue'
                        setValue = int(initGetValue)
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Successfully reverted back to inital value"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Unable to revert to initial value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "setRadioTransmitPower() call failed"
		break;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "getRadioTransmitPower() call failed"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "getRadioTransmitPowerSupported() call failed"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

