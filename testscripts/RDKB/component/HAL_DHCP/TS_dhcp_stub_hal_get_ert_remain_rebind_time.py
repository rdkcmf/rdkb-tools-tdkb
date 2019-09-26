#  ===========================================================================
#  Copyright 2016-2017 Intel Corporation

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#  ===========================================================================

'''
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>4</version>
  <name>TS_dhcp_stub_hal_get_ert_remain_rebind_time</name>
  <primitive_test_id/>
  <primitive_test_name>dhcp_stub_hal_get_ert_remain_rebind_time</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate HAL API dhcpv4c_get_ert_remain_rebind_time()</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_HAL_DHCP_24</test_case_id>
    <test_objective>To validate HAL API dhcpv4c_get_ert_remain_rebind_time()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dhcpv4c_get_ert_remain_rebind_time()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  dhcp module.
2. From script invoke dhcpv4c_get_ert_remain_rebind_time().
3. Get the value of rebind time
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_DHCP stub.</automation_approch>
    <except_output>Value should be greater than zero..</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_DHCP</test_stub_interface>
    <test_script>TS_dhcp_stub_hal_get_ert_remain_rebind_time</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_dhcp_stub_hal_get_ert_remain_rebind_time');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("dhcp_stub_hal_get_ert_remain_rebind_time");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if (expectedresult == actualresult and int(details)  > 0):
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the dhcp_stub_hal_get_ert_remain_rebind_time";
            print "EXPECTED RESULT 1: Should retrieve the dhcp_stub_hal_get_ert_remain_rebind_time successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "dhcp_ert_remain_rebind_time: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "TEST STEP 1: Retrieve the dhcp_stub_hal_get_ert_remain_rebind_time";
            print "EXPECTED RESULT 1: Should retrieve the dhcp_stub_hal_get_ert_remain_rebind_time successfully";
            print "Time value is invalid: %s" %details;
            print "[TEST EXECUTION RESULT] : Failure";

        obj.unloadModule("dhcp");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
