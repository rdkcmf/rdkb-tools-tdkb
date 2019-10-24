##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckMinidumpsAfterProcessCrash</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check dump file is created under minidump after process crash</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>7</execution_time>
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
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_28</test_case_id>
    <test_objective>To check dump file is created under minidump after process crash</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load sysutil module
2.Get the PID of CcspPandMSsp
3.Crash the process
4.Check if dump files are created after process crash
5.Unload sysutil module</automation_approch>
    <expected_output>Dump files should be generated after process crash</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckMinidumpsAfterProcessCrash</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
MAX_RETRY = 6;


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckMinidumpsAfterProcessCrash');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    #check whether the process is running or not
    query="sh %s/tdk_platform_utility.sh checkProcess CcspPandMSsp" %TDK_PATH
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and pid:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:CcspPandMSsp process should be running";
        print "ACTUAL RESULT 1: PID of CcspPandMSsp %s" %pid;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        cmd = "ls /minidumps | grep -i .dmp | wc -l";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details_beforecrash = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2:Get number of minidump files created before process crash";
            print "ACTUAL RESULT 2:Retrieved number of minidump files created before process crash";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "kill -11 %s" %pid;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:CcspPandMSsp should be crashed";
                print "ACTUAL RESULT 3: CcspPandMSsp process is crashed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj = obj.createTestStep('ExecuteCmd');
                cmd = "ls /minidumps | grep -i .dmp | wc -l";
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                dumpfiledetails = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                command = "ls /minidumps | grep -i .dmp";
                tdkTestObj.addParameter("command",command);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                dumpfile = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and int(dumpfiledetails) > int(details_beforecrash):
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4:minidump files should be created after process crash";
                    print "ACTUAL RESULT 4:minidump files are created after process crash:%s" %dumpfile;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    query="sh %s/tdk_platform_utility.sh checkProcess CcspPandMSsp" %TDK_PATH
                    print "query:%s" %query
                    tdkTestObj = obj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", query)
                    print "Check for every 10 secs whether the process is up"
                    retryCount = 0;
                    while retryCount < MAX_RETRY:
                        tdkTestObj.executeTestCase("SUCCESS");
                        actualresult = tdkTestObj.getResult();
                        pid = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                        if expectedresult in actualresult and pid:
                            break;
                        else:
                            sleep(10);
                            retryCount = retryCount + 1;

                    if not pid:
                        print "Retry Again: Check for every 5 mins whether the process is up"
                        retryCount = 0;
                        while retryCount < MAX_RETRY:
                            tdkTestObj.executeTestCase("SUCCESS");
                            actualresult = tdkTestObj.getResult();
                            pid = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                            if expectedresult in actualresult and pid:
                                break;
                            else:
                                sleep(300);
                                retryCount = retryCount + 1;

                    if expectedresult in actualresult and pid:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5:CcspPandMSsp process should be running";
                        print "ACTUAL RESULT 5: PID of CcspPandMSsp %s" %pid;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5:Check CcspPandMSsp process";
                        print "ACTUAL RESULT 5:CcspPandMSsp is not running";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4:minidump files should be created after process crash";
                    print "ACTUAL RESULT 4:minidump files are not created after process crash";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:CcspPandMSsp should be crashed";
                print "ACTUAL RESULT 3: CcspPandMSsp process is not crashed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:Get number of minidump files created before process crash";
            print "ACTUAL RESULT 2:Retrieved number of minidump files created before process crash";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Check CcspPandMSsp process";
        print "ACTUAL RESULT 1:CcspPandMSsp is not running";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed"

