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
  <name>TS_WIFIHAL_5GHzSetApSecurityModeEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the security mode for 5GHz</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_160</test_case_id>
    <test_objective>To set and get the security mode for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
ApIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApSecurityModeEnabled() and save the get value
3. Choose a SecurityMode from supported SecurityModes list and using  WIFIHAL_GetOrSetParamStringValue invoke wifi_setApSecurityModeEnabled()
4. Invoke wifi_getApSecurityModeEnabled() to get the previously set value. 
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the SecurityMode back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of SecurityMode should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApSecurityModeEnabled</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApSecurityModeEnabled');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getApSecurityModesSupported"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method to execute wifi_getApSecurityModeSupported()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
        supportedModes = details.split(":")[1].strip()

        expectedresult="SUCCESS";
        apIndex = 1
        getMethod = "getApSecurityModeEnabled"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method to execute wifi_getApSecurityModeEnabled()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
            initMode = details.split(":")[1].strip()
            if initMode in supportedModes.split(','):
                print supportedModes.split(',');
                tdkTestObj.setResultStatus("SUCCESS");
                for setMode in supportedModes.split(','):
                    if setMode == initMode:
                        continue;
                    else:
                        expectedresult="SUCCESS";
                        apIndex = 1
                        setMethod = "setApSecurityModeEnabled"
                        primitive = 'WIFIHAL_GetOrSetParamStringValue'

                        #Calling the method to execute wifi_setApSecurityModeEnabled()
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

                        if expectedresult in actualresult:
                            expectedresult="SUCCESS";
                            apIndex = 1
                            getMethod = "getApSecurityModeEnabled"
                            primitive = 'WIFIHAL_GetOrSetParamStringValue'

                            #Calling the method to execute wifi_getApSecurityModeEnabled()
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                            if expectedresult in actualresult:
                                finalMode = details.split(":")[1].strip()
                                if finalMode == setMode:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP: Compare the set and get values of ApSecurityModeEnabled"
                                    print "EXPECTED RESULT: Set and get values of ApSecurityModeEnabled should be same"
                                    print "ACTUAL RESULT: Set and get values of ApSecurityModeEnabled are the same"
                                    print "setMode = ",setMode
                                    print "getMode = ",finalMode
                                    print "TEST EXECUTION RESULT : SUCCESS"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP: Compare the set and get values of ApSecurityModeEnabled"
                                    print "EXPECTED RESULT: Set and get values of ApSecurityModeEnabled should be same"
                                    print "ACTUAL RESULT: Set and get values of ApSecurityModeEnabled are NOT the same"
                                    print "setMode = ",setMode
                                    print "getMode = ",finalMode
                                    print "TEST EXECUTION RESULT : FAILURE"

                                #Revert the ApSecurityModeEnabled back to initial value
                                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initMode, setMethod)
                                if expectedresult in actualresult:
                                    print "Successfully reverted the ApSecurityModeEnabled to initial value"
                                    tdkTestObj.setResultStatus("SUCCESS");
                                else:
                                    print "Unable to revert the ApSecurityModeEnabled"
                                    tdkTestObj.setResultStatus("FAILURE");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "wifi_getApSecurityModeEnabled() call failed after set operation"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "wifi_setApSecurityModeEnabled() call failed"
                    break;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Initial ApSecurityMode is not in supported modes"
        else:
            print "wifi_getApSecurityModeEnabled() failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getApSecurityModeSupported() failed"
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

