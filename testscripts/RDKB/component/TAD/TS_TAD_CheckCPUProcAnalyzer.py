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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TAD_CheckCPUProcAnalyzer</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if cpuprocanalyzer process is running after enabling Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TAD_81</test_case_id>
    <test_objective>To check if cpuprocanalyzer process is running after enabling Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_SetOnly
</api_or_interface_used>
    <input_parameters>Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable</input_parameters>
    <automation_approch>1.Load the module
2.Set the value to true "sysevent set UPLOAD_LOGS_VAL_DCM true" if it is false.
3.Trigger the process by enabling Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable
4.Check the process ps | grep -i /usr/bin/cpuprocanalyzer
5.Verify no Error messages are seen  in /rdklogs/logs/CPUPROCANALYZERlog.txt.0
6.Unload the Module</automation_approch>
    <expected_output>After enabling Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable   cpuprocanalyzer process should be running</expected_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_CheckCPUProcAnalyzer</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_CheckCPUProcAnalyzer');
obj1.configureTestCase(ip,port,'TS_TAD_CheckCPUProcAnalyzer');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and  "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult :
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the CPUProc Analyzer Enable status";
       print "EXPECTED RESULT 1: Should get the CPUProc Analyzer Enable status";
       print "ACTUAL RESULT 1: CPUProc Analyzer Enable status is:",details
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       tdkTestObj = obj.createTestStep('ExecuteCmd');
       cmd= "sysevent get UPLOAD_LOGS_VAL_DCM";
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("command",cmd);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       default = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if expectedresult in actualresult  and default !="":
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Get the UPLOAD_LOGS_VAL_DCM value";
           print "EXPECTED RESULT 2: Should get the UPLOAD_LOGS_VAL_DCM value";
           print "ACTUAL RESULT 2: UPLOAD_LOGS_VAL_DCM  status is:",default
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";

           tdkTestObj = obj.createTestStep('ExecuteCmd');
           cmd= "sysevent set UPLOAD_LOGS_VAL_DCM true";
           expectedresult="SUCCESS";
           tdkTestObj.addParameter("command",cmd);
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
           if expectedresult in actualresult:
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Set the UPLOAD_LOGS_VAL_DCM to true";
              print "EXPECTED RESULT 3 : Should set the UPLOAD_LOGS_VAL_DCM value to true";
              print "ACTUAL RESULT 3:",details
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";

              tdkTestObj = obj.createTestStep('ExecuteCmd');
              cmd= "sysevent get UPLOAD_LOGS_VAL_DCM";
              expectedresult="SUCCESS";
              tdkTestObj.addParameter("command",cmd);
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
              if expectedresult in actualresult  and details =="true":
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 4: Check if  UPLOAD_LOGS_VAL_DCM is true";
                 print "EXPECTED RESULT 4: Should get the UPLOAD_LOGS_VAL_DCM as true";
                 print "ACTUAL RESULT 4: UPLOAD_LOGS_VAL_DCM  status is:",details
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";

                 tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_SetOnly');
                 tdkTestObj.addParameter("ParamName","Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable");
                 tdkTestObj.addParameter("ParamValue","true");
                 tdkTestObj.addParameter("Type","bool");
                 expectedresult="SUCCESS";
                 #Execute the test case in DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 details = tdkTestObj.getResultDetails();
                 if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Enable CPUProc Analyzer";
                    print "EXPECTED RESULT 5: Should enable CPUProc Analyzer";
                    print "ACTUAL RESULT 5:",details
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    sleep(10);
                    tdkTestObj = obj.createTestStep('ExecuteCmd');
                    cmd= "pidof cpuprocanalyzer";
                    expectedresult="SUCCESS";
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if expectedresult in actualresult and details != "":
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "TEST STEP 6: Check if cpuprocanalyzer process is running";
                       print "EXPECTED RESULT 6: cpuprocanalyzer process should be running";
                       print "ACTUAL RESULT 6:pidof cpuprocanalyzer is :",details
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : SUCCESS";

                       tdkTestObj = obj.createTestStep('ExecuteCmd');
                       cmd= "grep -rin \"error\" /rdklogs/logs/CPUPROCANALYZERlog.txt.0";
                       expectedresult="SUCCESS";
                       tdkTestObj.addParameter("command",cmd);
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                       if expectedresult in actualresult:
                          #Set the result status of execution
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 7: Check if any Error mesages are present in CPUPROCANALYZERlog.txt.0";
                          print "EXPECTED RESULT 7: No Error messages should be present in CPUPROCANALYZERlog.txt.0";
                          print "ACTUAL RESULT 7:",details
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";
                       else:
                           #Set the result status of execution
                           tdkTestObj.setResultStatus("FAILURE");
                           print "TEST STEP 7: Check if any Error mesages are present in CPUPROCANALYZERlog.txt.0";
                           print "EXPECTED RESULT 7: No Error messages should be present in CPUPROCANALYZERlog.txt.0";
                           print "ACTUAL RESULT 7:",details
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: Check if cpuprocanalyzer process is running";
                        print "EXPECTED RESULT 6: cpuprocanalyzer process should be running";
                        print "ACTUAL RESULT 6:pidof cpuprocanalyzer is :",details
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                    #Revert the Value
                    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_SetOnly');
                    tdkTestObj.addParameter("ParamName","Device.SelfHeal.X_RDK_CPUProcAnalyzer_Enable");
                    tdkTestObj.addParameter("ParamValue","false");
                    tdkTestObj.addParameter("Type","bool");
                    expectedresult="SUCCESS";
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "TEST STEP 7: Disable the CPUProcAnalyzer";
                       print "EXPECTED RESULT 7:Should disable the CPUProcAnalyzer";
                       print "ACTUAL RESULT 7:",details
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : SUCCESS";

                       tdkTestObj = obj.createTestStep('ExecuteCmd');
                       cmd= "sysevent set UPLOAD_LOGS_VAL_DCM %s" %default;
                       expectedresult="SUCCESS";
                       tdkTestObj.addParameter("command",cmd);
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                       if expectedresult in actualresult:
                          #Set the result status of execution
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 8: Revert the UPLOAD_LOGS_VAL_DCM to %s" %default;
                          print "EXPECTED RESULT 8 : Should revert the UPLOAD_LOGS_VAL_DCM to previous";
                          print "ACTUAL RESULT 8:Revert success";
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";
                          #rebooting the device to stop the running process
                          print "**Device is going for a reboot to stop the running process as a part of revert operation **";
                          obj.initiateReboot();
                          sleep(300);

                          tdkTestObj = obj.createTestStep('ExecuteCmd');
                          cmd= "pidof cpuprocanalyzer";
                          expectedresult="SUCCESS";
                          tdkTestObj.addParameter("command",cmd);
                          tdkTestObj.executeTestCase(expectedresult);
                          actualresult = tdkTestObj.getResult();
                          details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                          if expectedresult in actualresult and details == "":
                             #Set the result status of execution
                             tdkTestObj.setResultStatus("SUCCESS");
                             print "TEST STEP 9:Check if cpuprocanalyzer process is running";
                             print "EXPECTED RESULT 9 : cpuprocanalyzer process should not be running";
                             print "ACTUAL RESULT 9: ",details;
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] : SUCCESS";
                          else:
                             #Set the result status of execution
                             tdkTestObj.setResultStatus("FAILURE");
                             print "TEST STEP 9:Check if cpuprocanalyzer process is running";
                             print "EXPECTED RESULT 9 : cpuprocanalyzer process should not be running";
                             print "ACTUAL RESULT 9: ",details;
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] : FAILURE";
                       else:
                           #Set the result status of execution
                           tdkTestObj.setResultStatus("FAILURE");
                           print "TEST STEP 8: Revert the UPLOAD_LOGS_VAL_DCM to %s" %default;
                           print "EXPECTED RESULT 8 : Should revert the UPLOAD_LOGS_VAL_DCM to previous";
                           print "ACTUAL RESULT 8:Revert failed";
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 7: Disable the CPUProcAnalyzer";
                       print "EXPECTED RESULT 7:Should disable the CPUProcAnalyzer";
                       print "ACTUAL RESULT 7:",details
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                 else:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 5: Enable CPUProc Analyzer";
                     print "EXPECTED RESULT 5: Should enable CPUProc Analyzer";
                     print "ACTUAL RESULT 5:",details
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4: Check if  UPLOAD_LOGS_VAL_DCM is true";
                  print "EXPECTED RESULT 4: Should get the UPLOAD_LOGS_VAL_DCM as true";
                  print "ACTUAL RESULT 4: UPLOAD_LOGS_VAL_DCM  status is:",details
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Set the UPLOAD_LOGS_VAL_DCM to true";
               print "EXPECTED RESULT 3 : Should set the UPLOAD_LOGS_VAL_DCM value to true";
               print "ACTUAL RESULT 3:",details
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the UPLOAD_LOGS_VAL_DCM value";
           print "EXPECTED RESULT 2: Should get the UPLOAD_LOGS_VAL_DCM value";
           print "ACTUAL RESULT 2: UPLOAD_LOGS_VAL_DCM  status is:",default
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the CPUProc Analyzer Enable status";
        print "EXPECTED RESULT 1: Should get the CPUProc Analyzer Enable status";
        print "ACTUAL RESULT 1: CPUProc Analyzer Enable status is:",details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj1.unloadModule("tdkbtr181");
    obj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
