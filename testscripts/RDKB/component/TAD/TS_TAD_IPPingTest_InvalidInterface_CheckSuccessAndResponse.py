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
  <name>TS_TAD_IPPingTest_InvalidInterface_CheckSuccessAndResponse</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the ping test done using Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run with an invalid interface is success or not</synopsis>
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
    <test_case_id>TC_TAD_60</test_case_id>
    <test_objective>Check if the ping test done using Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run with an invalid interface is success or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI.</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get, TADstub_Set</api_or_interface_used>
    <input_parameters>Device.IP.Diagnostics.IPPing.Host
Device.IP.Diagnostics.IPPing.Interface
Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run
Device.IP.Diagnostics.IPPing.SuccessCount
Device.IP.Diagnostics.IPPing.AverageResponseTime
Device.IP.Diagnostics.IPPing.MinimumResponseTime
Device.IP.Diagnostics.IPPing.MaximumResponseTime</input_parameters>
    <automation_approch>1. Load TAD module
2. Get the value of Device.IP.Diagnostics.TraceRoute.Host
3. Get the hostname from tdkb config file
4. If the current hostname is not same as the one in config file, set it as new host name
5.Set Device.IP.Diagnostics.IPPing.Interface as an invalid interface
6. Set Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run as true to start the ping test
7. After ping test, check if the success count, average response time, minimum response time, maximum response time is greater than zero
8. Unload the TAD module</automation_approch>
    <except_output>The ping test done using Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run with an invalid interface should be success</except_output>
    <priority>High</priority>
    <test_stub_interface>tad</test_stub_interface>
    <test_script>TS_TAD_IPPingTest_InvalidInterface_CheckSuccessAndResponse</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
import time;
import tdkutility;
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_IPPingTest_InvalidInterface_CheckSuccessAndResponse');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    host = tdkutility.readtdkbConfigFile(obj);
    tdkTestObj = obj.createTestStep('TADstub_Get');
    tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.IPPing.Host");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgHost = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        if host == "NULL":
             tdkTestObj.setResultStatus("FAILURE");
             print "Host name not available in tdkb config file"
        else:
             if orgHost != host :
                 tdkTestObj = obj.createTestStep('TADstub_Set');
                 tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.Host");
                 tdkTestObj.addParameter("ParamValue",host);
                 tdkTestObj.addParameter("Type","string");
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 details = tdkTestObj.getResultDetails();
                 if expectedresult in actualresult:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 2: Set the host of IPPing";
                     print "EXPECTED RESULT 2: Should set the host of IPPing";
                     print "ACTUAL RESULT 2: %s" %details;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                 else:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 2: Set the host of IPPing";
                     print "EXPECTED RESULT 2: Should set the host of IPPing";
                     print "ACTUAL RESULT 2: %s" %details;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";
                     obj.unloadModule("tad");
                     exit();

             tdkTestObj = obj.createTestStep('TADstub_Set');
             tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.Interface")
             tdkTestObj.addParameter("ParamValue","Interface");
             tdkTestObj.addParameter("Type","string");
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails();
             if expectedresult in actualresult:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 3: Set Ping interface as an invalid value"
                 print "EXPECTED RESULT 3: Should set Ping interface as an invalid value"
                 print "ACTUAL RESULT 3: %s" %details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";

	         #start the ping test after setting host value
	         tdkTestObj = obj.createTestStep('TADstub_Set');
                 tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run")
                 tdkTestObj.addParameter("ParamValue","true");
                 tdkTestObj.addParameter("Type","boolean");
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 details = tdkTestObj.getResultDetails();
                 if expectedresult in actualresult:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 4: Set PingTest.Run of IPPing as true";
                     print "EXPECTED RESULT 4: Should set PingTest.Run of IPPing as true";
                     print "ACTUAL RESULT 4: %s" %details;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                     time.sleep(40);

	             #Check if the ping test was succes, by checking the ping's success count and response time values
	             paramList=["Device.IP.Diagnostics.IPPing.SuccessCount", "Device.IP.Diagnostics.IPPing.AverageResponseTime", "Device.IP.Diagnostics.IPPing.MinimumResponseTime", "Device.IP.Diagnostics.IPPing.MaximumResponseTime"]
                     print "TEST STEP 5: Get the successcount, AverageResponseTime, MinimumResponseTime, MaximumResponseTime of ping test"
                     print "EXPECTED RESULT 5: successcount, AverageResponseTime, MinimumResponseTime, MaximumResponseTime of ping test should be greater than 0"
	             tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
	             if expectedresult in status and orgValue[0]>0 and orgValue[1]>0 and orgValue[2]>0 and orgValue[3]>0:
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "ACTUAL RESULT 5: %s" %orgValue;
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";
	             else:
                         tdkTestObj.setResultStatus("FAILURE");
                         print "ACTUAL RESULT 5: %s" %orgValue;
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : FAILURE"
	         else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 4: Set PingTest.Run of IPPing as true";
                     print "EXPECTED RESULT 4: Should set PingTest.Run of IPPing as true";
                     print "ACTUAL RESULT 4: %s" %details;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";
	     else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Set Ping interface as an invalid value"
                 print "EXPECTED RESULT 3: Should set Ping interface as an invalid value"
                 print "ACTUAL RESULT 3: %s" %details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
	print "Failed to get Device.IP.Diagnostics.IPPing.Host"
	print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");

else:
    print "Failed to load tad module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
