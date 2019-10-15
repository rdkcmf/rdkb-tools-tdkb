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
  <version>56</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TAD_IPPingTest_ValidHostName</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set host name of IPPing to valid and check whether diagnostic state is set to Complete</synopsis>
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
    <test_case_id>TC_TAD_56</test_case_id>
    <test_objective>To set host name of IPPing to valid and check whether diagnostic state is set to Complete</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Set,TADstub_Get</api_or_interface_used>
    <input_parameters>mode
host</input_parameters>
    <automation_approch>1. Load  TAD modules
2. From script invoke TADstub_Set with type as string and a host name as www.google.com
3. Invoke TADstub_Get() to check for the  values from Device.IP.Diagnostics.IPPing.DiagnosticsState
4. check whether status is complete 
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>Value retreived by TADstub_Get should have the status as Complete</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_IPPingTest_ValidHostName</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkutility;
from tdkutility import *
import time

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_IPPingTest_ValidHostName');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
  obj.setLoadModuleStatus("SUCCESS")
  host = tdkutility.readtdkbConfigFile(obj);
  if host == "NULL":
    tdkTestObj.setResultStatus("FAILURE");
    print "Host name not available in tdkb config file"
  else:
    #get default timeout value
    tdkTestObj = obj.createTestStep('TADstub_Get');
    tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.IPPing.Timeout");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    timeout = tdkTestObj.getResultDetails();
    #convert milliseconds to seconds
    details1=int(timeout)
    sleepoutvalue=float((details1/1000)%60)
    if expectedresult in actualresult and timeout != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get value of Device.IP.Diagnostics.IPPing.Timeout";
        print "EXPECTED RESULT 1: Should get value of Device.IP.Diagnostics.IPPing.Timeout";
        print "ACTUAL RESULT 1:  %s" %timeout;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
	#setting host for traceroute
	tdkTestObj = obj.createTestStep('TADstub_Set');
        tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.Host");
        tdkTestObj.addParameter("Type","string");
        tdkTestObj.addParameter("ParamValue",host);
        #Execute the test case in DUT
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Set ping host URL"
          print "EXPECTED RESULT 2: Should set the host URL";
          print "ACTUAL RESULT 2:  %s" %details;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
          tdkTestObj = obj.createTestStep('TADstub_Set');
          tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run");
          tdkTestObj.addParameter("ParamValue","true");
          tdkTestObj.addParameter("Type","boolean");
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();
          if expectedresult in actualresult :
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Set ping test run value as true"
            print "EXPECTED RESULT 3: Should set the ping test run value as true";
            print "ACTUAL RESULT 3:  %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    time.sleep(sleepoutvalue)
            tdkTestObj = obj.createTestStep('TADstub_Get');
            tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.IPPing.DiagnosticsState");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and details == "Complete":
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 4: Get ping test diagnostic state"
               print "EXPECTED RESULT 4: Should get the ping test diagnostic state as Complete";
               print "ACTUAL RESULT 4:  %s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 4: Get ping test diagnostic state"
               print "EXPECTED RESULT 4: Should get the ping test diagnostic state as Complete";
               print "ACTUAL RESULT 4:  %s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
          else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Set ping test run value as true"
            print "EXPECTED RESULT 3: Should set ping test run value as true";
            print "ACTUAL RESULT 3:  %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
        else:
          #Set the result status of execution
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 2: Set ping host URL"
          print "EXPECTED RESULT 2: Should set the ping host URL"
          print "ACTUAL RESULT 2: %s" %details;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Get value of Device.IP.Diagnostics.IPPing.Timeout"; 
        print "EXPECTED RESULT 1: Should get value of Device.IP.Diagnostics.IPPing.Timeout";
        print "ACTUAL RESULT 1:  %s" %timeout;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

  obj.unloadModule("tad");
else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
