##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_MTAHAL_InitDB</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MTAHAL_InitDB</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Retrieves the global information for all shared DBs and makes them accessible locally.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_MTAHAL_38</test_case_id>
    <test_objective>Retrieves the global information for all shared DBs</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mta_hal_InitDB()</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load mtahal module
2. Using TS_MTAHAL_InitDB invoke mta_hal_InitDB() to initialize the MTA.
3. Using TS_MTAHAL_GetMtaResetCount invoke mta_hal_Get_MTAResetCount() to check if the count is zero.
4. Using TS_MTAHAL_GetLineResetCount invoke mta_hal_Get_LineResetCount() to check if the count is zero.
5. Unload mtahal module</automation_approch>
    <except_output>The api should initialize the DB</except_output>
    <priority>High</priority>
    <test_stub_interface>MTAHAL</test_stub_interface>
    <test_script>TS_MTAHAL_InitDB</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mtahal","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MTAHAL_InitDB')

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus 

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MTAHAL_InitDB")    
    expectedresult="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()    
    resultDetails = " "
    resultDetails = tdkTestObj.getResultDetails()

    if expectedresult in actualresult and resultDetails != " ":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print "TEST STEP 1: Initializing the DB of MTA"
        print "EXPECTED RESULT 1: Should initialize the MTA DB successfully"
        print "ACTUAL RESULT 1:  %s" %resultDetails;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("MTAHAL_GetParamUlongValue");
        tdkTestObj.addParameter("paramName","MTAResetCount");
        expectedresult="SUCCESS"
        tdkTestObj.executeTestCase(expectedresult)
        actualresult = tdkTestObj.getResult()    
        resultDetails = tdkTestObj.getResultDetails()
        
        if expectedresult in actualresult and resultDetails == "0":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the MtaResetCount";
            print "EXPECTED RESULT 2: Should get the MtaResetCount successfully";
            print "ACTUAL RESULT 2: The MtaResetCount is %s" %resultDetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("MTAHAL_GetParamUlongValue");
            tdkTestObj.addParameter("paramName","LineResetCount");
            expectedresult="SUCCESS"
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()    
            resultDetails = tdkTestObj.getResultDetails()
            
            if expectedresult in actualresult and resultDetails == "0":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the LineResetCount";
                print "EXPECTED RESULT 2: Should get the LineResetCount successfully";
                print "ACTUAL RESULT 2: The LineResetCount is %s" %resultDetails;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Get the LineResetCount";
                print "EXPECTED RESULT 2: Should get the LineResetCount successfully";
                print "ACTUAL RESULT 2: Failed to get the LineResetCount, Details : %s" %resultDetails;
                print "[TEST EXECUTION RESULT] : FAILURE";

        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the MtaResetCount";
            print "EXPECTED RESULT 2: Should get the MtaResetCount successfully";
            print "ACTUAL RESULT 2: Failed to get the MtaResetCount, Details : %s" %resultDetails;
            print "[TEST EXECUTION RESULT] : FAILURE";
 
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print "TEST STEP 1: Initializing the DB of MTA"
        print "EXPECTED RESULT 1: Should initialize the MTA DB successfully"
        print "ACTUAL RESULT 1: Failed to initialise the MTA DB, Details: %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("mtahal")
else:
    print "Failed to load the module"
    obj.setLoadModuleStatus("FAILURE")
    print "Module loading failed"
