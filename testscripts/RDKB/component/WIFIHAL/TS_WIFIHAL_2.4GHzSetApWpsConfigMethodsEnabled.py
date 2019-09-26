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
  <name>TS_WIFIHAL_2.4GHzSetApWpsConfigMethodsEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the ApWpsConfigMethodsEnabled for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_158</test_case_id>
    <test_objective>To set and get  the ApWpsConfigMethodsEnabled for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsConfigMethodsEnabled()
wifi_setApWpsConfigMethodsEnabled()</api_or_interface_used>
    <input_parameters>methodName : getApWpsConfigMethodsEnabled
methodName : setApWpsConfigMethodsEnabled
ApIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApWpsConfigMethodsEnabled() and save the get value
3. Invoke wifi_getApWpsConfigMethodsSupported() 
 and choose a WpsConfigMethod from the list 4. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_setApWpsConfigMethodsEnabled()
5. Invoke wifi_getApWpsConfigMethodsEnabled() to get the previously set value. 
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the WpsConfigMethod back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>Set and get values of WpsConfigMethod should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApWpsConfigMethodsEnabled</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApWpsConfigMethodsEnabled');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 0
    getMethod = "getApWpsConfigMethodsEnabled"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    #Calling the method from wifiUtility to execute test case and set result status for the test. Fetching the WPS Config Mode Supported.
    tdkTestObj1, actualresult1, details1 = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", "getApWpsConfigMethodsSupported")

    if expectedresult in actualresult and expectedresult in actualresult1:
        supportedWpsConfigModes = list(details1.split(":")[1].strip().split(','))
        supportedWpsConfigModes = map(str.strip, supportedWpsConfigModes)
        initConfigMethod = details.split(":")[1].strip()
        initConfigMethodList = map(str.strip, list(details.split(":")[1].strip().split(',')))

        for setConfigMethod in supportedWpsConfigModes:
            if setConfigMethod in initConfigMethodList:
                continue;
            else:
                expectedresult="SUCCESS";
                apIndex = 0
                setMethod = "setApWpsConfigMethodsEnabled"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                #Calling the method to execute wifi_setApWpsConfigMethodsEnabled()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setConfigMethod, setMethod)

                if expectedresult in actualresult:
                    expectedresult="SUCCESS";
                    apIndex = 0
                    getMethod = "getApWpsConfigMethodsEnabled"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'

                    #Calling the method from wifiUtility to execute test case and set result status for the test.
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                    if expectedresult in actualresult:
                        finalConfigMethod = details.split(":")[1].strip()
                        if finalConfigMethod == setConfigMethod:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP: Compare the set and get values of ApWpsConfigMethodsEnabled"
                            print "EXPECTED RESULT: Set and get values of ApWpsConfigMethodsEnabled should be same"
                            print "ACTUAL RESULT: Set and get values of ApWpsConfigMethodsEnabled are the same"
                            print "setConfigMethod = ",setConfigMethod
                            print "getConfigMethod = ",finalConfigMethod
                            print "TEST EXECUTION RESULT : SUCCESS"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP: Compare the set and get values of ApWpsConfigMethodsEnabled"
                            print "EXPECTED RESULT: Set and get values of ApWpsConfigMethodsEnabled should be same"
                            print "ACTUAL RESULT: Set and get values of ApWpsConfigMethodsEnabled are NOT the same"
                            print "setConfigMethod = ",setConfigMethod
                            print "getConfigMethod = ",finalConfigMethod
                            print "TEST EXECUTION RESULT : FAILURE"

                        #Revert the ConfigMethod back to initial value
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initConfigMethod, setMethod)
                        if expectedresult in actualresult:
                            print "Successfully reverted the ApWpsConfigMethod to initial value"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Unable to revert the ApWpsConfigMethod"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "wifi_getApWpsConfigMethodsEnabled() call failed after set operation"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "wifi_setApWpsConfigMethodsEnabled() call failed"
                    tdkTestObj.setResultStatus("FAILURE");
            break;
    else:
        print "wifi_getApWpsConfigMethodsEnabled() failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

