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
  <name>TS_SANITY_CheckNvramUsage</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the bbhm_cur_cfg.xml is absent under nvram and present under tmp and bbhm_bak_cfg.xml is present under nvram.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_44</test_case_id>
    <test_objective>To check if the bbhm_cur_cfg.xml is absent under nvram and present under tmp and bbhm_bak_cfg.xml is present under nvram.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>command : command to check whether the required file exists or not</input_parameters>
    <automation_approch>1. Load the sysutil module
2. Check if bbhm_cur_cfg.xml is absent and bbhm_bak_cfg.xml is present under nvram
3. Check if bhm_cur_cfg.xml is present under tmp
4. Unload the module</automation_approch>
    <expected_output>bbhm_cur_cfg.xml should be absent under nvram and present under tmp and bbhm_bak_cfg.xml should be present under nvram.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckNvramUsage</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import tdkutility;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckNvramUsage');

#Get the result of connection with test component and DUT
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #In nvram check if the file bbhm_cur_cfg.xml is not present
    print "\nTEST STEP 1: Check if bbhm_cur_cfg.xml is present or not under nvram";
    print "EXPECTED RESULT 1: bbhm_cur_cfg.xml should not be present under nvram";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    cmd = "[ -f /nvram/bbhm_cur_cfg.xml ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if details == "File does not exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1 : bbhm_cur_cfg.xml is not present under nvram";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check whether bbhm_bak_cfg.xml is present or not under nvram
        print "TEST STEP 2: Check if bbhm_bak_cfg.xml is present or not under nvram";
        print "EXPECTED RESULT 2: bbhm_bak_cfg.xml should be prsent under nvram";
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd = "[ -f /nvram/bbhm_bak_cfg.xml ] && echo \"File exist\" || echo \"File does not exist\"";
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        if details == "File exist":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: bbhm_bak_cfg.xml is present under nvram";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check whether bbhm_cur_cfg.xml is present or not under tmp
            print "TEST STEP 3: Check if bbhm_cur_cfg.xml is present or not under tmp";
            print "EXPECTED RESULT 3: bbhm_cur_cfg.xml should be present under tmp";
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "[ -f /tmp/bbhm_cur_cfg.xml ] && echo \"File exist\" || echo \"File does not exist\"";
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: bbhm_cur_cfg.xml is present under tmp";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: bbhm_cur_cfg.xml is not present under tmp";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: bbhm_bak_cfg.xml is not present under nvram";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1 : bbhm_cur_cfg.xml is present under nvram";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");

