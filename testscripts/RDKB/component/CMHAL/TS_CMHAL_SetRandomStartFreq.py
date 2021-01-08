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
  <name>TS_CMHAL_SetRandomStartFreq</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_SetStartFreq</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set a random value as StartFreq using the api docsis_SetStartFreq()</synopsis>
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
    <test_case_id>TC_CMHAL_56</test_case_id>
    <test_objective>To set the StartFreq  to a random value using the api docsis_SetStartFreq()</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_SetStartFreq()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load CMHAL Module
2. Get and save the Start frequency
3. Set the start frequency to an invalid value
4. Validate the set function using get, that the start frequency has not changed
5. Revert the start frequency, in case it got changed to invalid value
6. Unload CMHAL module</automation_approch>
    <expected_output>The api docsis_SetStartFreq() should not set the given random Start Frequency</expected_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_SetRandomStartFreq</test_script>
    <skipped>No</skipped>
    <release_version>M62</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_SetRandomStartFreq');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
    tdkTestObj.addParameter("paramName","DownFreq");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    startFreq = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the start frequency";
        print "EXPECTED RESULT 1: Should get the start frequency";
        print "ACTUAL RESULT 1: Start frequency is %s" %startFreq;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        setValue = int(startFreq) + 1000;
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("CMHAL_SetStartFreq");
        tdkTestObj.addParameter("Value",setValue);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the Start frequency to a random value";
            print "EXPECTED RESULT 2: Setting a random value as the start frequency must fail";
            print "ACTUAL RESULT 2:  ",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #validate the set function using get
            tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
            tdkTestObj.addParameter("paramName","DownFreq");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            newStartFreq = tdkTestObj.getResultDetails();
    	    if expectedresult in actualresult and int(newStartFreq) != setValue:
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 3: Get the start frequency and check if it became the random value set";
    	        print "EXPECTED RESULT 3: Start frequency should not change to the random value: ",setValue;
    	        print "ACTUAL RESULT 3: New Start frequency is %s" %newStartFreq;
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
	        #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
    	        print "TEST STEP 3: Get the start frequency and check if it became the random value set";
    	        print "EXPECTED RESULT 3: Start frequency should not change to the random value: ",setValue;
                print "ACTUAL RESULT 3: Start frequency is %s" %newStartFreq;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

	        #Revert the start freq
	        tdkTestObj = obj.createTestStep("CMHAL_SetStartFreq");
                tdkTestObj.addParameter("Value",int(startFreq));
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Revert the value of Start frequency";
                    print "EXPECTED RESULT 4: Should revert the start frequency";
                    print "ACTUAL RESULT 4:  ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
	        else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Revert the value of Start frequency";
                    print "EXPECTED RESULT 4: Should revert the start frequency";
                    print "ACTUAL RESULT 4:  ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the Start frequency";
            print "EXPECTED RESULT 2: Should set the start frequency";
            print "ACTUAL RESULT 2:  ",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the start frequency";
        print "EXPECTED RESULT 1: Should get the start frequency";
        print "ACTUAL RESULT 1: Start frequency is %s" %StartFreq;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("cmhal");

else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
