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
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzRemoveSteeringClient</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_SteeringClientRemove</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if wifi_steering_clientRemove() removes the client config</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_295</test_case_id>
    <test_objective>Check if wifi_steering_clientRemove() removes the client config</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_steering_clientRemove()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2. Check if SSID and passphrase of 2.4G and 5G are same. If not, set same SSID and passphrase values for 2.4G and 5G
3. Invoke wifi_steering_clientSet() to add a steering client config for 2.4G.
4. Do a get of steering client config using the platform specific logic specified in tdk_platform_utility.sh and check if added config is present
5. Using wifi_steering_clientRemove(), remove the client config added in step3
6. Do a get of steering client config and confirm if the specified client config got removed
7. If SSID and passphrase were changed in step2, revert them back
8. Unload wifihal module</automation_approch>
    <expected_output>wifi_steering_clientRemove() should remove the specified client config</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzRemoveSteeringClient</test_script>
    <skipped>No</skipped>
    <release_version>M80</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
wifiObj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzRemoveSteeringClient');
sysObj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzRemoveSteeringClient');
wifiObj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzRemoveSteeringClient');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus
wifiloadmodulestatus =wifiObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus

#To get 2.4G steering client config
def getSteeringClient(tdkTestObj):
    query="sh %s/tdk_platform_utility.sh getAp0SteeringClient" %TDK_PATH
    print "query:%s" %query
    tdkTestObj.addParameter("command", query);
    expectedresult="SUCCESS";
    print "TEST STEP :Get the current steering client MAC configured";
    print "EXPECTED RESULT :Should successfully get the current steering client MAC configured"
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
    print " SteeringClient:  ", details;
    return details,actualresult;

def checkSteeringSSIDPassphrase(tdkTestObj, wifiObj):
    expectedresult="SUCCESS";
    print "TEST STEP 1: Get the current KeyPassphrase, SSID"
    print "EXPECTED RESULT 1: Should retrieve the current KeyPassphrase, SSID"
    getParams = "Device.WiFi.AccessPoint.1.Security.KeyPassphrase,Device.WiFi.AccessPoint.2.Security.KeyPassphrase,Device.WiFi.SSID.1.SSID,Device.WiFi.SSID.2.SSID"
    getList = getParams.split(',');
    actualresult_get = [];
    orgValue = [];
    revertFlag = 0
    actualresult="FAILURE";

    for index in range(len(getList)):
        tdkTestObj.addParameter("paramName",getList[index])
        #execute the step
        tdkTestObj.executeTestCase(expectedresult);
        actualresult_get.append(tdkTestObj.getResult())
	details = tdkTestObj.getResultDetails();
        orgValue.append( details.split("VALUE:")[1].split(' ')[0] );

    getFlag = 1;
    for index in range(len(getList)):
	if expectedresult not in actualresult_get[index]:
	    getFlag = 0;
	    break;

    if getFlag == 1:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Get operation SUCCESS"
        print "Device.WiFi.AccessPoint.1.Security.KeyPassphrase : %s ,Device.WiFi.AccessPoint.2.Security.KeyPassphrase: %s, Device.WiFi.SSID.1.SSID: %s, Device.WiFi.SSID.2.SSID: %s" %(orgValue[0], orgValue[1], orgValue[2], orgValue[3])

        #Check if 2.4G SSID and passphrase are same as 5G SSID and passphrase
        if orgValue[0] != orgValue[1] or orgValue[2] != orgValue[3]:
            revertFlag = 1
            print "TEST STEP 2: Set SSID and passphrase values of 2.4G and 5G as same for steering purpose"
            print "EXPECTED RESULT 2: Should  Set SSID and passphrase values of 2.4G and 5G as same"

            tdkTestObj = wifiObj.createTestStep("WIFIAgent_SetMultiple");
            passPhrase = "test_password"
            ssid = "TDK_TEST_SSID"
            tdkTestObj.addParameter("paramList","Device.WiFi.AccessPoint.1.Security.KeyPassphrase|%s|string|Device.WiFi.AccessPoint.2.Security.KeyPassphrase|%s|string|Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string" %(passPhrase, passPhrase, ssid, ssid))
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "ACTUAL RESULT 2: Set operation SUCCESS"
                return orgValue, actualresult, revertFlag
            else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "ACTUAL RESULT 2: Set operation FAILURE"
                return orgValue, actualresult, revertFlag
        else:
            print "2.4G SSID and passphrase are same as 5G SSID and passphrase. Can proceed for steering test"
            actualresult="SUCCESS";
            return orgValue, actualresult, revertFlag
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Get operation Failed"
        return orgValue, actualresult, revertFlag


if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper() and "SUCCESS" in wifiloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");
    wifiObj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        tdkTestObj = wifiObj.createTestStep("WIFIAgent_Get");
        orgValue, actualresult, revertFlag = checkSteeringSSIDPassphrase(tdkTestObj, wifiObj)
        if expectedresult in actualresult :
	    apIndex = idx
            clientMAC = "AA:BB:CC:DD:EE:FF"
	    primitive = 'WIFIHAL_SteeringClientSet'
	    tdkTestObj = obj.createTestStep(primitive);
	    tdkTestObj.addParameter("apIndex",apIndex);
	    tdkTestObj.addParameter("steeringgroupIndex",0);
	    tdkTestObj.addParameter("rssiProbeHWM",0);
	    tdkTestObj.addParameter("rssiProbeLWM",0);
	    tdkTestObj.addParameter("rssiAuthHWM",0);
	    tdkTestObj.addParameter("rssiAuthLWM",0);
	    tdkTestObj.addParameter("rssiInactXing",0);
	    tdkTestObj.addParameter("rssiHighXing",0);
	    tdkTestObj.addParameter("rssiLowXing",0);
	    tdkTestObj.addParameter("authRejectReason",17);
	    tdkTestObj.addParameter("clientMAC", clientMAC);
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
	    if expectedresult in actualresult :
		print "TEST STEP 3:Add steering client config for MAC %s using wifi_steering_clientSet()" %clientMAC;
		print "EXPECTED RESULT 3:wifi_steering_clientSet() should return SUCCESS"
		print "ACTUAL RESULT 3: wifi_steering_clientSet() returns SUCCESS"
		tdkTestObj.setResultStatus("SUCCESS");
		#Get the result of execution
		print "[TEST EXECUTION RESULT] 1: SUCCESS";
		# Get the New enable status
		tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                expectedresult="SUCCESS";
                details, actualresult = getSteeringClient(tdkTestObj);

		if expectedresult in actualresult and details !="" and clientMAC in details :
		    print "wifi_steering_clientSet() validation using get operation is success"

		    #Remove the client config added using wifi_steering_clientRemove()
		    print "TEST STEP 4:Remove the previously added steering client config using wifi_steering_clientRemove()";
		    print "EXPECTED RESULT 4: wifi_steering_clientRemove() should return SUCCESS"
                    primitive = 'WIFIHAL_SteeringClientRemove'
	            tdkTestObj = obj.createTestStep(primitive);
	            tdkTestObj.addParameter("apIndex",apIndex);
	            tdkTestObj.addParameter("steeringgroupIndex",0);
         	    tdkTestObj.addParameter("clientMAC", clientMAC);
	            tdkTestObj.executeTestCase(expectedresult);
	            actualresult = tdkTestObj.getResult();
	            details = tdkTestObj.getResultDetails()
		    if expectedresult in actualresult :
		        print "ACTUAL RESULT 4: wifi_steering_clientRemove() returns SUCCESS"
		        tdkTestObj.setResultStatus("SUCCESS");

		        print "TEST STEP 5:Get steering client config and check if client is removed";
		        print "EXPECTED RESULT 5:Client config should be removed"
		        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                        expectedresult="SUCCESS";
                        details, actualresult = getSteeringClient(tdkTestObj);
		        if expectedresult in actualresult and (details =="" or clientMAC not in details) :
                            print "ACTUAL RESULT 5: Client config successfully removed with wifi_steering_clientRemove()";
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "[TEST EXECUTION RESULT] 5: SUCCESS";
                        else:
                            print "ACTUAL RESULT 5: Failed to remove Client config with wifi_steering_clientRemove()";
		            tdkTestObj.setResultStatus("FAILURE");
           		    print "[TEST EXECUTION RESULT] 5: FAILURE";
		    else:
		        print "wifi_steering_clientRemove() validation using get operation failed"
		        tdkTestObj.setResultStatus("FAILURE");
		else:
		    print "wifi_steering_clientSet() validation using get operation failed"
		    tdkTestObj.setResultStatus("FAILURE");
	    else:
		print "TEST STEP 3:Add steering client config for MAC %s using wifi_steering_clientSet()" %clientMAC;
		print "EXPECTED RESULT 3:wifi_steering_clientSet() should return SUCCESS"
		print "ACTUAL RESULT 3: wifi_steering_clientSet() returns FAILURE"
		tdkTestObj.setResultStatus("FAILURE");
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";
            if revertFlag == 1:
                tdkTestObj = wifiObj.createTestStep("WIFIAgent_SetMultiple");
                tdkTestObj.addParameter("paramList","Device.WiFi.AccessPoint.1.Security.KeyPassphrase|%s|string|Device.WiFi.AccessPoint.2.Security.KeyPassphrase|%s|string|Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string" %(orgValue[0],orgValue[1],orgValue[2],orgValue[3]));
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                if expectedresult in actualresult:
                    print "Successfully reverted SSIDs and passphrases to previous values"
                    tdkTestObj.setResultStatus("SUCCESS");
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    print "Failed to revert SSIDs and passphrases to previous values";
                    tdkTestObj.setResultStatus("FAILURE");
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
    sysObj.unloadModule("sysutil");
    wifiObj.unloadModule("wifiagent");
else:
    print "Failed to load wifihal/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
