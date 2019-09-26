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
  <name>TS_WIFIHAL_2.4GHzDisableApEncryption</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_ParamRadioIndex</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke wifi_disableApEncryption() api and check whether the security mode is changed to "None" by invoking wifi_getApSecurityModeEnabled() api for 2.4GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_280</test_case_id>
    <test_objective>To invoke wifi_disableApEncryption() api and check whether the security mode is changed to "None" by invoking wifi_getApSecurityModeEnabled() api for 2.4GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_disableApEncryption()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : disableApEncryption
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
radioIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Get ApSecurityModeEnabled using wifi_getApSecurityModeEnabled() api.
3.Invoke wifi_disableApEncryption() api.
4.Again get ApSecurityModeEnabled and check whether the mode is changed to 'None'.
5.If changed return SUCCESS and revert the security mode to initial value,else FAILURE.
6.Unload the module.</automation_approch>
    <except_output>The security mode should be changed to "None" after invoking the wifi_disableApEncryption() api for 2.4GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzDisableApEncryption</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzDisableApEncryption');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    apIndex = 0
    getMethod = "getApSecurityModeEnabled"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
    if expectedresult in actualresult:
        ModeEnabled_initial = details.split(":")[1].strip();
	#Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("WIFIHAL_ParamRadioIndex");
        #Giving the method name to invoke the api wifi_disableApEncryption()
        tdkTestObj.addParameter("methodName","disableApEncryption")
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",0);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "details",details;
	if expectedresult in actualresult:
	    expectedresult="SUCCESS";
            apIndex = 0
            getMethod = "getApSecurityModeEnabled"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
	    if expectedresult in actualresult:
		ModeEnabled_final = details.split(":")[1].strip();
		if ModeEnabled_final == 'None':
	            tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 1: To disable Ap Encryption by calling wifi_disableApEncryption api for 2.4GHz";
                    print "EXPECTED RESULT 1: The ModeEnabled should be changed to 'None' state after invoking wifi_disableApEncryption() api for 2.4GHz";
                    print "ACTUAL RESULT 1: The ModeEnabled is changed to 'None' state";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    #Revert the mode security to initial value
                    expectedresult="SUCCESS"
                    apIndex=0
                    setMethod = "setApSecurityModeEnabled"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                    #Calling the method to execute wifi_setApSecurityModeEnabled()
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, ModeEnabled_initial, setMethod)
                    if expectedresult in actualresult:
                        print "Successfully reverted the ApSecurityModeEnabled to initial value";
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Unable to revert the ApSecurityModeEnabled";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
		    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 1: To disable Ap Encryption by calling wifi_disableApEncryption api for 2.4GHz";
                    print "EXPECTED RESULT 1: The ModeEnabled should be changed to 'None' state after invoking wifi_disableApEncryption() api for 2.4GHz";
                    print "ACTUAL RESULT 1: The ModeEnabled is NOT changed to 'None' state";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
		print"wifi_getApSecurityModeEnabled() operation failed after invoking wifi_disableApEncryption() api for 2.4GHz";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"wifi_disableApEncryption() operation failed for 2.4GHz";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print"wifi_getApSecurityModeEnabled() operation failed for 2.4GHz";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
