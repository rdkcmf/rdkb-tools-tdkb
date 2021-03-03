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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_TR069PA_CustomDataModel_GetValueWithSyscfg</name>
  <primitive_test_id/>
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To query the Custom Data Model Enable parameter and check its current status via syscfg</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TR069_11</test_case_id>
    <test_objective>This test case is to query the Custom Data Model Enable parameter and check its current status via syscfg</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>syscfg get custom_data_model_enabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the value of  syscfg get custom_data_model_enabled
3.If value received is "0" the feature is disabled else if received is "1"  the feature is enabled
4.Unload the module</automation_approch>
    <expected_output>syscfg get custom_data_model_enabled should tell wether feature is enabled or disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_TR069PA_CustomDataModel_GetValueWithSyscfg</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj= tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_GetValueWithSyscfg');

#Get the result of connection with test component and DUT
loadmodulestatus1=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
if "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    cmd = "syscfg get custom_data_model_enabled";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and details != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Custom Data Model Enabled status via syscfg";
        print "EXPECTED RESULT 1: Should get the Custom Data Model Enabled status via syscfg";
        print "ACTUAL RESULT 1: Custom Data Model Enabled status retreived successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if details == "1" :
            value = "enabled";
        else:
             value = "disabled";

        if  details  == "0" or details  == "1":
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Check if Custom Data Model is enabled or disabled";
             print "EXPECTED RESULT 2: Custom Data Model should be either enabled or disabled";
             print "ACTUAL RESULT 2: Custom Data Model Enable status is %s" %value;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
             #Set the result status of execution
             tdkTestObj.setResultStatus("FAILURE");
             print "TEST STEP 2: Check if Custom Data Model is enabled or disabled";
             print "EXPECTED RESULT 2: Custom Data Model should be either enabled or disabled";
             print "ACTUAL RESULT 2: Custom Data Model Enable status is %s" %value;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Custom Data Model Enabled status via sycfg";
        print "EXPECTED RESULT 1: Should get the Custom Data Model Enabled status via syscfg";
        print "ACTUAL RESULT 1: Failed to retreived Custom Data Model Enabled status ";
        #Get the result of execution
        print "[TEST EXECUTION RESULT]: FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
