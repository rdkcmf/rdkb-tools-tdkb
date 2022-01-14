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
  <version>4</version>
  <name>TS_PAM_CheckSyndicationPartnerPersistenceOnFactoryReset_test-partner</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the Syndication Test Partner ID "test-partner" is activated successfully and if the Partner ID persists on factory reset.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_PAM_243</test_case_id>
    <test_objective>Check if the Syndication Test Partner ID "test-partner" is activated successfully and if the Partner ID persists on factory reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId
ParamValue : setValue(test-partner)
Type : string
ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId
ParamValue : true
Type : bool
ParamName : Device.X_CISCO_COM_DeviceControl.FactoryReset
ParamValue : Router,Wifi,VoIP,Dect,MoCA
Type : string</input_parameters>
    <automation_approch>1. Load the modules
2. Get the current Syndication Partner ID using Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId and store it.
3. Set the Syndication Partner ID to "test-partner" and check if the SET operation returned success.
4. Activate the Test Partner by setting Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId to "true" which will cause the device to go for a reboot.
5. Once the device comes up, query the Partner ID and check if its is the Test Partner ID set.
6. Initiate a factory reset.
7. Once the device comes up, query the Syndication partner ID and verify if the Test Partner ID persisted on factory reset
8. Revert the syndication partner ID and activate the same.
9. Unload the modules</automation_approch>
    <expected_output>The Test Partner ID "test-partner" should be successfully set to Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId and activated and the Test Partner ID should persist on Factory Reset.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckSyndicationPartnerPersistenceOnFactoryReset_test-partner</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckSyndicationPartnerPersistenceOnFactoryReset_test-partner');

setValue = "test-partner"

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    #Get the current syndication partner
    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails().strip();

    print "\nTEST STEP 1 : Get the value of Syndication Partner ID using Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId";
    print "EXPECTED RESULT 1 : Syndication Partner ID should be retrieved successfully";

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1 : GET operation success; Syndication Partner ID : %s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #Set to new Partner ID
        tdkTestObj = obj.createTestStep('pam_Setparams');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
        tdkTestObj.addParameter("ParamValue",setValue);
        tdkTestObj.addParameter("Type","string");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip();

        print "\nTEST STEP 2 : Set the value for Syndication PartnerId to %s using Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId" %setValue;
        print "EXPECTED RESULT 2 : New syndication Partner ID should be set successfully";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2 : SET operation success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            #save device's current state before it goes for reboot when Partner ID is activated
            obj.saveCurrentState();
            tdkTestObj = obj.createTestStep("pam_Setparams");
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","bool");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();

            print "\nTEST STEP 3 : Activate the Syndication Partner ID using Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId";
            print "EXPECTED RESULT 3 : New Syndication Partner ID should be activated successfully"

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3 : SET operation success; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
                print "Device going for a reboot....";
                obj.restorePreviousStateAfterReboot();

                #Check the new syndication Partner ID
                tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip();

                print "\nTEST STEP 4: Get the set value of Syndication Partner ID after activating the partner ID";
                print "EXPECTED RESULT 4 : The syndication Partner ID should be the same as the set value after activation";
                print "Syndication Partner ID set : %s" %setValue;
                print "Syndication Partner ID after activation : %s" %details;

                if expectedresult in actualresult and setValue == details:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: GET operation success; Syndication PartnerId :%s" %details;
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

                    print "\nTEST STEP 5: Initiate factory reset";
                    print "EXPECTED RESULT 5 : DUT should be factory resetted successfully";

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5: Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        #Restore the device state saved before reboot
                        obj.restorePreviousStateAfterReboot();

                        #Get the syndication Partner ID and check if the setValue persists on FR
                        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
                        expectedresult="SUCCESS";
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        new_partner = tdkTestObj.getResultDetails().strip();

                        print "\nTEST STEP 6: Get the value of Syndication Partner ID after factory reset";
                        print "EXPECTED RESULT 6 : The Syndication Partner ID should be retrived after factory reset";

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6: GET operation success; Syndication PartnerId :%s" %new_partner;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            print "\nTEST STEP 7 : Check if the current Syndication Partner ID is the same as the test partner ID set";
                            print "EXPECTED RESULT 7 : The current Syndication Partner ID should be the same as the test partner ID set";
                            print "Test Partner ID Set : %s" %setValue;
                            print "Current Syndication Partner ID : %s" %new_partner;

                            if new_partner == setValue:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 7: The Syndication Test Partner ID set is reflected in get";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS"

                                #Revert operation
                                tdkTestObj = obj.createTestStep("pam_Setparams");
                                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.PartnerId");
                                tdkTestObj.addParameter("ParamValue",orgValue);
                                tdkTestObj.addParameter("Type","string");
                                #Execute the test case in DUT
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                print "\nTEST STEP 8 : Revert the Syndication Partner ID to initial value : %s" %orgValue;
                                print "EXPECTED RESULT 8 : Should revert the Syndication partner ID to %s successfully" %orgValue;

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 8 : SET operation success; Details : %s" %details;
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

                                    print "\nTEST STEP 9 : Activate the Syndication Partner ID using Device.DeviceInfo.X_RDKCENTRAL-COM_Syndication.RDKB_Control.ActivatePartnerId";
                                    print "EXPECTED RESULT 9 : Should activate the initial Syndication Partner ID successfully";

                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT 9: Activation success; Details : %s" %details;
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS"
                                        print "Device going for a reboot....";
                                        obj.restorePreviousStateAfterReboot();
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT 9 :Activation failed; Details : %s" %details;
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 8: SET operation failed; Details : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE"
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 7: Test Syndication Partner ID set is not reflected in get after factory reset";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6: GET operation failed; Syndication Partner ID :%s" %new_partner;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE"
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5: Factory Reset failed; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: Syndication PartnerId :%s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Partner ID activation failed; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: SET operation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: GET operation failed; Details : %s" %orgValue;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam");
else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
