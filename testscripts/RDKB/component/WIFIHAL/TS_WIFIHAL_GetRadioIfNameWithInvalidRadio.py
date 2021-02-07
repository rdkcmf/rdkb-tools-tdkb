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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_GetRadioIfNameWithInvalidRadio</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To pass a invalid radio i,e radio index greater than number of radio entries and check the behaviour of wifi_getRadioIfName api</synopsis>
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
    <test_case_id>TC_WIFIHAL_456</test_case_id>
    <test_objective>This test case is to pass a invalid radio i,e radio index greater than number of radio entries and check the behaviour of api </test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband </test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioNumberOfEntries
wifi_getRadioIfName</api_or_interface_used>
    <input_parameters>radioindex
radio num of entries</input_parameters>
    <automation_approch>1.Load the module
2. get the radio number of entries using wifi_getRadioNumberOfEntries
3. query wifi_getRadioIfName with radioindex greater than number of radio entries and the api call is expected to fail
4.unload the module</automation_approch>
    <expected_output>The query to api wifi_getRadioIfName should fail with invalid radio index </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_GetRadioIfNameWithInvalidRadio</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from wifiUtility import *;
radio = "2.4G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetRadioIfNameWithInvalidRadio');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    ## Check if a invalid index is returned
    tdkTestObjTemp, idx = getIndex(obj, radio);
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
        #Giving the method name to invoke the api wifi_getRadioNumberOfEntries()
        tdkTestObj.addParameter("methodName","getRadioNumberOfEntries")
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        noofEntries = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            noofEntries = noofEntries.split(":")[1];
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the Radio number of entries";
            print "EXPECTED RESULT 1: Should get the radio number of entries";
            print "ACTUAL RESULT 1: %s" %noofEntries;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            index = int(noofEntries) + 1;
            #Script to load the configuration file of the component
            expectedresult= "FAILURE";
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            #Giving the method name to invoke the api wifi_getRadioIfName()
            tdkTestObj.addParameter("methodName","getRadioIfName")
            #Radio index is 0 for 2.4GHz and 1 for 5GHz
            tdkTestObj.addParameter("radioIndex",index);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the Radio If Name for a invalid radio index %d" %index;
                print "EXPECTED RESULT 2: Should not get the Radio If Name for a invalid radio index";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Get the Radio If Name for a invalid radio index %d" %index;
                print "EXPECTED RESULT 2: Should not get Radio If Name for a invalid radio index ";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the Radio number of entries";
            print "EXPECTED RESULT 1: Should get the radio number of entries";
            print "ACTUAL RESULT 1: %s" %noofEntries;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
