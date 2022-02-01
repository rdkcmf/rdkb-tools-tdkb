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
  <version>2</version>
  <name>TS_PAM_BridgeModeCheckRabidProcess</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if cujo-agent process is stopped when device is in bridge mode.</synopsis>
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
    <test_case_id>TC_PAM_224</test_case_id>
    <test_objective>To check if cujo-agent process is stopped when device is in bridge mode</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
</input_parameters>
    <automation_approch>1.Load the module
2.Get the current lan mode and store the value
3.Change the lan mode to bridge-static
4.Check if cujo-agent process is running
5.if process is not running mark script as success else mark script as failure
6.Revert the set value
7.Unload the module
</automation_approch>
    <expected_output>cujo-agent process is not expected to run when in bridge mode</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_BridgeModeCheckRabidProcess</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>none</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_BridgeModeCheckRabidProcess');
pamObj.configureTestCase(ip,port,'TS_PAM_BridgeModeCheckRabidProcess');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");

    #Get the current Lan mode
    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanMode = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult and lanMode:
        tdkTestObj.setResultStatus("SUCCESS");
        #Set the result status of execution
        print "TEST STEP 1: Get the current lanMode"
        print "EXPECTED RESULT 1: Should get the current lanMode"
        print "ACTUAL RESULT 1: Current lanMode is %s" %lanMode;
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set the lanMode to bridge-static
        tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
        tdkTestObj.addParameter("ParamValue","bridge-static");
        tdkTestObj.addParameter("Type","string");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the lanMode to bridge-static";
            print "EXPECTED RESULT 2: Should set the lanMode to bridge-static";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS" ;
            print"***wait for the set operation to get reflected****";
            sleep(60);

            query="pidof cujo-agent";
            print "query:%s" %query
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n","");
            if expectedresult in  actualresult  and details == "":
                tdkTestObj.setResultStatus("SUCCESS");
                #Set the result status of execution
                print "TEST STEP 3: Check if cujo-agent process is up"
                print "EXPECTED RESULT 3: In Bridge mode cujo-agent process should not be running";
                print "ACTUAL RESULT 3: pid of cujo-agent  is %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                #Set the result status of execution
                print "TEST STEP 3: Check if cujo-agent process is up"
                print "EXPECTED RESULT 3:  In Bridge mode cujo-agent process should not be running";
                print "ACTUAL RESULT 3: pid of cujo-agent  is %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert the value of lanMode
            tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
            tdkTestObj.addParameter("ParamValue",lanMode);
            tdkTestObj.addParameter("Type","string");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4:Revert the value of lanMode";
                print "EXPECTED RESULT 4: Should revert the lanMode";
                print "ACTUAL RESULT 4: %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS" ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4:Revert the value of lanMode";
                print "EXPECTED RESULT 4: Should revert the lanMode";
                print "ACTUAL RESULT 4: %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE" ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the lanMode to bridge-static";
            print "EXPECTED RESULT 2: Should set the lanMode to bridge-static";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE" ;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        #Set the result status of execution
        print "TEST STEP 1: Get the current lanMode"
        print "EXPECTED RESULT 1: Should get the current lanMode"
        print "ACTUAL RESULT 1: Current lanMode is %s" %lanMode;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
    pamObj.unloadModule("pam");

else:
     print "Failed to load sysutil module";
     obj.setLoadModuleStatus("FAILURE");
     pamObj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
