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
  <name>TS_PAM_SetRabidLogLevelError</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the Rabid logging level to error and verify.</synopsis>
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
    <test_case_id>TC_PAM_225</test_case_id>
    <test_objective>To set the Rabid logging level to error and verify </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.LogLevel</input_parameters>
    <automation_approch>1.Load the module
2.Get the current rabid log level
3.Set the log level to  Error
4.Verify the same with CUJO get api
5.Check the same logged in agent.txt with log message "to LogLevel-1"
6.if all the conditions are satisfied mark script as success else mark as failure
7.Revert the set value
8.Unload the module</automation_approch>
    <expected_output>with change in rabid log level same has to be reflected in agent.txt log file and with cujo get api</expected_output>
    <priority>High</priority>
    <test_stub_interface>M95</test_stub_interface>
    <test_script>TS_PAM_SetRabidLogLevelError</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
from tdkbVariables import *;
from time import sleep;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_PAM_SetRabidLogLevelError');
pamObj.configureTestCase(ip,port,'TS_PAM_SetRabidLogLevelError');

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper()):
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.LogLevel")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Finger Print Log Level"
       print "EXPECTED RESULT 1: Should get the Finger Print Log Level";
       print "ACTUAL RESULT 1:Finger Print Log Level:",default;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       print "TEST STEP 2: Setting Finger print log level to Error";
       tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.LogLevel")
       tdkTestObj.addParameter("ParamValue","1");
       tdkTestObj.addParameter("Type","unsignedint");
       expectedresult="SUCCESS";
       #Execute testcase on DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details= tdkTestObj.getResultDetails();
       if expectedresult in actualresult:
           tdkTestObj.setResultStatus("SUCCESS");
           print "EXPECTED RESULT 2 :  Set operation for log level is expected to be success";
           print "ACTUAL RESULT 2 : %s " %details
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";

           sleep(10);
           tdkTestObj = sysObj.createTestStep('ExecuteCmd');
           expectedresult="SUCCESS";
           cmd= "cat /rdklogs/logs/agent.txt | grep -i \"to LogLevel-1\""
           tdkTestObj.addParameter("command",cmd);
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
           if expectedresult in actualresult  and "LogLevel-1" in details:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 3 : Check for log level change in agent log file";
               print "EXPECTED RESULT 3 : should log change in log file";
               print "ACTUAL RESULT :%s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";

               tdkTestObj = sysObj.createTestStep('ExecuteCmd');
               path= "sh %s/tdk_utility.sh parseConfigFile CUJO_GET" %TDK_PATH;
               print path;
               expectedresult="SUCCESS";
               tdkTestObj.addParameter("command", path);
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               CUJO_GET = tdkTestObj.getResultDetails().strip().replace("\\n","")
               if expectedresult in actualresult and CUJO_GET!="":
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 4: Get the cujo get api ";
                   print "EXPECTED RESULT 4: Should Get the cujo get api ";
                   print "ACTUAL RESULT 4: get api is  : %s" %CUJO_GET;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS"

                   tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                   cmd= "%s" %CUJO_GET;
                   expectedresult="SUCCESS";
                   tdkTestObj.addParameter("command",cmd);
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                   if expectedresult in actualresult and details  == "1":
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "TEST STEP 5 : Get the log level set with cujo api";
                       print "EXPECTED RESULT 5: should get log level as 1 for Error log level";
                       print "ACTUAL RESULT 5:%s" %details;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : SUCCESS";
                   else:
                       #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5 : Get the log level set with cujo api";
                        print "EXPECTED RESULT 5 : should get log level as 1 for Error log level";
                        print "ACTUAL RESULT 5 :%s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "TEST STEP 4: Get the cujo get api ";
                   print "EXPECTED RESULT 4: Should Get the cujo get api ";
                   print "ACTUAL RESULT 4: get api is  : %s" %CUJO_GET;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT]: FAILURE"
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3 : Check for log level change in agent log file";
               print "EXPECTED RESULT 3 : should log change in log file";
               print "ACTUAL RESULT :%s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "EXPECTED RESULT 2 :  Set operation for log level is expected to be success";
           print "ACTUAL RESULT 2 : %s " %details
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";

       #Revert the value
       tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_DeviceFingerPrint.LogLevel");
       tdkTestObj.addParameter("ParamValue",default);
       tdkTestObj.addParameter("Type","unsignedint");
       expectedresult="SUCCESS";
       #Execute testcase on DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       result = tdkTestObj.getResultDetails();

       if expectedresult in  expectedresult:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 6: Revert Finger Print Log Level to its default";
          print "EXPECTED RESULT 6: Revert Finger Print Log Level to previous value";
          print "ACTUAL RESULT 6: Revert Operation success:",result ;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
          #Set the result status of execution
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 6: Revert Finger Print Log Level to its default";
          print "EXPECTED RESULT 6: Revert Finger Print Log Level to previous value";
          print "ACTUAL RESULT 6: Revert Operation failed:",result ;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Finger Print Log Level";
        print "EXPECTED RESULT 1: Should get the Finger Print Log Level";
        print "ACTUAL RESULT 1:Finger Print Log Level",default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
    pamObj.unloadModule("pam");

else:
    print "Failed to load sysutil/pam  module";
    sysObj.setLoadModuleStatus("FAILURE");
    pamObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
