##########################################################################
# Copyright 2016-2017 Intel Corporation
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
  <version>7</version>
  <name>TS_ethsw_stub_hal_Set_Port_Admin_Status_True_Disabled_Port</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_SetPortAdminStatus</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus() if it return FAILURE in case of setting port status to up for disabled/disconnected port.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_HAL_Ethsw_9</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus() if it return FAILURE in case of setting port status to up for disabled/disconnected port.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwSetPortAdminStatus, CcspHalEthSwGetPortAdminStatus</api_or_interface_used>
    <input_parameters>PortID, adminstatus</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_SetPortAdminStatus().
3. Set the value of Admin port status
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <except_output>API should return FAILURE.</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Set_Port_Admin_Status_True_Disabled_Port</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
#LIbrary funtions
import tdklib;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
#No CPE should be connected to testPort
testPort = 4;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Set_Port_Admin_Status_True_Disabled_Port');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Admin_Status");
        tdkTestObj.addParameter("PortID",testPort);
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "actualresult : %s" %actualresult
        if expectedresult in actualresult and details:
            currPortStatus = details;
            print "TEST STEP 1: Retrieve the current Ethsw_Get_Port_Admin_Status";
            print "EXPECTED RESULT 1: Should retrieve the Ethsw_Get_Port_Admin_Status successfully";
            print "ACTUAL RESULT 1: Current port status is %s" %currPortStatus;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;

            #if port status is disconnected then validate the test
            if currPortStatus == "CCSP_HAL_ETHSW_AdminDown":
                tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortAdminStatus");
                tdkTestObj.addParameter("PortID",testPort);
                tdkTestObj.addParameter("adminstatus","CCSP_HAL_ETHSW_AdminUp");
                expectedresult = "FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Admin_Status");
                tdkTestObj.addParameter("PortID",testPort);
                tdkTestObj.executeTestCase("SUCCESS");
                portStatusAfterSet = tdkTestObj.getResultDetails();

                if expectedresult in actualresult or portStatusAfterSet == currPortStatus:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Retrieve the EthSw_SetPortAdminStatus of a port - %d" %testPort;
                    print "EXPECTED RESULT 2: As the port is down, EthSw_SetPortAdminStatus should be failed";
                    print "ACTUAL RESULT 2: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Retrieve the EthSw_SetPortAdminStatus of a down port - %d" %testPort;
                    print "EXPECTED RESULT 2:As the port is down, EthSw_SetPortAdminStatus should be failed";
                    print "ACTUAL RESULT 2: %s" %details;
                    print "[TEST EXECUTION RESULT] : Failure";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "It seems port is connected to CPE, so test cannot be validated"
                print "Please disconnect the port %d before validating the test" %testPort;
        else:
            print "TEST STEP 1: Retrieve the current Ethsw_Get_Port_Admin_Status";
            print "EXPECTED RESULT 1: Should retrieve the Ethsw_Get_Port_Admin_Status successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;

        obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
