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
  <name>TS_PAM_SetInvalidAutoRebootuptime</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set a Invalid  Window time for Auto Reboot uptime and validate</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_PAM_163</test_case_id>
    <test_objective>This test case is to set  a Invalid  Window time for Auto Reboot uptime and validate</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime</input_parameters>
    <automation_approch>1. Load the Module
2.Perform a Factory reset and check if Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime is 120 and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.Enable is true
3.Try setting Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime  to the invalid range of values and should fail
4.Revert the Auto Reboot UpTime to initial if a invalid value is set and mark the script as failure
5.Unload the Module.</automation_approch>
    <expected_output>The invalid range values set for  Auto Reboot UpTime should fail </expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_SetInvalidAutoRebootuptime</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetInvalidAutoRebootuptime');
obj1.configureTestCase(ip,port,'TS_PAM_SetInvalidAutoRebootuptime');
#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
loadmodulestatus1 = obj1.getLoadModuleResult();
flag =0;
SetValue =0;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("paramType","string");
    expectedresult="SUCCESS";
    #save device's current state before it goes for reboot
    obj.saveCurrentState();

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Initiate factory reset ";
       print "EXPECTED RESULT 1: Should initiate factory reset";
       print "ACTUAL RESULT 1: %s" %details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       #Restore the device state saved before reboot
       obj.restorePreviousStateAfterReboot();

       tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.Enable");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();

       if expectedresult in actualresult  and details == "true":
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the Auto Reboot Status";
          print "EXPECTED RESULT 2: Should Get the Auto Reboot Status as enabled";
          print "ACTUAL RESULT 2: %s" %details;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          defaultUptime = tdkTestObj.getResultDetails();

          if expectedresult in actualresult  and int(defaultUptime)== 120:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the AutoReboot UpTime";
             print "EXPECTED RESULT 3: Should Get the Auto Reboot Uptime as 120";
             print "ACTUAL RESULT 3: %s" %defaultUptime;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             #The valid range is 1-365
             InvalidValue = [-1,0,366,367]
             # getting length of list
             length = len(InvalidValue);

             for i in range(length):
                 print "Setting Auto Reboot Uptime to ",InvalidValue[i];

                 tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
                 tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime")
                 tdkTestObj.addParameter("ParamValue",str(InvalidValue[i]));
                 tdkTestObj.addParameter("Type","int");
                 expectedresult= "FAILURE";

                 #Execute testcase on DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 Setresult = tdkTestObj.getResultDetails();

                 SetValue = InvalidValue[i];

                 if expectedresult in actualresult:
                    flag =0;
                    print "The Invalid value %d  failed to set " %SetValue;
                 else:
                     flag =1;
                     print"The Invalid value %d  did not failed to set " %SetValue;
                     break;

             if flag ==0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Set the AutoReboot UpTime to a Invalid range";
                print "EXPECTED RESULT 4: Should not Set the Auto Reboot Uptime to a Invalid range";
                print "ACTUAL RESULT 4: Auto Reboot Uptime failed to set the Invalid Range";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Set the AutoReboot UpTime to a Invalid range";
                 print "EXPECTED RESULT 4: Should not Set the Auto Reboot Uptime to a Invalid range";
                 print "ACTUAL RESULT 4: Auto Reboot Uptime was set to Invalid Range";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";

                 #Reverting the value
                 tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                 tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AutoReboot.UpTime")
                 tdkTestObj.addParameter("ParamValue",defaultUptime);
                 tdkTestObj.addParameter("Type","int");
                 expectedresult= "SUCCESS";
                 #Execute testcase on DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 Setresult = tdkTestObj.getResultDetails();

                 if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Set the AutoReboot UpTime to its default value";
                    print "EXPECTED RESULT 5: Should Set the Auto Reboot Uptime to its default value";
                    print "ACTUAL RESULT 5: Revert was success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                 else:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 5: Set the AutoReboot UpTime to its default value";
                     print "EXPECTED RESULT 5: Should Set the Auto Reboot Uptime to its default value";
                     print "ACTUAL RESULT 5: Revert failed";
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] :FAILURE"
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Get the AutoReboot UpTime";
              print "EXPECTED RESULT 3: Should Get the Auto Reboot Uptime as 10";
              print "ACTUAL RESULT 3: %s" %defaultUptime;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] :FAILURE";
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the Auto Reboot Status";
           print "EXPECTED RESULT 2: Should Get the Auto Reboot Status as disabled";
           print "ACTUAL RESULT 2: %s" %details;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should initiate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
    obj1.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
     obj1.setLoadModuleStatus("FAILURE");
