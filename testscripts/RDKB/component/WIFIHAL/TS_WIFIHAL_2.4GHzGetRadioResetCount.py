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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzGetRadioResetCount</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the radio reset count and verify that it is incremented after a reset operation</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_172</test_case_id>
    <test_objective>To get the radio reset count and verify that it is incremented after a reset operation</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioResetCount()
wifi_reset()
</api_or_interface_used>
    <input_parameters>methodName : getRadioResetCount
RadioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using  WIFIHAL_GetOrSetParamULongValue invoke wifi_getRadioResetCount() and save the value returned.
3. Using  WIFIHAL_Reset invoke wifi_reset()
4. Invoke wifi_getRadioResetCount() and check if the value returned has incremented by 1
5.Depending upon the value returned , return SUCCESS or FAILURE
6. Unload wifihal module</automation_approch>
    <except_output>Should increment by 1 after reset operation</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetRadioResetCount</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioResetCount');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getRadioResetCount"
    primitive = 'WIFIHAL_GetOrSetParamULongValue'

    #Calling the method to execute wifi_getRadioResetCount()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult:
	initCount = details.split(":")[1].strip()
	
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("WIFIHAL_Reset");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            print "Reset operation SUCCESS"
	    tdkTestObj.setResultStatus("SUCCESS");
 
            expectedresult="SUCCESS";
   	    radioIndex = 0
	    getMethod = "getRadioResetCount"
	    primitive = 'WIFIHAL_GetOrSetParamULongValue'

	    #Calling the method to execute wifi_getRadioResetCount()
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

	    if expectedresult in actualresult:
	        finalCount = details.split(":")[1].strip()

		if int(finalCount) == int(initCount)+1:
                    #Set the result status of execution
	            tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP: Check if the ResetCount is incremented by 1 after reset operation"
		    print "EXPECTED RESULT : Final count should increment by 1"
	            print "ACTUAL RESULT : Final count is incremented by 1"
		    print "Initial RadioResetCount = %s" %initCount
		    print "RadioResetCount after reset operation = %s" %finalCount
		    print "TEST EXECUTION RESULT : SUCCESS"
		else:
                    #Set the result status of execution
	            tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP: Check if the ResetCount is incremented by 1 after reset operation"
		    print "EXPECTED RESULT : Final count should increment by 1"
	            print "ACTUAL RESULT : Final count is NOT incremented by 1"
		    print "Initial RadioResetCount = %s" %initCount
		    print "RadioResetCount after reset operation = %s" %finalCount
		    print "TEST EXECUTION RESULT : FAILURE"
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "wifi_getRadioResetCount() call failed after reset operation"
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "wifi_reset() call failed"
    else:
	tdkTestObj.setResultStatus("FAILURE");
	print "wifi_getRadioResetCount() call failed"

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";


	
		    





