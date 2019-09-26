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
  <version>1</version>
  <name>TS_WIFIHAL_5GHzSetRadioDCSChannelPool</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the dynamic channel selection pool from a set of possible channels</synopsis>
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
    <test_case_id>TC_WIFIHAL_126</test_case_id>
    <test_objective>To set the dynamic channel selection pool from a set of possible channels and verify by getting it</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioPossibleChannels()
wifi_getRadioDCSChannelPool()
wifi_setRadioDCSChannelPool()</api_or_interface_used>
    <input_parameters>methodName :getRadioPossibleChannels
methodName :getRadioDCSChannelPool
methodName :setRadioDCSChannelPool
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getRadioPossibleChannels() and save the get value
3. Randomly choose few radio channels from the above obtained string and using WIFIHAL_GetOrSetParamStringValue invoke wifi_setRadioDCSChannelPool()
4. Invoke wifi_getRadioDCSChannelPool() to get the previously set value. 
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
5. Unload wifihal module</automation_approch>
    <except_output>Set and get values of DCS Channel Pool should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioDCSChannelPool</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioDCSChannelPool');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    radioIndex = 1
    getMethod = "getRadioPossibleChannels"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method to execute wifi_getRadioPossibleChannels()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

    possibleChannels = details.split(":")[1].strip().split(",")
    setDcsChList = random.sample(possibleChannels,3)
    setDcsChPool = ','.join(setDcsChList)

    if expectedresult in actualresult:
        expectedresult="SUCCESS";
        radioIndex = 1
        getMethod = "getRadioDCSChannelPool"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method to execute wifi_getRadioDCSChannelPool()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        initialDCSChPool = details.split(":")[1].strip()
        if expectedresult in actualresult:
            expectedresult="SUCCESS";
            radioIndex = 1
            setMethod = "setRadioDCSChannelPool"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
            print "setDcsChList",setDcsChList

            #Calling the method to execute wifi_setRadioDCSChannelPool()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setDcsChPool, setMethod)

            if expectedresult in actualresult:
                    radioIndex = 1
                    expectedresult="SUCCESS";
                    radioIndex = 1
                    getMethod = "getRadioDCSChannelPool"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'

                    #Calling the method to execute wifi_getRadioDCSChannelPool()
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

                    finalDCSChPool = details.split(":")[1].strip()
                    if expectedresult in actualresult:
                        if setDcsChPool == finalDCSChPool:
                            print "TEST STEP: Comparing the set and get value of DCS Channel Pool"
                            print "EXPECTED RESULT : Set and get values should be the same"
                            print "ACTUAL RESULT : Set and get values are the same"
                            print "TEST EXECUTION RESULT : SUCCESS"
			    print "setDcsChList:",setDcsChList
			    print "getDcsChList: ",finalDCSChPool
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "TEST STEP: Comparing the set and get value of DCS Channel Pool"
                            print "EXPECTED RESULT : Set and get values should be the same"
                            print "ACTUAL RESULT : Set and get values are not the same"
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
                        print "wifi_getRadioDCSChannelPool() failed";
                        tdkTestObj.setResultStatus("FAILURE");
            else:
                print "Wifi_setRadioDCSChannelPool() failed";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "Wifi_getRadioDCSChannelPool() failed";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getRadioPossibleChannels() falied"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

