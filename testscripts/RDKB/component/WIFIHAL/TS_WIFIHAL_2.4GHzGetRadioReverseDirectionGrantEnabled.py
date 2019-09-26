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
  <name>TS_WIFIHAL_2.4GHzGetRadioReverseDirectionGrantEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if RadioReverseDirectionGrant is supported and if supported check if it is enabled for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_250</test_case_id>
    <test_objective>To check if RadioReverseDirectionGrant is supported and if supported check if it is enabled for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioReverseDirectionGrantSupported()
wifi_getRadioReverseDirectionGrantEnable()</api_or_interface_used>
    <input_parameters>methodName: getRadioReverseDirectionGrantSupported
methodName: getRadioReverseDirectionGrantEnable
radioIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getRadioReverseDirectionGrantSupported() API.
3.If it is supported, invoke wifi_getRadioReverseDirectionGrantEnable() to get the present status, else return SUCCESS and exit.
4.Unload the module.</automation_approch>
    <except_output>If ReverseDirectionGrant is supported, enable status should return either Enabled or Disabled.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetRadioReverseDirectionGrantEnabled</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioReverseDirectionGrantEnabled');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getRadioReverseDirectionGrantSupported"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    #Getting if ReverseDirectionGrant is supported or not
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        enable = details.split(":")[1].strip()
        if "Enabled" in enable:
            expectedresult="SUCCESS";
            radioIndex = 0
            getMethod = "getRadioReverseDirectionGrantEnable"
            primitive = 'WIFIHAL_GetOrSetParamBoolValue'
            #Getting the default enable state
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                enable = details.split(":")[1].strip()
                if "Enabled" in enable:
                    print "Reverse Direction Grant is Enabled for Radio 2.4GHz"
                else:
                    print "Reverse Direction Grant is Disabled for Radio 2.4GHz"
            else:
                print "getRadioReverseDirectionGrantEnable() failed"
                tdkTestObj.setResultStatus("FAILURE");
	else:
	    print "RadioReverseDirectionGrant feature not supported"
	    tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "getRadioReverseDirectionGrantSupported() failed"
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

