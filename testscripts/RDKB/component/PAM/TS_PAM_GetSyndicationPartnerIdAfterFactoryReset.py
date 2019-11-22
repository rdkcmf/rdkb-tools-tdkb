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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_PAM_GetSyndicationPartnerIdAfterFactoryReset</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set a different value to syndication partner ID.To check if value is changed to default syndication partner ID after factory reset</synopsis>
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
    <test_case_id>TC_PAM_155</test_case_id>
    <test_objective>Set a different value to syndication partner ID.To check if value is changed to default syndication partner ID after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId</input_parameters>
    <automation_approch>1.Load module
2.Set value for syndication partner ID
3.Do a factory reset
4.Check if default syndication partner ID is retrieved after factory reset</automation_approch>
    <expected_output>Value should change to default syndication partner ID after factory reset</expected_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_PAM_GetSyndicationPartnerIdAfterFactoryReset</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","RDKB");



#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_GetSyndicationPartnerIdAfterFactoryReset');
obj1.configureTestCase(ip,port,'TS_PAM_GetSyndicationPartnerIdAfterFactoryReset');
setValue = "unknown"

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;


if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the value of Syndication PartnerId";
        print "ACTUAL RESULT 1: Syndication PartnerId :%s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        tdkTestObj = obj.createTestStep('pam_Setparams');
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
                obj.restorePreviousStateAfterReboot();

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
                    print "TEST STEP 4: Get the set value of Syndication PartnerId after activating partner ID";
                    print "ACTUAL RESULT 4: Syndication PartnerId :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    #Restore the device state saved before reboot
                    obj.saveCurrentState();
                    #Initiate Factory reset before checking the default value
                    tdkTestObj = obj.createTestStep('pam_Setparams');
                    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
                    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
                    tdkTestObj.addParameter("Type","string");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Initiate factory reset ";
                        print "ACTUAL RESULT 5: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        #Restore the device state saved before reboot
                        obj.restorePreviousStateAfterReboot();

                        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
                        expectedresult="SUCCESS";

                        #Execute the test case in STB
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Get the value of Syndication PartnerId after factory reset";
                            print "ACTUAL RESULT 6: Syndication PartnerId :%s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS"
                            tdkTestObj = obj1.createTestStep('ExecuteCmd');
                            command= "sh %s/tdk_utility.sh parseConfigFile PARTNER_ID" %TDK_PATH;
                            print command;
                            expectedresult="SUCCESS";
                            tdkTestObj.addParameter("command", command);
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            partner_id_details = tdkTestObj.getResultDetails().replace("\\n", "");
                            if expectedresult in actualresult and partner_id_details != "":
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7: Should get the value of PARTNER_ID from properties file"
                                print "ACTUAL RESULT 7:Syndication PartnerId : %s" %partner_id_details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                if partner_id_details == details:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP 8: PARTNER_ID from properties file and default Syndication PartnerId should be same"
                                    print "ACTUAL RESULT 8:PARTNER_ID from properties file and default Syndication PartnerId are same";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP 8: PARTNER_ID from properties file and default Syndication PartnerId should be same"
                                    print "ACTUAL RESULT 8:PARTNER_ID from properties file and default Syndication PartnerId are not same";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
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
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 7: Get value of PARTNER_ID"
                                print "ACTUAL RESULT 7: Failed to get the value of PARTNER_ID from properties file";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Get the value of Syndication PartnerId after factory reset";
                            print "ACTUAL RESULT 6: Syndication PartnerId :%s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE"
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Initiate factory reset"
                        print "ACTUAL RESULT 5: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the set value of Syndication PartnerId after activating partner ID";
                    print "ACTUAL RESULT 4: Syndication PartnerId :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Activate the Syndication PartnerId";
                print "ACTUAL RESULT 3:%s" %details;
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
    obj1.unloadModule("sysutil");

else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

