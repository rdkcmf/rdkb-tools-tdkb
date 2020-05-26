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
  <version>13</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ethsw_stub_hal_Set_EthWanEnable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ethsw_stub_hal_Set_EthWanEnable</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set ethwan enable status using CcspHalExtSw_setEthWanEnable and validate the operation using CcspHalExtSw_getEthWanEnable</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_26</test_case_id>
    <test_objective>Set ethwan enable status using CcspHalExtSw_setEthWanEnable and validate the operation using CcspHalExtSw_getEthWanEnable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Device should be in ethwan mode
2. Ccsp Components  should be in a running state of DUT
3.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalExtSw_setEthWanEnable
CcspHalExtSw_getEthWanEnable</api_or_interface_used>
    <input_parameters>CcspHalExtSw_setEthWanEnable() - enable</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. Get the EthWan mode using CcspHalExtSw_getEthWanEnable() and save it
3. Set ethwan enable as the above saved value using CcspHalExtSw_setEthWanEnable(). (we are not using the set api for toggling ethwan enable state. Because if ethwan state is disabled, DUT's connectivity with TDK test manager will be lost)
4. Get the ethwan enable state and check if it is same as the set state
5. Unload halethsw module</automation_approch>
    <expected_output>Should successfully set ethwan enable state using CcspHalExtSw_setEthWanEnable</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Set_EthWanEnable</test_script>
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
obj = tdklib.TDKScriptingLibrary("halethsw","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Set_EthWanEnable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        tdkTestObj = obj.createTestStep('ethsw_stub_hal_Get_EthWanEnable');
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details and (details == "0" or details == "1"):
           
            #As part of set api validation, ethwan_enable state is NOT being toggled, as ETHWAN disable will cause the TDK test manager to lose connectivity with the test device. Hence using the current ethwanenable state as set's input 
            if details == "1":
                Enable_ethwan = 1;
                Enable_ethwan_str = "ENABLE"
            else:
                Enable_ethwan = 0;
                Enable_ethwan_str = "DISABLE"

            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the value of ethsw_stub_hal_Get_EthWanEnable";
            print "EXPECTED RESULT 1: Should retrieve the ethsw_stub_hal_Get_EthWanEnable successfully";
            print "ACTUAL RESULT 1: EthWanEnable state is %s" %Enable_ethwan_str;
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            #------------- Set ETHWAN Enable ----------------
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Set_EthWanEnable");
            tdkTestObj.addParameter("enable", Enable_ethwan);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set ethwan enable state using ethsw_stub_hal_Set_EthWanEnable";
                print "EXPECTED RESULT 2: Should set ethwan enable state as: ", Enable_ethwan_str;
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;

	        #----------- Cross verify ethwan enable --------------------
	        tdkTestObj = obj.createTestStep('ethsw_stub_hal_Get_EthWanEnable');
	        expectedresult="SUCCESS";
	        tdkTestObj.executeTestCase(expectedresult);
	        actualresult = tdkTestObj.getResult();
	        details = tdkTestObj.getResultDetails();

	        if expectedresult in actualresult and details and (details == "0" or details == "1"):
                    if details == "1":
                        Enable_ethwan_new = 1;
                        Enable_ethwan_new_str = "ENABLE"
                    else:
                        Enable_ethwan_new = 0;
                        Enable_ethwan_new_str = "DISABLE"
                    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 3: Retrieve the value of ethsw_stub_hal_Get_EthWanEnable";
		    print "EXPECTED RESULT 3: Should retrieve the value of ethsw_stub_hal_Get_EthWanEnable successfully as: ", Enable_ethwan_str;
		    print "ACTUAL RESULT 3: EthWanEnable state is %s" %Enable_ethwan_new_str
		    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    if Enable_ethwan_new == Enable_ethwan:
		        print "TEST STEP 4: Cross verifying values of GET and SET";
		        print "EXPECTED RESULT 4: GET and SET values should be ",Enable_ethwan_str;
		        print "ACTUAL RESULT 3: GET and SET value is %s" %Enable_ethwan_new_str;
		        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
		        print "TEST STEP 4: Cross verifying values of GET and SET";
		        print "EXPECTED RESULT 4: GET and SET values should be :", Enable_ethwan_str;
		        print "ACTUAL RESULT 4: %s" %details;
		        print "[TEST EXECUTION RESULT] : %s" %actualresult;
		        print "GET and SET values are not same";

               #Not adding the steps to revert ethwan state to original value, as we are not toggling its value in this script
                else:
                    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 3: Retrieve the value of ethsw_stub_hal_Get_EthWanEnable";
		    print "EXPECTED RESULT 3: Should retrieve the value of ethsw_stub_hal_Get_EthWanEnable successfully as: ", Enable_ethwan_str;
		    print "ACTUAL RESULT 3: %s" %details;
		    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set ethwan enable using ethsw_stub_hal_Set_EthWanEnable";
                print "EXPECTED RESULT 2: Should set ethwan enable state as: ", Enable_ethwan_str;
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult ; 
        else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Retrieve the value of ethsw_stub_hal_Get_EthWanEnable";
                print "EXPECTED RESULT 1: Should Retrieve the value of ethsw_stub_hal_Get_EthWanEnable successfully";
                print "ACTUAL RESULT 1: %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE" 
        obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
