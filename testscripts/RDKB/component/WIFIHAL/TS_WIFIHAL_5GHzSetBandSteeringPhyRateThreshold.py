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
  <name>TS_WIFIHAL_5GHzSetBandSteeringPhyRateThreshold</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the band steering physical modulation rate threshold parameters for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_152</test_case_id>
    <test_objective>To set and get the band steering physical modulation rate threshold parameters for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringCapability()
wifi_getBandSteeringPhyRateThreshold()
wifi_setBandSteeringPhyRateThreshold()</api_or_interface_used>
    <input_parameters>methodName : getBandSteeringCapability
methodName : getBandSteeringPhyRateThreshold
methodName : setBandSteeringPhyRateThreshold
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringCapability() to see if the BandSteering Capability is available or not. If available proceed to next step, else return SUCCESS and exit. 
3. Using  WIFIHAL_GetOrSetParamIntValue invoke wifi_getBandSteeringPhyRateThreshold()
4. Using WIFIHAL_GetOrSetParamIntValue 
 invoke wifi_setBandSteeringPhyRateThreshold and set a valid value
5. Invoke wifi_getBandSteeringPhyRateThreshold() to get the previously set value. 
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the PhyRateThreshold back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>Set and get values of PhyRateThreshold should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetBandSteeringPhyRateThreshold</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetBandSteeringPhyRateThreshold');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    getMethod = "getBandSteeringCapability"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    radioIndex = 1
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    if expectedresult in actualresult:
        enable = details.split(":")[1].strip()
        tdkTestObj.setResultStatus("SUCCESS");
        if "Enabled" in enable:

            getMethod = "getBandSteeringPhyRateThreshold"
            primitive = 'WIFIHAL_GetOrSetParamIntValue'
            radioIndex = 1
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
            initGetValue = details.split(":")[1].strip()

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                setMethod = "setBandSteeringPhyRateThreshold"
                radioIndex = 1
                primitive = 'WIFIHAL_GetOrSetParamIntValue'
                r = range(30,int(initGetValue)) + range(int(initGetValue)+1, 100)
                setValue = random.choice(r)
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                if expectedresult in actualresult:
                    getMethod = "getBandSteeringPhyRateThreshold"
                    radioIndex = 1
                    primitive = 'WIFIHAL_GetOrSetParamIntValue'
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        finalGetValue = details.split(":")[1].strip()

                        if setValue == int(finalGetValue):
                            print "TEST STEP: Comparing set and get values of BandSteeringPhyRateThreshold"
                            print "EXPECTED RESULT: Set and get values should be the same"
                            print "ACTUAL RESULT : Set and get values are the same"
                            print "Set value: %s"%setValue
                            print "Get value: %s"%finalGetValue
                            print "TEST EXECUTION RESULT :SUCCESS"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "TEST STEP: Comparing set and get values of BandSteeringPhyRateThreshold"
                            print "EXPECTED RESULT: Set and get values should be the same"
                            print "ACTUAL RESULT : Set and get values are NOT the same"
                            print "Set value: %s"%setValue
                            print "Get value: %s"%finalGetValue
                            print "TEST EXECUTION RESULT :FAILURE"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "getBandSteeringPhyRateThreshold() call failed after set operation"

                    #Revert back to initial value
                    setMethod = "setBandSteeringPhyRateThreshold"
                    primitive = 'WIFIHAL_GetOrSetParamIntValue'
                    setValue = int(initGetValue)
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Successfully reverted back to inital value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to revert to initial value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "setBandSteeringPhyRateThreshold() call failed"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "getBandSteeringPhyRateThreshold() call failed"
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


