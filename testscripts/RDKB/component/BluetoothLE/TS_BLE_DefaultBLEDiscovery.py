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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_BLE_DefaultBLEDiscovery</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>BLE_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery is False</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_BluetoothLE_5</test_case_id>
    <test_objective>Check if the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery is False</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>TDK agent should be running in the DUT and DUT should be online in TDK test manager</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery
Device.X_CISCO_COM_DeviceControl.FactoryReset</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Get and save the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery
3. If current state is false set it as true
4. Save the device's state using saveCurrentState()
5. Do factory reset using Device.X_CISCO_COM_DeviceControl.FactoryReset
6. Restore device state using restorePreviousStateAfterReboot()
7. Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio and check if it is false
8. Revert the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio
9. Unload tdkbtr181 module</automation_approch>
    <expected_output>Default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery should be True</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_BLE_DefaultBLEDiscovery</test_script>
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
obj1 = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_BLE_DefaultBLEDiscovery');
obj1.configureTestCase(ip,port,'TS_BLE_DefaultBLEDiscovery');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    BLEDiscoveryOrg = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the enable status of BLEDiscovery";
        print "EXPECTED RESULT 1: Should get the enable status of BLEDiscovery";
        print "ACTUAL RESULT 1: BLEDiscovery Enable status is %s" %BLEDiscoveryOrg;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if BLEDiscoveryOrg == "false":
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery")
            tdkTestObj.addParameter("ParamValue", "true");
            tdkTestObj.addParameter("Type","boolean");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            newBLERadio = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: If current enable state is false, set it as true";
                print "EXPECTED RESULT 2: Should set the enable status of BLEDiscovery as true";
                print "ACTUAL RESULT 2: BLEDiscovery set is success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: If current enable state is false, set it as true";
                print "EXPECTED RESULT 2: Should set the enable status of BLEDiscovery as true";
                print "ACTUAL RESULT 2: BLEDiscovery set is success"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                obj.unloadModule("tdkbtr181");
                obj1.unloadModule("pam");
                exit();

	#save device's current state before it goes for reboot
        obj.saveCurrentState();

        #Initiate Factory reset before checking the default value
        tdkTestObj = obj1.createTestStep('pam_Setparams');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
        tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
        tdkTestObj.addParameter("Type","string");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Initiate factory reset ";
            print "EXPECTED RESULT 3: Should initiate factory reset";
            print "ACTUAL RESULT 3: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Restore the device state saved before reboot
            obj.restorePreviousStateAfterReboot();

	    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    	    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery");

    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    newBLEDiscovery = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and newBLEDiscovery == "false":
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 4: Get the default BLEDiscovery after factory reset";
    	        print "EXPECTED RESULT 4: Should get the default  BLEDiscovery as false";
    	        print "ACTUAL RESULT 4: BLEDiscovery status is %s" %newBLEDiscovery;
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Get the default BLEDiscovery after factory reset";
                print "EXPECTED RESULT 4: Should get the default  BLEDiscovery as false";
                print "ACTUAL RESULT 4: BLEDiscovery status is %s" %newBLEDiscovery;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Discovery");
            tdkTestObj.addParameter("ParamValue",BLEDiscoveryOrg);
            tdkTestObj.addParameter("Type","boolean");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            newBLERadio = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: Revert  enable status of BLEDiscovery same as previous status";
                print "EXPECTED RESULT 5: Should revert the enable status of BLEDiscovery same as previous status";
                print "ACTUAL RESULT 5: BLEDiscovery revert is success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 5: Revert  enable status of BLEDiscovery same as previous status";
                print "EXPECTED RESULT 5: Should revert the enable status of BLEDiscovery same as previous status";
                print "ACTUAL RESULT 5: BLEDiscovery revert failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Initiate factory reset ";
            print "EXPECTED RESULT 2: Should inititate factory reset";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the enable status of BLEDiscovery";
        print "EXPECTED RESULT 1: Should get the enable status of BLEDiscovery";
        print "ACTUAL RESULT 1: BLEDiscovery Enable status is %s" %BLEDiscoveryOrg;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("pam");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
