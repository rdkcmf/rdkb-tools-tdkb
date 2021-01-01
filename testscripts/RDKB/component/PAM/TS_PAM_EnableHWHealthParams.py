##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_PAM_EnableHWHealthParams</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if enabling Hw Health and execute the test should log the result in HWSTLog file</synopsis>
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
    <test_case_id>TC_PAM_191</test_case_id>
    <test_objective>This test case is to check if enabling Hw Health and execute the test should log the result in HWSTLog file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable
Device.X_RDK_hwHealthTest.executeTest</input_parameters>
    <automation_approch>1.Load the module
2.Get the enable status of  hw Health Test and hw Health execute Test
3.Enable the  hw Health parameters
4.Check if HwTestResult2: is logged in HWSTLog.txt.0 log file.
5.Revert the set parameter
6.Unload the module</automation_approch>
    <expected_output>After enabling hw Health  parameter  HwTestResult2:  should be logged in log file</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_EnableHWHealthParams</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2= tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_EnableHWHealthParams');
obj2.configureTestCase(ip,port,'TS_PAM_EnableHWHealthParams');

#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
loadmodulestatus1=obj2.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult ="SUCCESS";

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    defEnable = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Health Test Enable status";
        print "EXPECTED RESULT 1: Should Get the Health Test Enable status";
        print "ACTUAL RESULT 1: %s" %defEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_hwHealthTest.executeTest");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        defExecTest = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Health Test ExecuteTest status";
            print "EXPECTED RESULT 2: Should Get the Health Test ExecuteTest status";
            print "ACTUAL RESULT 2: %s" %defExecTest;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","boolean");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Enabling the  Health Test Enable";
                print "EXPECTED RESULT 3: Should Enable the Health Test Enable";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                tdkTestObj.addParameter("ParamName","Device.X_RDK_hwHealthTest.executeTest");
                tdkTestObj.addParameter("ParamValue","true");
                tdkTestObj.addParameter("Type","boolean");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Executing the  Hw Health Test by enabling Device.X_RDK_hwHealthTest.executeTest";
                    print "EXPECTED RESULT 4: Should execute the  Hw Health Test";
                    print "ACTUAL RESULT 4: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj2.createTestStep('ExecuteCmd');
                    cmd = "[ -f /rdklogs/logs/HWSTLog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
                    tdkTestObj.addParameter("command",cmd);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if details == "File exist":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Check for HWSTLog.txt.0 log file presence";
                        print "EXPECTED RESULT 5:HWSTLog.txt.0 log file should be present";
                        print "ACTUAL RESULT 5: HWSTLog.txt.0 log file is present";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        markerfound = 0;
                        for i in range(1,6):
                            if markerfound == 1:
                                break;
                            else:
                                tdkTestObj = obj2.createTestStep('ExecuteCmd');
                                cmd = "grep -i \"HwTestResult2:\" /rdklogs/logs/HWSTLog.txt.0";
                                tdkTestObj.addParameter("command",cmd);
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                                print "Marker Detail Found fromLog file is: %s "%details;

                                if (len(details) == 0) or "HwTestResult2:" not in details:
                                    markerfound = 0;
                                    sleep(60);
                                else:
                                    markerfound = 1;
                                    break;
                        if expectedresult in actualresult and markerfound ==1:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Check for HwTestResult2  logged in log file";
                            print "EXPECTED RESULT 6:HwTestResult2 should be logged in log file";
                            print "ACTUAL RESULT 6: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FALIURE");
                            print "TEST STEP 6: Check for HwTestResult2  logged in log file";
                            print "EXPECTED RESULT 6:HwTestResult2 should be logged in log file";
                            print "ACTUAL RESULT 6: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Check for HWSTLog.txt.0 log file presence";
                        print "EXPECTED RESULT 5:HWSTLog.txt.0 log file should be present";
                        print "ACTUAL RESULT 5: HWSTLog.txt.0 log file is present";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                    #Revert the value
                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                    tdkTestObj.addParameter("ParamName","Device.X_RDK_hwHealthTest.executeTest");
                    tdkTestObj.addParameter("ParamValue",defExecTest);
                    tdkTestObj.addParameter("Type","boolean");
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 7: Reverting the  Hw Health Test execute parameter";
                        print "EXPECTED RESULT 7: Should revert the Hw Health Test execute parameter";
                        print "ACTUAL RESULT 7: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 7: Reverting the  Hw Health Test execute parameter";
                        print "EXPECTED RESULT 7: Should revert the Hw Health Test execute parameter";
                        print "ACTUAL RESULT 7: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Executing the  Hw Health Test by enabling Device.X_RDK_hwHealthTest.executeTest";
                    print "EXPECTED RESULT 4: Should execute the  Hw Health Test";
                    print "ACTUAL RESULT 4: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                #Reverting the value
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.hwHealthTest.Enable");
                tdkTestObj.addParameter("ParamValue",defEnable);
                tdkTestObj.addParameter("Type","boolean");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 8: Reverting the  Health Test Enable";
                    print "EXPECTED RESULT 8: Should revert the Health Test Enable";
                    print "ACTUAL RESULT 8: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("FAILURE");
                   print "TEST STEP 8: Reverting the  Health Test Enable";
                   print "EXPECTED RESULT 8: Should revert the Health Test Enable";
                   print "ACTUAL RESULT 8: %s" %details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Enabling the  Health Test Enable";
                print "EXPECTED RESULT 3: Should Enable the Health Test Enable";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Health Test ExecuteTest status";
            print "EXPECTED RESULT 2: Should Get the Health Test ExecuteTest status";
            print "ACTUAL RESULT 2: %s" %defExecTest;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Health Test Enable status";
        print "EXPECTED RESULT 1: Should Get the Health Test Enable status";
        print "ACTUAL RESULT 1: %s" %defEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
     obj2.setLoadModuleStatus("FAILURE");
