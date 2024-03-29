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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckDibblerProcess</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if dibbler-server is running  after server.pid and server.conf file are deleted on reboot  and  no log message like "Server Config is empty"  is present</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_41</test_case_id>
    <test_objective>This test case is to check if dibbler-server is running  after server.pid and server.conf file are deleted on reboot  and  no log message like "Server Config is empty"  is present</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the module
2. Check if dibbler process is running
3. delete the server.pid and server.conf file
4. Trigger a reboot on the DUT
5. Check if the deleted files are restored
6. No error message like "Server Config is empty"    should be present in log files
7.Unload the Module</automation_approch>
    <expected_output>No error message like "Server Config is empty"   should be present in log files  on deleting the server.pid and server.conf file with a device reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckDibblerProcess</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckDibblerProcess');

#Get the result of connection with test component and DUT
loadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    #Check whether the file is present or not
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "pidof dibbler-server";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult  and details != "":
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Check if dibbler-server process is running";
       print "EXPECTED RESULT 1 :dibbler-server process should be running";
       print "ACTUAL RESULT 1: %s" %details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       tdkTestObj = sysObj.createTestStep('ExecuteCmd');
       cmd = "[ -f /etc/dibbler/server.conf ] && echo \"File exist\" || echo \"File does not exist\"";
       tdkTestObj.addParameter("command",cmd);
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if details == "File exist":
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Check for server.conf file presence";
          print "EXPECTED RESULT 2:server.conf file should be present";
          print "ACTUAL RESULT 2:server.conf file is present";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          tdkTestObj = sysObj.createTestStep('ExecuteCmd');
          cmd = "[ -f /etc/dibbler/server.pid ] && echo \"File exist\" || echo \"File does not exist\"";
          tdkTestObj.addParameter("command",cmd);
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
          if details == "File exist":
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Check for server.pid file presence";
             print "EXPECTED RESULT 3:server.pid file should be present";
             print "ACTUAL RESULT 3:server.pid file is present";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             cmd = "rm -rf /etc/dibbler/server.conf /etc/dibbler/server.pid";
             tdkTestObj.addParameter("command",cmd);
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
             if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Delete the server.conf and server.pid files";
                print "EXPECTED RESULT 4 : Should delete server.conf and server.pid files";
                print "ACTUAL RESULT 4: File deletion was successfull";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #rebooting the device
                sysObj.initiateReboot();
                sleep(300);

                cmd = "[ -f /etc/dibbler/server.conf ] && echo \"File exist\" || echo \"File does not exist\"";
                tdkTestObj.addParameter("command",cmd);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if details == "File exist":
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 5: Check for existence of server.conf file";
                   print "EXPECTED RESULT 5:server.conf file should be present";
                   print "ACTUAL RESULT 5:server.conf file is present";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   cmd = "[ -f /etc/dibbler/server.pid ] && echo \"File exist\" || echo \"File does not exist\"";
                   tdkTestObj.addParameter("command",cmd);
                   expectedresult="SUCCESS";
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                   if details == "File exist":
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 6: Check for existence of server.pid file";
                      print "EXPECTED RESULT 6:server.pid file should be present";
                      print "ACTUAL RESULT 6:server.pid file is present";
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      cmd = "grep -rin  \"Server Config is empty\" /rdklogs/logs/";
                      tdkTestObj.addParameter("command",cmd);
                      expectedresult="SUCCESS";
                      tdkTestObj.executeTestCase(expectedresult);
                      actualresult = tdkTestObj.getResult();
                      details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                      if expectedresult in actualresult and details  == "":
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 7: Check if any log messages like Server Config is empty is present";
                         print "EXPECTED RESULT 7: Should not include and log messages like Server Config is empty";
                         print "ACTUAL RESULT 7:No such Log mesages are present";
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 7: Check if any log messages like Server Config is empty is present";
                          print "EXPECTED RESULT 7: Should not include and log messages like Server Config is empty";
                          print "ACTUAL RESULT 7:",details;
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] :FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 6: Check for existence of server.pid file";
                       print "EXPECTED RESULT 6:server.pid file should be present";
                       print "ACTUAL RESULT 6:server.pid file is not present";
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Check for existence of server.conf file";
                    print "EXPECTED RESULT 5:server.conf file should be present";
                    print "ACTUAL RESULT 5:server.conf file is not present";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Delete the server.conf and server.pid files";
                 print "EXPECTED RESULT 4 : Should delete server.conf and server.pid files";
                 print "ACTUAL RESULT 4: File deletion failed";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Check for server.pid file presence";
              print "EXPECTED RESULT 3:server.pid file should be present";
              print "ACTUAL RESULT 3:server.pid file is not present";
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Check for server.conf file presence";
           print "EXPECTED RESULT 2:server.conf file should be present";
           print "ACTUAL RESULT 2:server.conf file is not present";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check if dibbler-server process is running";
        print "EXPECTED RESULT 1 :dibbler-server process should be running";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
