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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_ethsw_stub_hal_SetPortAdminStatus_InvalidPort</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_SetPortAdminStatus</primitive_test_name>
  <primitive_test_version>7</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus()	by giving invalid port number.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_HAL_Ethsw_17</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus()	by giving invalid port number.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwSetPortAdminStatus, </api_or_interface_used>
    <input_parameters>PortID, adminstatus</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_SetPortAdminStatus().
3. Set the invalid value of port number for Admin port status
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <expected_output>The set operation of invalid port should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_SetPortAdminStatus_InvalidPort</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
#Library funtions
import tdklib;


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
#Reserve port #1 to connect Test Manager, don't change it's status.
testPortStatus = "CCSP_HAL_ETHSW_AdminDown";
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortAdminStatus_InvalidPort');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper() :
        obj.setLoadModuleStatus("SUCCESS");

        #Setting invalid values
	invalid_port = 0;
        tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortAdminStatus");
        tdkTestObj.addParameter("PortID",invalid_port);
        tdkTestObj.addParameter("adminstatus", testPortStatus);
        expectedresult = "FAILURE";
        print "Setting port status to %s for port %d" %(testPortStatus, invalid_port)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details:
            print "TEST STEP 1: Set port admin status to invalid port number";
            print "EXPECTED RESULT 1: The port status should not set with invalid port number";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

        else:
            tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 1: Set port admin status to invalid port number";
            print "EXPECTED RESULT 1: The port status should not set with invalid port number";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
        obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
