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
  <name>TS_MTAHAL_devResetNow</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MTAHAL_devResetNow</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Reset the MTA device.</synopsis>
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
    <test_case_id>TC_MTAHAL_39</test_case_id>
    <test_objective>Reset the MTA device</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mta_hal_InitDB()</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load mtahal module
2. Using TS_MTAHAL_devResetNow to invoke mta_hal_devResetNow() to reset the MTA.
3. Using TS_MTAHAL_getMtaOperationalStatus to invoke mta_hal_getMtaOperationalStatus() to get the MTA operational status, when MTA_COMPLETE is received, MTA reset is done.
4. Unload mtahal module</automation_approch>
    <except_output>The MTA device should be reset</except_output>
    <priority>High</priority>
    <test_stub_interface>MTAHAL</test_stub_interface>
    <test_script>TS_MTAHAL_devResetNow</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib
import time

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mtahal","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MTAHAL_devResetNow')

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus 

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MTAHAL_devResetNow")    
    expectedresult="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()    
    resultDetails = " "
    resultDetails = tdkTestObj.getResultDetails()

    if expectedresult in actualresult and resultDetails != " ":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print "TEST STEP 1: Reset the MTA device"
        print "EXPECTED RESULT 1: Should reset the MTA device successfully"
        print "ACTUAL RESULT 1:  %s" %resultDetails;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        # sleep a while when MTA device resets
        time.sleep(30)

        resultDetails = " "
        timeout = time.time() + 30
        while (resultDetails.find('MTA_COMPLETE') == -1 and resultDetails.find('MTA_ERROR') == -1):

            if time.time() >= timeout:
                tdkTestObj.setResultStatus("FAILURE")
                print "TEST EXECUTION TIMEOUT"
                print "[TEST EXECUTION RESULT] : FAILURE"
                break

            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("MTAHAL_getMtaOperationalStatus")    
            expectedresult="SUCCESS"
            tdkTestObj.executeTestCase(expectedresult)
            actualresult = tdkTestObj.getResult()    
            resultDetails = " "
            resultDetails = tdkTestObj.getResultDetails()
            
            if expectedresult in actualresult and resultDetails != " ":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS")
                print "TEST STEP 2: Get MTA Operational Status"
                print "EXPECTED RESULT 2: Should get MTA operational status successfully"
                print "ACTUAL RESULT 2:  %s" %resultDetails;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print "TEST STEP 2: Get MTA Operational Status"
                print "EXPECTED RESULT 2: Should get MTA operational status successfully"
                print "ACTUAL RESULT 2: Failed to get MTA operational status, Details: %s" %resultDetails;
                print "[TEST EXECUTION RESULT] : FAILURE"

            # sleep a while when MTA device resets in progress
            time.sleep(1)

    else:
        tdkTestObj.setResultStatus("FAILURE")
        print "TEST STEP 1: Reset the MTA device"
        print "EXPECTED RESULT 1: Should reset the MTA device successfully"
        print "ACTUAL RESULT 1: Failed to reset the MTA device, Details: %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("mtahal")    
else:
    print "Failed to load the module"
    obj.setLoadModuleStatus("FAILURE")
    print "Module loading failed"

