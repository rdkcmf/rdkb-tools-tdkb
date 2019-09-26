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
  <name>TS_CMHAL_SetStartFreq</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_SetStartFreq</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the StartFreq using the api docsis_SetStartFreq()</synopsis>
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
    <test_case_id>TC_CMHAL_56</test_case_id>
    <test_objective>To set the StartFreq using the api docsis_SetStartFreq()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_SetStartFreq()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load CMHAL Module
2. Get and save the Start frequency
3. Set the start frequnecy
4. Validate the set function using get
5. Unload CMHAL module</automation_approch>
    <except_output>The api should set the given Start Frequency</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_SetStartFreq</test_script>
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
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_SetStartFreq');
obj1.configureTestCase(ip,port,'TS_CMHAL_SetStartFreq');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_CableModem.StartDSFrequency");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    StartFreq = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the start frequency";
        print "EXPECTED RESULT 1: Should get the start frequency";
        print "ACTUAL RESULT 1: Start frequency is %s" %StartFreq;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	setValue = int(StartFreq) + 1000;
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("CMHAL_SetStartFreq");
        tdkTestObj.addParameter("Value",setValue);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the Start frequency";
            print "EXPECTED RESULT 2: Should set the start frequency";
            print "ACTUAL RESULT 2:  ",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #validate the set function using get
	    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    	    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_CableModem.StartDSFrequency");
    	    expectedresult="SUCCESS";

    	    #Execute the test case in DUT
    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    StartFreq1 = tdkTestObj.getResultDetails();

    	    if expectedresult in actualresult and int(StartFreq1) == setValue:
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 3: Get the start frequency";
    	        print "EXPECTED RESULT 3: Should get the start frequency";
    	        print "ACTUAL RESULT 3: Start frequency is %s" %StartFreq1;
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the start frequency";
                print "EXPECTED RESULT 3: Should get the start frequency";
                print "ACTUAL RESULT 3: Start frequency is %s" %StartFreq1;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

	    #Revert the start freq
	    tdkTestObj = obj.createTestStep("CMHAL_SetStartFreq");
            tdkTestObj.addParameter("Value",int(StartFreq));
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Revert the value of Start frequency";
                print "EXPECTED RESULT : Should revert the start frequency";
                print "ACTUAL RESULT :  ",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Revert the value of Start frequency";
                print "EXPECTED RESULT : Should revert the start frequency";
                print "ACTUAL RESULT :  ",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the Start frequency";
            print "EXPECTED RESULT 2: Should set the start frequency";
            print "ACTUAL RESULT 2:  ",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the start frequency";
        print "EXPECTED RESULT 1: Should get the start frequency";
        print "ACTUAL RESULT 1: Start frequency is %s" %StartFreq;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("cmhal");
    obj1.unloadModule("tdkbtr181");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
