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
  <name>TS_PAM_CheckDefaultLocalIPv4SubnetRange_EqualToLanSubnetMask</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Default Local IPv4 Subnet Range equal to Lan Subnet Mask</synopsis>
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
    <test_case_id>TC_PAM_207</test_case_id>
    <test_objective>This test case is to check if Default Local IPv4 Subnet Range equal to Lan Subnet Mask</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand ,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask
Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultLocalIPv4SubnetRange</input_parameters>
    <automation_approch>1.Load the module
2.Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultLocalIPv4SubnetRange
3.Get the value for Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask
4.Check if Default Local IPv4 Subnet Range is equal to Lan Subnet Mask
5.Unload the module</automation_approch>
    <expected_output>The Default Local IPv4 Subnet Range is expected to be equal to Lan Subnet Mask</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckDefaultLocalIPv4SubnetRange_EqualToLanSubnetMask</test_script>
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
obj.configureTestCase(ip,port,'TS_PAM_CheckDefaultLocalIPv4SubnetRange_EqualToLanSubnetMask');
obj1.configureTestCase(ip,port,'TS_PAM_CheckDefaultLocalIPv4SubnetRange_EqualToLanSubnetMask');

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
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_UIBranding.DefaultLocalIPv4SubnetRange");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    subnetRange = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the value of Default Local IPv4 Subnet Range";
        print "EXPECTED RESULT 1: Should get the Default Local IPv4 Subnet Range";
        print "ACTUAL RESULT 1: Default Local IPv4 Subnet Range :%s" %subnetRange;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        LanSubnetMask = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the value of LanSubnetMask";
            print "EXPECTED RESULT 2: Should get the LanSubnetMask";
            print "ACTUAL RESULT 2: LanSubnetMask is :%s" %LanSubnetMask;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if subnetRange == LanSubnetMask:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if LanSubnetMask and Default Local IPv4 Subnet Range are equal";
                print "EXPECTED RESULT 3: Should get the LanSubnetMask and Default Local IPv4 Subnet Range equal";
                print "ACTUAL RESULT 3: LanSubnetMask is :%s and Default Local IPv4 Subnet Range is %s" %(LanSubnetMask,subnetRange);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if LanSubnetMask and Default Local IPv4 Subnet Range are equal";
                print "EXPECTED RESULT 3: Should get the LanSubnetMask and Default Local IPv4 Subnet Range equal";
                print "ACTUAL RESULT 3: LanSubnetMask is :%s and Default Local IPv4 Subnet Range is %s" %(LanSubnetMask,subnetRange);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the value of LanSubnetMask";
            print "EXPECTED RESULT 2: Should get the LanSubnetMask";
            print "ACTUAL RESULT 2: LanSubnetMask is :%s" %LanSubnetMask;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the value of Default Local IPv4 Subnet Range";
        print "EXPECTED RESULT 1: Should get the Default Local IPv4 Subnet Range";
        print "ACTUAL RESULT 1: Default Local IPv4 Subnet Range :%s" %subnetRange;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
