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
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_MoCAHAL_GetResetCount</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MoCAHAL_GetResetCount</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test the HAL api moca_GetResetCount()</synopsis>
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
    <test_case_id>TC_MoCAHAL_14</test_case_id>
    <test_objective>Test the HAL api moca_GetResetCount()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>moca_GetResetCount()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load mocahal module
2. Invoke the HAL api moca_GetResetCount() and save the reset count
3. Do a moca reset using Device.MoCA.Interface.1.X_CISCO_COM_Reset
4. Again check the reset count using moca_GetResetCount()
5. The new reset count should be one more than the previous value
6. UnLoad mocahal module</automation_approch>
    <except_output>moca_GetResetCount should return should return the current MoCA reset count properly</except_output>
    <priority>High</priority>
    <test_stub_interface>mocahal</test_stub_interface>
    <test_script>TS_MoCAHAL_GetResetCount</test_script>
    <skipped>No</skipped>
    <release_version>M61</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
objhal = tdklib.TDKScriptingLibrary("mocahal","1");
obj = tdklib.TDKScriptingLibrary("moca","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
objhal.configureTestCase(ip,port,'TS_MoCAHAL_GetResetCount');
obj.configureTestCase(ip,port,'TS_MoCAHAL_GetResetCount');

#Get the result of connection with test component and DUT
loadmodulestatus1 =objhal.getLoadModuleResult();
loadmodulestatus2 =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s " %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper():
    #Set the result status of execution
    objhal.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = objhal.createTestStep('MoCAHAL_GetResetCount');
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    LastResetCount= tdkTestObj.getResultDetails().split(":")[1].strip();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the MocaResetCount";
        print "EXPECTED RESULT 1: Should get the MocaResetCount";
        print "ACTUAL RESULT 1: MocaResetCount is:%s" %LastResetCount;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj.createTestStep('Mocastub_Set');
        tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.X_CISCO_COM_Reset");
        tdkTestObj.addParameter("ParamValue","true");
        tdkTestObj.addParameter("Type","bool");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details= tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set reset to true";
            print "EXPECTED RESULT 2: Should set reset to true";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = objhal.createTestStep('MoCAHAL_GetResetCount');
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            sleep(30);
            NewResetCount = tdkTestObj.getResultDetails().split(":")[1].strip();
	    Resetcount = int(LastResetCount) +1;
            print "NewResetCount : %s" %NewResetCount;
            print "Resetcount : %s" %Resetcount;
            print "LastResetCount : %s" %LastResetCount;
            if expectedresult in actualresult and str(Resetcount) in NewResetCount:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the MocaResetCount";
                print "EXPECTED RESULT 3:Should get the MocaResetCount as one incremented";
                print "ACTUAL RESULT 3: %s" %NewResetCount;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the MocaResetCount";
                print "EXPECTED RESULT 3:Should get the MocaResetCount as one incremented";
                print "ACTUAL RESULT 3: %s" %NewResetCount;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set reset to true";
            print "EXPECTED RESULT 2: Should set reset to true";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the MocaResetCount";
        print "EXPECTED RESULT 1: Should get the MocaResetCount";
        print "ACTUAL RESULT 1: MocaResetCount is:%s" %LastResetCount;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("moca");
    objhal.unloadModule("mocahal");
else:
        print "Failed to load moca module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
