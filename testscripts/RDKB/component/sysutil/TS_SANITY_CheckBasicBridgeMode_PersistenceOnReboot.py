##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_SANITY_CheckBasicBridgeMode_PersistenceOnReboot</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if setting Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to full-bridge-static (Basic bridge mode) is success and if it persists on reboot.</synopsis>
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
    <test_case_id>TC_SANITY_77</test_case_id>
    <test_objective>To check if setting Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to full-bridge-static (Basic bridge mode) is success and if it persists on reboot.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
ParamValue : full-bridge-static/bridge-static/router
Type : string</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial lan mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.
3. If the initial lan mode is not Basic bridge mode (full-bridge-static), perform the set operation and validate with get.
4. Reboot the DUT.
5. Once the device is up, retrieve the lan mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.
6. Check if the lan mode is Basic bridge static.
7. Revert to initial lan mode if required.
8. Unload the module</automation_approch>
    <expected_output>The Basic bridge mode (full-bridge-static) should persist on reboot.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckBasicBridgeMode_PersistenceOnReboot</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamObj.configureTestCase(ip,port,'TS_SANITY_CheckBasicBridgeMode_PersistenceOnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus1 =pamObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    pamObj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the current Lan mode
    step = 1;
    revert_flag = 0;
    proceed_flag = 0;
    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanMode_initial = tdkTestObj.getResultDetails().strip();

    print "\nTEST STEP %d : Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
    print "EXPECTED RESULT %d : Should successfully retrieve the initial Lan Mode" %step;

    if expectedresult in actualresult and lanMode_initial != "":
        tdkTestObj.setResultStatus("SUCCESS");
        #Set the result status of execution
        print "ACTUAL RESULT %d : Initial Lan Mode is %s" %(step, lanMode_initial);
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set the Lan Mode to basic bridge mode : full-bridge-static if not already in that mode
        if lanMode_initial != "full-bridge-static":
            step = step + 1;
            tdkTestObj = pamObj.createTestStep('pam_Setparams');
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
            tdkTestObj.addParameter("ParamValue","full-bridge-static");
            tdkTestObj.addParameter("Type","string");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            sleep(150);

            print "\nTEST STEP %d : Set the Lan Mode to Basic bridge mode : full-bridge-static using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
            print "EXPECTED RESULT %d : Should set to basic bridge mode successfully" %step;

            if expectedresult in actualresult and details != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Setting to full-bridge-static was success; Details : %s" %(step, details);
                print "[TEST EXECUTION RESULT] : SUCCESS" ;

                #Validate the set operation with get
                step = step + 1;
                tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
                tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                lanMode_current = tdkTestObj.getResultDetails().strip();

                print "\nTEST STEP %d : Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
                print "EXPECTED RESULT %d : Should successfully retrieve the current Lan Mode" %step;

                if expectedresult in actualresult and lanMode_current != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Current Lan Mode is %s" %(step, lanMode_current);
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if lanMode_current == "full-bridge-static":
                        revert_flag = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Device is in Basic Bridge Mode";
                    else:
                        proceed_flag = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Device is NOT in Basic Bridge Mode";
                else:
                    proceed_flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Unable to retrieve the current Lan Mode; Details : %s" %(step, lanMode_current);
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                proceed_flag = 1;
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Setting to full-bridge-static failed; Details : %s" %(step, details);
                print "[TEST EXECUTION RESULT] : SUCCESS" ;
        else:
            print "DUT already in full-bridge-static mode, SET operation not required...";

        if proceed_flag == 0:
	        #rebooting the device
            print "\n********************Rebooting the Device********************";
            pamObj.initiateReboot();
            print "Sleeping for 300s";
            sleep(300);
            print "\n********************Device Up after reboot********************";

            #Check if the full-bridge-static mode persists on reboot
            step = step + 1;
            tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            lanMode = tdkTestObj.getResultDetails().strip();

            print "\nTEST STEP %d : Retrieve the Lan Mode after reboot" %step;
            print "EXPECTED RESULT %d : Lan Mode should be retrieved successfully after reboot" %step;

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Lan Mode after reboot is : %s" %(step, lanMode);
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if basic bridge mode persists on reboot
                step = step + 1;
                print "\nTEST STEP %d : Check if the Basic bridge mode set is persisting on device reboot" %step;
                print "EXPECTED RESULT %d : Basic bridge mode set should persist on device reboot" %step;

                if lanMode == "full-bridge-static":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Basic Bridge Mode persists on reboot" %step;
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if revert_flag == 1:
                        step = step + 1;
                        tdkTestObj = pamObj.createTestStep('pam_Setparams');
                        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
                        tdkTestObj.addParameter("ParamValue",lanMode_initial);
                        tdkTestObj.addParameter("Type","string");
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        sleep(150);

                        print "\nTEST STEP %d : Revert the Lan Mode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, lanMode_initial);
                        print "EXPECTED RESULT %d : Should revert to initial lan mode successfully" %step;

                        if expectedresult in actualresult and details != "":
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Reverting the lan mode was success; Details : %s" %(step, details);
                            print "[TEST EXECUTION RESULT] : SUCCESS" ;
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Reverting the lan mode failed; Details : %s" %(step, details);
                            print "[TEST EXECUTION RESULT] : FAILURE" ;
                    else :
                        print "Lan Mode revert operation not required";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Basic Bridge Mode does NOT persist on reboot" %step;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Lan Mode after reboot is not retrieved; Details : %s" %(step, lanMode);
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Lan Mode is not set to Basic bridge static, cannot proceed...";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        #Set the result status of execution
        print "ACTUAL RESULT %d : Initial Lan Mode is not retrieved successfully; Details : %s" %(step, lanMode_initial);
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamObj.unloadModule("pam");
else:
    print "Failed to load sysutil module";
    pamObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
