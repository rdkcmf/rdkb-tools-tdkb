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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckProcessUptimeAfterReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the all the processes are up after reboot and within the expected uptime</synopsis>
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
    <test_case_id>TC_SYSUTIL_39</test_case_id>
    <test_objective>This test case is to check if the all the processes are up after reboot and within the expected uptime</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,EMU,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module
1. Do a reboot on the device
2. Check if the uptime is greater than Wait Time else sleep untill the wait time is reached.
3. Check whether critical process are up after the reboot.
4. Unload the module</automation_approch>
    <expected_output>All the critical processes should be up and running once the devices comes up after reboot within the expected uptime</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckProcessUptimeAfterReboot</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import time;
from time import sleep;
from xfinityWiFiLib import *
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckProcessUptimeAfterReboot');
obj1.configureTestCase(ip,port,'TS_SANITY_CheckProcessUptimeAfterReboot');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    expectedresult ="SUCCESS";
    cmd = "sh %s/tdk_utility.sh parseConfigFile MAX_PROCESS_UPTIME" %TDK_PATH;
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    WaitTime  = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and WaitTime!="":
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Wait time to Check if the processes are up";
       print "EXPECTED RESULT 1: Should get the Wait time to Check if the processes are up";
       print "ACTUAL RESULT 1: ",WaitTime;
       print "[TEST EXECUTION RESULT] : SUCCESS";
       print "****DUT is going for a reboot and will be up after 300 seconds*****";
       obj.initiateReboot();
       sleep(300);

       tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       upTime = tdkTestObj.getResultDetails();

       if expectedresult in actualresult:
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the Uptime of the DUT";
          print "EXPECTED RESULT 2: Should get the Uptime of the DUT";
          print "ACTUAL RESULT 2: Uptime of the DUT is :",upTime;
          print "[TEST EXECUTION RESULT] : SUCCESS";

          if int(upTime) < int(WaitTime):
             sleepTime = (int(WaitTime) -int(upTime));
             print " *********Sleeping for %s sec to check if the processes are up to reach a wait time of %s sec ****" %(sleepTime,WaitTime);
             sleep(sleepTime);

          tdkTestObj = obj.createTestStep('ExecuteCmd');
          List = ["CCSP_PROCESS","SNMP_PROCESS","WEBPA_PROCESS","LIGHTTPD_PROCESS","DROPBEAR_PROCESS"];
          process_List = [];
          for item in List :
              Process= "sh %s/tdk_utility.sh parseConfigFile %s" %(TDK_PATH,item);
              print Process;
              expectedresult="SUCCESS";
              tdkTestObj.addParameter("command",Process);
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              getProcess = tdkTestObj.getResultDetails().strip();
              getProcess = getProcess.replace("\\n", "");
              if getProcess !="":
                 getProcess=getProcess.split(",")
                 process_List.append(getProcess);

          processList = [] ;
          #converting nested list to flat list
          processList = [ item for elem in process_List for item in elem]
          if "Invalid Argument passed" not in processList and processList != "":
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the list of processes ";
             print "EXPECTED RESULT 3: Should get the list of processes";
             print "ACTUAL RESULT 3: %s" %processList;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS"

             for item in processList:
                 if item == "CcspHotspot":
                    #Get current values of public wifi params
                    tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get');
                    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable");
                    expectedresult="SUCCESS";
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in  actualresult and details == "true":
                       command1 = "pidof %s" %item
                       tdkTestObj = obj.createTestStep('ExecuteCmd');
                       tdkTestObj.addParameter("command", command1);
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       details = tdkTestObj.getResultDetails().strip();
                       details = details.replace("\\n", "");
                       if expectedresult in actualresult and "" != details:
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "Process Name : %s" %item;
                          print "PID : %s" %details;
                          print "%s with process ID %s is running" %(item,details)
                          print "[TEST EXECUTION RESULT] : SUCCESS"
                       else:
                           tdkTestObj.setResultStatus("FAILURE");
                           print "Process Name : %s" %item
                           print "%s is not running" %item
                           print "[TEST EXECUTION RESULT] : FAILURE"
                    else:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Since xfinitywifi is disabled CcspHotspot is not running"
                        print "[TEST EXECUTION RESULT] : SUCCESS"

                 else:
                     command1 = "pidof %s" %item
                     tdkTestObj = obj.createTestStep('ExecuteCmd');
                     tdkTestObj.addParameter("command", command1);
                     tdkTestObj.executeTestCase(expectedresult);
                     actualresult = tdkTestObj.getResult();
                     details = tdkTestObj.getResultDetails().strip();
                     details = details.replace("\\n", "");
                     if expectedresult in actualresult and "" != details:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Process Name : %s" %item;
                        print "PID : %s" %details;
                        print "%s with process ID %s is running" %(item,details)
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                     else:
                         tdkTestObj.setResultStatus("FAILURE");
                         print "Process Name : %s" %item
                         print "%s is not running" %item
                         print "[TEST EXECUTION RESULT] : FAILURE"
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Get the list of processes ";
              print "EXPECTED RESULT 3: Should get the list of processes";
              print "ACTUAL RESULT 3: %s" %processList;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE"
       else:
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 2: Get the Uptime of the DUT";
          print "EXPECTED RESULT 2: Should get the Uptime of the DUT";
          print "ACTUAL RESULT 2: Uptime of the DUT is :",upTime;
          print "[TEST EXECUTION RESULT] : FAILURE";
    else:
       tdkTestObj.setResultStatus("FAILURE");
       print "TEST STEP 1: Get the Wait time to Check if the processed are up";
       print "EXPECTED RESULT 1: Should get the Wait time to Check if the processed are up";
       print "ACTUAL RESULT 1: ",WaitTime;
       print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
else:
     print "Failed to load sysutil module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
