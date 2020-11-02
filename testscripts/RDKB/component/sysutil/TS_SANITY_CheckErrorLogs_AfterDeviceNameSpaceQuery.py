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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckErrorLogs_AfterDeviceNameSpaceQuery</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check if Failed to get parameter log Message is seen on querying Device Namespaces</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <test_case_id>TC_SYSUTIL_37</test_case_id>
    <test_objective>This test case is to Check if Failed to get parameter log Message is seen on querying Device Namespaces</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband ,RPI,EMU</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the module
2. Query the Namespace's
3. Check if  log message like "Failed to get parameter value of" is present in /rdklogs/logs/
4. Display the Log message if the above mentioned Log message is present and mark the script as failure
5. Unload the module
</automation_approch>
    <expected_output>On querying the Namespaces  "Failed to get parameter value of" should not be present in /rdklogs/logs/.</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckErrorLogs_AfterDeviceNameSpaceQuery</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckErrorLogs_AfterDeviceNameSpaceQuery');
obj1.configureTestCase(ip,port,'TS_SANITY_CheckErrorLogs_AfterDeviceNameSpaceQuery');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    Namespaces = "sh %s/tdk_utility.sh parseConfigFile NAMESPACES" %TDK_PATH;

    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", Namespaces);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    paramList = tdkTestObj.getResultDetails().strip();
    paramList = paramList.replace("\\n", "");
    paramList = paramList.split(",");
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of TR-181 parameters to be queried";
        print "EXPECTED RESULT 1: Should get the list of TR-181 parameters to be queried";
        print "ACTUAL RESULT 1: Got the list of TR-181 parameters to be queried ";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        print "TEST STEP 2: Query the below listed parameters";

        print paramList;

        logFile = "/rdklogs/logs/";
        logMsg = "Failed to get parameter value";
        getresult = [];
        logresult = []
        getFailure =0;
        patternFound =0;
        for item in paramList:
            print "Querying  %s" %item;

            tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.%s." %item);
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            if expectedresult not in actualresult:
               getFailure =1;
               getresult.append(item);

        if  getFailure == 0:
            tdkTestObj.setResultStatus("SUCCESS");
            print "EXPECTED RESULT 2: Should Query the listed parameters";
            print "ACTUAL RESULT 2: Get was successfull";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "EXPECTED RESULT 2: Should Query the listed parameters";
            print "ACTUAL RESULT 2: Failed to Query:",getresult;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        query="grep -rin \"%s\" \"%s\"" %(logMsg,logFile);
        print "query:%s" %query
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", query)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n","");
        print "Search Result :%s "%details;
        if (len(details) != 0)  and  logMsg in details:
           logresult.append(details);
           patternFound = 1;

        if patternFound ==0:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 3: Check if %s pattern seen in log file" %logMsg
           print "EXPECTED RESULT 3: Should Check if the pattern is present in log file";
           print "ACTUAL RESULT 3: No such pattern found";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Check if %s pattern seen in log file" %logMsg
            print "EXPECTED RESULT 3: Should Check if the pattern is present in log file";
            print "ACTUAL RESULT 3: " ,logresult;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of TR-181 parameters to be queried";
        print "EXPECTED RESULT 1: Should get the list of TR-181 parameters to be queried";
        print "ACTUAL RESULT 1: Failed to get the list of TR-181 parameters to be queried ";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
