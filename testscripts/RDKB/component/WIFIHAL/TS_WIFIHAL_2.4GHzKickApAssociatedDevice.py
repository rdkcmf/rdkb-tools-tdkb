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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzKickApAssociatedDevice</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Verify the Access point kick functionality using wifi_kickApAssociatedDevice()</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_517</test_case_id>
    <test_objective>Verify the Access point kick functionality using wifi_kickApAssociatedDevice()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.DUT should be connected with a WiFi client
2. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
3.TDK Agent should be in running state or invoke it through StartTdk.sh script.</pre_requisite>
    <api_or_interface_used>wifi_kickApAssociatedDevice()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2.Invoke wifi_getApNumDevicesAssociated() to check the no: of associated devices
3. No: of associated devices should be greater than 0
4. Get the MAC of AssociatedDevice.1 using Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress
5. Pass the above MAC to wifi_kickApAssociatedDevice(), so that wifi connection to that MAC gets disconnected
6. Invoke wifi_getApNumDevicesAssociated() to check the no: of associated devices after kick operation
7. If no: of associated device is returned as 0, then kick operation was success
8. If no: of associated device is greater than 0, then check if the current value of Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress is not equal to the kicked MAC
9. Unload wifihal module</automation_approch>
    <expected_output>wifi_kickApAssociatedDevice() should successfully disconnect WiFi connection to the specified MAC </expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzKickApAssociatedDevice</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzKickApAssociatedDevice');
wifiobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzKickApAssociatedDevice');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
wifiloadmodulestatus = wifiobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in wifiloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	radioIndex = idx
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamULongValue');
        tdkTestObj.addParameter("radioIndex",radioIndex);
        tdkTestObj.addParameter("methodName","getApNumDevicesAssociated");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

	if expectedresult in actualresult:
	    ApNumDevices = details.split(":")[1].strip();
	    if  ApNumDevices != "" and int(ApNumDevices) > 0:
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP 1: Get the number of Ap Associated Devices"
		print "EXPECTED RESULT 1: Should get the number of Ap Associated Devices as greater than 0"
		print "ACTUAL RESULT 1: Received the number of Ap Associated Devices as greater than 0"
		print "ApNumDevicesAssociated : %s"%ApNumDevices
		print "TEST EXECUTION RESULT 1: SUCCESS"

                #Find an associated MAC to be kicked
                print "TEST STEP 2: Get an AssociatedDevice MAC to be kicked "
                print "EXPECTED RESULT 2: Should successfully get the  AssociatedDevice MAC"
        	tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        	tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress");
        	expectedresult="SUCCESS";
        	tdkTestObj.executeTestCase(expectedresult);
        	actualresult = tdkTestObj.getResult();
        	details = tdkTestObj.getResultDetails();
        	if expectedresult in actualresult :
                    print "ACTUAL RESULT 2: Successfully gets the AssociatedDevice MAC ";
                    print "[TEST EXECUTION RESULT] 2: SUCCESS";
            	    tdkTestObj.setResultStatus("SUCCESS");
            	    macAddress = details.split("VALUE:")[1].split(' ')[0];
		    print "Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress :",macAddress;

                    print "TEST STEP 3: Kick the MAC %s using wifi_kickApAssociatedDevice()"%macAddress
                    print "EXPECTED RESULT 3: Should successfully Kick the MAC %s"%macAddress
                    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamStringValue');
                    tdkTestObj.addParameter("radioIndex",radioIndex);
                    tdkTestObj.addParameter("methodName","kickApAssociatedDevice");
                    tdkTestObj.addParameter("param", macAddress);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        print "ACTUAL RESULT 3: wifi_kickApAssociatedDevice() returns success";
                        print "[TEST EXECUTION RESULT] 3: SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        getMethod = "getApNumDevicesAssociated"
                        primitive = 'WIFIHAL_GetOrSetParamULongValue'
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                        if expectedresult in actualresult:
                             ApNumDevices = details.split(":")[1].strip();
                             tdkTestObj.setResultStatus("SUCCESS");
                             print "ApNumDevicesAssociated : %s"%ApNumDevices
                             if int(ApNumDevices) > 0:
                                 print "TEST STEP 4: Check if Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress is no longer ",macAddress
                                 print "EXPECTED RESULT 4: Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress should not be equal to ",macAddress
                                 tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
                                 tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress");
                                 expectedresult="SUCCESS";
                                 tdkTestObj.executeTestCase(expectedresult);
                                 actualresult = tdkTestObj.getResult();
                                 details = tdkTestObj.getResultDetails();
                                 if expectedresult in actualresult:
                                     newMacAddress = details.split("VALUE:")[1].split(' ')[0];
                                     print "Device.WiFi.AccessPoint.1.AssociatedDevice.x.MACAddress :",newMacAddress;
                                     if newMacAddress != macAddress:
                                         print "ACTUAL RESULT 4: Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress is not equal to kicked MAC ",macAddress
                                         print "[TEST EXECUTION RESULT] 4: SUCCESS";
                                         tdkTestObj.setResultStatus("SUCCESS");
                                     else:
                                         print "ACTUAL RESULT 4: Device.WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress is equal to kicked MAC",macAddress
                                         print "[TEST EXECUTION RESULT] 4: FAILURE";
                                         tdkTestObj.setResultStatus("FAILURE");
                                 else:
                                     print "ACTUAL RESULT : Failed to get the AssociatedDevice MAC ";
                                     print "[TEST EXECUTION RESULT] : FAILURE";
                                     tdkTestObj.setResultStatus("FAILURE");
                             else:
                                 tdkTestObj.setResultStatus("SUCCESS");
                                 print "Received the number of Ap Associated Devices as 0. Kick operation is SUCCESS"
                        else:
                             tdkTestObj.setResultStatus("FAILURE");
                             print "wifi_getApNumDevicesAssociated() call failed"
                    else:
                        print "ACTUAL RESULT 3: wifi_kickApAssociatedDevice() returned failure";
                        print "[TEST EXECUTION RESULT] 3: FAILURE";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "ACTUAL RESULT 2: Failed to get the AssociatedDevice MAC ";
                    print "[TEST EXECUTION RESULT] 2: FAILURE";
            	    tdkTestObj.setResultStatus("FAILURE");
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 1: Get the number of Ap Associated Devices"
		print "EXPECTED RESULT 1: Should get the number of Ap Associated Devices as greater than 0"
		print "ACTUAL RESULT 1: Received the number of Ap Associated Devices as greater than 0"
		print "ApNumDevicesAssociated : %s"%ApNumDevices
		print "TEST EXECUTION RESULT 1: FAILURE"
	else:
            tdkTestObj.setResultStatus("FAILURE");
	    print "getApNumDevicesAssociated() call failed"
    obj.unloadModule("wifihal");
    wifiobj.unloadModule("wifiagent");
else:
    obj.setLoadModuleStatus("FAILURE");
    wifiobj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
