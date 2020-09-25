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
  <name>TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_MAC_TOTAL_COUNT</name>
  <primitive_test_id/>
  <primitive_test_name>ETHAgent_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if marker  ETH_MAC_{i}_TOTAL_COUNT is present when EthLog Enabled with a connected LAN Client</synopsis>
  <groups_id/>
  <execution_time>25</execution_time>
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
    <test_case_id>TC_ETHAGENT_8</test_case_id>
    <test_objective>This test case is to check if marker ETH_MAC_{i}_TOTAL_COUNT is present when EthLog Enabled with a connected LAN Client</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. DUT must have a LAN client connected</pre_requisite>
    <api_or_interface_used>
N/A</api_or_interface_used>
    <input_parameters>Device.Hosts.HostNumberOfEntries
Device.Hosts.Host.{i}.Layer1Interface
Device.Hosts.Host.{i}.PhysAddress
Device.Ethernet.InterfaceNumberOfEntries
Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress
Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled
Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod
Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries</input_parameters>
    <automation_approch>1.Load the pam and sysutil module
2. Get the number of hosts connected using Device.Hosts.HostNumberOfEntries
3. Check at what instance  the connected host is Ethernet using Device.Hosts.Host.{i}.Layer1Interface
4. At the same instance get the devices Mac address using Device.Hosts.Host.{i}.PhysAddress
5. Loop for the Device.Ethernet.InterfaceNumberOfEntries and  check at what instance the mac address equals to the one received from the Host table entry using Device.Ethernet.Interface,{i}.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress to confirm on the active LAN client connected and at what interface was the client connected.
6. Get the default value of  Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled  and Enable it.
7. Get the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod and set it 10 sec .
8. Now grep on /rdklogs/logs/eth_telemetry.txt and check for ETH_MAC_{i}_TOTAL_COUNT marker with polling logic of 15 min and retrieve the mac.
9  Check if the count equals to the value present in Device.Ethernet.Interface.{i}.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries
10.Revert the parameters set to their default
11.Unload the module</automation_approch>
    <expected_output>ETH_MAC_{i}_TOTAL_COUNT  marker should be present when Ethlog is enabled </expected_output>
    <priority>High</priority>
    <test_stub_interface>ETHAGENT</test_stub_interface>
    <test_script>TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_MAC_TOTAL_COUNT</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_MAC_TOTAL_COUNT');
sysObj.configureTestCase(ip,port,'TS_ETHAGENT_CheckTelemetryMarkerWithEthClient_ETH_MAC_TOTAL_COUNT');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
revertflag = 0;
flag =1;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.Hosts.HostNumberOfEntries");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoOfHosts = tdkTestObj.getResultDetails();
    clientfound= 0;

    if expectedresult in actualresult and int(NoOfHosts)>0:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the number of hosts from Host Table";
       print "EXPECTED RESULT 1: Should get the number of hosts";
       print "ACTUAL RESULT 1: Number of hosts :%s" %NoOfHosts;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       #Find the Ethernet host amoung the listed Hosts.
       for i in range(1,int(NoOfHosts)+1):
           if int(clientfound) == 1:
              break;
           tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%d.Layer1Interface" %i);
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           Status = tdkTestObj.getResultDetails();

           if "Ethernet" in Status:
              clientfound =1;
              tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%d.PhysAddress" %i);
              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              macHost = tdkTestObj.getResultDetails();
              macHost = macHost.upper();

              if expectedresult in actualresult  and macHost!="":
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 2: Get the mac of connected ethernet client from Host Table";
                 print "EXPECTED RESULT 2: Should get the mac of connected ethernet client";
                 print "ACTUAL RESULT 2: mac :",macHost;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";

                 tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                 tdkTestObj.addParameter("ParamName","Device.Ethernet.InterfaceNumberOfEntries");
                 expectedresult="SUCCESS";
                 #Execute the test case in DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 NoOfInstances = tdkTestObj.getResultDetails();

                 if expectedresult in actualresult and int(NoOfInstances)>0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get the number of interfaces for Ethernet";
                    print "EXPECTED RESULT 3: Should get the number of interfaces for Ethernet";
                    print "ACTUAL RESULT 3: Number of interfaces: %s" %NoOfInstances;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    clientInterface =0;
                    #Find the client connected interface
                    for j in range(1,int(NoOfInstances)+1):
                        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                        tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%d.X_RDKCENTRAL-COM_AssociatedDevice.1.MACAddress" %j);
                        expectedresult="SUCCESS";
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        EthernetMAC = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult and EthernetMAC == macHost:
                           clientInterface =j;
                           #Set the result status of execution
                           tdkTestObj.setResultStatus("SUCCESS");
                           print "TEST STEP 4: Get the Associated Devices MAC ";
                           print "EXPECTED RESULT 4: Should get the Associated Devices MAC";
                           print "ACTUAL RESULT 4: Associated Devices MAC:",EthernetMAC;
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : SUCCESS";
                           print "*****************************************************"
                           print "Ethernet Client connected at %d interface" %clientInterface;
                           break;
                    if clientInterface !=0:
                       tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled");
                       expectedresult="SUCCESS";
                       #Execute the test case in DUT
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       logEnable  = tdkTestObj.getResultDetails();
                       if expectedresult in actualresult:
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 5: Get the Ethernet Log Enable state ";
                          print "EXPECTED RESULT 5: Should get the Ethernet Log Enable state";
                          print "ACTUAL RESULT 5: Ethernet Log Enable state :",logEnable;
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";

                          if logEnable == "false":
                             tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                             tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled");
                             tdkTestObj.addParameter("ParamValue","true");
                             tdkTestObj.addParameter("Type","bool");
                             expectedresult="SUCCESS";
                             tdkTestObj.executeTestCase(expectedresult);
                             actualresult = tdkTestObj.getResult();
                             details = tdkTestObj.getResultDetails();
                             if expectedresult in actualresult:
                                flag =1;
                                revertflag =1;
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 6: Set the  Ethernet Log Enable state to true";
                                print "EXPECTED RESULT 6: Should set the  Ethernet Log Enable state to true";
                                print "ACTUAL RESULT 6: Ethernet Log Enable state :",details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                             else:
                                 flag =0;
                                 revertflag =0;
                                 tdkTestObj.setResultStatus("FAILURE");
                                 print "TEST STEP 6: Set the  Ethernet Log Enable state to true";
                                 print "EXPECTED RESULT 6: Should set the  Ethernet Log  Enable state to true";
                                 print "ACTUAL RESULT 6:  Ethernet Log Enable state :",details;
                                 #Get the result of execution
                                 print "[TEST EXECUTION RESULT] : FAILURE";

                          if flag == 1:
                             tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                             tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod");
                             expectedresult="SUCCESS";
                             #Execute the test case in DUT
                             tdkTestObj.executeTestCase(expectedresult);
                             actualresult = tdkTestObj.getResult();
                             DeflogInt = tdkTestObj.getResultDetails();
                             if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7: Get the  Ethernet LogPeriod";
                                print "EXPECTED RESULT 7: Should get the Ethernet LogPeriod";
                                print "ACTUAL RESULT 7: Ethernet LogPeriod:",DeflogInt;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod");
                                tdkTestObj.addParameter("ParamValue","10");
                                tdkTestObj.addParameter("Type","unsignedint");
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();
                                if expectedresult in actualresult:
                                   tdkTestObj.setResultStatus("SUCCESS");
                                   print "TEST STEP 8: Set the Ethernet LogPeriod to 10 sec";
                                   print "EXPECTED RESULT 8: Should set the Ethernet LogPeriod to 10 sec";
                                   print "ACTUAL RESULT 8:",details;
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] : SUCCESS";

                                   #Check whether the eth_telemetry.txt file is present or not
                                   tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                                   cmd = "[ -f /rdklogs/logs/eth_telemetry.txt ] && echo \"File exist\" || echo \"File does not exist\"";
                                   tdkTestObj.addParameter("command",cmd);
                                   expectedresult="SUCCESS";
                                   tdkTestObj.executeTestCase(expectedresult);
                                   actualresult = tdkTestObj.getResult();
                                   details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                                   if details == "File exist":
                                      tdkTestObj.setResultStatus("SUCCESS");
                                      print "TEST STEP 9: Check for eth_telemetry log file presence";
                                      print "EXPECTED RESULT 9:eth_telemetry log file should be present";
                                      print "ACTUAL RESULT 9:eth_telemetry log file is present";
                                      #Get the result of execution
                                      print "[TEST EXECUTION RESULT] : SUCCESS";

                                      markerfound = 0;
                                      for i in range(1,5):
                                          if markerfound == 1:
                                             break;
                                          else:
                                              #Query for the Telemetry Marker
                                              query="cat /rdklogs/logs/eth_telemetry.txt | grep -i \"ETH_MAC_%d_TOTAL_COUNT:\""%j;
                                              print "query:%s" %query
                                              tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                                              tdkTestObj.addParameter("command", query)
                                              expectedresult="SUCCESS";
                                              tdkTestObj.executeTestCase(expectedresult);
                                              actualresult = tdkTestObj.getResult();
                                              details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                                              print "Marker Detail Found fromLog file is: %s "%details;

                                          if  details.endswith("0") or details == "" or  "TOTAL_COUNT" not in details:
                                              markerfound = 0;
                                              sleep(300);
                                          else:
                                               markerValue = details.split("TOTAL_COUNT:")[1].split(',')[0].strip().replace("\\n","");
                                               markerfound = 1;

                                      if expectedresult in actualresult and markerfound == 1 and markerValue!= "":
                                         tdkTestObj.setResultStatus("SUCCESS");
                                         print "TEST STEP 10: ETH_MAC_%d_TOTAL_COUNT Marker should be present"%j;
                                         print "EXPECTED RESULT 10: ETH_MAC_%d_TOTAL_COUNT Marker should be present"%j;
                                         print "ACTUAL RESULT 10:ETH_MAC_%d_TOTAL_COUNT Marker is %s" %(j,markerValue);
                                         #Get the result of execution
                                         print "[TEST EXECUTION RESULT] : SUCCESS";

                                         tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                                         tdkTestObj.addParameter("ParamName","Device.Ethernet.Interface.%d.X_RDKCENTRAL-COM_AssociatedDeviceNumberOfEntries" %j);
                                         expectedresult="SUCCESS";
                                         #Execute the test case in DUT
                                         tdkTestObj.executeTestCase(expectedresult);
                                         actualresult = tdkTestObj.getResult();
                                         noofEntries = tdkTestObj.getResultDetails();
                                         if expectedresult in actualresult:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "TEST STEP 11: Get the Associated Device Number Of Entries via TR-181 parameter";
                                            print "EXPECTED RESULT 11: Should get the  Associated Device Number Of Entries";
                                            print "ACTUAL RESULT 11:Associated Device Number Of Entries via TR-181 parameter:",noofEntries;
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : SUCCESS";

                                            if int(noofEntries) == int(markerValue):
                                               tdkTestObj.setResultStatus("SUCCESS");
                                               print "TEST STEP 12: Associated Device Number Of Entries via TR-181 parmeter and via marker should be equal";
                                               print "EXPECTED RESULT 12: Should get the  Associated Device Number Of Entries and via marker equal";
                                               print "ACTUAL RESULT 12:Associated Device Number Of Entries via TR-181 parmeter:",noofEntries,"value from marker:",markerValue;
                                               #Get the result of execution
                                               print "[TEST EXECUTION RESULT] : SUCCESS";
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "TEST STEP 12: Associated Device Number Of Entries via TR-181 parmeter and via marker should be equal";
                                                print "EXPECTED RESULT 12: Should get the  Associated Device Number Of Entries and via marker equal";
                                                print "ACTUAL RESULT 12:Associated Device Number Of Entries via TR-181 parmeter:",noofEntries,"value from marker:",markerValue;
                                                #Get the result of execution
                                                print "[TEST EXECUTION RESULT] : FAILURE";
                                         else:
                                             tdkTestObj.setResultStatus("FAILURE");
                                             print "TEST STEP 11: Get the Associated Device Number Of Entries via TR-181 parameter";
                                             print "EXPECTED RESULT 11: Should get the  Associated Device Number Of Entries";
                                             print "ACTUAL RESULT 11:Associated Device Number Of Entries via TR-181 parameter:",noofEntries;
                                             #Get the result of execution
                                             print "[TEST EXECUTION RESULT] : FAILURE";
                                      else:
                                          tdkTestObj.setResultStatus("FAILURE");
                                          print "TEST STEP 10: ETH_MAC_%d_TOTAL_COUNT Marker should be present"%j;
                                          print "EXPECTED RESULT 10: ETH_MAC_%d_TOTAL_COUNT Marker should be present"%j;
                                          print "ACTUAL RESULT 10:ETH_MAC_%d_TOTAL_COUNT Marker not found or doesnt have non-zero value"%j;
                                          #Get the result of execution
                                          print "[TEST EXECUTION RESULT] : FAILURE";
                                   else:
                                       tdkTestObj.setResultStatus("FAILURE");
                                       print "TEST STEP 9: Check for eth_telemetry log file presence";
                                       print "EXPECTED RESULT 9:eth_telemetry log file should be present";
                                       print "ACTUAL RESULT 9:eth_telemetry log file is not present";
                                       #Get the result of execution
                                       print "[TEST EXECUTION RESULT] : FAILURE";

                                   #revert the log interval to previous
                                   tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                                   tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogPeriod");
                                   tdkTestObj.addParameter("ParamValue",DeflogInt);
                                   tdkTestObj.addParameter("Type","unsignedint");
                                   expectedresult="SUCCESS";
                                   tdkTestObj.executeTestCase(expectedresult);
                                   actualresult = tdkTestObj.getResult();
                                   details = tdkTestObj.getResultDetails();
                                   if expectedresult in actualresult:
                                      tdkTestObj.setResultStatus("SUCCESS");
                                      print "TEST STEP 13: Revert the Ethernet LogPeriod to previous";
                                      print "EXPECTED RESULT 13: Should revert the Ethernet LogPeriod to previous";
                                      print "ACTUAL RESULT 13: Revert successfull";
                                      #Get the result of execution
                                      print "[TEST EXECUTION RESULT] : SUCCESS";
                                   else:
                                       tdkTestObj.setResultStatus("FAILURE");
                                       print "TEST STEP 13: Revert the Ethernet LogPeriod to previous";
                                       print "EXPECTED RESULT 13: Should revert the Ethernet LogPeriod to previous";
                                       print "ACTUAL RESULT 13: Revertion failed";
                                       #Get the result of execution
                                       print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP 8: Set the Ethernet LogPeriod to 10 sec";
                                    print "EXPECTED RESULT 8: Should set the Ethernet LogPeriod to 10 sec";
                                    print "ACTUAL RESULT 8:",details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                             else:
                                 tdkTestObj.setResultStatus("FAILURE");
                                 print "TEST STEP 7: Get the  Ethernet LogPeriod";
                                 print "EXPECTED RESULT 7: Should get the Ethernet LogPeriod";
                                 print "ACTUAL RESULT 7: Ethernet LogPeriod:",DeflogInt;
                                 #Get the result of execution
                                 print "[TEST EXECUTION RESULT] : FAILURE";
                             #Revert the Value
                             if revertflag == 1:
                                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Logging.xOpsDMEthLogEnabled");
                                tdkTestObj.addParameter("ParamValue",logEnable);
                                tdkTestObj.addParameter("Type","bool");
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();
                                if expectedresult in actualresult:
                                   tdkTestObj.setResultStatus("SUCCESS");
                                   print "TEST STEP 14: Revert the Ethernet LogEnable state to previous";
                                   print "EXPECTED RESULT 14: Should revert the Ethernet LogEnable state to previous";
                                   print "ACTUAL RESULT 14: Revert success";
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] :SUCCESS";
                                else:
                                   tdkTestObj.setResultStatus("FAILURE");
                                   print "TEST STEP 14: Revert the Ethernet LogEnable state to previous";
                                   print "EXPECTED RESULT 14: Should revert the Ethernet LogEnable state to previous";
                                   print "ACTUAL RESULT 14: Revert failed";
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] :FAILURE";
                          else:
                              tdkTestObj.setResultStatus("FAILURE");
                              print "Ethernet log was disabled and failed on enabling";
                       else:
                           tdkTestObj.setResultStatus("FAILURE");
                           print "TEST STEP 5: Get the Ethernet Log Enable state ";
                           print "EXPECTED RESULT 5: Should get the Ethernet Log Enable state";
                           print "ACTUAL RESULT 5: Ethernet Log Enable state :",logEnable;
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "Failed to find the MAc address of associated client at the available interfaces";
                 else:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 3: Get the number of interfaces for Ethernet";
                     print "EXPECTED RESULT 3: Should get the number of interfaces for Ethernet";
                     print "ACTUAL RESULT 3: Number of interfaces: %s" %NoOfInstances;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 2: Get the mac of connected ethernet client from Host Table";
                  print "EXPECTED RESULT 2: Should get the mac of connected ethernet client";
                  print "ACTUAL RESULT 2: mac :",macHost;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "No Ethernet Client Associated with DUT";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the number of hosts from Host Table";
        print "EXPECTED RESULT 1: Should get the number of hosts";
        print "ACTUAL RESULT 1: Number of hosts :%s" %NoOfHosts;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    obj.unloadModule("pam")
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
