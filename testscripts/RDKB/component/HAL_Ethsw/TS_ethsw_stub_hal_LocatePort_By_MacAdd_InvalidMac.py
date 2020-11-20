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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>9</version>
  <name>TS_ethsw_stub_hal_LocatePort_By_MacAdd_InvalidMac</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_LocatePort_By_MacAddress</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate HAL API CcspHalEthSwLocatePortByMacAddress() by passing an invalid mac address</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_5</test_case_id>
    <test_objective>To validate Ethsw HAL API CcspHalEthSwInit().</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalEthSwLocatePortByMacAddress</api_or_interface_used>
    <input_parameters>macID</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. From script invoke ethsw_stub_hal_LocatePort_By_MacAddress() with an invalid mac
3. Check if the api returns failure status
4. Unload  halethsw module.</automation_approch>
    <expected_output>API should return FAILURE.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_LocatePort_By_MacAdd_InvalidMac</test_script>
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
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_LocatePort_By_MacAddress_InvalidMac');
#macID of the device
testMacID = "00:aa:bb:cc:dd:ee"

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("ethsw_stub_hal_LocatePort_By_MacAddress");
        tdkTestObj.addParameter("macID", testMacID);
        expectedresult = "FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Invoke CcspHalEthSwLocatePortByMacAddress() by passing an invalid macaddress: ",testMacID;
            print "EXPECTED RESULT 1: Should not be able to retrieve the Port ID of invalid Mac Address";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
            print "Actual result is: %s" %details;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Invoke CcspHalEthSwLocatePortByMacAddress() by passing an invalid macaddress: ",testMacID;
            print "EXPECTED RESULT 1: Should not be able to retrieve the Port ID of invalid Mac Address";
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
            print "Actual result is: %s" %details;
        obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
