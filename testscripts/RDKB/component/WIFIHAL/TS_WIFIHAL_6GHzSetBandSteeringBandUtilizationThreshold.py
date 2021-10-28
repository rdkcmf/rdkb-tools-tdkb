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
  <name>TS_WIFIHAL_6GHzSetBandSteeringBandUtilizationThreshold</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the Band Utilization Threshold for 6GHz      with the HAL APIs wifi_setBandSteeringBandUtilizationThreshold and wifi_getBandSteeringBandUtilizationThreshold.</synopsis>
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
    <test_case_id>TC_WIFIHAL_631</test_case_id>
    <test_objective>To set and get the Band Utilization Threshold for 6GHz with the HAL APIs wifi_setBandSteeringBandUtilizationThreshold and wifi_getBandSteeringBandUtilizationThreshold.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringCapability()
wifi_getBandSteeringBandUtilizationThreshold()
wifi_setBandSteeringBandUtilizationThreshold()</api_or_interface_used>
    <input_parameters>methodName : getBandSteeringCapability
methodName : getBandSteeringBandUtilizationThreshold
methodName : setBandSteeringBandUtilizationThreshold
setValue : valid random value
radioIndex : index corresponding to 6G radio</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringCapability() to see if the BandSteering Capability is available or not. If available proceed to next step, else return SUCCESS and exit.
3. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getBandSteeringBandUtilizationThreshold()
4. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_setBandSteeringBandUtilizationThreshold and set a valid value
5. Invoke wifi_getBandSteeringBandUtilizationThreshold() to get the previously set value.
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the BandUtilizationThreshold back to initial value
8. Unload wifihal module</automation_approch>
    <expected_output>Setting the Band Steering Band Utilization Threshold using the HAL API wifi_setBandSteeringBandUtilizationThreshold() should be successful and the get value using wifi_getBandSteeringBandUtilizationThreshold() should reflect the value set if the device is Band Steering capable for 6GHz. </expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetBandSteeringBandUtilizationThreshold</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import random;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetBandSteeringBandUtilizationThreshold');
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
        getMethod = "getBandSteeringCapability"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        radioIndex = idx;
        print "\nStep 1 : Check the Band Steering Capability";
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

        if expectedresult in actualresult:
            enable = details.split(":")[1].strip()
            tdkTestObj.setResultStatus("SUCCESS");

            if "Enabled" in enable:
                print "\nStep 2 : Get initial value of Band Utilization Threshold";
                getMethod = "getBandSteeringBandUtilizationThreshold"
                primitive = 'WIFIHAL_GetOrSetParamIntValue'
                radioIndex = idx;
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                if expectedresult in actualresult:
                    initGetValue = details.split(":")[1].strip();
                    tdkTestObj.setResultStatus("SUCCESS");

                    setMethod = "setBandSteeringBandUtilizationThreshold"
                    radioIndex = idx;
                    primitive = 'WIFIHAL_GetOrSetParamIntValue'
                    r = range(1,int(initGetValue)) + range(int(initGetValue)+1, 100)
                    setValue = random.choice(r)
                    print "\nStep 3 : Set the Band Utilization Threshold to : %d" %setValue;
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                    if expectedresult in actualresult:
                        getMethod = "getBandSteeringBandUtilizationThreshold"
                        radioIndex = idx;
                        primitive = 'WIFIHAL_GetOrSetParamIntValue'
                        print "\nStep 4 : Get the current value of Band Utilization Threshold";
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            finalGetValue = details.split(":")[1].strip()
                            print "\nStep 5 : Validating the set operation for Band Utilization Threshold";
                            print "TEST STEP: Comparing set and get values of BandSteeringBandUtilizationThreshold"
                            print "EXPECTED RESULT: Set and get values should be the same"
                            print "Set value: %s"%setValue
                            print "Get value: %s"%finalGetValue

                            if setValue == int(finalGetValue):
                                print "ACTUAL RESULT : Set and get values are the same"
                                print "TEST EXECUTION RESULT :SUCCESS"
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "ACTUAL RESULT : Set and get values are NOT the same"
                                print "TEST EXECUTION RESULT :FAILURE"
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "getBandSteeringBandUtilizationThreshold() call failed after set operation"

                        #Revert back to initial value
                        setMethod = "setBandSteeringBandUtilizationThreshold"
                        primitive = 'WIFIHAL_GetOrSetParamIntValue'
                        setValue = int(initGetValue)
                        print "\nStep 6 : Reverting to initial Band Utilization Threshold value";
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Successfully reverted back to inital value"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Unable to revert to initial value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "setBandSteeringBandUtilizationThreshold() call failed"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "getBandSteeringBandUtilizationThreshold() call failed"
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

