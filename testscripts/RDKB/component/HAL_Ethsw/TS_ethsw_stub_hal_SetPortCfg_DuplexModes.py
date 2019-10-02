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
  <name>TS_ethsw_stub_hal_SetPortCfg_DuplexModes</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_SetPortCfg</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortCfg() by setting all possible duplex modes</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_23</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwSetPortCfg() by setting all possible duplex modes</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. One client should be connected to the device</pre_requisite>
    <api_or_interface_used>CcspHalEthSwSetPortCfg</api_or_interface_used>
    <input_parameters>PortID, linkrate, mode</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_SetPortCfg().
3. Set the all possible values of duplex mode for port cfg
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <expected_output>The set operation of all duplex modes should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_SetPortCfg_DuplexModes</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>LAN</remarks>
  </test_cases>
</xml>

'''
#Library functions
import tdklib;
import time;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
port_ID = 2;
testDuplexModeList = ["CCSP_HAL_ETHSW_DUPLEX_Half", "CCSP_HAL_ETHSW_DUPLEX_Full"];
testLinkRate = 10;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortCfg_DuplexModes');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
            obj.setLoadModuleStatus("SUCCESS");
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Cfg");
            tdkTestObj.addParameter("PortID",port_ID);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and details:
                curLinkRate = details.split("/")[1];
                curDuplexMode = details.split("/")[2];
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Retrieve the Ethsw_Get_Port_Cfg for port 1" 
                print "EXPECTED RESULT 1: Should retrieve the Ethsw_Get_Port_Cfg successfully"
                print "ACTUAL RESULT 1: DuplexMode = %s: Bitrate = %s" %(curDuplexMode, curLinkRate);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;

                #Setting the values
                #Script to load the configuration file of the component
		for mode in testDuplexModeList:
                    tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortCfg");
                    print "PortID : %s" %port_ID
                    tdkTestObj.addParameter("PortID",port_ID);
                    tdkTestObj.addParameter("linkrate", testLinkRate);
                    tdkTestObj.addParameter("mode", mode);
                    expectedresult = "SUCCESS";
                    print "Setting link rate = %d and Duplex mode = %s" %(testLinkRate, mode);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult and details:
                        print "TEST STEP 2: Set the Ethsw_Set_Port_Cfg for port 1"
                        print "EXPECTED RESULT 2: Should set the Ethsw_Set_Port_Cfg successfully";
                        print "ACTUAL RESULT 2: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;

                        #Cross verify values
		        #Script to load the configuration file of the component
		        time.sleep(20);
                        tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Cfg");
		        tdkTestObj.addParameter("PortID",port_ID);
		        tdkTestObj.executeTestCase(expectedresult);
		        actualresult = tdkTestObj.getResult();
		        details = tdkTestObj.getResultDetails();
		        if expectedresult in actualresult and details:
                            linkRateAfterSet = details.split("/")[1];
		    	    duplexModeAfterSet = details.split("/")[2];
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 3: Retrieve the Ethsw_Get_Port_Cfg for port 1" ;
                            print "EXPECTED RESULT 3: Should retrieve the Ethsw_Get_Port_Cfg successfully"
                            print "ACTUAL RESULT 3: DuplexMode = %s: Bitrate = %s" %(duplexModeAfterSet, linkRateAfterSet);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                            if duplexModeAfterSet == mode:
                                print "TEST STEP 4: Cross verify value if those get set" 
                                print "EXPECTED RESULT 4: Values should be matched";
                                print "ACTUAL RESULT 4: Values are matched";
			    else:
				tdkTestObj.setResultStatus("FAILURE");
				print "TEST STEP 4: Cross verify value if those get set"
                                print "EXPECTED RESULT 4: Values should be matched";
                                print "ACTUAL RESULT 4: Values are not matched";
			else:
			    tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 3: Retrieve the Ethsw_Get_Port_Cfg for port 1" ;
                            print "EXPECTED RESULT 3: Should retrieve the Ethsw_Get_Port_Cfg successfully"
                            print "ACTUAL RESULT 3: Faied to get the port cfg";
                    else:
			tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 2: Set the Ethsw_Set_Port_Cfg for port 1"
                        print "EXPECTED RESULT 2: Should set the Ethsw_Set_Port_Cfg successfully";
                        print "ACTUAL RESULT 2: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
		
                #Resetting the values back
                #Script to load the configuration file of the component
                tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortCfg");
                tdkTestObj.addParameter("PortID",port_ID);
                tdkTestObj.addParameter("linkrate", int(curLinkRate));
                tdkTestObj.addParameter("mode", curDuplexMode);
                expectedresult = "SUCCESS";
                print "Re-setting link rate = %s and Duplex mode = %s" %(curLinkRate, curDuplexMode);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Resetting the Ethsw_Set_Port_Cfg for port 1" ;
                    print "EXPECTED RESULT : Should retrieve the Ethsw_Set_Port_Cfg successfully";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP : Resetting the Ethsw_Set_Port_Cfg for port 1" ;
                    print "EXPECTED RESULT : Should retrieve the Ethsw_Set_Port_Cfg successfully" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : Failure";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Retrieve the Ethsw_Get_Port_Cfg for port1 " ;
                print "EXPECTED RESULT 2: Should retrieve the Ethsw_Get_Port_Cfg successfully";
                print "ACTUAL RESULT 2: Failed to retrieve the Ethsw_Get_Port_Cfg successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
    	    obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
