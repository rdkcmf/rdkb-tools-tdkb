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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_CMHAL_SetUSChannelId</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_SetUSChannelId</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To not set the upstream Channel ID using the api docsis_SetUSChannelId()</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_CMHAL_57</test_case_id>
    <test_objective>To not set the upstream Channel ID using the api docsis_SetUSChannelId()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_SetUSChannelId()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load CMHAL module
2. Get and save US Channel ID
3. Set the US channel ID
4. Validate the set function using get and get value should be not be equal to set value and should be equal to initial get value
5. unload CMHAL module</automation_approch>
    <except_output>The api should set the given USChannelID</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_SetUSChannelId</test_script>
    <skipped>No</skipped>
    <release_version>M62</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_CMHAL_SetUSChannelId');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
    tdkTestObj.addParameter("paramName","USChannelId");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    USChannelID = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the initial US Channel ID";
        print "EXPECTED RESULT 1: Should get the initial US Channel ID successfully";
        print "ACTUAL RESULT 1: Initial US Channel ID is %s" %USChannelID;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	setValue = int(USChannelID) + 1;
	print "The US Channel ID to set is %d" %setValue;

        tdkTestObj = obj.createTestStep("CMHAL_SetUSChannelId");
        tdkTestObj.addParameter("Value",setValue);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the upstream channel Id";
            print "EXPECTED RESULT 2: Should set the upstream channel Id";
            print "ACTUAL RESULT 2:  ",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #Validation of set function using get
	    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
    	    tdkTestObj.addParameter("paramName","USChannelId");
    	    expectedresult="SUCCESS";
    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    USChannelID1 = tdkTestObj.getResultDetails();

    	    if expectedresult in actualresult and setValue != int(USChannelID1) and int(USChannelID1) == int(USChannelID):
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 3: Get the US Channel ID and it should be equal to the set value";
    	        print "EXPECTED RESULT 3: Should get the US Channel ID successfully and it should be equal to the set value";
    	        print "ACTUAL RESULT 3: US Channel ID is %s" %USChannelID1;
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the US Channel ID";
                print "EXPECTED RESULT 3: Should get the US Channel ID successfully";
                print "ACTUAL RESULT 3: US Channel ID is %s" %USChannelID1;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	    #revert the value of US Channel Id
	    tdkTestObj = obj.createTestStep("CMHAL_SetUSChannelId");
            tdkTestObj.addParameter("Value",int(USChannelID));
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Revert the value of upstream channel Id";
                print "EXPECTED RESULT : Should set the upstream channel Id";
                print "ACTUAL RESULT :  ",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Revert the value of upstream channel Id";
                print "EXPECTED RESULT : Should set the upstream channel Id";
                print "ACTUAL RESULT :  ",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the upstream channel Id";
            print "EXPECTED RESULT 2: Should set the upstream channel Id";
            print "ACTUAL RESULT 2:  ",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the US Channel ID";
        print "EXPECTED RESULT 1: Should get the US Channel ID successfully";
        print "ACTUAL RESULT 1: US Channel ID is %s" %USChannelID;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
