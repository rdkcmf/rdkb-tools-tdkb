##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetApSecurityModeEnabled_Personal</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get all the personal security modes for 5GHz.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_514</test_case_id>
    <test_objective>To set and get all the personal security modes for 5GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityModeSupported()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : getApSecurityModeSupported
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
ApIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApSecurityModeEnabled() and save the get value
3. Set all the Personal SecurityModes from supported SecurityModes list and using  WIFIHAL_GetOrSetParamStringValue invoke wifi_setApSecurityModeEnabled()
4. Invoke wifi_getApSecurityModeEnabled() to get the previously set value.
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the SecurityMode back to initial value
7. Unload wifihal module</automation_approch>
    <expected_output>Should be able to set and get all the personal security modes for 5GHz.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApSecurityModeEnabled_Personal</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApSecurityModeEnabled_Personal');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
	apIndex = idx;
	getMethod = "getApSecurityModesSupported"
	primitive = 'WIFIHAL_GetOrSetParamStringValue'

	#Calling the method to execute wifi_getApSecurityModeSupported()
	tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
            supportedModes = details.split(":")[1].strip()
	    supportedModes = supportedModes.split(',')
            expectedresult="SUCCESS";
	    apIndex = idx;
            getMethod = "getApSecurityModeEnabled"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'

	    #Calling the method to execute wifi_getApSecurityModeEnabled()
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

            if expectedresult in actualresult:
		initMode = details.split(":")[1].strip()
                if initMode in supportedModes:
                    tdkTestObj.setResultStatus("SUCCESS");
		    print "Initial ApSecurityMode is from the supported modes"
                    PersonalModes = list(filter(lambda x: 'Personal' in x, supportedModes))
                    print "Setting and checking the Personal security modes : ",PersonalModes
                    for setMode in PersonalModes :
                        print "Setting the ApSecurityMode to ",setMode
                        expectedresult="SUCCESS";
			apIndex = idx;
			setMethod = "setApSecurityModeEnabled"
			primitive = 'WIFIHAL_GetOrSetParamStringValue'

			#Calling the method to execute wifi_setApSecurityModeEnabled()
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

                        if expectedresult in actualresult:
			    expectedresult="SUCCESS";
			    apIndex = idx;
		            getMethod = "getApSecurityModeEnabled"
			    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                            #Calling the method to execute wifi_getApSecurityModeEnabled()
			    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                            if expectedresult in actualresult:
				finalMode = details.split(":")[1].strip()
                                if finalMode == setMode:
				    tdkTestObj.setResultStatus("SUCCESS");
				    print "TEST STEP: Compare the set and get values of ApSecurityModeEnabled"
			            print "EXPECTED RESULT: Set and get values of ApSecurityModeEnabled should be same"
				    print "ACTUAL RESULT: Set and get values of ApSecurityModeEnabled are the same"
			            print "setMode = ",setMode
				    print "getMode = ",finalMode
				    print "TEST EXECUTION RESULT : SUCCESS"
			        else:
				    tdkTestObj.setResultStatus("FAILURE");
			            print "TEST STEP: Compare the set and get values of ApSecurityModeEnabled"
			            print "EXPECTED RESULT: Set and get values of ApSecurityModeEnabled should be same"
				    print "ACTUAL RESULT: Set and get values of ApSecurityModeEnabled are NOT the same"
				    print "setMode = ",setMode
				    print "getMode = ",finalMode
				    print "TEST EXECUTION RESULT : FAILURE"

                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "wifi_getApSecurityModeEnabled() call failed after set operation"

                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "wifi_setApSecurityModeEnabled() call failed"

                    expectedresult="SUCCESS";
                    apIndex = idx;
                    setMethod = "setApSecurityModeEnabled"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                    #Revert the ApSecurityModeEnabled back to initial value
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initMode, setMethod)
                    if expectedresult in actualresult:
                        print "Successfully reverted the ApSecurityModeEnabled to initial value"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else :
                        print "Unable to revert the ApSecurityModeEnabled"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
			tdkTestObj.setResultStatus("FAILURE");
			print "Initial ApSecurityMode is not in supported modes"

            else:
		    print "wifi_getApSecurityModeEnabled() failed"
		    tdkTestObj.setResultStatus("FAILURE");
        else:
		print "wifi_getApSecurityModeSupported() failed"
		tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
