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
  <name>TS_Telemetry2_0_SelfHeal</name>
  <primitive_test_id/>
  <primitive_test_name>Telemetry_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if telemetry2_0 process gets restarted as a part of Self-Heal</synopsis>
  <groups_id/>
  <execution_time>40</execution_time>
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
    <test_case_id>TC_Telemetry2_0_51</test_case_id>
    <test_objective>This test case is to check if telemetry2_0 process gets restarted as a part of Self-Heal</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module
2. Execute the Telemetry pre-requisite and ensure that the process is running
3. Kill the telemetry2_0 process
4. Check if the process restarts itself as a part of Selfheal.
5. If the process restart by itself mark the script as success else its a failure
6. Execute the Telemetry post-requisite
7. Unload the Module
</automation_approch>
    <expected_output>When Telemetry2_0 process is killed explicitly the process should get restarted as a  part of self Heal</expected_output>
    <priority>High</priority>
    <test_stub_interface>Telemetry2_0</test_stub_interface>
    <test_script>TS_Telemetry2_0_SelfHeal</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbTelemetry2_0Utility import *;
from time import sleep;
MAX_RETRY = 6;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_SelfHeal');
tr181obj.configureTestCase(ip,port,'TS_Telemetry2_0_SelfHeal');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_set = tr181obj .createTestStep('TDKB_TR181Stub_Set');

    revertFlag = 0;
    initialStatus = "";
    initialVersion = "";
    initialURL = "";

    print "***************************************************************"
    print "TEST STEP 1: Initiating Pre-Requisite Check for Telemetry2_0";
    print "EXPECTED RESULT 1:Pre-Requisite Check for Telemetry2_0 Should be Success";

    preReq_Status,revertFlag,initialStatus,initialVersion,initialURL = telemetry2_0_Prerequisite(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_set);

    if preReq_Status == 1:
        print "ACTUAL RESULT 1: Pre-Requisite for Telemetry2_0 was successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "***************************************************************"

        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
        # Kill the process
        query="sh %s/tdk_platform_utility.sh killProcess telemetry2_0" %TDK_PATH
        print "query:%s" %query
        tdkTestObj_Sys_ExeCmd.addParameter("command", query)
        tdkTestObj_Sys_ExeCmd.executeTestCase("SUCCESS");
        actualresult = tdkTestObj_Sys_ExeCmd.getResult();
        result = tdkTestObj_Sys_ExeCmd.getResultDetails().strip()
        if expectedresult in actualresult:
            print "TEST STEP 2:Kill telemetry2_0 process"
            print "EXPECTED RESULT 2: telemetry2_0 should be killed";
            print "ACTUAL RESULT 2: telemetry2_0 should be killed"
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "[TEST EXECUTION RESULT] : SUCCESS";

            actualresult,pid = checkProcessRestarted(tdkTestObj_Sys_ExeCmd,"telemetry2_0");
            if expectedresult in actualresult and pid != "":
                print "TEST STEP 3:Check if telemetry2_0 process is running"
                print "EXPECTED RESULT 3: telemetry2_0 should be running";
                print "ACTUAL RESULT 3: telemetry2_0 process is running"
                print "telemetry2_0 PID: %s" %pid
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            else:
                print "TEST STEP 3:Check if telemetry2_0 process is running"
                print "EXPECTED RESULT 3: telemetry2_0 should be running";
                print "ACTUAL RESULT 3: telemetry2_0 process is not running"
                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                print "[TEST EXECUTION RESULT] : FAILURE";
                # Initiate reboot if process is not restarted automatically
                sysobj.initiateReboot();
        else:
            print "TEST STEP 2:Kill telemetry2_0 process"
            print "EXPECTED RESULT 2: telemetry2_0 should be killed";
            print "ACTUAL RESULT 2: telemetry2_0 not killed"
            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Pre-Requisite for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "***************************************************************"

    print "***************************************************************"
    print "TEST STEP 4: Initiating Post Process for Telemetry2_0";
    print "EXPECTED RESULT 4: Post Process should be success";

    postprocess_Status = telemetry2_0_PostProcess(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_set,revertFlag,initialStatus,initialVersion,initialURL);
    if postprocess_Status == 1:
        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 4 : Post Process for Telemetry2_0 was Successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 4: Post Process for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
