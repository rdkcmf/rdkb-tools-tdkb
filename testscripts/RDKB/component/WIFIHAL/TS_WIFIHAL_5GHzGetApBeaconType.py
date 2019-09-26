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
  <version>7</version>
  <name>TS_WIFIHAL_5GHzGetApBeaconType</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the Beacon type value set in device for 5GHz radio using wifi_getApBeaconType HAL API and validate the same using wifi_getApSecurityModeEnabled HAL API</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_69</test_case_id>
    <test_objective>To check the Beacon type value set in device for 5GHz radio using wifi_getApBeaconType HAL API and validate the same using wifi_getApSecurityModeEnabled HAL API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBeaconType()
wifi_getApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName  : getApBeaconType
methodName : getApSecurityModeEnabled
apIndex : 1</input_parameters>
    <automation_approch>1. Load the wifihal module.
2. Get the current Ap Security Mode Enabled by invoking wifi_getApSecurityModeEnabled() HAL API.
3. Get the current ApBeaconType by invoking wifi_getApBeaconType() HAL API.
4. ApBeaconType should match with the corresponding Ap Security Mode Enabled.
5. If yes, return SUCCESS, else FAILURE
6. Unload the module.</automation_approch>
    <except_output>ApBeaconType should match with the corresponding Ap Security Mode Enabled for 5GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetApBeaconType</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApBeaconType');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getApSecurityModeEnabled"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
        mode = details.split(":")[1].strip();
        dict_valid = {'None':'None','WPA-Personal':'WPA','WPA-WPA2-Personal':'WPAand11i','WPA2-Personal':'11i'}

        getMethod = "getApBeaconType"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
	    Beaconvalue = details.split(":")[1].strip()
            if mode in dict_valid :
                print "Ap Security Mode Enabled is within the valid securityMode:beaconType mapping list";
                if Beaconvalue == dict_valid.get(mode) :
                    print "ApBeaconType is matching with the security mode enabled %s"%details
   	            tdkTestObj.setResultStatus("SUCCESS");
	            print "TEST STEP 1: Validate the Ap BeaconType";
	            print "EXPECTED RESULT 1: Ap BeaconType should be %s when the Ap Security Mode Enabled is %s and Ap BeaconType should be in ['None', 'Basic', 'WPA', '11i', 'WPAand11i']"%(dict_valid.get(mode),mode);
	            print "ACTUAL RESULT 1: AP BeaconType Received: %s"%Beaconvalue;
	            print "[TEST EXECUTION RESULT] : SUCCESS";
	        else:
		    print "ApBeaconType is NOT matching with the security mode enabled %s"%details
	            tdkTestObj.setResultStatus("FAILURE");
	            print "TEST STEP 1: Validate the Ap BeaconType";
	            print "EXPECTED RESULT 1: Ap BeaconType should be %s when the Ap Security Mode Enabled is %s and Ap BeaconType should be in ['None', 'Basic', 'WPA', '11i', 'WPAand11i']"%(dict_valid.get(mode),mode);
	            print "ACTUAL RESULT 1: AP BeaconType Received: %s"%Beaconvalue;
	            print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                print "Ap Security Mode Enabled is not within the valid securityMode:beaconType mapping list";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "getApBeaconType() failed"
            obj.setLoadModuleStatus("FAILURE");
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "getApSecurityModeEnabled() failed";
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
