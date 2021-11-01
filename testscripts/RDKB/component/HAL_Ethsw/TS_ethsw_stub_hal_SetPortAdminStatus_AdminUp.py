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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ethsw_stub_hal_SetPortAdminStatus</primitive_test_name>
  <!--  -->
  <primitive_test_version>7</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortAdminStatus() by giving status as CCSP_HAL_ETHSW_AdminUp</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
2. Get the number of Interfaces from Device.Ethernet.InterfaceNumberOfEntries and make sure that the Port number from the config file tdkbVariables.py is valid
3. From script invoke ethsw_stub_hal_SetPortAdminStatus().
4. Set the value of Admin port status as adminUp
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <expected_output>API should return SUCCESS and values should be set properly.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>LAN</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#Library funtions
import tdklib;
from tdkbVariables import *;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp');
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortAdminStatus_AdminUp');

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
        print "\nTEST STEP 1: Get the number of interface entries";
        print "EXPECTED RESULT 1: Should get the number of interface entries";
        print "ACTUAL RESULT 1: The number of interface entries : %s" %value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Number of interface entries minus 2 will be the number of ports
        NumOfPorts = int(value)-2;
        print "Number of ports is ", NumOfPorts

        #Get the Port to which the client is connected
        print "\nTEST STEP 2 : Fetch the the Port Number to which LAN client is connected";
        print "EXPECTED RESULT 2 : Should fetch the Port Number to which LAN client is connected successfully";

        #Check if the LAN_PORT_Number is retrieved from the config file
        if LAN_PORT_Number != "" :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2 : Port number is fetched successfully";
            print "Port : %s" %LAN_PORT_Number;
            port = int(LAN_PORT_Number);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the Port Number is valid
            if port <= NumOfPorts :
                print "The Port Number is valid";
                tdkTestObj.setResultStatus("SUCCESS");

                #Script to load the configuration file of the component
                testStep = 3;
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
                    print "\nTEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                    print "ACTUAL RESULT %d: Current port status is  %s" %(testStep, currPortStatus);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    testStep = testStep + 1;

                    #Setting the values
                    #Script to load the configuration file of the component
                    testPortStatus = "CCSP_HAL_ETHSW_AdminUp";
                    tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortAdminStatus");
                    tdkTestObj.addParameter("PortID",port);
                    tdkTestObj.addParameter("adminstatus", testPortStatus);
                    expectedresult = "SUCCESS";
                    print "Setting port status to %s for port %d" %(testPortStatus, port)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details:
                        print "\nTEST STEP %d: Set the Port status using EthSw_SetPortAdminStatus for port %d" %(testStep, port);
                        print "EXPECTED RESULT %d: Should set the EthSw_SetPortAdminStatus successfully" %testStep;
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
                            print "\nTEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                            print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                            print "ACTUAL RESULT %d: Now port status is  %s" %(testStep, portStatusAfterSet);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                            testStep = testStep + 1;

                            if testPortStatus in portStatusAfterSet:
                                print "\nTEST STEP %d: Cross verify value if those get set" %testStep;
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
                                    print "\nTEST STEP %d: Revert the PortAdminStatus for port %d" %(testStep, port);
                                    print "EXPECTED RESULT %d: Should revert the PortAdminStatus successfully" %testStep;
                                    print "ACTUAL RESULT %d: Value reverted successfully" %testStep;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "\nTEST STEP %d: Revert the PortAdminStatus for port %d" %(testStep, port);
                                    print "EXPECTED RESULT %d: Should revert the PortAdminStatus successfully" %testStep;
                                    print "ACTUAL RESULT %d: Value not reverted successfully" %testStep;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : Failure";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "\nTEST STEP %d: Cross verify value if those get set" %testStep;
                                print "EXPECTED RESULT %d: Values should be matched" %testStep;
                                print "ACTUAL RESULT %d: Values are not matched" %testStep;
                                print "[TEST EXECUTION RESULT] : Failure";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "\nTEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                            print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                            print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : Failure";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "\nTEST STEP %d: Retrieve the EthSw_SetPortAdminStatus for port %d" %(testStep, port);
                        print "EXPECTED RESULT %d: Should retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                        print "ACTUAL RESULT %d: Failed to retrieve the EthSw_SetPortAdminStatus successfully" %testStep;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "\nTEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(testStep, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                    print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Admin_Status successfully" %testStep;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
            else :
                print "The Port Number is not valid";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2 : Port number is not fetched successfully";
            print "Port : %s" %LAN_PORT_Number;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "\nTEST STEP 1: Get the number of interface entries";
        print "EXPECTED RESULT 1: Should get the number of interface entries";
        print "ACTUAL RESULT 1: The number of interface entries : %s" %value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("halethsw");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

