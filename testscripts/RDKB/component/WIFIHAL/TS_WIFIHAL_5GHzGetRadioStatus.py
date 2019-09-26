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
  <version>5</version>
  <name>TS_WIFIHAL_5GHzGetRadioStatus</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify if wifi_getRadioStatus is changed on changing the RadioEnable  using wifi_setRadioEnable() for 5GHz</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_236</test_case_id>
    <test_objective>To verify if wifi_getRadioStatus is changed on changing the RadioEnable  using wifi_setRadioEnable() for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioEnable()
wifi_getRadioStatus()</api_or_interface_used>
    <input_parameters>methodName : getRadioStatus
methodName : setRadioEnable
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the Module.
2.Get the radio status by invoking the wifi_getRadioStatus() api.
3.If it is enabled,disable it or if it is disabled,enable it using the wifi_setRadioEnable() api.
4.Verify whether the radio status has changed using wifi_getRadioStatus() api.
5.Revert the toggle state to the initial value using wifi_setRadioEnable() api.
6.Unload the module.</automation_approch>
    <except_output>wifi_getRadioStatus should change on changing the RadioEnable  using wifi_setRadioEnable() for 2.4GHz</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioStatus</test_script>
    <skipped>No</skipped>
    <release_version/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioStatus');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getRadioEnable"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    if expectedresult in actualresult:
        enable1 = details.split(":")[1].strip()
        obj.setLoadModuleStatus("SUCCESS");

        expectedresult="SUCCESS";
        radioIndex = 1
        getMethod = "getRadioStatus"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
        if expectedresult in actualresult:
            enable = details.split(":")[1].strip()
            if enable == enable1:
                if "Enabled" in enable1:
	            oldEnable = 1
                    newEnable = 0
                else:
	            oldEnable = 0
                    newEnable = 1
                setMethod = "setRadioEnable"
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, setMethod)

                if expectedresult in actualresult :
                    print "Enable state toggled using set"
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                    if expectedresult in actualresult and enable not in details.split(":")[1].strip():
                        print "setRadioEnable and getRadioStatus values are same"
                        #Reverting back to initial value
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, oldEnable, setMethod)

                        if expectedresult in actualresult :
                            print "Enable status reverted back";
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Couldn't revert enable status";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "setRadioEnable and getRadioStatus values are not same"
		        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "Unable to toggle the Enable state using set"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print"getRadioEnable and getRadioStatus values are not same"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print"getRadioStatus() operation failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
           print"getRadioEnable() operation failed"
           tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
