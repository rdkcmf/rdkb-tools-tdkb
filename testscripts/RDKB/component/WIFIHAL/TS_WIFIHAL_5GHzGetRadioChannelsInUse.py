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
  <version>5</version>
  <name>TS_WIFIHAL_5GHzGetRadioChannelsInUse</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test if the list returned by wifi_getRadioChannelsInUse()api is a subset of the list returned by wifi_getRadioPossibleChannels()</synopsis>
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
    <test_case_id>TC_WIFIHAL_06</test_case_id>
    <test_objective>Test if the list returned by wifi_getRadioChannelsInUse()api is a subset of the list returned by wifi_getRadioPossibleChannels()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioChannelsInUse()
wifi_getRadioPossibleChannels()</api_or_interface_used>
    <input_parameters>methodName : getRadioPossibleChannels
methodName : getRadioChannelsInUse
radioIndex     :    1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioChannelsInUse()  to get the current channels in use
3.Get the possible channel list using wifi_getRadioPossibleChannels()  
4. check if current channels in use value is from the possible channel list
5. Unload wifihal module</automation_approch>
    <except_output>current channels in use value should be from the possible channel list</except_output>
    <priority>High</priority>
    <test_stub_interface>WiFiAgent</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioChannelsInUse</test_script>
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

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioChannelsInUse');

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
	    radioIndex = idx
	    getMethod = "getRadioPossibleChannels"
	    primitive = 'WIFIHAL_GetOrSetParamStringValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

	    if expectedresult in actualresult :
		possibleCh = details.split(":")[1].strip()

		getMethod = "getRadioChannelsInUse"
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
		if expectedresult in actualresult :
		    chInUse = details.split(":")[1].strip();

		    flag = 1
		    for index in range(len(chInUse)):
			if chInUse[index] not in possibleCh:
			    flag = 0;
			    break;

		    if flag == 1 :
			print "Channel In use is a subset of possible cahannels"
		    else:
			print "Error:Channel In use not found in possible channel list"
		else:
		    print "getChannelInUse() failed"
	    else:
		print "getRadioPossibleChannels failed"

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

