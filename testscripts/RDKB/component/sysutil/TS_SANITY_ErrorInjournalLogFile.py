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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_ErrorInjournalLogFile</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To verify if relevant error log messages are present in Journal_log file</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_56</test_case_id>
    <test_objective>To verify if relevant error log messages are present in Journal_log file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Execute_Cmd</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module .
2.Check if  journal_logs.txt  file is present
3.Check for unexpected Error log messages from the file
4.Mark script as failure in case the Error log messages are present
5.Unload the module</automation_approch>
    <expected_output>Check if  no error log messages are present in  journal_logs.txt </expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_ErrorInjournalLogFile</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_ErrorInjournalLogFile');
#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    #Check whether the file is present or not
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/journal_logs.txt.0  ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check for existence of journal_logs.txt.0 ";
        print "EXPECTED RESULT 1: journal_logs.txt.0  file should be present";
        print "ACTUAL RESULT 1:journal_logs.txt.0  file is present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        logFile = "/rdklogs/logs/journal_logs.txt.0 ";
        logMsg = ["/etc/rdm/opensslVerifier.sh: line 148: [: : integer expression expected"];
        markerfound = 0;
        for list in logMsg:
            if markerfound == 1:
               break;
            else:
                query="cat %s | grep -i \"%s\"" %(logFile,list);
                print "query:%s" %query
                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                print "Marker Detail Found fromLog file is: %s "%details;
                if (len(details) == 0)  or list  not in details:
                   markerfound = 0;
                else:
                    markerfound = 1;
        if expectedresult in actualresult and markerfound == 1:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Check if Error Log Message present in journal_logs.txt.0 ";
           print "EXPECTED RESULT 2:  Error log Message should not be present";
           print "ACTUAL RESULT 2: ",details
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
        else:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Check if Error Message present in journal_logs.txt.0 ";
           print "EXPECTED RESULT 2:  Error log Message should not be present";
           print "ACTUAL RESULT 2: Log Message not found";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 1: Check for existence of journal_logs.txt.0 ";
         print "EXPECTED RESULT 1: journal_logs.txt.0  file should be present";
         print "ACTUAL RESULT 1:journal_logs.txt.0  file is not present";
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
else:
     print "Failed to load module";
     sysObj.setLoadModuleStatus("FAILURE");
