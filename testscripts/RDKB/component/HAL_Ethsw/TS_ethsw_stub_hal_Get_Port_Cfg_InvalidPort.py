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
  <name>TS_ethsw_stub_hal_Get_Port_Cfg_InvalidPort</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_Get_Port_Cfg</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate HAL API CcspHalEthSwGetPortCfg() with invalid port ID</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_12</test_case_id>
    <test_objective>To validate HAL API CcspHalEthSwGetPortCfg() with invalid port ID</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwGetPortCfg</api_or_interface_used>
    <input_parameters>PortID</input_parameters>
    <automation_approch>1. Load HAL_Ethsw module
2. Give invalid port number to CcspHalEthSwGetPortCfg
3. check if the api returns error or not
4. Unload module</automation_approch>
    <expected_output>The API should not return the port config with invalid port number</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Get_Port_Cfg_InvalidPort</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Get_Port_Cfg_InvalidPort');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    invalid_port = 0;
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_Port_Cfg");
    tdkTestObj.addParameter("PortID",invalid_port);
    expectedresult = "FAILURE";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Retrieve the Ethsw_Get_Port_Cfg for port";
        print "EXPECTED RESULT 1: Should not retrieve the Ethsw_Get_Port_Cfg with invalid port";
        print "ACTUAL RESULT 1: %s" %details;
	print "[TEST EXECUTION RESULT] :SUCCESS"
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
	print "TEST STEP 1: Retrieve the Ethsw_Get_Port_Cfg for port";
        print "EXPECTED RESULT 1: Should not retrieve the Ethsw_Get_Port_Cfg with invalid port";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] :FAILURE"
    obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
