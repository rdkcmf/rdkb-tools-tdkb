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
  <name>TS_TR069PA_CustomDataModel_ToggleValue</name>
  <primitive_test_id/>
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check for successfull toggling of Device.DeviceInfo.CustomDataModelEnabled</synopsis>
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
    <test_case_id>TC_TR069_16</test_case_id>
    <test_objective>This test case is to check for successfull toggling of Device.DeviceInfo.CustomDataModelEnabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.CustomDataModelEnabled  </input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of Device.DeviceInfo.CustomDataModelEnabled  
3.Toggle the value and check for successful set 
4.Revert the Device.DeviceInfo.CustomDataModelEnabled status to previous
5.Unload the module</automation_approch>
    <expected_output>The set operation on Device.DeviceInfo.CustomDataModelEnabled is expected to be successfull</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_TR069PA_CustomDataModel_ToggleValue</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_ToggleValue');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.CustomDataModelEnabled");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    default = details.strip().replace("\\n", "");
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Custom Data Model Enabled status";
        print "EXPECTED RESULT 1: Should get the Custom Data Model Enabled status";
        print "ACTUAL RESULT 1: Custom Data Model Enabled status is : %s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if default =="false":
            setValue = "true";
        else:
            setValue = "false";

        print "The value to toggle for Custom Data Model Enabled is %s" %setValue;
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.CustomDataModelEnabled");
        tdkTestObj.addParameter("ParamValue",setValue);
        tdkTestObj.addParameter("Type","boolean");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Toggle the Custom Data Model Enabled status";
            print "EXPECTED RESULT 2: Should toggle the Custom Data Model Enabled status to %s" %setValue;
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #waiting for set to reflect 
            sleep(60);
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.CustomDataModelEnabled");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            details = details.strip().replace("\\n", "");
            if expectedresult in actualresult and details == setValue:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check for successful set with a get operation";
                print "EXPECTED RESULT 3: Paramter value should change after successful set";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check for successful set with a get operation";
                print "EXPECTED RESULT 3: Paramter value should change after successful set";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            
            #revert the value to previous
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.CustomDataModelEnabled");
            tdkTestObj.addParameter("ParamValue",default);
            tdkTestObj.addParameter("Type","boolean");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
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
            print "TEST STEP 2: Toggle the Custom Data Model Enabled status";
            print "EXPECTED RESULT 2: Should toggle the Custom Data Model Enabled status to %s" %setValue;
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Custom Data Model Enabled status";
        print "EXPECTED RESULT 1: Should get the Custom Data Model Enabled status";
        print "ACTUAL RESULT 1: Custom Data Model Enabled status is %s:" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
