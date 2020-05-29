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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_BLEHAL_Enable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>BLEHAL_Enable</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set bluetooth enable status using  BLE hal api ble_Enable() and verify using ble_GetStatus()</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_BLE_HAL_1</test_case_id>
    <test_objective>Set bluetooth enable status using  BLE hal api ble_Enable() and verify using ble_GetStatus()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>ble_Enable
ble_GetStatus</api_or_interface_used>
    <input_parameters>enable</input_parameters>
    <automation_approch>1. Load  blehal module.
2. Get the ble status using ble_GetStatus() and save it
3.Toggle the BLE enable state using ble_Enable().
4. Get the BLE enable state and check if it is same as the set state
5. Revert back the ble enable state to original value
6. Unload halethsw module</automation_approch>
    <expected_output>Should successfully change ble enable state using ble_Enable()</expected_output>
    <priority>High</priority>
    <test_stub_interface>BLEHAL</test_stub_interface>
    <test_script>TS_BLEHAL_Enable</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("blehal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_BLEHAL_Enable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        tdkTestObj = obj.createTestStep('BLEHAL_GetStatus');
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details and (details == "1" or details == "2" or  details == "3"):
            if details == "1":
                Enable_ble = 2;
                #storing states as string for logging purpose
                toBeSet = "DISABLE"
                present_ble_str = "ENABLE"
            else:
                Enable_ble = 1;
                #storing states as string for logging purpose
                toBeSet = "ENABLE"
                present_ble_str = "DISABLE"

	    present_ble = int(details)

            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the value of BLEHAL_GetStatus";
            print "EXPECTED RESULT 1: Should retrieve the BLEHAL_GetStatus successfully";
            print "ACTUAL RESULT 1: BLE_Enable state is %s" %present_ble_str
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            #Set the result status of execution

            #------------- Set BLE Enable ----------------
            tdkTestObj = obj.createTestStep("BLEHAL_Enable");
            tdkTestObj.addParameter("enable", Enable_ble);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set ble_enable to ", toBeSet;
                print "EXPECTED RESULT 2: Should set ble_enable using BLEHAL_Enable()";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;

	        #----------- Cross verify ble enable --------------------
	        tdkTestObj = obj.createTestStep('BLEHAL_GetStatus');
	        expectedresult="SUCCESS";
	        tdkTestObj.executeTestCase(expectedresult);
	        actualresult = tdkTestObj.getResult();
	        details = tdkTestObj.getResultDetails();
	        if expectedresult in actualresult and details and (details == "1" or details == "2" or  details == "3"):
                    if details == "1":
                        #storing states as string for logging purpose
                        new_ble_str = "ENABLE"
                    else:
                        #storing states as string for logging purpose
                        new_ble_str = "DISABLE"
                    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 3: Retrieve the value of BLEHAL_GetStatus";
		    print "EXPECTED RESULT 3: Should retrieve the value of BLEHAL_GetStatus successfully";
		    print "ACTUAL RESULT 3: BLEHAL_GetStatus value is %s" %new_ble_str;
		    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    if int(details) == Enable_ble:
		        print "TEST STEP 4: Cross verifying values of GET and SET";
		        print "EXPECTED RESULT 4: GET and SET values should be same";
		        print "ACTUAL RESULT 3: GET and SET value is %s" %new_ble_str
		        print "[TEST EXECUTION RESULT] : %s" %actualresult;

                        #--------- Re-setting the value -----------
                        tdkTestObj = obj.createTestStep("BLEHAL_Enable");
                        tdkTestObj.addParameter("enable", present_ble);
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult and details:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 5: Revert the ble_enable state to ", present_ble_str;
                            print "EXPECTED RESULT 5: Should Revert the ble_enable successfully";
                            print "ACTUAL RESULT 5: %s" %details;
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Revert the ble_enable state";
                            print "EXPECTED RESULT 5: Should Revert the ble_enable successfully";
                            print "ACTUAL RESULT 5: %s" %details;
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
		        print "TEST STEP 4: Cross verifying values of GET and SET";
		        print "EXPECTED RESULT 4: GET and SET values should be same";
		        print "ACTUAL RESULT 4: %s" %details;
		        print "[TEST EXECUTION RESULT] : %s" %actualresult;
		        print "GET and SET values are not same";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 3: Retrieve the value of BLEHAL_GetStatus";
		    print "EXPECTED RESULT 3: Should retrieve the value of BLEHAL_GetStatus successfully";
		    print "ACTUAL RESULT 3: %s" %details;
		    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set ble_enable using BLEHAL_Enable() to ", toBeSet;
                print "EXPECTED RESULT 2: Should Set ble_enable using BLEHAL_Enable successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Retrieve the value of BLEHAL_GetStatus";
                print "EXPECTED RESULT 1: Should Retrieve the value of BLEHAL_GetStatus successfully";
                print "ACTUAL RESULT 1: %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE"
        obj.unloadModule("blehal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
