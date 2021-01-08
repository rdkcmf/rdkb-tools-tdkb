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
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_Property_SetNext</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_PropertyCommands</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the RBUS 2.0 API rbusProperty_SetNext by creating three different properties</synopsis>
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
    <test_case_id>TC_RBUS_10</test_case_id>
    <test_objective>To Validate the RBUS 2.0 API rbusProperty_SetNext by creating three different properties</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbusProperty_SetNext</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Open the RBUS connection using rbus_open API
2. Initiate the BRUS values using rbusValue_Init and set the string to the value using rbusValue_SetString API
3. Initiate the Property  using rbusProperty_Init with rbus value from step 2 and release the rbus value using rbusValue_Release
4. Repeat step 2 and Step 3 for property 2 and property 3.
5. While creating second Property, set the Property Set Next with property1 and Property2 using rbusProperty_SetNext API
6. While creating Third Property, set the Property Set Next with property2 and Property3 using rbusProperty_SetNext API
7. Get all three value of the properties using rbusProperty_GetValue API
8. Get all three names of the properties using rbusProperty_GetName API
9. Compare the Names and values with the initiated values and the values should match
10. Release all three properties using rbusProperty_Release API
11. Close the RBUS connection using rbus_close API
</automation_approch>
    <expected_output>Should be able to get the Names and values of three different properties which was set for rbusProperty_SetNext</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_Property_SetNext</test_script>
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
obj.configureTestCase(ip,port,'TS_RBUS_Property_SetNext');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    prop_name = "Device.rbusPropertyTest1"

    print "\n********** Start of RBUS Open ****************"
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

        for loop in range(1,4):
            value_to_set = "test"+str(loop)
            property_to_Set = "Device.rbusPropertyTest"+str(loop)

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
                print "TEST STEP 2: Initiate rbusValue_Init function";
                print "EXPECTED RESULT 2: rbusValue_Init should be success";
                print "ACTUAL RESULT 2: rbusValue_Init  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "\nValue to be set for rbusValue is ",value_to_set
                tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                tdkTestObj.addParameter("operation","rbusValue_SetString");
                tdkTestObj.addParameter("prop_count",1);
                tdkTestObj.addParameter("property_name",value_to_set);
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Initiate rbusValue_SetString function";
                    print "EXPECTED RESULT 3: rbusValue_SetString should be success";
                    print "ACTUAL RESULT 3: rbusValue_SetString  was Success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    print "\nInitiaize the Property prop%d with Property name %s" %(loop,property_to_Set)
                    tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                    tdkTestObj.addParameter("operation","rbusProperty_Init_WithRBUSValue");
                    tdkTestObj.addParameter("prop_count",loop);
                    tdkTestObj.addParameter("property_name",property_to_Set);
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Initiate rbusProperty_Init_WithRBUSValue function";
                        print "EXPECTED RESULT 4: rbusProperty_Init_WithRBUSValue should be success";
                        print "ACTUAL RESULT 4: rbusProperty_Init_WithRBUSValue  was Success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                        if loop != 1:
                            tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                            tdkTestObj.addParameter("operation","rbusProperty_SetNext");
                            if loop == 2:
                                tdkTestObj.addParameter("prop_count",1);
                                print "Initiate the Property SetNext for Prop1 and Prop2"
                            else:
                                tdkTestObj.addParameter("prop_count",2);
                                print "Initiate the Property SetNext for Prop2 and Prop3"

                            tdkTestObj.addParameter("property_name","dummy");
                            expectedresult = "SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 5: Initiate rbusProperty_SetNext function";
                                print "EXPECTED RESULT 5: rbusProperty_SetNext should be success";
                                print "ACTUAL RESULT 5: rbusProperty_SetNext  was Success";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 5: Initiate rbusProperty_SetNext function";
                                print "EXPECTED RESULT 5: rbusProperty_SetNext should be success";
                                print "ACTUAL RESULT 5: rbusProperty_SetNext  was Failed";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

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
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Initiate rbusValue_Release function";
                            print "EXPECTED RESULT 6: rbusValue_Release should be success";
                            print "ACTUAL RESULT 6: rbusValue_Release  was Failed";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Initiate rbusProperty_Init_WithRBUSValue function";
                        print "EXPECTED RESULT 4: rbusProperty_Init_WithRBUSValue should be success";
                        print "ACTUAL RESULT 4: rbusProperty_Init_WithRBUSValue  was Success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Initiate rbusValue_SetString function";
                    print "EXPECTED RESULT 3: rbusValue_SetString should be success";
                    print "ACTUAL RESULT 3: rbusValue_SetString  was Success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Initiate rbusValue_Init function";
                print "EXPECTED RESULT 2: rbusValue_Init should be success";
                print "ACTUAL RESULT 2: rbusValue_Init  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        #End of loop....!!!

        for count in range(1,4):
            print "\nGet the Property Value for prop%d" %count
            tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
            tdkTestObj.addParameter("operation","rbusProperty_GetValue");
            tdkTestObj.addParameter("prop_count",count);
            tdkTestObj.addParameter("property_name","Device.rbusPropertyTest1");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            value = tdkTestObj.getResultDetails();
            print "rbusProperty_GetValue  Value is ",value

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 7: Initiate rbusProperty_GetValue function";
                print "EXPECTED RESULT 7: rbusProperty_GetValue should be success";
                print "ACTUAL RESULT 7: rbusProperty_GetValue  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "\nGet the Property Name for prop%d" %count
                tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                tdkTestObj.addParameter("operation","rbusProperty_GetName");
                tdkTestObj.addParameter("prop_count",1);
                tdkTestObj.addParameter("property_name","Device.rbusPropertyTest1");
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                name = tdkTestObj.getResultDetails();

                print "rbusProperty_GetName Value is ",name

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 8: Initiate rbusProperty_GetName function";
                    print "EXPECTED RESULT 8: rbusProperty_GetName should be success";
                    print "ACTUAL RESULT 8: rbusProperty_GetName  was Success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    if count == 1:
                        if name == "Device.rbusPropertyTest1" and value == "test1":
                            print "Property name %s for prop1 and its value %s is Successfully Set" %(name,value)
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Property name %s for prop1 and its value %s is NOT Successfully Set" %(name,value)
                            tdkTestObj.setResultStatus("FAILURE");
                    if count == 2:
                        if name == "Device.rbusPropertyTest2" and value == "test2":
                            print "Property name %s for prop2 and its value %s is Successfully Set" %(name,value)
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Property name %s for prop2 and its value %s is NOT Successfully Set" %(name,value)
                            tdkTestObj.setResultStatus("FAILURE");
                    if count == 3:
                        if name == "Device.rbusPropertyTest3" and value == "test3":
                            print "Property name %s for prop3 and its value %s is Successfully Set" %(name,value)
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "Property name %s for prop3 and its value %s is NOT Successfully Set" %(name,value)
                            tdkTestObj.setResultStatus("FAILURE");

                    print "\nInitiating the Property Get Next for Prop1"
                    tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                    tdkTestObj.addParameter("operation","rbusProperty_GetNext");
                    tdkTestObj.addParameter("prop_count",1);
                    tdkTestObj.addParameter("property_name","Device.rbusPropertyTest1");
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 9: Initiate rbusProperty_GetNext function";
                        print "EXPECTED RESULT 9: rbusProperty_GetNext should be success";
                        print "ACTUAL RESULT 9: rbusProperty_GetNext  was Success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 9: Initiate rbusProperty_GetNext function";
                        print "EXPECTED RESULT 9: rbusProperty_GetNext should be success";
                        print "ACTUAL RESULT 9: rbusProperty_GetNext  was Failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 8: Initiate rbusProperty_GetName function";
                    print "EXPECTED RESULT 8: rbusProperty_GetName should be success";
                    print "ACTUAL RESULT 8: rbusProperty_GetName was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 7: Initiate rbusProperty_GetValue function";
                print "EXPECTED RESULT 7: rbusProperty_GetValue should be success";
                print "ACTUAL RESULT 7: rbusProperty_GetValue was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "\n********** Start of RBUS Property Release ****************"
        for count1 in range(1,4):
            print "Release the Property prop%d" %count1
            tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
            tdkTestObj.addParameter("operation","rbusProperty_Release");
            tdkTestObj.addParameter("prop_count",count1);
            tdkTestObj.addParameter("property_name","Device.rbusPropertyTest1");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 10: Initiate rbusProperty_Release function";
                print "EXPECTED RESULT 10: rbusProperty_Release should be success";
                print "ACTUAL RESULT 10: rbusProperty_Release  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 10: Initiate rbusProperty_Release function";
                print "EXPECTED RESULT 10: rbusProperty_Release should be success";
                print "ACTUAL RESULT 10: rbusProperty_Release was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Property Release ****************\n"

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
            print "TEST STEP 11: Close the RBUS connection";
            print "EXPECTED RESULT 11: rbus_close should be success";
            print "ACTUAL RESULT 11: rbus_close was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 11: Close the RBUS connection";
            print "EXPECTED RESULT 11: rbus_close should be success";
            print "ACTUAL RESULT 11: rbus_close was Failed";
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