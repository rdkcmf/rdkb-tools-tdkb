##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_ethsw_stub_hal_SetPortCfg_GetPortStatus_AutoMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ethsw_stub_hal_Get_Port_Status</primitive_test_name>
  <!--  -->
  <primitive_test_version>4</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate Ethsw HAL API CcspHalEthSwSetPortCfg() and CcspHalEthSwGetPortStatus()  by setting duplex mode as Auto</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_29</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwSetPortCfg() and CcspHalEthSwGetPortStatus()  by setting duplex mode as Auto</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. A lan client should be connected</pre_requisite>
    <api_or_interface_used>CcspHalEthSwSetPortCfg
CcspHalEthSwGetPortStatus
</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. Get and save the current port cfg values using CcspHalEthSwGetPortCfg()
3. Using CcspHalEthSwSetPortCfg(), set duplex mode as Auto
4. Iinvoke CcspHalEthSwGetPortStatus() and check if  duplex mode is changed to Auto
5. Revert back to the initial port cfg values
6. Unload halethsw module.</automation_approch>
    <expected_output>CcspHalEthSwSetPortCfg() should change  duplex mode as Auto and this should reflect in subsequent CcspHalEthSwGetPortStatus() output</expected_output>
    <priority>High</priority>
    <test_stub_interface>halethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_SetPortCfg_GetPortStatus_AutoMode</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
port_ID = 2;
testDuplexMode = "CCSP_HAL_ETHSW_DUPLEX_Auto";
testLinkRateAuto = 10;
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_SetPortCfg_GetPortStatus_AutoMode');

#Get the result of connection with test component and DUT
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
        print "TEST STEP 1: Retrieve the Ethsw_Get_Port_Cfg"
        print "EXPECTED RESULT 1: Should retrieve the Ethsw_Get_Port_Cfg successfully"
        print "ACTUAL RESULT 1: DuplexMode = %s: Bitrate = %s" %(curDuplexMode, curLinkRate);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult;

        #Setting the values
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("ethsw_stub_hal_SetPortCfg");
        print "PortID : %s" %port_ID
        tdkTestObj.addParameter("PortID",port_ID);
        tdkTestObj.addParameter("linkrate", testLinkRateAuto);
        tdkTestObj.addParameter("mode", testDuplexMode);
        expectedresult = "SUCCESS";
        print "Setting link rate = %d and Duplex mode = %s" %(testLinkRateAuto, testDuplexMode);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details:
            print "TEST STEP 2: Set the Ethsw_Set_Port_Cfg"
            print "EXPECTED RESULT 2: Should set the Ethsw_Set_Port_Cfg successfully";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult;

            #Cross verify values
            #Script to load the configuration file of the component
            time.sleep(20);
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Status");
            tdkTestObj.addParameter("PortID",port_ID);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and details:
                linkRateAfterSet = details.split("/")[1];
                duplexModeAfterSet = details.split("/")[3];
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Retrieve the Ethsw_Get_Port_Status" ;
                print "EXPECTED RESULT 3: Should retrieve the Ethsw_Get_Port_Status successfully"
                print "ACTUAL RESULT 3: DuplexMode = %s" %(duplexModeAfterSet);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                if duplexModeAfterSet == testDuplexMode :
                    print "TEST STEP 4: Check if duplex mode is Auto in  Ethsw_Get_Port_Status() output"
                    print "EXPECTED RESULT 4: Duplex mode should be changed to Auto";
                    print "ACTUAL RESULT 4: Values are matched";
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
            	    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Check if duplex mode is Auto in  Ethsw_Get_Port_Status() output"
                    print "EXPECTED RESULT 4: Duplex mode should be changed to Auto";
                    print "ACTUAL RESULT 4: Values are not matched";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Retrieve the Ethsw_Get_Port_Status" ;
                print "EXPECTED RESULT 3: Should retrieve the Ethsw_Get_Port_Status successfully"
                print "ACTUAL RESULT 3: Failed to get the port status";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the Ethsw_Set_Port_Cfg"
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
            print "TEST STEP 5: Resetting the Ethsw_Set_Port_Cfg" ;
            print "EXPECTED RESULT 5: Should retrieve the Ethsw_Set_Port_Cfg successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] 5: %s" %actualresult;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 5: Resetting the Ethsw_Set_Port_Cfg" ;
            print "EXPECTED RESULT 5: Should retrieve the Ethsw_Set_Port_Cfg successfully" ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] 5: Failure";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Retrieve the Ethsw_Get_Port_Cfg" ;
        print "EXPECTED RESULT 1: Should retrieve the Ethsw_Get_Port_Cfg successfully";
        print "ACTUAL RESULT 1: Failed to retrieve the Ethsw_Get_Port_Cfg successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult;
    obj.unloadModule("halethsw");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
