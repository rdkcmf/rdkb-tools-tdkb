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
  <name>TS_CMHAL_ClearDocsisEventLog</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_ClearDocsisEventLog</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To clear the docsis event logs using docsis_ClearDocsisEventLog()</synopsis>
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
    <test_case_id>TC_CMHAL_53</test_case_id>
    <test_objective>To clear the docsis event logs using docsis_ClearDocsisEventLog()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_ClearDocsisEventLog()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  cmhal module
2. From script invoke CMHAL_ClearDocsisEventLog()
3. Get the number of docsis event logs
4. If it is greater than zero clear it
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>The docsis event log items should be cleared</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_ClearDocsisEventLog</test_script>
    <skipped>No</skipped>
    <release_version>M62</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_ClearDocsisEventLog');
obj1.configureTestCase(ip,port,'TS_CMHAL_ClearDocsisEventLog');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_CableModem.DocsisLogNumberOfEntries");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    numofDocsisLog = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the number of docsis logs";
        print "EXPECTED RESULT 1: Should get the number of docsis logs";
        print "ACTUAL RESULT 1: number of docsis logs is %s" %numofDocsisLog;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	if int(numofDocsisLog) > 0:

    	    #Script to load the configuration file of the component
    	    tdkTestObj = obj.createTestStep("CMHAL_ClearDocsisEventLog");
    	    expectedresult="SUCCESS";
    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    details = tdkTestObj.getResultDetails();


    	    if expectedresult in actualresult:
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 2: Clear the Docsis logs";
    	        print "EXPECTED RESULT 2: Should clear the Docsis successfully";
    	        print "ACTUAL RESULT 2:  %s" %details;
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";

		time.sleep(30);
		#Validate the clear function using get
		tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    		tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_CableModem.DocsisLogNumberOfEntries");
    		expectedresult="SUCCESS";

    		#Execute the test case in DUT
    		tdkTestObj.executeTestCase(expectedresult);
    		actualresult = tdkTestObj.getResult();
    		numofDocsisLog1 = tdkTestObj.getResultDetails();

    		if expectedresult in actualresult and int(numofDocsisLog1)== 0:
    		    #Set the result status of execution
    		    tdkTestObj.setResultStatus("SUCCESS");
    		    print "TEST STEP 3: Get the number of docsis logs";
    		    print "EXPECTED RESULT 3: Should get the number of docsis logs";
    		    print "ACTUAL RESULT 3: number of docsis logs is %s" %numofDocsisLog1;
    		    #Get the result of execution
    		    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
		    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get the number of docsis logs";
                    print "EXPECTED RESULT 3: Should get the number of docsis logs";
                    print "ACTUAL RESULT 3: number of docsis logs is %s" %numofDocsisLog1;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
    	    else:
    	        tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 2: Clear teh Docsis logs";
                print "EXPECTED RESULT 2: Should clear the Docsis successfully";
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    print "Number of Docsis Log entries is already zero";
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of docsis logs";
        print "EXPECTED RESULT 1: Should get the number of docsis logs";
        print "ACTUAL RESULT 1: number of docsis logs is %s" %numofDocsisLog;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("cmhal");
    obj1.unloadModule("tdkbtr181");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
