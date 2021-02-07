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
  <name>TS_WIFIHAL_2.4GHzSetGuardInterval_auto</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set guard interval value to auto using wifi_setGuardInterval() and verify it using wifi_getGuardInterval()</synopsis>
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
    <test_case_id>TC_WIFIHAL_489</test_case_id>
    <test_objective>Set guard interval value to auto using wifi_setGuardInterval() and verify it using wifi_getGuardInterval()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setGuardInterval
wifi_getGuardInterval</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getGuardInterval for 2.4GHz and save the current guard interval
3. Using wifi_setGuardInterval() set guard interval as auto
4. Using wifi_getGuardInterval() check if set value is reflecting in further get
5. Revert guard interval to its initial value
6. Unload wifihal module</automation_approch>
    <expected_output>wifi_setGuardInterval() should successfully set  guard interval value to auto</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetGuardInterval_auto</test_script>
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

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetGuardInterval_auto');

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
        print "TEST STEP 1: Get and save the current guard interval using wifi_getGuardInterval ";
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
            print "ACTUAL RESULT 1:  API returned success status. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            initGuardInterval= details.split(":")[1].strip()
            guardList = {"0":"wifi_guard_interval_400", "1":"wifi_guard_interval_800", "2":"wifi_guard_interval_1600", "3":"wifi_guard_interval_3200", "4":"wifi_guard_interval_auto"};
            newInterval = "4"

            print "Current guard interval is ",guardList[initGuardInterval]
            print "TEST STEP 2: Set guard interval as wifi_guard_interval_auto using wifi_setGuardInterval() from the supported list of ", guardList
            print "EXPECTED RESULT 2: wifi_setGuardInterval should successfully set guard interval value to ",guardList[newInterval] ;
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
            tdkTestObj.addParameter("methodName","setGuardInterval")
            tdkTestObj.addParameter("radioIndex", idx)
            tdkTestObj.addParameter("param", int(newInterval))
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "TEST STEP 3: Invoke  wifi_getGuardInterval to verify set done by wifi_setGuardInterval api";
                print "EXPECTED RESULT 3: wifi_getGuardInterval should return the value set by wifi_setGuardInterval";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                tdkTestObj.addParameter("methodName","getGuardInterval")
                tdkTestObj.addParameter("radioIndex", idx)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and newInterval == details.split(":")[1].strip():
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "wifi_getGuardInterval() returned guard interval same as the set value"
                    print "ACTUAL RESULT 3:  API returned success status. New guard interval = ", guardList[newInterval] ;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3:  %s" %details;
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert guard interval to initial value
                print "TEST STEP 4: Revert the guard interval to %s using wifi_setGuardInterval api" %guardList[initGuardInterval];
                print "EXPECTED RESULT 4: wifi_setGuardInterval should successfully revert guard interval value";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                tdkTestObj.addParameter("methodName","setGuardInterval")
                tdkTestObj.addParameter("radioIndex", idx)
                tdkTestObj.addParameter("param", int(initGuardInterval))
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4:  %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4:  %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
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
