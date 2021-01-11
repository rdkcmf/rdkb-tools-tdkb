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
  <name>TS_PAM_SetComputeWindow_EqualtoSetAggresInterval</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the compute window equal to self heal aggressive interval and check the behaviour</synopsis>
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
    <test_case_id>TC_PAM_187</test_case_id>
    <test_objective>This test case is to set the compute window equal to self heal aggressive interval and check the behaviour</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Set
TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval</input_parameters>
    <automation_approch>1.Load the module
2.Get the current compute window and self heal aggressive interval
3.Set compute window equal to self heal aggressive interval
4.The set operation should fail,revert the value in case of failure
5.Unload the module</automation_approch>
    <expected_output>Setting compute window equal to self  aggressive interval should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_SetComputeWindow_EqualtoSetAggresInterval</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_PAM_SetComputeWindow_EqualtoSetAggresInterval');

#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
#result of connection with test component and DUT
result =obj.getLoadModuleResult();
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult ="SUCCESS";

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    defAggInt = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Self Heal Aggressive Interval";
       print "EXPECTED RESULT 1: Should Get the Self Heal Aggressive Interval";
       print "ACTUAL RESULT 1: %s" %defAggInt;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
       tdkTestObj.addParameter("ParamName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow");
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       defCompuWindow = tdkTestObj.getResultDetails();

       if expectedresult in actualresult:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the Usage Compute Window";
          print "EXPECTED RESULT 2: Should Get the Usage Compute Window";
          print "ACTUAL RESULT 2: %s" %defCompuWindow;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";

          setValue = defAggInt;
          tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
          tdkTestObj.addParameter("ParamName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow")
          tdkTestObj.addParameter("ParamValue",setValue);
          tdkTestObj.addParameter("Type","unsignedint");
          expectedresult= "FAILURE";

          #Execute testcase on DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          Setresult = tdkTestObj.getResultDetails();

          if expectedresult in actualresult:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Set the Usage Compute Window";
             print "EXPECTED RESULT 3: Should not set the Usage Compute Window  equal to self HealAggressive Interval";
             print "ACTUAL RESULT 3: %s" %Setresult;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Set the Usage Compute Window";
              print "EXPECTED RESULT 3: Should not set the Usage Compute Window  equal to self HealAggressive Interval";
              print "ACTUAL RESULT 3: %s" %Setresult;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";

              #revert in caseof invalid set
              tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
              tdkTestObj.addParameter("ParamName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow")
              tdkTestObj.addParameter("ParamValue",defCompuWindow);
              tdkTestObj.addParameter("Type","unsignedint");
              expectedresult= "FAILURE";

              #Execute testcase on DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              Setresult = tdkTestObj.getResultDetails();
              if expectedresult in actualresult:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 4: Revert the Usage Compute Window  to previous";
                 print "EXPECTED RESULT 4: Should revert the Usage Compute Window Interval to %s " %defAggInt;
                 print "ACTUAL RESULT 4: %s" %Setresult;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4: Revert the Usage Compute Window to previous";
                  print "EXPECTED RESULT 4: Should revert the Usage Compute Window to %s " %defAggInt;
                  print "ACTUAL RESULT 4: %s" %Setresult;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the Usage Compute Window";
           print "EXPECTED RESULT 2: Should Get the Usage Compute Window";
           print "ACTUAL RESULT 2: %s" %defCompuWindow;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Self Heal Aggressive Interval";
        print "EXPECTED RESULT 1: Should Get the Self Heal Aggressive Interval";
        print "ACTUAL RESULT 1: %s" %defAggInt;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
