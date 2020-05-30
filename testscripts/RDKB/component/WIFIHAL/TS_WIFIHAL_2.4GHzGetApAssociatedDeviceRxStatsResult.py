##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzGetApAssociatedDeviceRxStatsResult</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceRxStatsResult</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the WIFI HAL API wifi_getApAssociatedDeviceRxStatsResult for 2.4GHz AP</synopsis>
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
    <test_case_id>TC_WIFIHAL_366</test_case_id>
    <test_objective>To validate the WiFI HAL API wifi_getApAssociatedDeviceRxStatsResult for the 2.4GHz AP</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WiFI Client should be connected</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceRxStatsResult(), wifi_getApNumDevicesAssociated()</api_or_interface_used>
    <input_parameters>radioIndex - 2.4GHz radioIndex value
MAC - Associated Device MAC Address</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using "WIFIHAL_GetOrSetParamBoolValue" invoke wifi_getRadioStatsEnable to get the current RadioStatsEnable Value
3. If RadioStats is "Disabled" then using "WIFIHAL_GetOrSetParamBoolValue" invoke wifi_setRadioStatsEnable to enable it since its pre-requisite to get ApAssociatedDeviceRxStats value. If its "Enabled" by default then proceed to step 5
4. Using "WIFIHAL_GetOrSetParamBoolValue" invoke wifi_getRadioStatsEnable to confirm RadioStat is Enabled, if Enabled Proceed to next step else return FAILURE
5. Using "WIFIHAL_GetApNumDeviesAssociated" invoke wifi_getApNumDevicesAssociated() to get the assoiated devices MAC address If available proceed to next step, else return FAILURE and exit.
6. Using "WIFIHAL_GetApAssociatedDeviceRxStatsResult" invoke wifi_getApAssociatedDeviceRxStatsResult() to get the associated Device RxStats values.
7. Revert the RadioStatsEnable Value if its changed in step 3
8. Unload wifihal module</automation_approch>
    <expected_output>AP associated device RX stats should be return from HAL</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAssociatedDeviceRxStatsResult</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import re;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAssociatedDeviceRxStatsResult');

radio = "2.4G"

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

def getRadioStatsEnable(radioIndex):
    getMethod = "getRadioStatsEnable"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    radio_stat = details.split(":")[1].strip();
    return tdkTestObj,actualresult,radio_stat

def setRadioStatsEnable(radioIndex,value_to_set):
    setMethod = "setRadioStatsEnable"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, value_to_set, setMethod)
    return tdkTestObj,actualresult,details

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        radioIndex = idx;
        expectedresult="SUCCESS";
        radioStatEnable = 0;
        revertFlag = 0;

        #Get Initial RadioStatEnable value
	tdkTestObj,initial_result,initial_stat = getRadioStatsEnable(radioIndex);

	if expectedresult in initial_result:
            #Skipped Logging in STEP1, STEP2 and STEP3 (getRadioStatsEnable and setRadioStatsEnable) since its already handled in ExecuteWIFIHalCallMethod
	    print "TEST STEP 1: Successfully got the Radio stat enable value %s"%initial_stat

	    if initial_stat =="Disabled":
   	        #Enable the RadioStat value which is prerequisite to get the ApAssoiatedDeviceRxStatsResult
	        value_to_set = 1;
                tdkTestObj,setresult,setdetails = setRadioStatsEnable(radioIndex,value_to_set);

                if expectedresult in setresult:
		    #Making the revert flag as 1 only if setRadioStatEnable is success
		    revertFlag = 1;
	            print "TEST STEP 2: Successfully set the Radio Stat value to Enabled"
	            tdkTestObj,getresult,getdetails = getRadioStatsEnable(radioIndex);

                    if expectedresult in getresult and getdetails == "Enabled":
			#Making radioStatEnable flag as 1 after verified with get method
			radioStatEnable = 1;
		        print "TEST STEP 3: Radio Stat value is Enabled and Verified it with Get method, Details %s"%getdetails

                    else:
			radioStatEnable = 0;
		        print "TEST STEP 3: Failed to verify the Radio Stat value with Get call"
                else:
                    radioStatEnable = 0;
	            print "TEST STEP 2: Failed to set the Radio Stat value to Enabled"
	    else:
                radioStatEnable = 1;
                print "RadioStat is Already Enabled"

	    if radioStatEnable == 1:
	        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDevice');
		tdkTestObj.addParameter("apIndex",int(radioIndex));
		expectedresult="SUCCESS";
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		details = tdkTestObj.getResultDetails();
		print "Entire Details:",details;

            	if expectedresult in actualresult:
	     	    outputList = details.split("=")[1].strip()
		    if "," in outputList:
		        outputValue = outputList.split(",")[0].strip()
		    else:
			outputValue = outputList.split(":Value")[0].strip()

                    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 4: Get the Associated device MAC device"
		    print "EXPECTED RESULT 4: Should get the associated device MAC address"
		    print "ACTUAL RESULT 4: Associated Device's MAC address:",outputValue
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : SUCCESS";

        	    #check if outputvalue is a MAC address
		    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", outputValue.lower()):
		    	#Primitive test case which is associated to this Script
		    	tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceRxStatsResult');
		    	print "MAC address is %s"%outputValue
		    	tdkTestObj.addParameter("radioIndex", int(radioIndex));
		    	tdkTestObj.addParameter("MAC", outputValue);
		    	expectedresult="SUCCESS";
		    	tdkTestObj.executeTestCase(expectedresult);
		    	actualresult = tdkTestObj.getResult();
		   	details = tdkTestObj.getResultDetails();
		    	print"details",details;
		    	if expectedresult in actualresult :
		    	    tdkTestObj.setResultStatus("SUCCESS");
		   	    print "TEST STEP 5: Get the ApAssociatedDeviceRxStatsResult"
		            print "EXPECTED RESULT 5: Should successfully get the ApAssociatedDeviceRxStatsResult"
		    	    print "ACTUAL RESULT 5: Successfully gets the ApAssociatedDeviceRxStatsResult"
			    #Get the result of execution
			    print "[TEST EXECUTION RESULT] : SUCCESS";
		    	    print "Details: "
		    	    detailList = details.split(",")
		    	    output_array_size = details.split("=")
		    	    for i in detailList:
			        print i;
			    	print "output_array_size=",output_array_size
			    	print "Identified %s neighboring access points"%output_array_size
			    	#Get the result of execution
			   	print "[TEST EXECUTION RESULT] : SUCCESS";
		    	else:
		    	    tdkTestObj.setResultStatus("FAILURE");
		   	    print "TEST STEP 5: Get the ApAssociatedDeviceRxStatsResult"
		            print "EXPECTED RESULT 5: Should successfully get the ApAssociatedDeviceRxStatsResult"
		    	    print "ACTUAL RESULT 5: Failed to get the ApAssociatedDeviceRxStatsResult"
			    #Get the result of execution
			    print "[TEST EXECUTION RESULT] : FAILURE";
		    else:
                        tdkTestObj.setResultStatus("FAILURE");
		    	print "wifi_getApAssociatedDevice didn't return a proper MAC address in response - prerequisite is not met to get ApAssociatedDeviceRxStatsResult"
		else:
                    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 4: Get the Associated device MAC device"
		    print "EXPECTED RESULT 4: Should get the associated device MAC address"
		    print "ACTUAL RESULT 4: Failed to get Associated Device MAC address"
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
                tdkTestObj.setResultStatus("FAILURE");
	        print "Radio Stat was not enabled which is pre_requisite is get the RxStatsResult"

	#Revert the value only if setRadioStat in Step 2 was success
	if revertFlag == 1:
            tdkTestObj,setresult,setdetails = setRadioStatsEnable(radioIndex,value_to_set);
	    if expectedresult in setresult:
            	tdkTestObj.setResultStatus("SUCCESS");
           	print "TEST STEP 6: Revert the Radio Stat value"
	        print "EXPECTED RESULT 6: Should Revert the Radio Stat value"
	        print "ACTUAL RESULT 6: Successfully Reverted the Radio Stat value"
           	#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 6: Revert the Radio Stat value"
	        print "EXPECTED RESULT 6: Should Revert the Radio Stat value"
	        print "ACTUAL RESULT 6: Failed to Revert the Radio Stat value"
           	#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    print "TEST STEP 1: Failed to get the Radio stat enable value %s"%initial_stat

    obj.unloadModule("wifihal");

else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
