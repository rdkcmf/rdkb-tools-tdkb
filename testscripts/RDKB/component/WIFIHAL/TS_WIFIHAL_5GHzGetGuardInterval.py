##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_WIFIHAL_5GHzGetGuardInterval</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke wifi_getGuardInterval() and check if it returns a value from the expected list</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_481</test_case_id>
    <test_objective>Invoke wifi_getGuardInterval() and check if it returns a value from the expected list</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getGuardInterval</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getGuardInterval for 5GHz and check if its return was success
3. Check if output of wifi_getGuardInterval() is one from the list {    wifi_guard_interval_400,    wifi_guard_interval_800,    wifi_guard_interval_1600,    wifi_guard_interval_3200,    wifi_guard_interval_auto,}
4. Unload wifihal module</automation_approch>
    <expected_output>wifi_getGuardInterval() should return a value from the expected list</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetGuardInterval</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetGuardInterval');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Script to load the configuration file of the component
        print "TEST STEP 1: Invoke the wifi_getGuardInterval api";
        print "EXPECTED RESULT 1:Invocation of wifi_getGuardInterval should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
        tdkTestObj.addParameter("methodName","getGuardInterval")
        tdkTestObj.addParameter("radioIndex", idx)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getGuardInterval was success. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            guardList = {"1":"wifi_guard_interval_400", "2":"wifi_guard_interval_800", "4":"wifi_guard_interval_1600", "8":"wifi_guard_interval_3200", "16":"wifi_guard_interval_auto"};
            print "TEST STEP 2: Check if value returned by wifi_getGuardInterval api is from the list ",guardList;
            print "EXPECTED RESULT 2 : The value returned by wifi_getGuardInterval api should be from the above list";
            guardInterval= details.split(":")[1].strip()
            if guardInterval and 0 <= int(guardInterval) and int(guardInterval) <= 16:
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "ACTUAL RESULT 2: GuardInterval = %s. Value is from the expected list" %guardList[guardInterval]
                 print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "ACTUAL RESULT 2: GuardInterval = %s. Value is not within the expected range" %guardInterval
                 print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
