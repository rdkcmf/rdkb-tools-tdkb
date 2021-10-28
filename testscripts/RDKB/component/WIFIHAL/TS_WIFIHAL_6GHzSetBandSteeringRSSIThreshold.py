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
  <name>TS_WIFIHAL_6GHzSetBandSteeringRSSIThreshold</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the Band Steering RSSI Threshold value for 6GHz with the HAL APIs wifi_setBandSteeringRSSIThreshold and wifi_getBandSteeringRSSIThreshold.</synopsis>
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
    <test_case_id>TC_WIFIHAL_630</test_case_id>
    <test_objective>To set and get the Band Steering RSSI Threshold value for 6GHz with the HAL APIs wifi_setBandSteeringRSSIThreshold and wifi_getBandSteeringRSSIThreshold.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringCapability()
wifi_getBandSteeringRSSIThreshold()
wifi_setBandSteeringRSSIThreshold()</api_or_interface_used>
    <input_parameters>methodName : getBandSteeringCapability
methodName : getBandSteeringRSSIThreshold
methodName : setBandSteeringRSSIThreshold
setValue : valid random value
radioIndex : index corresponding to 6G radio</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringCapability() to see if the BandSteering Capability is available or not. If available proceed to next step, else return SUCCESS and exit.
3. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getBandSteeringRSSIThreshold()
4. Get the RSSI range from the platform property file and generate a random value within the specified range. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_setBandSteeringRSSIThreshold  and set the valid random value
5. Invoke wifi_getBandSteeringRSSIThreshold() to get the previously set value.
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the RSSIThreshold back to initial value
8. Unload wifihal module</automation_approch>
    <expected_output>Setting the Band Steering RSSI Threshold using the HAL API wifi_setBandSteeringRSSIThreshold() should be successful and the get value using wifi_getBandSteeringRSSIThreshold() should reflect the value set if the device is Band Steering capable for 6GHz. </expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetBandSteeringRSSIThreshold</test_script>
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
from tdkbVariables import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetBandSteeringRSSIThreshold');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetBandSteeringRSSIThreshold');

loadmodulestatus =obj.getLoadModuleResult();
sysutilmodulestatus =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysutilmodulestatus

if "SUCCESS" in (loadmodulestatus.upper() and sysutilmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
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
                print "\nStep 2 : Get initial value of RSSI Threshold";
                getMethod = "getBandSteeringRSSIThreshold"
                primitive = 'WIFIHAL_GetOrSetParamIntValue'
                radioIndex = idx;
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                if expectedresult in actualresult:
                    initGetValue = details.split(":")[1].strip();
                    tdkTestObj.setResultStatus("SUCCESS");

                    setMethod = "setBandSteeringRSSIThreshold"
                    radioIndex = idx;
                    primitive = 'WIFIHAL_GetOrSetParamIntValue'

                    #Get the Range of the value to set
                    print "\nStep 3 : Get the range of RSSI Threshold values for set";
                    tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
                    cmd = "sh %s/tdk_utility.sh parseConfigFile RSSI_RANGE" %TDK_PATH;
                    print cmd;
                    expectedresult="SUCCESS";
                    tdkTestObj1.addParameter("command", cmd);
                    tdkTestObj1.executeTestCase(expectedresult);
                    actualresult = tdkTestObj1.getResult();
                    details = tdkTestObj1.getResultDetails().strip();
                    Range = details.replace("\\n", "");

                    print "TEST STEP : Get the RSSI range value";
                    print "EXPECTED RESULT : Should Get RSSI range value";

                    if Range != ""  and (expectedresult in actualresult):
                        Range = Range.split(",");
                        tdkTestObj1.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT : The RSSI range value : %s" % Range;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"

                        #min_rssi and max_rssi are the random numbers range
                        #coeffecient gives whether the range is negative or positive
                        coeffecient = int (Range[2])
                        min_rssi= int (Range[0])
                        print"Minimum RSSI: ",min_rssi*coeffecient
                        max_rssi = int (Range[1])
                        print"Maximum RSSI: ", max_rssi*coeffecient
                        value= random.randint(min_rssi,max_rssi)
                        setValue = coeffecient* value
                        print"RSSI value to be set:",setValue

                        print "\nStep 4 : Set the RSSI Threshold to : %d" %setValue;
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                        if expectedresult in actualresult:
                            getMethod = "getBandSteeringRSSIThreshold"
                            radioIndex = idx;
                            primitive = 'WIFIHAL_GetOrSetParamIntValue'
                            print "\nStep 5 : Get the current value of RSSI Threshold";
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                finalGetValue = details.split(":")[1].strip()
                                print "\nStep 6 : Validating the set operation for RSSI Threshold";
                                print "TEST STEP: Comparing set and get values of RSSI Threshold"
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
                                print "getBandSteeringRSSIThreshold() call failed after set operation"

                            #Revert back to initial value
                            setMethod = "setBandSteeringRSSIThreshold"
                            primitive = 'WIFIHAL_GetOrSetParamIntValue'
                            setValue = int(initGetValue)
                            print "\nStep 7 : Reverting to initial RSSI Threshold value";
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "Successfully reverted back to inital value"
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Unable to revert to initial value"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "setBandSteeringRSSIThreshold() call failed"
                    else:
                        tdkTestObj1.setResultStatus("FAILURE");
                        print "ACTUAL RESULT : Failed to get  the RSSI range value";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "getBandSteeringRSSIThreshold() call failed"
            else:
                tdkTestObj.setResultStatus("SUCCESS");
                print "BandSteeringCapability is disabled"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "getBandSteeringCapability() call failed"

    obj.unloadModule("wifihal");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load modules";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");

