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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzSetApBridgeInfo</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetApBridgeInfo</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the ApBridgeInfo for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_206</test_case_id>
    <test_objective>To set and get the ApBridgeInfo for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBridgeInfo()
wifi_setApBridgeInfo()</api_or_interface_used>
    <input_parameters>methodName : getApBridgeInfo
methodName : setApBridgeInfo
radioIndex : 0
bridgeName : "newBranch0"
IP : "1.1.1.1"
subnet : "255.255.255.1"</input_parameters>
    <automation_approch>1. Load wifihal module 
2. Using  WIFIHAL_GetOrSetApBridgeInfo invoke wifi_getApBridgeInfo()
3. Using WIFIHAL_GetOrSetApBridgeInfo 
 invoke wifi_setApBridgeInfo and set a valid bridge info
4. Invoke wifi_getApBridgeInfo() to get the previously set value. 
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the ApBridgeInfo back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of ApBridgeInfo should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApBridgeInfo</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApBridgeInfo');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetApBridgeInfo');
    #Giving the method name to invoke the api wifi_getApBridgeInfo()
    tdkTestObj.addParameter("methodName","getApBridgeInfo");
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
	tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the ApBridgeInfo for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the ApBridgeInfo for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
	bridgeName = details.split(":")[1].split(",")[0].split("=")[1];
	IP = details.split(":")[1].split(",")[1].split("=")[1];
	subnet = details.split(":")[1].split(",")[2].split("=")[1];

        #Prmitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetApBridgeInfo');
        #Giving the method name to invoke the api wifi_setApBridgeInfo()
        tdkTestObj.addParameter("methodName","setApBridgeInfo");
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",0);
        tdkTestObj.addParameter("bridgeName","newBranch0");
        tdkTestObj.addParameter("IP","1.1.1.1");
        tdkTestObj.addParameter("subnet","255.255.255.1");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the ApBridgeInfo for 2.4GHz";
            print "EXPECTED RESULT 2: Should set the ApBridgeInfo for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #Prmitive test case which associated to this Script
	    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetApBridgeInfo');
    	    #Giving the method name to invoke the api wifi_getApBridgeInfo()
	    tdkTestObj.addParameter("methodName","getApBridgeInfo");
	    #Radio index is 0 for 2.4GHz and 1 for 5GHz
	    tdkTestObj.addParameter("radioIndex",0);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
	    if expectedresult in actualresult:
        	tdkTestObj.setResultStatus("SUCCESS");
	        print "TEST STEP 3: Get the previously set ApBridgeInfo for 2.4GHz";
	        print "EXPECTED RESULT 3: Should get the previously set ApBridgeInfo for 2.4GHz";
	        print "ACTUAL RESULT 3: %s" %details;
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : SUCCESS";	
	    else:
        	tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 3: Get the previously set ApBridgeInfo for 2.4GHz";
	        print "EXPECTED RESULT 3: Should get the previously set ApBridgeInfo for 2.4GHz";
	        print "ACTUAL RESULT 3: %s" %details;
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : FAILURE";	

            #Prmitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetApBridgeInfo');
    	    #Giving the method name to invoke the api wifi_setApBridgeInfo()
            tdkTestObj.addParameter("methodName","setApBridgeInfo");
            #Radio index is 0 for 2.4GHz and 1 for 5GHz
            tdkTestObj.addParameter("radioIndex",0);
            tdkTestObj.addParameter("bridgeName",bridgeName);
            tdkTestObj.addParameter("IP",IP);
            tdkTestObj.addParameter("subnet",subnet);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
		tdkTestObj.setResultStatus("SUCCESS");
		print "Successfully reverted to initial values"
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "Unable to revert to initial value"
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the ApBridgeInfo for 2.4GHz";
            print "EXPECTED RESULT 2: Should set the ApBridgeInfo for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the ApBridgeInfo for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the ApBridgeInfo for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
	
