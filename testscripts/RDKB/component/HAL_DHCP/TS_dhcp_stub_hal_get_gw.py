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
  <version>42</version>
  <name>TS_dhcp_stub_hal_get_gw</name>
  <primitive_test_id/>
  <primitive_test_name>dhcp_stub_hal_get_ert_gw</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate HAL API dhcpv4c_get_gw()</synopsis>
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
    <test_case_id>TC_HAL_DHCP_26</test_case_id>
    <test_objective>To validate HAL API dhcpv4c_get_gw()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dhcpv4c_get_gw()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  dhcp module.
2. From script invoke dhcpv4c_get_gw().
3. Get the IP address of gateway
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_DHCP stub.</automation_approch>
    <except_output>IP address should be valid.</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_DHCP</test_stub_interface>
    <test_script>TS_dhcp_stub_hal_get_gw</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
#Import the following stubs for execution
import tdklib;
import re;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("dhcp","RDKB");
obj.configureTestCase(ip,port,'TS_dhcp_stub_hal_get_ert_gw');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("dhcp_stub_hal_get_ert_gw");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details1 = details;
            print "TEST STEP 1: Retrieve the dhcp_stub_hal_get_ert_gw";
            print "EXPECTED RESULT 1: Should retrieve the dhcp_stub_hal_get_ert_gw successfully";
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
            print "Erouter gateway address is %s" %details1;
            tdkTestObj = obj.createTestStep("erouter_ip_stub_get_ip_address");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details3 = tdkTestObj.getResultDetails();
            details4 = details3;
            details5 = details4.split(".")[0]+"."+details4.split(".")[1]+"."+details4.split(".")[2];
            details6 = details1.split(".")[0]+"."+details1.split(".")[1]+"."+details1.split(".")[2];
            if details6 == details5:
                print "valid Gateway address";
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details3= tdkTestObj.getResultDetails();
                tdkTestObj = obj.createTestStep("dhcp_stub_hal_get_ert_mask");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                tdkTestObj.setResultStatus("SUCCESS");
                details7= tdkTestObj.getResultDetails();
                details8 = details7;
                print "Mask of erouter IP is %s" %details8;
                details9 = details8.split(".");
                details10 = details9[3];
                details13 = int(details10);
                details11 = details4[0:-3];
                if details13 == 0:
                    details13 = int(details13 + 1);
                    details13 = str(details13);
                    details12 = details11 + "." + details13;
                    print "only one Network so the gateway address is %s" %details12;
            else:
                print "invalid ip address"; 
                tdkTestObj.setResultStatus("FAILURE");
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "TEST STEP 1: Retrieve the dhcp_stub_hal_get_ert_gw";
            print "EXPECTED RESULT 1: Should retrieve the dhcp_stub_hal_get_ert_gw successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        obj.unloadModule("dhcp");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
