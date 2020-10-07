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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_WIFIHAL_5GHzGetBTMClientCapability</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetBTMClientCapabilityList</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the BTM capability of the connected wifi client device using wifi_getBTMClientCapabilityList() and check if the value returned is proper</synopsis>
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
    <test_case_id>TC_WIFIHAL_410</test_case_id>
    <test_objective>Get the BTM capability of the connected wifi client device using wifi_getBTMClientCapabilityList() and check if the value returned is proper</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.DUT should be connected with a single WiFi client
2. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
3.TDK Agent should be in running state or invoke it through StartTdk.sh scrip</pre_requisite>
    <api_or_interface_used>wifi_getBTMClientCapabilityList</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2.Invoke wifi_getApNumDevicesAssociated() to check the no: of associated devices
3. No: of associated devices should be greater than 0
3. Get the MAC of associated device
4. Invoke wifi_getBTMClientCapabilityList() using the above client mac, to get its BTM capability
5. Cross check the capability value from hal o/p with the client btm capability value configured in the config file tdkbVariables.py
6. Unload wifihal module</automation_approch>
    <expected_output>wifi_getBTMClientCapabilityList() api should successfully return the client's BTM capability</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetBTMClientCapability</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetBTMClientCapability');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	radioIndex = idx
	getMethod = "getApNumDevicesAssociated"
	primitive = 'WIFIHAL_GetOrSetParamULongValue'
	tdkTestObj = obj.createTestStep(primitive);
	tdkTestObj.addParameter("radioIndex",radioIndex);
        tdkTestObj.addParameter("methodName",getMethod);
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

	        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDevice');
                tdkTestObj.addParameter("apIndex",radioIndex);
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
		    print " TEST STEP 2: Get the mac address of one associated device using wifi_getApAssociatedDevice api"
		    print "EXPECTED RESULT 2 : Should get the Mac address of the associated device "
		    print "ACTUAL RESULT 2 :  Mac address of the associated device :%s" %macAddress;
		    tdkTestObj.setResultStatus("SUCCESS");
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] 2 : SUCCESS";

	            primitive = 'WIFIHAL_GetBTMClientCapabilityList'
	            tdkTestObj = obj.createTestStep(primitive);
	            tdkTestObj.addParameter("apIndex",radioIndex);
	            tdkTestObj.addParameter("clientMAC",macAddress);
	            tdkTestObj.addParameter("count",1);
	            tdkTestObj.executeTestCase(expectedresult);
	            actualresult = tdkTestObj.getResult();
	            details = tdkTestObj.getResultDetails();
	            if expectedresult in actualresult:
	                tdkTestObj.setResultStatus("SUCCESS");
	                print "TEST STEP 3: Get the BTM capability for 2.4GHz client";
	                print "EXPECTED RESULT 3: wifi_getBTMClientCapabilityList() should return the BTM capability for 2.4GHz client";
	                print "ACTUAL RESULT 3: wifi_getBTMClientCapabilityList() operation returned SUCCESS";
	                print "Actual result is :",details;
	                print "[TEST EXECUTION RESULT] 3: SUCCESS";
                        capability =  details.split(',')[2].split(' ')[2]
                        if capability == '1':
		            capability = "TRUE"
		        elif capability == '0':
		            capability = "FALSE"
		        else:
		            print "ERROR: Received invalid BTM capability value from hal api. Exiting script"
		            tdkTestObj.setResultStatus("FAILURE");
		            obj.unloadModule("wifihal");
		            exit()

                        print "TEST STEP 4: Check if the BTM Capability value from api is matching with the client details from config file";
                        print "EXPECTED RESULT 4: HAL output should match the BTM value specified in config file. Hal o/p is %s, config value is %s" %(capability, BTM_CLIENT_CAPABILITY);
                        if capability == BTM_CLIENT_CAPABILITY:
                            print "ACTUAL RESULT 4: BTM Capability value from api is matching with the client details from config file"
                            print "[TEST EXECUTION RESULT] 4: SUCCESS";
                        else:
                            print "ACTUAL RESULT 4: BTM Capability value from api is matching with the client details from config file"
                            print "[TEST EXECUTION RESULT] 4: FAILURE";
	            else:
		        tdkTestObj.setResultStatus("FAILURE");
  		        print "TEST STEP 3: Get the BTM capability for 2.4GHz client";
		        print "EXPECTED RESULT 3: wifi_getBTMClientCapabilityList() should return the BTM capability for 2.4GHz client";
		        print "ACTUAL RESULT 3: Failed to get the BTM capability for 2.4GHz client";
		        print "Actual result is :",details;
		        print "[TEST EXECUTION RESULT] 3: FAILURE";
		else:
		    print " TEST STEP 2: Get the mac address of one associated device using wifi_getApAssociatedDevice api"
		    print "EXPECTED RESULT 2 : Should get the Mac address of the asssociated device "
		    print "ACTUAL RESULT 2 :  Failed to get Mac address of the asssociated device"
		    tdkTestObj.setResultStatus("FAILURE");
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] 2 : FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 1: Get the number of Ap Associated Devices"
		print "EXPECTED RESULT 1: Should get the number of Ap Associated Devices as greater than 0"
		print "ACTUAL RESULT 1: Received number of Ap Associated Devices is not greater than 0"
		print "ApNumDevicesAssociated : %s"%ApNumDevices
		print "TEST EXECUTION RESULT 1: FAILURE"
	else:
            tdkTestObj.setResultStatus("FAILURE");
	    print "getApNumDevicesAssociated() call failed"
    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
