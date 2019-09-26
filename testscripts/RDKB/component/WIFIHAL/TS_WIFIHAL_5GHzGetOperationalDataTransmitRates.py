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
  <version>8</version>
  <name>TS_WIFIHAL_5GHzGetOperationalDataTransmitRates</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the operational data transmit rate using wifi_getRadioOperationalDataTransmitRates() and see if its a subset of values returned by wifi_getRadioSupportedDataTransmitRates()</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_05</test_case_id>
    <test_objective>Get the operational data transmit rate using wifi_getRadioOperationalDataTransmitRates() and see if its a subset of values returned by wifi_getRadioSupportedDataTransmitRates()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioOperationalDataTransmitRates()
wifi_getRadioSupportedDataTransmitRates()</api_or_interface_used>
    <input_parameters>methodName : getSupportedDataTransmitRates
methodName : getOperationalDataTransmitRates
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioOperationalDataTransmitRates()  to get the current data transmit rate
3.Get the supported transmit rate using wifi_getRadioSupportedDataTransmitRates()  and check if current value is from this list
5. Unload wifihal module</automation_approch>
    <except_output>OperationalDataTransmitRates should be a subset of supported data transmit rates</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetOperationalDataTransmitRates</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetOperationalDataTransmitRates');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    flag = 1
    getMethod = "getSupportedDataTransmitRates"
    #getMethod = "getRadioSupportedFrequencyBands"
    primitive = "WIFIHAL_GetOrSetParamStringValue"
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

    if expectedresult in actualresult :
        supportedRates = details.split(":")[1].strip().split(",")

        getMethod = "getOperationalDataTransmitRates"
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        if expectedresult in actualresult :
            operationalRates = details.split(":")[1].strip().split(",")

	    for rate in operationalRates:
		if rate not in supportedRates:
		    flag = 0;
		    break;
	    if flag == 1:
                print "OperationalDataTransmitRates is in the list of SupportedDataTransmitRates"
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "OperationalDataTransmitRates is not in the list of SupportedDataTransmitRates"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "getOperationalDataTransmitRates() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "getSupportedDataTransmitRates() call failed"
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

