##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_BootTimeLogMarkers</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the expected boot log markers are present on device boot up</synopsis>
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
    <test_case_id>TC_SYSUTIL_43</test_case_id>
    <test_objective>This test case is to check if the expected boot log markers are present on device boot up</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the module
2. Trigger a reboot on DUT
3. check if the  markers are present in /rdklogs/logs/BootTime.log once the DUT is up
4. Unload the module</automation_approch>
    <expected_output>The expected BootTime.log marker should be present</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_BootTimeLogMarkers</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
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
from time import sleep;
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_BootTimeLogMarkers');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    cmd = "sh %s/tdk_utility.sh parseConfigFile BOOTTIME_LOG_MARKERS" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult  and details!= "":
       logMsg = details.split(",");
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 0: Execute the command";
       print "EXPECTED RESULT 0: Should execute the command successfully";
       print "ACTUAL RESULT 0: Details: %s" %details;
       print "[TEST EXECUTION RESULT] : SUCCESS";
       revert =0;
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

           print" *****if device type is RPI disable  rdkbLogMonitor.service******";
           if devicetype == "RPI":
               tdkTestObj = obj.createTestStep('ExecuteCmd');
               cmd = "systemctl disable rdkbLogMonitor.service";
               print cmd;
               expectedresult="SUCCESS";
               tdkTestObj.addParameter("command", cmd);
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
               if expectedresult in actualresult:
                   revert =1;
                   print"rdkbLogMonitor.service disabled sucessfully";
                   tdkTestObj.setResultStatus("SUCCESS");
               else:
                   print"rdkbLogMonitor.service disable failed";
                   tdkTestObj.setResultStatus("FAILURE");

           obj.initiateReboot();
           sleep(300);
           logFile = "/rdklogs/logs/BootTime.log";
           print "***************************************************";
           print "TEST STEP 2: Checking if the following Log Message are present in /rdklogs/logs/BootTime.log";
           print "%s" %logMsg;
           for item in logMsg:
               print "\n*** Checking if %s Log Message is present in BootTime File***" %item;
               query="grep -rin \"%s\" \"%s\"" %(item,logFile);
               print "query:%s" %query
               tdkTestObj = obj.createTestStep('ExecuteCmd');
               tdkTestObj.addParameter("command", query)
               expectedresult="SUCCESS";
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               details = tdkTestObj.getResultDetails().strip().replace("\\n","");
               if (len(details) != 0)  and  item in details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Search Result :%s "%details;
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "Search Result :%s "%details;
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 1: Get the DEVICE TYPE"
           print "EXPECTED RESULT 1: Should get the device type";
           print "ACTUAL RESULT 1:Device type  %s" %devicetype;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
       if revert ==1:
           tdkTestObj = obj.createTestStep('ExecuteCmd');
           cmd = "systemctl enable rdkbLogMonitor.service";
           print cmd;
           expectedresult="SUCCESS";
           tdkTestObj.addParameter("command", cmd);
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
           if expectedresult in actualresult:
               tdkTestObj.setResultStatus("SUCESS");
               print "TEST STEP 3: Enable the rdkbLogMonitor.service as a part of revertion"
               print "EXPECTED RESULT 3: revert operation should be sucessfull";
               print "ACTUAL RESULT 3:Revertion success";
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Enable the rdkbLogMonitor.service as a part of revertion"
               print "EXPECTED RESULT 3: revert operation should be sucessfull";
               print "ACTUAL RESULT 3:Revertion failed";
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 0: Execute the command";
        print "EXPECTED RESULT 0: Should execute the command successfully";
        print "ACTUAL RESULT 0: Details: %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
