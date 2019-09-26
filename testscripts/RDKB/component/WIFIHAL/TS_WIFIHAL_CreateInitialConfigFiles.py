##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_CreateInitialConfigFiles</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To create the initial configuration files </synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <test_case_id>TC_WIFIHAL_292</test_case_id>
    <test_objective>To create initial configuration files /nvram/log4crc</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_createInitialConfigFiles()</api_or_interface_used>
    <input_parameters>methodName : WIFIHAL_CreateInitialConfigFiles</input_parameters>
    <automation_approch>1. Load wifihal module
2. Load sysutil module
3. Remove the existing initial configuration file
4. Using WIFIHAL_CreateInitialConfigFiles invoke wifi_createInitialConfigFiles()
5. Check whether the initial config file is created
6. Revert the changes back to initial
7. Unload sysutil module
7. Unload wifihal module</automation_approch>
    <except_output>The api should create initial config file</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_CreateInitialConfigFiles</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;
from tdkbVariables import *;


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_CreateInitialConfigFiles');
obj.configureTestCase(ip,port,'TS_WIFIHAL_CreateInitialConfigFiles');
def createInitialConfigfiles():
    print "Entered to the Function"
    #calling the wifi api wifi_createHostApdConfig to create Initial config file /nvram/log4crc
    tdkTestObj = obj.createTestStep('WIFIHAL_CreateInitialConfigFiles');
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 2: Call the wifi_createInitialConfigFiles api to create initial configuration file";
        print "EXPECTED RESULT 2: Should create the file /nvram/log4crc";
        print "ACTUAL RESULT 2: Successfully created the file and execution returns SUCCESS";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        time.sleep(30)
        #Calling the Function checkInitialConfigFiles to check whether the file creation
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        query = "sh %s/tdk_platform_utility.sh checkInitialConfigFile | tr \"\n\" \" \"" %TDK_PATH
        tdkTestObj.addParameter("command", query);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Get the created initial config files";
            print "EXPECTED RESULT 3: Should get the files created";
            print "ACTUAL RESULT 3: Operation returned SUCCESS";
            print "Created Files are:",details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #Revert back the changes
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            query = "sh %s/tdk_platform_utility.sh removeInitialConfigFile" %TDK_PATH
            tdkTestObj.addParameter("command", query);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and "Invalid Argument passed" not in details:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Remove the created initial config files";
                print "EXPECTED RESULT 4: Should remove the file";
                print "ACTUAL RESULT 4: Successfully removed the file and execution returns SUCCESS";
                print "details is :",details
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                print "TEST STEP 4: Remove the created initial config files";
                print "EXPECTED RESULT 4: Should remove the file";
                print "ACTUAL RESULT 4: Failed to remove the files and execution returns FAILURE";
                print "details is :",details
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Get the created initial config file";
            print "EXPECTED RESULT 3: Should get the files created initial config file";
            print "ACTUAL RESULT 3: Failed to get the result",actualresult;
            print "Details is :",details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 2: Call the function wifi_createHostApdConfig to create initial config file";
        print "EXPECTED RESULT 2: Should create the initial config files";
        print "ACTUAL RESULT 2: Failed to create the file and api returns failure";
        print "[TEST EXECUTION RESULT] : FAILURE";

#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
sysloadmodulestatus = sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Removing the existing files in the Arm side
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    query = "sh %s/tdk_platform_utility.sh removeInitialConfigFile" %TDK_PATH
    tdkTestObj.addParameter("command", query);
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and "Invalid Argument passed" not in details:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Remove the existing initial config file";
        print "EXPECTED RESULT 1: Should remove the file";
        print "ACTUAL RESULT 1: Successfully removed the files and execution returns SUCCESS";
        print "details is :",details
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Calling the function to execute the functionality
        createInitialConfigfiles()
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Remove the existing initial config file";
        print "EXPECTED RESULT 1: Should remove the file";
        print "ACTUAL RESULT 1: Failed to remove  the existing files and execution returns FAILURE";
        print "details is :",details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysobj.unloadModule("sysutil");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");


