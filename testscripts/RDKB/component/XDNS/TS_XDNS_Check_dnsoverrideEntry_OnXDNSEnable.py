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
  <name>TS_XDNS_Check_dnsoverrideEntry_OnXDNSEnable</name>
  <primitive_test_id/>
  <primitive_test_name>XDNS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if dnsoverride entry is present in resolv.conf on Enabling the XDNS.</synopsis>
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
    <test_case_id>TC_XDNS_13</test_case_id>
    <test_objective>This test case is to check if dnsoverride entry is present in resolv.conf on Enabling the XDNS.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS</input_parameters>
    <automation_approch>1.Load the sysutil and tr181 module
2.Check if dnsmasq process is running
3.Get the XDNS Enable Status using Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS
4.if XDNS is disabled then resolv.conf should not have dnsoverride entry, verify the same if dnsoverride entry is present after XDNS enable
5.if XDNS is enabled then resolv.conf should have dnsoverride entry, verify the same if dnsoverride entry is not present after XDNS disable
6.Revert the XDNS status to previous
7.Unload the module</automation_approch>
    <expected_output>dnsoverride entry should be present in resolv.conf on XDNS enable and absent on disable</expected_output>
    <priority>High</priority>
    <test_stub_interface>XDNS</test_stub_interface>
    <test_script>TS_XDNS_Check_dnsoverrideEntry_OnXDNSEnable</test_script>
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
sysobj.configureTestCase(ip,port,'TS_XDNS_Check_dnsoverrideEntry_OnXDNSEnable');
tr181obj.configureTestCase(ip,port,'TS_XDNS_Check_dnsoverrideEntry_OnXDNSEnable');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

def ToggleXDNSStatus(tdkTestObj,setValue):
    tdkTestObj_Tr181_Set.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS")
    tdkTestObj_Tr181_Set.addParameter("ParamValue",setValue);
    tdkTestObj_Tr181_Set.addParameter("Type","bool")
    expectedresult="SUCCESS";
    tdkTestObj_Tr181_Set.executeTestCase(expectedresult);
    actualresult = tdkTestObj_Tr181_Set.getResult();
    details = tdkTestObj_Tr181_Set.getResultDetails();

    return actualresult,details;

def CheckFordnsoverrideEntry(tdkTestObj):
    cmd="cat /etc/resolv.conf |grep \"dnsoverride\" ";
    print "cmd:",cmd;
    tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
    tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
    actualresult = tdkTestObj_Sys_ExeCmd.getResult();
    details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");

    return details,actualresult;

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

          if default =="false":
             print"***XDNS is Disabled ******";
             setValue = "true";
             details,actualresult = CheckFordnsoverrideEntry(tdkTestObj_Sys_ExeCmd);
             if expectedresult in actualresult and details =="":
                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if dnsoverride  is present in resolv.conf";
                print "EXPECTED RESULT 3 :XDNS is disabled and dnsoverride entry should not be present";
                print "ACTUAL RESULT 3:",details;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                actualresult,details=ToggleXDNSStatus(tdkTestObj_Tr181_Set,setValue);
                if expectedresult in actualresult:
                   revertflag =1;
                   tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                   print "TEST STEP 4:Enbaling the XDNS Status";
                   print "EXPECTED RESULT 4 :Should Enable the XDNS Status";
                   print "ACTUAL RESULT 4:",details;
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   details,actualresult = CheckFordnsoverrideEntry(tdkTestObj_Sys_ExeCmd);
                   if expectedresult in actualresult and details != "" and "dnsoverride" in details:
                      tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                      print "TEST STEP 5:Check if dnsoverride entry is present in resolv.conf";
                      print "EXPECTED RESULT 5 :XDNS is Enabled and dnsoverride entry should be present";
                      print "ACTUAL RESULT 5:",details;
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                   else:
                       tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                       print "TEST STEP 5:Check if dnsoverride entry is present in resolv.conf";
                       print "EXPECTED RESULT 5 :XDNS is Enabled and dnsoverride entry should be present";
                       print "ACTUAL RESULT 5:",details;
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                    print "TEST STEP 4:Enbaling the XDNS Status";
                    print "EXPECTED RESULT 4 :Should Enable the XDNS Status";
                    print "ACTUAL RESULT 4:",details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                 print "TEST STEP 3:Check if dnsoverride  is present in resolv.conf";
                 print "EXPECTED RESULT 3 :XDNS is disabled and dnsoverride entry should not be present";
                 print "ACTUAL RESULT 3:",details;
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
               print"***XDNS is Enabled ******";
               setValue = "false";
               details,actualresult = CheckFordnsoverrideEntry(tdkTestObj_Sys_ExeCmd);
               if expectedresult in actualresult and details != "" and "dnsoverride" in details:
                  tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                  print "TEST STEP 3:Check if dnsoverride is present in resolv.conf";
                  print "EXPECTED RESULT 3 :XDNS is enabled and dnsoverride entry should be present";
                  print "ACTUAL RESULT 3:",details;
                  print "[TEST EXECUTION RESULT] : SUCCESS";

                  actualresult,details=ToggleXDNSStatus(tdkTestObj_Tr181_Set,setValue);
                  if expectedresult in actualresult :
                     revertflag =1;
                     tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                     print "TEST STEP 4:Disabling the XDNS Status";
                     print "EXPECTED RESULT 4 :Should Disable the XDNS Status";
                     print "ACTUAL RESULT 4:",details;
                     print "[TEST EXECUTION RESULT] : SUCCESS";

                     details,actualresult = CheckFordnsoverrideEntry(tdkTestObj_Sys_ExeCmd);
                     if expectedresult in actualresult and details == "" :
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                        print "TEST STEP 5:Check if dnsoverride entry is not present in resolv.conf";
                        print "EXPECTED RESULT 5 :XDNS is disabled and dnsoverride entry should not be present";
                        print "ACTUAL RESULT 5:",details;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                     else:
                         tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                         print "TEST STEP 5:Check if dnsoverride entry is not present in resolv.conf";
                         print "EXPECTED RESULT 5 :XDNS is disabled and dnsoverride entry should not be present";
                         print "ACTUAL RESULT 5:",details;
                         print "[TEST EXECUTION RESULT] : FAILURE";
                  else:
                      tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                      print "TEST STEP 4:Disable the XDNS Status";
                      print "EXPECTED RESULT 4 :Should Disable the XDNS Status";
                      print "ACTUAL RESULT 4:",details;
                      print "[TEST EXECUTION RESULT] : FAILURE";
               else:
                   tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                   print "TEST STEP 3:Check if dnsoverride is present in resolv.conf";
                   print "EXPECTED RESULT 3 :XDNS is enabled and dnsoverride entry should be present";
                   print "ACTUAL RESULT 3:",details;
                   print "[TEST EXECUTION RESULT] : FAILURE";

          #revert the value
          if  revertflag ==1:
              actualresult,details=ToggleXDNSStatus(tdkTestObj_Tr181_Set,default);
              if expectedresult in actualresult:
                 tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");
                 print "TEST STEP 6:Revert the XDNS Status";
                 print "EXPECTED RESULT 6 :Should Revert the XDNS Status";
                 print "ACTUAL RESULT 6:",details;
                 print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
                  print "TEST STEP 6:Revert the XDNS Status";
                  print "EXPECTED RESULT 6:Should Revert the XDNS Status";
                  print "ACTUAL RESULT 6:",details;
                  print "[TEST EXECUTION RESULT] : FAILURE";
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
