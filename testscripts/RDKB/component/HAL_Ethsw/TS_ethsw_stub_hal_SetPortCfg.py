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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>12</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ethsw_stub_hal_SetPortCfg</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ethsw_stub_hal_SetPortCfg</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortCfg().</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_HAL_Ethsw_8</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwSetPortCfg()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwSetPortCfg, CcspHalEthSwGetPortCfg</api_or_interface_used>
    <input_parameters>PortID, linkrate, mode</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. Get the number of Interfaces from Device.Ethernet.InterfaceNumberOfEntries and make sure that the Port number from the config file tdkbVariables.py is valid
3. From script invoke ethsw_stub_hal_SetPortCfg().
4. Set the values of port cfg
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <except_output>API should return SUCCESS and values should be set properly.</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_SetPortCfg</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>

'''

#Library functions
import tdklib;
from tdkbVariables import *;
import time;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortCfg');
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortCfg');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus.upper():
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
                tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Cfg");
                tdkTestObj.addParameter("PortID",port);
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details:
                    curLinkRate = details.split("/")[1];
                    curDuplexMode = details.split("/")[2];
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "\nTEST STEP 3: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port);
                    print "EXPECTED RESULT 3: Should retrieve the Ethsw_Get_Port_Cfg successfully";
                    print "ACTUAL RESULT 3: DuplexMode = %s: Bitrate = %s" %(curDuplexMode, curLinkRate);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;

                    #Setting the values
                    #Script to load the configuration file of the component
                    testDuplexMode = "CCSP_HAL_ETHSW_DUPLEX_Half";
                    testLinkRate = 10;
                    tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortCfg");
                    print "PortID : %s" %port
                    tdkTestObj.addParameter("PortID",port);
                    tdkTestObj.addParameter("linkrate", testLinkRate);
                    tdkTestObj.addParameter("mode", testDuplexMode);
                    expectedresult = "SUCCESS";
                    print "Setting link rate = %d and Duplex mode = %s" %(testLinkRate, testDuplexMode);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details:
                        print "\nTEST STEP 4: Set the Ethsw_Set_Port_Cfg for port %d" %(port);
                        print "EXPECTED RESULT 4: Should set the Ethsw_Set_Port_Cfg successfully";
                        print "ACTUAL RESULT 4: %s" %(details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;

                        #Cross verify values
                        #Script to load the configuration file of the component
                        time.sleep(20);
                        tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Cfg");
                        tdkTestObj.addParameter("PortID",port);
                        expectedresult = "SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and details:
                            linkRateAfterSet = details.split("/")[1];
                            duplexModeAfterSet = details.split("/")[2];
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "\nTEST STEP 5: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port);
                            print "EXPECTED RESULT 5: Should retrieve the Ethsw_Get_Port_Cfg successfully";
                            print "ACTUAL RESULT 5: DuplexMode = %s: Bitrate = %s" %(duplexModeAfterSet, linkRateAfterSet);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;

                            if int (linkRateAfterSet) == testLinkRate and duplexModeAfterSet in testDuplexMode:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "\nTEST STEP 6: Cross verify value if those get set";
                                print "EXPECTED RESULT 6: Values should be matched";
                                print "ACTUAL RESULT 6: Values are matched";
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Resetting the values back
                                #Script to load the configuration file of the component
                                tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortCfg");
                                tdkTestObj.addParameter("PortID",port);
                                tdkTestObj.addParameter("linkrate", int(curLinkRate));
                                tdkTestObj.addParameter("mode", curDuplexMode);
                                expectedresult = "SUCCESS";
                                print "Re-setting link rate = %s and Duplex mode = %s" %(curLinkRate, curDuplexMode);
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                if expectedresult in actualresult and details:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "\nTEST STEP 7: Resetting the Port_Cfg using Ethsw_Set_Port_Cfg for port %d" %port;
                                    print "EXPECTED RESULT 7: Should reset the Port_Cfg successfully";
                                    print "ACTUAL RESULT 7 : Port_Cfg reset successfully";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "\nTEST STEP 7: Resetting the Port_Cfg using Ethsw_Set_Port_Cfg for port %d" %(port);
                                    print "EXPECTED RESULT 7: Should reset the Port_Cfg successfully";
                                    print "ACTUAL RESULT 7 : Port_Cfg not reset successfully";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "\nTEST STEP 6: Cross verify value if those get set";
                                print "EXPECTED RESULT 6: Values should be matched";
                                print "ACTUAL RESULT 6: Values are not matched";
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port);
                            print "EXPECTED RESULT 5: Should retrieve the Ethsw_Get_Port_Cfg successfully" ;
                            print "ACTUAL RESULT 5: Failed to retrieve the Ethsw_Get_Port_Cfg successfully";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Retrieve the Ethsw_Set_Port_Cfg for port %d" %(port);
                        print "EXPECTED RESULT 4: Should retrieve the Ethsw_Set_Port_Cfg successfully";
                        print "ACTUAL RESULT 4: Failed to retrieve the Ethsw_Set_Port_Cfg successfully";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port);
                    print "EXPECTED RESULT 3: Should retrieve the Ethsw_Get_Port_Cfg successfully";
                    print "ACTUAL RESULT 3: Failed to retrieve the Ethsw_Get_Port_Cfg successfully";
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

