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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>6</version>
  <name>TS_PAM_DistinctPID</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Tests if Process table has no two entries with same pid values</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>RPI</box_type>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_102</test_case_id>
    <test_objective>To  check if no two process has same PID</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
ExecuteCmd

Input:
ParamName -
dmcli %s getvalues Device.DeviceInfo.ProcessStatus.Process. | grep -A 1 PID | head -n 100 | tail -3 | cut -f3 -d ':' | head -n 1 | tr '\r\n' ' '</input_parameters>
    <automation_approch>1.Function which needs to be tested will be configured in Test Manager GUI.
2.Python Script will be generated by Test Manager with provided arguments in configure page.
3.TM will load thesysutil library via Test agent
4.From python script, invoke ExecuteCmd() stub function to get the PID.                                                                                             5.Check if that PID has a duplicate using ExecuteCmd().
5.Responses from the sysutil stub function will be logged in Agent Console log.
6.pam stub will validate the actual result with the expected result and send the result status to Test Manager.
7.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_PAM_DistinctPID</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
#import statement
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_DistinctPID');

#Get the result of connection with test component and STB
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

    #select a random PID from process table
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", "dmcli %s getvalues Device.DeviceInfo.ProcessStatus.Process. | grep -A 1 PID | head -n 100 | tail -3 | cut -f3 -d ':' | head -n 1 | tr '\r\n' ' '" %prefix);
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details:
	pid = details;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get a random PID";
        print "EXPECTED RESULT 1: Should get a random PID";
        print "ACTUAL RESULT 1: ProcessId is %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#check for the no: of occurences of that pid in process table
	tdkTestObj = obj.createTestStep('ExecuteCmd');
	tdkTestObj.addParameter("command", "dmcli %s getvalues Device.DeviceInfo.ProcessStatus.Process. | grep -A 1 PID | cut -f3 -d ':' | grep -w %s | wc -l | tr '\r\n' ' '" %(prefix, pid));
	expectedresult="SUCCESS";

        #Execute the test case in STB
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip();

        if expectedresult in actualresult and details == "1":
            pid = details;
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get no: of occurence of PID";
            print "EXPECTED RESULT 2: Should get no: of occurence of PID as one";
            print "ACTUAL RESULT 2: no: of occurence is %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get no: of occurence of PID";
            print "EXPECTED RESULT 2: Should get no: of occurence of PID as one";
            print "ACTUAL RESULT 2: no: of occurence is %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get a random PID";
        print "EXPECTED RESULT 1: Should get a random PID";
        print "ACTUAL RESULT 1: ProcessId is %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");

else:
        print "Failed to load sysutil module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
