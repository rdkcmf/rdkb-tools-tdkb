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
  <version>10</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzCreateAp</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_CreateAp</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check the functionality of wifi_createAp  WIFIHAL api.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TS_WIFIHAL_298</test_case_id>
    <test_objective>To validate the functionality of
 wifi_createAp api for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script.</pre_requisite>
    <api_or_interface_used>wifi_createAp</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module.
2. Identify an AP to be used for create operation using wifi_getSSIDName()
3. If new AP available ,create the AP using wifi_createAp api.if not exit the script saying no new AP available to validate wifi_createAp api
4.Crosscheck the AP creation by checking ssidname using wifi_getSSIDName api
5.Delete the AP created using wifi_deleteAp api
6. Unload the module</automation_approch>
    <expected_output>Should create AP  using wifi_createAp api successfully</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzCreateAp</test_script>
    <skipped>No</skipped>
    <release_version>M80</release_version>
    <remarks>Nil</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");
radio = "5G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzCreateAp');
wifiobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzCreateAp');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
sysloadmodulestatus = wifiobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus

if "SUCCESS" in loadmodulestatus.upper() and sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the number of Wifi Accesspoints
	tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPointNumberOfEntries");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            APCount = int(details.split("VALUE:")[1].split(' ')[0]);
	    print "TEST STEP 1 : Get the number of Wifi Accesspoints using TR181 param ";
            print "EXPECTED RESULT 1: Should get the number of Wifi Accesspoints ";
            print "ACTUAL RESULT 1 : Number of Wifi Accesspoints :",APCount;
            print "[TEST EXECUTION RESULT] 1 : SUCCESS"
            #Identify a free Accesspoint to be created out of total Accesspoints
	    newFlag = 0;
            print " Check SSID Name of all AccessPoints to identify free AccessPoint using Wifi_getSSIDName api"
	    for apIndex in range(1, APCount, 2):
                expectedresult="SUCCESS";
	        getMethod = "getSSIDName"
	        primitive = 'WIFIHAL_GetOrSetParamStringValue'
                #Calling the method from wifiUtility to execute test case and set result status for the test.
	        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
                if expectedresult in actualresult:
		    ssidName = details.split(":")[1].strip()
		    print "ssidname for apindex %d = %s" %(apIndex,ssidName);
		    if len(ssidName) <= 32:
		        print "Wifi_getSSIDName() function called successfully and %s"%details
		        tdkTestObj.setResultStatus("SUCCESS");
		        #Get the result of execution
            	        print "[TEST EXECUTION RESULT] : SUCCESS";
		        if ssidName == "OutOfService":
		            newapIndex = apIndex;
			    newFlag = 1;
		            break;
		        else:
		            continue;
		    else:
		        tdkTestObj.setResultStatus("FAILURE");
			print "wifi_getSSIDName function failed,Failed to receive SSID string %s"%details
		        #Get the result of execution
            	        print "[TEST EXECUTION RESULT] : FAILURE";
			obj.unloadModule("wifihal");
			wifiobj.unloadModule("wifiagent");
		        print "Exiting the script"
		        exit();
	        else:
		    tdkTestObj.setResultStatus("FAILURE");
	            print "wifi_getSSIDName function failed";
		    obj.unloadModule("wifihal");
		    wifiobj.unloadModule("wifiagent");
		    print "Exiting the script"
		    exit();
	    if newFlag == 1 :
	        tdkTestObj.setResultStatus("SUCCESS");
	        print "TEST STEP 2 : Identify a free Accesspoint to be created out of total Accesspoints"
		print "EXPECTED RESULT 2 : Get  a free AccessPoint for 5 G"
		print "ACTUAL RESULT  2: %d APIndex is available for 5G " %newapIndex
		#Get the result of execution
                print "[TEST EXECUTION RESULT] 2 : SUCCESS";
	        #Prmitive test case which associated to this Script
                print "new apIndex :%d" %newapIndex;
                tdkTestObj = obj.createTestStep('WIFIHAL_CreateAp');
	        tdkTestObj.addParameter("apIndex",newapIndex);
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.addParameter("essid","ssid_name");
	        tdkTestObj.addParameter("hideSsid",0);
	        expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
	            #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Create the new AP using wifi_createAp api with ssid_name as SSID name";
                    print "EXPECTED RESULT 3: Should create the new AP using wifi_createAp api";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    time.sleep(20);
                    print "[TEST EXECUTION RESULT] 3 : SUCCESS";
	            #Calling the method from wifiUtility to execute test case and set result status for the test.
	            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, newapIndex, "0", getMethod)
                    if expectedresult in actualresult:
		        ssidName = details.split(":")[1].strip()
		        print "ssid name =%s " %ssidName;
		        if ssidName == "ssid_name":
		            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 4: Verify the ssid name of new ap created using Wifi_getSSIDName api  ";
            	            print "EXPECTED RESULT 4: Should match with ssid name of newly created api";
            	            print "ACTUAL RESULT 4: Successfully matched with ssid name of newly created api"
            	            #Get the result of execution
            	            print "[TEST EXECUTION RESULT] 4 : SUCCESS";
		            tdkTestObj = obj.createTestStep('WIFIHAL_ParamApIndex');
	                    tdkTestObj.addParameter("apIndex",newapIndex);
        	            tdkTestObj.addParameter("methodName","deleteAp");
		            expectedresult="SUCCESS";
        	            tdkTestObj.executeTestCase(expectedresult);
        	            actualresult = tdkTestObj.getResult();
        	            details = tdkTestObj.getResultDetails();
        	            if expectedresult in actualresult:
		                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 5: Delete ap created using wifi_deleteAp api";
                                print "EXPECTED RESULT 5: wifi_deleteAp api should be SUCCESS ";
                                print "ACTUAL RESULT 5: wifi_deleteAp api call returns SUCCESS"
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] 5 : SUCCESS";
		            else:
		                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
			        print "TEST STEP 5: Delete ap created using wifi_deleteAp api";
                                print "EXPECTED RESULT 5: wifi_deleteAp api should be SUCCESS ";
                                print "ACTUAL RESULT 5: wifi_deleteAp api call returns FAILURE"
			        #Get the result of execution
                                print "[TEST EXECUTION RESULT] 5 : FAILURE";
		        else:
		            tdkTestObj.setResultStatus("FAILURE");
		            print "TEST STEP 4: Verify the ssid name of new ap created using Wifi_getSSIDName api  ";
            	            print "EXPECTED RESULT 4: Should match with ssid name of newly created api";
            	            print "ACTUAL RESULT 4: Failed to match with ssid name of newly created api"
            	            #Get the result of execution
            	            print "[TEST EXECUTION RESULT] 4 : FAILURE";
	            else:
	                print "wifi_getSSIDName function failed";
		        tdkTestObj.setResultStatus("FAILURE");
    	        else:
      	            tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Create the new AP using wifi_createAp api with ssid_name as SSID name";
                    print "EXPECTED RESULT 3: Should create the new AP using wifi_createAp api";
	            print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] 3 : FAILURE";
	    else:
	        tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 2 : Identify a free Accesspoint to be created out of total Accesspoints"
		print "EXPECTED RESULT 2 : Get  a free AccessPoint for 5 G"
	        print " ACTUAL RESULT  2 : Cannot validate wifi_createAp api , as max supported APs are already created"
	        #Get the result of execution
                print "[TEST EXECUTION RESULT] 2 : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 1 : Get the number of Wifi Accesspoints using TR181 param";
            print "ACTUAL RESULT 1: Should get the number of Wifi Accesspoints ";
            print "EXPECTED RESULT 1 : Failed to get the number of Wifi Accesspoints ";
            print "[TEST EXECUTION RESULT] 1 : FAILURE"
    obj.unloadModule("wifihal");
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load the wifihal/wifiagent module";
    obj.setLoadModuleStatus("FAILURE");
    wifiobj.setLoadModuleStatus("FAILURE");
