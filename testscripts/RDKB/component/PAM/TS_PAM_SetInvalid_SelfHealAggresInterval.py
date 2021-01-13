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
  <name>TS_PAM_SetInvalid_SelfHealAggresInterval</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the self heal aggressive interval excepts an invalid interval</synopsis>
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
    <test_case_id>TC_PAM_190</test_case_id>
    <test_objective>This test case is to check if the self heal aggressive interval excepts an invalid interval</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval
</input_parameters>
    <automation_approch>1.Load the module
2.Get the current self heal aggressive interval
3.Set a  invalid value like 1min which is less than its min interval i,e 2mim
4.The set operation should fail
5.Unload the module</automation_approch>
    <expected_output> self heal aggressive interval should not accept a  interval below its  min value </expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_SetInvalid_SelfHealAggresInterval</test_script>
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
obj.configureTestCase(ip,port,'TS_PAM_SetInvalid_SelfHealAggresInterval');
#result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();

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

       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval")
       tdkTestObj.addParameter("ParamValue","1");
       tdkTestObj.addParameter("Type","unsignedint");
       expectedresult= "FAILURE";
       #Execute testcase on DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       Setresult = tdkTestObj.getResultDetails();
       if expectedresult in actualresult:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Set the Self Heal Aggressive Interval to a invalid value ";
          print "EXPECTED RESULT 2: Should not set the Self Heal Aggressive Interval to 1 min";
          print "ACTUAL RESULT 2: %s" %Setresult;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Set the Self Heal Aggressive Interval to a invalid value";
           print "EXPECTED RESULT 2: Should not set the Self Heal Aggressive Interval to 1 min";
           print "ACTUAL RESULT 2: %s" %Setresult;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";

           #revert in caseof invalid set
           tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
           tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SoftwareProcessManager.SelfHeal.AggressiveInterval")
           tdkTestObj.addParameter("ParamValue",defAggInt);
           tdkTestObj.addParameter("Type","unsignedint");
           expectedresult= "SUCCESS";
           #Execute testcase on DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           Setresult = tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Revert the Self Heal Aggressive Interval  to previous";
              print "EXPECTED RESULT 3: Should revert the Self Heal Aggressive Interval Interval to %s " %defAggInt;
              print "ACTUAL RESULT 3: %s" %Setresult;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Revert the Self Heal Aggressive Interval to previous";
               print "EXPECTED RESULT 3: Should revert the Self Heal Aggressive Interval to %s " %defAggInt;
               print "ACTUAL RESULT 3: %s" %Setresult;
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
