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
  <version>3</version>
  <name>TS_WIFIHAL_2.4GHzSetApSecuritySecondaryRadiusServer_NonEnterpriseMode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set Security Secondary Radius Server details with non-enterprise modes and check whether the return status is failure</synopsis>
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
    <test_case_id>TS_WIFIHAL_531</test_case_id>
    <test_objective>Set Security Secondary Radius Server details with non-enterprise modes and check whether the return status is failure</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityModeSupported()
wifi_setApSecuritySecondaryRadiusServer()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodname : getApSecurityModeSupported
methodName : setApSecuritySecondaryRadiusServer
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApSecurityModeSupported() and get the supported security modes.
3. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApSecurityModeEnabled() and save the initial value.
4. Set the security modes to Non Enterprise modes from the supported modes list by invoking the API wifi_setApSecurityModeEnabled(). Cross verify the set operation by invoking wifi_getApSecurityModeEnabled() API.
5. For each Non Enterprise mode, try to set the Security Radius Server details by invoking wifi_setApSecuritySecondaryRadiusServer(). Check if the Set operation returns Failure as expected.
6. Revert back to initial Security mode
7. Unload Wifihal module.</automation_approch>
    <expected_output>Security Secondary Radius Server details set with non-enterprise modes should return failure</expected_output>
    <priority>High</priority>
    <test_stub_interface>Wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApSecuritySecondaryRadiusServer_NonEnterpriseMode</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, IPAddress, port, RadiusSecret, methodname):
    #Prmitive test case which is associated to this Script
    tdkTestObj = obj.createTestStep(primitive);
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",radioIndex);
    tdkTestObj.addParameter("methodName", methodname);
    tdkTestObj.addParameter("IPAddress", IPAddress);
    tdkTestObj.addParameter("port", port);
    tdkTestObj.addParameter("RadiusSecret", RadiusSecret);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj, actualresult, details);

def setSecondaryRadiusServer(idx, setMode) :
    expectedresult = "FAILURE";
    radioIndex = idx;
    setMethod = "setApSecuritySecondaryRadiusServer"
    primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
    IPAddress = "1.1.2.2"
    port = 1234
    RadiusSecret = "12345"
    #Calling the method to execute wifi_setApSecuritySecondaryRadiusServer()
    tdkTestObj, actualresult, details = GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, IPAddress, port, RadiusSecret, setMethod)
    print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"
    print "TEST STEP : Should not set the ApSecuritySecondaryRadiusServer details in the Non Enterprise mode %s"%setMode
    print "EXPECTED RESULT : Should not set the IPAddress, port and RadiusSecret"
    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT : IPAddress, port and RadiusSecret are not set successfully in the Non Enterprise mode"
        print "TEST EXECUTION RESULT : SUCCESS"
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT : IPAddress, port and RadiusSecret are set successfully in the Non Enterprise mode"
        print "TEST EXECUTION RESULT : FAILURE"

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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApSecuritySecondaryRadiusServer_NonEnterpriseMode');
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        apIndex = idx;
        getMethod = "getApSecurityModesSupported"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'
        #Calling the method to execute wifi_getApSecurityModeSupported()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
        if expectedresult in actualresult:
            supportedModes = details.split(":")[1].strip()
            supportedModes = supportedModes.split(',')
            expectedresult="SUCCESS";
            apIndex = idx;
            getMethod = "getApSecurityModeEnabled"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
            #Calling the method to execute wifi_getApSecurityModeEnabled()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
            if expectedresult in actualresult:
                initMode = details.split(":")[1].strip()
                if initMode in supportedModes:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Initial ApSecurityMode is from the supported modes"
                    NonEnterpriseModes = list(filter(lambda x: 'Personal' in x, supportedModes))
                    print "Setting and checking the Non Enterprise security modes : ",NonEnterpriseModes
                    for setMode in NonEnterpriseModes :
                        print "Setting the ApSecurityMode to ",setMode
                        expectedresult="SUCCESS";
                        apIndex = idx;
                        setMethod = "setApSecurityModeEnabled"
                        primitive = 'WIFIHAL_GetOrSetParamStringValue'
                        #Calling the method to execute wifi_setApSecurityModeEnabled()
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)
                        if expectedresult in actualresult:
                            expectedresult="SUCCESS";
                            apIndex = idx;
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
                                    setSecondaryRadiusServer(idx, setMode);
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP: Compare the set and get values of ApSecurityModeEnabled"
                                    print "EXPECTED RESULT: Set and get values of ApSecurityModeEnabled should be same"
                                    print "ACTUAL RESULT: Set and get values of ApSecurityModeEnabled are NOT the same"
                                    print "setMode = ",setMode
                                    print "getMode = ",finalMode
                                    print "TEST EXECUTION RESULT : FAILURE"
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "wifi_getApSecurityModeEnabled() call failed after set operation"
                                print "TEST EXECUTION RESULT : FAILURE"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "wifi_setApSecurityModeEnabled() call failed"
                            print "TEST EXECUTION RESULT : FAILURE"

                    #Revert the ApSecurityModeEnabled back to initial value
                    expectedresult="SUCCESS";
                    apIndex = idx;
                    setMethod = "setApSecurityModeEnabled"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initMode, setMethod)
                    if expectedresult in actualresult:
                        print "Successfully reverted the ApSecurityModeEnabled to initial value"
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST EXECUTION RESULT : SUCCESS"
                    else :
                        print "Unable to revert the ApSecurityModeEnabled"
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST EXECUTION RESULT : FAILURE"
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Initial ApSecurityMode is not in supported modes"
                    print "TEST EXECUTION RESULT : FAILURE"
            else :
                print "wifi_getApSecurityModeEnabled() failed"
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST EXECUTION RESULT : FAILURE"
        else :
            print "wifi_getApSecurityModeSupported() failed"
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST EXECUTION RESULT : FAILURE"
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

