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
  <version>2</version>
  <name>TS_PAM_CheckDefaultAdminIP_EqualToLANIP</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Default Admin IP is equal to LAN IP Address</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_206</test_case_id>
    <test_objective>This test case is to check  if Default Admin IP equal to LANIP Address</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand ,RPI,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
pam_SetParameterValues</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultAdminIP
Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</input_parameters>
    <automation_approch>1.Load the module
2.Get the value of  Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultAdminIP
3.Get the Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress
4.Check if the Default Admin IP equal to LANIP Address
5.Unload the module</automation_approch>
    <expected_output>The Default Admin IP and LANIP Address are expected to be equal</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_PAM_CheckDefaultAdminIP_EqualToLANIP</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckDefaultAdminIP_EqualToLANIP');
obj1.configureTestCase(ip,port,'TS_PAM_CheckDefaultAdminIP_EqualToLANIP');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultAdminIP");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    DefaultAdminIP = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the value of DefaultAdminIP";
        print "EXPECTED RESULT 1: Should get the DefaultAdminIP";
        print "ACTUAL RESULT 1: DefaultAdminIP :%s" %DefaultAdminIP;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        LANIPAddress = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the value of LANIPAddress";
            print "EXPECTED RESULT 2: Should get the LANIPAddress";
            print "ACTUAL RESULT 2: LANIPAddress is :%s" %LANIPAddress;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if DefaultAdminIP == LANIPAddress:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if LANIPAddress and DefaultAdminIP are equal";
                print "EXPECTED RESULT 3: Should get the LANIPAddress and DefaultAdminIP equal";
                print "ACTUAL RESULT 3: LANIPAddress is :%s and DefaultAdminIP is %s" %(LANIPAddress,DefaultAdminIP);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if LANIPAddress and DefaultAdminIP are equal";
                print "EXPECTED RESULT 3: Should get the LANIPAddress and DefaultAdminIP equal";
                print "ACTUAL RESULT 3: LANIPAddress is :%s and DefaultAdminIP is %s" %(LANIPAddress,DefaultAdminIP);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the value of LANIPAddress";
            print "EXPECTED RESULT 2: Should get the LANIPAddress";
            print "ACTUAL RESULT 2: LANIPAddress is :%s" %LANIPAddress;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the value of DefaultAdminIP";
        print "EXPECTED RESULT 1: Should get the DefaultAdminIP";
        print "ACTUAL RESULT 1: DefaultAdminIP :%s" %DefaultAdminIP;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
