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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_XDNS_Check_ProcessRestart_OnXDNSEnable</name>
  <primitive_test_id/>
  <primitive_test_name>XDNS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the dnsmaq process restarted on toggling XDNS Enable status</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_XDNS_12</test_case_id>
    <test_objective>This test case is to check if the dnsmaq process restarted on toggling XDNS Enable status</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS</input_parameters>
    <automation_approch>1.Load the sysutil and tr181 module
2.Check if the dnmasq process is running
3.Toggle the dnsmasq status using Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS .
4.Check if the process restarted by comparing the initial pid and current pid are not equal.
5.Unload the module</automation_approch>
    <expected_output>On toggling the XDNS Enable status the dnsmasq process should get restarted</expected_output>
    <priority>High</priority>
    <test_stub_interface>XDNS</test_stub_interface>
    <test_script>TS_XDNS_Check_ProcessRestart_OnXDNSEnable</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_XDNS_Check_ProcessRestart_OnXDNSEnable');
tr181obj.configureTestCase(ip,port,'TS_XDNS_Check_ProcessRestart_OnXDNSEnable');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

flag =1;
revertflag =0;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_Set');

    cmd = "pidof dnsmasq";
    tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
    tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
    actualresult = tdkTestObj_Sys_ExeCmd.getResult();
    initPid = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and initPid!="":
       tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
       print "TEST STEP 1:Check if dnsmaq process is running";
       print "EXPECTED RESULT 1 : dnsmasq process should be running and should have a pid associated";
       print "ACTUAL RESULT 1: dnsmasq process pid is :",initPid;
       print "[TEST EXECUTION RESULT] : SUCCESS";

       tdkTestObj_Tr181_Get.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj_Tr181_Get.executeTestCase(expectedresult);
       actualresult = tdkTestObj_Tr181_Get.getResult();
       default = tdkTestObj_Tr181_Get.getResultDetails();

       if expectedresult in actualresult:
          tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
          print "TEST STEP 2:Get the XDNS Enable Status";
          print "EXPECTED RESULT 2 : Should get the XDNS Enable Status";
          print "ACTUAL RESULT 2: XDNS Enable Status is  :",default;
          print "[TEST EXECUTION RESULT] : SUCCESS";

          if default == "true":
             print"***XDNS is Enabled and Disabling it ******";
             tdkTestObj_Tr181_Set.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS")
             tdkTestObj_Tr181_Set.addParameter("ParamValue","false");
             tdkTestObj_Tr181_Set.addParameter("Type","bool")
             expectedresult="SUCCESS";
             tdkTestObj_Tr181_Set.executeTestCase(expectedresult);
             actualresult = tdkTestObj_Tr181_Set.getResult();
             details = tdkTestObj_Tr181_Set.getResultDetails();
             if expectedresult in actualresult:
                tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                print "TEST STEP 3:Disable the XDNS status";
                print "EXPECTED RESULT 3 : Should Disable the XDNS Status";
                print "ACTUAL RESULT 3: ",details;
                print "[TEST EXECUTION RESULT] : SUCCESS";
                revertflag =1;
             else:
                 tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                 print "TEST STEP 3:Disable the XDNS status";
                 print "EXPECTED RESULT 3 : Should Disable the XDNS Status";
                 print "ACTUAL RESULT 3: ",details;
                 print "[TEST EXECUTION RESULT] : FAILURE";
                 flag =0;
          else:
              print"***XDNS is Disabled and Enabling it ******";
              tdkTestObj_Tr181_Set.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS")
              tdkTestObj_Tr181_Set.addParameter("ParamValue","true");
              tdkTestObj_Tr181_Set.addParameter("Type","bool")
              expectedresult="SUCCESS";
              tdkTestObj_Tr181_Set.executeTestCase(expectedresult);
              actualresult = tdkTestObj_Tr181_Set.getResult();
              details = tdkTestObj_Tr181_Set.getResultDetails();
              if expectedresult in actualresult:
                 tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                 print "TEST STEP 3:Enable the XDNS status";
                 print "EXPECTED RESULT 3 : Should Enable the XDNS Status";
                 print "ACTUAL RESULT 3: ",details;
                 print "[TEST EXECUTION RESULT] : SUCCESS";
                 revertflag =1;
              else:
                  tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                  print "TEST STEP 3:Enable the XDNS status";
                  print "EXPECTED RESULT 3 : Should Enable the XDNS Status";
                  print "ACTUAL RESULT 3: ",details;
                  print "[TEST EXECUTION RESULT] : FAILURE";
                  flag =0;

          sleep(10);

          if flag == 1:
             cmd = "pidof dnsmasq";
             tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
             tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
             actualresult = tdkTestObj_Sys_ExeCmd.getResult();
             pid = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");

             if expectedresult in actualresult and pid!="":
                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                print "TEST STEP 4:Get the pidof dnsmasq after XDNS Enable status toggle";
                print "EXPECTED RESULT 4 : Should get the pidof dnsmasq after XDNS Enable status toggle";
                print "ACTUAL RESULT 4: dnsmasq process pid is :",pid;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if int(initPid) != int(pid):
                   tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                   print "TEST STEP 5:Check if the dnsmasq process restarted by comparing the pids";
                   print "EXPECTED RESULT 5 : Initial pid of dnsamsq should not be equal to the pid after XDNS Enable status toggle";
                   print "ACTUAL RESULT 5:Initial pid is :%s, Currrent pid:%s" %(initPid,pid);
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                    print "TEST STEP 5:Check if the dnsmasq process restarted by comparing the pids";
                    print "EXPECTED RESULT 5 : Initial pid of dnsamsq should not be equal to the pid after XDNS Enable status toggle";
                    print "ACTUAL RESULT 5:Initial pid is :%s, Currrent pid:%s" %(initPid,pid);
                    print "[TEST EXECUTION RESULT] : FAILURE";

             if revertflag ==1:
                tdkTestObj_Tr181_Set.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS")
                tdkTestObj_Tr181_Set.addParameter("ParamValue",default);
                tdkTestObj_Tr181_Set.addParameter("Type","bool")
                expectedresult="SUCCESS";
                tdkTestObj_Tr181_Set.executeTestCase(expectedresult);
                actualresult = tdkTestObj_Tr181_Set.getResult();
                details = tdkTestObj_Tr181_Set.getResultDetails();
                if expectedresult in actualresult:
                   tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                   print "TEST STEP 6:Revert the XDNS status";
                   print "EXPECTED RESULT 6 : Should revert the XDNS Status";
                   print "ACTUAL RESULT 6: ",details;
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                    print "TEST STEP 6:Revert the XDNS status";
                    print "EXPECTED RESULT 6: Should revert the XDNS Status";
                    print "ACTUAL RESULT 6: ",details;
                    print "[TEST EXECUTION RESULT] :FAILURE";
             else:
                 tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                 print "TEST STEP 4:Get the pidof dnsmasq after XDNS Enable status toggle";
                 print "EXPECTED RESULT 4 : Should get the pidof dnsmasq after XDNS Enable status toggle";
                 print "ACTUAL RESULT 4: dnsmasq process pid is :",pid;
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
               tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
               print "Failed to Toggle the XDNS Enable Status";
       else:
           tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
           print "TEST STEP 2:Get the XDNS Enable Status";
           print "EXPECTED RESULT 2 : Should get the XDNS Enable Status";
           print "ACTUAL RESULT 2: XDNS Enable Status is  :",default;
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
       tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
       print "TEST STEP 1:Check if dnsmaq process is running";
       print "EXPECTED RESULT 1 : dnsmasq process should be running and should have a pid associated";
       print "ACTUAL RESULT 1: dnsmasq process pid is :",initPid;
       print "[TEST EXECUTION RESULT] : FAILURE";
    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
