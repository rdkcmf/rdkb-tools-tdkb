##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_PAM_SetDHCPServerIPBeyondPrivateAddressRange</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>This test case will check whether setting the DHCP server IP beyond the allowed private address range is not allowed</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_177</test_case_id>
    <test_objective>This test case will check whether setting the DHCP server IP beyond the allowed private address range is not allowed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, RPI, Emulator</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state
2.TDK Agent should be in running state</pre_requisite>
    <api_or_interface_used>CcspBaseIf_setParameterValues</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress
</input_parameters>
    <automation_approch>1. Set the LAN Gateway IP address beyond the allowed range of private IP address using the parameter Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress.</automation_approch>
    <except_output>Setting the LAN Gateway IP address beyond the allowed range of private IP address using the parameter should fail</except_output>
    <priority>High</priority>
    <test_stub_interface>pam_SetParameterValues</test_stub_interface>
    <test_script>TS_PAM_SetDHCPServerIPBeyondPrivateAddressRange</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
						# import statements
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetDHCPServerIPBeyondPrivateAddressRange');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

if "SUCCESS" in loadModuleresult.upper():
        obj.setLoadModuleStatus("SUCCESS");

        tdkTestObj = obj.createTestStep("pam_SetParameterValues");
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress");
        tdkTestObj.addParameter("Type","string");
        tdkTestObj.addParameter("ParamValue","172.10.0.1");
        expectedresult = "FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details = tdkTestObj.getResultDetails();
            print "[TEST STEP 1]: Set the DHCP Server IP beyond allowed private address range";
            print "[EXPECTED RESULT 1]: Should fail to set DHCP Server IP beyond allowed private address range";
            print "[ACTUAL RESULT 1]: %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "[TEST STEP 1]: Set the DHCP Server IP beyond allowed private address range";
            print "[EXPECTED RESULT 1]: Should fail to set DHCP Server IP beyond allowed private address range";
            print "[ACTUAL RESULT 1]: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";
        obj.unloadModule("pam");
else:
        print "Failed to load pam module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";


