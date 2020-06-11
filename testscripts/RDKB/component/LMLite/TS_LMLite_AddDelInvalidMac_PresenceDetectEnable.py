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
  <version>2</version>
  <name>TS_LMLite_AddDelInvalidMac_PresenceDetectEnable</name>
  <primitive_test_id/>
  <primitive_test_name>LMLiteStub_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Invalid Mac Addition and Deletion for Presence Notification with Presence Detect Enabled.</synopsis>
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
    <test_case_id>TC_LMLite_23</test_case_id>
    <test_objective>This test case is to check if  Invalid Mac can be added and deleted when Presence Detect is enabled.</test_objective>
    <test_type>Negative</test_type>
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
2.Do a get on Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable and store the value.
3.Enable the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable if disabled.
4.Now try to add and delete the  Invalid MAc using Device.Hosts.X_RDKCENTRAL-COM_AddPresenceNotificationMac and Device.Hosts.X_RDKCENTRAL-COM_DeletePresenceNotificationMac and it should be Failure.
5.If the addition and deletion of MAC failed then the result will be displayed as SUCCESSS else FAILURE
6.Revert the Presence Detect status to false.
7.Unload the module</automation_approch>
    <expected_output>Adding or Deleting a Invalid  Mac with Presence Detect enabled  should Fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>LMLITE</test_stub_interface>
    <test_script>TS_LMLite_AddDelInvalidMac_PresenceDetectEnable</test_script>
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
obj.configureTestCase(ip,port,'TS_LMLite_AddDelInvalidMac_PresenceDetectEnable');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
flag = 1;
revertflag =1;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    #Initialize a invalid MAC
    hostMacAddress =  "FF:FF:FF:FF:FF:FF";
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable");
    #Execute the test case in DUT
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    status = tdkTestObj.getResultDetails();
    if expectedresult in actualresult :
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the status of Presence Detect";
       print "EXPECTED RESULT 1: should get the status of Presence Detect";
       print "ACTUAL RESULT 1: Status is:",status;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       if status == "false":
          tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.PresenceDetect.Enable");
          tdkTestObj.addParameter("ParamValue","true");
          tdkTestObj.addParameter("Type","bool");
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();

          if expectedresult in actualresult:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Set the status of Presence Detect to true";
             print "EXPECTED RESULT 2: should set the status of Presence Detect to true";
             print "ACTUAL RESULT 2: ",details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
             flag = 1;
             revertflag =0;
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Set the status of Presence Detect to true";
              print "EXPECTED RESULT 2: should set the status of Presence Detect to true";
              print "ACTUAL RESULT 2: ",details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] :FAILURE";
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
             print "TEST STEP 3: Add the Invalid MAC not present in host table to Presence Notification Mac when presence detect is enabled";
             print "EXPECTED RESULT 3: Should not add the Invalid MAC not present in host table to Presence Notification Mac when presence detect is enabled";
             print "ACTUAL RESULT 3: MAC addition failed";
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
                print "TEST STEP 4: Delete the Invalid MAC present in Presence Notification Mac when presence detect is enabled";
                print "EXPECTED RESULT 4: Should not delete  the Invalid MAC present in Presence Notification Mac when presence detect is enabled";
                print "ACTUAL RESULT 4: MAC deletion failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Delete the Invalid MAC present in Presence Notification Mac when presence detect is enabled";
                 print "EXPECTED RESULT 4: Should  not delete  the MAC present in Presence Notification Mac when presence detect is enabled";
                 print "ACTUAL RESULT 4: MAC deletion success";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Add the Invalid MAC not present in host table to Presence Notification Mac when presence detect is enabled";
              print "EXPECTED RESULT 3: Should not add the Invalid MAC not present in host table to Presence Notification Mac when presence detect is enabled";
              print "ACTUAL RESULT 3: Sucessfully  added MAc";
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
          if revertflag == 0:
             #Revert the Value
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
                print "TEST STEP 5: Revert the status to default";
                print "EXPECTED RESULT 5: Should revert the status to default";
                print "ACTUAL RESULT 5: Revert successfull";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 5: Revert the status to default";
                 print "EXPECTED RESULT 5: Should revert the status to default";
                 print "ACTUAL RESULT 5: Revertion failed";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           print "Present detect was disabled and failed on enabling";
           tdkTestObj.setResultStatus("FAILURE");
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the status of Presence Detect";
        print "EXPECTED RESULT 1: should get the status of Presence Detect";
        print "ACTUAL RESULT 1: Status is:",status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
