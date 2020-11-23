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
  <version>2</version>
  <name>TS_ETHWAN_SetInvalidOperationalMode</name>
  <primitive_test_id/>
  <primitive_test_name>EthWAN_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if setting invalid value to Device.X_RDKCENTRAL-COM_EthernetWAN.SelectedOperationalMode returns failure</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_ETHWAN_19</test_case_id>
    <test_objective>This test case is to check if setting invalid value to Device.X_RDKCENTRAL-COM_EthernetWAN.SelectedOperationalMode returns failure</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Braodband</test_setup>
    <pre_requisite>1. The broadband device should be in ETHWAN setup
2. The EthWAN mode should be enabled
3. TDK Agent must be up and running</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>Device.X_RDKCENTRAL-COM_EthernetWAN.SelectedOperationalMode</input_parameters>
    <automation_approch>1.Load the module
2.Set a invalid operational mode for Device.X_RDKCENTRAL-COM_EthernetWAN.SelectedOperationalMode
3.Mark the script as SUCCESS if the set fails else mark it as Failure
4.Unload the module</automation_approch>
    <expected_output>Setting a invalid operational mode to Device.X_RDKCENTRAL-COM_EthernetWAN.SelectedOperationalMode   should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>ETHWAN</test_stub_interface>
    <test_script>TS_ETHWAN_SetInvalidOperationalMode</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHWAN_SetInvalidOperationalMode');

loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
    tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_EthernetWAN.SelectedOperationalMode ");
    tdkTestObj.addParameter("ParamValue","InvalidValue");
    tdkTestObj.addParameter("Type","string");
    expectedresult="FAILURE";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Set the Operational mode to a Invalid value";
       print "EXPECTED RESULT 1: Should not set the Operational mode to a Invalid value";
       print "ACTUAL RESULT 1: %s" %details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Set the Operational mode to a Invalid value";
        print "EXPECTED RESULT 1: Should not set the Operational mode to a Invalid value";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load tr181 module";
     obj.setLoadModuleStatus("FAILURE");
