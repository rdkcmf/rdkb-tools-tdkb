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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckIPTablesRestore</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Perform a firewall restore operation and check if Error logs are seen in the files /tmp/.ipv4table_error and /tmp/.ipv6table_error</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_SANITY_60</test_case_id>
    <test_objective>Perform a firewall restore operation and check if Error logs are seen in the files /tmp/.ipv4table_error and /tmp/.ipv6table_error</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module.
2. Initiate a firewall restore
3. Check if the files .ipv4table_error and .ipv6table_error are present under /tmp.
4. Check if these files contain any error string.
5. Unload the module.</automation_approch>
    <expected_output>The IPtables Error files .ipv4table and .ipv6table should not contain any error logs after a firewall restore operation.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckIPTablesRestore</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
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
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckIPTablesRestore');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    #Restore firewall
    step = 1;
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "firewall";
    print "Command : ", cmd;
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Restore Firewall using the \"firewall\" command" %step;
    print "EXPECTED RESULT %d: Firewall Restore should be success" %step;

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Firewall Restore operation complete" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if /tmp/.ipv4table_error and /tmp/.ipv6table_error files are present and if they contain error logs
        sleep(10);
        tdkTestObj = sysObj.createTestStep('ExecuteCmd');

        for file in ["/tmp/.ipv4table_error", "/tmp/.ipv6table_error"]:
            step = step + 1;
            cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
            print "Command : ", cmd;
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d: Check for %s file presence" %(step, file);
            print "EXPECTED RESULT %d: %s file should be present" %(step, file);

            if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: %s file is present" %(step, file);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the file contains error logs
                step = step + 1;
                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                cmd = "cat " + file + " | grep -ire \"Error\"";
                print "Command : ", cmd;
                tdkTestObj.addParameter("command",cmd);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP %d: Check if Error is found in the file %s" %(step, file);
                print "EXPECTED RESULT %d: Error logs should not be present in the file %s" %(step, file);

                if expectedresult in actualresult and "Error" not in details :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Error logs are not found; Details : %s" %(step,details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Error logs are found; Details : %s" %(step,details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: %s file is not present" %(step, file);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Unable to perform the firewall restore operation" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

