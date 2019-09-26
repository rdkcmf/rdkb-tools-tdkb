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
  <version>26</version>
  <name>TS_ethsw_stub_hal_Get_Port_Cfg</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_Get_Port_Cfg</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate HAL API CcspHalEthSwGetPortCfg()</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_HAL_Ethsw_3</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwGetPortCfg()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwGetPortCfg</api_or_interface_used>
    <input_parameters>PortID</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_Get_Port_Cfg().
3. Get the value of Duplex mode and Bit rate.
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <except_output>Values should be from:
1. Bit rate - {"10","100","1000","10000"}
2. Duplex mode - {"CCSP_HAL_ETHSW_DUPLEX_Auto","CCSP_HAL_ETHSW_DUPLEX_Half","CCSP_HAL_ETHSW_DUPLEX_Full"}</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Get_Port_Cfg</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Get_Port_Cfg');

obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_Get_Port_Cfg');

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
        DuplexMode_List = ["CCSP_HAL_ETHSW_DUPLEX_Auto","CCSP_HAL_ETHSW_DUPLEX_Half","CCSP_HAL_ETHSW_DUPLEX_Full"];
        Bitrate_List = ["0","1","10","100","1000","10000"];

        while port <= NumOfPorts:
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Cfg");
            tdkTestObj.addParameter("PortID",port);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and details:
                bitRate = details.split("/")[1];
                duplexMode = details.split("/")[2];
                if duplexMode in DuplexMode_List and bitRate in Bitrate_List:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port+1, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %(port+1);
                    print "ACTUAL RESULT %d: DuplexMode = %s: Bitrate = %s" %(port+1, duplexMode, bitRate);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    port = port + 1;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port+1, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %(port+1);
                    print "ACTUAL RESULT %d: DuplexMode = %s: Bitrate = %s" %(port+1, duplexMode, bitRate);
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    break;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Cfg for port %d" %(port+1, port);
                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Cfg successfully" %(port+1);
                print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Cfg" %(port+1);
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
