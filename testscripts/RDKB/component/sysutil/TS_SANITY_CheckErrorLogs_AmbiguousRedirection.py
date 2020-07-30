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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckErrorLogs_AmbiguousRedirection</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if any  ambiguous redirect Log Messages are seen in Consolelog.txt.0</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_32</test_case_id>
    <test_objective>This test case is to check if any  ambiguous redirect Log Messages are seen in Consolelog.txt.0</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the module
2. Check if Consolelog.txt.0  file is present in /rdklogs/logs/
3. If file is present loop for 5 minutes and check if any  ambiguous redirect  log Messages are seen.
4. If found print the Failure message else print the Success message.
5. Unload the Module</automation_approch>
    <expected_output>ambiguous redirect  log Messages should not be seen in Consolelog.txt.0</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckErrorLogs_AmbiguousRedirection</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckErrorLogs_AmbiguousRedirection');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/Consolelog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check for Consolelog.txt.0 log file presence";
        print "EXPECTED RESULT 1:Consolelog.txt.0 log file should be present";
        print "ACTUAL RESULT 1:Consolelog.txt.0 log file is present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        logFile = "/rdklogs/logs/Consolelog.txt.0";
        logMsg = ["ambiguous redirect"];
        markerfound = 0;
        for list in logMsg:
            for i in range(1,6):
                if markerfound == 1:
                   break;
                else:
                    query="cat %s | grep -i \"%s\"" %(logFile,list);
                    print "query:%s" %query
                    tdkTestObj = obj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", query)
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                    print "Marker Detail Found fromLog file is: %s "%details;
                    if (len(details) == 0)  or list  not in details:
                       markerfound = 0;
                       sleep(60);
                    else:
                        markerfound = 1;
        if expectedresult in actualresult and markerfound == 1:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Check if ambiguous redirect Log Message present in Consolelog.txt.0";
           print "EXPECTED RESULT 2:  ambiguous redirect log Message should not be present";
           print "ACTUAL RESULT 2: ",details
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
        else:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Check if ambiguous redirect Log Message present in Consolelog.txt.0";
           print "EXPECTED RESULT 2:  ambiguous redirect log Message should not be present";
           print "ACTUAL RESULT 2: Log Message not found";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check for Consolelog.txt.0 log file presence";
        print "EXPECTED RESULT 1:Consolelog.txt.0 log file should be present";
        print "ACTUAL RESULT 1:Consolelog.txt.0 log file is not present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
