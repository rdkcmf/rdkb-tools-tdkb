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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ETHAGENT_SetWANEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ETHAgent_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled returns failure when set to false in RPI and  when set to true in real devices</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <test_case_id>TC_ETHAGENT_02</test_case_id>
    <test_objective>To check if Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled returns failure when set to false in RPI and  when set to true in real devices</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Device should not be in ethwan mode or ethwan setup</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled</input_parameters>
    <automation_approch>1.Load module
2.Get the device type from properties file
3.If it is RPI,set Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false
4.Check if setting Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false returns failure
5.If it is not RPI, set Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true
6.Check if setting Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true returns failure
7.Unload module</automation_approch>
    <except_output>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled should return failure when set to false in RPI and  when set to true in real devices</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_ETHAGENT_SetWANEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");


#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_SetWANEnabled.py');
obj1.configureTestCase(ip,port,'TS_ETHAGENT_SetWANEnabled.py');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile DEVICETYPE" %TDK_PATH;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    devicetype = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and devicetype != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the DEVICE TYPE"
        print "EXPECTED RESULT 1: Should get the device type";
        print "ACTUAL RESULT 1:Device type  %s" %devicetype;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        if devicetype == "RPI":
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
            tdkTestObj.addParameter("ParamValue","false");
            tdkTestObj.addParameter("Type","string");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult not in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false";
                print "EXPECTED RESULT 2 : Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false"
                print "ACTUAL RESULT 2 :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false";
                print "EXPECTED RESULT 2: Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to false";
                print "ACTUAL RESULT 2: Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled is set to false";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","string");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult not in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true";
                print "EXPECTED RESULT 2: Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true"
                print "ACTUAL RESULT 2 :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true";
                print "EXPECTED RESULT 2: Should not set the Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true";
                print "ACTUAL RESULT 2: Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled to true";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the DEVICE TYPE";
        print "EXPECTED RESULT 1: Should get the DEVICE TYPE";
        print "ACTUAL RESULT 1:Failed to get DEVICE TYPE";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";


