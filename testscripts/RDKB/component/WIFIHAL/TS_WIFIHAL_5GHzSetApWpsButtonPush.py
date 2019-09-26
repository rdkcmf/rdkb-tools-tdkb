##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>12</version>
  <name>TS_WIFIHAL_5GHzSetApWpsButtonPush</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>9</primitive_test_version>
  <status>FREE</status>
  <synopsis>To  start the WPS session for  5GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_334</test_case_id>
    <test_objective>To  start the WPS session for 5GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApWpsButtonPush()</api_or_interface_used>
    <input_parameters>methodName : setApWpsButtonPush
radioIndex : 1
setPIN : 3</input_parameters>
    <automation_approch>1.Load the module.
2.Enable the  WPS daemon if it is not enabled already.
3.Set the WpsButtonPush  for 5GHz by passing the parameters radioindex and setPin using wifi_setApWpsButtonPush() API by  invoking WIFIHAL_GetOrSetParamStringValue'
4. .Check if the api call is success, else return FAILURE from the script
5.Disable the Wps daemon if it was enabled in step 2.
6.Unload the module.</automation_approch>
    <except_output>Successfully set and press the WPS push button for 5GHz AP</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApWpsButtonPush</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApWpsButtonPush');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getApWpsEnable"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    print "TEST STEP1: Get ApWpsEnable state"
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        enable = details.split(":")[1].strip()
        if "Enabled" not in enable:
            print "Access point Wps is Disabled"
            oldEnable = 0
            newEnable = 1
            setMethod = "setApWpsEnable"
            print "TEST STEP2: Toggle the disabled ApWpsEnable state to enable"
            #Toggle the disabled state to enable state
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, newEnable, setMethod)
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Access point Wps is Enabled"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Unable to enable the WPS"
        else:
            oldEnable = 1
            print "Access point is already in Enabled state";
            
        radioIndex = 1
        setPIN = '3'
        setMethod = "setApWpsButtonPush"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'


        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setPIN, setMethod)

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP3 : Set the ApWpsButtonPush"
            print "EXPECTED RESULT : Set operation should return SUCCESS"
            print "ACTUAL RESULT : Set operation returned SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP3 : Set the ApWpsButtonPush"
            print "EXPECTED RESULT : Set operation should return SUCCESS"
            print "ACTUAL RESULT : Set operation returned FAILURE"
        #Revert back to original value
        print "TEST STEP4: Revert the ApWpsEnable state"
        if oldEnable == 0:
            setMethod = "setApWpsEnable"
            primitive = 'WIFIHAL_GetOrSetParamBoolValue'
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, oldEnable, setMethod)
            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "Set operation reverted to initial state"
                getMethod = "getApWpsEnable"
                primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    enable = details.split(":")[1].strip()
                    if "Enabled" not in enable:
                        print "Access point Wps is Disabled"
                    else:
                        print "ACTUAL RESULT : set operation failed"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print ": get operation failed after reverting"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print ": set operation failed while reverting"
        else:
            print "ACTUAL RESULT : No need reverting back to original value"
    else:
        print "Unable to Get Ap WPS enabled state"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
