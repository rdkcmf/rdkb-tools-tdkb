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
  <version>5</version>
  <name>TS_SANITY_CheckArpingLogs</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the string "ARPING_FROM_SOURCE:Success" is coming up in the SelfHeal.txt.0 logs instead of "ARPING_FROM_SOURCE:Failed no reply" logs.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SANITY_59</test_case_id>
    <test_objective>To check if the string "ARPING_FROM_SOURCE:Success" is coming up in the SelfHeal.txt.0 logs instead of "ARPING_FROM_SOURCE:Failed no reply" logs.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the modules
2. Check if SelfHeal.txt.0 is present under /rdklogs/logs
3. Check if the log line "ARPING_FROM_SOURCE" is present in SelfHeal.txt and verify if the string accompanying it is "Success" instead of "Failed no Reply".
4. Unload the module</automation_approch>
    <expected_output>The log file SelfHeal.txt.0 should be present under /rdklogs/logs and the log "ARPING_FROM_SOURCE:Success" should get populated instead of "ARPING_FROM_SOURCE:Failed no Reply".</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckArpingLogs</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
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
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckArpingLogs');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    #Check if SelfHeal.txt.0 file is present
    step = 1;
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/SelfHeal.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for SelfHeal.txt.0 log file presence" %step;
    print "EXPECTED RESULT %d:SelfHeal.txt.0 log file should be present" %step;

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d:SelfHeal.txt.0 log file is present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check for the ARPING_FROM_SOURCE string
        step = step + 1;
        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        cmd = "grep -ire \"ARPING_FROM_SOURCE\" /rdklogs/logs/SelfHeal.txt.0";
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";
        print "\nTEST STEP %d: Check for the presence of the string ARPING_FROM_SOURCE" %step;
        print "EXPECTED RESULT %d: ARPING_FROM_SOURCE string should be present" %step;
        stringfound = 0;

        #Giving 6 iterations of 60s as the logging of ARPING_FROM_SOURCE happens every 5 minutes
        for iteration in range(1,7):
            print "Waiting for the string to get populated in SelfHeal.txt.0....\nIteration : %d" %iteration;
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if expectedresult in actualresult and "ARPING_FROM_SOURCE" in details:
                stringfound = 1;
                break;
            else:
                sleep(60);
                continue;

        if stringfound == 1:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: ARPING_FROM_SOURCE string is found; Details : %s" %(step,details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the string does not contain "Failed no Reply"
            check_pattern = details.split("ARPING_FROM_SOURCE:")[1];
            print "ARPING_FROM_SOURCE:", check_pattern;
            step = step + 1;
            print "\nTEST STEP %d : Check if the pattern \"Failed no Reply\" is not present and \"Success\" is present" %step;
            print "EXPECTED RESULT %d : The pattern \"Failed no Reply\" should not be present and \"Success\" should be present" %step;

            if check_pattern == "Success" and check_pattern != "Failed no Reply":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: The pattern \"Failed no Reply\" is not present and \"Success\" is present" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: The pattern \"Failed no Reply\" is present and \"Success\" is not present" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: ARPING_FROM_SOURCE string is not found; Details : %s" %(step,details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: SelfHeal.txt.0 log file is not present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

