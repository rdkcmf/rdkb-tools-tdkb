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
  <name>TS_platform_stub_hal_SetFanMaxOverride</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_setFanMaxOverride</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the set functionality of Fan Max Override</synopsis>
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
    <test_case_id>TC_HAL_Platform_42</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_SetFanMaxOverride()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetFanMaxOverride()</api_or_interface_used>
    <input_parameters>flag -true or false value</input_parameters>
    <automation_approch>1. Load  platform module.
2. check which among systemd-fan.service and systemd-fan-highspeed.service are active
3. Based on the active status of fan speed set platform_hal_SetFanMaxOverride().
4. Validate the set funciton by checking the systemd fan services
5. Revert the value back to original fan speed.
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>setFanMaxOverride value should be set successful.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFORM</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetFanMaxOverride</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetFanMaxOverride');
sysObj.configureTestCase(ip,port,'TS_platform_stub_hal_SetFanMaxOverride');

loadmodulestatus  = obj.getLoadModuleResult();
sysyutilmodulestatus = sysObj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysyutilmodulestatus

revertValue = 2
SetValue = 2

if "SUCCESS" in (loadmodulestatus.upper() and  sysyutilmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    query = "systemctl status systemd-fan.service | grep -i \"Active\" "
    print "query:%s" %query
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details= tdkTestObj.getResultDetails().strip().replace("\\n","");

    if expectedresult in actualresult:
       splitvalue = details.split("Active:")[1];
       lowspeed  = splitvalue.split(' ')[1].strip().replace("\\n","");
       print "TEST STEP 1: Get the status of systemd-fan.service";
       print "EXPECTED RESULT 1: Should Get the status of systemd-fan.service";
       print "ACTUAL RESULT1: systemd-fan.service is %s" %lowspeed;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS"
       tdkTestObj.setResultStatus("SUCCESS");

       query = "systemctl status systemd-fan-highspeed.service | grep -i \"Active\" "
       print "query:%s" %query
       tdkTestObj = sysObj.createTestStep('ExecuteCmd');
       tdkTestObj.addParameter("command", query)
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip().replace("\\n","");

       if expectedresult in actualresult:
          splitvalue = details.split("Active:")[1];
          highspeed = splitvalue.split(' ')[1].strip().replace("\\n","");
          print "TEST STEP 2: Get the status of systemd-fan-highspeed.service";
          print "EXPECTED RESULT 2: Should Get the status of systemd-fan-highspeed.service";
          print "ACTUAL RESULT1 2: systemd-fan-highspeed.service is %s" %highspeed;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS"
          tdkTestObj.setResultStatus("SUCCESS");

          #getting the value to be set for FanMaxOverride api
          if highspeed == "active":
             setValue = 0;
          else:
              setValue = 1;

          print "The value to be set : ",setValue

          #toggling the value
          tdkTestObj = obj.createTestStep("platform_stub_hal_setFanMaxOverride");
          tdkTestObj.addParameter("flag",setValue);
          tdkTestObj.addParameter("fanIndex", 0);
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();

          if expectedresult in  actualresult :
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Set the Fan Max Override speed";
             print "EXPECTED RESULT 3: Should set the Fan Max Override speed successfully";
             print "ACTUAL RESULT 3: %s" %details;
             print "[TEST EXECUTION RESULT] : %s" %actualresult ;

             query = "systemctl status systemd-fan-highspeed.service | grep -i \"Active\" "
             print "query:%s" %query
             tdkTestObj = sysObj.createTestStep('ExecuteCmd');
             tdkTestObj.addParameter("command", query)
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails().strip().replace("\\n","");

             if expectedresult in actualresult:
                splitvalue = details.split("Active:")[1];
                highspeed = splitvalue.split(' ')[1].strip().replace("\\n","");
                print "TEST STEP 4: Get the status of systemd-fan-highspeed.service after set Fan Max Override";
                print "EXPECTED RESULT 4: Should Get the status of systemd-fan-highspeed.service after set Fan Max Override";
                print "ACTUAL RESULT 4: systemd-fan-highspeed.service after set Fan Max Override set is %s" %highspeed;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
                tdkTestObj.setResultStatus("SUCCESS");

                if highspeed == "active":
                   checkvalue = 1;
                else:
                    checkvalue = 0;

                print "Value set by Fan Max Override:",setValue
                print "Value of systemd fan service after set",checkvalue

                if setValue == checkvalue:
                   print "TEST STEP 5: Check if Fan Max Override speed after set equals the get value systemd-fan-highspeed.service"
                   print "EXPECTED RESULT 5: Fan Max Override speed after set should equal the get value systemd-fan-highspeed.service"
                   print "ACTUAL RESULT 5: Fan Max Override speed after set equals the get value systemd-fan-highspeed.service"
                   print "[TEST EXECUTION RESULT] : SUCCESS"
                   tdkTestObj.setResultStatus("SUCCESS");

                   query = "systemctl status systemd-fan.service | grep -i \"Active\" "
                   print "query:%s" %query
                   tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                   tdkTestObj.addParameter("command", query)
                   expectedresult="SUCCESS";
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details= tdkTestObj.getResultDetails().strip().replace("\\n","");

                   if expectedresult in actualresult:
                      splitvalue = details.split("Active:")[1];
                      lowspeed  = splitvalue.split(' ')[1].strip().replace("\\n","");
                      print "TEST STEP 6: Get the status of systemd-fan.service";
                      print "EXPECTED RESULT 6: Should Get the status of systemd-fan.service";
                      print "ACTUAL RESULT 6: systemd-fan.service is %s" %lowspeed;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS"
                      tdkTestObj.setResultStatus("SUCCESS");
                      if lowspeed == "active":
                         checkvalue = 0;
                      else:
                          checkvalue = 1;

                      if setValue == checkvalue:
                         print "TEST STEP 7: Check if Fan Max Override speed after set equals the get value systemd-fan.service"
                         print "EXPECTED RESULT 7: Fan Max Override speed after set should equal the get value systemd-fan.service"
                         print "ACTUAL RESULT 7: Fan Max Override speed after set equals the get value systemd-fan.service"
                         print "[TEST EXECUTION RESULT] : SUCCESS"
                         tdkTestObj.setResultStatus("SUCCESS");
                      else:
                         print "TEST STEP 7: Check if Fan Max Override speed after set equals the get value systemd-fan.service"
                         print "EXPECTED RESULT 7: Fan Max Override speed after set should equal the get value systemd-fan.service"
                         print "ACTUAL RESULT 7: Fan Max Override speed after set does not equals the get value systemd-fan.service"
                         print "[TEST EXECUTION RESULT] : FAILURE"
                         tdkTestObj.setResultStatus("FAILURE");
                   else:
                       print "TEST STEP 6: Get the status of systemd-fan.service after set Fan Max Override";
                       print "EXPECTED RESULT 6: Should Get the status of systemd-fan.service after set Fan Max Override";
                       print "ACTUAL RESULT 6: systemd-fan.service after set Fan Max Override is %s" %lowspeed;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] :FAILURE"
                       tdkTestObj.setResultStatus("FAILURE");

                else:
                   print "TEST STEP 5: Check if Fan Max Override speed after set equals the get value systemd-fan-highspeed.service"
                   print "EXPECTED RESULT 5: Fan Max Override speed after set should equal the get value systemd-fan-highspeed.service"
                   print "ACTUAL RESULT 5: Fan Max Override speed after set does not equals the get value systemd-fan-highspeed.service"
                   print "[TEST EXECUTION RESULT] : FAILURE"
                   tdkTestObj.setResultStatus("FAILURE");
             else:
                 print "TEST STEP 4: Get the status of systemd-fan-highspeed.service after set Fan Max Override";
                 print "EXPECTED RESULT 4: Should Get the status of systemd-fan-highspeed.service after set Fan Max Override";
                 print "ACTUAL RESULT 4: systemd-fan-highspeed.service after set Fan Max Override set is %s" %highspeed;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE"
                 tdkTestObj.setResultStatus("FAILURE");

             #value to be reverted
             if  setValue == 0 :
                 revertValue  = 1;
             else:
                 revertValue = 0;

             #Reverting the value
             tdkTestObj = obj.createTestStep("platform_stub_hal_setFanMaxOverride");
             tdkTestObj.addParameter("flag",revertValue);
             tdkTestObj.addParameter("fanIndex", 0);
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails();

             if expectedresult in  actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: Revertining the Fan Max Override speed to intial";
                print "EXPECTED RESULT 5: Should set the Fan Max Override speed to initial successfully";
                print "ACTUAL RESULT 5: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 5: Revertining the Fan Max Override speed to intial";
                 print "EXPECTED RESULT 5: Should set the Fan Max Override speed to initial successfully";
                 print "ACTUAL RESULT 5:  %s" %details;
                 print "[TEST EXECUTION RESULT] : %s" %actualresult ;
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Set the Fan Max Override speed";
              print "EXPECTED RESULT 3: Should set the Fan Max Override speed successfully";
              print "ACTUAL RESULT 3: %s" %details;
              print "[TEST EXECUTION RESULT] : %s" %actualresult ;
       else:
           print "TEST STEP 2: Get the status of systemd-fan-highspeed.service";
           print "EXPECTED RESULT 2: Should Get the status of systemd-fan-highspeed.service";
           print "ACTUAL RESULT1 2: systemd-fan-highspeed.service is %s" %highspeed;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
           tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1: Get the status of systemd-fan.service";
        print "EXPECTED RESULT 1: Should Get the status of systemd-fan.service";
        print "ACTUAL RESULT1: systemd-fan.service is %s" %lowspeed;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
        tdkTestObj.setResultStatus("FAILURE");


    obj.unloadModule("halplatform");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load sysyutil/hal_platform  module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

