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
  <version>3</version>
  <name>TS_WIFIHAL_6GHzManualToAutoChannel</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To test if on enabling Auto Channel mode using wifi_setRadioAutoChannelEnable(), the manually set and get channel number is from the list of possible channels returned by wifi_getRadioPossibleChannels() api for 6GHz radio.</synopsis>
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
    <test_case_id>TC_WIFIHAL_688</test_case_id>
    <test_objective>To test if on enabling Auto Channel mode using wifi_setRadioAutoChannelEnable(), the manually set and get channel number is from the list of possible channels returned by wifi_getRadioPossibleChannels() api for 6GHz radio.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioAutoChannelEnable()
wifi_getRadioPossibleChannels()
wifi_getRadioChannel()
wifi_setRadioChannel()</api_or_interface_used>
    <input_parameters>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</input_parameters>
    <automation_approch>1. Load the modules.
2. Invoke the HAL API wifi_getRadioChannel() to get the current radio channel and store.
3. Then invoke the HAL API wifi_getRadioPossibleChannels() to get the possible channels for 6G radio and set a new channel from the list using the HAL API wifi_setRadioChannel().
4. Cross check if the new channel is set successfully with a get.
5. Set the AutoChannel enable using the HAL API wifi_getRadioAutoChannelEnable() and check if the SET reflected in the GET.
6. Now invoke wifi_getRadioChannel() and check if the current channel is a subset of the possible channels list.
7. Revert the radio channel to initial value
8. Unload the modules.</automation_approch>
    <expected_output>On enabling Auto Channel mode using wifi_setRadioAutoChannelEnable(), the manually set and get channel number should be from the list of possible channels returned by wifi_getRadioPossibleChannels() api for 6GHz radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzManualToAutoChannel</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

def get_function(tdkTestObj, idx, methodname):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("methodName",methodname);
    tdkTestObj.addParameter("radioIndex",idx);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return details, actualresult;

def set_function(tdkTestObj, idx, setValue, methodname):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("methodName",methodname);
    tdkTestObj.addParameter("radioIndex",idx);
    tdkTestObj.addParameter("param",setValue);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return details, actualresult;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from time import sleep;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzManualToAutoChannel');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the initial radio channel value
        step = 1;
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
        methodname = "getRadioChannel";
        details, actualresult = get_function(tdkTestObj, idx, methodname);

        print "\nTEST STEP %d : Invoke the HAL API wifi_getRadioChannel() to retrieve the current radio channel for 6G radio" %step;
        print "EXPECTED RESULT %d : The HAL API wifi_getRadioChannel() should be invoked successfully" %step;

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: API invocation success; Details : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            currentChannel = details.split(":")[1];
            if currentChannel != "" and currentChannel.isdigit():
                print "Current radio channel is : ", currentChannel;
                tdkTestObj.setResultStatus("SUCCESS");

                #Get the possible list of radio channels
                step = step + 1;
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP %d : Invoke the HAL API wifi_getRadioPossibleChannels() to get the possible radio channels for 6G radio" %step;
                print "EXPECTED RESULT %d : The HAL API wifi_getRadioPossibleChannels() should be invoked successfully" %step;

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: API invocation is success; Details : %s" %(step, details);
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

                        #Set new radio channel
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                        methodname = "setRadioChannel"
                        details, actualresult = set_function(tdkTestObj, idx, newChannel, methodname);

                        print "\nTEST STEP %d: Set new radio channel %s using the HAL API wifi_setRadioChannel() for 6G radio" %(step, newChannel);
                        print "EXPECTED RESULT %d: The HAL API wifi_setRadioChannel() should be invoked successfully" %step;

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: API invocation success; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Get the radio channel
                            sleep(10);
                            step = step + 1;
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                            methodname = "getRadioChannel";
                            details, actualresult = get_function(tdkTestObj, idx, methodname);

                            print "\nTEST STEP %d : Invoke the HAL API wifi_getRadioChannel() to retrieve the current radio channel for 6G radio" %step;
                            print "EXPECTED RESULT %d : The HAL API wifi_getRadioChannel() should be invoked successfully" %step;

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: API invocation success; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                getChannel = details.split(":")[1];
                                print "New radio channel set : ", newChannel;
                                print "New radio channel get : ", getChannel;

                                step = step + 1;
                                print "\nTEST STRP %d : Check if the radio channel GET matches with SET" %step;
                                print "EXPECTED RESULT %d : radio channel GET should match with the SET" %step;

                                if newChannel == int(getChannel):
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: The SET and GET values are the same" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Set AutoChannel enable to true
                                    step = step + 1;
                                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                                    setValue = 1;
                                    methodname = "setAutoChannelEnable"
                                    details, actualresult = set_function(tdkTestObj, idx, setValue, methodname);

                                    print "\nTEST STEP %d : Set the AutoChannel Enable to false using the HAL API wifi_setRadioAutoChannelEnable()" %step;
                                    print "EXPECTED RESULT %d : The HAL API should be invoked successfully" %step;

                                    if expectedresult in actualresult:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: SET operation is success; Details : %s" %(step, details);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";

                                        #cross check the SET with GET
                                        step = step + 1;
                                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                                        methodname = "getAutoChannelEnable";
                                        details, actualresult = get_function(tdkTestObj, idx, methodname);

                                        print "\nTEST STEP %d : Invoke the HAL API and get the AutoChannel Enable using the HAL API wifi_getRadioAutoChannelEnable()" %step;
                                        print "EXPECTED RESULT %d : The HAL API should be invoked successfully" %step;

                                        if expectedresult in actualresult:
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "ACTUAL RESULT %d: API invocation success; Details : %s" %(step, details);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : SUCCESS";

                                            if "Enabled" in details :
                                                print "Setting AutoChannel Enable to true is success and reflects in GET";
                                                tdkTestObj.setResultStatus("SUCCESS");

                                                #Get the radio channel
                                                sleep(10);
                                                step = step + 1;
                                                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                                                methodname = "getRadioChannel";
                                                details, actualresult = get_function(tdkTestObj, idx, methodname);

                                                print "\nTEST STEP %d : Invoke the HAL API wifi_getRadioChannel() to retrieve the current radio channel for 6G radio" %step;
                                                print "EXPECTED RESULT %d : The HAL API wifi_getRadioChannel() should be invoked successfully" %step;

                                                if expectedresult in actualresult:
                                                    #Set the result status of execution
                                                    tdkTestObj.setResultStatus("SUCCESS");
                                                    print "ACTUAL RESULT %d: API invocation success; Details : %s" %(step, details);
                                                    #Get the result of execution
                                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                                    ChannelAfterAuto = details.split(":")[1];
                                                    if ChannelAfterAuto != "" and ChannelAfterAuto.isdigit():
                                                        print "Current radio channel after Auto Channel is enabled is : ", ChannelAfterAuto;
                                                        tdkTestObj.setResultStatus("SUCCESS");

                                                        #Check if the channel is from the possible channel list
                                                        step = step + 1;
                                                        print "\nTEST STEP %d: Get the Radio channel for 6GHz and the channel should be from the list of Possible Channels" %step;
                                                        print "EXPECTED RESULT %d: Should get the Radio channel for 6GHz and the channel should be from the list of Possible Channels" %step;

                                                        if int(ChannelAfterAuto) in PossibleChannels:
                                                            #Set the result status of execution
                                                            tdkTestObj.setResultStatus("SUCCESS");
                                                            print "ACTUAL RESULT %d: The channel after enabling auto channel is from the possible channel list " %(step);
                                                            #Get the result of execution
                                                            print "[TEST EXECUTION RESULT] : SUCCESS";
                                                        else:
                                                            #Set the result status of execution
                                                            tdkTestObj.setResultStatus("FAILURE");
                                                            print "ACTUAL RESULT %d: The channel after enabling auto channel is NOT from the possible channel list " %(step);
                                                            #Get the result of execution
                                                            print "[TEST EXECUTION RESULT] : FAILURE";
                                                    else:
                                                        print "Current radio channel is empty or invalid: ", currentChannel;
                                                        tdkTestObj.setResultStatus("FAILURE");
                                                else:
                                                    #Set the result status of execution
                                                    tdkTestObj.setResultStatus("FAILURE");
                                                    print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
                                                    #Get the result of execution
                                                    print "[TEST EXECUTION RESULT] : FAILURE";
                                            else :
                                                print "Set operation does not reflect in GET";
                                                tdkTestObj.setResultStatus("FAILURE");
                                        else:
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : FAILURE";
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: SET operation failed; Details : %s" %(step, details);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: The SET and GET values are NOT the same" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

                            #Revert the radio channel
                            step = step + 1;
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                            methodname = "setRadioChannel"
                            details, actualresult = set_function(tdkTestObj, idx, int(currentChannel), methodname);
                            sleep(10);

                            print "\nTEST STEP %d: Revert radio channel to %s using the HAL API wifi_setRadioChannel() for 6G radio" %(step, currentChannel);
                            print "EXPECTED RESULT %d: The HAL API wifi_setRadioChannel() should be invoked successfully" %step;

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: API invocation success; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "\nNo new channel to be set from the values in possible channels list";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Current radio channel is empty or invalid: ", currentChannel;
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: API invocation failed; Details : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");

