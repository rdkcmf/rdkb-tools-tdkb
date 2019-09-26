##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzSetInvalidRadioChannel</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set an invalid value to RadioChannel and check whether it is failing or not</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types/>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_25</test_case_id>
    <test_objective>To set an invalid value to RadioChannel and check whether it is failing or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioChannel()</api_or_interface_used>
    <input_parameters>methodName: setRadioChannel
radioIndex :1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamULongValue" to set the invalid value to radio channel for 2.4GHz
3.Check if it is failing or not 
4. If not, return failure
5.Unload wifihal module</automation_approch>
    <except_output>The invalid value must not set to radio channel</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetInvalidRadioChannel</test_script>
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
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetInvalidRadioChannel');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
    #Giving the method name to invoke the api for getting Radio Channel. ie,wifi_getRadioChannel()
    tdkTestObj.addParameter("methodName","getRadioChannel");
    #Radio index is 1 or 5 for 2.4GHz and 2 or 6 for 5GHz
    tdkTestObj.addParameter("radioIndex",1);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    CurrentChannel= details.split(":")[1];
    if expectedresult in actualresult:
	#Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Radio channel for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the Radio channel for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %CurrentChannel;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        #Giving the method name to invoke the api for getting possible channels. ie,wifi_getRadioPossibleChannels()
        tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",0);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        PossibleChannels = details.split(":")[1];
        if expectedresult in actualresult:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Possible radio channels for 2.4GHz";
            print "EXPECTED RESULT 2: Should get the Possible radio channels for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    if "-" in PossibleChannels:
		MaxValue = PossibleChannels.split("-")[1]; 
	    elif "," in PossibleChannels:
		MaxValue = PossibleChannels.split(",")[1];
	    #select a channel number which is invalid
	    Channel = int(MaxValue)+1;
	    print "The invalid channel number to set is :" ,Channel;
	    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
    	    #Giving the method name to invoke the api for getting Radio Channel. ie,wifi_getRadioChannel()
    	    tdkTestObj.addParameter("methodName","setRadioChannel");
    	    #Radio index is 1 or 5 for 2.4GHz and 2 or 6 for 5GHz
    	    tdkTestObj.addParameter("radioIndex",1);
	    tdkTestObj.addParameter("param",Channel);
    	    expectedresult="FAILURE";
    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    details = tdkTestObj.getResultDetails();
    	    if expectedresult in actualresult:
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 3: Set invalid value to Radio channel for 2.4GHz";
    	        print "EXPECTED RESULT 3: Should not set the invalid value to Radio channel for 2.4GHz";
    	        print "ACTUAL RESULT 3: %s" %details;
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Set invalid value to Radio channel for 2.4GHz";
                print "EXPECTED RESULT 3: Should not set the invalid value to Radio channel for 2.4GHz";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	    #set the default value to radio channel
	    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
            #Giving the method name to invoke the api for getting Radio Channel. ie,wifi_getRadioChannel()
            tdkTestObj.addParameter("methodName","setRadioChannel");
            #Radio index is 1 or 5 for 2.4GHz and 2 or 6 for 5GHz
            tdkTestObj.addParameter("radioIndex",1);
            tdkTestObj.addParameter("param",int(CurrentChannel));
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Set default value to Radio channel for 2.4GHz";
                print "EXPECTED RESULT : Should set the default value to Radio channel for 2.4GHz";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Set default value to Radio channel for 2.4GHz";
                print "EXPECTED RESULT : Should set the default value to Radio channel for 2.4GHz";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Possible radio channels for 2.4GHz";
            print "EXPECTED RESULT 2: Should get the Possible radio channels for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %PossibleChannels;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Radio channel for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the Radio channel for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %CurrentChannel;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";	
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
