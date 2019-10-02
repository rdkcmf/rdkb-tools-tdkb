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
  <name>TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_SetPortAdminStatus</primitive_test_name>
  <primitive_test_version>7</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus() by giving status as CCSP_HAL_ETHSW_AdminUp</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_19</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus() by giving status as CCSP_HAL_ETHSW_AdminUp</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. One client should be connected to set the status</pre_requisite>
    <api_or_interface_used>CcspHalEthSwSetPortAdminStatus, CcspHalEthSwGetPortAdminStatus</api_or_interface_used>
    <input_parameters>PortID, adminstatus</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_SetPortAdminStatus().
3. Set the value of Admin port status as adminUp
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <expected_output>API should return SUCCESS and values should be set properly.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>LAN</remarks>
  </test_cases>
</xml>

'''
#LIbrary funtions
import tdklib;


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
#Reserve port #1 to connect Test Manager, don't change it's status.
startPort = 2
testPortStatus = "CCSP_HAL_ETHSW_AdminUp";
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp');

obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortAdminStatus');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Ethernet.InterfaceNumberOfEntries");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    value = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the number of interface entries";
        print "EXPECTED RESULT 1: Should get the number of interface entries";
        print "ACTUAL RESULT 1: The number of interface entries : %s" %value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#Number of interface entries minus 2 will be the number of ports
        NumOfPorts = int(value)-2;
        print "Number of ports is ", NumOfPorts

        testStep = 1;
        port = startPort;
        while port <= NumOfPorts:
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Admin_Status");
            tdkTestObj.addParameter("PortID",port);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and details:
                currPortStatus = details;
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");

                print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                print "ACTUAL RESULT %d: Current port status is  %s" %(testStep, currPortStatus);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                testStep = testStep + 1;
                #Setting the values
                #Script to load the configuration file of the component
                tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortAdminStatus");
                tdkTestObj.addParameter("PortID",port);
                tdkTestObj.addParameter("adminstatus", testPortStatus);
                expectedresult = "SUCCESS";
                print "Setting port status to %s for port %d" %(testPortStatus, port)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details:
                    print "TEST STEP %d: Retrieve the EthSw_SetPortAdminStatus for port %d" %(testStep, port);
                    print "EXPECTED RESULT %d: Should retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                    print "ACTUAL RESULT %d: %s" %(testStep, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    testStep = testStep + 1;

                    #Cross verify values
                    #Script to load the configuration file of the component
                    tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Admin_Status");
                    tdkTestObj.addParameter("PortID",port);
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult and details:
                        portStatusAfterSet = details;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                        print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                        print "ACTUAL RESULT %d: Now port status is  %s" %(testStep, portStatusAfterSet);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        testStep = testStep + 1;
                        if testPortStatus in portStatusAfterSet:
                            print "TEST STEP %d: Cross verify value if those get set" %testStep;
                            print "EXPECTED RESULT %d: Values should be matched" %testStep;
                            print "ACTUAL RESULT %d: Values are matched" %testStep;
                            testStep = testStep + 1;

                            #Resetting the values back
                            #Script to load the configuration file of the component
                            tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortAdminStatus");
                            tdkTestObj.addParameter("PortID",port);
                            tdkTestObj.addParameter("adminstatus", currPortStatus);
                            expectedresult = "SUCCESS";
                            print "Re-setting port status = %s" %currPortStatus;
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            if expectedresult in actualresult and details:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP %d: Retrieve the EthSw_SetPortAdminStatus for port %d" %(testStep, port);
                                print "EXPECTED RESULT %d: Should retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                testStep = testStep + 1;
                                port = port + 1;
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP %d: Retrieve the EthSw_SetPortAdminStatus for port %d" %(testStep, port);
                                print "EXPECTED RESULT %d: Should retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : Failure";
                                break;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP %d: Cross verify value if those get set" %testStep;
                            print "EXPECTED RESULT %d: Values should be matched" %testStep;
                            print "ACTUAL RESULT %d: Values are not matched" %testStep;
                            print "[TEST EXECUTION RESULT] : Failure";
                            break;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                        print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                        print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : Failure";
                        break;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP %d: Retrieve the EthSw_SetPortAdminStatus for port %d" %(testStep, port);
                    print "EXPECTED RESULT %d: Should retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                    print "ACTUAL RESULT %d: Failed to retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    break;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                break;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of interface entries";
        print "EXPECTED RESULT 1: Should get the number of interface entries";
        print "ACTUAL RESULT 1: The number of interface entries : %s" %value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("halethsw");
    obj1.unloadModule("tdkbtr181");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
