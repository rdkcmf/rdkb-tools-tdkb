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
  <version>30</version>
  <name>TS_ethsw_stub_hal_Get_Port_Admin_Status</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_Get_Port_Admin_Status</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate HAL API CcspHalEthSwGetPortAdminStatus()</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_2</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwGetPortAdminStatus()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwGetPortAdminStatus</api_or_interface_used>
    <input_parameters>PortID</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_Get_Port_Admin_Status().
3. Get the value of Admin port status
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Ethsw stub.</automation_approch>
    <except_output>Value should be from {"CCSP_HAL_ETHSW_AdminUp","CCSP_HAL_ETHSW_AdminDown"}.</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Get_Port_Admin_Status</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
#Library function
import tdklib;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","RDKB");
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Get_Port_Admin_Status');

obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_Get_Port_Admin_Status');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj.getLoadModuleResult();
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
        PortStatus_List = ["CCSP_HAL_ETHSW_AdminUp","CCSP_HAL_ETHSW_AdminDown"];

        while port <= NumOfPorts:
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Admin_Status");
            tdkTestObj.addParameter("PortID",port);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and details:
                portStatus = details;
                if portStatus in PortStatus_List:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(port+1, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %(port+1);
                    print "ACTUAL RESULT %d: Port status is %s" %(port+1, portStatus);
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    port = port + 1;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(port+1, port);
                    print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %(port+1);
                    print "ACTUAL RESULT %d: Port status is %s" %(port+1, portStatus);
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    break;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP %d: Retrieve the Ethsw_Get_Port_Admin_Status for port %d" %(port+1, port);
                print "EXPECTED RESULT %d: Should retrieve the Ethsw_Get_Port_Admin_Status successfully" %(port+1);
                print "ACTUAL RESULT %d: Failed to retrieve the Ethsw_Get_Port_Admin_Status" %(port+1);
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
