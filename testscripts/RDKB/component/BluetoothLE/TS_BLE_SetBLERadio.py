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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_BLE_SetBLERadio</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>BLE_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Do set operation to toggle the enable state of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_BluetoothLE_2</test_case_id>
    <test_objective>Do set operation to toggle the enable state of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>TDK agent should be running in the DUT and DUT should be online in TDK test manager</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Get and save the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio
3. Do a set operation to toggle the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio
4. Do a get and check whether the set operation was success or not
5. Revert back the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio
6. Unload tdkbtr181 module</automation_approch>
    <expected_output>Toggling of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_BLE_SetBLERadio</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_BLE_SetBLERadio');

#Get the result of connection with test component and STB
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    BLERadioOrg = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the BLERadio status";
        print "EXPECTED RESULT 1: Should get the BLERadio status";
        print "ACTUAL RESULT 1: BLERadio status is %s" %BLERadioOrg;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if BLERadioOrg == "true":
            setBLERadio = "false"
        else:
            setBLERadio = "true"

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio");
        tdkTestObj.addParameter("ParamValue",setBLERadio);
        tdkTestObj.addParameter("Type","boolean");

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();
        newBLERadio = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and expectedresult in actualresult1 and newBLERadio == setBLERadio:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Toggle the enable status of BLERadio";
            print "EXPECTED RESULT 2: Should toggle the enable status of BLERadio";
            print "ACTUAL RESULT 2: BLERadio toggle is success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Revert to the original value of BLERadio status
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio");
            tdkTestObj.addParameter("ParamValue",BLERadioOrg);
            tdkTestObj.addParameter("Type","boolean");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            newBLERadio = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Revert  enable status of BLERadio same as previous status";
                print "EXPECTED RESULT 3: Should revert the enable status of BLERadio same as previous status";
                print "ACTUAL RESULT 3: BLERadio revert is success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Revert  enable status of BLERadio same as previous status";
                print "EXPECTED RESULT 3: Should revert the enable status of BLERadio same as previous status";
                print "ACTUAL RESULT 3: BLERadio revert failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Toggle the enable status of BLERadio";
            print "EXPECTED RESULT 2: Should toggle the enable status of BLERadio";
            print "ACTUAL RESULT 2: BLERadio toggle is success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the BLERadio status";
        print "EXPECTED RESULT 1: Should get the BLERadio status";
        print "ACTUAL RESULT 1: BLERadio status is %s" %BLERadioOrg;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
