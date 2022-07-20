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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzSetRadioAutoChannelRefreshPeriod</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the auto channel refresh period if the automatic channel selection is enabled for 2.4GHz</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_109</test_case_id>
    <test_objective>To set the auto channel refresh period if the automatic channel selection is enabled for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioAutoChannelRefreshPeriodSupported
wifi_getRadioAutoChannelRefreshPeriod
wifi_setRadioAutoChannelRefreshPeriod
wifi_getRadioAutoChannelSupported
wifi_getRadioAutoChannelEnable
wifi_setRadioAutoChannelEnable
wifi_getRadioChannel
wifi_setRadioChannel
wifi_getRadioPossibleChannels</api_or_interface_used>
    <input_parameters>getRadioAutoChannelRefreshPeriodSupported
getRadioAutoChannelRefreshPeriod
setRadioAutoChannelRefreshPeriod
getRadioAutoChannelSupported
getRadioAutoChannelEnable
setRadioAutoChannelEnable
getRadioChannel
setRadioChannel
getRadioPossibleChannels
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get if auto channel selection is supported(getAutoChannelSupported)
3. If not supported, check if getAutoChannelEnable is false, if not return FAILURE
3. If supported, invoke "WIFIHAL_GetOrSetParamBoolValue" to get if auto channel selection is enabled (getAutoChannelEnable)
4. If not enabled, enable it using setAutoChannelEnable
4. Check if AutoChannelRefreshPeriod is supported, if yes get AutoChannelRefreshPeriod ,getRadioChannel,
5. Set AutoChannelRefreshPeriod to a value and get it , if both are same return SUCCESS
6. Sleep for the previously set refresh period.
7. Get the radio possible channels using wifi_getRadioPossibleChannels()
8. getRadioChannel and check if the channel returned is from the list of possible channels. If yes, return SUCCESS.
9. If not, return failure
10. Unload wifihal module</automation_approch>
    <except_output>Check points:
1. getRadioAutoChannelSupported should return true
2. getRadioAutoChannelEnable should be true, if not setRadioAutoChannelEnable should be made true
3. setRadioAutoChannelRefreshPeriod should be success
4. RadioChannel after the refresh period should be from the list of radio possible channels</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioAutoChannelRefreshPeriod</test_script>
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
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioAutoChannelRefreshPeriod');

def getRadioPossibleChannels(idx):
        print "*********************************************************";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        #Giving the method name to invoke the api for getting possible Radio Channel. ie,wifi_getRadioPossibleChannels()
        tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Get the possible Radio Channels for 2.4GHz";
            print "EXPECTED RESULT : Should get the possible Radio Channels for 2.4GHz";
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
            return PossibleChannels;
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the possible Radio Channels for 2.4GHz";
            print "EXPECTED RESULT : Should get the possible Radio Channels for 2.4GHz";
            print "ACTUAL RESULT : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
        print "*********************************************************";

def setandgetAutoChannelRefreshPeriod(radioIndex):

    #Giving the method name to invoke the api wifi_getRadioAutoChannelRefreshPeriodSupported()
    print "*********************************************************";
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    getMethod = "getAutoChannelRefreshPeriodSupported"
    expectedresult="SUCCESS";
   
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

    enable = details.split(":")[1].strip();
    if expectedresult in actualresult and "Enabled" in enable:      
	tdkTestObj.setResultStatus("SUCCESS");
        print "*********************************************************";
        print "AutoChannelRefreshPeriod is supported by this radio";
        #Giving the method name to invoke the api wifi_getRadioAutoChannelRefreshPeriod()
        primitive = 'WIFIHAL_GetOrSetParamULongValue'
        getMethod = "getAutoChannelRefreshPeriod"
        expectedresult="SUCCESS";
   	tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	if expectedresult in actualresult:
            initialRefreshPeriod = details.split(":")[1];
            print "InitialRefreshPeriod = ",initialRefreshPeriod;
	    if int(initialRefreshPeriod) == 0:
	        print "Automatic channel selection is done only at boot time"
		tdkTestObj.setResultStatus("SUCCESS");
	    else:
		tdkTestObj.setResultStatus("SUCCESS");
		print "*********************************************************";
                #Giving the method name to invoke the api wifi_getRadioChannel()
                primitive = 'WIFIHAL_GetOrSetParamULongValue'
        	getMethod = "getRadioChannel"
        	expectedresult="SUCCESS";
        	
		tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
		initialRadioChannel = details.split(":")[1].strip();
		print "InitialRadioChannel = ",initialRadioChannel;

		print "*********************************************************";
                #Giving the method name to invoke the api wifi_setRadioAutoChannelRefreshPeriod()
                primitive = 'WIFIHAL_GetOrSetParamULongValue'
        	setMethod = "setRadioAutoChannelRefreshPeriod"
        	expectedresult="SUCCESS";
        
		setRefreshPeriod = 600;
		tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setRefreshPeriod, setMethod)

                if expectedresult in actualresult:
        	        print "*********************************************************";
			tdkTestObj.setResultStatus("SUCCESS");
        		print "*********************************************************";
                        #Giving the method name to invoke the api wifi_getRadioAutoChannelRefreshPeriod()
		        primitive = 'WIFIHAL_GetOrSetParamULongValue'
		        getMethod = "getAutoChannelRefreshPeriod"
		        expectedresult="SUCCESS";
		        
			tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
  		        getRefreshPeriod = details.split(":")[1].strip();
		        print "getRefreshPeriod = " ,getRefreshPeriod;
		        print "setRefreshPeriod = ", setRefreshPeriod;
		        if expectedresult in actualresult and int(getRefreshPeriod) == setRefreshPeriod:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "EXPECTED RESULT: Get the auto channel refresh period and it equals setRefreshPeriod";
                            print "ACTUAL RESULT: Set and Get auto channel refresh period are equal";
			    print "TEST EXECUTION RESULT :SUCCESS";
		        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "EXPECTED RESULT: Get the auto channel refresh period and it equals setRefreshPeriod";
                            print "ACTUAL RESULT: Set and get auto channel refresh period are not equal";
			    print "TEST EXECUTION RESULT :FAILURE";
 
		        print "Going for a sleep of %s seconds"%setRefreshPeriod;
		        time.sleep(setRefreshPeriod);
		   
			print "*********************************************************";
                        #Giving the method name to invoke the api wifi_getRadioChannel()
	                primitive = 'WIFIHAL_GetOrSetParamULongValue'
         		getMethod = "getRadioChannel"
	        	expectedresult="SUCCESS";
        		
			tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                        finalRadioChannel = details.split(":")[1].strip();
		        print "finalRadioChannel =",finalRadioChannel;
                        PossibleChannels = getRadioPossibleChannels(idx);
                        if expectedresult in actualresult and int(finalRadioChannel) in PossibleChannels:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP : To get the currently used radio channel after the refresh period";
                            print "EXPECTED RESULT: The currently used radio channel should be from the list of RadioPossibleChannels";
                            print "ACTUAL RESULT: %s" %details;
			    print "TEST EXECUTION RESULT : SUCCESS"

			    #Reverting RadioChannel back to initial channel
                            #Script to load the configuration file of the component
	                    print "*********************************************************";
                            #Giving the method name to invoke the api wifi_setRadioChannel()
	                    primitive = 'WIFIHAL_GetOrSetParamULongValue'
         		    setMethod = "setRadioChannel"
	        	    expectedresult="SUCCESS";
        		    
			    setRadioCh = int(initialRadioChannel)
			    tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setRadioCh, setMethod)
           	            if expectedresult in actualresult:
				print "Successfully reverted the radio channel to initial channel"
				tdkTestObj.setResultStatus("SUCCESS");
        	            else:
				print "Unable to revert the radio channel to initial channel"
				tdkTestObj.setResultStatus("FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP : To get the currently used radio channel after the refresh period";
                            print "EXPECTED RESULT: The currently used radio channel should be from the list of RadioPossibleChannels";
                            print "ACTUAL RESULT: %s" %details;
                            print "TEST EXECUTION RESULT : FAILURE";

	                #Reverting the refresh period back to initial
                        #Giving the method name to invoke the api wifi_setRadioAutoChannelRefreshPeriod()
			print "*********************************************************";
	                primitive = 'WIFIHAL_GetOrSetParamULongValue'
        		setMethod = "setRadioAutoChannelRefreshPeriod"
        		expectedresult="SUCCESS";
			setRefreshPeriod = int(initialRefreshPeriod);
	        	
			tdkTestObj ,actualresult ,details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setRefreshPeriod, setMethod)
                        if expectedresult in actualresult:
                            print "Successfully reverted the auto channel refresh period back to initialRefreshPeriod";
			    tdkTestObj.setResultStatus("SUCCESS");
	                else:
                            print "Unable to revert the auto channel refresh period back to initialRefreshPeriod";
			    tdkTestObj.setResultStatus("FAILURE");
		else:
		    print "Set auto channel refresh period failed"
		    tdkTestObj.setResultStatus("FAILURE");
	else:
	    print "Get auto channel refresh period failed"
	    tdkTestObj.setResultStatus("FAILURE");

    elif expectedresult in actualresult and "Disabled" in enable:
	tdkTestObj.setResultStatus("SUCCESS");
	print "Auto channel refresh period not supported by this radio"

    else:
	tdkTestObj.setResultStatus("FAILURE");
	print "Getting Auto channel refresh period supported failed"

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

	    #Giving the method name to invoke the api wifi_getRadioAutoChannelSupported()
	    print "*********************************************************";
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    getMethod = "getAutoChannelSupported"
	    expectedresult="SUCCESS";
	    radioIndex = idx;
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	    autoChannelSupport = details.split(":")[1].strip();
	    print "AutoChannelSupport =" ,autoChannelSupport;
	    if expectedresult in actualresult and "Disabled" in autoChannelSupport:
		#Set the result status of execution
		tdkTestObj.setResultStatus("SUCCESS");
		print "Automatic channel selection is not supported by this radio";

		#Giving the method name to invoke the api wifi_getRadioAutoChannelEnable()
		print "*********************************************************";
		primitive = 'WIFIHAL_GetOrSetParamBoolValue'
		getMethod = "getAutoChannelEnable"
		expectedresult="SUCCESS";
		radioIndex = idx;
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
		enable = details.split(":")[1].strip();
		print "Auto channel enable status = " ,enable
		if expectedresult in actualresult and "Disabled" in enable:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "Auto channel enable returns false as AutoChannelSupported is false"
		else:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("FAILURE");
		    print "Auto channel enable returned true instead of false"

	    elif expectedresult in actualresult and "Enabled" in autoChannelSupport:
		tdkTestObj.setResultStatus("SUCCESS");
		print "Automatic channel selection is supported by this radio";

		#Giving the method name to invoke the api wifi_getRadioAutoChannelEnable()
		print "*********************************************************";
		primitive = 'WIFIHAL_GetOrSetParamBoolValue'
		getMethod = "getAutoChannelEnable"
		expectedresult="SUCCESS";
		radioIndex = idx;
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
		enable = details.split(":")[1].strip();
		print "Auto channel enable status = " ,enable
		if expectedresult in actualresult and "Enabled" in enable:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "Auto channel enable returned true"

		    setandgetAutoChannelRefreshPeriod(radioIndex);

		elif expectedresult in actualresult and "Disabled" in enable:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "Auto channel enable returned false"

		    print "*********************************************************";
		    #Giving the method name to invoke the api to set auto channel enable. ie,wifi_setRadioAutoChannelEnable()
		    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
		    setMethod = "setRadioAutoChannelEnable"
		    expectedresult="SUCCESS";
		    radioIndex = idx;
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 1, setMethod)
		    if expectedresult in actualresult:
			print "Auto channel enable set as true for 2.4GHz";

			#Giving the method name to invoke the api wifi_getRadioAutoChannelEnable()
			print "*********************************************************";
			primitive = 'WIFIHAL_GetOrSetParamBoolValue'
			getMethod = "getAutoChannelEnable"
			expectedresult="SUCCESS";
			radioIndex = idx;
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
			enable = details.split(":")[1].strip();
			if expectedresult in actualresult and "Enabled" in enable:
			    print "Auto channel Enabled"
			    tdkTestObj.setResultStatus("SUCCESS");

			    setandgetAutoChannelRefreshPeriod(radioIndex);

			else:
			    print "Unable to enable Auto channel"
			    tdkTestObj.setResultStatus("FAILURE");

		    else:
			print "Unable to set auto channel enable as true for 2.4GHz";
			tdkTestObj.setResultStatus("FAILURE");

	    else:
		#Set the result status of execution
		tdkTestObj.setResultStatus("FAILURE");
		print "getAutoChannelSupported() failed";

    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
