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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_SetBoolParamValue</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_SetValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set the DML parameter (boolean) using rbus_set and rbusValue_SetBoolean RBUS APIs</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <test_case_id>TC_RBUS_28</test_case_id>
    <test_objective>To Set the DML parameter (boolean) using rbus_set and rbusValue_SetBoolean RBUS APIs</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_set
rbusValue_SetBoolean</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_CloudUIEnable</input_parameters>
    <automation_approch>1. Load the rbus module
2. Open the rbus connection using rbus_open RBUS API
3. Get the initial value of the DML parameter using rbusValue_GetBoolean and store it
4. Invoke the RBUS API rbusValue_SetBoolean with the parameter name and parametervalue (toggle from initial value)
5. Set operation should be success
6. Get the parameter value using rbusValue_GetBoolean and check value was set properly
7. Revert the parameter value to its initial value using rbusValue_SetBoolean API
8. Close the rbus connection using rbus_close RBUS API
9. Unload the module</automation_approch>
    <expected_output>Set operation should be success using rbusValue_SetBoolean API</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_SetBoolParamValue</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RBUS_SetBoolParamValue');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    parameterName = "Device.DeviceInfo.X_RDKCENTRAL-COM_CloudUIEnable"

    tdkTestObj = obj.createTestStep('RBUS_Open');
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "RBUS Open Detail is ",details

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "RBUS status is %s" %details;

        tdkTestObj = obj.createTestStep('RBUS_GetValue');
        tdkTestObj.addParameter("paramName",parameterName);
        tdkTestObj.addParameter("paramType","Boolean");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initial_Value = tdkTestObj.getResultDetails();

        print "Initial Value is :",initial_Value

        if expectedresult in actualresult and initial_Value != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the value of parameter using rbusValue_GetBoolean";
            print "EXPECTED RESULT 2: Should get the value of the parameter: ",parameterName;
            print "ACTUAL RESULT 2: value of the parameter is ", initial_Value;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            if initial_Value == "true":
                new_value_to_set = "0";
                revert_Value = "1";
            else:
                new_value_to_set = "1";
                revert_Value = "0";

            print "Value to be Set is :",new_value_to_set

            tdkTestObj = obj.createTestStep('RBUS_SetValue');
            tdkTestObj.addParameter("paramName",parameterName);
            tdkTestObj.addParameter("paramType","Boolean");
            tdkTestObj.addParameter("paramValue",new_value_to_set);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and details != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Set the value for parameter using rbusValue_SetBoolean";
                print "EXPECTED RESULT 3: Set function should be succcess";
                print "ACTUAL RESULT 3: Set function was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                tdkTestObj = obj.createTestStep('RBUS_GetValue');
                tdkTestObj.addParameter("paramName",parameterName);
                tdkTestObj.addParameter("paramType","Boolean");
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                new_Value = tdkTestObj.getResultDetails();

                print "New Value is :",new_Value

                if expectedresult in actualresult and new_Value!= "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the value of parameter using rbusValue_GetBoolean";
                    print "EXPECTED RESULT 4: Should get the value of the parameter: ",parameterName;
                    print "ACTUAL RESULT 4: value of the parameter is ", new_Value;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    if (new_Value == "true" and initial_Value == "false") or (new_Value == "false" and initial_Value == "true"):
                        print "Validation for set operation was Successful"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Validation for set operation was Failed"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the value of parameter using rbusValue_GetBoolean";
                    print "EXPECTED RESULT 4: Should get the value of the parameter: ",parameterName;
                    print "ACTUAL RESULT 4: value of the parameter is ", new_Value;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "Value to be set for Revert operation is :",revert_Value

                tdkTestObj = obj.createTestStep('RBUS_SetValue');
                tdkTestObj.addParameter("paramName",parameterName);
                tdkTestObj.addParameter("paramType","Boolean");
                tdkTestObj.addParameter("paramValue",revert_Value);
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Set the value to initial_Value";
                    print "EXPECTED RESULT 5: Revert operation should be succcess";
                    print "ACTUAL RESULT 5: Revert operation was Successful";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Set the value to initial_Value";
                    print "EXPECTED RESULT 5: Revert operation should be succcess";
                    print "ACTUAL RESULT 5: Revert operation was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Set the value for parameter using rbusValue_SetBoolean";
                print "EXPECTED RESULT 3: Set function should be succcess";
                print "ACTUAL RESULT 3: Set function was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the value of parameter using rbusValue_GetBoolean";
            print "EXPECTED RESULT 2: Should get the value of the parameter: ",parameterName;
            print "ACTUAL RESULT 2: Failed to get the value of the parameter "
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        tdkTestObj = obj.createTestStep('RBUS_Close');
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS close Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 6: Close the RBUS connection";
            print "EXPECTED RESULT 6: rbus_close should be success";
            print "ACTUAL RESULT 6: rbus_close was success";
             #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 6: Close the RBUS connection";
            print "EXPECTED RESULT 6: rbus_close should be success";
            print "ACTUAL RESULT 6: rbus_close was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    obj.unloadModule("rbus");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
