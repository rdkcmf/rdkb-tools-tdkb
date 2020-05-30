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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_MoCAHAL_SetIfConfig</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MoCAHAL_SetIfConfig</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the MoCA HAL API moca_SetIfConfig</synopsis>
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
    <test_case_id>TC_MoCAHAL_16</test_case_id>
    <test_objective>To validate the MoCA HAL API moca_setIfConfig</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>moca_GetIfConfig, moca_SetIfConfig</api_or_interface_used>
    <input_parameters>privacyEnable - To Enable/Disable the Privacy settings
keyPassphrase - Keypassphrase to be set
autoPowerRate - Auto Power Control Rate value
autoPowerEnable - Auto Power Control Enable value</input_parameters>
    <automation_approch>1.Load the module
2.Using MoCAHAL_GetIfConfig, call moca_GetIfConfig MoCA API to get the configuration values and store it
3.Using MoCAHAL_SetIfConfig , call moca_SetIfConfig with updated parameters (privacyEnable,keyPassphrase,autoPowerRate and autoPowerEnable)
4.Using MoCAHAL_GetIfConfig, call moca_GetIfConfig API and compare the values (privacyEnable,autoPowerRate and autoPowerEnable) with previous set operation, Keypassspharse cannot be compared since its encrypted
5.Unload the Module</automation_approch>
    <expected_output>should be able to set the moca_SetIfConfig HAL with updated parameters</expected_output>
    <priority>High</priority>
    <test_stub_interface>mocahal</test_stub_interface>
    <test_script>TS_MoCAHAL_SetIfConfig</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mocahal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MoCAHAL_SetIfConfig');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MoCAHAL_GetIfConfig");
    tdkTestObj.addParameter("ifIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    conf = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the MoCA Configuration Parameters"
        print "EXPECTED RESULT 1: Should get the MoCA Configuration Parameters";
        print "ACTUAL RESULT 1: The MoCA Configuration is %s" %conf;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#store the configuration values
	privacyEnable= conf.split("PrivacyEnabledSetting=")[1].split(",")[0]
        keyPassphrase = conf.split("KeyPassphrase=")[1].split(",")[0]
        autoPowerRate = conf.split("AutoPowerControlPhyRate=")[1].split(",")[0]
        autoPowerEnable = conf.split("AutoPowerControlEnable=")[1].split(",")[0]

	#Values to be changed on set call
	privacyEnable_set = 1 - int(privacyEnable)
        keyPassphrase_set = "0987654321098"
        autoPowerRate_set = int(autoPowerRate)+10
	autoPowerEnable_set = 1 - int(autoPowerEnable)
	print "PrivacyEnable_set is %s"%privacyEnable_set
	print "KeyPassPhrase_set is %s"%keyPassphrase_set
	print "AutoPowerRate_set is %s"%autoPowerRate_set
	print "AutoPowerEnable_set is %s"%autoPowerEnable_set

	#Set call with updated values
	tdkTestObj = obj.createTestStep("MoCAHAL_SetIfConfig");
	tdkTestObj.addParameter("privacyEnable",int(privacyEnable_set));
	tdkTestObj.addParameter("keyPassphrase",keyPassphrase_set);
	tdkTestObj.addParameter("autoPowerRate",int(autoPowerRate_set));
	tdkTestObj.addParameter("autoPowerEnable",int(autoPowerEnable_set));
	tdkTestObj.addParameter("ifIndex",0);
	expectedresult="SUCCESS";
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();

	if expectedresult in actualresult:
            #Set the result status of execution
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: Set the MoCA Configuration Parameters"
	    print "EXPECTED RESULT 2: Should set the MoCA Configuration Parameters";
            print "ACTUAL RESULT 2: The MoCA set coniguration was success %s" %details;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";

            #Verify the set using get function
	    tdkTestObj = obj.createTestStep("MoCAHAL_GetIfConfig");
	    tdkTestObj.addParameter("ifIndex",0);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    conf_afterset = tdkTestObj.getResultDetails();

	    privacyEnable_afterset = conf_afterset.split("PrivacyEnabledSetting=")[1].split(",")[0]
	    autoPowerRate_afterset = conf_afterset.split("AutoPowerControlPhyRate=")[1].split(",")[0]
	    autoPowerEnable_afterset = conf_afterset.split("AutoPowerControlEnable=")[1].split(",")[0]

            #keyPassPharse can be set with any string value of length within 16, But keyPassphrase in get function will always return encrypted value (888888888), so keypassphrase is not being validated in get method
	    if expectedresult in actualresult and int(privacyEnable_afterset) == int(privacyEnable_set) and int(autoPowerRate_afterset) == int(autoPowerRate_set) and int(autoPowerEnable_afterset) == int(autoPowerEnable_set):
		#Set the result status of execution
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP 3: Compare the configuration parameters with set values"
		print "EXPECTED RESULT 3: Configuration parameters should match with set vlues";
		print "ACTUAL RESULT 3: Configurations are matching %s" %conf_afterset;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 3: Compare the configuration parameters with set values"
		print "EXPECTED RESULT 3: Configuration parameters should match with set vlues";
		print "ACTUAL RESULT 3: Configurations are NOT matching %s" %conf_afterset;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";

	    #Revert the values
	    tdkTestObj = obj.createTestStep("MoCAHAL_SetIfConfig");
	    tdkTestObj.addParameter("privacyEnable",int(privacyEnable));
	    tdkTestObj.addParameter("keyPassphrase",keyPassphrase);
	    tdkTestObj.addParameter("autoPowerRate",int(autoPowerRate));
	    tdkTestObj.addParameter("autoPowerEnable",int(autoPowerEnable));
	    tdkTestObj.addParameter("ifIndex",0);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();

	    if expectedresult in actualresult:
                #Set the result status of execution
	        tdkTestObj.setResultStatus("SUCCESS");
	        print "TEST STEP 4: Set the MoCA Configuration Parameters"
	        print "EXPECTED RESULT 4: Should set the MoCA Configuration Parameters";
                print "ACTUAL RESULT 4: The MoCA set configuration was success for Revert operation %s" %details;
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : SUCCESS";

            else:
	        #Set the result status of execution
	        tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 4: Set the MoCA Configuration Parameters"
	        print "EXPECTED RESULT 4: Should set the MoCA Configuration Parameters";
	        print "ACTUAL RESULT 4: Failed to revert to original value %s" %details;
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : FAILURE";

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the MoCA Configuration Parameters"
            print "EXPECTED RESULT 2: Should set the MoCA Configuration Parameters";
            print "ACTUAL RESULT 2: Failed to MoCA set coniguration Values %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the MoCA Configuration Parameters"
        print "EXPECTED RESULT 1: Should get the MoCA Configuration Parameters";
        print "ACTUAL RESULT 1: %s" %conf;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("mocahal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed"
