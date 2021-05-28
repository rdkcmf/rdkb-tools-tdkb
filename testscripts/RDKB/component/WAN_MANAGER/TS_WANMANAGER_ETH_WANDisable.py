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
  <version>3</version>
  <name>TS_WANMANAGER_ETH_WANDisable</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To disable the Ethernet WAN and check if device goes to reboot when set operation is performed</synopsis>
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
    <test_case_id>TC_WANMANAGER_43</test_case_id>
    <test_objective>This test case is to disable the Ethernet WAN and check if device goes to reboot when set operation is performed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the Ethernet WAN Disable status and is expected to be true
3.Disable the parameter and with successful set operation device is expected to go for a reboot
4.Revert the set parameter
5.Unload the module</automation_approch>
    <expected_output>When a Disable operation is done on Ethernet WAN parameter the device is expected go for reboot after successful set operation</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_ETH_WANDisable</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_ETH_WANDisable');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_ETH_WANDisable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and default == "true":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 : Check if WAN is enabled by default";
        print "EXPECTED RESULT 1: WAN should be enabled by default";
        print "ACTUAL RESULT 1:  WAN enable status is :",default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #save device's current state before it goes for reboot
        obj1.saveCurrentState();
        tdkTestObj1 = obj1.createTestStep('ExecuteCmdReboot');
        query="sleep 2 && dmcli eRT setv Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled bool false";
        print "query:%s" %query;
        tdkTestObj1.addParameter("command", query);
        #Execute the test case in DUT
        tdkTestObj1.executeTestCase(expectedresult);
        sleep(300);
        print "Set operation completed";
        #Restore previous state after reboot
        obj1.restorePreviousStateAfterReboot();
        sleep(60);
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 : Disable the WAN parameter";
            print "EXPECTED RESULT 2:Should disable the WAN parameter";
            print "ACTUAL RESULT 2: Disable operation successful";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #revert the value
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled")
            tdkTestObj.addParameter("ParamValue",default);
            tdkTestObj.addParameter("Type","bool");
            expectedresult= "SUCCESS";
            #Execute testcase on DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Setresult = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2 : Revert  the WAN parameter to previous";
                print "EXPECTED RESULT 2:Should revert the WAN parameter to previous";
                print "ACTUAL RESULT  2 : Revert operation successful";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2 : Revert  the WAN parameter to previous";
                print "EXPECTED RESULT 2:Should revert the WAN parameter to previous";
                print "ACTUAL RESULT  2 : Revert operation failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 : Disable the WAN parameter";
            print "EXPECTED RESULT 2:Should disable the WAN parameter";
            print "ACTUAL RESULT 2: Disable operation failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 : Check if WAN is enabled by default";
        print "EXPECTED RESULT 1: WAN should be enabled by default";
        print "ACTUAL RESULT 1:  WAN enable status is :",default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
