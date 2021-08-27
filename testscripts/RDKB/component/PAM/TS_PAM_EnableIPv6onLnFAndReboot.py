##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_PAM_EnableIPv6onLnFAndReboot</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To enable IPv6onLnF ,reboot and check if parameter is not triggering a reboot</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_PAM_215</test_case_id>
    <test_objective>This test case is to enable IPv6onLnF ,reboot and check if parameter is not triggering a reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable
3.Enable the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable and reboot
4.Check the last reboot reason and it should not be a rfc_reboot
5.Unload the module</automation_approch>
    <expected_output>With Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable enabled the RFC should not a trigger a reboot on the DUT</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_EnableIPv6onLnFAndReboot</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_EnableIPv6onLnFAndReboot');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;


if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the value ofIPv6onLnF Enable";
        print "EXPECTED RESULT 1: Should get the value of IPv6onLnF";
        print "ACTUAL RESULT 1:IPv6onLnF Enable :%s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        tdkTestObj = obj.createTestStep("pam_Setparams");
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable");
        tdkTestObj.addParameter("ParamValue","true");
        tdkTestObj.addParameter("Type","bool");

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the value forIPv6onLnF Enable";
            print "EXPECTED RESULT 2: Should set the value of IPv6onLnF";
            print "ACTUAL RESULT 2:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            #rebooting the device
            obj.initiateReboot();
            time.sleep(300);

            tdkTestObj = obj.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_LastRebootReason");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and "rfc_reboot" not  in details:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the reboot reason after IPv6onLnF is enabled ";
                print "EXPECTED RESULT 3:IPv6onLnF Enable should not cause reboot";
                print "ACTUAL RESULT 3: result :",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the reboot reason after IPv6onLnF is enabled ";
                print "EXPECTED RESULT 3:IPv6onLnF Enable should not cause reboot";
                print "ACTUAL RESULT 3: result :",details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"

            #Revert the value
            tdkTestObj = obj.createTestStep("pam_Setparams");
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.IPv6onLnF.Enable");
            tdkTestObj.addParameter("ParamValue",orgValue);
            tdkTestObj.addParameter("Type","bool");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4:Revert value forIPv6onLnF Enable";
                print "EXPECTED RESULT 4: Should revert the value of IPv6onLnF";
                print "ACTUAL RESULT 4:%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4:Revert value forIPv6onLnF Enable";
                print "EXPECTED RESULT 4: Should set the value of IPv6onLnF";
                print "ACTUAL RESULT 4:%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the value forIPv6onLnF Enable";
            print "EXPECTED RESULT 2: Should set the value of IPv6onLnF";
            print "ACTUAL RESULT 2:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the value ofIPv6onLnF Enable";
        print "EXPECTED RESULT 1: Should get the value of IPv6onLnF";
        print "ACTUAL RESULT 1: Failed to getIPv6onLnF Enable";
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");

else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
