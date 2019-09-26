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
  <name>TS_MTAHAL_GetCalls</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MTAHAL_GetCalls</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Retrieve all call info for the given instance number of LineTable</synopsis>
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
    <test_case_id>TC_MTAHAL_6</test_case_id>
    <test_objective>Retrieve all call info for the given instance number of LineTable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mta_hal_GetCalls()</api_or_interface_used>
    <input_parameters>instanceNumber
Count
PMTAMGMT_MTA_CALLS</input_parameters>
    <automation_approch>1. Load mtahal module
2. Get the number of entries for the MTA
3. Using TS_MTAHAL_GetCalls invoke mta_hal_GetCalls() to see if the call info for the instance number can be triggered or not. If available return SUCCESS and exit else return FAILURE and exit.
4. Unload mtahal module</automation_approch>
    <except_output>All call info for the given instance number of LineTable</except_output>
    <priority>High</priority>
    <test_stub_interface>MTAHAL</test_stub_interface>
    <test_script>TS_MTAHAL_GetCalls</test_script>
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
obj.configureTestCase(ip,port,'TS_MTAHAL_GetCalls')

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus 

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")

    # Get number of entries for MTA
    tdkTestObj = obj.createTestStep("MTAHAL_GetParamUlongValue")
    tdkTestObj.addParameter("paramName","LineTableNumberOfEntries")
    expectedresult="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    NumOfEntries = tdkTestObj.getResultDetails()

    if expectedresult in actualresult and int(NumOfEntries) > 0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print "TEST STEP 1: Get the LineTableNumberOfEntries"
        print "EXPECTED RESULT 1: Should get the LineTableNumberOfEntries successfully"
        print "ACTUAL RESULT 1: The LineTableNumberOfEntries is %s" %NumOfEntries
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        for y in range(int(NumOfEntries)):
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("MTAHAL_GetCalls")    
            tdkTestObj.addParameter("value",y)
            expectedresult="SUCCESS"
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()    
            resultDetails = " "
            resultDetails = tdkTestObj.getResultDetails()

            if expectedresult in actualresult and resultDetails != " ":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print "TEST STEP %s: Get call info for line %s" %(y+2, y+1)
                print "EXPECTED RESULT %s: Should get the call info for line %s" %(y+2, y+1)
                print "ACTUAL RESULT %s: call info for line %s:" %(y+2, y+1)
                print ""
                for x in resultDetails.split(";"):
                    print x
                print ""
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print "TEST STEP %s: Get call info for line %s" %(y+2, y+1)
                print "EXPECTED RESULT %s: Should get the call info for line %s" %(y+2, y+1)
                print "ACTUAL RESULT %s: Failed to get the call info for line %s:" %(y+2, y+1)
                print "%s" %resultDetails
                print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print "TEST STEP 1: Get the LineTableNumberOfEntries"
        print "EXPECTED RESULT 1: Should get the LineTableNumberOfEntries successfully"
        print "ACTUAL RESULT 1: Failed to get the LineTableNumberOfEntries, Details :%s" %NumOfEntries
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("mtahal")
else:
    print "Failed to load the module"
    obj.setLoadModuleStatus("FAILURE")
    print "Module loading failed"
