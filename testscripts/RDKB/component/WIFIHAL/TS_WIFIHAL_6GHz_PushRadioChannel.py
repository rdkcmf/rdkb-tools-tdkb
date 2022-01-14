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
  <name>TS_WIFIHAL_6GHz_PushRadioChannel</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_pushRadioChannel() to set a new radio channel from a list of possible channels and cross checking whether the new channel is reflected in wifi_getRadioChannel().</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_722</test_case_id>
    <test_objective>Invoke the HAL API wifi_pushRadioChannel() to set a new radio channel from a list of possible channels and cross checking whether the new channel is reflected in wifi_getRadioChannel().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioChannel()
wifi_pushRadioChannel()
wifi_getRadioPossibleChannels()</api_or_interface_used>
    <input_parameters>methodname : getRadioChannel
methodname : pushRadioChannel
methodname : getRadioPossibleChannels
radioIndex : 6G radio index
param : newChannel</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Invoke the HAL API wifi_getRadioChannel() to get the current radio channel for 6G radio
3. Invoke the HAL API wifi_getRadioPossibleChannels() to retrieve the possible radio channels supported for 6G radio and chose a channel different from the initial radio channel.
4. Push the newly selected radio channel using the HAL API wifi_pushRadioChannel() and check if the API returns success.
5. Cross check if the radio channel is pushed successfully using the get API wifi_getRadioChannel().
6. Revert to initial radio channel
7. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_pushRadioChannel() should successfully set a new radio channel from a list of possible channels and the set should reflect in wifi_getRadioChannel() for 6G radio..</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHz_PushRadioChannel</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

radio = "6G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHz_PushRadioChannel');

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

        print "\nTEST STEP 1: Get the current radio channel for 6GHz using the HAL API wifi_getRadioChannel()";
        print "EXPECTED RESULT 1: Should get the current channel for 6GHz using the HAL API wifi_getRadioChannel()";

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API invocation was success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            currentChannel = details.split(":")[1].strip();

            if currentChannel != "" and currentChannel.isdigit():
                print "Current radio channel is : ", currentChannel;
                tdkTestObj.setResultStatus("SUCCESS");

                #Get the possible list of radio channels
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 2 : Invoke the HAL API wifi_getRadioPossibleChannels() to get the possible radio channels for 6G radio";
                print "EXPECTED RESULT 2 : The HAL API wifi_getRadioPossibleChannels() should be invoked successfully";

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 2: API invocation is success; Details : %s" %(details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #if possible channels are given as a range eg: 1-11
                    if "-" in details:
                        #get the possible channels as a list of integers
                        PossibleChannelRange = [int(x) for x in details.split(":")[1].split("-")];
                        PossibleChannels = range(PossibleChannelRange[0],PossibleChannelRange[1]+1);
                        print "Possible channels are ", PossibleChannels;
                    #if possible channels are given as values eg:1,2,3,4,5
                    else:
                        #get the possible channels as a list of integers
                        PossibleChannels = [int(x) for x in details.split(":")[1].split(",")];
                        print "Possible channels are ", PossibleChannels;

                    #select a channel from possible channels which is not the current channel
                    newChannel = -1;
                    for channel in PossibleChannels:
                        if channel != int(currentChannel):
                            newChannel= channel;
                            break;

                    if newChannel != -1:
                        print "\nNew channel to set is ", newChannel;
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Push the new radio channel
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                        tdkTestObj.addParameter("param",newChannel);
                        tdkTestObj.addParameter("radioIndex",idx);
                        tdkTestObj.addParameter("methodName","pushRadioChannel");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print "\nTEST STEP 3: Set the radio channel using wifi_pushRadioChannel()";
                        print "EXPECTED RESULT 3: Should set the radio channel using wifi_pushRadioChannel()";

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 3: API invocation success; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            time.sleep(10);

                            #Cross check the Push radio channel with get radio channel
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                            tdkTestObj.addParameter("methodName","getRadioChannel");
                            tdkTestObj.addParameter("radioIndex",idx);
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            print "\nTEST STEP 4: Get the radio channel for 6GHz using the HAL API wifi_getRadioChannel() after Push Radio Channel operation";
                            print "EXPECTED RESULT 4: Should get the radio channel for 6GHz using the HAL API wifi_getRadioChannel()";

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 4: API invocation was success; Details : %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                newValue = details.split(":")[1].strip()

                                print "\nTEST STEP 5: Verify the wifi_pushRadioChannel() with wifi_getrAdioChannel() for 6G radio";
                                print "EXPECTED RESULT 5: The radio channel get should be same as the radio channel pushed";
                                print "Radio Channel set : %d" %newChannel;
                                print "Radio Channel get : %s" %newValue;

                                if newValue.isdigit() and int(newValue) == int(newChannel):
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 5: SET matches with the GET";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 5: Values do not match";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 4: API invocation failed; Details : %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

                            #Revert the channel value
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                            tdkTestObj.addParameter("param",int(currentChannel));
                            tdkTestObj.addParameter("radioIndex",idx);
                            tdkTestObj.addParameter("methodName","pushRadioChannel");
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "Successfully reverted to the initial radio channel : ", currentChannel;
                            else :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Not reverted to the initial radio channel : ", currentChannel;
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 3: API invocation success; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "\nNo new channel to be set from the values in possible channels list";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 2: API invocation failed; Details : %s" %(details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Current radio channel is empty or invalid: ", currentChannel;
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    tdkTestObj.setResultStatus("FAILURE");
    print "Module loading failed";
