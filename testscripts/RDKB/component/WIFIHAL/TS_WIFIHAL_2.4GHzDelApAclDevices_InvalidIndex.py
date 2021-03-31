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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzDelApAclDevices_InvalidIndex</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_DelApAclDevices</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To invoke delApAclDevices() with invalid index and check if the operation fails</synopsis>
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
    <test_case_id>TS_WIFIHAL_535</test_case_id>
    <test_objective>To invoke delApAclDevices() with invalid index and check if the operation fails</test_objective>
    <test_type>Negative</test_type>
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
4.Check for the count if it is 0,add 2 mac address or else 1 mac address. No mac address needs to be added if it is greater than 2.
5.Add a ApAcl device by passing its mac address to the api wifi_addApAclDevice().
6.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is incremented by 1 or 2.
7.Invoke wifi_delApAclDevices() api with invalid index.
8.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is same as that of before invoking.
9. Revert operation
10.Unload the module.</automation_approch>
    <expected_output>When invalid index is passed to delApAclDevices(), the API should return failure. </expected_output>
    <priority>High</priority>
    <test_stub_interface>Wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzDelApAclDevices_InvalidIndex</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def revert(macAddress, olddeviceNum, index, obj):
    for deviceMac in macAddress:
        tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
        tdkTestObj.addParameter("methodName","addApAclDevice");
        tdkTestObj.addParameter("apIndex",index);
        tdkTestObj.addParameter("DeviceMacAddress",deviceMac);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "Added device :%s"%deviceMac
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "Device not added during revert operation :%s"%deviceMac
    getMethod = "getApAclDeviceNum"
    primitive = 'WIFIHAL_GetOrSetParamUIntValue'
    #Calling "getApAclDeviceNum" to get the number of connected devices after adding back the Mac addresses
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
    if expectedresult in actualresult:
        newdeviceNum = int(details.split(":")[1].strip());
        print "New device count:",newdeviceNum;
        if newdeviceNum == olddeviceNum:
            tdkTestObj.setResultStatus("SUCCESS");
            print"Successfully reverted back";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"Not reverted back Successfully";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print"wifi_getApAclDeviceNum() operation failed after add operation";

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import randint;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio2 = "2.4G"
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzDelApAclDevices_InvalidIndex');
#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio2);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
        tdkTestObj.addParameter("apIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details_new = tdkTestObj.getResultDetails();
        print "Mac Details",details_new;
        if expectedresult in actualresult:
           tdkTestObj.setResultStatus("SUCCESS");
           getMethod = "getApAclDeviceNum"
           primitive = 'WIFIHAL_GetOrSetParamUIntValue'
           tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive,idx, 0, getMethod);
           olddeviceNum = int(details.split(":")[1].strip());
           if olddeviceNum != "":
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 1: Get the number of devices in the filter list"
              print "EXPECTED RESULT 1: Should get the number of devices as a non empty value"
              print "ACTUAL RESULT 1: Received the number of devices as a NON EMPTY value"
              print "Device number : %s"%olddeviceNum
              print "TEST EXECUTION RESULT: SUCCESS"
              print"Number of ApAcl devices initially : ",olddeviceNum;
              # Generate MAC address
              mac_partial_1 = "7A:36:76:41:9A:"
              mac_partial_2 = "8A:46:86:51:AA:"
              x = str(randint(10,99))
              addMAC=[mac_partial_1+x, mac_partial_2+x];
              macAddress= [];
              if olddeviceNum == 0:
                 count=2;
                 #If olddeviceNum is 0, need to add 2 MAC addresses
              elif olddeviceNum == 1:
                  count=1;
                  #If oldDeviceNum is 1, need to add 1 MAC addresses
              else:
                  count=0;
                  #If olddEviceNum is any other, need not add MAC addresses
              if olddeviceNum > 0:
                 #Copying the initial MAC addresses
                 macAddress = details_new.split(";")[1].split("n")
                 for i in range(len(macAddress)):
                     macAddress[i] =  macAddress[i].replace("\\", '').strip()
              else:
                  print"No mac address listed"
                  print macAddress;
              #Adding the mac addresses depending on the value of count
              for i in range(0,count):
                  tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                  tdkTestObj.addParameter("methodName","addApAclDevice");
                  tdkTestObj.addParameter("apIndex",idx);
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
              getMethod = "getApAclDeviceNum";
              primitive = 'WIFIHAL_GetOrSetParamUIntValue';
              #Get the current ApAclDevice count
              tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
              print "TEST STEP 2: Get ApAclDevice Number"
              print "EXPECTED RESULT 2: getApAclDeviceNum should be successfully invoked"
              if expectedresult in actualresult:
                  deviceNum_add = int(details.split(":")[1].strip());
                  print "ACTUAL RESULT 2: %s"%details
                  print "TEST EXECUTION RESULT: SUCCESS"
                  if deviceNum_add == (olddeviceNum + count):
                      tdkTestObj.setResultStatus("SUCCESS");
                      print"Number of ApAcl devices after adding =",deviceNum_add;
                      #Deleting the ApAcl devices by passing Invalid Index
                      tdkTestObj = obj.createTestStep('WIFIHAL_DelApAclDevices');
                      tdkTestObj.addParameter("apIndex",100);
                      tdkTestObj.executeTestCase(expectedresult);
                      actualresult = tdkTestObj.getResult();
                      details = tdkTestObj.getResultDetails();
                      print"TEST STEP 3: Invoke DelApAclDevice with Invalid Index";
                      print"EXPECTED RESULT 3: DelApAclDevice should return failure"
                      if expectedresult not in actualresult:
                          tdkTestObj.setResultStatus("SUCCESS");
                          print"ACTUAL RESULT 3: %s"%details;
                          print"[TEST EXECUTION RESULT] : SUCCESS"
                          print"DelApAclDevices returns failure when Invalid index is passed";
                          getMethod = "getApAclDeviceNum"
                          primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                          # get the current ApAcl device count after trying to delete the ApAcl devices with invalid index
                          time.sleep(2)
                          tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
                          print "TEST STEP 4: Get ApAclDevice Number"
                          print "EXPECTED RESULT 4: getApAclDeviceNum should be successfully invoked"
                          if expectedresult in actualresult:
                              tdkTestObj.setResultStatus("SUCCESS");
                              deviceNum_del = int(details.split(":")[1].strip());
                              print "ACTUAL RESULT 4: %s"%details
                              print "TEST EXECUTION RESULT: SUCCESS"
                              if deviceNum_del == deviceNum_add:
                                  tdkTestObj.setResultStatus("SUCCESS");
                                  print"Number of ApAcl devices after passing Invalid Index to delApAclDevices is %d"%deviceNum_del;
                                  print"The number of ApAclDevices remains unchanged"
                                  #Reverting back
                                  #Delete the added ApAclDevices by passing valid index and then restrore initial state
                                  tdkTestObj = obj.createTestStep('WIFIHAL_DelApAclDevices');
                                  tdkTestObj.addParameter("apIndex",idx);
                                  tdkTestObj.executeTestCase(expectedresult);
                                  actualresult = tdkTestObj.getResult();
                                  details = tdkTestObj.getResultDetails();
                                  print"Reverting back to initial state"
                                  print"TEST STEP 5: Invoke DelApAclDevice with valid Index";
                                  print"EXPECTED RESULT 5: DelApAclDevice should return success"
                                  if expectedresult in actualresult:
                                      tdkTestObj.setResultStatus("SUCCESS");
                                      print "ACTUAL RESULT 5: %s"%details
                                      print "TEST EXECUTION RESULT: SUCCESS"
                                      getMethod = "getApAclDeviceNum"
                                      primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                                      #Calling "getApAclDeviceNum" to get the number of connected devices
                                      time.sleep(2)
                                      tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
                                      print "TEST STEP 6: Get ApAclDevice Number"
                                      print "EXPECTED RESULT 6: getApAclDeviceNum should be successfully invoked"
                                      if expectedresult in actualresult:
                                          newdeviceNum = int(details.split(":")[1].strip());
                                          print"Device count after invoking delApAclDevices :%d"%newdeviceNum
                                          tdkTestObj.setResultStatus("SUCCESS");
                                          print"ACTUAL RESULT 6: %s"%details
                                          print "TEST EXECUTION RESULT: SUCCESS"
                                          print "wifi_getApAclDeviceNum()is success after wifi_delApAclDevices() is invoked by passing valid Index"
                                          if newdeviceNum == 0:
                                              tdkTestObj.setResultStatus("SUCCESS");
                                              print "ApAclDevices are deleted"
                                              #Revert to initial state
                                              revert(macAddress, olddeviceNum, idx, obj);
                                          else:
                                              tdkTestObj.setResultStatus("FAILURE");
                                              print "DelApAclDevices did not delete all devices"
                                      else:
                                         tdkTestObj.setResultStatus("FAILURE");
                                         print"ACTUAL RESULT 6: %s"%details
                                         print"[TEST EXECUTION RESULT] : FAILURE"
                                         print "wifi_getApAclDeviceNum()failed after wifi_delApAclDevices() is invoked by passing valid Index"
                                  else:
                                      tdkTestObj.setResultStatus("FAILURE");
                                      print"ACTUAL RESULT 5: %s"%details
                                      print"[TEST EXECUTION RESULT] : FAILURE"
                                      print"ApAclDevices are not deleted";
                              else:
                                  tdkTestObj.setResultStatus("FAILURE");
                                  print"Number of ApAcl devices after deleting by passing Invalid Index is 0"
                          else:
                              tdkTestObj.setResultStatus("FAILURE");
                              print"ACTUAL RESULT 4: %s"%details
                              print"[TEST EXECUTION RESULT] : FAILURE"
                              print"wifi_getApAclDeviceNum()failed after wifi_delApAclDevices() is invoked by passing Invalid Index";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print"ACTUAL RESULT 3: %s"%details
                          print"[TEST EXECUTION RESULT] : FAILURE"
                          print"wifi_delApAclDevice() operation is success when Invalid Index is passed";
                          getMethod = "getApAclDeviceNum"
                          primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                          #Calling "getApAclDeviceNum" to get the number of connected devices
                          tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
                          if expectedresult in actualresult:
                              tdkTestObj.setResultStatus("SUCCESS");
                              newdeviceNum = int(details.split(":")[1].strip());
                              print"Device count after invoking delApAclDevices :%d"%newdeviceNum
                              if newdeviceNum == 0:
                                  tdkTestObj.setResultStatus("SUCCESS");
                                  print "ApAclDevices are deleted"
                                  #Revert to initial state
                                  revert(macAddress, olddeviceNum, idx, obj);
                              else:
                                  tdkTestObj.setResultStatus("FAILURE");
                                  print "DelApAclDevices did not delete all devices"
                          else:
                              tdkTestObj.setResultStatus("FAILURE");
                              print "wifi_getApAclDeviceNum()failed after wifi_delApAclDevices() is invoked by passing Invalid Index"
                  else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print"Device number not changed properly";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print"ACTUAL RESULT 2: %s"%details
                  print "[TEST EXECUTION RESULT] : FAILURE"
                  print"getApAclDeviceNum() operation failed";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the number of devices in the filter list"
            print "EXPECTED RESULT 1: Should get the number of devices as a non empty value"
            print "ACTUAL RESULT 1: Received the number of devices as an EMPTY value"
            print "Device number : %s"%olddeviceNum
            print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");

