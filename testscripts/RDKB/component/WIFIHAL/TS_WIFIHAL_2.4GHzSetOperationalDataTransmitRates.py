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
  <version>2</version>
  <name>TS_WIFIHAL_2.4GHzSetOperationalDataTransmitRates</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the operational data transmit rate using wifi_setRadioOperationalDataTransmitRates() and get it using wifi_getRadioOperationalDataTransmitRates() for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_120</test_case_id>
    <test_objective>To set the operational data transmit rate using wifi_setRadioOperationalDataTransmitRates() and get it using wifi_getRadioOperationalDataTransmitRates()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioOperationalDataTransmitRates()
wifi_getRadioSupportedDataTransmitRates()
wifi_setRadioOperationalDataTransmitRates()</api_or_interface_used>
    <input_parameters>methodName : getSupportedDataTransmitRates
methodName : getOperationalDataTransmitRates
methodName : setOperationalDataTransmitRates
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioOperationalDataTransmitRates()  to get the current data transmit rate
3.Get the supported transmit rate using wifi_getRadioSupportedDataTransmitRates()  
4.Invoke wifi_setRadioOperationalDataTransmitRates() to set a value present in SupportedDataTransmitRates
5. Get the previously set OperationalDataTransmitRate and verify
5. Unload wifihal module</automation_approch>
    <except_output>OperationalDataTransmitRates set using wifi_setRadioOperationalDataTransmitRates() should be obtained with get api wifi_getRadioOperationalDataTransmitRates()</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetOperationalDataTransmitRates</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetOperationalDataTransmitRates');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getSupportedDataTransmitRates"
    primitive = "WIFIHAL_GetOrSetParamStringValue"
    #Invoke the api wifi_getRadioSupportedDataTransmitRates() using wifiUtility function
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

    if expectedresult in actualresult :
        supportedRates = details.split(":")[1].strip().split(",")

        getMethod = "getOperationalDataTransmitRates"
        #Invoke the api wifi_getRadioOperationalDataTransmitRates() using wifiUtility function
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        if expectedresult in actualresult :
            operationalRates = details.split(":")[1].strip()

            for setOperRate in supportedRates:
                setMethod = "setOperationalDataTransmitRates"
		print "Set OperationalDataTransmitRate = %s"%setOperRate
                #Invoke the api wifi_setRadioOperationalDataTransmitRates() using wifiUtility function
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setOperRate, setMethod)
                if expectedresult in actualresult :
                    print "OperationalDataTransmitRates set successfully with value %s"%setOperRate

                    getMethod = "getOperationalDataTransmitRates"
                    #Invoke the api wifi_getRadioOperationalDataTransmitRates() using wifiUtility function
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
                    getOperRate = details.split(":")[1].strip()
                    #Compare the results of set and get
                    if expectedresult in actualresult and setOperRate == getOperRate:
                        print "SUCCESS: Set and get OperationalDataTransmitRates are the same"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "FAILURE: Set and get OperationalDataTransmitRates are not the same"
                        tdkTestObj.setResultStatus("FAILURE");

                    #Reverting the OperationalDataTransmitRate to initial value
                    setMethod = "setOperationalDataTransmitRates"
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, operationalRates, setMethod)
                    if expectedresult in actualresult :
                        print "Successfully reverted to initial value"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Unable to revert to initial value"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "Unable to set OperationalDataTransmitRates with value %s"%setOperRate
                    tdkTestObj.setResultStatus("FAILURE");
                break;
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

