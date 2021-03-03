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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TR069PA_CustomDataModel_CheckPersistentAfterReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if  value set for Device.DeviceInfo.CustomDataModelEnabled is persistent on reboot</synopsis>
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
    <test_case_id>TC_TR069_17</test_case_id>
    <test_objective>This test case is to check if  value set for Device.DeviceInfo.CustomDataModelEnabled is persistent on reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Set
TDKB_TR181Stub_Get
</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.CustomDataModelEnabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of  Device.DeviceInfo.CustomDataModelEnabled and toggle
3.Trigger a reboot on the DUT
4. Check if the value is persistent on reboot via syscg and tr-181
5.Revert the value to previous 
6.Unload the module</automation_approch>
    <expected_output>Device.DeviceInfo.CustomDataModelEnabled is expected to be persistent on reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_TR069PA_CustomDataModel_CheckPersistentAfterReboot</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2= tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_CheckPersistentAfterRebootl');
obj2.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_CheckPersistentAfterReboot');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1=obj2.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");

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

        if default == "false" :
            setValue = "true";
            checkValue = "1";
        else:
             setValue = "false";
             checkValue = "0";

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

            print "****DUT is going for a reboot and will be up after 300 seconds*****";
            obj2.initiateReboot();
            sleep(300);

            tdkTestObj = obj2.createTestStep('ExecuteCmd');
            cmd = "syscfg get custom_data_model_enabled";
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and details != checkValue:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if the Custom Data Model Enable via syscfg does not persists on reboot";
                print "EXPECTED RESULT 3: The setValue %s should not persist after reboot" %setValue;
                print "ACTUAL RESULT 3: Custom Data Model Enabled status is : %s the set value was %s" %(details,setValue);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.CustomDataModelEnabled");
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                details = details.strip().replace("\\n", "");
                if expectedresult in actualresult and details !=setValue:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Check if the Custom Data Model Enable via tr181 does not persists on reboot";
                    print "EXPECTED RESULT 4: The setValue %s should not persist after reboot" %setValue;
                    print "ACTUAL RESULT 4: Custom Data Model Enabled status is : %s the set value was %s" %(details,setValue);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Check if the Custom Data Model Enable via tr181 does not persists on reboot";
                    print "EXPECTED RESULT 4: The setValue %s should not persist after reboot" %setValue;
                    print "ACTUAL RESULT 4: Custom Data Model Enabled status is : %s the set value was %s" %(details,setValue);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if the Custom Data Model Enable via syscfg does not persists on reboot";
                print "EXPECTED RESULT 3: The setValue %s should not persist after reboot" %setValue;
                print "ACTUAL RESULT 3: Custom Data Model Enabled status is : %s the set value was %s" %(details,setValue);
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
                print "TEST STEP 5: Revert the Custom Data Model Enable to previous"
                print "EXPECTED RESULT 5: Should revert the Custom Data Model Enable to %s" %default;
                print "ACTUAL RESULT 5: %s" %details;
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
    obj2.unloadModule("sysutil");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
     obj2.setLoadModuleStatus("FAILURE");
