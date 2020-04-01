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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckWiFiHealthLogFile</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Validate if the file wifihealth.txt is created within 10 minutes of uptime after a factory reset.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_98</test_case_id>
    <test_objective>Validate if the file wifihealth.txt  is created within 10 minutes of uptime after a factory reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the Module
2. Factory reset the DUT
2. Wait for 10 min then check whether wifihealth.txt file is presnt or not
3. Unload the Module</automation_approch>
    <expected_output>wifihealth.txt file should be created within 10 minutes of uptime after a factory reset.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckWiFiHealthLogFile</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckWiFiHealthFile');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckWiFiHealthFile');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    obj.saveCurrentState();

    #Initiate Factory reset before checking the default value
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("paramType","string");
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
        print "Wait till box comes up - 10 Min"
        sleep(600);
        tdkTestObj = obj1.createTestStep('ExecuteCmd');
        cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Check for wifihealth log file presence";
                print "EXPECTED RESULT 2:wifihealth log file should be present";
                print "ACTUAL RESULT 2:wifihealth log file is present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Check for wifihealth log file presence";
                print "EXPECTED RESULT 2:wifihealth log file should be present";
                print "ACTUAL RESULT 2:wifihealth log file is not present";
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
    obj1.unloadModule("sysutil");
else:
    print "FAILURE to load wifiagent module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
