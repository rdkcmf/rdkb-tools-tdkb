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
  <version>6</version>
  <name>TS_PAM_GetHardwareHealthTestResults</name>
  <primitive_test_id/>
  <primitive_test_name>pam_Setparams</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable the Hardware Health RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable and check if Hardware Health results are populated for Device.X_RDK_hwHealthTest.Results when Device.X_RDK_hwHealthTest.executeTest is enabled.</synopsis>
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
    <test_case_id>TC_PAM_247</test_case_id>
    <test_objective>Enable the Hardware Health RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable and check if Hardware Health results are populated for Device.X_RDK_hwHealthTest.Results when Device.X_RDK_hwHealthTest.executeTest is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable
ParamValue : true/false
Type : boolean
ParamName : Device.X_RDK_hwHealthTest.executeTest
ParamValue : true/false
Type : boolean
ParamName : Device.X_RDK_hwHealthTest.Results</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial enable status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable
3. If the RFC is not enabled, set to true and reboot the DUT. Once the DUT comes up, validate with get operation.
4. Get the enable status of Device.X_RDK_hwHealthTest.executeTest
5. If Device.X_RDK_hwHealthTest.executeTest is not already true, set to true and validate with get operation.
6. Check if the hardware test results are populated under the DM Device.X_RDK_hwHealthTest.Results
7. Revert Device.X_RDK_hwHealthTest.executeTest to initial value if required
8. Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable to initial state if required
9. Unload the module</automation_approch>
    <expected_output>Device.X_RDK_hwHealthTest.Results should be populated after Device.X_RDK_hwHealthTest.executeTest is enabled when the controlling RFC for hardware health Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is in enabled state.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_GetHardwareHealthTestResults</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getValues(param, tdkTestObj):
    expectedresult = "SUCCESS"
    tdkTestObj.addParameter("ParamName", param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    value = tdkTestObj.getResultDetails().strip();
    return value, actualresult;

def setValues(param, paramValue, paramType, tdkTestObj):
    expectedresult = "SUCCESS"
    tdkTestObj.addParameter("ParamName",param);
    tdkTestObj.addParameter("ParamValue",paramValue);
    tdkTestObj.addParameter("Type",paramType);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return details, actualresult;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_PAM_GetHardwareHealthTestResults');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper():
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Get the Hardware Health Test RFC
    step = 1;
    tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
    RFC_param = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable";
    initial_enable, actualresult = getValues(RFC_param, tdkTestObj);

    print "\nTEST STEP %d : Get the enable status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable" %step;
    print "EXPECTED RESULT %d : The RFC value should be retrieved successfully" %step;

    if expectedresult in actualresult and initial_enable != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is : %s" %(step, initial_enable) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check the GET value, if it is not true, set to true and reboot
        revert_flag = 0;
        rfc_set = 0;
        if initial_enable != "true":
            step = step + 1;
            tdkTestObj = obj1.createTestStep('pam_Setparams');
            details, actualresult = setValues(RFC_param, "true", "boolean", tdkTestObj);

            print "\nTEST STEP %d : Set the enable status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable to true" %step;
            print "EXPECTED RESULT %d : The RFC value should be enabled successfully" %step;

            if expectedresult in actualresult and details != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is set successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "****DUT is going for a reboot for RFC to take effect and will be up after 360 seconds*****";
                obj1.initiateReboot();
                sleep(360);

                #After the device comes up, verify if the RFC set was success
                step = step + 1;
                tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
                curr_enable, actualresult = getValues(RFC_param, tdkTestObj);

                print "\nTEST STEP %d : Get the enable status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable" %step;
                print "EXPECTED RESULT %d : The RFC value should be retrieved successfully" %step;

                if expectedresult in actualresult and curr_enable != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is : %s" %(step, curr_enable) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if curr_enable == "true":
                        revert_flag = 1;
                        rfc_set = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Hardware Health Test RFC is enabled successfully";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Hardware Health Test RFC is NOT enabled successfully";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is : %s" %(step, curr_enable) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is NOT set successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            rfc_set = 1;
            print "Hardware Health Test RFC is in enabled state, SET operation not required";

        if rfc_set == 1:
            #Get initial value of Device.X_RDK_hwHealthTest.executeTest
            step = step + 1;
            tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
            test_param = "Device.X_RDK_hwHealthTest.executeTest";
            initial_test, actualresult = getValues(test_param, tdkTestObj);

            print "\nTEST STEP %d : Get the enable status of Device.X_RDK_hwHealthTest.executeTest" %step;
            print "EXPECTED RESULT %d : The parameter value should be retrieved successfully" %step;

            if expectedresult in actualresult and initial_test != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is : %s" %(step, initial_test) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Set Device.X_RDK_hwHealthTest.executeTest to true if not already enabled
                test_set = 0;
                test_revert = 0;
                if initial_test != "true":
                    step = step + 1;
                    tdkTestObj = obj1.createTestStep('pam_Setparams');
                    details, actualresult = setValues(test_param, "true", "boolean", tdkTestObj);

                    print "\nTEST STEP %d : Set the enable status of Device.X_RDK_hwHealthTest.executeTest to true" %step;
                    print "EXPECTED RESULT %d : The parameter should be enabled successfully" %step;

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is set successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Cross check with GET
                        step = step + 1;
                        tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
                        curr_test, actualresult = getValues(test_param, tdkTestObj);

                        print "\nTEST STEP %d : Get the enable status of Device.X_RDK_hwHealthTest.executeTest" %step;
                        print "EXPECTED RESULT %d : The parameter value should be retrieved successfully" %step;

                        if expectedresult in actualresult and curr_test != "":
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is : %s" %(step, curr_test) ;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if curr_test == "true":
                                test_set = 1;
                                test_revert = 1;
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ExecuteTest is enabled successfully";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ExecuteTest is NOT enabled successfully";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is : %s" %(step, curr_test) ;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is NOT set successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    test_set = 1;
                    print "Execute Test is in enabled state, SET operation not required";

                if test_set == 1:
                    #Check if Hardware Health Test Results are populated
                    step = step + 1;
                    sleep(30);
                    tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
                    hw_results_param = "Device.X_RDK_hwHealthTest.Results";
                    hw_results, actualresult = getValues(hw_results_param, tdkTestObj);

                    print "\nTEST STEP %d : Get the Hardware Health Test Results using Device.X_RDK_hwHealthTest.Results" %step;
                    print "EXPECTED RESULT %d : The Hardware Health Test Results should be retrieved successfully" %step;

                    if expectedresult in actualresult and hw_results != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.Results is : %s" %(step, hw_results) ;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.Results is : %s" %(step, hw_results) ;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Cannot proceed with the next step as Execute Test is not enabled...";

                #Revert operation of Execute Test
                if test_revert == 1:
                    step = step + 1;
                    tdkTestObj = obj1.createTestStep('pam_Setparams');
                    details, actualresult = setValues(test_param, initial_enable, "boolean", tdkTestObj);

                    print "\nTEST STEP %d : Revert the enable status of Device.X_RDK_hwHealthTest.executeTest" %step;
                    print "EXPECTED RESULT %d : The parameter should be reverted successfully" %step;

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is reverted successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is NOT reverted successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Execute Test revert not required...";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Device.X_RDK_hwHealthTest.executeTest is : %s" %(step, initial_test) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Cannot proceed with the next steps as Hardware Health Test RFC is not enabled...";

        #Revert operation of RFC
        if revert_flag == 1:
            step = step + 1;
            tdkTestObj = obj1.createTestStep('pam_Setparams');
            details, actualresult = setValues(RFC_param, initial_enable, "boolean", tdkTestObj);

            print "\nTEST STEP %d : Revert the enable status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable" %step;
            print "EXPECTED RESULT %d : The RFC value should be reverted successfully" %step;

            if expectedresult in actualresult and details != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is reverted successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "****DUT is going for a reboot for RFC to take effect and will be up after 360 seconds*****";
                obj1.initiateReboot();
                sleep(360);
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is NOT reverted successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "RFC revert not required...";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable is : %s" %(step, initial_enable) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj1.unloadModule("pam");
else:
    print "Failed to load sysutil module";
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
