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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>9</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_GetATMCapable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>4</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the api which returns the ATM capable value.</synopsis>
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
    <test_case_id>TC_WIFIHAL_361</test_case_id>
    <test_objective>To get the ATM enable status  in device using wifi_getATMCapable API .</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getATMCapable()</api_or_interface_used>
    <input_parameters>methodName : getATMCapable.
no input parameters.</input_parameters>
    <automation_approch>1.Load the module.
2.Get the  ATM capable status of the device attached to the AP by using wifi_getATMCapable,by calling in the wrapper file.
3. If Disabled from the details(it is unsupported) , it is counted as SUCCESS or else FAILURE.
4.Unload the module.</automation_approch>
    <except_output>Should successfully get the ATM capable value from the device by calling from the wrapper file.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_GetATMCapable</test_script>
    <skipped>No</skipped>
    <release_version>Nil</release_version>
    <remarks>None</remarks>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetATMCapable');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    #passing radio index as a place holder only
    radioIndex = 0
    getMethod = "getATMCapable"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    print "Before ExecuteWIFIHalCallMethod"

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    print "After ExecuteWIFIHalCallMethod"


    if expectedresult in actualresult:
        enablestate = details.split(":")[1].strip()
        if 'Disabled' in enablestate:
            print "ATMCapable status is unsupported "
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Validate the ATMCapable";
            print "EXPECTED RESULT : ATM Capable status should be returned";
            print "ACTUAL RESULT 1: getATMCapable is unsupported %s"%enablestate;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        elif 'Enabled' in enablestate:
            print "ATMCapable status is supported "
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Validate the ATMCapable";
            print "EXPECTED RESULT : ATM Capable status should be returned";
            print "ACTUAL RESULT 1: getATMCapable is supported %s"%enablestate;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            print "getATMCapable is failed"
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Validate the ATMCapable";
            print "EXPECTED RESULT : ATM Capable status should be returned";
            print "ACTUAL RESULT 1: getATMCapable function is failed %s"%enablestate;
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        print "wifi_getATMpable failed";
        tdkTestObj.setResultStatus("FAILURE");
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
