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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzDelApAclDevice_InvalidIndex</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_AddorDelApAclDevice</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To pass Invalid Index to delApAclDevice HAL API and verify if the operation fails</synopsis>
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
    <test_case_id>TS_WIFIHAL_533</test_case_id>
    <test_objective>To pass Invalid Index to delApAclDevice HAL API and verify if the operation fails</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAclDeviceNum()
wifi_addApAclDevice()
wifi_delApAclDevice()</api_or_interface_used>
    <input_parameters>methodName : getApAclDeviceNum
methodName : addApAclDevice
methodName : delApAclDevice
apIndex : 1
</input_parameters>
    <automation_approch>1.Load the module.
2.Get the number of ApAcl devices using the wifi_getApAclDeviceNum() API
3.Add a ApAcl device by passing its mac address to the api wifi_addApAclDevice().
4.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is incremented by 1.
5. Invoking wifi_delApAclDevice() api with invalid Index and check if it returns failure.
6.Get the number of ApAcl devices using wifi_getApAclDeviceNum() and check if it is unchanged after delete operation
7.Revert to initial state
8.Unload the module.</automation_approch>
    <expected_output>delApAclDevice HAL API should return failure when Invalid Index is passed</expected_output>
    <priority>High</priority>
    <test_stub_interface>Wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzDelApAclDevice_InvalidIndex</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import randint
radio = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzDelApAclDevice_InvalidIndex');
#Get the result of connection with test component and DUT
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
        expectedresult = "SUCCESS"
        radioIndex = idx
        getMethod = "getApAclDeviceNum"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
        print"TEST STEP 1 : Get ApAclDevice Number"
        print"EXPECTED RESULT 1 : getApAclDeviceNum successfully retrieves the Number "
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print"ACTUAL RESULT 1 : %s"%details;
            print"[TEST EXECUTION RESULT] : SUCCESS"
            deviceNum = int(details.split(":")[1].strip());
            print"Number of ApAcl devices initially =",deviceNum;
            #Primitive test case which associated to this Script
            tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
            #Giving the method name to invoke the api wifi_addApAclDevice()
            tdkTestObj.addParameter("methodName","addApAclDevice");
            tdkTestObj.addParameter("apIndex",idx);
            # Generate MAC address
            mac_partial = "7A:36:76:41:9A:"
            x = str(randint(10,99))
            mac = mac_partial+x
            print "Mac Address to be added : %s"%mac
            tdkTestObj.addParameter("DeviceMacAddress",mac);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print"TEST STEP 2 : Add the MAC address using addApAclDevice"
            print"EXPECTED RESULT 2 : addApAclDevice should be success"
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print"ACTUAL RESULT 2 : %s"%details;
                print"[TEST EXECUTION RESULT] : SUCCESS"
                expectedresult = "SUCCESS"
                radioIndex = idx
                getMethod = "getApAclDeviceNum"
                primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                print"TEST STEP 3 : Get ApAclDevice Number"
                print"EXPECTED RESULT 3 : getApAclDeviceNum successfully retrieves the Number "
                if expectedresult in actualresult:
                    deviceNum_add = int(details.split(":")[1].strip());
                    deviceNum_new = deviceNum_add - deviceNum;
                    if deviceNum_new == 1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print"ACTUAL RESULT 3 : %s"%details;
                        print"[TEST EXECUTION RESULT] : SUCCESS"
                        print"Number of ApAcl devices after adding =",deviceNum_add;
                        #Primitive test case which associated to this Script
                        tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                        #Giving the method name to invoke the api wifi_delApAclDevice
                        tdkTestObj.addParameter("methodName","delApAclDevice");
                        #Give invalid AccessPoint Index
                        tdkTestObj.addParameter("apIndex",100);
                        tdkTestObj.addParameter("DeviceMacAddress",mac);
                        expectedresult="FAILURE";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        print"TEST STEP 4: delApAclDevice invoked with Invalid Index";
                        print"EXPECTED RESULT 4: delApAclDevice should return failure";
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print"ACTUAL RESULT 4: %s"%details
                            print"[TEST EXECUTION RESULT] : SUCCESS"
                            print"ApAclDevice is not deleted when an Invalid Index is passed";
                            expectedresult = "SUCCESS"
                            radioIndex = idx
                            getMethod = "getApAclDeviceNum"
                            primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                            print"TEST STEP 5 : Get ApAclDevice Number"
                            print"EXPECTED RESULT 5 : getApAclDeviceNum successfully retrieves the Number "
                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print"ACTUAL RESULT 5 : %s"%details;
                                print"[TEST EXECUTION RESULT] : SUCCESS"
                                deviceNum_del = int(details.split(":")[1].strip());
                                print"Number of ApAcl devices after deleting  =",deviceNum_del;
                                if deviceNum_del == deviceNum + 1:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print"Number of ApAcl devices remains unchanged when delApAclDevice is invoked with Invalid Index";
                                    #Revert Operation
                                    tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                                    #Giving the method name to invoke the api wifi_delApAclDevice
                                    tdkTestObj.addParameter("methodName","delApAclDevice");
                                    tdkTestObj.addParameter("apIndex",idx);
                                    tdkTestObj.addParameter("DeviceMacAddress",mac);
                                    expectedresult="SUCCESS";
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    details = tdkTestObj.getResultDetails();
                                    print"TEST STEP 6: Revert ApAclDevice to initial state";
                                    print"EXPECTED RESULT 6: DelApAclDevice operation should be success";
                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print"ACTUAL RESULT 6: %s"%details;
                                        print"[TEST EXECUTION RESULT] : SUCCESS"
                                        print"DelApAclDevice returns Success";
                                        #Cross check with getApAclDeviceNum
                                        expectedresult = "SUCCESS"
                                        radioIndex = idx
                                        getMethod = "getApAclDeviceNum"
                                        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                                        print"TEST STEP 7: Get ApAclDevice Number"
                                        print"EXPECTED RESULT 7 : getApAclDeviceNum successfully retrieves the Number "
                                        if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print"ACTUAL RESULT 7: %s"%details;
                                            print"[TEST EXECUTION RESULT] : SUCCESS"
                                            deviceNum_del = int(details.split(":")[1].strip());
                                            print"Number of ApAcl devices after deleting  =",deviceNum_del;
                                            if deviceNum_del == deviceNum:
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print"Revert Operation is Success"
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print"Revert Operation has Failed"
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print"wifi_getApAclDeviceNum() operation failed after revert operation"
                                            print"ACTUAL RESULT 7: %s"%details;
                                            print"[TEST EXECUTION RESULT] : FAILURE"
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print"ApAclDevice is not successfully reverted to initial state";
                                        print"ACTUAL RESULT 6: %s"%details;
                                        print"[TEST EXECUTION RESULT] : FAILURE"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print"wifi_getApAclDeviceNum() operation failed after delete operation";
                                    print"ACTUAL RESULT 5: %s"%details;
                                    print"[TEST EXECUTION RESULT] : FAILURE"
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print"delApAclDevice returns success when Invalid Index is passed";
                                print"ACTUAL RESULT 4: %s"%details;
                                print"[TEST EXECUTION RESULT] : FAILURE"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Number of ApAclDevices not incremented after add operation";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print"wifi_getApAclDeviceNum() operation failed after add operation";
                        print"ACTUAL RESULT 3: %s"%details;
                        print"[TEST EXECUTION RESULT] : FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print"wifi_addApAclDevice() operation failed";
                    print"ACTUAL RESULT 2: %s"%details;
                    print"[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"wifi_getApAclDeviceNum() operation failed";
                print"ACTUAL RESULT 1: %s"%details;
                print"[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");

