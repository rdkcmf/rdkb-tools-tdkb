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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_BLE_GetBLERadio</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>BLE_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if BLERadio Enable status from rfc_configdata.txt and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio are equal</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_BluetoothLE_4</test_case_id>
    <test_objective>This test case is to check if BLERadio Enable status from rfc_configdata.txt and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio are equal</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>TDK agent should be running in the DUT and DUT should be online in TDK test manager</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio
3. Get the value of tr181.Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio from rfc_configdata.txt and should be equal to the tr181 value
4. Unload tdkbtr181 module</automation_approch>
    <expected_output>BLERadio Enable status from rfc_configdata.txt and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio should be equal</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_BLE_GetBLERadio</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2 = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_BLE_GetBLERadio');
obj2.configureTestCase(ip,port,'TS_BLE_GetBLERadio');
#Get the result of connection with test component and STB
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus2=obj2.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper() and  "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj2.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    BLERadioOrg = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the enable status of BLERadio";
        print "EXPECTED RESULT 1: Should get the enable status of BLERadio";
        print "ACTUAL RESULT 1: BLERadio Enable status is %s" %BLERadioOrg;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj2.createTestStep('ExecuteCmd');
        query="cat /tmp/rfc_configdata.txt | grep -i \"tr181.Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio\"";
        print "query:%s" %query
        tdkTestObj.addParameter("command", query)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n","");
        details=details.split("#~")[1];
        if expectedresult in actualresult and details != "" and details == BLERadioOrg:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Enable status of BLERadio from rfc_configdata.txt and tr181 query should be equal";
           print "EXPECTED RESULT 2: Should get status of BLERadio from rfc_configdata.txt and tr181 query  equal";
           print "ACTUAL RESULT 2: BLERadio status from tr181 is %s and from rfc_configdata.txt is %s" %(BLERadioOrg,details);
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Enable status of BLERadio from rfc_configdata.txt and tr181 query should be equal";
           print "EXPECTED RESULT 2: Should get status of BLERadio from rfc_configdata.txt and tr181 query  equal";
           print "ACTUAL RESULT 2: BLERadio status from tr181 is %s and from rfc_configdata.txt is %s" %(BLERadioOrg,details);
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the enable status of BLERadio";
        print "EXPECTED RESULT 1: Should get the enable status of BLERadio";
        print "ACTUAL RESULT 1: BLERadio Enable status is %s" %BLERadioOrg;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
