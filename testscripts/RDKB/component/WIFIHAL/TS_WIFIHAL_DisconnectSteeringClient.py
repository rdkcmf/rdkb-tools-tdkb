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
  <version>20</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_DisconnectSteeringClient</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_SteeringClientDisconnect</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if wifi_steering_clientDisconnect() disconnect the steering client</synopsis>
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
    <test_case_id>TC_WIFIHAL_299</test_case_id>
    <test_objective>Disconnect steering client  using wifi_steering_clientDisconnect() api</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a wifi client.
4.  SSID and passphrase of 2.4G and 5G should be  same.</pre_requisite>
    <api_or_interface_used>wifi_steering_clientDisconnect()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2. Check if SSID and passphrase of 2.4G and 5G are same. If not, exit the script.
3. Get the number of devices connected to each AP using wifi_getApNumDevicesAssociated  api
4. Get the mac address of the device to be disconnected  using wifi_getApAssociatedDevice api.
5. Invoke wifi_steering_clientDisconnect() to disconnect a steering client  with specific mac address
6. Check whether client disconnected after wifi_steering_clientDisconnect using wifi_getApNumDevicesAssociated  api.
7. Unload wifihal module</automation_approch>
    <expected_output>Should successfully disconnect steering client using wifi_steering_clientDisconnect()</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_DisconnectSteeringClient</test_script>
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
from tdkbVariables import *;

radio0 = "2.4G"
radio1 = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
wifiObj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_DisconnectSteeringClient');
wifiObj.configureTestCase(ip,port,'TS_WIFIHAL_DisconnectSteeringClient');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
wifiloadmodulestatus =wifiObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus

# check and ensure the ssid and passphrase same for 2.4G and 5G
def checkSteeringSSIDPassphrase(tdkTestObj, wifiObj):
    expectedresult="SUCCESS";
    print "TEST STEP 1: Get the current KeyPassphrase, SSID"
    print "EXPECTED RESULT 1: Should retrieve the current KeyPassphrase, SSID"
    getParams = "Device.WiFi.AccessPoint.1.Security.KeyPassphrase,Device.WiFi.AccessPoint.2.Security.KeyPassphrase,Device.WiFi.SSID.1.SSID,Device.WiFi.SSID.2.SSID"
    getList = getParams.split(',');
    actualresult_get = [];
    orgValue = [];
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
        print "ACTUAL RESULT : Get operation SUCCESS"

        #Check if 2.4G SSID and passphrase are same as 5G SSID and passphrase
        if orgValue[0] == orgValue[1] and orgValue[2] == orgValue[3]:
            actualresult="SUCCESS";
    return  actualresult

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in wifiloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    wifiObj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx0 = getIndex(obj, radio0);
    tdkTestObjTemp, idx1 = getIndex(obj, radio1);
    ## Check if a invalid index is returned
    if idx0 == -1 or idx1 == -1:
        if idx0 == -1 :
            print "Failed to get radio index for radio %s\n" %radio0;
        if idx1 == -1:
	    print "Failed to get radio index for radio %s\n" %radio1;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
	connectFlag = 0;
	index = [idx0,idx1];
        tdkTestObj = wifiObj.createTestStep("WIFIAgent_Get");
        actualresult = checkSteeringSSIDPassphrase(tdkTestObj, wifiObj)
        if expectedresult in actualresult :
	    print "TEST STEP 2 : Check the SSID and passphrase are same for 2.4G and 5G."
            print " EXPECTED RESULT 2 : 2.4G SSID and passphrase are same as 5G SSID and passphrase. Can proceed for steering test"
	    print " ACTUAL RESULT 2 :  2.4G SSID and passphrase are same as 5G SSID and passphrase. "
            tdkTestObj.setResultStatus("SUCCESS");
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] 2 : SUCCESS";
	    # check to which radioIndex client got connected
	    for radioIndex in index:
	        getMethod = "getApNumDevicesAssociated"
	        primitive = 'WIFIHAL_GetOrSetParamULongValue'
	        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	        if expectedresult in actualresult:
		    ApNumDevices = int(details.split(":")[1].strip());
		    if  ApNumDevices != 0:
		       connectFlag = 1;
		       break;
		    else:
		       continue;
		else:
		    print "wifi_getApNumDevicesAssociated failed"
		    tdkTestObj.setResultStatus("FAILURE");
		    print "Exiting the script"
		    exit();
	    if connectFlag == 1:
	        print "TESTSTEP 3 : Get the number of devices connected to each AP using wifi_getApNumDevicesAssociated  api"
	        print "EXPECTED RESULT 3 : Atleast one device connected to any  AP"
		print "ACTUAL RESULT 3 : %d device connected to radioIndex %d" %(ApNumDevices,radioIndex);
	        tdkTestObj.setResultStatus("SUCCESS");
		#Get the result of execution
		print "[TEST EXECUTION RESULT] 3 : SUCCESS";
		# Get the mac address of device
	        apIndex = radioIndex;
	        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDevice');
                tdkTestObj.addParameter("apIndex",apIndex);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "Entire Details:",details;
                if expectedresult in actualresult:
                    outputList = details.split("=")[1].strip()
                    if "," in outputList:
                        macAddress = outputList.split(",")[0].strip()
                    else:
                        macAddress = outputList.split(":Value")[0].strip()
		    print " TEST STEP 4: Get the mac address of one associated device using wifi_getApAssociatedDevice api"
		    print "EXPECTED RESULT 4 : Should get the Mac address of the asssociated device "
		    print "ACTUAL RESULT 4 :  Mac address of the asssociated device :%s" %macAddress;
		    tdkTestObj.setResultStatus("SUCCESS");
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] 4 : SUCCESS";
		else:
		    print " TEST STEP 4: Get the mac address of one associated device using wifi_getApAssociatedDevice api"
		    print "EXPECTED RESULT 4 : Should get the Mac address of the asssociated device "
		    print "ACTUAL RESULT 4 :  Failed to get Mac address of the asssociated device"
		    tdkTestObj.setResultStatus("FAILURE");
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] 4 : FAILURE";
		    print "Exiting the script"
		    exit();
                print "MacAddress :", macAddress;
	        primitive = 'WIFIHAL_SteeringClientDisconnect';
		tdkTestObj = obj.createTestStep(primitive);
		tdkTestObj.addParameter("steeringgroupIndex",0);
	        tdkTestObj.addParameter("apIndex",radioIndex);
		tdkTestObj.addParameter("clientMAC",macAddress);
		tdkTestObj.addParameter("disconnectType",2);
		tdkTestObj.addParameter("reason",3);
		tdkTestObj.executeTestCase(expectedresult);
	        actualresult = tdkTestObj.getResult();
	        details = tdkTestObj.getResultDetails();
	        if expectedresult in actualresult :
		    print "TEST STEP 5:Disconnect steering client of specific mac using wifi_steering_clientDisconnect()";
		    print "EXPECTED RESULT 5: wifi_steering_clientDisconnect() should return SUCCESS"
		    print "ACTUAL RESULT 5:  wifi_steering_clientDisconnect() returns SUCCESS"
		    tdkTestObj.setResultStatus("SUCCESS");
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] 5 : SUCCESS";
		    # check whether client get disconnected
                    print "check whether client got disconnected"
		    getMethod = "getApNumDevicesAssociated"
	            primitive = 'WIFIHAL_GetOrSetParamULongValue'
	            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	            if expectedresult in actualresult:
		        ApNumDevicesNew = int(details.split(":")[1].strip());
		        if  ApNumDevicesNew == ApNumDevices-1:
			    print "TEST STEP 6 :Check whether client got disconnected after wifi_steering_clientDisconnect()  using wifi_getApNumDevicesAssociated  api"
		            print "EXPECTED RESULT 6: Specific client should disconnect after wifi_steering_clientDisconnect "
			    print "ACTUAL RESULT 6 : Client successfully disconnected after wifi_steering_clientDisconnect()"
			    tdkTestObj.setResultStatus("SUCCESS");
			    #Get the result of execution
		            print "[TEST EXECUTION RESULT] 6 : SUCCESS";
			else:
			    print "TEST STEP 6 :Check whether client got disconnected after wifi_steering_clientDisconnect()  using wifi_getApNumDevicesAssociated  api"
		            print "EXPECTED RESULT 6: Specific client should disconnect after wifi_steering_clientDisconnect "
			    print "ACTUAL RESULT 6: Client failed to disconnect after wifi_steering_clientDisconnect()"
		            tdkTestObj.setResultStatus("FAILURE");
		            #Get the result of execution
		            print "[TEST EXECUTION RESULT] 6 : FAILURE";
		    else:
		        print "wifi_getApNumDevicesAssociated failed after wifi_steering_clientDisconnect()"
		        tdkTestObj.setResultStatus("FAILURE");
			print "Exiting the script"
		        exit();
		else:
		    print "TEST STEP 5:Disconnect steering client of specific mac using wifi_steering_clientDisconnect()";
		    print "EXPECTED RESULT 5: wifi_steering_clientDisconnect() should return SUCCESS"
		    print "ACTUAL RESULT 5:  wifi_steering_clientDisconnect() FAILED"
		    tdkTestObj.setResultStatus("FAILURE");
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] 5: FAILURE";
	    else:
	        print "TESTSTEP 3 : Get the number of devices connected to each AP using wifi_getApNumDevicesAssociated  api"
	        print "EXPECTED RESULT 3 : Atleast one device connected to any  AP "
		print "ACTUAL RESULT 3: No wifi client connected "
		tdkTestObj.setResultStatus("FAILURE");
		#Get the result of execution
		print "[TEST EXECUTION RESULT] 3: FAILURE";
	        print "Exiting the script"
	        exit();
	else:
	    print "TEST STEP 2: Check the SSID and passphrase are same for 2.4G and 5G."
            print " EXPECTED RESULT 2 : 2.4G SSID and passphrase are same as 5G SSID and passphrase. Can proceed for steering test"
	    print " EXPECTED RESULT 2 : 2.4G SSID and passphrase are not same as 5G SSID and passphrase "
	    tdkTestObj.setResultStatus("FAILURE");
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] 2 : FAILURE";
    obj.unloadModule("wifihal");
    wifiObj.unloadModule("wifiagent");
else:
    print "Failed to load wifihal/wifiagent module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";