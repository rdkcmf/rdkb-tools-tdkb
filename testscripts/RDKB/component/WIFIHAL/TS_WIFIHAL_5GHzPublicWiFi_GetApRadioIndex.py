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
  <version>4</version>
  <name>TS_WIFIHAL_5GHzPublicWiFi_GetApRadioIndex</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get Public WiFi AP radio index using wifi_getApRadioIndex HAL API and validate the same</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_575</test_case_id>
    <test_objective>To get AP radio index using wifi_getApRadioIndex HAL API and validate the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApRadioIndex()</api_or_interface_used>
    <input_parameters>methodName: getApRadioIndex
idx   : 8</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested (WIFIHAL_GetOrSetParamIntValue  - func name - "If not exists already" WIFIHAL - module name Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIHAL_5GHzPublicWiFi_GetApRadioIndex.py)
3.Execute the generated Script(TS_WIFIHAL_5GHzPublicWiFi_GetApRadioIndex.py) using execution page of  Test Manager GUI
4.wifihalstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIHAL_GetOrSetParamIntValue through registered TDK wifihalstub function along with necessary Path Name as arguments
5.WIFIHAL_GetOrSetParamIntValue function will call Ccsp Base Function named "ssp_WIFIHALGetOrSetParamIntValue", that inturn will call WIFIHAL Library Function wifi_getApRadioIndex() function
6.Response(s)(printf) from TDK Component,Ccsp Library function and wifihalstub would be logged in Agent Console log based on the debug info redirected to agent console
7.wifihalstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result
8.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifihalstub</automation_approch>
    <expected_output>"""CheckPoint
1:wifi_getApRadioIndex from DUT should be available in Agent Console LogCheckPoint
2:TDK agent Test Function will log the test case result as PASS based on API response CheckPoint
3:Test Manager GUI will publish the result as SUCCESS in Execution page"""</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_GetApRadioIndex</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_GetApRadioIndex');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    #Checking for idx 9, Similary can be check for other APs 1,3,5,7,9,11,13,15
    getMethod = "getApRadioIndex"
    apIndex = apIndex_5G_Public_Wifi;
    primitive = 'WIFIHAL_GetOrSetParamIntValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

    expectedRadioIndexValue = 1;
    if expectedresult in actualresult:
       radioIndexValue = details.split(":")[1].strip()
       print "TEST STEP 1: Get the getApRadioIndex API";
       print "EXPECTED RESULT 1: Function Should return a Radio Index value(int) value";
       if expectedRadioIndexValue == int(radioIndexValue):
          print "getApRadioIndex function successful, %s"%details
          tdkTestObj.setResultStatus("SUCCESS");
          print "ACTUAL RESULT 1: Radio Index value associated with AP received Successfully: %s"%radioIndexValue;
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
           print "getApRadioIndex failed, %s"%details
           tdkTestObj.setResultStatus("FAILURE");
           print "ACTUAL RESULT 1:Failed to receive a Radio Index value: %s"%radioIndexValue;
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "getApRadioIndex failed"
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");