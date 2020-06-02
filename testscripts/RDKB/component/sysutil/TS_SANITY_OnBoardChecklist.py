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
  <name>TS_SANITY_OnBoardChecklist</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify on-boarding process logging in
the already onboarded device</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_SYSUTIL_30</test_case_id>
    <test_objective>This test case is to check if the On-boarding process and the related files are present in the device which is On-boarded</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the modules
2. check if the device is On Boarded and ONBOARD_LOGGING_ENABLE,.device_onboarded files are present .
3. Check if there is no snmp-onboard-reboot event
4. check if the unit_activated is 1.
5.Unload module</automation_approch>
    <expected_output>the onBoarded related files should be present and unit_activated to be one and no snmp-onboard-reboot event should be present</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_OnBoardChecklist</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_OnBoardChecklist');
sysObj.configureTestCase(ip,port,'TS_SANITY_OnBoardChecklist');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('LMLiteStub_Get');
    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_OnBoarding_State");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details == "OnBoarded":
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the OnBoarding_State";
       print "EXPECTED RESULT 1: Should get the OnBoarding_State as OnBoarded";
       print "ACTUAL RESULT 1: OnBoarding_State is :%s" %details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       #Check whether the file is present or not
       tdkTestObj = sysObj.createTestStep('ExecuteCmd');
       cmd = "[ -f /etc/ONBOARD_LOGGING_ENABLE ] && echo \"File exist\" || echo \"File does not exist\"";
       tdkTestObj.addParameter("command",cmd);
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if details == "File exist":
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Check for existence of ONBOARD_LOGGING_ENABLE file";
          print "EXPECTED RESULT 2:ONBOARD_LOGGING_ENABLE file should be present";
          print "ACTUAL RESULT 2:ONBOARD_LOGGING_ENABLE file is present";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          #Check whether the file is present or not
          tdkTestObj = sysObj.createTestStep('ExecuteCmd');
          cmd = "[ -f /nvram/.device_onboarded ] && echo \"File exist\" || echo \"File does not exist\"";
          tdkTestObj.addParameter("command",cmd);
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
          if details == "File exist":
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Check for existence of .device_onboarded file";
             print "EXPECTED RESULT 3: .device_onboarded file should be present";
             print "ACTUAL RESULT 3:.device_onboarded  file is present";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = sysObj.createTestStep('ExecuteCmd');
             cmd= "syscfg get unit_activated";
             expectedresult="SUCCESS";
             tdkTestObj.addParameter("command",cmd);
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             syscfg_unit_activated  = tdkTestObj.getResultDetails().strip().replace("\\n", "");

             if expectedresult in actualresult and int(syscfg_unit_activated)== 1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Get the unit_activated via syscfg get";
                print "EXPECTED RESULT 4: Should get the unit_activated as 1 via syscfg get";
                print "ACTUAL RESULT 4: unit_activated returned via syscfg get:%s" %syscfg_unit_activated;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                cmd= "sysevent get snmp-onboard-reboot";
                expectedresult="SUCCESS";
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                snmponboardreboot  = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if expectedresult in actualresult and snmponboardreboot == "":
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 5: Get the snmp-onboard-reboot via syscfg get";
                   print "EXPECTED RESULT 5: Should get the  snmp-onboard-reboot as empty  via syscfg get";
                   print "ACTUAL RESULT 5: snmp-onboard-reboot  via syscfg get:%s" %snmponboardreboot;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Get the snmp-onboard-reboot via syscfg get";
                    print "EXPECTED RESULT 5: Should get the  snmp-onboard-reboot as empty  via syscfg get";
                    print "ACTUAL RESULT 5: snmp-onboard-reboot  via syscfg get:%s" %snmponboardreboot;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Get the unit_activated via syscfg get";
                 print "EXPECTED RESULT 4: Should get the unit_activated as 1 via syscfg get";
                 print "ACTUAL RESULT 4: unit_activated returned via syscfg get:%s" %syscfg_unit_activated;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Check for existence of .device_onboarded file";
              print "EXPECTED RESULT 3: .device_onboarded file should be present";
              print "ACTUAL RESULT 3:.device_onboarded  file is not present";
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Check for existence of ONBOARD_LOGGING_ENABLE file";
           print "EXPECTED RESULT 2:ONBOARD_LOGGING_ENABLE file should be present";
           print "ACTUAL RESULT 2:ONBOARD_LOGGING_ENABLE file is not present";
           #Get the result of execution
           print "[TEST EXECUTION RESULT]: FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the OnBoarding_State";
        print "EXPECTED RESULT 1: Should get the OnBoarding_State as OnBoarded";
        print "ACTUAL RESULT 1: OnBoarding_State is :%s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("lmlite")
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load lmlite/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
