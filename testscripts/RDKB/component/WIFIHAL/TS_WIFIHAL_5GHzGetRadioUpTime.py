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
  <name>TS_WIFIHAL_5GHzGetRadioUpTime</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the radio up time for 5GHz</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_164</test_case_id>
    <test_objective>To get the radio up time for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioUpTime()</api_or_interface_used>
    <input_parameters>methodName : getRadioUpTime
RadioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_getRadioUpTime() 
3. Check if the value received is greater than zero, if yes return SUCCESS, else return FAILURE
4. Unload wifihal module</automation_approch>
    <except_output>RadioUpTime &gt; 0</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioUpTime</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioUpTime');

#Get the result of connection with test component and STB
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

	    expectedresult = "SUCCESS"
	    radioIndex = idx
	    getMethod = "getRadioUpTime"
	    primitive = 'WIFIHAL_GetOrSetParamULongValue'

	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

	    if expectedresult in actualresult:
		upTime = details.split(":")[1].strip()
		if int(upTime) > 0:
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP : Check if Radio Up Time is greater than 0"
		    print "EXPECTED RESULT : Radio up time should is greater than 0"
		    print "ACTUAL RESULT : Radio up time is greater than 0"
		    print "Radio UpTime = %s"%upTime
		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP : Check if Radio Up Time is greater than 0"
		    print "EXPECTED RESULT : Radio up time should is greater than 0"
		    print "ACTUAL RESULT : Radio up time is greater than 0"
		    print "Radio UpTime = %s"%upTime
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "wifi_getRadioUpTime() call failed"
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

