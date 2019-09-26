##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_5GHzIsAutoChannelRefreshPeriodSupported</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if AutoChannelRefreshPeriod is supported using wifi_getRadioAutoChannelRefreshPeriodSupported(), if supported, get refresh period using wifi_getRadioAutoChannelRefreshPeriod()</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_08</test_case_id>
    <test_objective>Check if AutoChannelRefreshPeriod is supported using wifi_getRadioAutoChannelRefreshPeriodSupported(), if supported, get refresh period using wifi_getRadioAutoChannelRefreshPeriod()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioAutoChannelRefreshPeriodSupported()
wifi_getRadioAutoChannelRefreshPeriod()</api_or_interface_used>
    <input_parameters>methodName : getAutoChannelRefreshPeriodSupported
methodName : getAutoChannelRefreshPeriod
radioIndex     :    1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioAutoChannelRefreshPeriodSupported()  to to check if AutoChannelRefreshPeriod is supported or not 
3.If supported, get the refresh period using wifi_getRadioAutoChannelRefreshPeriod()
4. If not supported also return success
5. Unload wifihal module</automation_approch>
    <except_output>Radio AutoChannelRefreshPeriod should be supported</except_output>
    <priority>High</priority>
    <test_stub_interface>WiFiAgent</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzIsAutoChannelRefreshPeriodSupported</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzIsAutoChannelRefreshPeriodSupported');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getAutoChannelRefreshPeriodSupported"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult :
        enable = details.split(":")[1].strip()
        if "Enabled" in enable:
            print "AutoChannelRefreshPeriod is Supported"
            tdkTestObj.setResultStatus("SUCCESS");

            getMethod = "getAutoChannelRefreshPeriod"
            primitive = 'WIFIHAL_GetOrSetParamULongValue'
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

            if expectedresult in actualresult :
                period = int(details.split(":")[1].strip())
                print "Refresh period retreived as %d" %period
            else:
                print "getAutoChannelRefreshPeriod() failed"
        else:
            print "AutoChannelRefreshPeriod is not Supported"
            tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "AutoChannelRefreshPeriod() failed"

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

