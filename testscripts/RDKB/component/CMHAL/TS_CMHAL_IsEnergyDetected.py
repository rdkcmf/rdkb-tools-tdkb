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
  <name>TS_CMHAL_IsEnergyDetected</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_IsEnergyDetected</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the CM HAL API docsis_IsEnergyDetected()</synopsis>
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
    <test_case_id>TC_CMHAL_79</test_case_id>
    <test_objective>To validate the CM HAL API docsis_IsEnergyDetected()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_IsEnergyDetected()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the CM HAL module
2. From the script invoke the CMHAL API docsis_IsEnergyDetected() and store the result
3. Get the current operational mode using TR181 parameter , If the value is DOCSIS then set docsis_enable flag as 1 else 0
4. Compare the value from HAL and docsis_enable, both should be same
5. Unload the CMHAL module</automation_approch>
    <expected_output>Energy Detected status  should be retrieved successfully </expected_output>
    <priority>High</priority>
    <test_stub_interface>cmhal</test_stub_interface>
    <test_script>TS_CMHAL_IsEnergyDetected</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
cmobj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_IsEnergyDetected');
cmobj.configureTestCase(ip,port,'TS_CMHAL_IsEnergyDetected');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
cmloadmodulestatus =cmobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %cmloadmodulestatus ;

if "SUCCESS" in (loadmodulestatus.upper() and cmloadmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    cmobj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = cmobj.createTestStep("CMHAL_IsEnergyDetected");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Status = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Energy Detected status";
        print "EXPECTED RESULT 1: Should get the Energy Detected status successfully";
        print "ACTUAL RESULT 1: Details : ",Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        value_from_hal = Status.split(':')[1].strip().replace("\\n", "");

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EthernetWAN.CurrentOperationalMode");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        CurrentOperationalMode = tdkTestObj.getResultDetails().strip();

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the CurrentOperationalMode Value";
            print "EXPECTED RESULT 1: Should get the CurrentOperationalMode value successfully";
            print "ACTUAL RESULT 1: CurrentOperationalMode Value retrieved successfully %s"%CurrentOperationalMode ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if CurrentOperationalMode.upper() == "DOCSIS":
                docsis_enabled = 1;
            else:
                docsis_enabled = 0;

            print "docsis_enabled is %s"%docsis_enabled
            print "Value returned from HAL is %s"%value_from_hal

            #Is_EnergyDetected will return 1 if docsis signal found else 0
            if int(docsis_enabled) == int(value_from_hal):
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Validate the Value Returned from CM HAL is proper";
                print "EXPECTED RESULT 1: Docsis enable value and value from HAL should be same";
                print "ACTUAL RESULT 1: Docsis enable value retrieved from current operational mode and value from HAL is same";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Validate the Value Returned from CM HAL is proper";
                print "EXPECTED RESULT 1: Docsis enable value and value from HAL should be same";
                print "ACTUAL RESULT 1: Docsis enable value retrieved from current operational mode and value from HAL is NOT same";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the CurrentOperationalMode Value";
            print "EXPECTED RESULT 1: Should get the CurrentOperationalMode value successfully";
            print "ACTUAL RESULT 1: CurrentOperationalMode Value NOT retrieved successfully ";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Energy Detected status";
        print "EXPECTED RESULT 1: Should get the Energy Detected status successfully";
        print "ACTUAL RESULT 1: Failed to get the Energy Detected Status";
        print "[TEST EXECUTION RESULT] : FAILURE";

    cmobj.unloadModule("cmhal");
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    cmobj.setLoadModuleStatus("FAILURE");
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
