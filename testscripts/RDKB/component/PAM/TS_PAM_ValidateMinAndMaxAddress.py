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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_PAM_ValidateMinAndMaxAddress</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the Parameters Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress have the expected values when Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress are set to 255.255.255.0 and 10.1.10.1 respectively and DUT is rebooted.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_245</test_case_id>
    <test_objective>To check if the Parameters Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress have the expected values when Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress are set to 255.255.255.0 and 10.1.10.1 respectively and DUT is rebooted.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask
paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress
paramName : Device.DHCPv4.Server.Pool.1.MinAddress
paramName : Device.DHCPv4.Server.Pool.1.MaxAddress
subnet_mask = "255.255.255.0"
lanip_addr = "10.1.10.1"</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and store them.
3. Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to 255.255.255.0 and 10.1.10.1 respectively. Check if SET operation is success.
4. Validate the SET with GET
5. Reboot the DUT.
6. Once the device comes up, check the values of Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress.
7. The Min Address should be 10.1.10.2 and the Max Address should be 10.1.10.253.
8. Revert to initial state
9. Unload the modules</automation_approch>
    <expected_output>The Parameters Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress should have the expected values when Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress are set to 255.255.255.0 and 10.1.10.1 respectively and DUT is rebooted.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_ValidateMinAndMaxAddress</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
import time;
from tdkbVariables import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_ValidateMinAndMaxAddress');
obj1.configureTestCase(ip,port,'TS_PAM_ValidateMinAndMaxAddress');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the initial Lan IP and Subnet Mask and store it
    tdkTestObj = obj.createTestStep('TADstub_Get');
    paramList=["Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress", "Device.DHCPv4.Server.Pool.1.MinAddress", "Device.DHCPv4.Server.Pool.1.MaxAddress"]
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
    print "\nTEST STEP 1: Get the initial values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress";
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "" and orgValue[3] != "" :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Lan Subnet Mask is : %s, Lan IP Address is : %s, Min Address : %s, Max Address : %s" %(orgValue[0],orgValue[1],orgValue[2],orgValue[3]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set the Subnet Mask and Lan IP to new values
        subnet_mask = "255.255.255.0"
        lanip_addr = "10.1.10.1";

        tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
        tdkTestObj.addParameter("paramList", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask|%s|string|Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress|%s|string"%(subnet_mask,lanip_addr));
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        sleep(30);

        print "\nTEST STEP 2 : Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to %s and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to %s" %(subnet_mask,lanip_addr);
        print "EXPECTED RESULT 2 : SET operations should be success";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Set operation success; Details : %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS";

            #Validate the SET with GET
            paramList=["Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress"];
            tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)
            print "\nTEST STEP 3: Get the values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask an Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress";
            print "EXPECTED RESULT 3: The values should be retrieved successfully and should be the same as set values";

            if expectedresult in status and setValue[0] == subnet_mask and setValue[1] == lanip_addr:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Values after the GET are same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Reboot the device
                print "\nDevice going for reboot....";
                obj.initiateReboot();
                time.sleep(300);

                #Once the device comes up, check if the Min and Max Address have the expected values
                expected_MinAddr = "10.1.10.2";
                expected_MaxAddr = "10.1.10.253";

                paramList=["Device.DHCPv4.Server.Pool.1.MinAddress", "Device.DHCPv4.Server.Pool.1.MaxAddress"];
                tdkTestObj,status,getValue = getMultipleParameterValues(obj,paramList)
                print "\nTEST STEP 4: Get the values of Device.DHCPv4.Server.Pool.1.MinAddress as %s and Device.DHCPv4.Server.Pool.1.MaxAddress as %s" %(expected_MinAddr, expected_MaxAddr);
                print "EXPECTED RESULT 4: The values should be retrieved successfully and should be the same as expected values";
                print "Expected Min Address : ", expected_MinAddr;
                print "Actual Min Address : ", getValue[0];
                print "Expected Max Address : ", expected_MaxAddr;
                print "Actual Max Address : ", getValue[1];

                if expectedresult in status and getValue[0] == expected_MinAddr and getValue[1] == expected_MaxAddr:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4   : Values after the GET are same as the expected values : %s, %s" %(getValue[0],getValue[1]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4   : Values after the GET are not same as the expected values : %s, %s" %(getValue[0],getValue[1]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert to initial state
                tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                tdkTestObj.addParameter("paramList", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask|%s|string|Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress|%s|string|Device.DHCPv4.Server.Pool.1.MinAddress|%s|string|Device.DHCPv4.Server.Pool.1.MaxAddress|%s|string"%(orgValue[0],orgValue[1],orgValue[2],orgValue[3]));
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                sleep(30);

                print "\nTEST STEP 5 : Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to %s, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to %s, Device.DHCPv4.Server.Pool.1.MinAddress to %s and Device.DHCPv4.Server.Pool.2.MinAddress to %s" %(orgValue[0],orgValue[1],orgValue[2],orgValue[3]);
                print "EXPECTED RESULT 5 : SET operations should be success";

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 5: Revert operation success; Details : %s" %details;
                    print "TEST EXECUTION RESULT :SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 5: Revert operation failed; Details : %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Values after the GET are not same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Set operation failed; Details : %s" %details;
            print "TEST EXECUTION RESULT :FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: GET operation failed";
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
