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
  <name>TS_PAM_DisableWEBUI</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To test the Disable feature for WEBUI Enable tr181 parameter.</synopsis>
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
    <test_case_id>TC_PAM_238</test_case_id>
    <test_objective>To test the Disable feature for WEBUI Enable tr181 parameter</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable
Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current http enable status and enable it
3.Now Disable the WEBUI feature enable parameter
4.This set should cause http enable to be disabled
5.verify the same and print the result status accordingly
6.Revert the set values
7.Unload the module</automation_approch>
    <expected_output>With WEBUI feature being disabled , http should also be disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_DisableWEBUI</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
import tdklib;
from tdkbVariables import *;
from time import sleep;
#Test component to be tested
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamObj.configureTestCase(ip,port,'TS_PAM_DisableWEBUI');
#Get the result of connection with test component and DUT
loadmodulestatus =pamObj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper():

    #Set the result status of execution
    pamObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable")
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails().strip();


    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName" ,"Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable")
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj.getResult();
    defHttp = tdkTestObj.getResultDetails().strip();

    if expectedresult in (actualresult and actualresult1):
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the current WEBUI config and http enable status"
       print "EXPECTED RESULT 1: Should get the WEBUI config and http enable status";
       print "ACTUAL RESULT 1: WEBUI config is :%s  , HTTP enable status is %s"%(default,defHttp);
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       revertflag =0;
       print "TEST STEP 2: Check  if Remote Access Http Enable status is true else enable it";
       if defHttp != "true":
           tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
           tdkTestObj.addParameter("ParamName","Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable")
           tdkTestObj.addParameter("ParamValue","true");
           tdkTestObj.addParameter("Type","bool");
           expectedresult="SUCCESS";
           #Execute testcase on DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details= tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
               revertflag=1;
               tdkTestObj.setResultStatus("SUCCESS");
               print "EXPECTED RESULT 2 :  Enabling Remote Access Http Enable status is success";
               print "ACTUAL RESULT 2 : %s " %details
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "EXPECTED RESULT 2 :  Enabling Remote Access Http Enable status failed";
               print "ACTUAL RESULT 2 : %s " %details
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";

       tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
       tdkTestObj.addParameter("ParamName" ,"Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable")
       expectedresult="SUCCESS";
       #Execute the test case in DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult1 = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip();
       if expectedresult in actualresult and details=="true":
           print " Remote Access Http Enable status is now true";

           tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
           tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable")
           tdkTestObj.addParameter("ParamValue","Disable");
           tdkTestObj.addParameter("Type","string");
           expectedresult="SUCCESS";
           #Execute testcase on DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details= tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 3 : Set the WEBUI enable status to Disable";
               print "EXPECTED RESULT 3 : should set the WEBUI enable status to Disable";
               print "ACTUAL RESULT :%s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";

               sleep(10);

               tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
               tdkTestObj.addParameter("ParamName" ,"Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable")
               expectedresult="SUCCESS";
               #Execute the test case in DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult1 = tdkTestObj.getResult();
               details= tdkTestObj.getResultDetails().strip();
               if expectedresult in actualresult1 and details == "false":
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 4:Check if Remote Access Http Enable is disabled  after WEBUI being disabled"
                   print "EXPECTED RESULT 4: Should get Remote Access Http Enable as  disabled after WEBUI being disabled";
                   print "ACTUAL RESULT 4:%s"%details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "TEST STEP 4:Check if Remote Access Http Enable is disabled  after WEBUI being disabled"
                   print "EXPECTED RESULT 4: Should get Remote Access Http Enable as  disabled after WEBUI being disabled";
                   print "ACTUAL RESULT 4:%s"%details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : FAILURE";

               tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
               tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable")
               tdkTestObj.addParameter("ParamValue",default);
               tdkTestObj.addParameter("Type","string");
               expectedresult="SUCCESS";
               #Execute testcase on DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               details= tdkTestObj.getResultDetails();
               if expectedresult in actualresult:
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 5: Revert the WEBUI enable feature";
                   print "EXPECTED RESULT 5: Revert operation should be successful";
                   print "ACTUAL RESULT 5: %s"%details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "TEST STEP 5: Revert the  WEBUI enable feature";
                   print "EXPECTED RESULT 5: Revert operation should be successful";
                   print "ACTUAL RESULT 5: %s"%details;
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3 : Set the WEBUI enable status to Disable";
               print "EXPECTED RESULT 3 : should set the WEBUI enable status to Disable";
               print "ACTUAL RESULT :%s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
       else:
            tdkTestObj.setResultStatus("FAILURE");
            print "EXPECTED RESULT 2 :  Enabling Remote Access Http Enable status failed";
            print "ACTUAL RESULT 2 : %s " %details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

       if revertflag==1:
           tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
           tdkTestObj.addParameter("ParamName","Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable")
           tdkTestObj.addParameter("ParamValue",defHttp);
           tdkTestObj.addParameter("Type","bool");
           expectedresult="SUCCESS";
           #Execute testcase on DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details= tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 6: Revert the  Remote Access Http Enable status"
               print "EXPECTED RESULT 6: Revert operation should be successful";
               print "ACTUAL RESULT 6: %s"%details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 6: Revert the  Remote Access Http Enable status"
               print "EXPECTED RESULT 6: Revert operation should be successful";
               print "ACTUAL RESULT 6: %s"%details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current WEBUI config and http enable status"
        print "EXPECTED RESULT 1: Should get the WEBUI config and http enable status";
        print "ACTUAL RESULT 1: WEBUI config is :%s  , HTTP enable status is %s"%(default,defHttp);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamObj.unloadModule("pam");
else:
    print "Failed to load pam  module";
    pamObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
