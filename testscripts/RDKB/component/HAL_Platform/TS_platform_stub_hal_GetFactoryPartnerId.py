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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_platform_stub_hal_GetFactoryPartnerId</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_getFactoryPartnerId</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate Platform HAL API platform_hal_getFactoryPartnerId with partner ID in configuration file</synopsis>
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
    <test_case_id>TC_HAL_Platform_33</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_getFactoryPartnerId with partner ID in configuration file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_getFactoryPartnerId()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  platform module.
2.Get partner ID from configuration file
2. From script invoke platform_stub_hal_getFactoryPartnerId()
3. Get the value
4. Validate whether partner ID from platform_stub_hal_getFactoryPartnerId and partner ID from configuration file are same</automation_approch>
    <expected_output>Partner ID from platform_stub_hal_getFactoryPartnerId and Partner ID from configuration file should be same</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetFactoryPartnerId</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#Library functions
import tdklib;
from tdkbVariables import *;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetFactoryPartnerId');
sysObj.configureTestCase(ip,port,'TS_platform_stub_hal_GetFactoryPartnerId');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysObj.getLoadModuleResult();


if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile PARTNER_ID" %TDK_PATH;
    print command;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    configPartnerID = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and configPartnerID != " ":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get value of PARTNER_ID"
        print "EXPECTED RESULT 1: Should get the value of PARTNER_ID";
        print "ACTUAL RESULT 1:Partner ID from config file  %s" %configPartnerID;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep("platform_stub_hal_getFactoryPartnerId");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        factoryPartnerID = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and factoryPartnerID != " ":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Retrieve the Platform_getFactoryPartnerId";
            print "EXPECTED RESULT 2: Should retrieve the Platform_getFactoryPartnerId successfully";
            print "ACTUAL RESULT 2: Platform_getFactoryPartnerId value retrieved: %s" %factoryPartnerID
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            if configPartnerID == factoryPartnerID:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Validate the Platform_getFactoryPartnerId";
                print "EXPECTED RESULT 3: Should validate the Platform_getFactoryPartnerId successfully";
                print "ACTUAL RESULT 3: Platform_getFactoryPartnerId validated successfully"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Validate the Platform_getFactoryPartnerId";
                print "EXPECTED RESULT 3: Should validate the Platform_getFactoryPartnerId successfully";
                print "ACTUAL RESULT 3: Platform_getFactoryPartnerId and partner ID retrieved from config file are not same"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Retrieve the Platform_getFactoryPartnerId";
            print "EXPECTED RESULT 2: Should retrieve the Platform_getFactoryPartnerId successfully";
            print "ACTUAL RESULT 2: Failed to retrieve Platform_getFactoryPartnerId"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get value of PARTNER_ID"
        print "EXPECTED RESULT 1: Should get the value of PARTNER_ID";
        print "ACTUAL RESULT 1: Failed to get PARTNER_ID from configuration file" ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("halplatform");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

