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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzGetRadioIEEE80211hEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>4</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check RadioIEEE80211h enable status of Radio 5GHz using wifi_getRadioIEEE80211hEnabled HAL API</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_238</test_case_id>
    <test_objective>To Check RadioIEEE80211h enable status of Radio 5GHz using wifi_getRadioIEEE80211hEnabled HAL API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioIEEE80211hSupported()
wifi_getRadioIEEE80211hEnabled()</api_or_interface_used>
    <input_parameters>methodName : getRadioIEEE80211hSupported
methodName : getRadioIEEE80211hEnabled
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get Radio IEEE80211hSupported status using wifi_getRadioIEEE80211hSupported() API.
3.If the status is Enabled get the Radio IEEE80211hEnabled status using wifi_getRadioIEEE80211hEnabled() API
4.Unload the Module.</automation_approch>
    <except_output>To get the RadioIEEE80211h enable status for 5GHz</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioIEEE80211hEnabled</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioIEEE80211hEnabled');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getRadioIEEE80211hSupported"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'

    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    enablestate = details.split(":")[1].strip(" ");
    if expectedresult in actualresult:
        if 'Enabled' in enablestate :
            expectedresult="SUCCESS";
            radioIndex = 1
            getMethod = "getRadioIEEE80211hEnabled"
            primitive = 'WIFIHAL_GetOrSetParamBoolValue'

            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)        
            if expectedresult in actualresult:
                print"TEST STEP : Get the Radio IEEE80211h Enabled Status for 5GHz";
                print"EXPECTED RESULT : Get the radio enabled status for 5GHz";
                print"ACTUAL RESULT : Got the radio enabled status for 5GHz";
                print"details",details;
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print"TEST STEP : Get the Radio IEEE80211h Enabled Status for 5GHz";
                print"EXPECTED RESULT : Get the radio enabled status for 5GHz";
                print"ACTUAL RESULT : Unable to get the radio enabled status for 5GHz";
                print"details",details;
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print"Radio IEEE80211h feature is not supported for 5GHz";
            tdkTestObj.setResultStatus("SUCCESS");
    else:
        print"wifi_getRadioIEEE80211hSupported() operation failed";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
