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
  <version>10</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzWifiDown</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To call the wifi down for 5GHz radio using wifi_down HAL API and validate the same</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_234</test_case_id>
    <test_objective>To set the wifi down for 5GHz radio using wifi_down HAL API and validate the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB6</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_down()</api_or_interface_used>
    <input_parameters>methodName   :   wifiDown
apIndex   :    1</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested (WIFIHAL_GetOrSetParamStringValue  - func name - "If not exists already" WIFIHAL - module name Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIHAL_5GHzWifiDown.py)
3.Execute the generated Script(TS_WIFIHAL_5GHzWifiDown.py) using execution page of  Test Manager GUI
4.wifihalstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIHAL_GetOrSetParamStringValue through registered TDK wifihalstub function along with necessary Path Name as arguments
5.WIFIHAL_Down (stub function) will call  Ccsp Base Function named "ssp_WIFIHALDown" that inturn will call WIFIHAL Library Function wifi_down() function
6.Response(s)(printf) from TDK Component,Ccsp Library function and wifihalstub would be logged in Agent Console log based on the debug info redirected to agent console
7.wifihalstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result
8.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifihalstub</automation_approch>
    <expected_output>"""CheckPoint
1:wifi_down() from DUT should be available in Agent Console LogCheckPoint
2:TDK agent Test Function will log the test case result as PASS based on API response CheckPoint
3:Test Manager GUI will publish the result as SUCCESS in Execution page"""</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzWifiDown</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from wifiUtility import *;
radio0 = "2.4G"
radio1 = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzWifiDown');
def wifidown (idx0,idx1):
    #Calling the method from wifiUtility to execute wifidown test case and set result status for the test
    expectedresult = "SUCCESS";
    tdkTestObj = obj.createTestStep("WIFIHAL_Down");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 4: Validate the wifi_down Function";
        print "EXPECTED RESULT 4: wifi_down should return SUCCESS";
        print "ACTUAL RESULT 4: wifi_down operation returned SUCCESS";
        print "Actual result is :",details;
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Get the Radiostatus
        radioIndex = idx1;
        getMethod = "getRadioStatus"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            RadioEnableStatus_afterwifidown = details.split(":")[1].strip()
            if "Disabled" in RadioEnableStatus_afterwifidown:
                print "TEST STEP 5: Get the Radioenable status after wifidown operation";
                print "EXPECTED RESULT 5: Radioenable status should be return the state as 'Disabled'";
                print "ACTUAL RESULT 5:Radioenable status is returned as 'Enable'";
                print "Radioenable status is :",RadioEnableStatus_afterwifidown;
                print "wifi_down api functioned properly"
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Initializes the down radios
                tdkTestObj = obj.createTestStep('WIFIHAL_ParamRadioIndex');
                tdkTestObj.addParameter("radioIndex", idx0);
                tdkTestObj.addParameter("methodName", "initRadio");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult0 = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                tdkTestObj = obj.createTestStep('WIFIHAL_ParamRadioIndex');
                tdkTestObj.addParameter("radioIndex", idx1);
                tdkTestObj.addParameter("methodName", "initRadio");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult1 = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult0 and expectedresult in actualresult1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "wifi_initRadio operation success"
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "wifi_initRadio operation failed"
                    print "[TEST EXECUTION RESULT] : FAILURE";
                #Revert back to initial value
                setMethod = "setRadioEnable"
                primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                newEnable = 1
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx0, newEnable, setMethod)
                tdkTestObj, actualresult1, details = ExecuteWIFIHalCallMethod(obj, primitive, idx1, newEnable, setMethod)
                if expectedresult in actualresult and expectedresult in actualresult1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 6:Revert back the RadiostatusEnable as 'Enable'";
                    print "EXPECTED RESULT 6:Should Revert back the RadiostatusEnable as 'Enable'";
                    print "ACTUAL RESULT 6:Reverted back the RadiostatusEnable as 'Enable'";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 6:Revert back the RadiostatusEnable as 'Enable'";
                    print "EXPECTED RESULT 6:Should Revert back the RadiostatusEnable as 'Enable'";
                    print "ACTUAL RESULT 6:Failed to Revert back the RadiostatusEnable as 'Enable'";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "wifi_down operation not functioned successfully";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "Failed to get the Radiostatus"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 4: Validate the wifi_down Function";
        print "EXPECTED RESULT 4: wifi_down should return SUCCESS";
        print "ACTUAL RESULT 4: wifi_down operation returned FAILURE";
        print "[TEST EXECUTION RESULT] : FAILURE";
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx0 = getIndex(obj, radio0);
    tdkTestObjTemp, idx1 = getIndex(obj, radio1);
    ## Check if a invalid index is returned
    if idx0 == -1 or idx1 == -1:
        if idx0 == -1 :
            print "Failed to get radio index for radio %s\n" %radio0;
        if idx1 == -1:
	    print "Failed to get radio index for radio %s\n" %radio1;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the radio status
	expectedresult="SUCCESS";
	radioIndex = idx1;
        getMethod = "getRadioStatus"
	primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	if expectedresult in actualresult:
	    enable = details.split(":")[1].strip()
	    tdkTestObj.setResultStatus("SUCCESS");
	    if "Enabled" in enable:
	        print "TEST STEP 1:Get the current radio status";
		print "EXPECTED RESULT 1:Radio Status should be 'Enabled' for 5GHz";
		print "ACTUAL RESULT 1: Radio status is ",enable;
		wifidown (idx0,idx1)
		time.sleep(10)
	    else:
	        print "TEST STEP 1:Get the current radio status";
		print "EXPECTED RESULT 1:Radio Status should be 'Enabled' for 5GHz";
		print "ACTUAL RESULT 1: Radio status is",enable;
		#set radiostatus as "Enabled"
		setMethod = "setRadioEnable"
		newEnable = 1
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, setMethod)
		if expectedresult in actualresult :
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 2:Set the Radio status as 'Enabled'";
		    print "EXPECTED RESULT 2:Should set the Radio Status as 'Enabled' for 5GHz";
		    print "ACTUAL RESULT 2: Radio status set as 'Enabled'";
		    getMethod = "getRadioEnable"
		    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
		    if expectedresult in actualresult:
		        tdkTestObj.setResultStatus("SUCCESS");
			Radioenablestatus = details.split(":")[1].strip()
			if "Enabled" in Radioenablestatus:
			    print "TEST STEP 3:Get the RadiostatusEnable after set operation";
			    print "EXPECTED RESULT 3:Radio Status should be 'Enabled' state for 5GHz";
			    print "ACTUAL RESULT 3: RadiostatusEnable state  is",Radioenablestatus;
			    wifidown (idx0,idx1)
			    time.sleep(10)
			else:
			    tdkTestObj.setResultStatus("FAILURE");
			    print "TEST STEP 3:Get the RadiostatusEnable after set operation";
			    print "EXPECTED RESULT 3:Radio Status should be 'Enabled' state for 5GHz";
			    print "ACTUAL RESULT 3: RadiostatusEnable state  is",Radioenablestatus;
			    print "WIFI API 'wifi_setRadioEnable' returns false success"
		    else:
		        print "TEST STEP 3:Get the Radio status for 5GHz"
			print "EXPECTED RESULT 3:Radio Status should be return some status for 5GHz";
			print "ACTUAL RESULT 3: Failed to get the Radio status";
		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 2:Set the Radio status as 'Enabled'";
		    print "EXPECTED RESULT 2:Should set the Radio Status as 'Enabled' for 5GHz";
		    print "ACTUAL RESULT 2: Failed to set the Radio status as 'Enabled'";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1:Get the Radio status";
	    print "EXPECTED RESULT 1:Should get the Radio Status for 5GHz";
	    print "ACTUAL RESULT 1: Failed to get the Radio status";
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");