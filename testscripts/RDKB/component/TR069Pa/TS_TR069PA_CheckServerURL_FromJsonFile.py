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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TR069PA_CheckServerURL_FromJsonFile</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the Management Server URL from Tr181 is the one configured in partners_default.json</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_TR069_20</test_case_id>
    <test_objective>This test case is to check if the Management Server URL from Tr181 param Device.ManagementServer.URL is the one configured in partners_default.json</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand ,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.ManagementServer.URL</input_parameters>
    <automation_approch>1.Load the module
2.Get the Server URL using Device.ManagementServer.URL
3.Check if the URL received via tr181 is present in parteners_default.json
4.Unload the module</automation_approch>
    <expected_output>The server URL received via TR-181 Device.ManagementServer.URL should be present in parteners_defaults.json</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_TR069PA_CheckServerURL_FromJsonFile</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_CheckServerURL_FromJsonFile');
sysobj.configureTestCase(ip,port,'TS_TR069PA_CheckServerURL_FromJsonFile');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult ="SUCCESS";
    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
    tdkTestObj.addParameter("ParamName","Device.ManagementServer.URL");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    serverURL  = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the TR069 Managment Server URL";
        print "EXPECTED RESULT 1: Should get the TR069 Managment Server URL";
        print "ACTUAL RESULT 1: serverURL fetched successfully";
        print "TEST EXECUTION RESULT : %s" %actualresult;

        tdkTestObj = sysobj.createTestStep("ExecuteCmd");
        cmd = "cat /nvram/partners_defaults.json |  grep -i \"%s\"" %serverURL;
        print cmd;
        tdkTestObj.addParameter("command", cmd);
        expectedresult="SUCCESS"
        tdkTestObj.executeTestCase(expectedresult);
        actualresult=tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().replace("\\n", "");
        if expectedresult in actualresult and details!= "" and serverURL in details: 
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Check if the Server URL is present in parteners_defaults.json file";
            print "EXPECTED RESULT 2: parteners_defaults.json file should have Managment Server URL entry";
            print "ACTUAL RESULT 2: Server URL is present in parteners_defaults.json file" ;
            print "TEST EXECUTION RESULT : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if the Server URL  is present in parteners_defaults.json file";
            print "EXPECTED RESULT 2: parteners_defaults.json file should have Managment Server URL entry";
            print "ACTUAL RESULT 2:Server URL is not present in parteners_defaults.json file";
            print "TEST EXECUTION RESULT : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the TR069 Managment Server URL";
        print "EXPECTED RESULT 1: Should get the TR069 Managment Server URL";
        print "ACTUAL RESULT 1: failed to fetch serverURL";
        print "TEST EXECUTION RESULT : %s" %actualresult;
    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
