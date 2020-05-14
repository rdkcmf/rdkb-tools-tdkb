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
  <name>TS_PAM_CheckRabidEnableStatus_Persistence_OnReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check RabidEnableStatus persist on reboot</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_164</test_case_id>
    <test_objective>To check RabidEnableStatus persist on reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup></test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable</input_parameters>
    <automation_approch>1.Load module
2.Get Rabid Enable status
3.If it is enabled,disable it
4.If it is disabled,enable it
5.Reboot
6.Check if Rabid enable status persists on reboot
7.Unload module</automation_approch>
    <expected_output>Rabid enable status should persist on reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckRabidEnableStatus_Persistence_OnReboot</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckRabidEnableStatus_Persistence_OnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the RabidFramework Enable status";
        print "ACTUAL RESULT 1:RabidFramework Enable status is %s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        if orgValue == "true":
            print "Disable RabidFramework status"
            setValue = "false"
        else:
            print "Enable RabidFramework status"
            setValue = "true"

        tdkTestObj = obj.createTestStep('pam_Setparams');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
        tdkTestObj.addParameter("ParamValue",setValue);
        tdkTestObj.addParameter("Type","bool");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: RabidFramework status toggled using set";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #rebooting the device
            obj.initiateReboot();
            time.sleep(300)
            tdkTestObj = obj.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            enabledetails = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and setValue in enabledetails:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if RabidFramework status persists on reboot";
                print "ACTUAL RESULT 3:RabidFramework status persists on reboot";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Check if RabidFramework status persists on reboot";
                print "ACTUAL RESULT 3:RabidFramework status does not persist on reboot";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj = obj.createTestStep('pam_Setparams');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
            tdkTestObj.addParameter("ParamValue",orgValue);
            tdkTestObj.addParameter("Type","bool");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP :Revert RabidFramework status";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP :Revert RabidFramework status";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:Toggle RabidFramework status";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the RabidFramework Enable status";
        print "ACTUAL RESULT 1:Failed to get RabidFramework Enable status";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam");

else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

