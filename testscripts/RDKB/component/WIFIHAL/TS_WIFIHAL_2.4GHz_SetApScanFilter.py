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
  <version>15</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHz_SetApScanFilter</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_SetApScanFilter</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the WiFi HAL API wifi_setApScanFilter for 2.4GHz AccessPoint</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>3</execution_time>
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
    <test_case_id>TC_WIFIHAL_362</test_case_id>
    <test_objective>Validte the WIFi HAL API wifi_setApScanFilter for the 2.4GHz AccessPoint</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApScanFilter()</api_or_interface_used>
    <input_parameters>radioIndex - radioIndex value
mode - scan filter mode (0 or 1 or 2)</input_parameters>
    <automation_approch>1.Load the module
2.Get the current scan filter mode and store it
3.Using WIFIHAL_SetApScanFilter call wifi_setApSanFilter()API for all three modes (0-WIFI_SCANFILTER_MODE_DISABLED, 1-WIFI_SCANFILTER_MODE_ENABLED, 2- WIFI_SCANFILTER_MODE_FIRST)
4.Verify the set
5.Revert back to the original Scan Filter mode value
6.Unload the module</automation_approch>
    <expected_output>The APScanFilter should be set with all three possible modes</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHz_SetApScanFilter</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from time import sleep;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHz_SetApScanFilter');
sysObj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHz_SetApScanFilter');

def get_gscanfilter(tdkTestObj):
    query = "sh %s/tdk_platform_utility.sh getAP0ScanFilter | grep gscanfilter | cut -f2 -d ':' " %TDK_PATH
    tdkTestObj.addParameter("command", query);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    tmp_details = tdkTestObj.getResultDetails().strip();
    print "tmp_details is %s"%tmp_details
    details = int(tmp_details[0])
    return details,actualresult

def set_apscanfilter(mode,tdkTestObj):
    tdkTestObj.addParameter("apIndex", 0);
    tdkTestObj.addParameter("methodName", "setApScanFilter");
    tdkTestObj.addParameter("mode", int(mode));
    tdkTestObj.addParameter("essid", "NULL");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return details, actualresult


#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus

if "SUCCESS" in (loadmodulestatus.upper() and  sysutilloadmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");
    revert_flag = 0;
    #Get the Initial Scan Filter Value
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    initial_mode,initial_result = get_gscanfilter(tdkTestObj);

    if expectedresult in initial_result:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get Scan Filter mode "
        print "EXPECTED RESULT 1: Should successfully get Scan Filter mode "
        print "ACTUAL RESULT 1: Successfully got the Scan Filter mode and initial mode is %s"%initial_mode
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Verify set scan filter for all 3 modes (0-WIFI_SCANFILTER_MODE_DISABLED, 1-WIFI_SCANFILTER_MODE_ENABLED, 2- WIFI_SCANFILTER_MODE_FIRST)
        for mode in range (0,3):
            #Prmitive test case which is associated to this Script
            tdkTestObj = obj.createTestStep('WIFIHAL_SetApScanFilter');
            set_details,set_result = set_apscanfilter(int(mode),tdkTestObj);

            if expectedresult in set_result :
                revert_flag = 1;
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set AccessPoint scan filter mode"
                print "EXPECTED RESULT 2: Should successfully set the AccessPoint scan filter for mode %s"%mode
                print "ACTUAL RESULT 2: Successfully set the AccessPoint scan filter mode %s"%set_details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                sleep(10);

                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                expectedresult="SUCCESS";
                get_mode,get_result = get_gscanfilter(tdkTestObj);

                #Get mode should match with set mode
                if expectedresult in get_result and int(mode) == int(get_mode):
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get AccessPoint scan filter mode and compare with set value"
                    print "EXPECTED RESULT 3: Should successfully Get the AccessPoint scan filter for mode %s"%get_mode
                    print "ACTUAL RESULT 3: Get Value is matching with set value %s"%get_result
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get AccessPoint scan filter mode and compare with set value"
                    print "EXPECTED RESULT 3: Should successfully Get the AccessPoint scan filter for mode %s"%get_mode
                    print "ACTUAL RESULT 3: Get Value is not matching with set value %s"%get_result
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set AccessPoint scan filter mode"
                print "EXPECTED RESULT 2: Should successfully set the AccessPoint scan filter for mode %s"%mode
                print "ACTUAL RESULT 2: Failed to set the AccessPoint scan filter mode %s"%set_details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

        if revert_flag == 1:
            #Revert back to origial set filter value
            tdkTestObj = obj.createTestStep('WIFIHAL_SetApScanFilter');
            revert_details,revert_result = set_apscanfilter(int(initial_mode),tdkTestObj);
            if expectedresult in revert_result :
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Set AccessPoint Initial scan filter mode"
                print "EXPECTED RESULT 4: Should successfully set the AccessPoint scan filter with initial mode %s"%initial_mode
                print "ACTUAL RESULT 4: Successfully set the AccessPoint scan filter with initial mode %s"%revert_details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Set AccessPoint Initial scan filter mode"
                print "EXPECTED RESULT 4: Should successfully set the AccessPoint scan filter with initial mode %s"%initial_mode
                print "ACTUAL RESULT 4: Failed to set the AccessPoint scan filter with initial mode %s"%revert_details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get Scan Filter mode"
        print "EXPECTED RESULT 1: Should successfully get Scan Filter mode"
        print "ACTUAL RESULT 1: Failed to get Scan Filter mode %s"%initial_result
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
