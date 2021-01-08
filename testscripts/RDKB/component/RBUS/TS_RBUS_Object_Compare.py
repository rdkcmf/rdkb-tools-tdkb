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
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_Object_Compare</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_ObjectCommands</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the RBUS 2.0 API rbusObject_Compare</synopsis>
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
    <test_case_id>TC_RBUS_66</test_case_id>
    <test_objective>To Validate the RBUS 2.0 API rbusObject_Compare</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbusObject_Compare</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Open the RBUS connection using rbus_open API
2. Initiate the RBUS value using rbusValue_Init and set string value to it using rbusValue_Init API
3. Initiate the RBUS property using rbusProperty_Init with rbus value from step 2 and release the RBUS value using rbusValue_Release API
4. Repeat step 2 and 3 for Property 2 initialization.
5. Initiate 4 different Objects (two parent objects and two child objects) using rbusObject_Init API
6. Set the Property for the Object using rbusObject_SetProperty API
7. set properties combination should be -  (Parent obj1 and property1), (parent obj2 and property2) , (child obj1 and property1 ) and (child obj2 and property2)
8. Release the properties using rbusProperty_Release API
9. Set the children to the Object using rbusObject_SetChildren API, the combination was (parent obj1 and child obj1 ) and (parent obj2 and child obj2)
10. Compare the Objects using rbusObject_Compare , the return status should be success and value should be zero.
11. Release all the objects using rbusObject_Release API and return status should be success
12. Close the RBUS Connection using rbus_close API
</automation_approch>
    <expected_output>rbusObject_Compare should return zero if RBUS objects has same property values</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_Object_Compare</test_script>
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
obj.configureTestCase(ip,port,'TS_RBUS_Object_Compare');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    obj_name = "gTestObject"
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

        for count in range (1,3):
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

                value_to_set = "string1"
                print "Value to be set for RBUSValue is ",value_to_set

                tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
                tdkTestObj.addParameter("operation","rbusValue_SetFromString");
                tdkTestObj.addParameter("obj_count",1);
                tdkTestObj.addParameter("object_name",value_to_set);
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Initiate rbusValue_SetFromString function";
                    print "EXPECTED RESULT 3: rbusValue_SetFromString should be success";
                    print "ACTUAL RESULT 3: rbusValue_SetFromString  was Success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;

                    print "Initialize the Property prop%d with property name %s" %(count,prop_name);
                    tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
                    tdkTestObj.addParameter("operation","rbusProperty_Init");
                    tdkTestObj.addParameter("prop_count",count);
                    tdkTestObj.addParameter("property_name",prop_name);
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Validate rbusProperty_Init function";
                        print "EXPECTED RESULT 4: rbusProperty_Init should be success";
                        print "ACTUAL RESULT 4: rbusProperty_Init  was Success";
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
                            print "TEST STEP 5: Initiate rbusValue_Release function";
                            print "EXPECTED RESULT 5: rbusValue_Release should be success";
                            print "ACTUAL RESULT 5: rbusValue_Release  was Success";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Initiate rbusValue_Release function";
                            print "EXPECTED RESULT 5: rbusValue_Release should be success";
                            print "ACTUAL RESULT 5: rbusValue_Release  was Failed";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Validate rbusProperty_Init function";
                        print "EXPECTED RESULT 4: rbusProperty_Init should be success";
                        print "ACTUAL RESULT 4: rbusProperty_Init was Failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Initiate rbusValue_SetFromString function";
                    print "EXPECTED RESULT 3: rbusValue_SetFromString should be success";
                    print "ACTUAL RESULT 3: rbusValue_SetFromString  was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s \n" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Initiate rbusValue_Init function";
                print "EXPECTED RESULT 2: rbusValue_Init should be success";
                print "ACTUAL RESULT 2: rbusValue_Init  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "\n *************** Start of RBUS Object Init Function **********************"
        for count1 in range (1,5):
            if count1 == 1 or count1 == 2:
                obj_name = "gTestObject1";
            else:
                obj_name = "gTestObject_ch1"

            print "Initialize the RBUS Object obj%d with Object name %s" %(count1,obj_name);
            tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
            tdkTestObj.addParameter("operation","rbusObject_Init");
            tdkTestObj.addParameter("obj_count",count1);
            tdkTestObj.addParameter("object_name",obj_name);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 6: Initiate rbusObject_Init function";
                print "EXPECTED RESULT 6: rbusObject_Init should be success";
                print "ACTUAL RESULT 6: rbusObject_Init  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 6: Initiate rbusObject_Init function";
                print "EXPECTED RESULT 6: rbusObject_Init should be success";
                print "ACTUAL RESULT 6: rbusObject_Init  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "*************** End of RBUS Object Init Function **********************"

        print "\n *************** Start of RBUS Object Set Property Function **********************"
        for count2 in range (1,5):
            print "Set Property for the RBUS Object obj%d" %count2
            tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
            tdkTestObj.addParameter("operation","rbusObject_SetProperty");
            tdkTestObj.addParameter("obj_count",count2);
            tdkTestObj.addParameter("object_name","dummy");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 7: Initiate rbusObject_SetProperty function";
                print "EXPECTED RESULT 7: rbusObject_SetProperty should be success";
                print "ACTUAL RESULT 7: rbusObject_SetProperty  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 7: Initiate rbusObject_SetProperty function";
                print "EXPECTED RESULT 7: rbusObject_SetProperty should be success";
                print "ACTUAL RESULT 7: rbusObject_SetProperty  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "*************** End of RBUS Object Set Property Function **********************"

        print "\n *************** Start of RBUS Property Release Function **********************"
        for count3 in range (1,3):
            print "Release the RBUS Property prop%d" %count3
            tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
            tdkTestObj.addParameter("operation","rbusProperty_Release");
            tdkTestObj.addParameter("prop_count",count3);
            tdkTestObj.addParameter("property_name","dummy");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 8: Initiate rbusProperty_Release function";
                print "EXPECTED RESULT 8: rbusProperty_Release should be success";
                print "ACTUAL RESULT 8: rbusProperty_Release  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 8: Initiate rbusProperty_Release function";
                print "EXPECTED RESULT 8: rbusProperty_Release should be success";
                print "ACTUAL RESULT 8: rbusProperty_Release  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "*************** End of RBUS Property Release Function **********************"

        print "\n *************** Start of RBUS Object SetChildren Function **********************"
        for count4 in range (1,3):
            print "Set the children for the Object obj%d" %count4
            tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
            tdkTestObj.addParameter("operation","rbusObject_SetChildren");
            tdkTestObj.addParameter("obj_count",count4);
            tdkTestObj.addParameter("object_name","dummy");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 9: Initiate rbusObject_SetChildren function";
                print "EXPECTED RESULT 9: rbusObject_SetChildren should be success";
                print "ACTUAL RESULT 9: rbusObject_SetChildren  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 9: Initiate rbusObject_SetChildren function";
                print "EXPECTED RESULT 9: rbusObject_SetChildren should be success";
                print "ACTUAL RESULT 9: rbusObject_SetChildren  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "*************** End of RBUS Property Release Function **********************"

        print "\n *************** Start of RBUS Object Compare Function **********************"
        print "Compare the Objects obj1 and obj1"
        tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
        tdkTestObj.addParameter("operation","rbusObject_Compare");
        tdkTestObj.addParameter("obj_count",1);
        tdkTestObj.addParameter("object_name","dummy");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        compare_value = tdkTestObj.getResultDetails();
        print "RBUS Object Compare value is ",compare_value

        if expectedresult in actualresult  and int(compare_value) == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 10: Initiate rbusObject_Compare function";
            print "EXPECTED RESULT 10: rbusObject_Compare should be success";
            print "ACTUAL RESULT 10: rbusObject_Compare was Success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 10: Initiate rbusObject_Compare function";
            print "EXPECTED RESULT 10: rbusObject_Compare should be success";
            print "ACTUAL RESULT 10: rbusObject_Compare  was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "*************** End of RBUS Object Compare Function **********************"

        print "\n *************** Start of RBUS Object Release Function **********************"
        for count5 in range (1,5):
            print "Release the RBUS Object obj%d" %count5
            tdkTestObj = obj.createTestStep('RBUS_ObjectCommands');
            tdkTestObj.addParameter("operation","rbusObject_Release");
            tdkTestObj.addParameter("obj_count",count5);
            tdkTestObj.addParameter("object_name","dummy");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 11: Initiate rbusObject_Release function";
                print "EXPECTED RESULT 11: rbusObject_Release should be success";
                print "ACTUAL RESULT 11: rbusObject_Release  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 11: Initiate rbusObject_Release function";
                print "EXPECTED RESULT 11: rbusObject_Release should be success";
                print "ACTUAL RESULT 11: rbusObject_Release  was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "*************** End of RBUS Property Release Function **********************"

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
            print "TEST STEP 12: Close the RBUS connection";
            print "EXPECTED RESULT 12: rbus_close should be success";
            print "ACTUAL RESULT 12: rbus_close was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 12: Close the RBUS connection";
            print "EXPECTED RESULT 12: rbus_close should be success";
            print "ACTUAL RESULT 12: rbus_close was Failed";
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