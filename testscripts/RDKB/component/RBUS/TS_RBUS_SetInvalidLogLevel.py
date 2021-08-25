##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_SetInvalidLogLevel</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_SetLogLevel</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the invocation of RBUS API rbus_setLogLevel() fails when invalid log level is passed as input.</synopsis>
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
    <test_case_id>TC_RBUS_56</test_case_id>
    <test_objective>Check if the invocation of RBUS API rbus_setLogLevel() fails when invalid log level is passed as input.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>RBUS_SetLogLevel</api_or_interface_used>
    <input_parameters>level : random integer value in the range [5,100]</input_parameters>
    <automation_approch>1. Load the rbus module
2. With the device in rbus mode invoke rbus_setLogLevel() with invalid level in the range [5,100]. The API should return failure.
3. Unload the module
</automation_approch>
    <expected_output>rbus_setLogLevel() should fail when invalid log level is passed as input.</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_SetInValidLogLevel</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from random import randint;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RBUS_SetInvalidLogLevel');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    #Choose a random invalid log level
    level = randint(5,100);
    print "\nSetting to Invalid Level : %d" %level;
    tdkTestObj = obj.createTestStep('RBUS_SetLogLevel');
    tdkTestObj.addParameter("level", level);
    expectedresult = "FAILURE";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "\nTEST STEP 1: rbus_setLogLevel should not be invoked successfully with invalid log level value = %d" %level;
        print "EXPECTED RESULT 1: rbus_setLogLevel should fail";
        print "ACTUAL RESULT 1: rbus_setLogLevel was failed; Details %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS" ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "\nTEST STEP 1: rbus_setLogLevel should not be invoked successfully with invalid log level value = %d" %level;
        print "EXPECTED RESULT 1: rbus_setLogLevel should fail";
        print "ACTUAL RESULT 1: rbus_setLogLevel was success; Details %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE" ;

    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

