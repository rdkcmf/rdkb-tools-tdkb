##########################################################################
#If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_CMHAL_GetToDStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check whether the ToD Status is Complete if the CMStatus is OPERTAIONAL</synopsis>
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
    <test_case_id>TC_CMHAL_38</test_case_id>
    <test_objective>To check whether the ToD Status is Complete if the CMStatus is OPERTAIONAL</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetDOCSISInfo</api_or_interface_used>
    <input_parameters>paramName : "ToDStatus"</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Invoke docsis_GetDOCSISInfo to get the ToD Status
3. Check if the ToDStatus is "Complete" if the CMStatus is "OPERATIONAL"
4. The test should return FAILURE otherwise
5. Unload cmhal module</automation_approch>
    <except_output>The ToDStatus should be Complete if the CMStatus is OPERATIONAL</except_output>
    <priority>High</priority>
    <test_stub_interface>CM_HAL</test_stub_interface>
    <test_script>TS_CMHAL_GetToDStatus</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_CMHAL_GetToDStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
    tdkTestObj.addParameter("paramName","CMStatus");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Status = tdkTestObj.getResultDetails();
    
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the status of cable modem";
        print "EXPECTED RESULT 1: Should get the status of cable modem successfully successfully";
        print "ACTUAL RESULT 1: Status of cable modem is %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    
        #This method invokes the HAL API docsis_GetDOCSISInfo to retrieve the ToD Status
        tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
        tdkTestObj.addParameter("paramName","ToDStatus");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        ToD_Status = tdkTestObj.getResultDetails();


        if expectedresult in actualresult and "OPERATIONAL" in Status and "Complete" in ToD_Status:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get ToDStatus as Complete  ";
            print "EXPECTED RESULT 1: Should get the ToDStatus as Complete";
            print "ACTUAL RESULT 1: The ToDStatus is %s" %ToD_Status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get ToDStatus as Complete";
            print "EXPECTED RESULT 1:Should get the ToDStatus as Complete ";
            print "ACTUAL RESULT 1: Failed to get the ToDStatus as Complete, Details %s" %ToD_Status;
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
         #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the status of cable modem";
        print "EXPECTED RESULT 1: Should get the status of cable modem successfully";
        print "ACTUAL RESULT 1: Failed to get the status of cable modem %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
