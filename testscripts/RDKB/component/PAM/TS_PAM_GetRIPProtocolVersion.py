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
  <version>4</version>
  <name>TS_PAM_GetRIPProtocolVersion</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>This test case will retrieve the current RIP protocol version. The Send and receive protocol version of RIP should be RIP2</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_PAM_173</test_case_id>
    <test_objective>This test case will retrieve the current RIP protocol version. The Send and receive protocol version of RIP should be RIP2</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state
2.TDK Agent should be in running state</pre_requisite>
    <api_or_interface_used>CcspBaseIf_getParameterValues</api_or_interface_used>
    <input_parameters>Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_SendVersion
Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_ReceiveVersion</input_parameters>
    <automation_approch>Retrieve the current send and receive RIP protocol version using the TR-181 parameters Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_SendVersion
Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_ReceiveVersion</automation_approch>
    <except_output>The retrieved RIP protocol version of both should be RIP2</except_output>
    <priority>High</priority>
    <test_stub_interface>pam_GetParameterValues</test_stub_interface>
    <test_script>TS_PAM_GetRIPProtocolVersion</test_script>
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
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_GetRIPProtocolVersion');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_SendVersion");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    SendVersion = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and "RIP2" in SendVersion:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the RIP Protocol Version";
            print "EXPECTED RESULT 1:RIP Protocol Version should be RIP2";
            print "ACTUAL RESULT 1: RIP Protocol Version: SendVersion:%s" %SendVersion;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            tdkTestObj = obj.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.Routing.RIP.InterfaceSetting.1.X_CISCO_COM_ReceiveVersion");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            ReceiveVersion = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and "RIP2" in ReceiveVersion:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Retrieve the RIP Protocol Version";
                print "EXPECTED RESULT 2:RIP Protocol Version should be RIP2";
                print "ACTUAL RESULT 2: RIP Protocol Version: ReceiveVersion:%s" %ReceiveVersion;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Retrieve the RIP Protocol Version";
                print "EXPECTED RESULT 2:RIP Protocol Version should be RIP2";
                print "ACTUAL RESULT 2: RIP Protocol Version: ReceiveVersion:%s" %ReceiveVersion;
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Retrieve the RIP Protocol Version";
        print "EXPECTED RESULT 1:RIP Protocol Version should be RIP2";
        print "ACTUAL RESULT 1: RIP Protocol Version: SendVersion:%s" %SendVersion;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");

else:
        print "Failed to load pam module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";




