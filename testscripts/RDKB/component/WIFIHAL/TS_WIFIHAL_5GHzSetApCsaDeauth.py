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
  <name>TS_WIFIHAL_5GHzSetApCsaDeauth</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate wifi_setApCsaDeauth() HAL API by trying to switch between different modes and check the return status of the API for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_318</test_case_id>
    <test_objective>To validate wifi_setApCsaDeauth() HAL API by trying to switch between different modes and check the return status of the API fo 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApCsaDeauth()</api_or_interface_used>
    <input_parameters>methodName : setApCsaDeauth
radioIndex : 1
mode : 0(none) , 1(unicast), 2(broadcast)</input_parameters>
    <automation_approch>1. Load the wifihal module.
2. Switch the ApCsaDeauth mode to None by invoking wifi_setApCsaDeauth() HAL API.
3. If API return status is SUCCESS, switch the mode to unicast by invoking wifi_setApCsaDeauth() HAL API.
4. If API return status is SUCCESS, switch the mode to broadcast by invoking wifi_setApCsaDeauth() HAL API.
5. Finally, set the mode back to default mode : broadcast
6. Unload the module.</automation_approch>
    <expected_output>Should successfully switch between the modes for 5GHz.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApCsaDeauth</test_script>
    <skipped>No</skipped>
    <release_version>M66</release_version>
    <remarks></remarks>
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
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApCsaDeauth');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;


def setApCsaDeauth(obj,mode,radioIndex) :
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
    tdkTestObj.addParameter("methodName","setApCsaDeauth");
    tdkTestObj.addParameter("radioIndex",radioIndex);
    #mode is 0:none;1:unicast;2:broadcast
    tdkTestObj.addParameter("param",mode);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj,actualresult,details)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj,actualresult,details = setApCsaDeauth(obj,0,idx);
        expectedresult="SUCCESS";
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "**************************************************";
            print "TEST STEP 1: To switch the ApCsaDeauth mode to None for 5GHz";
            print "EXPECTED RESULT 1: Should successfully switch the ApCsaDeauth mode to None for 5GHz";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "**************************************************";
            tdkTestObj,actualresult,details = setApCsaDeauth(obj,1,idx);
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "**************************************************";
                print "TEST STEP 2: To switch the ApCsaDeauth mode to unicast for 5GHz";
                print "EXPECTED RESULT 2: Should successfully switch the ApCsaDeauth to unicast for 5GHz";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                print "**************************************************";
                tdkTestObj,actualresult,details = setApCsaDeauth(obj,2,idx);
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "**************************************************";
                    print "TEST STEP 3: To switch the ApCsaDeauth mode to broadcast for 5GHz";
                    print "EXPECTED RESULT 3: Should successfully switch the broadcast to broadcast for 5GHz";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    print "**************************************************";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "**************************************************";
                    print "TEST STEP 3: To switch the ApCsaDeauth mode to broadcast for 5GHz";
                    print "EXPECTED RESULT 3: Should successfully switch the broadcast to broadcast for 5GHz";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    print "**************************************************";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "**************************************************";
                print "TEST STEP 2: To switch the ApCsaDeauth mode to unicast for 5GHz";
                print "EXPECTED RESULT 2: Should successfully switch the ApCsaDeauth to unicast for 5GHz";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "**************************************************";

                #Revert the mode to default mode(broadcast)
                tdkTestObj,actualresult,details = setApCsaDeauth(obj,2,idx);
                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Successfully reverted the mode to default mode:broadcast for 5GHz";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Unable to revert the mode to default mode:broadcast for 5GHz";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "**************************************************";
            print "TEST STEP 1: To switch the ApCsaDeauth mode to None for 5GHz";
            print "EXPECTED RESULT 1: Should successfully switch the ApCsaDeauth mode to None for 5GHz";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
            print "**************************************************";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");