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
  <name>TS_TR069PA_CustomDataModel_ToggleWithSyscfg</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check for successful toggling of custom_data_model_enabled via syscfg</synopsis>
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
    <test_case_id>TC_TR069_15</test_case_id>
    <test_objective>This test case is to check for successful toggling of custom_data_model_enabled via syscfg</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>custom_data_model_enabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of custom_data_model_enabled via syscfg
3. Toggle the value and check for successful set 
4.Revert the custom_data_model_enabled status to previous
5.Unload the module</automation_approch>
    <expected_output>The set operation on custom_data_model_enabled via syscfg is expected to be successfull</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_TR069PA_CustomDataModel_ToggleWithSyscfg</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_ToggleWithSyscfg');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    cmd = "syscfg get custom_data_model_enabled";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and default != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Custom Data Model Enabled status via syscfg";
        print "EXPECTED RESULT 1: Should get the Custom Data Model Enabled status";
        print "ACTUAL RESULT 1: Custom Data Model Enabled status is : %s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if default == "0" :
            setValue = "1";
        else:
            setValue = "0";

        print "The value to toggle for custom_data_model_enabled is %s" %setValue;

        tdkTestObj = obj.createTestStep('ExecuteCmd');
        cmd = "syscfg set custom_data_model_enabled %s" %setValue;
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Toggle the Custom Data Model Enabled status via syscfg";
            print "EXPECTED RESULT 2: Should toggle the Custom Data Model Enabled status to %s" %setValue;
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "syscfg get custom_data_model_enabled";
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and details == setValue:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if set reflected for Custom Data Model Enabled via syscfg";
                print "EXPECTED RESULT 3: The value set for Custom Data Model Enable should be reflected";
                print "ACTUAL RESULT 3: set value was %s , get via syscfg is %s" %(setValue,details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if set reflected for Custom Data Model Enabled via syscfg";
                print "EXPECTED RESULT 3: The value set for Custom Data Model Enable should be reflected";
                print "ACTUAL RESULT 3: set value was %s , get via syscfg is %s" %(setValue,details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            #revert the value to previous
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "syscfg set custom_data_model_enabled %s" %default;
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Revert the Custom Data Model Enable to previous"
                print "EXPECTED RESULT 4: Should revert the Custom Data Model Enable to %s" %default;
                print "ACTUAL RESULT 4: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Revert the Custom Data Model Enable to previous"
                print "EXPECTED RESULT 4: Should revert the Custom Data Model Enable to %s" %default;
                print "ACTUAL RESULT 4: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Toggle the Custom Data Model Enabled status via syscfg";
            print "EXPECTED RESULT 2: Should toggle the Custom Data Model Enabled status to %s" %setValue;
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Custom Data Model Enabled status via syscfg";
        print "EXPECTED RESULT 1: Should get the Custom Data Model Enabled status";
        print "ACTUAL RESULT 1: Custom Data Model Enabled status is %s:" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
