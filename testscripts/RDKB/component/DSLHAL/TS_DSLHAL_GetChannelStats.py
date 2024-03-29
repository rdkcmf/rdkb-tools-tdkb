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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_DSLHAL_GetChannelStats</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>DSLHAL_GetChannelStats</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the DSL Channel Statistics value using the parameter Device.DSL.Channel.1.Stats.</synopsis>
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
    <test_case_id>TC_DSLHAL_6</test_case_id>
    <test_objective>To get the DSL Channel Statistics value using the parameter Device.DSL.Channel.1.Stats.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>json_hal_client_get_request_header
json_hal_add_param
json_hal_client_send_and_get_reply
json_object_object_get_ex
json_hal_get_param
</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the DSL HAL Module
2. Invoke the json_hal_client_get_request_header api with GET request
3. Invoke the json_hal_add_param with the parameter name "Device.DSL.Channel.1.Stats."
4. Invoke the json_hal_client_send_and_get_reply API to send the request to JSON HAL server
5. Invoke the json_hal_get_param API to get the value of the parameter
6. Return the parameter values in the structure only if above API's are success else failure.
7. Unload the DSL HAL Module</automation_approch>
    <expected_output>Should be able to get the DSL Channel Statistics values</expected_output>
    <priority>High</priority>
    <test_stub_interface>dslhal</test_stub_interface>
    <test_script>TS_DSLHAL_GetChannelStats</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("dslhal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_DSLHAL_GetChannelStats');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('DSLHAL_Init');
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate the DSLHAL_init operation";
        print "EXPECTED RESULT 1: DSLHAL_init Should be success";
        print "ACTUAL RESULT 1: DSLHAL_init was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        tdkTestObj = obj.createTestStep('DSLHAL_GetChannelStats');
        tdkTestObj.addParameter("paramName"," Device.DSL.Channel.1.Stats.");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        channel_stats = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Channel Stats";
            print "EXPECTED RESULT 2: GetChannelStats operation should be success ";
            print "ACTUAL RESULT 2: GetChannelStats operation was success , Line Stats is: ",channel_stats
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Channel Stats";
            print "EXPECTED RESULT 2: GetChannelStats operation should be success ";
            print "ACTUAL RESULT 2: GetChannelStats operation was Failed ";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate the DSLHAL_init operation";
        print "EXPECTED RESULT 1: DSLHAL_init Should be Success";
        print "ACTUAL RESULT 1: DSLHAL_init was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    obj.unloadModule("dslhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

