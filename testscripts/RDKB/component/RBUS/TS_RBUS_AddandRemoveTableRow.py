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
  <version>13</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_AddandRemoveTableRow</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_PropertyCommands</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the RBUS 2.0 API rbusTable_addRow and rbusTable_addRow to add and remove row in existing table</synopsis>
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
    <test_case_id>TC_RBUS_70</test_case_id>
    <test_objective>To Validate the RBUS 2.0 API rbusTable_addRow and rbusTable_addRow to add and remove row in existing table</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode
</pre_requisite>
    <api_or_interface_used>rbusTable_addRow
rbusTable_addRow </api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Open the RBUS connection using rbus_open API
2. Get the initial number of entries of users Tree (Device.Users.UserNumberOfEntries) and store it
3. Add a new row to the table using rbusTable_addRow API and return status should be success
4. Get the number of entries again and the value should be greater than the initial value
5. Remove the added row using the instance number form step 3 using rbusTable_removeRow and return status should be success
6. Get the number of entries again and the value should be equals to the initial value
7. Close the RBUS connection using rbus_close API</automation_approch>
    <expected_output>Should be able to add and remove table row using rbusTable_addRow and rbusTable_removeRow APIs</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_AddandRemoveTableRow</test_script>
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
obj.configureTestCase(ip,port,'TS_RBUS_AddandRemoveTableRow');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    print "\n********** Start of RBUS Open ******************"
    tdkTestObj = obj.createTestStep('RBUS_Open');
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "RBUS status is %s" %details;

        parameter_no_of_entries = "Device.Users.UserNumberOfEntries"
        parameter_name = "Device.Users.User."

        tdkTestObj = obj.createTestStep('RBUS_GetValue');
        tdkTestObj.addParameter("paramType","UnsignedInt");
        tdkTestObj.addParameter("paramName",parameter_no_of_entries);
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initial_value = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and initial_value != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the value of parameter using rbusValue_GetUInt32";
            print "EXPECTED RESULT 2: Should get the value of the parameter: ",parameter_no_of_entries;
            print "ACTUAL RESULT 2: value of the parameter is ",initial_value;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "\n ***************** Initial No of Entries %s **************\n" %initial_value

            print "************ Start of rbusTable_addRow ***************************"
            tdkTestObj = obj.createTestStep('RBUS_TableRowCommands');
            tdkTestObj.addParameter("operation","rbusTable_addRow");
            tdkTestObj.addParameter("table_row",parameter_name);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            ins_num = tdkTestObj.getResultDetails();
            print "\n************ Instance Number is %s **************\n" %ins_num

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Initiate rbusTable_addRow function";
                print "EXPECTED RESULT 3: rbusTable_addRow should be success";
                print "ACTUAL RESULT 3: rbusTable_addRow  was Success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                tdkTestObj = obj.createTestStep('RBUS_GetValue');
                tdkTestObj.addParameter("paramType","UnsignedInt");
                tdkTestObj.addParameter("paramName",parameter_no_of_entries);
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                new_count = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the value of parameter using rbusValue_GetUInt32";
                    print "EXPECTED RESULT 4: Should get the value of the parameter: ",parameter_no_of_entries;
                    print "ACTUAL RESULT 4: value of the parameter is ",new_count;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    print "\n ****************** No of Entries after addrow is %s ****************\n" %new_count

                    if int(new_count) == (int(initial_value) + 1):
                        print "The value of Number of Entries is increased by 1 after adding one row"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "The value of Number of Entries is NOT increased by 1 after adding one row"
                        tdkTestObj.setResultStatus("FAILURE");

                    #Remove the added row Even number of entries are not changed
                    print "************ Start of rbusTable_removeRow ***************************"
                    parameter_to_remove = parameter_name + str(ins_num) + '.';
                    print "Table Row To be Removed is ", parameter_to_remove

                    tdkTestObj = obj.createTestStep('RBUS_TableRowCommands');
                    tdkTestObj.addParameter("operation","rbusTable_removeRow");
                    tdkTestObj.addParameter("table_row",parameter_to_remove);
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Initiate rbusTable_removeRow function";
                        print "EXPECTED RESULT 5: rbusTable_removeRow should be success";
                        print "ACTUAL RESULT 5: rbusTable_removeRow  was Success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                        tdkTestObj = obj.createTestStep('RBUS_GetValue');
                        tdkTestObj.addParameter("paramType","UnsignedInt");
                        tdkTestObj.addParameter("paramName",parameter_no_of_entries);
                        expectedresult = "SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        after_remove = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Get the value of parameter using rbusValue_GetUInt32";
                            print "EXPECTED RESULT 6: Should get the value of the parameter: ",parameter_no_of_entries;
                            print "ACTUAL RESULT 6: value of the parameter is ",after_remove;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                            print "\n ***************** No of entries after removerow is %s" %after_remove

                            if int(after_remove) == int(initial_value):
                                print "The value of Number of Entries is Decreased by 1 after removing one row"
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "The value of Number of Entries is NOT Decreased by 1 after removing one row"
                                tdkTestObj.setResultStatus("FAILURE");

                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Get the value of parameter using rbusValue_GetUInt32";
                            print "EXPECTED RESULT 6: Should get the value of the parameter: ",parameter_no_of_entries;
                            print "ACTUAL RESULT 6: value of the parameter is ",details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Initiate rbusTable_removeRow function";
                        print "EXPECTED RESULT 5: rbusTable_removeRow should be success";
                        print "ACTUAL RESULT 5: rbusTable_removeRow  was Failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    print "************ End of rbusTable_removeRow ***************************"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the value of parameter using rbusValue_GetUInt32";
                    print "EXPECTED RESULT 4: Should get the value of the parameter: ",parameter_no_of_entries;
                    print "ACTUAL RESULT 4: value of the parameter is ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Initiate rbusTable_addRow function";
                print "EXPECTED RESULT 3: rbusTable_addRow should be success";
                print "ACTUAL RESULT 3: rbusTable_addRow was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            print "************ End of rbusTable_addRow ***************************"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the value of parameter using rbusValue_GetUInt32";
            print "EXPECTED RESULT 2: Should get the value of the parameter: ",parameter_no_of_entries;
            print "ACTUAL RESULT 2: Failed to get the value of the parameter "
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "\n********** Start of RBUS Close ******************"
        tdkTestObj = obj.createTestStep('RBUS_Close');
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS close Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 7: Close the RBUS connection";
            print "EXPECTED RESULT 7: rbus_close should be success";
            print "ACTUAL RESULT 7: rbus_close was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 7: Close the RBUS connection";
            print "EXPECTED RESULT 7: rbus_close should be success";
            print "ACTUAL RESULT 7: rbus_close was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Open ******************"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    print "********** End of RBUS Open ******************\n"
    obj.unloadModule("rbus");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";