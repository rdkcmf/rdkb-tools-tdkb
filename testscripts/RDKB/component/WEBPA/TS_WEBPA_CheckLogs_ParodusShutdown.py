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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WEBPA_CheckLogs_ParodusShutdown</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check for Parodus proper Shutdown and SIGTREM received in Consolelog.txt.0  and PARODUSlog.txt.0 when rebooted by Device.X_CISCO_COM_DeviceControl.RebootDevice via WEBPA</synopsis>
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
    <test_case_id>TC_WEBPA_38</test_case_id>
    <test_objective>This test case is to Check for Parodus proper Shutdown and SIGTREM received in Consolelog.txt.0  and PARODUSlog.txt.0 when rebooted by Device.X_CISCO_COM_DeviceControl.RebootDevice via WEBPA</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable
Device.X_CISCO_COM_DeviceControl.RebootDevice</input_parameters>
    <automation_approch>1)Load the module
2)Get the  Manageable Notification status using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.ManageableNotification.Enable Check if enabled  if not enable it.
3)Check for PARODUSlog.txt.0 and Consolelog.txt.0 file presence.
4)Capture the tail -f of /rdklogs/logs/PARODUSlog.txt.0 in /nvram/tdk_PARODUStail
5)Capture the tail -f of /rdklogs/logs/Consolelog.txt.0 in /nvram/tdk_Consoletail
6)Trigger a reboot via Webpa  using Device.X_CISCO_COM_DeviceControl.RebootDevice set  to "Device"
7)Grep for the following in tdk_PAMtail
grep -i "reboot-pending" /nvram/tdk_PARODUStail
grep -i "PARODUS: SIGTERM received" /nvram/tdk_PARODUStail
grep -i "PARODUS: cloud_status set as offline after connection close" /nvram/tdk_PARODUStail
grep -i "PARODUS: SIGTERM received" /nvram/tdk_PARODUStail
grep -i "Shutdown parodus" /nvram/tdk_Consoletail
8) Remove the file created rm -rf /nvram/tdk_PARODUStail and /nvram/tdk_Consoletail
9)Revert the Manageable Notification status to default if set
10)Unload the Module</automation_approch>
    <expected_output>The log Message "reboot-pending","PARODUS: SIGTERM received","PARODUS: cloud_status set as offline after connection close","PARODUS: SIGTERM received","Shutdown parodus", should be available in the logs captured at the time of reboot initiation</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_WEBPA_CheckLogs_ParodusShutdown</test_script>
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
obj1.configureTestCase(ip,port,'TS_WEBPA_CheckLogs_ParodusShutdown');
obj2.configureTestCase(ip,port,'TS_WEBPA_CheckLogs_ParodusShutdown');

#Get the result of connection with test component and DUT
loadmodulestatus1=obj1.getLoadModuleResult();
loadmodulestatus2=obj2.getLoadModuleResult();

setflag = 1;
revertflag = 0;

def verify_logMsgs(tdkTestObj):
    ParoduslogMsgs_list = ["reboot-pending","PARODUS: SIGTERM received","PARODUS: cloud_status set as offline after connection close","PARODUS: SIGTERM received"]
    ConsolelogMsgs_list = ["Shutdown parodus"]
    print"The following logs should be present when undergoing webpa reboot";
    print ParoduslogMsgs_list;
    print ConsolelogMsgs_list;

    for list in ParoduslogMsgs_list:
        cmd = "cat /nvram/tdk_PARODUStail | grep -ire \"%s\"" %list;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        print "LogMsg is :",details
        if expectedresult in actualresult and details != "" and list in details:
           Pmsgpresent = 1;
        else:
            Pmsgpresent = 0;
            print "Log Mesage %s is NOT present"%list
            break;

    for list in ConsolelogMsgs_list:
        cmd = "cat /nvram/tdk_Consoletail | grep -ire \"%s\"" %list;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        print "LogMsg is :",details
        if expectedresult in actualresult and details !="" and list in details:
           Cmsgpresent = 1;
        else:
            Cmsgpresent = 0;
            print "Log Mesage %s is NOT present"%list
            break;

    return Pmsgpresent,Cmsgpresent;

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
          cmd = "[ -f /rdklogs/logs/PARODUSlog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
          tdkTestObj.addParameter("command",cmd);
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

          if details == "File exist":
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Check for PARODUSlog.txt.0 log file presence";
             print "EXPECTED RESULT 2:PARODUSlog.txt.0 log file should be present";
             print "ACTUAL RESULT 2:PARODUSlog.txt.0 file is present";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = obj2.createTestStep('ExecuteCmd');
             cmd = "[ -f /rdklogs/logs/Consolelog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
             tdkTestObj.addParameter("command",cmd);
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

             if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check for Consolelog.txt.0 log file presence";
                print "EXPECTED RESULT 3:Consolelog.txt.0 log file should be present";
                print "ACTUAL RESULT 3:Consolelog.txt.0 file is present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                query="echo > /nvram/tdk_PARODUStail"
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
                   print "TEST STEP 4: Create a file in nvram to copy the tail -f of PARODUSlog.txt.0";
                   print "EXPECTED RESULT 4: Should create a file in nvram  to copy the tail -f of PARODUSlog.txt.0";
                   print "ACTUAL RESULT 4: File creation was successful";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   query="echo > /nvram/tdk_Consoletail"
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
                      print "TEST STEP 5: Create a file in nvram  to copy the tail -f of Consolelog.txt.0";
                      print "EXPECTED RESULT 5: Should create a file in nvram to copy the tail -f of Consolelog.txt.0";
                      print "ACTUAL RESULT 5: File creation was successful";
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      query="tail -f /rdklogs/logs/PARODUSlog.txt.0 > /nvram/tdk_PARODUStail &"
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
                         print "TEST STEP 6: Tail the Parodus Logs to the file created in nvram and add  the process to background";
                         print "EXPECTED RESULT 6: Should tail the Parodus Logs to the file created in nvram and add  the process to background";
                         print "ACTUAL RESULT 6: Tail the Parodus Logs to the file created in nvram and add  the process to background was successfull";
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";

                         query="tail -f /rdklogs/logs/Consolelog.txt.0 > /nvram/tdk_Consoletail &"
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
                            print "TEST STEP 7: Tail the Console Logs to the file created in nvram and add  the process to background";
                            print "EXPECTED RESULT 7: Should tail the Console Logs to the file created in nvram and add  the process to background";
                            print "ACTUAL RESULT 7: Tail the Console Logs to the file created in nvram and add  the process to background was successfull";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj2);
                            #Saving Current state before reboot
                            obj2.saveCurrentState();

                            if "SUCCESS" in preRequisiteStatus:
                               queryParam = {"name":"Device.X_CISCO_COM_DeviceControl.RebootDevice","value":"Device","dataType":0}
                               queryResponse = webpaQuery(obj2, queryParam,"set")
                               parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
                               print "parsedResponse : %s" %parsedResponse;
                               tdkTestObj = obj2.createTestStep('ExecuteCmd');
                               tdkTestObj.executeTestCase("SUCCESS");

                               if "SUCCESS" in parsedResponse[0]:
                                  tdkTestObj.setResultStatus("SUCCESS");
                                  print "TEST STEP 8: Call for Device Reboot via WEBPA";
                                  print "EXPECTED RESULT 8: Device Reboot via WEBPA should be successfull"
                                  print "ACTUAL RESULT 8:  Device Reboot via WEBPA was successfull";
                                  #Get the result of execution
                                  print "[TEST EXECUTION RESULT] : SUCCESS";
                                  #Restore the device state saved before reboot
                                  obj2.restorePreviousStateAfterReboot();

                                  tdkTestObj = obj2.createTestStep('ExecuteCmd');
                                  Presult,Cresult = verify_logMsgs(tdkTestObj);

                                  if Presult  == 1 and Cresult == 1:
                                     tdkTestObj.setResultStatus("SUCCESS");
                                     print "TEST STEP 9: Check if the above mentioned LogMsgs are present in PARODUSlog.txt.0 and Consolelog.txt.0";
                                     print "EXPECTED RESULT 9: The above mentioned LogMsgs Should be present in PARODUSlog.txt.0 and Consolelog.txt.0"
                                     print "ACTUAL RESULT 9: The expected LogMsgs were populated successfully in PARODUSlog.txt.0 and Consolelog.txt.0";
                                     #Get the result of execution
                                     print "[TEST EXECUTION RESULT] : SUCCESS";
                                  else:
                                      tdkTestObj.setResultStatus("FAILURE");
                                      print "TEST STEP 9: Check if the above mentioned LogMsgs are presnt in PARODUSlog.txt.0 and Consolelog.txt.0";
                                      print "EXPECTED RESULT 9: The above mentioned LogMsgs Should be present in PARODUSlog.txt.0 and Consolelog.txt.0"
                                      print "ACTUAL RESULT 9:  The expected LogMsgs failed to  populate in PARODUSlog.txt.0 or Consolelog.txt.0";
                                      #Get the result of execution
                                      print "[TEST EXECUTION RESULT] : FAILURE";
                               else:
                                   tdkTestObj.setResultStatus("FAILURE");
                                   print "TEST STEP 8: Call for Device Reboot via WEBPA";
                                   print "EXPECTED RESULT 8: Device Reboot via WEBPA should be successfull"
                                   print "ACTUAL RESULT 8: Device Reboot via WEBPA was successfull";
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] :FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"
                         else:
                             #Set the result status of execution
                             tdkTestObj.setResultStatus("FAILURE");
                             print "TEST STEP 7: Tail the Console Logs to the file created in nvram and add  the process to background";
                             print "EXPECTED RESULT 7: Should tail the Console Logs to the file created in nvram and add  the process to background";
                             print "ACTUAL RESULT 7: Tail the Console Logs to the file created in nvram and add  the process to background failed";
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] :FAILURE";
                      else:
                          #Set the result status of execution
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 6: Tail the Parodus Logs to the file created in nvram and add  the process to background";
                          print "EXPECTED RESULT 6: Should tail the Parodus Logs to the file created in nvram and add  the process to background";
                          print "ACTUAL RESULT 6: Tail the Parodus Logs to the file created in nvram and add  the process to background failed";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                      #Delete the file created under nvram
                      query="rm -rf /nvram/tdk_Consoletail"
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
                         print "TEST STEP 10: Delete the tdk_Consoletail file created under nvram";
                         print "EXPECTED RESULT 10: Should Delete the tdk_Consoletail file created under nvram";
                         print "ACTUAL RESULT 10: File Deletion was successfull";
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] :SUCCESS";
                      else:
                          #Set the result status of execution
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 10: Delete the tdk_Consoletail file created under nvram";
                          print "EXPECTED RESULT 10: Should Delete the tdk_Consoletail file created under nvram";
                          print "ACTUAL RESULT 10: File Deletion Failed";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] :FAILURE";
                   else:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 5: Create a file in nvram to copy the tail -f of Consolelog.txt.0";
                       print "EXPECTED RESULT 5: Should create a file in nvram to copy the tail -f of Consolelog.txt.0";
                       print "ACTUAL RESULT 5: File creation was successful";
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";

                   #Delete the file created under nvram
                   query="rm -rf /nvram/tdk_PARODUStail"
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
                      print "TEST STEP 11: Delete the tdk_PARODUSTail file created under nvram";
                      print "EXPECTED RESULT 11: Should Delete tdk_ParodusTail file created under nvram";
                      print "ACTUAL RESULT 11: File Deletion was successfull";
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] :SUCCESS";
                   else:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 11: Delete the tdk_PARODUSTail file created under nvram";
                       print "EXPECTED RESULT 11: Should Delete the tdk_PARODUSTail file created under nvram";
                       print "ACTUAL RESULT 11: File Deletion Failed";
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] :FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Create a file in nvram to copy the tail -f of PARODUSlog.txt.0";
                    print "EXPECTED RESULT 4: Should create a file in nvram to copy the tail -f of PARODUSlog.txt.0";
                    print "ACTUAL RESULT 4: File creation failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Check for Consolelog.txt.0 log file presence";
                 print "EXPECTED RESULT 3:Consolelog.txt.0 log file should be present";
                 print "ACTUAL RESULT 3:Consolelog.txt.0 file is not present";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Check for PARODUSlog.txt.0 log file presence";
              print "EXPECTED RESULT 2:PARODUSlog.txt.0 log file should be present";
              print "ACTUAL RESULT 2:PARODUSlog.txt.0 file is not present";
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
          print "TEST STEP 12: Revert the Manageable Notification to previous value";
          print "EXPECTED RESULT 12:Should Revert the Manageable Notification to previous value"
          print "ACTUAL RESULT 12:Revert was successfull";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] :SUCCESS";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 12: Revert the Manageable Notification to previous value";
           print "EXPECTED RESULT 12:Should Revert the Manageable Notification to previous value"
           print "ACTUAL RESULT 12:Revertion failed";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] :FAILURE";
    obj1.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj1.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
