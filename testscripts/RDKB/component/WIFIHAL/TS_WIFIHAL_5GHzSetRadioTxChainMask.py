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
  <name>TS_WIFIHAL_5GHzSetRadioTxChainMask</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get RadioTxChainMask for 5GHz</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_217</test_case_id>
    <test_objective>To set and get the RadioTxChainMask for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioTxChainMask()
wifi_setRadioTxChainMask()</api_or_interface_used>
    <input_parameters>methodName: getRadioTxChainMask
methodName: setRadioTxChainMask
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using  WIFIHAL_GetOrSetParamIntValue invoke wifi_getRadioTxChainMask()
3. Using WIFIHAL_GetOrSetParamIntValue
 invoke wifi_setRadioTxChainMask and set a valid value from the range 1-32
4. Invoke wifi_getRadioTxChainMask() to get the previously set value.
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the TxChainMask back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>The set and get values of TxChainMask should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioTxChainMask</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioTxChainMask');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getRadioTxChainMask"
    primitive = 'WIFIHAL_GetOrSetParamIntValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    #wifi_getRadioTxChainMask() outputs the number of Tx streams
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult :
        initMask = int(details.split(":")[1].strip());
        print "initMask:",initMask
        tdkTestObj.setResultStatus("SUCCESS");

        expectedresult="SUCCESS";
        radioIndex = 1
        setMethod = "setRadioTxChainMask"
        r = range(1,initMask) + range(initMask+1, 32)
        setMask = random.choice(r)
        primitive = 'WIFIHAL_GetOrSetParamIntValue'
        print "Set RadioTxChainMask = ",setMask

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setMask, setMethod)

        if expectedresult in actualresult :
            expectedresult="SUCCESS";
            radioIndex = 1
            getMethod = "getRadioTxChainMask"
            primitive = 'WIFIHAL_GetOrSetParamIntValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

            if expectedresult in actualresult :
                finalMask= int(details.split(":")[1]);
                if setMask == finalMask:
                    print "TEST STEP : Comparing the set and get values of RadioTxChainMask"
                    print "EXPECTED RESULT : Set and get values should be the same"
                    print "ACTUAL RESULT : Set and get values are the same"
                    print "Set RadioTxChainMask = ",setMask
                    print "Get RadioTxChainMask =",finalMask;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");

                else:
                    print "TEST STEP : Comparing the set and get values of RadioTxChainMask"
                    print "EXPECTED RESULT : Set and get values should be the same"
                    print "ACTUAL RESULT : Set and get values are NOT the same"
                    print "Set RadioTxChainMask = ",setMask
                    print "Get RadioTxChainMask =",finalMask;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "wifi_getRadioTxChainMask function failed after set operation"

            #Revert to initial TxChainMask
            primitive = 'WIFIHAL_GetOrSetParamIntValue'
            setMethod = "setRadioTxChainMask"
            setMask = initMask

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setMask, setMethod)

            if expectedresult in actualresult :
                print "Successfully reverted to initial value"
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "Unable  to revert to initial value"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "wifi_setRadioTxChainMask() function failed"
    else:
        print "wifi_getRadioTxChainMask() call failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

