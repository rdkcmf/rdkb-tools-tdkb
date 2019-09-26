##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_MOCA_SetKeyPassphrase_LessThan_12Chars</name>
  <primitive_test_id/>
  <primitive_test_name>Mocastub_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the KeyPassphrase less than 12 characters. Test should fail since the password is expected to be more than 12 character long.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_MOCA_06</test_case_id>
    <test_objective>To set the KeyPassphrase less than 12 characters. Test should fail since the password is expected to be more than 12 character long.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>XB3,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Mocastub_Set, Mocastub_Get</api_or_interface_used>
    <input_parameters>Device.MoCA.Interface.1.KeyPassphrase</input_parameters>
    <automation_approch>1. Load MOCA modules
2. From script invoke Mocastub_Get to get the KeyPassphrase
3. Invoke Mocastub_Set to set the password of less than 12 character
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from Moca stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_MOCA_SetKeyPassphrase_LessThan_12Chars</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("moca","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MOCA_SetKeyPassphrase_LessThan_12Chars');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('Mocastub_Get');
    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj.getResult();
    Moca_interface_status= tdkTestObj.getResultDetails();

    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.PrivacyEnabledSetting");

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult2 = tdkTestObj.getResult();
    privacy_setting_status= tdkTestObj.getResultDetails();

    if expectedresult in (actualresult1,actualresult2):
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the status of privacy settings and moca interface";
        print "EXPECTED RESULT 1: Should get the status of privacy settings and moca interface";
        print "ACTUAL RESULT 1: The status of privacy settings and moca interface are %s and %s" %(privacy_setting_status,Moca_interface_status);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
	
	tdkTestObj = obj.createTestStep('Mocastub_Set');
        tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.Enable");
        tdkTestObj.addParameter("ParamValue","true")
        tdkTestObj.addParameter("Type","bool");

	#Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details= tdkTestObj.getResultDetails();

	if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Enable the moca interface";
            print "EXPECTED RESULT 2: Should enable the moca interface";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.PrivacyEnabledSetting");
            tdkTestObj.addParameter("ParamValue","true")
            tdkTestObj.addParameter("Type","bool");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details= tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Enable the privacy settings";
                print "EXPECTED RESULT 3: Should enable the privacy settings";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

    		tdkTestObj = obj.createTestStep('Mocastub_SetKeypassphrase');
    		tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.KeyPassphrase");
    		tdkTestObj.addParameter("ParamValue","12345");
    		tdkTestObj.addParameter("Type","string");
    		expectedresult="FAILURE";

    		#Execute the test case in DUT
    		tdkTestObj.executeTestCase(expectedresult);
    		actualresult = tdkTestObj.getResult();
    		details= tdkTestObj.getResultDetails();
    		if expectedresult in actualresult:
    		    #Set the result status of execution
    		    tdkTestObj.setResultStatus("SUCCESS");
    		    print "TEST STEP 5: Set the KeyPassphrase";
    		    print "EXPECTED RESULT 5: Should not set a KeyPassphrase less than 12 character long";
    		    print "ACTUAL RESULT 5: %s" %details;
    		    #Get the result of execution
    		    print "[TEST EXECUTION RESULT] : SUCCESS";
    		else:
    		    #Set the result status of execution
    		    tdkTestObj.setResultStatus("FAILURE");
    		    print "TEST STEP 5: Set the KeyPassphrase";
    		    print "EXPECTED RESULT 5: Should not set a KeyPassphrase less than 12 character long";
    		    print "ACTUAL RESULT 5:%s" %details;
    		    #Get the result of execution
    		    print "[TEST EXECUTION RESULT] : FAILURE";
    		#setting the default password
		tdkTestObj = obj.createTestStep('Mocastub_SetKeypassphrase');
        	tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.KeyPassphrase");
        	tdkTestObj.addParameter("ParamValue","99999999988888888");
        	tdkTestObj.addParameter("Type","string");
        	expectedresult="SUCCESS";

        	#Execute the test case in DUT
        	tdkTestObj.executeTestCase(expectedresult);
        	actualresult = tdkTestObj.getResult();
        	details= tdkTestObj.getResultDetails();
        	if expectedresult in actualresult:
		    #Set the result status of execution
        	    tdkTestObj.setResultStatus("SUCCESS");
        	    print "TEST STEP : Set the KeyPassphrase";
        	    print "EXPECTED RESULT : Should set the default KeyPassphrase";
        	    print "ACTUAL RESULT : %s" %details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : SUCCESS";
        	else:
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("FAILURE");
        	    print "TEST STEP : Set the KeyPassphrase";
        	    print "EXPECTED RESULT : Should set the default KeyPassphrase";
        	    print "ACTUAL RESULT : %s" %details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Enable the privacy settings";
                print "EXPECTED RESULT 3: Should enable the privacy settings";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Enable the moca interface";
            print "EXPECTED RESULT 2: Should enable the moca interface";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
	#Set default values
	tdkTestObj = obj.createTestStep('Mocastub_Set');
        tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.Enable");
        tdkTestObj.addParameter("ParamValue",Moca_interface_status)
        tdkTestObj.addParameter("Type","bool");
	expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();
        details= tdkTestObj.getResultDetails();

        tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.PrivacyEnabledSetting");
        tdkTestObj.addParameter("ParamValue",privacy_setting_status)
        tdkTestObj.addParameter("Type","bool");

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult2 = tdkTestObj.getResult();
        details= tdkTestObj.getResultDetails();

        if expectedresult in (actualresult1,actualresult2):
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Set the previous values";
            print "EXPECTED RESULT : Should set previous values";
            print "ACTUAL RESULT : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Set the previous values";
            print "EXPECTED RESULT : Should set previous values";
            print "ACTUAL RESULT : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the status of privacy settings and moca interface";
        print "EXPECTED RESULT 1: Should get the status of privacy settings and moca interface";
        print "ACTUAL RESULT 1: The status of privacy settings and moca interface are %s and %s" %(privacy_setting_status,Moca_interface_status);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("moca");
else:
        print "Failed to load moca module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
