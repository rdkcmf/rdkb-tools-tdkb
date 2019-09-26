##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_5GHZ_SetRadioChannel</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test to manually set channel value using an entry from PossibleChannels list</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_36</test_case_id>
    <test_objective>Test to manually set channel value using an entry from PossibleChannels list</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get
WIFIAgent_Set</api_or_interface_used>
    <input_parameters>Device.WiFi.Radio.2.PossibleChannels
Device.WiFi.Radio.2.Channel</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Using WIFIAgent_Get, get and save the value of Device.WiFi.Radio.2.Channel 
3. Using WIFIAgent_Get, get Device.WiFi.Radio.2.PossibleChannels
4. Using WIFIAgent_Set, set a value to Device.WiFi.Radio.2.Channel from possible channel list
5. Using WIFIAgent_Get, verify the set operation
6. Restore values of Device.WiFi.Radio.2.Channel
7. Unload wifiagent module</automation_approch>
    <except_output>Manual setting of channel value using an entry from possibleChannels list should be success</except_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHZ_SetChannel</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHZ_SetRadioChannel');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #get the list of possible channels
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.PossibleChannels")
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    possChannels = details.split("VALUE:")[1].split(' ')[0].split(',');

    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of possible channles"
        print "EXPECTED RESULT 1: Should get the list of possible channles"
        print "ACTUAL RESULT 1: channel list is %s " %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #get the current channel and save it
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Channel")
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        currChannel = details.split("VALUE:")[1].split(' ')[0]

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the current channel"
            print "EXPECTED RESULT 1: Should get the current channel"
            print "ACTUAL RESULT 1: Channel is %s " %details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #set a new channel value manually from possible list
            for index in range(len(possChannels)):
                if possChannels[index] != currChannel:
                    channel = possChannels[index] ;
                    break;
	    #this function will set a value and do a get to see if set was success
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Channel")
            tdkTestObj.addParameter("paramValue",channel)
            tdkTestObj.addParameter("paramType","unsignedint")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

	    time.sleep(5);
            #get the current channel and compare it the set value
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Channel")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult2 = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            newChannel = details.split("VALUE:")[1].split(' ')[0]

            if expectedresult in actualresult1 and expectedresult in actualresult2 and newChannel == channel :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Set the current channel and verify using get"
                print "EXPECTED RESULT 1: Should set the current channel and verify using get"
                print "ACTUAL RESULT 1: Channel is %s " %details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #set the channel value to previous one
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Channel")
                tdkTestObj.addParameter("paramValue",currChannel)
                tdkTestObj.addParameter("paramType","unsignedint")
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 1: Set channel value to orginal one"
                    print "EXPECTED RESULT 1: should set channel value to orginal one"
                    print "ACTUAL RESULT 1:  %s " %details
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 1: Set channel value to orginal one"
                    print "EXPECTED RESULT 1: should set channel value to orginal one"
                    print "ACTUAL RESULT 1:  %s " %details
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Set the current channel and verify using get"
                print "EXPECTED RESULT 1: Should set the current channel and verify using get"
                print "ACTUAL RESULT 1: Channel is %s " %details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

