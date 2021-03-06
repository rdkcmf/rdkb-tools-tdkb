##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_MTAHAL_SetDSXLogEnableOn</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MTAHAL_SetParamUlongValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set value 1 to DSXLogEnable</synopsis>
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
    <test_case_id>TC_MTAHAL_11</test_case_id>
    <test_objective>Set value 1 to DSXLogEnable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mta_hal_SetDSXLogEnable()</api_or_interface_used>
    <input_parameters>Boolean 1</input_parameters>
    <automation_approch>1. Load mtahal module
2. Save the current value of DSXLogEnable
3. Using TS_MTAHAL_SetDSXLogEnableOn invoke mta_hal_SetDSXLogEnable() to see if the value of DSX enable can be set to 1 or not. If available return SUCCESS and exit else return FAILURE and exit.
4. If SUCCESS, check if the DSXLogEnable is 1 or not.
5. Restore the value from (3) to DSXLogEnable
6. Unload mtahal module</automation_approch>
    <except_output>Value (1) to set DSX log enable to</except_output>
    <priority>High</priority>
    <test_stub_interface>MTAHAL</test_stub_interface>
    <test_script>TS_MTAHAL_SetDSXLogEnableOn</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mtahal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MTAHAL_SetDSXLogEnableOn');
#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    # Get the current value of DSXLogEnable
    tdkTestObj = obj.createTestStep("MTAHAL_GetParamUlongValue");
    tdkTestObj.addParameter("paramName","DSXLogEnable");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    currValue = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Script to load the configuration file of the component
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current value of DSXLogEnable";
        print "EXPECTED RESULT 1: Should get the DSXLogEnable successfully";
        print "ACTUAL RESULT 1: The current value of DSXLogEnable is %s" %currValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep("MTAHAL_SetParamUlongValue");
        tdkTestObj.addParameter("paramName","DSXLogEnable");
        tdkTestObj.addParameter("value",1);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        resultDetails = tdkTestObj.getResultDetails();
        
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the DSXLogEnable";
            print "EXPECTED RESULT 2: Should set the DSXLogEnable successfully";
            print "ACTUAL RESULT 2: The DSXLogEnable is %s (1)" %resultDetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            # Get the value of DSXLogEnable
            tdkTestObj = obj.createTestStep("MTAHAL_GetParamUlongValue");
            tdkTestObj.addParameter("paramName","DSXLogEnable");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            DSXLogEnable  = tdkTestObj.getResultDetails();
            print "DSXLogEnable before converting to little endian:",DSXLogEnable
  
            #if the received value is not 1
            #Doing a conversion from Bigendian to little endian
            if DSXLogEnable != 1:
               num = int(DSXLogEnable)
               #converting to binary value
               binarynum  = bin(num)[2:]
               #removing the appened character b
               reversenum =  binarynum[::-1]
               #reversing the number to get a decimal value
               DSXLogEnable = int(reversenum,2)
               print"DSXLogEnable after converting to little endian:",DSXLogEnable
              

            if expectedresult in actualresult and DSXLogEnable  == 1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the value of DSXLogEnable";
                print "EXPECTED RESULT 3: Should get the DSXLogEnable successfully";
                print "ACTUAL RESULT 3: The current value of DSXLogEnable is %s" %DSXLogEnable;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the value of DSXLogEnable";
                print "EXPECTED RESULT 3: Should get the DSXLogEnable successfully";
                print "ACTUAL RESULT 3: Failed to get the DSXLogEnable, Details : %s" %DSXLogEnable;
                print "[TEST EXECUTION RESULT] : FAILURE";            
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the DSXLogEnable";
            print "EXPECTED RESULT 2: Should set the DSXLogEnable successfully";
            print "ACTUAL RESULT 2: Failed to set the DSXLogEnable, Details : %s" %resultDetails;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current value of DSXLogEnable";
        print "EXPECTED RESULT 1: Should get the DSXLogEnable successfully";
        print "ACTUAL RESULT 1: Failed to get the DSXLogEnable, Details : %s" %currValue;
        print "[TEST EXECUTION RESULT] : FAILURE";

    # Revert the value (currValue) of DSXLogEnable
    tdkTestObj = obj.createTestStep("MTAHAL_SetParamUlongValue");
    tdkTestObj.addParameter("paramName","DSXLogEnable");
    tdkTestObj.addParameter("value",int(currValue));
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    resultDetails = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 4: Revert the previous value of DSXLogEnable";
        print "EXPECTED RESULT 4: Should set the DSXLogEnable successfully";
        print "ACTUAL RESULT 4: The DSXLogEnable is %s (%s)" %(resultDetails, currValue);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 4: Revert the previous value of DSXLogEnable";
        print "EXPECTED RESULT 4: Should set the DSXLogEnable successfully";
        print "ACTUAL RESULT 4: Failed to set the DSXLogEnable, Details : %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("mtahal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";



