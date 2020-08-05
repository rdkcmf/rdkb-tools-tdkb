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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_platform_stub_hal_ValidateGetFanSpeed</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_GetFanSpeed</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if FanSpeed  is  0 when the speed_fan file is not present.</synopsis>
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
    <test_case_id>TC_HAL_PLATFORM_63</test_case_id>
    <test_objective>This test case is to check if FanSpeed  is  0 when the speed_fan file is not present.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_stub_hal_GetFanSpeed</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module
2. move the /tmp/speed_fan to /nvram/TDK/
3. Invoke the platform_stub_hal_GetFanSpeed and the speed should be returned as 0
4. Move the speed_fan file back to /tmp
5. Unload the module</automation_approch>
    <expected_output>With  /tmp/speed_fan not present Fan speed should be 0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_ValidateGetFanSpeed</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_ValidateGetFanSpeed');
obj1.configureTestCase(ip,port,'TS_platform_stub_hal_ValidateGetFanSpeed');
#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
result1=obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;
print "[LIB LOAD STATUS]  :  %s" %result1;

if "SUCCESS" in  result.upper() and "SUCCESS" in result1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    cmd = " mv /tmp/speed_fan /nvram/TDK/";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: move the speed_fan to /nvram/TDK/";
        print "EXPECTED RESULT 1: Should move the speed_fan to /nvram/TDK/"
        print "ACTUAL RESULT 1: File move was successfull"
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetFanSpeed");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        details = tdkTestObj.getResultDetails().strip.replace("\\n", "");
        if expectedresult in actualresult and int(details) == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Retrieve the Platform_GetFanSpeed";
            print "EXPECTED RESULT 2: Should retrieve the Platform_GetFanSpeed as 0";
            print "ACTUAL RESULT 2 :FanSpeed is  %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Retrieve the Platform_GetFanSpeed";
            print "EXPECTED RESULT 2: Should retrieve the Platform_GetFanSpeed as 0";
            print "ACTUAL RESULT 2: FanSpeed is  %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE" ;

        tdkTestObj = obj1.createTestStep('ExecuteCmd');
        cmd = " mv /nvram/TDK/speed_fan  /tmp/";
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult :
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 3: move the speed_fan back to /tmp/";
           print "EXPECTED RESULT 3: Should move the speed_fan to /tmp/"
           print "ACTUAL RESULT 3: File move failed"
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: move the speed_fan back to /tmp/";
            print "EXPECTED RESULT 3: Should move the speed_fan to /tmp/"
            print "ACTUAL RESULT 3: File move failed"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: move the speed_fan to /nvram/TDK/";
        print "EXPECTED RESULT 1: Should move the speed_fan to /nvram/TDK/"
        print "ACTUAL RESULT 1: File move failed"
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    obj.unloadModule("halplatform");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
