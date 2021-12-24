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
  <version>2</version>
  <name>TS_PAM_SetValidValues_WEBUI</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the valid values for WEBUI Enable feature and verify the same with syscfg.</synopsis>
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
    <test_objective>To set the valid values for WEBUI Enable feature and verify the same with syscfg</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current WEBUI feature Enable value
3.Set the possible value ie, Enable,Disable,MSOonly which confer to syscfg values as 1,0,2 respectively
4.Validate if the set and get are success
5.Revert the set value
6.Unload the module </automation_approch>
    <expected_output>The set operation to all possible values should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_SetValidValues_WEBUI</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_PAM_SetValidValues_WEBUI');
pamObj.configureTestCase(ip,port,'TS_PAM_SetValidValues_WEBUI');

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper):
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the  WEBUI tr181 configuration"
       print "EXPECTED RESULT 1: Should get the  WEBUI tr181 configuration";
       print "ACTUAL RESULT 1: WEBUI tr181 configuration:",default;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       ConfigValues =["Enable","Disable","MSOonly"];
       # getting length of list
       length = len(ConfigValues);
       flag = 0;
       equalflag = 0;
       print "Trying to Set the  WEBUI tr181 configuration to the following:",ConfigValues;

       for i in range(length):
           print "Setting  WEBUI tr181 configuration to ",ConfigValues[i];

           tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
           tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable")
           tdkTestObj.addParameter("ParamValue",str(ConfigValues[i]));
           tdkTestObj.addParameter("Type","string");
           expectedresult="SUCCESS";

           #Execute testcase on DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           Setresult = tdkTestObj.getResultDetails();

           flag = 0;
           equalflag = 0;
           SetValue = ConfigValues[i];

           if expectedresult in actualresult:
              flag =0;
              print " Value set successfully to ",SetValue;

              tdkTestObj = sysObj.createTestStep('ExecuteCmd');
              cmd= "syscfg get WebUIEnable";
              expectedresult="SUCCESS";
              tdkTestObj.addParameter("command",cmd);
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
              syscfgGet = details.strip().replace("\\n", "");

              print "Value configured for WEBUI param via Syscfg is:",syscfgGet
              print "Value configured for WEBUI param set using tr-181 parameter :",SetValue

              if syscfgGet == "0":
                  checkValue = "Disable";
              elif syscfgGet == "1":
                    checkValue = "Enable";
              else:
                  checkValue ="MSOonly";

              if expectedresult in actualresult and checkValue  == SetValue:
                 equalflag =0;
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "[TEST EXECUTION RESULT] : SUCCESS, Set and syscfg  O/P are same";
              else:
                  equalflag =1
                  tdkTestObj.setResultStatus("FAILURE");
                  print "[TEST EXECUTION RESULT] : FAILURE, Set and syscfg  O/P not same";
                  break;
           else:
                flag =1;
                break;

       if flag == 0 and equalflag == 0:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Set the  WEBUI tr181 configuration to:",ConfigValues,"and check if the value set via tr181 and syscfg get WebUIEnable are same ";
          print "EXPECTED RESULT 2: Should set the WEBUI tr181 configuration to:",ConfigValues,"and check if the value set via tr181 and syscfg get WebUIEnable are same "
          print "ACTUAL RESULT 2:  WEBUI tr181 configuration set successfully";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
            #Set the result status of execution
            print "TEST STEP 2: Set the  WEBUI tr181 configuration to:",ConfigValues,"and check if the value set via tr181 and syscfg get WebUIEnable are same ";
            print "EXPECTED RESULT 2: Should set the WEBUI tr181 configuration to:",ConfigValues,"and check if the value set via tr181 and syscfg get WebUIEnable are same "
            print "ACTUAL RESULT 2:  WEBUI tr181 configuration set failed for",SetValue;
            tdkTestObj.setResultStatus("FAILURE");
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

       #Revert the value
       tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WebUI.Enable");
       tdkTestObj.addParameter("ParamValue",default);
       tdkTestObj.addParameter("Type","string");
       expectedresult="SUCCESS";
       #Execute testcase on DUT
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       result = tdkTestObj.getResultDetails();

       if expectedresult in  expectedresult:
          #Set the result status of execution
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 3: Revert  WEBUI tr181 configuration to its default";
          print "EXPECTED RESULT 3: Revert  WEBUI tr181 configuration to previous value";
          print "ACTUAL RESULT 3: Revert Operation sucesss:",result ;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
          #Set the result status of execution
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 3: Revert  WEBUI tr181 configuration to its default";
          print "EXPECTED RESULT 3: Revert  WEBUI tr181 configuration to previous value";
          print "ACTUAL RESULT 3: Revert Operation failed:",result ;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the  WEBUI tr181 configuration";
        print "EXPECTED RESULT 1: Should get the  WEBUI tr181 configuration";
        print "ACTUAL RESULT 1: WEBUI tr181 configuration",default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
    pamObj.unloadModule("pam");

else:
    print "Failed to load sysutil/pam  module";
    sysObj.setLoadModuleStatus("FAILURE");
    pamObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
