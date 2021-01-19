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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetApBeaconRate</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>This hal api is to set the access point beacon rate for 5GHz</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_310</test_case_id>
    <test_objective>This hal api is to set the access point beacon rate for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApBeaconRate()
wifi_getApBeaconRate()</api_or_interface_used>
    <input_parameters>methodName = "getApBeaconRate"
radioIndex =1
param = 6Mbps</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the current beacon rate using wifi_getApBeaconRate()
3.Set the beacon rate to another value using wifi_setApBeaconRate()
4. validate the set function using get function
5. Revert back to the initial beacon rate
6. Unload wifihal module</automation_approch>
    <expected_output>The beacon rate set function should be successful</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApBeaconRate</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from wifiUtility import *;
radio = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApBeaconRate');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:

            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            tdkTestObj.addParameter("methodName","getApBeaconRate");
            tdkTestObj.addParameter("radioIndex",idx);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Get the current ap beacon rate";
                print "EXPECTED RESULT 1: Should get the current ap beacon rate";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                currRate = details.split(":")[1].strip();
                setRates = ["6Mbps","12Mbps","24Mbps"];
                for newRate in setRates :
                    if newRate == currRate :
                        continue;
                    else :
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                        tdkTestObj.addParameter("param",newRate);
                        tdkTestObj.addParameter("radioIndex",idx);
                        tdkTestObj.addParameter("methodName","setApBeaconRate");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 2: Set the new beacon rate using wifi_setApBeaconRate";
                            print "EXPECTED RESULT 2: Should set the beacon rate using wifi_setApBeaconRate";
                            print "ACTUAL RESULT 2: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            time.sleep(10);

                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                            tdkTestObj.addParameter("methodName","getApBeaconRate");
                            tdkTestObj.addParameter("radioIndex",idx);
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            if expectedresult in actualresult:
                                newValue = details.split(":")[1].strip()
                                if newValue == newRate:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP 3: Verify the set function using get function";
                                    print "EXPECTED RESULT 3: Should get the current beacon rate";
                                    print "ACTUAL RESULT 3: %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP 3: Verify the set function using get function";
                                    print "EXPECTED RESULT 3: Should get the current beacon rate";
                                    print "ACTUAL RESULT 3: %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                                #Revert the channel value
                                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                                tdkTestObj.addParameter("param",currRate);
                                tdkTestObj.addParameter("radioIndex",idx);
                                tdkTestObj.addParameter("methodName","setApBeaconRate");
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();
                                if expectedresult in actualresult:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP : Revert the beacon rate using wifi_setApBeaconRate";
                                    print "EXPECTED RESULT : Should revert the beacon rate using wifi_setApBeaconRate";
                                    print "ACTUAL RESULT : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP : Revert the beacon rate using wifi_setApBeaconRate";
                                    print "EXPECTED RESULT : Should revert the beacon rate using wifi_setApBeaconRate";
                                    print "ACTUAL RESULT : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "wifi_getApBeaconRate() call failed after set operation";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 2: Set the beacon rate using wifi_setApBeaconRate";
                            print "EXPECTED RESULT 2: Should the beacon rate using wifi_setApBeaconRate";
                            print "ACTUAL RESULT 2: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    break;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Get the beacon rate ";
                print "EXPECTED RESULT 1: Should get beacon rate";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
