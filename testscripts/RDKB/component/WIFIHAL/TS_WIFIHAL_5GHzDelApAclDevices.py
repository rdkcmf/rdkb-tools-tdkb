##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>10</version>
  <name>TS_WIFIHAL_5GHzDelApAclDevices</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_DelApAclDevices</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the delApAclDevices api by deleting the ap acl associated devices and restore back to the initial condition.</synopsis>
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
    <test_case_id>TC_WIFIHAL_349</test_case_id>
    <test_objective>To delete all ApAclDevices  using delApAclDevices() api for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAclDeviceNum()
wifi_getApAclDevices()
wifi_addApAclDevice()
wifi_delApAclDevices()</api_or_interface_used>
    <input_parameters>methodName : getApAclDeviceNum
methodName : getApAclDevices
methodName : addApAclDevice
methodName : delApAclDevices
apIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Get the number of ApAcl devices list and count using the wifi_getApAclDevices() API.
3.Store the mac address in a array variable.
4.Check for the count if it is 0,add 2 mac address or else 1 mac address.
5.Add a ApAcl device by passing its mac address to the api wifi_addApAclDevice().
6.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is incremented by 1 or 2.
7.Delete all the mac addr associated with  ApAcl device by invoking wifi_delApAclDevices() api.
8.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is zero or not.
9.Unload the module.</automation_approch>
    <except_output>Should be able to delete all ApAclDevices  using delApAclDevices() api for 5GHz</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzDelApAclDevices</test_script>
    <skipped>No</skipped>
    <release_version>nil</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzDelApAclDevices');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
    tdkTestObj.addParameter("apIndex",1);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details_new = tdkTestObj.getResultDetails();
    print "Mac Details",details_new;
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        apIndex = 1
        getMethod = "getApAclDeviceNum"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod);
        olddeviceNum = int(details.split(":")[1].strip());

        if olddeviceNum != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Get the number of devices in the filter list"
            print "EXPECTED RESULT : Should get the number of devices as a non empty value"
            print "ACTUAL RESULT : Received the number of devices as a NON EMPTY value"
            print "Device number : %s"%olddeviceNum
            print "TEST EXECUTION RESULT: SUCCESS"
            print"Number of ApAcl devices initially for 5GHz=",olddeviceNum;
            
            addMAC=["7A:36:76:41:9A:5F","8A:46:86:51:AA:6F"];
            macAddress= [];

            if olddeviceNum == 0:
                count=2;
                no_add=1
            else:
                count=1;
                no_add=0;
            if olddeviceNum > 0:
                macAddress = details_new.split(";")[1].split("n")
                for i in range(len(macAddress)):
                    macAddress[i] =  macAddress[i].replace("\\", '')
            else:
                print"No mac address listed"
            print macAddress;

            #Adding the mac addresses
            for i in range(0,count):
                tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                tdkTestObj.addParameter("methodName","addApAclDevice");
                tdkTestObj.addParameter("apIndex",1);
                tdkTestObj.addParameter("DeviceMacAddress",addMAC[i]);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print"Successfully added ApAclDevice", addMAC[i]
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print"wifi_addApAclDevice() operation failed after add operation";
                    break
            if expectedresult in actualresult:
                apIndex = 1;
                getMethod = "getApAclDeviceNum";
                primitive = 'WIFIHAL_GetOrSetParamUIntValue';
                #Get the current ApAclDevice count
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
                deviceNum_add = int(details.split(":")[1].strip());
                if expectedresult in actualresult:
                    deviceNum_new = deviceNum_add - olddeviceNum;
                    if deviceNum_new == 1 or deviceNum_new == 2:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print"Number of ApAcl devices after adding for 5GHz =",deviceNum_add;
                        #Deleting the ApAcl devices
                        tdkTestObj = obj.createTestStep('WIFIHAL_DelApAclDevices');
                        tdkTestObj.addParameter("apIndex",1);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        print"details",details;
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print"ApAclDevices is successfully deleted";
                            apIndex = 1
                            getMethod = "getApAclDeviceNum"
                            primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                            # get the current ApAcl device count after deleting the ApAcl devices
			    time.sleep(2)
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                deviceNum_del = int(details.split(":")[1].strip());
                                if deviceNum_del == 0:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print"Number of ApAcl devices after deleting is equal to 0";
                                    #Reverting back
                                    if no_add == 0:
                                        for deviceMac in macAddress:
                                            tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                                            tdkTestObj.addParameter("methodName","addApAclDevice");
                                            tdkTestObj.addParameter("apIndex",1);
                                            tdkTestObj.addParameter("DeviceMacAddress",deviceMac);
                                            tdkTestObj.executeTestCase(expectedresult);
                                            actualresult = tdkTestObj.getResult();
                                            details = tdkTestObj.getResultDetails();
                                            if expectedresult in actualresult:
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "Added device :", deviceMac
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "addApAclDevice failed not reverted back"
                                        apIndex = 1
                                        getMethod = "getApAclDeviceNum"
                                        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                                        #Calling "getApAclDeviceNum" to get the number of connected devices after adding back the Mac addresses
                                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
                                        newdeviceNum = int(details.split(":")[1].strip());
                                        if expectedresult in actualresult:
                                            print "New device count:",newdeviceNum;
                                            if newdeviceNum == olddeviceNum:
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print"Successfully reverted back";
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print"wifi_addApAclDevice() failed after delete operation Not Reverted back";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print"wifi_getApAclDeviceNum() operation failed after add operation";
                                    else:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print"No need of adding devices as no device listed initially";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print"Number of ApAcl devices after deleting is equal not 0";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print"wifi_getApAclDeviceNum()failed after deleting the ApAcl devices";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print"wifi_delApAclDevice() operation failed";
                    else:
                        tdkTestObj.setResultStatus("FAILURE"); 
                        print"Device number not changed properly after add operation";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print"getApAclDeviceNum() operation failed after add operation ";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"wifi_addApAclDevice() operation failed";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the number of devices in the filter list"
            print "EXPECTED RESULT : Should get the number of devices as a non empty value"
            print "ACTUAL RESULT : Received the number of devices as an EMPTY value"
            print "Device number : %s"%olddeviceNum
            print "TEST EXECUTION RESULT: FAILURE"
    else: 
        tdkTestObj.setResultStatus("FAILURE");
        print"wifi_getApAclDevices() operation failed";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
