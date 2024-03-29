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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_PAM_CheckNonRootSupportForParodus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if Parodus is running as a non-root user</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_167</test_case_id>
    <test_objective>This test case is to check if Parodus is running as a non-root user</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable</input_parameters>
    <automation_approch>1.Load the tr181 and sysutil module
2.Check the status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable
3.Get the process details of parodus
4.Check if the process is running as non-root user when Non Root Support is enabled and as root when Non Root Support is disabled
5.Unload the Module
</automation_approch>
    <expected_output>When Non Root Support is enabled parodus should run as a non-root user and as root when Non Root Support is disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_CheckNonRootSupportForParodus</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_PAM_CheckNonRootSupportForParodus');
tr181obj.configureTestCase(ip,port,'TS_PAM_CheckNonRootSupportForParodus');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');

    tdkTestObj_Tr181_Get.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable");
    #Execute the test case in DUT
    tdkTestObj_Tr181_Get.executeTestCase(expectedresult);
    actualresult = tdkTestObj_Tr181_Get.getResult();
    details  = tdkTestObj_Tr181_Get.getResultDetails();

    if expectedresult  in actualresult :
       print "TEST STEP 1: Get NonRootSupport enabled  Status";
       print "EXPECTED RESULT 1:Should get the NonRootSupport enabled Status";
       print "ACTUAL RESULT 1: %s" %details;
       print "[TEST EXECUTION RESULT] :SUCCESS";
       tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
       if details == "true":
          print "TEST STEP 2: Check  if NonRootSupport is enabled ";
          print "EXPECTED RESULT 2:NonRootSupport should be enabled ";
          print "ACTUAL RESULT 2: %s" %details;
          print "[TEST EXECUTION RESULT] : SUCCESS";
          tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

          cmd = "ps  | grep -i \"parodus\" | grep -v \"grep\"";
          tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
          tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
          actualresult = tdkTestObj_Sys_ExeCmd.getResult();
          details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");

          if expectedresult  in actualresult and details!= "" and "parodus" in details:
             print "TEST STEP 3: Get the parodus proccess details";
             print "EXPECTED RESULT 3:  Should get the parodus proccess details";
             print "ACTUAL RESULT 3: %s" %details;
             print "[TEST EXECUTION RESULT] : SUCCESS";
             tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

             userType =  details.split(" ")[1].strip().replace("\\n","");
             if userType == "non-root":
                print "TEST STEP 4: Check if the user-type is non-root";
                print "EXPECTED RESULT 4: Should get the user type as non-root";
                print "ACTUAL RESULT 4: %s" %userType;
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
             else:
                 print "TEST STEP 4: Check if the user-type is non-root";
                 print "EXPECTED RESULT 4: Should get the user type as non-root";
                 print "ACTUAL RESULT 4: %s" %userType;
                 print "[TEST EXECUTION RESULT] : FAILURE";
                 tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
          else:
              print "TEST STEP 3: Get the parodus proccess details ";
              print "EXPECTED RESULT 3:  Should get the parodus proccess details";
              print "ACTUAL RESULT 3: %s" %details;
              print "[TEST EXECUTION RESULT] : FAILURE";
              tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
       else:
           print "TEST STEP 2: Check  if NonRootSupport is diabled ";
           print "EXPECTED RESULT 2:NonRootSupport should be disabled ";
           print "ACTUAL RESULT 2: %s" %details;
           print "[TEST EXECUTION RESULT] : SUCCESS";
           tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

           cmd = "ps  | grep -i \"parodus\" | grep -v \"grep\"";
           tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
           tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
           actualresult = tdkTestObj_Sys_ExeCmd.getResult();
           details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");

           if expectedresult  in actualresult and details!= "" and "parodus" in details:
              print "TEST STEP 3: Get the parodus proccess details";
              print "EXPECTED RESULT 3:  Should get the parodus proccess details";
              print "ACTUAL RESULT 3: %s" %details;
              print "[TEST EXECUTION RESULT] : SUCCESS";
              tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

              userType =  details.split(" ")[1].strip().replace("\\n","");
              if userType == "root":
                 print "TEST STEP 4: Check if the user-type is root";
                 print "EXPECTED RESULT 4: Should get the user type as root";
                 print "ACTUAL RESULT 4: %s" %userType;
                 print "[TEST EXECUTION RESULT] : SUCCESS";
                 tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
              else:
                  print "TEST STEP 4: Check if the user-type is root";
                  print "EXPECTED RESULT 4: Should get the user type as root";
                  print "ACTUAL RESULT 4: %s" %userType;
                  print "[TEST EXECUTION RESULT] : FAILURE";
                  tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
           else:
               print "TEST STEP 3: Get the parodus proccess details ";
               print "EXPECTED RESULT 3:  Should get the parodus proccess details";
               print "ACTUAL RESULT 3: %s" %details;
               print "[TEST EXECUTION RESULT] : FAILURE";
               tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1: Get NonRootSupport enabled  Status";
        print "EXPECTED RESULT 1:Should get the NonRootSupport enabled Status";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
