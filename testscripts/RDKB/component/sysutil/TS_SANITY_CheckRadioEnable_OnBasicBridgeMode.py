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
  <name>TS_SANITY_CheckRadioEnable_OnBasicBridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the radios are disabled when device is set to "full-bridge-static" (Basic bridge mode) using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_SANITY_78</test_case_id>
    <test_objective>To check if the radios are disabled when device is set to "full-bridge-static" (Basic bridge mode) using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
ParamValue : full-bridge-static/bridge-static/router
Type : string
ParamName : Device.WiFi.Radio.1.Enable
ParamName : Device.WiFi.Radio.2.Enable</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial lan mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
3. If the lan mode is not already full-bridge-static, set to full-bridge-static and validate with get.
4. Get the enable state of Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable
5. Check if both the radio enables are false when device is in basic bridge mode.
6. Revert the lan mode to initial value if required.
7. Unload the module.</automation_approch>
    <expected_output>Radios should be disabled when device is set to "full-bridge-static" (Basic bridge mode) using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckRadioEnable_OnBasicBridgeMode</test_script>
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
pamObj.configureTestCase(ip,port,'TS_SANITY_CheckRadioEnable_OnBasicBridgeMode');

#Get the result of connection with test component and STB
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
            #Get the radio enable state
            status = 0;
            Values = [];
            step = step + 1;
            paramList = ["Device.WiFi.Radio.1.Enable", "Device.WiFi.Radio.2.Enable"];
            print "\nTEST STEP %d : Get the initial 2.4G and 5G Radio enable states" %step;
            print "EXPECTED RESULT %d : The values should be retrieved successfully" %step;

            for param in paramList:
                tdkTestObj = pamObj.createTestStep("pam_GetParameterValues");
                tdkTestObj.addParameter("ParamName",param)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                enable = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if expectedresult in actualresult and enable != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "\n%s : %s" %(param, enable);
                    Values.append(enable);
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "\n%s : %s" %(param, enable);

            if status == 0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 1: The values retrieved are respectively : %s, %s" %(Values[0], Values[1]) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the radios are in disabled state
                step = step + 1;
                print "\nTEST STEP %d : Check if both radios are in disabled state when device is in basic bridge mode" %step;
                print "EXPECTED RESULT %d : Both radios should be in disabled state when device is in basic bridge mode" %step;

                if Values[0] == "false" and Values[1] == "false":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Both radios are disabled when device is in basic bridge mode" %step ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Both radios are NOT disabled when device is in basic bridge mode" %step ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert to initial lan mode
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
                print "ACTUAL RESULT %d: The values are NOT retrieved successfully" %step;
                #Get the result of execution
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
