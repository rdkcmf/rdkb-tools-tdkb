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
  <name>TS_WIFIHAL_2.4GHzGetApAssociatedDevicesHighWatermarkThreshold</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the HighWatermarkThreshold value for 2.4GHz radio using wifi_getApAssociatedDevicesHighWatermarkThreshold HAL API and validate the same</synopsis>
  <groups_id>4</groups_id>
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
    <test_case_id>TC_WIFIHAL_33</test_case_id>
    <test_objective>To get the HighWatermarkThreshold value for 2.4GHz radio using wifi_getApAssociatedDevicesHighWatermarkThreshold() HAL API respectively. HighWatermarkThreshold value should be less than or equal to MaxAssociatedDevices. If MaxAssociatedDevices value is 0 then  HighWatermarkThreshold value should be 50 which is the default value.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDevicesHighWatermarkThreshold()
wifi_getApMaxAssociatedDevices()</api_or_interface_used>
    <input_parameters>methodName   :   getApAssociatedDevicesHighWatermarkThreshold
methodName   : getApMaxAssociatedDevices
apIndex      :   0</input_parameters>
    <automation_approch>1. Load wifihal module.
2. Get the HighWatermarkThreshold value by invoking wifi_getApAssociatedDevicesHighWatermarkThreshold() HAL API.
3. Get the MaxAssociatedDevices value by invoking wifi_getApMaxAssociatedDevices() HAL API.
4.  If MaxAssociatedDevices value is 0 then HighWatermarkThreshold value should be 50 which is the default value, else HighWatermarkThreshold value should be less than or equal to MaxAssociatedDevices.
5. Unload the module.</automation_approch>
    <except_output>HighWatermarkThreshold value should be less than or equal to MaxAssociatedDevices. If MaxAssociatedDevices value is 0 then HighWatermarkThreshold value should be 50 which is the default value.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAssociatedDevicesHighWatermarkThreshold</test_script>
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

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAssociatedDevicesHighWatermarkThreshold');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

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
	    getMethod = "getApAssociatedDevicesHighWatermarkThreshold"
	    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

	    #Calling the method from wifiUtility to execute test case and set result status for the test.
	    tdkTestObj, actualresult, details1 = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

	    #Default Threshold value.
	    defaultThresholdValue = 50

	    if expectedresult in actualresult:
		tdkTestObj.setResultStatus("SUCCESS");
		thresholdValue = details1.split(":")[1].strip();
		print "TEST STEP 1: To get the HighWatermarkThreshold value by invoking wifi_getApAssociatedDevicesHighWatermarkThreshold() HAL API";
		print "EXPECTED RESULT 1: To get the HighWatermarkThreshold value successfully";
		print "ACTUAL RESULT 1:  HighWatermarkThreshold value : %s"%thresholdValue;
		print "[TEST EXECUTION RESULT] : SUCCESS";
		getMethodToCheck = "getApMaxAssociatedDevices"

		#Calling the method from wifiUtility to execute test case and set result status for the test.
		tdkTestObj, actualresult, details2 = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethodToCheck)

		if expectedresult in actualresult:
		    tdkTestObj.setResultStatus("SUCCESS");
		    maxAssociatedDeviceValue = details2.split(":")[1].strip();
		    print "TEST STEP 2:  To get the MaxAssociatedDevices value by invoking wifi_getApMaxAssociatedDevices() HAL API";
		    print "EXPECTED RESULT 2: To get the MaxAssociatedDevices value successfully";
		    print "ACTUAL RESULT 2: MaxAssociatedDevices value : %s"%maxAssociatedDeviceValue;
		    print "[TEST EXECUTION RESULT] : SUCCESS";
		    print "HighWatermarkThreshold value : %s"%thresholdValue;
		    print "MaxAssociatedDevices value : %s"%maxAssociatedDeviceValue;
		    if int(maxAssociatedDeviceValue)==0:
		       print "maxAssociatedDeviceValue is 0. thresholdValue is expected to be equal to  defaultThresholdValue  %d"%defaultThresholdValue;
		       if int(thresholdValue) == defaultThresholdValue :
			   tdkTestObj.setResultStatus("SUCCESS");
			   print "TEST STEP 3: To check if  HighWatermarkThreshold value is equal to %d  which is the default value"%defaultThresholdValue;
			   print "EXPECTED RESULT3:thresholdValue should be equal to defaultThresholdValue";
			   print "ACTUAL RESULT 3:thresholdValue is equal to defaultThresholdValue";
			   print "[TEST EXECUTION RESULT] : SUCCESS";
		       else:
			   tdkTestObj.setResultStatus("FAILURE");
			   print "TEST STEP 3: To check if  HighWatermarkThreshold value is equal to %d  which is the default value"%defaultThresholdValue;
			   print "EXPECTED RESULT3:thresholdValue should be equal to defaultThresholdValue";
			   print "ACTUAL RESULT 3:thresholdValue is not equal to defaultThresholdValue";
			   print "[TEST EXECUTION RESULT] :FAILURE";
		    else:
			print"maxAssociatedDeviceValue is not equal to 0. thresholdValue is expected to be less than or equal to  maxAssociatedDeviceValue";
			if int(thresholdValue) <= int(maxAssociatedDeviceValue):
			   tdkTestObj.setResultStatus("SUCCESS");
			   print "TEST STEP 4: To check if  HighWatermarkThreshold value is less than or  equal to MaxAssociatedDevices";
			   print "EXPECTED RESULT 4: thresholdValue should be less than or equal to maxAssociatedDeviceValue";
			   print "ACTUAL RESULT 4:thresholdValue is less than or equal to maxAssociatedDeviceValue";
			   print "[TEST EXECUTION RESULT] : SUCCESS";
			else :
			   tdkTestObj.setResultStatus("FAILURE");
			   print "TEST STEP 4: To check if  HighWatermarkThreshold value is less than or equal to MaxAssociatedDevices";
			   print "EXPECTED RESULT 4: thresholdValue should be less than or equal to maxAssociatedDeviceValue";
			   print "ACTUAL RESULT 4: thresholdValue is not less than  or equal to maxAssociatedDeviceValue";
			   print "[TEST EXECUTION RESULT] : FAILURE";


		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 2:  To get the MaxAssociatedDevices value by invoking wifi_getApMaxAssociatedDevices() HAL API";
		    print "EXPECTED RESULT 2: To get the MaxAssociatedDevices value successfully";
		    print "ACTUAL RESULT 2: Failed to get MaxAssociatedDevices value : %s"%details2;
		    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 1: To get the HighWatermarkThreshold value by invoking wifi_getApAssociatedDevicesHighWatermarkThreshold() HAL API";
		print "EXPECTED RESULT 1: To get the HighWatermarkThreshold value successfully";
		print "ACTUAL RESULT 1:  Failed to get HighWatermarkThreshold value : %s"%details1;
		print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");



