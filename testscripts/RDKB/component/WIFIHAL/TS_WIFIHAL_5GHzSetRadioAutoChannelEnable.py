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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetRadioAutoChannelEnable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test to enable/disable Auto Channel Enable enable status</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_525</test_case_id>
    <test_objective>Test to enable/disable AutoChannel enable status </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioAutoChannelEnable()
wifi_getRadioAutoChannelEnable()
wifi_getRadioChannel
wifi_setRadioChannel
wifi_getRadioPossibleChannels</api_or_interface_used>
    <input_parameters>methodname : getRadioAutoChannelEnable
methodname : setRadioAutoChannelEnable
methodname : getRadioChannel
methodname : setRadioChannel
methodname : getRdioPossibleChannels
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamBoolValue" to get if auto channel selection is enabled (getAutoChannelEnable)
3. If enabled, invoke getradiochannel(), getradiopossiblechannels() and set a new radiochannel with setradiochannel() api.
4. After that check if AutoChannelEnable toggled to false. Else return failure.
5. If initially, AutoChannelEnable is disabled, invoke setAutoChannelEnable() and set to true. If set operation fails, return failure.
6. Revert to initial values for AutoChannelEnable
7. Unload wifihal module</automation_approch>
    <expected_output>Should be able to toggle AutoChannelEnable</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioAutoChannelEnable</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def getchannel(index,obj) :
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
    #Giving the method name to invoke the api for getting Radio channel. ie,wifi_getRadioChannel()
    tdkTestObj.addParameter("methodName","getRadioChannel");
    tdkTestObj.addParameter("radioIndex",index);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    currentChannel = 0
    if expectedresult in actualresult :
        currentChannel = details.split(":")[1];
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Get the Radio channel for 5GHz";
        print "EXPECTED RESULT : Should get the Radio channel for 5GHz";
        print "ACTUAL RESULT : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        return currentChannel;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Get the Radio channel for 5GHz";
        print "EXPECTED RESULT : Should get the Radio channel for 5GHz";
        print "ACTUAL RESULT : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        return currentChannel;

def getpossiblechanneltoset(index,currentChannel,obj) :
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
    #Giving the method name to invoke the api for getting possible Radio Channel. ie,wifi_getRadioPossibleChannels()
    tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
    tdkTestObj.addParameter("radioIndex",index);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    newChannel = 0
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Get the possible Radio Channels for 5GHz";
        print "EXPECTED RESULT : Should get the possible Radio Channels for 5GHz";
        print "ACTUAL RESULT : %s" %details;
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
        for channel in PossibleChannels:
            if channel != int(currentChannel):
                newChannel= channel;
                break;
        print "New channel to set is ", newChannel;
        return newChannel;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 2: Get the possible Radio Channels for 5GHz";
        print "EXPECTED RESULT 2: Should get the possible Radio Channels for 5GHz";
        print "ACTUAL RESULT 2: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        return newChannel;

def setnewchannel(index, newChannel, obj):
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
    #Giving the method name to invoke the api for getting Radio Channel. ie,wifi_setRadioChannel()
    tdkTestObj.addParameter("methodName","setRadioChannel");
    tdkTestObj.addParameter("radioIndex",index);
    tdkTestObj.addParameter("param",newChannel);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 3: Set new Radio channel for 5GHz";
        print "EXPECTED RESULT 3: Should  set the new Radio channel for 5GHz";
        print "ACTUAL RESULT 3: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        return 1
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 3: Set new Radio channel for 5GHz";
        print "EXPECTED RESULT 3: Should  set the new Radio channel for 5GHz";
        print "ACTUAL RESULT 3: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        return 0

def revert(newEnable,index,obj) :
    #Revert Operation for AutoChannelEnable
    if newEnable == 1 :
        #If newEnable is True, set the radiochannel to a new channel and then check if AutoChannelEnable is false
        print "Revert AutoChannelEnable to False"
        currentChannel = getchannel(index,obj);
        newChannel = getpossiblechanneltoset(index,currentChannel,obj);
        newchanset = setnewchannel(index, newChannel, obj);
        if newchanset == 1 :
            getMethod = "getAutoChannelEnable"
            primitive = 'WIFIHAL_GetOrSetParamBoolValue'
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
            expectedresult="SUCCESS";
            print "TEST STEP : Get AutoChannelEnable value after setRadioChannel operation"
            print "EXPECTED RESULT: Should successfully get the AutoChannelEnable"
            print "ACTUAL RESULT: getAutoChannelEnable : %s"%details;
            if expectedresult in actualresult and currEnable == details.split(":")[1].strip() :
                print "AutoChannelEnable reverted Successfully";
                tdkTestObj.setResultStatus("SUCCESS");
            else :
                print "AutoChannelEnable did not revert Successfully"
                tdkTestObj.setResultStatus("FAILURE");
        else :
            print "Radio Channel did not change after the set operation";
            tdkTestObj.setResultStatus("FAILURE");
    else :
        #If newEnable is false, directly toggle the AutoChannelEnable to true
        print "Revert AutoChannelEnable to True"
        setMethod = "setRadioAutoChannelEnable"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, oldEnable, setMethod)
        expectedresult="SUCCESS";
        print "TEST STEP : Get AutoChannelEnable value after set operation"
        print "EXPECTED RESULT: Should successfully get the AutoChannelEnable"
        print "ACTUAL RESULT: getAutoChannelEnable : %s"%details;
        if expectedresult in actualresult :
            getMethod = "getAutoChannelEnable"
            primitive = 'WIFIHAL_GetOrSetParamBoolValue'
            sleep(5);
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
            expectedresult="SUCCESS";
            print "TEST STEP : Get AutoChannelEnable value after set operation"
            print "EXPECTED RESULT: Should successfully get the AutoChannelEnable"
            print "ACTUAL RESULT: getAutoChannelEnable : %s"%details;
            if expectedresult in actualresult and currEnable == details.split(":")[1].strip() :
                print "AutoChannelEnable toggled Successfully to True";
                tdkTestObj.setResultStatus("SUCCESS");
            else :
                print "AutoChannelEnable did not toggle Successfully to True"
                tdkTestObj.setResultStatus("FAILURE");

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio = "5G"

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioAutoChannelEnable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        radioIndex = idx
        getMethod = "getAutoChannelEnable"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
        expectedresult="SUCCESS";
        if expectedresult in actualresult :
            print "TEST STEP 1: Get AutoChannelEnable value"
            print "EXPECTED RESULT 1: Should successfully get the AutoChannelEnable"
            print "ACTUAL RESULT 1: getAutoChannelEnable : %s"%details;
            print "[TEST EXECUTION RESULT]: SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");
            currEnable = details.split(":")[1].strip()
            if "Enabled" in currEnable:
                oldEnable = 1
                newEnable = 0
                #If oldEnable is true, set the radiochannel to a new channel and then check if AutoChannelEnable is false
                print "Initially AutoChannelEnable is Enabled"
                print "Set radio channel to a new channel to toggle to false"
                currentChannel = getchannel(idx,obj);
                newChannel = getpossiblechanneltoset(idx,currentChannel,obj);
                newchanset = setnewchannel(idx, newChannel,obj);
                if newchanset == 1 :
                   getMethod = "getAutoChannelEnable"
                   primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                   tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                   expectedresult="SUCCESS";
                   print "Radio Channel is changed successfully"
                   print "TEST STEP 2: Get AutoChannelEnable value after setRadioChannel operation"
                   print "EXPECTED RESULT 2: Should successfully get the AutoChannelEnable"
                   if expectedresult in actualresult :
                       print "ACTUAL RESULT 2: getAutoChannelEnable : %s"%details;
                       print "[TEST EXECUTION RESULT]: SUCCESS"
                       tdkTestObj.setResultStatus("SUCCESS");
                       if currEnable not in details.split(":")[1].strip() :
                           print "AutoChannelEnable toggled Successfully to false";
                           tdkTestObj.setResultStatus("SUCCESS");
                           #Revert to initial value
                           revert(newEnable,idx,obj);
                       else :
                           print "AutoChannelEnable did not toggle Successfully to false"
                           tdkTestObj.setResultStatus("FAILURE");
                   else :
                       print "ACTUAL RESULT 2: getAutoChannelEnable : %s"%details;
                       print "[TEST EXECUTION RESULT]: FAILURE"
                       tdkTestObj.setResultStatus("FAILURE");
                else :
                   print "Radio Channel is not changed successfully"
            else :
               oldEnable = 0
               newEnable = 1
               #If oldEnable is false, directly toggle the AutoChannelEnable to true
               print "Initially AutoChannelEnable is Disabled"
               setMethod = "setRadioAutoChannelEnable"
               tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, setMethod)
               expectedresult="SUCCESS";
               print "TEST STEP 2 : Get AutoChannelEnable value after set operation"
               print "EXPECTED RESULT 2: Should successfully get the AutoChannelEnable"
               if expectedresult in actualresult :
                   print "ACTUAL RESULT 2: getAutoChannelEnable : %s"%details;
                   print "[TEST EXECUTION RESULT]: SUCCESS"
                   tdkTestObj.setResultStatus("SUCCESS");
                   getMethod = "getAutoChannelEnable"
                   primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                   sleep(5);
                   tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                   expectedresult="SUCCESS";
                   print "TEST STEP 3: Get AutoChannelEnable value after set operation"
                   print "EXPECTED RESULT 3: Should successfully get the AutoChannelEnable"
                   if expectedresult in actualresult :
                       print "ACTUAL RESULT 3: getAutoChannelEnable : %s"%details;
                       print "[TEST EXCEUTON RESULT]: SUCCESS"
                       tdkTestObj.setResultStatus("SUCCESS");
                       if currEnable not in details.split(":")[1].strip() :
                           print "AutoChannelEnable toggled Successfully to True";
                           tdkTestObj.setResultStatus("SUCCESS");
                           #Revert to initial value
                           revert(newEnable, idx, obj);
                       else :
                           print "AutoChannelEnable did not toggle Successfully to True"
                           tdkTestObj.setResultStatus("FAILURE");
                   else :
                       print "ACTUAL RESULT 3: getAutoChannelEnable : %s"%details;
                       print "[TEST EXCEUTON RESULT]: FAILURE"
                       tdkTestObj.setResultStatus("FAILURE");
               else :
                   print "ACTUAL RESULT 2: getAutoChannelEnable : %s"%details;
                   print "[TEST EXECUTION RESULT]: FAILURE"
                   tdkTestObj.setResultStatus("FAILURE");
        else :
            print "TEST STEP 1: Get AutoChannelEnable value"
            print "EXPECTED RESULT 1: Should successfully get the AutoChannelEnable"
            print "ACTUAL RESULT 1: getAutoChannelEnable : %s"%details;
            print "[TEST EXECUTION RESULT]: FAILURE"
            tdkTestObj.setResultStatus("FAILURE");
        obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

