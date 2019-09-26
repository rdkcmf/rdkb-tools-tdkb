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
2. From script invoke ethsw_stub_hal_SetPortCfg().
3. Set the values of port cfg
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
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
import time;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
MAX_PORT = 4;
testDuplexMode = "CCSP_HAL_ETHSW_DUPLEX_Half";
testLinkRate = 10;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortCfg');
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortCfg');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

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

        port = 1;
        while port <= NumOfPorts:
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
                print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port, port);
                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %port;
                print "ACTUAL RESULT %d: DuplexMode = %s: Bitrate = %s" %(port, curDuplexMode, curLinkRate);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;

                #Setting the values
                #Script to load the configuration file of the component
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
                    print "TEST STEP %d: Set the Ethsw_Set_Port_Cfg for port %d" %(port+1, port);
                    print "EXPECTED RESULT %d: Should set the Ethsw_Set_Port_Cfg successfully" %(port+1);
                    print "ACTUAL RESULT %d: %s" %(port+1, details);
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
                        print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port+2, port);
                        print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %port;
                        print "ACTUAL RESULT %d: DuplexMode = %s: Bitrate = %s" %(port+2, duplexModeAfterSet, linkRateAfterSet);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        if int (linkRateAfterSet) == testLinkRate and duplexModeAfterSet in testDuplexMode:
                            print "TEST STEP %d: Cross verify value if those get set" %(port+3);
                            print "EXPECTED RESULT %d: Values should be matched" %(port+3);
                            print "ACTUAL RESULT %d: Values are matched" %(port+3);

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
                                print "TEST STEP %d: Resetting the Ethsw_Set_Port_Cfg for port %d" %(port+4, port);
                                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Set_Port_Cfg successfully" %(port+4);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                port = port + 1;
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP %d: Resetting the Ethsw_Set_Port_Cfg for port %d" %(port+4, port);
                                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Set_Port_Cfg successfully" %(port+4);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : Failure";
                                break;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP %d: Cross verify value if those get set" %(port+3);
                            print "EXPECTED RESULT %d: Values should be matched" %(port+3);
                            print "ACTUAL RESULT %d: Values are not matched" %(port+3);
                            print "[TEST EXECUTION RESULT] : Failure";
                            break;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port+2, port);
                        print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %(port+2);
                        print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Cfg successfully" %(port+2);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : Failure";
                        break;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP %d: Retrieve the Ethsw_Set_Port_Cfg for port %d" %(port+1, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Set_Port_Cfg successfully" %(port+1);
                    print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Set_Port_Cfg successfully" %(port+1);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    break;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port, port);
                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %port;
                print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Cfg successfully" %port;
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
