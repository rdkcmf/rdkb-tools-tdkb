##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TAD_SelfHeal_PandM</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To test if by self healing CcspPandM is restarted when killed</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>40</execution_time>
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
    <test_case_id>TC_TAD_18</test_case_id>
    <test_objective>To test if by self healing CcspPAM is restarted when killed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3,Rpi</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>ps -ef | grep -i CcspPandMSsp | grep -v grep
killall CcspPandMSsp;  ps -ef | grep CcspPandMSsp | grep -v grep</input_parameters>
    <automation_approch>1. Load sysutil and TAD modules
2. From script invoke ExecuteCmd to check if PAM process is up or not
3. If CcspPAM is up, kill it using ExecuteCmd
4. Wait for 30 minutes for it to restart
5. Using ExecuteCmd, check if PAM is up again 
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.</automation_approch>
    <except_output>CcspPAMSsp process should get restarted</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD
sysutil</test_stub_interface>
    <test_script>TS_TAD_SelfHeal_PandM</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from time import sleep;
from tdkbVariables import *;

MAX_RETRY = 6;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_SelfHeal_PandM');
sysObj.configureTestCase(ip,port,'TS_TAD_SelfHeal_PandM');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysObj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    # Check whether the process is running
    query="sh %s/tdk_platform_utility.sh checkProcess CcspPandMSsp" %TDK_PATH
    print "query:%s" %query
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    pid = tdkTestObj.getResultDetails().strip().replace("\\n", "")
    print "CcspPandMSsp PID: %s" %pid

    if expectedresult in actualresult and pid:
        print "TEST STEP 1:Check if CcspPandMSsp process is running"
        print "EXPECTED RESULT 1: CcspPandMSsp should be running";
        print "ACTUAL RESULT 1: CcspPandMSsp process is running"
        tdkTestObj.setResultStatus("SUCCESS");

        # Kill the process
        query="sh %s/tdk_platform_utility.sh killProcess CcspPandMSsp" %TDK_PATH
        print "query:%s" %query
        tdkTestObj.addParameter("command", query)
        tdkTestObj.executeTestCase("SUCCESS");
        actualresult = tdkTestObj.getResult();
        result = tdkTestObj.getResultDetails().strip()
        if expectedresult in actualresult:
            print "TEST STEP 1:Kill CcspPandMSsp process"
            print "EXPECTED RESULT 1: CcspPandMSsp should be killed";
            print "ACTUAL RESULT 1: CcspPandMSsp should be killed"
            tdkTestObj.setResultStatus("SUCCESS");

            #check whether the process is restarted automatically
            query="sh %s/tdk_platform_utility.sh checkProcess CcspPandMSsp" %TDK_PATH
            print "query:%s" %query
            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";

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
                print "TEST STEP 3:Check if CcspPandMSsp process is running"
                print "EXPECTED RESULT 3: CcspPandMSsp should be running";
                print "ACTUAL RESULT 3: CcspPandMSsp process is running"
                print "CcspPandMSsp PID: %s" %pid
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "TEST STEP 3:Check if CcspPandMSsp process is running"
                print "EXPECTED RESULT 3: CcspPandMSsp should be running";
                print "ACTUAL RESULT 3: CcspPandMSsp process is not running"
                tdkTestObj.setResultStatus("FAILURE");
                # Initiate reboot if process is not restarted automatically
                obj.initiateReboot();
			
        else:
            print "TEST STEP 1:Kill CcspPandMSsp process"
            print "EXPECTED RESULT 1: CcspPandMSsp should be killed";
            print "ACTUAL RESULT 1: CcspPandMSsp not killed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1:Check if CcspPandMSsp process is running"
        print "EXPECTED RESULT 1: CcspPandMSsp should be running";
        print "ACTUAL RESULT 1: CcspPandMSsp process is not running"
        tdkTestObj.setResultStatus("FAILURE");

    sysObj.unloadModule("sysutil");
    obj.unloadModule("tad");
else:
    print "FAILURE to load TAD module";
    obj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
