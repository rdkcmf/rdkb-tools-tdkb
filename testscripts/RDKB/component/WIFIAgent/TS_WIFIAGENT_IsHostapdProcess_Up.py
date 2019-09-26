##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_IsHostapdProcess_Up</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the hostapd process for 2.4GHZ and 5GHZ are running or not</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_63</test_case_id>
    <test_objective>To check if the hostapd process for 2.4GHZ and 5GHZ are running or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifiagent and sysutil module
2. Using ExecuteCmd(), check if the hostapd process for 2.4GHZ and 5 GHZ are running
3. Unload modules</automation_approch>
    <except_output>The hostapd processes for both 2.4GHZ and 5GHZ should be up and running</except_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_IsHostapdProcess_Up</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags>
    <script_tag>BASIC</script_tag>
    <!--  -->
  </script_tags>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_IsHostapdProcess_Up');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_IsHostapdProcess_Up');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile HOSTAPD_PROCESS" %TDK_PATH;
    print command;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    hostapd_process = tdkTestObj.getResultDetails().strip();
    hostapd_process = hostapd_process.replace("\\n", "");
    if "Invalid Argument passed" not in hostapd_process:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the hostapd process names of device";
        print "EXPECTED RESULT 1: Should get the hostapd process names of device";
        print "ACTUAL RESULT 1: %s" %hostapd_process;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

	hostapd_process = hostapd_process.split(",");
	for item in hostapd_process:
	    tdkTestObj.addParameter("command", "ps -ef | grep %s | grep -v grep" %item);
	    #Execute the test case in STB
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();

            if expectedresult in actualresult and details:
		tdkTestObj.setResultStatus("SUCCESS");
		print "%s is running" %item
		print "[TEST EXECUTION RESULT] : SUCCESS"
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "%s is not running" %item
		print "[TEST EXECUTION RESULT] : FAILURE"
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the hostapd process names of device";
        print "EXPECTED RESULT 1: Should get the hostapd process names of device";
        print "ACTUAL RESULT 1: %s" %hostapd_process;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("wifiagent");
    sysObj.unloadModule("sysutil");
else:
        print "Failed to load module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
