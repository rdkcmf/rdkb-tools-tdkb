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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetRadioBasicDataTransmitRates</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the Basic Data Transmit Rates for 5GHz radio using wifi_setRadioBasicDataTransmitRates HAL API and validate the same by getting it with wifi_getRadioBasicDataTransmitRates</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_123</test_case_id>
    <test_objective>To set the basic data transmit rate using wifi_setRadioBasicDataTransmitRates() and get it using wifi_getRadioBasicDataTransmitRates()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioBasicDataTransmitRates()
wifi_getRadioSupportedDataTransmitRates()
wifi_setRadioBasicDataTransmitRates()</api_or_interface_used>
    <input_parameters>methodName : getSupportedDataTransmitRates
methodName : getRadioBasicDataTransmitRates
methodName : setRadioBasicDataTransmitRates
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadiobasicDataTransmitRates()  to get the current data transmit rate
3.Get the supported transmit rate using wifi_getRadioSupportedDataTransmitRates()  and check if current value is from this list
4.Invoke wifi_setRadioBasicDataTransmitRates() to set a value present in SupportedDataTransmitRates but not in BasicDataTransmitRates
5. Get the previously set BasicDataTransmitRate and verify
5. Unload wifihal module</automation_approch>
    <except_output>BasicDataTransmitRates set using wifi_setRadioBasicDataTransmitRates() should be obtained with get api wifi_getRadioBasicDataTransmitRates()</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioBasicDataTransmitRates</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioBasicDataTransmitRates');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getSupportedDataTransmitRates"
    primitive = "WIFIHAL_GetOrSetParamStringValue"
    #Invoke the api wifi_getRadioSupportedDataTransmitRates() using wifiUtility function
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

    if expectedresult in actualresult :
        supportedRates = details.split(":")[1].strip().split(",")

        getMethod = "getRadioBasicDataTransmitRates"
        #Invoke the api wifi_getRadioBasicDataTransmitRates() using wifiUtility function
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        if expectedresult in actualresult :
            basicRates = details.split(":")[1].strip()
            basicRatesList = details.split(":")[1].strip().split(",");

            for setBasicRate in supportedRates:
                if setBasicRate not in basicRatesList:
                    #Invoke the api wifi_setRadioBasicDataTransmitRates() using wifiUtility function
                    setMethod = "setRadioBasicDataTransmitRates"
		    print "Set BasicDataTransmitRate = %s"%setBasicRate
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setBasicRate, setMethod)
                    if expectedresult in actualresult :
                        print "BasicDataTransmitRates set successfully with value %s"%setBasicRate

                        getMethod = "getRadioBasicDataTransmitRates"
                        #Invoke the api wifi_getRadioBasicDataTransmitRates() using wifiUtility function
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
                        getBasicRate = details.split(":")[1].strip()
                        #Compare the results of set and get
                        if expectedresult in actualresult and setBasicRate == getBasicRate:
                            print "SUCCESS: Set and get BasicDataTransmitRates are the same"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "FAILURE: Set and get BasicDataTransmitRates are not the same"
                            tdkTestObj.setResultStatus("FAILURE");

                        #Reverting the BasicDataTransmitRate to initial value
                        setMethod = "setRadioBasicDataTransmitRates"
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, basicRates, setMethod)
                        if expectedresult in actualresult :
                            print "Successfully reverted to initial value"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Unable to revert to initial value"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "Unable to set BasicDataTransmitRates with value %s"%setBasicRate
                        tdkTestObj.setResultStatus("FAILURE");
                    break;
                else:
                    continue;
        else:
            print "getRadioBasicDataTransmitRates() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "getSupportedDataTransmitRates() call failed"
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

