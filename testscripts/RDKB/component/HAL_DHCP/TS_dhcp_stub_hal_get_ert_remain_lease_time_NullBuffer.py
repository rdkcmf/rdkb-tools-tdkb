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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_dhcp_stub_hal_get_ert_remain_lease_time_NullBuffer</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>dhcp_stub_hal_get_ert_remain_lease_time</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To verify NULL buffer functionality of dhcpv4c_get_ert_remain_lease_time()</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_HAL_DHCP_30</test_case_id>
    <test_objective>To verify NULL buffer functionality of dhcpv4c_get_ert_remain_lease_time()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dhcpv4c_get_ert_remain_lease_time()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load dhcphal module
2. invoke dhcpv4c_get_ert_remain_lease_time() by passing a NULL buffer
3. Check if dhcpv4c_get_ert_remain_lease_time() returns failure when NULL buffer is passed
4. Unload dhcphal module</automation_approch>
    <expected_output>Should not get ert remain lease time when NULL Buffer is passed</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAl_DHCP</test_stub_interface>
    <test_script>TS_dhcp_stub_hal_get_ert_remain_lease_time_NullBuffer</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("dhcp","RDKB");
obj.configureTestCase(ip,port,'TS_dhcp_stub_hal_get_ert_remain_lease_time_NullBuffer');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("dhcp_stub_hal_get_ert_remain_lease_time");
        tdkTestObj.addParameter("flag",1)
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the dhcp_stub_hal_get_ert_remain_lease_time with NULL Buffer";
            print "EXPECTED RESULT 1: Should not retrieve the dhcp_stub_hal_get_ert_remain_lease_time with NULL Buffer";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS" ;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "TEST STEP 1: Retrieve the dhcp_stub_hal_get_ert_remain_lease_time with NULL Buffer";
            print "EXPECTED RESULT 1: Should not retrieve the dhcp_stub_hal_get_ert_remain_lease_time with NULL Buffer";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        obj.unloadModule("dhcp");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

