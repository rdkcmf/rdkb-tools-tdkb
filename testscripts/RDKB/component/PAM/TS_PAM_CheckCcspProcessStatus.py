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
  <name>TS_PAM_CheckCcspProcessStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To  check the status of all Ccsp process.</synopsis>
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
    <test_case_id>TC_PAM_236</test_case_id>
    <test_objective>To  check the status of all Ccsp  process</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>
dmcli %s getvalues Device.DeviceInfo.ProcessStatus.Process. | grep -A 10 $(pidof ccspprocess) | grep -A 1 State | cut -f3 -d ':' | tr '\r\n' ' '</input_parameters>
    <automation_approch>1.Load the module
2. get the process status of all the  ccsp process
3.Check if its status is either "Sleeping"  or "Running"
4.print the result status on comparison
5.Unload the module</automation_approch>
    <expected_output>The appropriate status should be received for all the ccsp process
</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckCcspProcessStatus</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#import statement
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckCcspProcessStatus');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    #Check the box type
    imagename = obj.getDeviceBoxType()
    pattern = "Emulator"
    if pattern in imagename:
	print "Box Type is Emulator"
	prefix = "simu"
    else:
	prefix = "eRT"

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    CcspProcess= "sh %s/tdk_utility.sh parseConfigFile CCSP_PROCESS" %TDK_PATH;
    print CcspProcess;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", CcspProcess);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    CcspProcessList = tdkTestObj.getResultDetails().strip();
    CcspProcessList = CcspProcessList.replace("\\n", "");
    if "Invalid Argument passed" not in CcspProcessList:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of ccsp processes ";
        print "EXPECTED RESULT 1: Should get the list of ccsp processes";
        print "ACTUAL RESULT 1: %s" %CcspProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
	CcspProcessList = CcspProcessList.split(",");
        for item in CcspProcessList:
             #getting process status Ccsp process
             tdkTestObj = obj.createTestStep('ExecuteCmd');
             tdkTestObj.addParameter("command", "dmcli %s getvalues Device.DeviceInfo.ProcessStatus.Process. | grep -A 10 $(pidof %s) | grep -A 1 State | cut -f3 -d ':' | tr '\r\n' ' '"%(prefix,item));
             expectedresult="SUCCESS";
             #Execute the test case in DUT
             tdkTestObj.executeTestCase("expectedresult");
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails().strip();
             if expectedresult in actualresult and ("Sleeping" in details or "Running" in details):
	         pid = details;
                 #Set the result status of execution
                 print "TEST STEP : Get status of %s"%item
                 print "EXPECTED RESULT : Should get status of %s process"%item
                 print "ACTUAL RESULT : status is %s" %details;
                 tdkTestObj.setResultStatus("SUCCESS");
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP : Get status of %s"%item
                 print "EXPECTED RESULT : Should get status of %s process"%item
                 print "ACTUAL RESULT : status is %s" %details;
                 print "[TEST EXECUTION RESULT] : FAILURE";
                 break;
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the list of ccsp processes ";
        print "EXPECTED RESULT 1: Should get the list of ccsp processes";
        print "ACTUAL RESULT 1: %s" %CcspProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");
else:
        print "Failed to load sysutil module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
