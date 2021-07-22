##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_WANMANAGER_CheckQoSConfiguredAfterBootUp</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if QoS Queue is configured on Bootup.</synopsis>
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
    <test_case_id>TS_WANMANGER_112</test_case_id>
    <test_objective>This test case is to check if QoS Queue is configured on Bootup</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN Manager should be enabled</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module
2.Reboot the device
3.Once the device comes up after reboot check if Qos Configured message is logged in the VLANIFACEMGRLog.txt.0
4.Unload the module</automation_approch>
    <expected_output>On Bootup QoS Configuration should be successful</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckQoSConfiguredAfterBootUp</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
import time;
from WanManager_Utility import *;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_WANMANAGER_CheckQoSConfiguredAfterBootUp');
#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    print "***The Device is going for a reboot wait for 300 sec for the device to come up ****\n\n";

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    sysObj.initiateReboot();
    time.sleep(300);
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", "grep -rin \"QoS queue configured successfully\" %s " %VLANLOG);
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace(" ",",");

    if expectedresult in actualresult and "QoS,queue,configured,successfully" in details:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check if Qos Configured successfully"
        print "EXPECTED RESULT 1: Qos Configured message should be present in VLANIFACEMGRLog.txt.0";
        print "ACTUAL RESULT 1 : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check if Qos Configured successfully"
        print "EXPECTED RESULT 1: Qos Configured message should be present in VLANIFACEMGRLog.txt.0";
        print "ACTUAL RESULT 1: %s"%details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
