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
  <version>36</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TAD_IPPingTest_GetPartnerID</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and validate with value in tdk properties file</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>4</execution_time>
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
    <test_case_id>TC_TAD_74</test_case_id>
    <test_objective>To get value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and validate with value in tdk properties file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get,TADstub_Set</api_or_interface_used>
    <input_parameters>
Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID
</input_parameters>
    <automation_approch>1. Load  TAD modules
2. From script invoke TADstub_Get and get value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID
3.From python script, invoke ExecuteCmd() stub function to get the PARTNER_ID from the platform property file and validate both values
4.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>Value retreived by Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and from tdkproperties should be same</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_IPPingTest_GetPartnerID</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_IPPingTest_GetPartnerID');
sysObj.configureTestCase(ip,port,'TS_TAD_IPPingTest_GetPartnerID');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile PARTNER_ID" %TDK_PATH;
    print command;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details1 = tdkTestObj.getResultDetails();
    details1 = details1.replace("\\n", "");
    if expectedresult in actualresult and details1 != "":
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get value of PARTNER_ID"
       print "EXPECTED RESULT 1: Should get the value of PARTNER_ID";
       print "ACTUAL RESULT 1:  %s" %details1;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj = obj.createTestStep('TADstub_Get');
       tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID");
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details2 = tdkTestObj.getResultDetails();
       if expectedresult in actualresult and details2 != "":
         #Set the result status of execution
         tdkTestObj.setResultStatus("SUCCESS");
         print "TEST STEP 2: Get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID";
         print "EXPECTED RESULT 2: Should get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID";
         print "ACTUAL RESULT 2: %s" %details2;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : SUCCESS";
         if details1 == details2:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 3: Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and PARTNER_ID should be same ";
           print "EXPECTED RESULT 3:Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and PARTNER_ID are same ";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
         else:
           # Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 3: Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and PARTNER_ID should be same ";
           print "EXPECTED RESULT 3:Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID and PARTNER_ID are not same ";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
       else:
         #Set the result status of execution
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 2: Get the value of Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID";
         print "EXPECTED RESULT 1: Should get the Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.PartnerID";
         print "ACTUAL RESULT 2: %s" %details2;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";

    else:
       tdkTestObj.setResultStatus("FAILURE");
       print "TEST STEP 1: Get ping test run value"
       print "EXPECTED RESULT 1: Should get the ping test run value";
       print "ACTUAL RESULT 1:  %s" %details1;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");
    sysObj.unloadModule("sysutil");
else:
        print "Failed to load module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";


