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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_GetSessionID</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_Session</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get the current sessionID value using rbus_getCurrentSession API</synopsis>
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
    <test_case_id>TC_RBUS_19</test_case_id>
    <test_objective>To Get the current sessionID value using rbus_getCurrentSession API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_createSession
rbus_getCurrentSession
rbus_closeSession</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the rbus module
2. Open the rbus connection using rbus_open RBUS API
3. Create the rbus session using rbus_createSession RBUS API and stroe the session ID value
4. Get the current Session ID value using rbus_getCurrentSession RBUS API and store the session ID value
5. Compare the Session from created session(step3) and CurrentSession(step4) , both values should be matching
6. Close the created session using rbus_closeSession RBUS API with the sessionID from step 3.
7. Close the rbus connection using rbus_close RBUS API
8. Unload the module</automation_approch>
    <expected_output>Should be able to get the current Session ID value</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_GetSessionID</test_script>
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
obj.configureTestCase(ip,port,'TS_RBUS_GetSessionID');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

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

        tdkTestObj = obj.createTestStep('RBUS_Session');
        tdkTestObj.addParameter("operation","CreateSession");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        session_ID = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Create session using rbus_createSession";
            print "EXPECTED RESULT 2: Session should be created ";
            print "ACTUAL RESULT 2: Session was created successfully, SessionID: ",session_ID
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            tdktestObj = obj.createTestStep('RBUS_Session');
            tdkTestObj.addParameter("operation","GetSession");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            current_sessionID = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the current sessionID using rbus_getCurrentSession";
                print "EXPECTED RESULT 3: Should get the current session ID ";
                print "ACTUAL RESULT 3: Session ID was retrieved successfully: SessionID is ",current_sessionID;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                if int(current_sessionID) == int(session_ID):
                    print "Current SessionID is Matching with Created SessionID"
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "Current SessionID is NOT matching with Created SessionID"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the current sessionID using rbus_getCurrentSession";
                print "EXPECTED RESULT 3: Should get the current session ID ";
                print "ACTUAL RESULT 3: Failed to get the current Session ID";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            tdkTestObj = obj.createTestStep('RBUS_CloseSession');
            tdkTestObj.addParameter("sessionid",int(session_ID));
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Close the session using rbus_closeSession";
                print "EXPECTED RESULT 4: Session should be Closed ";
                print "ACTUAL RESULT 4: Session was Closed successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Close the session using rbus_closeSession";
                print "EXPECTED RESULT 4: Session should be Closed ";
                print "ACTUAL RESULT 4: Closing the session was failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Create session using rbus_createSession";
            print "EXPECTED RESULT 2: Session should be created ";
            print "ACTUAL RESULT 2: Creation of sessionID failed ";
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
            print "TEST STEP 5: Close the RBUS connection";
            print "EXPECTED RESULT 5: rbus_close should be success";
            print "ACTUAL RESULT 5: rbus_close was success";
             #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 5: Close the RBUS connection";
            print "EXPECTED RESULT 5: rbus_close should be success";
            print "ACTUAL RESULT 5: rbus_close was Failed";
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