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
  <name>TS_WIFIHAL_5GHzGetRadioCarrierSenseThresholdInUse</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the RadioCarrierSenseThresholdInuse value for 5GHz radio using wifi_getRadioCarrierSenseThresholdRange HAL API and validate the same with the Radio  CarrierSenseThresholdRange whether the value is inside the range</synopsis>
  <groups_id>4</groups_id>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_240</test_case_id>
    <test_objective>To get the RadioCarrierSenseThresholdInuse value for 5GHz radio using wifi_getRadioCarrierSenseThresholdRange HAL API and validate the same with the Radio  CarrierSenseThresholdRange whether the value is inside the range</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioCarrierSenseThresholdRange(),wifi_getRadioCarrierSenseThresholdInUse()</api_or_interface_used>
    <input_parameters>methodName   :   getRadioCarrierSenseThresholdRange,getRadioCarrierSenseThresholdInUse
apIndex      :   0</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested (WIFIHAL_GetOrSetParamIntValue  - func name - "If not exists already" WIFIHAL - module name Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIHAL_5GHzGetRadioCarrierSenseThresholdInUse.py)
3.Execute the generated Script(TS_WIFIHAL_5GHzGetRadioCarrierSenseThresholdInUse.py) using execution page of  Test Manager GUI
4.wifihalstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIHAL_GetOrSetParamUIntValue through registered TDK wifihalstub function along with necessary Path Name as arguments
5.WIFIHAL_GetOrSetParamIntValue function will call Ccsp Base Function named "ssp_WIFIHALGetOrSetParamUIntValue", that inturn will call WIFIHAL Library wifi_getRadioCarrierSenseThresholdRange(),wifi_getRadioCarrierSenseThresholdInUse() function
6.Response(s)(printf) from TDK Component,Ccsp Library function and wifihalstub would be logged in Agent Console log based on the debug info redirected to agent console
7.wifihalstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result
8.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifihalstub</automation_approch>
    <except_output>"
CheckPoint
1:wifi_getRadioCarrierSenseThresholdRange,wifi_getRadioCarrierSenseThresholdInUse from DUT should be available in Agent Console LogCheckPoint
2:TDK agent Test Function will log the test case result as PASS based on API response CheckPoint
3:Test Manager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioCarrierSenseThresholdInUse</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioCarrierSenseThresholdInUse');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getRadioCarrierSenseThresholdRange"
    primitive = 'WIFIHAL_GetOrSetParamIntValue'

    #Calling the method from wifiUtility to execute test case and get the result of getRadioCarrierSenseThresholdRange()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

    if expectedresult in actualresult:
        CarrierSenseThresholdRange = details.split(":")[1].strip()
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Carrier Sense Threshold Range";
        print "EXPECTED RESULT 1: Function Should return a Carrier Sense Threshold value";
        print "ACTUAL RESULT 1: Carrier Sense Threshold Range Received Successfully,value is:",CarrierSenseThresholdRange;
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Calling the method from wifiUtility to execute test case and get the result of wifi_getRadioCarrierSenseThresholdInUse()
        expectedresult="SUCCESS";
        apIndex = 1
        getMethod = "getRadioCarrierSenseThresholdInUse"
        primitive = 'WIFIHAL_GetOrSetParamIntValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            CarrierSenseThresholdInUse = details.split(":")[1].strip()
            print "TEST STEP 2: Get the Carrier Sense Threshold In use";
            print "EXPECTED RESULT 2: Function Should return a Carrier Sense Threshold value";
            print "ACTUAL RESULT 2: Carrier Sense Threshold In use Received Successfully,value is:",CarrierSenseThresholdInUse;
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Comparing the Carrier Sense ThresholdInUse with Carrier Sense ThresholdRange
            if CarrierSenseThresholdInUse < CarrierSenseThresholdRange :
                tdkTestObj.setResultStatus("SUCCESS");
                print "CarrierSenseThresholdInUse is inside the CarrierSenseThreshold Range"
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "CarrierSenseThresholdInUse is outside the CarrierSenseThreshold Range"
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Carrier Sense Threshold In use";
            print "EXPECTED RESULT 2: Function Should return a Carrier Sense Threshold value";
            print "ACTUAL RESULT 2: Failed to get the Carrier Sense Threshold In use";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Carrier Sense Threshold Range";
        print "EXPECTED RESULT 1: Function Should return a Carrier Sense Threshold value";
        print "ACTUAL RESULT 1: Failed to get the the Carrier Sense Threshold Range"
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");


