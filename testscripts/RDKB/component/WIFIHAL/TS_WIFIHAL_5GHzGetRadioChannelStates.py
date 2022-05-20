##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_WIFIHAL_5GHzGetRadioChannelStates</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioChannels</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRadioChannels() for 5G radio and check if a valid channel state is retrieved for each of the possible channels.</synopsis>
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
    <test_case_id>TC_WIFIHAL_797</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRadioChannels() for 5G radio and check if a valid channel state is retrieved for each of the possible channels.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioPossibleChannels()
wifi_getRadioChannels()</api_or_interface_used>
    <input_parameters>radioIndex : 5G radio index
numberOfChannels : number of channels retrieved from possible radio channels</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRadioPossibleChannels() for 5G radio to retrieve the possible radio channels.
3. Invoke the HAL API wifi_getRadioChannels() for 5G radio with the number of possible radio channels as input.
4. Check if the API invocation is success. If success, check if the channel state of each of the possible radio channels is any of the following states : {'1' : "CHAN_STATE_AVAILABLE", '2' : "CHAN_STATE_DFS_NOP_FINISHED", '3' : "CHAN_STATE_DFS_NOP_START", '4' : "CHAN_STATE_DFS_CAC_START", '5' : "CHAN_STATE_DFS_CAC_COMPLETED"}
5. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getRadioChannels() should be invoked successfully for 5G radio and the states of all possible radio channels for 5G radio should be a valid value from {'1' : "CHAN_STATE_AVAILABLE", '2' : "CHAN_STATE_DFS_NOP_FINISHED", '3' : "CHAN_STATE_DFS_NOP_START", '4' : "CHAN_STATE_DFS_CAC_START", '5' : "CHAN_STATE_DFS_CAC_COMPLETED"}.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioChannelStates</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioChannelStates');

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
        #Invoke the HAL API getRadioPossibleChannels
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1 : Invoke the HAL API wifi_getRadioPossibleChannels() to get the possible radio channels for 5G radio";
        print "EXPECTED RESULT 1 : The HAL API wifi_getRadioPossibleChannels() should be invoked successfully";

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API invocation is success; Details : %s" %(details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #get the possible channels as a list
            PossibleChannels = details.split(":")[1].split(",");
            print "Possible channels are : ", PossibleChannels;
            numOfChannels = len(PossibleChannels);
            print "Number of Channels : ", numOfChannels;

            #Invoke the HAL API getRadioChannels to get the Channel State
            tdkTestObj = obj.createTestStep("WIFIHAL_GetRadioChannels");
            tdkTestObj.addParameter("radioIndex",idx);
            tdkTestObj.addParameter("numberOfChannels",numOfChannels);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            chan_details = tdkTestObj.getResultDetails().strip("\\n");

            print "\nTEST STEP 2 : Invoke the HAL API wifi_getRadioChannels() to get the state of each of the possible radio channels";
            print "EXPECTED RESULT 2 : The HAL API wifi_getRadioChannels() should be invoked successfully";

            if expectedresult in actualresult and "Channel Details" in chan_details:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: %s" %(chan_details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Dictionary mapping of channel state
                channel_state_dict = {'1' : "CHAN_STATE_AVAILABLE", '2' : "CHAN_STATE_DFS_NOP_FINISHED", '3' : "CHAN_STATE_DFS_NOP_START", '4' : "CHAN_STATE_DFS_CAC_START", '5' : "CHAN_STATE_DFS_CAC_COMPLETED"};

                print "\nTEST STEP 3 : Check if the channel state details of all possible channels are received and if the states are valid";
                print "EXPECTED RESULT 3 : All possible channel state details should be retrieved and the states should be valid"

                success_flag = 0;

                for channel in PossibleChannels:
                    search_string = "Channel " + channel + " : ";

                    if search_string in chan_details :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "\nChannel State details of the channel %s is retrieved" %channel;
                        state = chan_details.split(search_string)[1].split(" ")[1];

                        if state in channel_state_dict :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            channel_state = channel_state_dict[state];
                            print "For Channel %s, the state is %s" %(channel, channel_state);
                        else :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            success_flag = 1;
                            channel_state = "Invalid";
                            print "For Channel %s, the state is %s" %(channel, channel_state);
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        success_flag = 1;
                        print "\nChannel State details of the channel %s is not retrieved" %channel;

                if success_flag == 0 :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 2: Channel state details of all possible channels are received and the states are valid";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 2: Channel state details of all possible channels are not received or the states are invalid";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: %s" %(chan_details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %(details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
