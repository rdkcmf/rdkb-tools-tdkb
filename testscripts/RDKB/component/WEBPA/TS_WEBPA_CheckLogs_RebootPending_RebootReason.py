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
  <name>TS_WEBPA_CheckLogs_RebootPending_RebootReason</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check the Reboot pending and its reason in PAMlog.txt.0 when triggered for reboot by Device.X_CISCO_COM_DeviceControl.RebootDevice via WEBPA</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WEBPA_37</test_case_id>
    <test_objective>This test case is to Check the Reboot pending and its reason in PAMlog.txt.0 when triggered for reboot by Device.X_CISCO_COM_DeviceControl.RebootDevice via WEBPA</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable
Device.X_CISCO_COM_DeviceControl.RebootDevice</input_parameters>
    <automation_approch>1)Load Module
2) Get the Manageable Notification status using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable ,Check if enabled if not enable it.
3) Confirm whether the PAMlog.txt.0 file is present or not
4)Capture the tail -f /rdklogs/logs/PAMlog.txt.0 in /nvram/tdk_PAMtail
5)Trigger a reboot via Webpa  using Device.X_CISCO_COM_DeviceControl.RebootDevice set  to "Device"
6)Grep for the following in tdk_PAMtail
grep -i "reboot-pending" /nvram/tdk_PAMtail
grep -i "webpa-reboot" /nvram/tdk_PAMtail
7)Remove the file cretaed  rm -rf /nvram/tdk_PAMtail
8)Revert the Manageable Notification status to default if set
9)Unload the Module</automation_approch>
    <expected_output>The log Message reboot-pending,webpa-reboot should be available in the logs captured at the time of reboot initiation</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_WEBPA_CheckLogs_RebootPending_RebootReason</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import webpaUtility;
from webpaUtility import *

#Test component to be tested
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2= tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,' TS_WEBPA_CheckLogs_RebootPending_RebootReason');
obj2.configureTestCase(ip,port,' TS_WEBPA_CheckLogs_RebootPending_RebootReason');

#Get the result of connection with test component and DUT
loadmodulestatus1=obj1.getLoadModuleResult();
loadmodulestatus2=obj2.getLoadModuleResult();

setflag = 1;
revertflag = 0;

def verify_logMsgs(tdkTestObj):
    logMsgs_list = ["reboot-pending","webpa-reboot"]

    print"The following logs should be present when undergoing webpa reboot";
    print logMsgs_list;

    for list in logMsgs_list:
        cmd = "cat /nvram/tdk_PAMtail | grep -ire \"%s\"" %list;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        print "LogMsg is :",details;
        if expectedresult in actualresult and details != "" and list in details:
           msgpresent = 1;
        else:
            msgpresent = 0;
            print "Log Mesage %s is NOT present"%list
            break;
    return msgpresent;

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() :
    #Set the result status of execution
    obj1.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the status  of Manageable Notification";
       print "EXPECTED RESULT 1: Should get the status of Manageable Notification";
       print "ACTUAL RESULT 1:  Manageable Notification status is :%s" %default;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       if default != "true":
          tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable");
          tdkTestObj.addParameter("ParamValue","true");
          tdkTestObj.addParameter("Type","bool");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();

          if expectedresult in actualresult :
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Set the status  of Manageable Notification to true";
             print "EXPECTED RESULT 2: Should set the status of Manageable Notification to true";
             print "ACTUAL RESULT 2:  Manageable Notification status is :%s" %details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
             revertflag = 1;
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Set the status  of Manageable Notification to true";
              print "EXPECTED RESULT 2: Should set the status of Manageable Notification to true";
              print "ACTUAL RESULT 2:  Manageable Notification status is :%s" %details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
              setflag = 0;

       if setflag ==1 :
          tdkTestObj = obj2.createTestStep('ExecuteCmd');
          cmd = "[ -f /rdklogs/logs/PAMlog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
          tdkTestObj.addParameter("command",cmd);
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

          if details == "File exist":
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Check for PAMlog.txt.0 log file presence";
             print "EXPECTED RESULT 2:PAMlog.txt.0 log file should be present";
             print "ACTUAL RESULT 2:PAMlog.txt.0 file is present";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             query="echo > /nvram/tdk_PAMtail"
             print "query:%s" %query
             tdkTestObj = obj2.createTestStep('ExecuteCmd');
             tdkTestObj.addParameter("command", query)
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails().strip().replace("\\n","");

             if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Create a file in nvram to copy the tail -f of PAMlog.txt.0";
                print "EXPECTED RESULT 3: Should create a file in nvram to copy the tail -f of PAMlog.txt.0";
                print "ACTUAL RESULT 3: File creation was successful";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                query="tail -f /rdklogs/logs/PAMlog.txt.0 > /nvram/tdk_PAMtail &"
                print "query:%s" %query
                tdkTestObj = obj2.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n","");

                if expectedresult in actualresult :
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 4: Tail the PAM Logs to the file created in nvram and add  the process to background";
                   print "EXPECTED RESULT 4: Should tail the PAM Logs to the file created in nvram and add  the process to background";
                   print "ACTUAL RESULT 4: Tail the PAM Logs to the file created in nvram and add  the process to background was successfull";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                   #Saving Current state before reboot
                   obj2.saveCurrentState();

                   tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj2);
                   if "SUCCESS" in preRequisiteStatus:
                      queryParam = {"name":"Device.X_CISCO_COM_DeviceControl.RebootDevice","value":"Device","dataType":0}
                      queryResponse = webpaQuery(obj2, queryParam,"set")
                      parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
                      print "parsedResponse : %s" %parsedResponse;
                      tdkTestObj = obj2.createTestStep('ExecuteCmd');
                      tdkTestObj.executeTestCase("SUCCESS");

                      if "SUCCESS" in parsedResponse[0]:
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 5: Call for Device Reboot via WEBPA";
                         print "EXPECTED RESULT 5: Device Reboot via WEBPA should be successfull"
                         print "ACTUAL RESULT 5:  Device Reboot via WEBPA was successfull";
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                         #Restore the device state saved before reboot
                         obj2.restorePreviousStateAfterReboot();

                         tdkTestObj = obj2.createTestStep('ExecuteCmd');
                         result = verify_logMsgs(tdkTestObj);

                         if result == 1:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Check if the above mentioned LogMsgs are present in PAMlog.txt.0";
                            print "EXPECTED RESULT 6: The above mentioned LogMsgs Should be present in PAMlog.txt.0"
                            print "ACTUAL RESULT 6:  The expected LogMsgs were populated successfully in PAMlog.txt.0";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                         else:
                             tdkTestObj.setResultStatus("FAILURE");
                             print "TEST STEP 6: Check if the above mentioned LogMsgs are present in PAMlog.txt.0";
                             print "EXPECTED RESULT 6: The above mentioned LogMsgs Should be present in PAMlog.txt.0"
                             print "ACTUAL RESULT 6:  The expected LogMsgs failed to  populate in PAMlog.txt.0";
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] : FAILURE";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 5: Call for Device Reboot via WEBPA";
                          print "EXPECTED RESULT 5: Device Reboot via WEBPA should be successfull"
                          print "ACTUAL RESULT 5:  Device Reboot via WEBPA was successfull";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] :FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Tail the PAM Logs to the file created in nvram and add  the process to background";
                    print "EXPECTED RESULT 4: Should tail the PAM Logs to the file created in nvram and add  the process to background";
                    print "ACTUAL RESULT 4: Tail the PAM Logs to the file created in nvram and add  the process to background failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] :FAILURE";
                #Delete the file created under nvram
                query="rm -rf /nvram/tdk_PAMtail"
                print "query:%s" %query
                tdkTestObj = obj2.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n","");

                if expectedresult in actualresult :
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 7: Delete the tdk_PAMtail file created under nvram";
                   print "EXPECTED RESULT 7: Should Delete the tdk_PAMtail file created under nvram";
                   print "ACTUAL RESULT 7: File Deletion was successfull";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] :SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 7: Delete the tdk_PAMtail file created under nvram";
                    print "EXPECTED RESULT 7: Should Delete the tdk_PAMtail file created under nvram";
                    print "ACTUAL RESULT 7: File Deletion Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] :FAILURE";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Create a file in nvram to copy the tail -f of PAMlog.txt.0";
                 print "EXPECTED RESULT 3: Should create a file in nvram to copy the tail -f of PAMlog.txt.0";
                 print "ACTUAL RESULT 3: File creation failed";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Check for PAMlog.txt.0 log file presence";
              print "EXPECTED RESULT 2:PAMlog.txt.0 log file should be present";
              print "ACTUAL RESULT 2:PAMlog.txt.0 file is not present";
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print " Manageable Notification was disabled and failed on enabling" ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the status  of Manageable Notification";
        print "EXPECTED RESULT 1: Should get the status of Manageable Notification";
        print "ACTUAL RESULT 1:  Manageable Notification status is :%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    if revertflag ==1:
       tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable");
       tdkTestObj.addParameter("ParamValue",default);
       tdkTestObj.addParameter("Type","bool");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();

       if expectedresult in actualresult :
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 8: Revert the Manageable Notification to previous value";
          print "EXPECTED RESULT 8:Should Revert the Manageable Notification to previous value"
          print "ACTUAL RESULT 8:Revert was successfull";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] :SUCCESS";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 8: Revert the Manageable Notification to previous value";
           print "EXPECTED RESULT 8:Should Revert the Manageable Notification to previous value"
           print "ACTUAL RESULT 8:Revertion failed";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] :FAILURE";
    obj1.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj1.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
