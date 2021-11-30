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
  <name>TS_SANITY_CheckIpTablesError</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if any error messages logged in ipv4table_error and ipv6table error</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_SYSUTIL_59</test_case_id>
    <test_objective>To check if any error messages logged in ipv4table_error and ipv6table error</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the sysutil module
2.Check if  ipv4table_error and ipv6table error file exists.
3.The files are expected to be empty with no errors
4.Mark the script as success if file is blank else mark script as failure
5.Unload the module</automation_approch>
    <expected_output>ipv4table_error and ipv6table error are expected to be empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckIpTablesError</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckIpTablesError');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    #Check if file is present
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /tmp/.ipv4table_error ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    #Check if file is present
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /tmp/.ipv6table_error ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details1 = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP 1: Check for ipv4table_error and ipv6table_error file presence";
    print "EXPECTED RESULT 1: Files should be present";

    if details == "File exist" and details1 == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1 :  ipv4table_error and ipv6table_error file are present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        cmd1 = "cat /tmp/.ipv4table_error";
        cmd2= "cat /tmp/.ipv6table_error";

        tdkTestObj.addParameter("command",cmd1);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();
        details1 = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        tdkTestObj.addParameter("command",cmd2);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult2 = tdkTestObj.getResult();
        details2 = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "\nTEST STEP 2: Check if error logs are present in ipv4table_error and ipv6table_error";
        print "EXPECTED RESULT 2: Files are expected to be empty without error";

        if (expectedresult in ( actualresult1  and actualresult2))  and ((details1 and details2)  == "") :
           tdkTestObj.setResultStatus("SUCCESS");
           print "ACTUAL RESULT 2 : Files are empty no errors flooded";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
           tdkTestObj.setResultStatus("FAILURE");
           print "ACTUAL RESULT 2 : Files are non empty";
           print "ipv4table_error :",details1;
           print "ipv6table_error :",details2;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1 :  ipv4table_error and ipv6table_error file are not present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
