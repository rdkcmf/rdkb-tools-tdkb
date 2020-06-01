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
  <name>TS_MoCAHAL_GetIfAcaStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MoCAHAL_GetIfAcaStatus</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get the MoCA Interface ACA status details using the hal api  moca_getIfAcaStatus()</synopsis>
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
    <test_case_id>TC_MoCAHAL_18</test_case_id>
    <test_objective>Get the MoCA Interface ACA status details using the hal api  moca_getIfAcaStatus()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>moca_getIfAcaStatus()</api_or_interface_used>
    <input_parameters>ifIndex</input_parameters>
    <automation_approch>1. Load mocahal module
2. Invoke the HAL api moca_GetIfAcaStatus()
3. Check if the return status was success or not
4. If Success display the MoCA ACA process status
5. Unload mocahal module</automation_approch>
    <expected_output>Call to moca_GetIfAcaStatus() should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>mocahal</test_stub_interface>
    <test_script>TS_MoCAHAL_GetIfAcaStatus</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>none</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mocahal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MoCAHAL_GetIfAcaStatus');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

#Prmitive test case which associated to this Script
tdkTestObj = obj.createTestStep('MoCAHAL_GetIfAcaStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MoCAHAL_GetIfAcaStatus");

    tdkTestObj.addParameter("ifIndex",1);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    info = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and info:
        #Set the result status of execution
        print "TEST STEP 1: Get MoCA interface ACA status using moca_getIfAcaStatus()"
        print "EXPECTED RESULT 1: Should Get MoCA interface ACA status"
        info = info.replace('\\n', '\n')
        print "ACTUAL RESULT 1:  %s" %info;

        ACAStatus = info.split("ACA Status=")[1].split(",")[0]

        if int(ACAStatus) == 0:
            status_str = "SUCCESS"
        elif int(ACAStatus) == 1:
            status_str = "Fail-BADCHANNEL"
        elif int(ACAStatus) == 2:
            status_str = "Fail-NoEVMPROBE"
        elif int(ACAStatus) == 3:
            status_str = "Fail"
        elif int(ACAStatus) == 4:
            status_str = "In-Progress"
        else:
            status_str = "Invalid status"

        if status_str != "Invalid status":
            #Get the result of execution
            print "ACA Status is ", status_str;
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");
        else:
            print "Received invalid ACA status as ", ACAStatus;
            print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get MoCA interface ACA status using moca_getIfAcaStatus()"
        print "EXPECTED RESULT 1: Should Get MoCA interface ACA status"
        print "ACTUAL RESULT 1: %s" %info;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("mocahal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
