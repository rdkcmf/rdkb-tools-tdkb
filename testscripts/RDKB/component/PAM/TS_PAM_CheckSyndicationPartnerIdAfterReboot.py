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
  <name>TS_PAM_CheckSyndicationPartnerIdAfterReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set a syndication partner ID and check if it persists after reboot</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>45</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_157</test_case_id>
    <test_objective>To set a syndication partner ID and check if it persists after reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId</input_parameters>
    <automation_approch>1.Load module
2.Set value for syndication partnerID.
3.Activate the partner ID
4.Get the syndication partnerID.
5.Do a reboot
6.Check if it persists after reboot
7.Unload the module</automation_approch>
    <expected_output>Syndication partnerID should persist after reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckSyndicationPartnerIdAfterReboot</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_PAM_SetInvalidSyndicationPartnerId');
setValue = "unknown"

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;


if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the value of Syndication PartnerId";
        print "ACTUAL RESULT 1: Syndication PartnerId :%s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        tdkTestObj = obj.createTestStep("pam_Setparams");
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
        tdkTestObj.addParameter("ParamValue",setValue);
        tdkTestObj.addParameter("Type","string");

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the value for Syndication PartnerId";
            print "ACTUAL RESULT 2:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            #save device's current state before it goes for reboot
            obj.saveCurrentState();
            tdkTestObj = obj.createTestStep("pam_Setparams");
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","bool");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Activate the Syndication PartnerId";
                print "ACTUAL RESULT 3:%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
                #Restore the device state saved before reboot
                obj.restorePreviousStateAfterReboot();
                time.sleep(60);
                tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
                expectedresult="SUCCESS";

                #Execute the test case in STB
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and setValue in details:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the value of Syndication PartnerId after activating partner ID";
                    print "ACTUAL RESULT 4: Syndication PartnerId :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                    #rebooting the device
                    obj.initiateReboot();
                    time.sleep(300)
                    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");

                    #Execute the test case in STB
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and setValue in details:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Get the value of Syndication PartnerId after reboot";
                        print "ACTUAL RESULT 5: Syndication PartnerId persists on reboot";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Get the value of Syndication PartnerId after reboot";
                        print "ACTUAL RESULT 5: Syndication PartnerId does not persist on reboot";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the value of Syndication PartnerId after activating partner ID";
                    print "ACTUAL RESULT 4: Syndication PartnerId :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Activate the Syndication PartnerId";
                print "ACTUAL RESULT 3:%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
            tdkTestObj = obj.createTestStep("pam_Setparams");
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
            tdkTestObj.addParameter("ParamValue",orgValue);
            tdkTestObj.addParameter("Type","string");

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP :Revert value for Syndication PartnerId";
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
                #save device's current state before it goes for reboot
                obj.saveCurrentState();
                tdkTestObj = obj.createTestStep("pam_Setparams");
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId");
                tdkTestObj.addParameter("ParamValue","true");
                tdkTestObj.addParameter("Type","bool");

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Activate the Syndication PartnerId";
                    print "ACTUAL RESULT :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP : Activate the Syndication PartnerId";
                    print "ACTUAL RESULT :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP :Revert value for Syndication PartnerId";
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the value for Syndication PartnerId";
            print "ACTUAL RESULT 2:%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the value of Syndication PartnerId";
        print "ACTUAL RESULT 1: Failed to get Syndication PartnerId";
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");

else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

