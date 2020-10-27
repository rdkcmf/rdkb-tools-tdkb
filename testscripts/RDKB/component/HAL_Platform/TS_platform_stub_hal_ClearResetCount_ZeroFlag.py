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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>4</version>
  <name>TS_platform_stub_hal_ClearResetCount_ZeroFlag</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_ClearResetCount</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify that the HAL API platform_hal_ClearResetCount() does not clear the reset count when invoked with parameter 0..</synopsis>
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
    <test_case_id>TC_HAL_Platform_71</test_case_id>
    <test_objective>To verify that the HAL API platform_hal_ClearResetCount() does not clear the reset count when invoked with parameter 0..</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_ClearResetCount</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  platform_hal module.
2. Get the current factory reset count using platform_hal_GetFactoryResetCount() api and save it
3. Invoke platform_hal_ClearResetCount() api with input flag as 0, so that reset count doesn't get cleared
4. Get the current factory reset count again using platform_hal_GetFactoryResetCount() api
5. Check if factory reset count before and after invoking platform_hal_ClearResetCount() is the same
6. Unload platform_hal module</automation_approch>
    <expected_output>platform_hal_ClearResetCount() should not clear the factory reset count when invoked with input flag 0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>platformhal</test_stub_interface>
    <test_script>TS_platform_stub_hal_ClearResetCount_ZeroFlag</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_ClearResetCount_ZeroFlag');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
	obj.setLoadModuleStatus("SUCCESS");
	#Get the reset count
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetFactoryResetCount");
	expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        resetCount = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and int (resetCount) >= 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the Platform_GetFactoryResetCount";
            print "EXPECTED RESULT 1: Should retrieve the Platform_GetFactoryResetCount ";
            print "ACTUAL RESULT 1: %s" %actualresult;
            print "Factory reset count: %s" %resetCount;

	    if int (resetCount) > 0:
        	tdkTestObj = obj.createTestStep("platform_stub_hal_ClearResetCount");
		tdkTestObj.addParameter("index",0);
        	expectedresult = "SUCCESS";
        	tdkTestObj.executeTestCase(expectedresult);
        	actualresult = tdkTestObj.getResult();

        	if expectedresult in actualresult:
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("SUCCESS");
        	    details = tdkTestObj.getResultDetails();
        	    print "TEST STEP 2: Invoke platform_hal_ClearResetCount() with 0 as parameter";
        	    print "EXPECTED RESULT 2: Should successfully invoke platform_hal_ClearResetCount()";
        	    print "ACTUAL RESULT 2: Invoked platform_hal_ClearResetCount() successfully"
        	    print "[TEST EXECUTION RESULT] : %s" %actualresult;

	    	    #Get the reset count
	    	    tdkTestObj = obj.createTestStep("platform_stub_hal_GetFactoryResetCount");
            	    tdkTestObj.executeTestCase(expectedresult);
            	    actualresult = tdkTestObj.getResult();
            	    details = tdkTestObj.getResultDetails();

            	    if expectedresult in actualresult and int (details) == int (resetCount):
            	        #Set the result status of execution
            	        tdkTestObj.setResultStatus("SUCCESS");
            	        print "TEST STEP 3: Retrieve the Platform_GetFactoryResetCount and check the new reset count";
            	        print "EXPECTED RESULT 3: FactoryResetCount should be same as the initial value ";
            	        print "ACTUAL RESULT 3 %s" %actualresult;
            	        print "Factory reset count: %s" %details;
            	    else:
            	        tdkTestObj.setResultStatus("FAILURE");
            	        print "TEST STEP 3: Retrieve the Platform_GetFactoryResetCount and check the new reset count";
            	        print "EXPECTED RESULT 3: FactoryResetCount should be same as the initial value ";
            	        print "[TEST EXECUTION RESULT] : FAILURE";
            	        print "Factory reset count: %s" %details;
		else:
		    #Set the result status of execution
        	    tdkTestObj.setResultStatus("FAILURE");
        	    details = tdkTestObj.getResultDetails();
        	    print "TEST STEP 2: Invoke platform_hal_ClearResetCount() with 0 as parameter";
        	    print "EXPECTED RESULT 2: Should successfully invoke platform_hal_ClearResetCount()";
        	    print "ACTUAL RESULT 2: platform_hal_ClearResetCount() invocation failed"
        	    print "[TEST EXECUTION RESULT] : %s" %actualresult;
	    else:
		print "Reset Count is already cleared"
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the Platform_GetFactoryResetCount";
            print "EXPECTED RESULT 1: Should retrieve the Platform_GetFactoryResetCount ";
            print "ACTUAL RESULT 1: %s" %actualresult;
            print "Factory reset count: %s" %resetCount;
        obj.unloadModule("halplatform");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
