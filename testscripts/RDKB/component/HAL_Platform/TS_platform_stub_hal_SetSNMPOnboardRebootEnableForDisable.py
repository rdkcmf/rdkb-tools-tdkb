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
  <name>TS_platform_stub_hal_SetSNMPOnboardRebootEnableForDisable</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_SetSNMPOnboardRebootEnable</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the platform hal api platform_hal_SetSNMPOnboardRebootEnable by passing disable value</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_HAL_Platform_46</test_case_id>
    <test_objective>To check the functionality of SNMP reboot disable using hal api platform_hal_SetSNMPOnboardRebootEnable()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTDK.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetSNMPOnboardRebootEnable()</api_or_interface_used>
    <input_parameters>SNMPonboard - indicates whether to go for a reboot</input_parameters>
    <automation_approch>1.Load the module.
2.Get the current uptime of the device and store the value.
3.Invoke the platform HAL API platform_hal_SetSNMPOnboardRebootEnable by passing disable value
4.Check for successful set operation
5.Initiate a Reboot through SNMP
6.Get the uptime and the uptime should be greater than the previously stored uptime to ensure device did not go for a reboot.
7.Now the device should  not go for a reboot
8.Validation of  the result is done within the python script and send the result status to Test Manager.
9.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub
10.Unload the module</automation_approch>
    <expected_output>The  set operation should be success and DUT should not go for  reboot.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFORM</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetSNMPOnboardRebootEnableForDisable</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;
from tdkbVariables import *;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
obj1= tdklib.TDKScriptingLibrary("sysutil","1");
obj2 = tdklib.TDKScriptingLibrary("pam","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetSNMPOnboardRebootEnableForDisbale');
obj1.configureTestCase(ip,port,'TS_platform_stub_hal_SetSNMPOnboardRebootEnableForDisable');
obj2.configureTestCase(ip,port,'TS_platform_stub_hal_SetSNMPOnboardRebootEnableForDisable');
#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
result1 = obj1.getLoadModuleResult();
result2 = obj2.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %result;
print "[LIB LOAD STATUS]  :  %s" %result1;
print "[LIB LOAD STATUS]  :  %s" %result2;

if "SUCCESS" in result.upper() and "SUCCESS" in result1.upper() and "SUCCESS" in result2.upper():

   obj.setLoadModuleStatus("SUCCESS");
   obj1.setLoadModuleStatus("SUCCESS");
   obj2.setLoadModuleStatus("SUCCESS");

   tdkTestObj = obj2.createTestStep('pam_GetParameterValues');
   tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
   expectedresult="SUCCESS";

   #Execute the test case in DUT
   tdkTestObj.executeTestCase(expectedresult);
   actualresult = tdkTestObj.getResult();
   Olduptime = tdkTestObj.getResultDetails();

   if expectedresult in actualresult:
      #Set the result status of execution
      tdkTestObj.setResultStatus("SUCCESS");
      print "STEP 1 :Get the uptime";
      print "EXPECTED RESULT 1: Should return the uptime successfully";
      print "ACTUAL RESULT 1:UpTime before reboot is %s" %Olduptime;
      print "[TEST EXECUTION RESULT]: SUCCESS";
      tdkTestObj.setResultStatus("SUCCESS");

      #Prmitive test case which associated to this Script
      tdkTestObj = obj.createTestStep('platform_stub_hal_SetSNMPOnboardRebootEnable');
      expectedresult ="SUCCESS"
      setValue = "disable"
      tdkTestObj.addParameter("SNMPonboard",setValue)
      #Execute the test case in DUT
      tdkTestObj.executeTestCase("expectedresult");
      #Get the result of execution
      actualresult = tdkTestObj.getResult();
      details = tdkTestObj.getResultDetails();
      if expectedresult in actualresult:
         print" TEST STEP 2: Set the SetSNMPOnboardRebootEnable to false";
         print" EXPECTED  RESULT 2: Should successfully set the SetSNMPOnboardRebootEnable";
         print" ACTUAL RESULT 2: %s" %details
         print"[TEST EXECUTION RESULT] : %s" %actualresult;

         tdkTestObj.setResultStatus("SUCCESS");
         # Resetting device using snmp command
         #Get the Community String
         communityString = snmplib.getCommunityString(obj1,"snmpset");
         #Get the IP Address
         ipaddress = snmplib.getIPAddress(obj1);
         ########## Script to Execute the snmp command ###########
         actResponse =snmplib.SnmpExecuteCmd("snmpset", communityString, "-v 2c", "1.3.6.1.2.1.69.1.1.3.0 i 1", ipaddress);
         if "INTEGER" in actResponse:
            print "TEST STEP 3 : Check for  successful SNMP set"
            print "EXPECTED RESULT 3:Should successfully set the SNMP OID for reboot"
            print"ACTUAL RESULT 3: SNMP set for reboot successful"
            print "[TEST EXECUTION RESULT]: SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");

            #sleep for one minute and check uptime
            sleep(60);

            #checking for uptime to ensure device did not go for a reboot
            tdkTestObj = obj2.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            curuptime = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and int(curuptime) > int(Olduptime):
               print" TEST STEP 4: Get the uptime of the device after disabling snmp reboot";
               print" EXPECTED RESULT 4: Should get the uptime of the device greater than previous retrieved uptime";
               print" ACTUAL RESULT 4: Uptime before disabling reboot is %s greater than old uptime %s" %(curuptime,Olduptime);
               print"[TEST EXECUTION RESULT] : SUCCESS";
               tdkTestObj.setResultStatus("SUCCESS");
            else:
                print" TEST STEP 4: Get the uptime of the device after disabling snmp reboot";
                print" EXPECTED RESULT 4: Should get the uptime of the device greater than previous retrieved uptime";
                print" ACTUAL RESULT 4: Uptime before disabling reboot is %s greater than old uptime %s" %(curuptime,Olduptime);
                print"[TEST EXECUTION RESULT] : FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
         else:
             #Set the result status of execution
             print "TEST STEP 3 : Check for  successful SNMP set"
             print "EXPECTED RESULT 3:Should successfully set the SNMP OID for reboot"
             print "ACTUAL RESULT 3: SNMP set failed for reboot"
             print "[TEST EXECUTION RESULT]: FAILURE";
             tdkTestObj.setResultStatus("FAILURE");
      else:
          print" TEST STEP 2: Set the SetSNMPOnboardRebootEnable false";
          print" EXPECTED  RESULT 2: Should successfully set the SetSNMPOnboardRebootEnable";
          print" ACTUAL RESULT 2: %s" %details
          print "[TEST EXECUTION RESULT] : %s" %actualresult;
          tdkTestObj.setResultStatus("FAILURE");
   else:
       #Set the result status of execution
       tdkTestObj.setResultStatus("FAILURE");
       print "STEP 1 :Get the uptime";
       print "EXPECTED RESULT 1: Should return the uptime successfully";
       print "ACTUAL RESULT 1:UpTime before reboot is %s" %Olduptime;
       print "[TEST EXECUTION RESULT]: SUCCESS";
       tdkTestObj.setResultStatus("FAILURE");

   obj.unloadModule("halplatform");
   obj1.unloadModule("sysutil");
   obj2.unloadModule("pam");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
