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
  <version>3</version>
  <name>TS_WIFIHAL_6GHzAddorDelApAclDevice</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_AddorDelApAclDevice</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To add a MAC address using the HAL API wifi_addApAclDevice() and check if the number of devices is getting incremented by 1 with wifi_getApAclDeviceNum() and then deleting the added MAC address using wifi_delApAclDevice() and checking if wifi_getApAclDeviceNum() returns the initial number of devices for 6GHz access point.</synopsis>
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
    <test_case_id>TC_WIFIHAL_628</test_case_id>
    <test_objective>To add a MAC address using the HAL API wifi_addApAclDevice() and check if the number of devices is getting incremented by 1 with wifi_getApAclDeviceNum() and then deleting the added MAC address using wifi_delApAclDevice() and checking if wifi_getApAclDeviceNum() returns the initial number of devices for 6GHz access point.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_addApAclDevice()
wifi_getApAclDevices()
wifi_delApAclDevice()
wifi_getApAclDeviceNum()</api_or_interface_used>
    <input_parameters>methodname : addApAclDevice
methodname : getApAclDevices
methodname : delApAclDevice
methodname : getApAclDeviceNum
apIndex : fetched from platform property file
DeviceMacAddress : dynamically generated</input_parameters>
    <automation_approch>1.Load the module.
2. Get the 6GHz access point index from the device platform property file
3.Get the number of ApAcl devices using the wifi_getApAclDeviceNum() API
4.Add a ApAcl device by passing its mac address to the api wifi_addApAclDevice().
5.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is incremented by 1.
6.Delete the previously added ApAcl device by invoking wifi_delApAclDevice() api.
7.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is decremented by 1.
8.Unload the module.</automation_approch>
    <expected_output>Should be able to add a MAC using the HAL API wifi_addApAclDevice() and the ApAclDeviceNum should be incremented by 1 when retrieved via wifi_getApAclDeviceNum(). Also, wifi_delApAclDevice() should delete the MAC address from the ApAcl List and the value retrieved using wifi_getApAclDeviceNum() should be decremented by 1.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzAddorDelApAclDevice</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def GetDeviceNum(tdkTestObj, apIndex, step):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("methodName","getApAclDeviceNum");
    tdkTestObj.addParameter("radioIndex",apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Invoke wifi_getApAclDeviceNum to get the ApAclDeviceNum" %step;
    print "EXPECTED RESULT %d: Should invoke wifi_getApAclDeviceNum successfully" %step;

    if expectedresult in actualresult:
        print "ACTUAL RESULT %d: wifi_getApAclDeviceNum is invoked successfully" %step ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "ACTUAL RESULT %d: wifi_getApAclDeviceNum is not invoked successfully" %step ;
        print "TEST EXECUTION RESULT :FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    return actualresult, details;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
from random import randint;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzAddorDelApAclDevice');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzAddorDelApAclDevice');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS";
    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the ApAclDeviceNum
        step = 2;
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamUIntValue');
        actualresult, details = GetDeviceNum(tdkTestObj, apIndex, step);

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            deviceNum = int(details.split(":")[1].strip());
            print"Number of ApAcl devices initially : ",deviceNum;

            # Generate MAC address
            mac_partial_1 = "2b:9c:4a:6c:92:"
            x = str(randint(10,99))
            addMAC = mac_partial_1+x;
            print "MAC to be added is ", addMAC;
            tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
            #Giving the method name to invoke the api wifi_addApAclDevice()
            tdkTestObj.addParameter("methodName","addApAclDevice");
            tdkTestObj.addParameter("apIndex",apIndex);
            tdkTestObj.addParameter("DeviceMacAddress",addMAC);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            step = step + 1;
            print "\nTEST STEP %d: Invoke the HAL API wifi_addApAclDevice() to add the MAC address" %step;
            print "EXPECTED RESULT %d: The API should be invoked successfully" %step;

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : The API was invoked successfully" %step;
                print"Successfully added ApAclDevice", addMAC
                print "TEST EXECUTION RESULT :SUCCESS";

                step = step + 1;
                tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamUIntValue');
                actualresult, details = GetDeviceNum(tdkTestObj, apIndex, step);

                if expectedresult in actualresult:
                    deviceNum_add = int(details.split(":")[1].strip());
                    deviceNum_new = deviceNum_add - deviceNum;

                    step = step + 1;
                    print "\nTEST STEP %d : Check if the Number of devices is incremented by 1" %step;
                    print "EXPECTED RESULT %d : The Number of Devices should be incremented by 1" %step;

                    if deviceNum_new == 1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Number of devices are incremented by 1" %step;
                        print"Number of ApAcl devices after add operation : ",deviceNum_add;
                        print "TEST EXECUTION RESULT :SUCCESS"

                        #Primitive test case which associated to this Script
                        tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                        #Giving the method name to invoke the api wifi_delApAclDevice
                        tdkTestObj.addParameter("methodName","delApAclDevice");
                        tdkTestObj.addParameter("apIndex",apIndex);
                        tdkTestObj.addParameter("DeviceMacAddress",addMAC);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        step = step + 1;
                        print "\nTEST STEP %d : Delete the added Acl Device using the HAL API wifi_delApAclDevice" %step;
                        print "EXPECTED RESULT %d: Should Delete the added Acl Device using the HAL API wifi_delApAclDevice" %step;

                        if expectedresult in actualresult:
                            print "ACTUAL RESULT %d : wifi_delApAclDevice was invoked successfully" %step;
                            print "Deleted device :", addMAC
                            print "TEST EXECUTION RESULT :SUCCESS";
                            tdkTestObj.setResultStatus("SUCCESS");

                            step = step + 1;
                            tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamUIntValue');
                            actualresult, details = GetDeviceNum(tdkTestObj, apIndex, step);

                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                deviceNum_del = int(details.split(":")[1].strip());

                                step = step + 1;
                                print "\nTEST STEP %d : Check if the Number of devices is restored to initial state" %step;
                                print "EXPECTED RESULT %d : The Number of Devices should be restored to initial state" %step;

                                if deviceNum == deviceNum_del:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print"ACTUAL RESULT %d: Number of ApAcl devices after deleting are equal to number of ApAcl devices initially" %step;
                                    print "TEST EXECUTION RESULT :SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print"ACTUAL RESULT %d: Number of ApAcl devices after deleting are not equal to number of ApAcl devices initially" %step;
                                    print "TEST EXECUTION RESULT :FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print"wifi_getApAclDeviceNum() operation failed after delete operation";
                        else:
                            print "ACTUAL RESULT %d : wifi_delApAclDevice was not invoked successfully" %step;
                            print "TEST EXECUTION RESULT :FAILURE";
                            tdkTestObj.setResultStatus("FAILURE")
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Number of devices are not incremented by 1" %step;
                        print"Number of ApAcl devices after add operation : ",deviceNum_add;
                        print "TEST EXECUTION RESULT :FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print"wifi_getApAclDeviceNum() operation failed after add operation";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : The API was invoked not successfully" %step;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"wifi_getApAclDeviceNum() operation failed";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

