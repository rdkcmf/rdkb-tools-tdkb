##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WIFIHAL_5GHzPushRadioChannel2</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_PushRadioChannel2</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>This HAL API is used to change the channel to destination channel, with destination bandwidth for 5GHZ.</synopsis>
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
    <test_case_id>TC_WIFIHAL_304</test_case_id>
    <test_objective>This HAL API is used to change the channel to destination channel, with destination bandwidth for 5GHZ.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_pushRadioChannel2()</api_or_interface_used>
    <input_parameters>channel = 44
channel_width_MHz = 80
csa_beacon_count=25
radioIndex = 1</input_parameters>
    <automation_approch>1.Load the module
2.Get the value of radio channel of 5GHZ and save
3. Change the channel using wifi_pushRadioChannel2 () and validate
4. Revert the channel value
5.Unload the module.</automation_approch>
    <except_output>The Channel should change to set value for 5GHZ</except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPushRadioChannel2</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPushRadioChannel2');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
            tdkTestObj.addParameter("methodName","getRadioChannel");
            tdkTestObj.addParameter("radioIndex",idx);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Get the current radio channel for 5GHz";
                print "EXPECTED RESULT 1: Should get the current channel for 5GHz";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                currChannel = details.split(":")[1].strip()

                if int(currChannel) == 44:
                    newChannel = 36;
                else:
                    newChannel = 44;

                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                tdkTestObj.addParameter("methodName","getChannelBandwidth");
                tdkTestObj.addParameter("radioIndex",idx);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Get the current bandwidth for 5GHz";
                    print "EXPECTED RESULT 2: Should get the bandwidth for 5GHz";
                    print "ACTUAL RESULT 2: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    currBandwidth = details.split(":")[1];
                    currBandwidth = currBandwidth.split("MHz")[0].strip();
                    tdkTestObj = obj.createTestStep("WIFIHAL_PushRadioChannel2");
                    tdkTestObj.addParameter("channel",newChannel);
                    tdkTestObj.addParameter("channel_width_MHz",80);
                    tdkTestObj.addParameter("csa_beacon_count",25);
                    tdkTestObj.addParameter("radioIndex", idx);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 2: Set the radio channel using wifi_pushRadioChannel2";
                        print "EXPECTED RESULT 2: Should set the radio channel using wifi_pushRadioChannel2";
                        print "ACTUAL RESULT 2: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        time.sleep(10);

                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                        tdkTestObj.addParameter("methodName","getRadioChannel");
                        tdkTestObj.addParameter("radioIndex", idx);
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            newValue = details.split(":")[1].strip()
                            if int(newValue) == int(newChannel):
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 3: Verify the set function using get function";
                                print "EXPECTED RESULT 3: Should get the current channel for 5GHz";
                                print "ACTUAL RESULT 3: %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 3: Verify the set function using get function";
                                print "EXPECTED RESULT 3: Should get the current channel for 5GHz";
                                print "ACTUAL RESULT 3: %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        #Revert the channel value
                        tdkTestObj = obj.createTestStep("WIFIHAL_PushRadioChannel2");
                        tdkTestObj.addParameter("channel",int(currChannel));
                        tdkTestObj.addParameter("channel_width_MHz",int(currBandwidth));
                        tdkTestObj.addParameter("csa_beacon_count",25);
                        tdkTestObj.addParameter("radioIndex", idx);
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP : Revert the radio channel using wifi_pushRadioChannel2";
                            print "EXPECTED RESULT : Should revert the radio channel using wifi_pushRadioChannel2";
                            print "ACTUAL RESULT : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP : Revert the radio channel using wifi_pushRadioChannel2";
                            print "EXPECTED RESULT : Should revert the radio channel using wifi_pushRadioChannel2";
                            print "ACTUAL RESULT : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 2: Set the radio channel using wifi_pushRadioChannel2";
                        print "EXPECTED RESULT 2: Should the radio channel using wifi_pushRadioChannel2";
                        print "ACTUAL RESULT 2: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Get the current bandwidth for 5GHz";
                    print "EXPECTED RESULT 2: Should get the bandwidth for 5GHz";
                    print "ACTUAL RESULT 2: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Get the SSID Enable status for 5GHz";
                print "EXPECTED RESULT 1: Should get SSID enable status for 5GHz";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
