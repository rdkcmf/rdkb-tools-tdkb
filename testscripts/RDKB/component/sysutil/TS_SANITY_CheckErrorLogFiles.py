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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckErrorLogFiles</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check for error messages in log files once device is up</synopsis>
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
    <test_case_id>TC_SYSUTIL_30</test_case_id>
    <test_objective>Check for error messages in log files once device is up</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load module
2.Do a reboot
3.Once device comes up check if there are error messages in log files
4.Unload module</automation_approch>
    <expected_output>Error logs should not be present in log files</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckErrorLogFiles</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
import time;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckErrorLogFiles');
count = 0;

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    sysObj.initiateReboot();
    time.sleep(300);

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", "grep -lir lvl=ERROR /rdklogs/logs/ | tr \"\n\" \" \"");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace(" ",",");

    ErrorlogfileCount = details.count(",") + 1
    list = details.split(",")
    for i in list:
        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        command = "tail %s | grep -i lvl=ERROR" %i
        tdkTestObj.addParameter("command", command);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        errordetails = tdkTestObj.getResultDetails().strip().replace("\\n","");
        if expectedresult in actualresult and errordetails != "":
            print "Error logs in %s" %i
            print errordetails
            count =count + 1;
    if count == 0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check if log files have error"
        print "ACTUAL RESULT 1: Log files does not have error logs";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check if log files have error"
        print "ACTUAL RESULT 1: Log files has error logs ";
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysObj.unloadModule("sysutil");

else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

