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
  <version>10</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_Object_SetValue</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_ObjectCommands</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the RBUS 2.0 API rbusObject_SetValue</synopsis>
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
    <test_case_id>TC_RBUS_65</test_case_id>
    <test_objective>To Validate the RBUS 2.0 API rbusObject_SetValue</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbusObject_SetValue</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Open the RBUS Connection using rbus_open API
2. Initiate the RBUS Object using rbusObject_Init API and return status should be success
3. Initiate the RBUS value using rbusValue_Init API and set a string value to it using rbusValue_SetFromString API
4. Set the RBUS value to RBUS Object using rbusObject_SetValue API and return status should be success
5. Release the RBUS value using rbusValue_Release API
6. Get the RBUS value of RBUS object using rbusObject_GetValue and the value should be matching with initial value
7. Get the Name of the object and compare it with initial value and the value should be matching
8. Release the RBUS Object using rbusObject_Release API and return status should be success
9. Close the RBUS Connection using rbus_close API
</automation_approch>
    <expected_output>Should be able to set the RBUS value to the RBUS object using rbusObject_SetValue</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_Object_SetValue</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
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
obj.configureTestCase(ip,port,'TS_RBUS_Object_SetValue');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    obj_name = "gTestObject"

    print "\n********** Step 1: Open the RBUS connection ****************"
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

        print "\n********** Step 2: Initiate rbusObject_Init function ****************"
        print "Initiate the RBUS Object with object name ",obj_name

        tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
        tdkTestObj.addParameter("operation","rbusObject_Init");
        tdkTestObj.addParameter("obj_count",1);
        tdkTestObj.addParameter("object_name",obj_name);
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Initiate rbusObject_Init function";
            print "EXPECTED RESULT 2: rbusObject_Init should be success";
            print "ACTUAL RESULT 2: rbusObject_Init  was Success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "\n********** Step 3: Initiate rbusValue_Init function ****************"
            tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
            tdkTestObj.addParameter("operation","rbusValue_Init");
            tdkTestObj.addParameter("prop_count",1);
            tdkTestObj.addParameter("property_name","dummy");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Initiate rbusValue_Init function";
                print "EXPECTED RESULT 3: rbusValue_Init should be success";
                print "ACTUAL RESULT 3: rbusValue_Init  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "\n********** Step 4: Initiate rbusValue_SetFromString function ****************"
                value_to_Set = "string"
                print "The Value to be set for RBUSValue is ",value_to_Set

                tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
                tdkTestObj.addParameter("operation","rbusValue_SetFromString");
                tdkTestObj.addParameter("obj_count",1);
                tdkTestObj.addParameter("object_name",value_to_Set);
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Initiate rbusValue_SetFromString function";
                    print "EXPECTED RESULT 4: rbusValue_SetFromString should be success";
                    print "ACTUAL RESULT 4: rbusValue_SetFromString  was Success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;

                    print "\n********** Step 5: Start of RBUS Object Set Value ****************"
                    obj_set_value = "gTestProp"
                    print "The Value to be set for RBUS Object(obj1) is ",obj_set_value

                    tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
                    tdkTestObj.addParameter("operation","rbusObject_SetValue");
                    tdkTestObj.addParameter("obj_count",1);
                    tdkTestObj.addParameter("object_name",obj_set_value);
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Initiate rbusObject_SetValue function";
                        print "EXPECTED RESULT 5: rbusObject_SetValue should be success";
                        print "ACTUAL RESULT 5: rbusObject_SetValue  was Success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;

                        print "\n********** Step 6: Initiate rbusValue_Release function  ****************"
                        tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                        tdkTestObj.addParameter("operation","rbusValue_Release");
                        tdkTestObj.addParameter("prop_count",1);
                        tdkTestObj.addParameter("property_name","dummy");
                        expectedresult = "SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Initiate rbusValue_Release function";
                            print "EXPECTED RESULT 6: rbusValue_Release should be success";
                            print "ACTUAL RESULT 6: rbusValue_Release  was Success";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;

                            print "\n********** Step 7: Initiate rbusObject_GetValue function ****************"
                            print "Get the Value of RBUS Object(obj1) "
                            tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
                            tdkTestObj.addParameter("operation","rbusObject_GetValue");
                            tdkTestObj.addParameter("obj_count",1);
                            tdkTestObj.addParameter("object_name","gTestProp");
                            expectedresult = "SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            get_value = tdkTestObj.getResultDetails();

                            print "\n Value retrieved from rbusObject_GetValue is ",get_value

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7: Initiate rbusObject_GetValue function";
                                print "EXPECTED RESULT 7: rbusObject_GetValue should be success";
                                print "ACTUAL RESULT 7: rbusObject_GetValue  was Success";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;

                                if get_value == value_to_Set:
                                    print "Value Received from rbusObject_GetValue(%s) is Matching with Set value (%s)" %(get_value,value_to_Set)
                                    tdkTestObj.setResultStatus("SUCCESS");
                                else:
                                    print "Value Received from rbusObject_GetValue(%s) is NOT Matching with Set value (%s)" %(get_value,value_to_Set)
                                    tdkTestObj.setResultStatus("FAILURE");
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 7: Initiate rbusObject_GetValue function";
                                print "EXPECTED RESULT 7: rbusObject_GetValue should be success";
                                print "ACTUAL RESULT 7: rbusObject_GetValue was Failed";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Initiate rbusValue_Release function";
                            print "EXPECTED RESULT 6: rbusValue_Release should be success";
                            print "ACTUAL RESULT 6: rbusValue_Release  was Failed";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Initiate rbusObject_SetValue function";
                        print "EXPECTED RESULT 5: rbusObject_SetValue should be success";
                        print "ACTUAL RESULT 5: rbusObject_SetValue  was Failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Initiate rbusValue_SetFromString function";
                    print "EXPECTED RESULT 4: rbusValue_SetFromString should be success";
                    print "ACTUAL RESULT 4: rbusValue_SetFromString  was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Initiate rbusValue_Init function";
                print "EXPECTED RESULT 3: rbusValue_Init should be success";
                print "ACTUAL RESULT 3: rbusValue_Init  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "\n********** Start of RBUS Object GetName ****************"
            print "Get the Object Name for obj1"
            tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
            tdkTestObj.addParameter("operation","rbusObject_GetName");
            tdkTestObj.addParameter("obj_count",1);
            tdkTestObj.addParameter("object_name","dummy");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            name = tdkTestObj.getResultDetails();
            print "value of name is ",name

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 8: Initiate rbusObject_GetName function";
                print "EXPECTED RESULT 8: rbusObject_GetName should be success";
                print "ACTUAL RESULT 8: rbusObject_GetName  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;

                if name == obj_name:
                    print "Name Retrieved from rbusObject_GetName(%s) function is Matching with initial value (%s)" %(name,obj_name)
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "Name Retrieved from rbusObject_GetName(%s) function is NOT Matching with initial value (%s)" %(name,obj_name)
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 8: Initiate rbusObject_GetName function";
                print "EXPECTED RESULT 8: rbusObject_GetName should be success";
                print "ACTUAL RESULT 8: rbusObject_GetName was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            print "********** End of RBUS Object GetName ****************"

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Initiate rbusObject_Init function";
            print "EXPECTED RESULT 2: rbusObject_Init should be success";
            print "ACTUAL RESULT 2: rbusObject_Init was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Object Init ****************"

        print "\n********** Start of RBUS Object Release ****************"
        print "Release the Object obj1"
        tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
        tdkTestObj.addParameter("operation","rbusObject_Release");
        tdkTestObj.addParameter("obj_count",1);
        tdkTestObj.addParameter("object_name",obj_name);
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 9: Initiate rbusObject_Release function";
            print "EXPECTED RESULT 9: rbusObject_Release should be success";
            print "ACTUAL RESULT 9: rbusObject_Release  was Success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 9: Initiate rbusObject_Release function";
            print "EXPECTED RESULT 9: rbusObject_Release should be success";
            print "ACTUAL RESULT 9: rbusObject_Release was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Object Release ****************\n"

        print "********** Start of RBUS Close ****************"
        tdkTestObj = obj.createTestStep('RBUS_Close');
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS close Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 10: Close the RBUS connection";
            print "EXPECTED RESULT 10: rbus_close should be success";
            print "ACTUAL RESULT 10: rbus_close was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 10: Close the RBUS connection";
            print "EXPECTED RESULT 10: rbus_close should be success";
            print "ACTUAL RESULT 10: rbus_close was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Close ****************"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    print "********** End of RBUS Open ****************\n"
    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
