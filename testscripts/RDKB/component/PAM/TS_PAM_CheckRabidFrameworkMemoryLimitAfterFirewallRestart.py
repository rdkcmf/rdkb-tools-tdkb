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
  <name>TS_PAM_CheckRabidFrameworkMemoryLimitAfterFirewallRestart</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check  if Rabid Framework Memory limit  does not change after firewall-restart</synopsis>
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
    <test_case_id>TC_PAM_166</test_case_id>
    <test_objective>This test case is to check if on firewall restart memory limit does not change</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.MemoryLimit</input_parameters>
    <automation_approch>1.Load the module
2.Get  Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.MemoryLimit and store the value
3.Do a Firewall Restart
4.Do a get again on  Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.MemoryLimit and compare the value with previous value.
5.On Comparison if the value before and after Firewall restart are equal then the result will be
displayed as success else failure.
6.Unload the module</automation_approch>
    <expected_output>The memory limit should not change after firewall restart</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckRabidFrameworkMemoryLimitAfterFirewallRestart</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_PAM_CheckRabidFrameworkMemoryLimitAfterFirewallRestart');
pamObj.configureTestCase(ip,port,'TS_PAM_CheckRabidFrameworkMemoryLimitAfterFirewallRestart');

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper:
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.MemoryLimit")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    MemLimit = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Rabid Framework Memory Limit"
       print "EXPECTED RESULT 1: Should get the Rabid Framework Memory Limit";
       print "ACTUAL RESULT 1:Rabid Framework Memory Limit:",MemLimit;
       print "[TEST EXECUTION RESULT] : SUCCESS";

       tdkTestObj = sysObj.createTestStep('ExecuteCmd');
       cmd= "sysevent set firewall-restart";
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("command",cmd);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();

       if expectedresult in actualresult:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Do a firewall-restart";
           print "EXPECTED RESULT 2: Should do a firewall restart";
           print "ACTUAL RESULT 2:Firewall restarted successfully";
           print "[TEST EXECUTION RESULT] : SUCCESS";

           tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
           tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.MemoryLimit")
           expectedresult="SUCCESS";

           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           AfterFRMemLimit = tdkTestObj.getResultDetails().strip();

           print "Rabid Framework Memory Limit after Firewall-reset",AfterFRMemLimit;
           print "Rabid Framework Memory Limit before Firewall-reset",MemLimit;

           if expectedresult in actualresult and AfterFRMemLimit == MemLimit:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 3: Get the Rabid Framework Memory Limit after Firewall-reset";
               print "EXPECTED RESULT 3: Should get the Rabid Framework Memory Limit before and after firewall-restart equal";
               print "ACTUAL RESULT 3:Rabid Framework Memory Limit before and after Firewall-reset are equal";
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Get the Rabid Framework Memory Limit after Firewall-reset";
               print "EXPECTED RESULT 3: Should get the Rabid Framework Memory Limit before and after firewall-restart equal";
               print "ACTUAL RESULT 3:Rabid Framework Memory Limit before and after Firewall-reset are not equal";
               print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Do a firewall-restart";
           print "EXPECTED RESULT 2: Should do a firewall restart";
           print "ACTUAL RESULT 2:Firewall restart failed";
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Rabid Framework Memory Limit"
        print "EXPECTED RESULT 1: Should get the Rabid Framework Memory Limit";
        print "ACTUAL RESULT 1:Rabid Framework Memory Limit:",MemLimit;
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysObj.unloadModule("sysutil");
    pamObj.unloadModule("pam");
else:
    print "Failed to load sysutil/pam  module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
