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
  <version>4</version>
  <name>TS_LMLite_AddAndDelMac_PresenceDetectDisable</name>
  <primitive_test_id/>
  <primitive_test_name>LMLiteStub_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Presence Notification Mac can be added and deleted with Presence Detect is disabled.</synopsis>
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
    <test_case_id>TC_LMLite_21</test_case_id>
    <test_objective>This test case is to check if Presence Notification Mac present in Host table entries  can be added and deleted with Presence Detect is disabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_SetOnly
TDKB_TR181Stub_Set
TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable
Device.Hosts.X_RDKCENTRAL-COM_AddPresenceNotificationMac
Device.Hosts.X_RDKCENTRAL-COM_DeletePresenceNotificationMac</input_parameters>
    <automation_approch>1.Load The module.
2.Get the no of Hosts using Device.Hosts.HostNumberOfEntries .
3.Check for the active hosts Device.Hosts.Host.{i}.Active" and get the instance number of active hosts.
4.Get the active hosts physical address using  Device.Hosts.Host.{i}.PhysAddress .
5.Do a get on Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable and disable the state if not disabled .
6.Now try to add and delete the MAc with the one received from Host table entries using Device.Hosts.X_RDKCENTRAL-COM_AddPresenceNotificationMaca and Device.Hosts.X_RDKCENTRAL-COM_DeletePresenceNotificationMac and it should fail.
7.TM will display the  SUCCESS  or FAILURE results accordingly.
8.Unload the module</automation_approch>
    <expected_output>Adding or Deleting a Presence Notification Mac with Presence Detect disabled should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>LMLITE</test_stub_interface>
    <test_script>TS_LMLite_AddAndDelMac_PresenceDetectDisable</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_AddAndDelMac_PresenceDetectDisable');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
flag = 1;
revertflag = 1;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    #Get the Number of Hosts from Lmlite
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Hosts.HostNumberOfEntries");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoOfHosts = tdkTestObj.getResultDetails();
    ActiveHost = 0;
    num = 0;
    if expectedresult in actualresult and int(NoOfHosts)>0:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the number of hosts";
       print "EXPECTED RESULT 1: Should get the number of hosts";
       print "ACTUAL RESULT 1: Number of hosts :%s" %NoOfHosts;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       for inst in range(1,int(NoOfHosts)+1):
           #Get the Active Clients from the Host table
           tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
           tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%d.Active" %inst);
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           Status = tdkTestObj.getResultDetails();

           if expectedresult in actualresult and "true" in Status:
              print " Active Host found at the instance number: ",inst;
              ActiveHost = 1;
              num = int(inst);
              break;
           else:
              ActiveHost = 0;

       if ActiveHost ==1 :
          tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%d.PhysAddress" %num);
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          hostMacAddress = tdkTestObj.getResultDetails();

          if expectedresult in actualresult:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Get the MAC address of the LAN Client   ";
             print "EXPECTED RESULT 2: Get the MAC address of the device";
             print "ACTUAL RESULT 2: Get MAC address :",hostMacAddress;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable");
             #Execute the test case in DUT
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             status = tdkTestObj.getResultDetails();

             if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the status of Presence Detect";
                print "EXPECTED RESULT 3: should get the status of Presence Detect";
                print "ACTUAL RESULT 3: Status is:",status;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if status == "true":
                   tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                   tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable");
                   tdkTestObj.addParameter("ParamValue","false");
                   tdkTestObj.addParameter("Type","bool");
                   expectedresult="SUCCESS";
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();

                   if expectedresult in actualresult:
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 4:Set Presence Detect status to false";
                      print "EXPECTED RESULT 4: should set the status of Presence Detect status to false";
                      print "ACTUAL RESULT 4: Status is:",details;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                      flag = 1;
                      revertflag = 0;
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 4:Set Presence Detect status to false";
                       print "EXPECTED RESULT 4: should set the status of Presence Detect status to false";
                       print "ACTUAL RESULT 4: Status is:",details;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                       flag = 0;

                if flag == 1:
                   tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly');
                   tdkTestObj.addParameter("ParamName","Device.Hosts.X_RDKCENTRAL-COM_AddPresenceNotificationMac");
                   tdkTestObj.addParameter("ParamValue",hostMacAddress);
                   tdkTestObj.addParameter("Type","string");
                   expectedresult="FAILURE";
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();
                   if expectedresult in actualresult:
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 4: Add the MAC present in host table to Presence Notification Mac when presence detect is disabled";
                      print "EXPECTED RESULT 4: Should not add the MAC present in host table to Presence Notification Mac when presence detect is disabled";
                      print "ACTUAL RESULT 4: MAC addition failed";
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly');
                      tdkTestObj.addParameter("ParamName","Device.Hosts.X_RDKCENTRAL-COM_DeletePresenceNotificationMac");
                      tdkTestObj.addParameter("ParamValue",hostMacAddress);
                      tdkTestObj.addParameter("Type","string");
                      expectedresult="FAILURE";
                      tdkTestObj.executeTestCase(expectedresult);
                      actualresult = tdkTestObj.getResult();
                      details = tdkTestObj.getResultDetails();
                      if expectedresult in actualresult:
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 5: Delete the MAC present in Presence Notification Mac when presence detect is disabled";
                         print "EXPECTED RESULT 5: Should not delete  the MAC present in Presence Notification Mac when presence detect is disabled";
                         print "ACTUAL RESULT 5: MAC deletion failed";
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 5: Delete the MAC present in Presence Notification Mac when presence detect is disabled";
                          print "EXPECTED RESULT 5: Should  not delete  the MAC present in Presence Notification Mac when presence detect is disabled";
                          print "ACTUAL RESULT 5: MAC deletion success";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Add the MAC present in host table to Presence Notification Mac when presence detect is disabled";
                        print "EXPECTED RESULT 4: Should not add the MAC present in host table to Presence Notification Mac when presence detect is disabled";
                        print "ACTUAL RESULT 4: Sucessfully  added MAc";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                   if  revertflag == 0:
                       #revert the value
                       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable");
                       tdkTestObj.addParameter("ParamValue",status);
                       tdkTestObj.addParameter("Type","bool");
                       expectedresult="SUCCESS";
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       details = tdkTestObj.getResultDetails();

                       if expectedresult in actualresult:
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 6: Revert the status to previous";
                          print "EXPECTED RESULT 6: Should revert the status to previous";
                          print "ACTUAL RESULT 6: Revert successfull";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";
                       else:
                           tdkTestObj.setResultStatus("FAILURE");
                           print "TEST STEP 6: Revert the status to previous";
                           print "EXPECTED RESULT 6: Should revert the status to previous";
                           print "ACTUAL RESULT 6: Revertion failed";
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                     print "Presence detect was enabled and disabling the status failed"
                     tdkTestObj.setResultStatus("FAILURE");
                     print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Get the status of Presence Detect";
                 print "EXPECTED RESULT 3: should get the status of Presence Detect as false";
                 print "ACTUAL RESULT 3: Status is:",status;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Get the MAC address of the LAN Client   ";
              print "EXPECTED RESULT 2: Get the MAC address of the device";
              print "ACTUAL RESULT 2: Get MAC address failed";
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           print "No active hosts found"
           tdkTestObj.setResultStatus("FAILURE");
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of hosts";
        print "EXPECTED RESULT 1: Should get the number of hosts";
        print "ACTUAL RESULT 1: Number of hosts :%s" %NoOfHosts;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
