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
  <name>TS_WIFIHAL_2.4GHzSetInvalidRadioDCSChannelPool</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set dynamic channel pool outside the set of possible channels and verify whether we are able to set it for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_208</test_case_id>
    <test_objective>To set dynamic channel pool outside the set of possible channels and verify whether we are able to set it.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioPossibleChannels()
wifi_getRadioDCSChannelPool()
wifi_setRadioDCSChannelPool()</api_or_interface_used>
    <input_parameters>methodName :getRadioPossibleChannels
methodName :getRadioDCSChannelPool
methodName :setRadioDCSChannelPool
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getRadioPossibleChannels() and save the get value
3. Randomly choose a radio channel not in the possible channels list.
4.Try to set that random value using wifi_setRadioDCSChannelPool().
5.The set operation should fail as we are trying to set value not in the radio possible channels list.
6. Unload wifihal module</automation_approch>
    <except_output>Set operation should fail as we are trying to set the value not in the  radio possible channels list.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetInvalidRadioDCSChannelPool</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetInvalidRadioDCSChannelPool');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    radioIndex = 0
    getMethod = "getRadioPossibleChannels"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method to execute wifi_getRadioPossibleChannels()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0",getMethod)
    possibleChannels = details.split(":")
    if expectedresult in actualresult:
        expectedresult="SUCCESS";
        radioIndex = 0
        getMethod = "getRadioDCSChannelPool"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method to execute wifi_getRadioDCSChannelPool()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        initialDCSChPool = details.split(":")[1].strip()
        for x in range(1):
	        z = random.randint(1,200);
		setDcsChannel = str(z);
	if expectedresult in actualresult:
	    if setDcsChannel not in possibleChannels:
  		expectedresult="FAILURE";
                radioIndex = 0
                setMethod = "setRadioDCSChannelPool"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'
                print "setDcsChannel",setDcsChannel
		#Calling the method to execute wifi_setRadioDCSChannelPool()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setDcsChannel, setMethod)
		if expectedresult in actualresult:
		    print "TEST STEP: Set the DCS channel pool out of possible channels"
                    print "EXPECTED RESULT : Set operation should fail"
                    print "ACTUAL RESULT : Set operation should fail"
                    print "TEST EXECUTION RESULT : SUCCESS"
                    print "setDcsChannel:",setDcsChannel
                    tdkTestObj.setResultStatus("SUCCESS");
		else:
		    print "TEST STEP: Set the DCS channel pool out of possible channels"
                    print "EXPECTED RESULT : Set operation should fail "
                    print "ACTUAL RESULT : Set operation is success"
                    print "TEST EXECUTION RESULT : FAILURE"
                    tdkTestObj.setResultStatus("FAILURE");
		    #Revert the DCS Channel Pool back to initial value
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initialDCSChPool, setMethod)
                    if expectedresult in actualresult:
                        print "Successfully reverted DCS Channel Pool to initial value"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Unable to revert the DCS Channel Pool"
                        tdkTestObj.setResultStatus("FAILURE");
        else:
            print "Wifi_getRadioDCSChannelPool() failed";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getRadioPossibleChannels() failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

