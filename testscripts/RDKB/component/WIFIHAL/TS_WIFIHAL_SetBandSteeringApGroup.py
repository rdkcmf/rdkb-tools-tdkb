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
  <version>3</version>
  <name>TS_WIFIHAL_SetBandSteeringApGroup</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the bandsteering ApGroup and get it</synopsis>
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
    <test_case_id>TC_WIFIHAL_144</test_case_id>
    <test_objective>To set and get the BandSteeringApGroup </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringCapability()
wifi_getBandSteeringApGroup()
wifi_setBandSteeringApGroup()
</api_or_interface_used>
    <input_parameters>methodName : getBandSteeringCapability
methodName : getBandSteeringApGroup
methodName : setBandSteeringApGroup</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringCapability() to see if the BandSteering Capability is available or not. If available proceed to next step, else return SUCCESS and exit. 
3. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getBandSteeringApGroup()
4. Using WIFIHAL_GetOrSetParamStringValue 
 invoke wifi_setBandSteeringApGroup and set another string "2,3" as the ApGroup
5. Invoke wifi_getBandSteeringApGroup() to get the previously set value. 
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the BandSteeringApGroup back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>Set and get values of BandSteeringApGroup should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_SetBandSteeringApGroup</test_script>
    <skipped>No</skipped>
    <release_version/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetBandSteeringEnable');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    getMethod = "getBandSteeringCapability"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, 0, getMethod)

    if expectedresult in actualresult:
	enable = details.split(":")[1].strip()
	tdkTestObj.setResultStatus("SUCCESS");
	if "Enabled" in enable:
	    
	    getMethod = "getBandSteeringApGroup"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, "0", getMethod)
	    initGetValue = details.split(":")[1].strip() 

	    if expectedresult in actualresult:
		tdkTestObj.setResultStatus("SUCCESS");
		setMethod = "setBandSteeringApGroup"
		primitive = 'WIFIHAL_GetOrSetParamStringValue'
		setValue = "3,4"
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, setValue, setMethod)

		if expectedresult in actualresult:
		    getMethod = "getBandSteeringApGroup"
		    primitive = 'WIFIHAL_GetOrSetParamStringValue'
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, "0", getMethod)
	
		    if expectedresult in actualresult:
			tdkTestObj.setResultStatus("SUCCESS");
			finalGetValue = details.split(":")[1].strip()
			
			if setValue == finalGetValue:
			    print "TEST STEP: Comparing set and get values of BandSteeringApGroup"
			    print "EXPECTED RESULT: Set and get values should be the same"
			    print "ACTUAL RESULT : Set and get values are the same"
			    print "Set value: %s"%setValue
			    print "Get value: %s"%finalGetValue
			    print "TEST EXECUTION RESULT :SUCCESS"
			    tdkTestObj.setResultStatus("SUCCESS");
			else:
			    print "TEST STEP: Comparing set and get values of BandSteeringApGroup"
			    print "EXPECTED RESULT: Set and get values should be the same"
			    print "ACTUAL RESULT : Set and get values are NOT the same"
			    print "Set value: %s"%setValue
			    print "Get value: %s"%finalGetValue
			    print "TEST EXECUTION RESULT :FAILURE"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "getBandSteeringApGroup() call failed after set operation"
		    #Revert back to initial value
		    setMethod = "setBandSteeringApGroup"
		    primitive = 'WIFIHAL_GetOrSetParamStringValue'
		    setValue = initGetValue
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, setValue, setMethod)

	            if expectedresult in actualresult:
		        tdkTestObj.setResultStatus("SUCCESS");
		        print "Successfully reverted back to inital value"
		    else:
	                tdkTestObj.setResultStatus("FAILURE");
			print "Unable to revert to initial value"
	        else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "setBandSteeringApGroup() call failed"
	    else:
	        tdkTestObj.setResultStatus("FAILURE");
	        print "getBandSteeringApGroup() call failed"
	else:
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "BandSteeringCapability is disabled"
    else:
	tdkTestObj.setResultStatus("FAILURE");
	print "getBandSteeringCapability() call failed"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

