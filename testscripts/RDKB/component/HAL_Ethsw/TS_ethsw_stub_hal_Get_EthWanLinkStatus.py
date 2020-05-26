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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ethsw_stub_hal_Get_EthWanLinkStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ethsw_stub_hal_Get_EthWanLinkStatus</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get the Ethwan link status by invoking the HAL API, "GWP_GetEthWanLinkStatus".The return status should be success and result should be  "ETH_WAN_LINK_UP"</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_25</test_case_id>
    <test_objective>Get the Ethwan link status by invoking the HAL API, "GWP_GetEthWanLinkStatus".The return status should be success and result should be  "ETH_WAN_LINK_UP"</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Device should be in ethwan mode</pre_requisite>
    <api_or_interface_used>GWP_GetEthWanLinkStatus</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. Get the EthWan link status by invoking the HAL API GWP_GetEthWanLinkStatus
3. Check if the result is "ETH_WAN_LINK_UP" 
4. Unload halethsw module</automation_approch>
    <expected_output>Check if "GWP_GetEthWanLinkStatus" result is "ETH_WAN_LINK_UP"</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Get_EthWanLinkStatus</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Get_EthWanLinkStatus');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

#Prmitive test case which associated to this Script
tdkTestObj = obj.createTestStep('ethsw_stub_hal_Get_EthWanLinkStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_EthWanLinkStatus");
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();

    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and int(details) ==1:
        linkStatus = "ETH_WAN_LINK_UP"
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Retrieve the ethwan link status via HAL api";
        print "EXPECTED RESULT 1: Should retrieve the ethwan link status via HAL api as ETH_WAN_LINK_UP";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "Ethwan link status is %s" %linkStatus;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Retrieve the ethwan link status via HAL api";
        print "EXPECTED RESULT 1: Should retrieve the ethwan link status via HAL api as ETH_WAN_LINK_UP";
        print "[TEST EXECUTION RESULT] : FAILURE" ;
        print "Failure details: %s" %details

    obj.unloadModule("halethsw");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
