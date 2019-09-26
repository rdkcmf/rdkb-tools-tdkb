##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_CMHAL_HTTP_Reboot_Now</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_Reboot_Now</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To reboot the device and check if it is rebooted</synopsis>
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
    <test_case_id>TC_CMHAL_77</test_case_id>
    <test_objective>To reboot the device and check if it is rebooted</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_HTTP_Download_Reboot_Now</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Invoke cm_hal_HTTP_Download_Reboot_Now to reboot the device
3. Check if uptime before reboot is greater than uptime after reboot
4. Unload cmhal module</automation_approch>
    <except_output>Device should be rebooted and uptime before reboot is greater than uptime after reboot</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_HTTP_Reboot_Now</test_script>
    <skipped>No</skipped>
    <release_version>M67</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_HTTP_Reboot_Now');
obj1.configureTestCase(ip,port,'TS_CMHAL_HTTP_Reboot_Now');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "STEP 1 :Get the uptime";
        print "EXPECTED RESULT : Should return the uptime successfully";
        print "ACTUAL RESULT :UpTime before reboot is %s" %details;
        #save device's current state before it goes for reboot
        obj1.saveCurrentState();
        tdkTestObj = obj.createTestStep("CMHAL_Reboot_Now");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        rebootdetails = tdkTestObj.getResultDetails();
        
        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 8: Start the reboot";
            print "EXPECTED RESULT 8: Should start the reboot successfully";
            print "ACTUAL RESULT 8: %s" %rebootdetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #Restore the device state saved before reboot
            obj1.restorePreviousStateAfterReboot();

            #checking the uptime after reboot
            tdkTestObj = obj1.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
            #Execute the test case in STB
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            afterdetails = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                if int(details)>=int(afterdetails):
                    print "STEP 2: compare the uptime before and after reboot";
                    print "EXPECTED RESULT :Uptime before reboot should be greater than uptime after reboot";
                    print "UpTime after reboot is %s" %afterdetails;
                    print "Successfully updated the uptime after reboot";

                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "STEP 2: compare the uptime before and after reboot";
                    print "EXPECTED RESULT :Uptime before reboot should be greater than uptime after reboot";
                    print "UpTime after reboot is %s" %afterdetails;
                    print "Failed to update the uptime after reboot"
                    print "[TEST EXECUTION RESULT] :%s" %actualresult;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "STEP 1 :Get the uptime";
            print "EXPECTED RESULT : Should return the uptime successfully";
            print "ACTUAL RESULT :Failed to get the uptime after reboot %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the UpTime";
        print "EXPECTED RESULT 1: Should return the uptime successfully";
        print "ACTUAL RESULT 1: Failed to get the uptime before reboot %s" %details;
        print "[TEST EXECUTION RESULT] : %s" %actualresult;

    obj.unloadModule("cmhal");
    obj1.unloadModule("pam");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");

