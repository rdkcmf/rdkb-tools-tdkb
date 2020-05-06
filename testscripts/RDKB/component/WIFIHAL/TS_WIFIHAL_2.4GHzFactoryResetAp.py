##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>3</version>
  <name>TS_WIFIHAL_2.4GHzFactoryResetAp</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_ParamApIndex</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Restore AP parameters to default without changing other AP or Radio parameters.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_331</test_case_id>
    <test_objective>To Restore AP parameters to default without changing other AP nor Radio parameters</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setSSIDName
wifi_getSSIDName
wifi_factoryResetAP</api_or_interface_used>
    <input_parameters>methodName : setSSIDName
methodName : getSSIDName
methodName : factoryResetAP
apIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2. Modify current ssid name by passing the parameters apindex and ssid using wifi_setSSIDName() API by  invoking WIFIHAL_GetOrSetParamStringValue'
3. Confirm that this ssid has been set properly by using wifi_getSSIDName() API  by  invoking WIFIHAL_GetOrSetParamStringValue
4. The factory reset API should be now invoked using wifi_factoryResetAP() API.
5. If factoryResetAP call is success , then the SSID name should be set to default value.
6. To confirm that the API  has worked, check the SSID by using  wifi_getSSIDName() API  which  invokes WIFIHAL_GetOrSetParamStringValue. 
7.Compare the SSID set before and after factory reset and confirm that this should be different.
8.Check if the api call is success, else return FAILURE from the script
9.Unload the module.</automation_approch>
    <except_output>The SSID before and after the factory reset should be different.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL_ParamApIndex</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzFactoryResetAp</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;
import time;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzFactoryResetAp');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else: 

	    apIndex = idx
	    getMethod = "getSSIDName"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    print "TEST STEP1: Get the current SSID name"
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

	    if expectedresult in actualresult:
		SSIDName_initial = details.split(":")[1].strip()
		print "SSIDName_initial:", SSIDName_initial

		apIndex = idx
		setMethod = "setSSIDName"
		SSIDName_beforeFactoryReset = "wifi_ssid"
		primitive = 'WIFIHAL_GetOrSetParamStringValue'
		print "TEST STEP2: Set the current SSID name"
		print "Trying to set SSIDName beforeFactoryReset  = ",SSIDName_beforeFactoryReset
		#Calling the method from wifiUtility to execute test case and set result status for the test.
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, SSIDName_beforeFactoryReset, setMethod)
		if expectedresult in actualresult:

		    apIndex = idx
		    getMethod = "getSSIDName"
		    primitive = 'WIFIHAL_GetOrSetParamStringValue'
		    print "TEST STEP3: Get the current SSID name and compare with the set valule"
		    #Calling the method from wifiUtility to execute test case and set result status for the test.
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
		    if expectedresult in actualresult:
			SSIDName_set = details.split(":")[1].strip()
			if SSIDName_set == SSIDName_beforeFactoryReset:
			    print "ACTUAL RESULT : set and get values are same"

			    #Prmitive test case which associated to this Script
			    print "Invoking wifi_factroryResetAP()"
			    print "TEST STEP4: Invoke wifi_factoryResetAP" 
			    print "EXPECTED RESULT: Should revert to default AP values"
			    tdkTestObj = obj.createTestStep('WIFIHAL_ParamApIndex');
			    tdkTestObj.addParameter("apIndex", idx);
			    tdkTestObj.addParameter("methodName", 'factoryResetAP');
			    expectedresult="SUCCESS";
			    tdkTestObj.executeTestCase(expectedresult);
			    actualresult = tdkTestObj.getResult();
			    details = tdkTestObj.getResultDetails();
			    time.sleep(5)
		     
			    if expectedresult in actualresult:
				print "wifi_factoryResetAP invocation success"
				apIndex = idx
				getMethod = "getSSIDName"
				primitive = 'WIFIHAL_GetOrSetParamStringValue'

				print "Get the SSID name after wifi_factoryResetAP"
				#Calling the method from wifiUtility to execute test case and set result status for the test.
				tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
				SSIDName_afterFactoryReset = details.split(":")[1].strip()
				if expectedresult in actualresult:
				    print "Get SSID name operation is success"
				    if SSIDName_afterFactoryReset !=  SSIDName_beforeFactoryReset:
					tdkTestObj.setResultStatus("SUCCESS");
					print "TEST STEP 5: Compare values of SSID Name before and after wifi_factoryResetAP"
					print "EXPECTED RESULT : The values of SSID Name should be different"
					print "ACTUAl RESULT : The values of SSID Name are different"
					print "SSIDName_beforeFactoryReset = ",SSIDName_beforeFactoryReset
					print "SSIDName_afterFactoryReset = ",SSIDName_afterFactoryReset
					print "TEST EXECUTION RESULT :SUCCESS"
				    else:
					tdkTestObj.setResultStatus("FAILURE");
					print "TEST STEP 5: Compare values of SSID Name before and after wifi_factoryResetAP"
					print "EXPECTED RESULT : The values of SSID Names should be different"
					print "ACTUAl RESULT : The values of SSID Names are the same"
					print "SSIDName_beforeFactoryReset = ",SSIDName_beforeFactoryReset
					print "SSIDName_afterFactoryReset = ",SSIDName_afterFactoryReset
					print "TEST EXECUTION RESULT :FAILURE"
				else:
				    print "wifi_getSSIDName() function failed"
				    tdkTestObj.setResultStatus("FAILURE");
			    else: 
			       print "wifi_factoryResetAP() function failed"
			       print "TEST EXECUTION RESULT :FAILURE"
			       tdkTestObj.setResultStatus("FAILURE");
			else:
			    print "SSIDName_initialGet and SSIDName_set are not same"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
			print "wifi_getSSIDName() function failed"
			tdkTestObj.setResultStatus("FAILURE");
		else:          
		     print "wifi_setSSIDName() function failed"
		     tdkTestObj.setResultStatus("FAILURE");  
	    else:
		print "wifi_getSSIDName() function before factoryResetAP failed"
		tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
