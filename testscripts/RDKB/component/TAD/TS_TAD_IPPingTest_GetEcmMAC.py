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
  <name>TS_TAD_IPPingTest_GetEcmMAC</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and Device.DeviceInfo.X_CISCO_COM_BaseMacAddress are same </synopsis>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TAD_65</test_case_id>
    <test_objective>To validate Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and Device.DeviceInfo.X_CISCO_COM_BaseMacAddress are same</test_objective>
    <test_type>Positive</test_type>
    <test_setup> Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get</api_or_interface_used>
    <input_parameters>
Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC
Device.DeviceInfo.X_CISCO_COM_BaseMacAddress
</input_parameters>
    <automation_approch>1. Load  TAD modules
2. From script invoke TADstub_Get and get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC
3.From script invoke TADstub_Get and get the value of Device.DeviceInfo.X_CISCO_COM_BaseMacAddress
4.Check whether both values are same
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>Value retreived by Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC should give ecm mac address</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_IPPingTest_GetEcmMAC</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_IPPingTest_GetEcmMAC');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TADstub_Get');
    tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details1 = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and details1 != "":
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC ";
       print "EXPECTED RESULT 1: Should get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC";
       print "ACTUAL RESULT 1: %s" %details1;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj = obj.createTestStep('TADstub_Get');
       tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_CISCO_COM_BaseMacAddress");
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details2 = tdkTestObj.getResultDetails();
       if expectedresult in actualresult and details2 != "":
         #Set the result status of execution
         tdkTestObj.setResultStatus("SUCCESS");
         print "TEST STEP 2: Get the value of Device.DeviceInfo.X_CISCO_COM_BaseMacAddress";
         print "EXPECTED RESULT 2: Should get the value of Device.DeviceInfo.X_CISCO_COM_BaseMacAddress";
         print "ACTUAL RESULT 2: %s" %details2;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : SUCCESS";
         if details1 == details2:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 3: Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and Device.DeviceInfo.X_CISCO_COM_BaseMacAddress should be same ";
           print "EXPECTED RESULT 3:Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and Device.DeviceInfo.X_CISCO_COM_BaseMacAddressare same ";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
         else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 3: Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and Device.DeviceInfo.X_CISCO_COM_BaseMacAddressshould be same ";
           print "EXPECTED RESULT 3:Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC and Device.DeviceInfo.X_CISCO_COM_BaseMacAddress are not same ";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
       else:
         #Set the result status of execution
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 2: Get the value of Device.DeviceInfo.X_CISCO_COM_BaseMacAddress";
         print "EXPECTED RESULT 2: Should get the value of Device.DeviceInfo.X_CISCO_COM_BaseMacAddress";
         print "ACTUAL RESULT 2: %s" %details2;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";
    else:
       #Set the result status of execution
       tdkTestObj.setResultStatus("FAILURE");
       print "TEST STEP 1:Get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC";
       print "EXPECTED RESULT 1: Should get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.ecmMAC";
       print "ACTUAL RESULT 1: %s" %details1;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");

else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";


