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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_WIFIHAL_6GHzSetRadiochannel</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set running channel no: using wifi_setRadioChannel() and verify using wifi_getRadioChannel.</synopsis>
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
    <test_case_id>TC_WIFIHAL_702</test_case_id>
    <test_objective>Set running channel no: using wifi_setRadioChannel() and verify using wifi_getRadioChannel()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioChannel()
wifi_getRadioChannel()
wifi_getRadioPossibleChannels()</api_or_interface_used>
    <input_parameters>methodName   :    getRadioChannel
methodName   :    getRadioPossibleChannels
methodName   :    setRadioChannel</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using wifi_getRadioChannel() get and save current channel
3. Set a new channel from possible channel list using wifi_setRadioChannel()
4. Verify whether the set was success by getting the channel value using wifi_getRadioChannel()
5. Revert back to the initial channel value
6. Unload wifihal module</automation_approch>
    <expected_output>Setting channel value using  wifi_setRadioChannel() should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetRadiochannel</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
import time;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetRadiochannel');

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

	    #get the current cahnnel number
	    expectedresult="SUCCESS";
	    radioIndex = idx;
	    getMethod = "getRadioChannel"
	    param = 0
	    primitive = 'WIFIHAL_GetOrSetParamULongValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

	    if expectedresult in actualresult :
		currChannel = int(details.split(":")[1].strip())

		#get the possible channel list
		getMethod = "getRadioPossibleChannels"
		primitive = 'WIFIHAL_GetOrSetParamStringValue'
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

		if expectedresult in actualresult :
		    possibleCh = details.split(":")[1].strip().split(',')
                    channel = int(possibleCh[0])
		    #from possible channel list, select a channel != current channel num:, to do set operation
		    for index in range(len(possibleCh)):
			if int(possibleCh[index]) != currChannel:
			    channel = int(possibleCh[index]) ;
			    break;
		    print "Channel to be set :",channel
		    #setchannel with the above selected channel number
		    setMethod = "setRadioChannel"
		    primitive = 'WIFIHAL_GetOrSetParamULongValue'

		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, channel, setMethod)
		    if expectedresult in actualresult :
			print "Radio channel set"

			time.sleep(20)

			#Verify set operation with a get operation
			getMethod = "getRadioChannel"
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
			if expectedresult in actualresult and channel == int(details.split(":")[1].strip()):
			    print "setRadioChannel Success, verified with getRadioChannel()"

			    #revert channel num
			    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, currChannel, setMethod)

			    if expectedresult in actualresult :
                                tdkTestObj.setResultStatus("SUCCESS");
				print "Radio channel reverted back";
			    else:
                                tdkTestObj.setResultStatus("FAILURE");
				print "Couldn't revert channel num"
			else:
			    print "Set validation with get api failed"
			    tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
