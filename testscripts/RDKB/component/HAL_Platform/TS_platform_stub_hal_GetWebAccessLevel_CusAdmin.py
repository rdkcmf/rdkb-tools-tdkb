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
  <name>TS_platform_stub_hal_GetWebAccessLevel_CusAdmin</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_GetWebAccessLevel</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the Web Access Level for Cus Admin using platform_hal_GetWebAccessLevel API</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>true</skip>
  <box_types>
    <box_type><!--Broadband--></box_type>
    <!--Commenting the box_types as these APIs are not implemented in any platform-->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_77</test_case_id>
    <test_objective>Get the Web Access Level for Cus Admin using platform_hal_GetWebAccessLevel API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_GetWebAccessLevel</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_stub_hal_GetWebAccessLevel(). userIndex = 5 for Cus Admin. The Interface Indices are 1,2,16,40 for Lan, CM, Mta and Wan respectively
3. Get the value
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>Should successfully get the Web Access Levels for CusAdmin using platform_hal_GetWebAccessLevel API</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetWebAccessLevel_CusAdmin</test_script>
    <skipped>Yes</skipped>
    <release_version>M87</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetWebAccessLevel_CusAdmin');
#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
if "SUCCESS" in result.upper():
   obj.setLoadModuleStatus("SUCCESS");
   #Prmitive test case which associated to this Script
   tdkTestObj = obj.createTestStep('platform_stub_hal_GetWebAccessLevel');
   expectedresult ="SUCCESS"
   #For CusAdmin, userIndex = 5
   tdkTestObj.addParameter("userIndex",5);
   #The interfaces are Lan, RfCM, Mta and WanRG : 1,2,16,40 indices respectively
   level_list = ["Lan", "RfCM", "Mta", "WanRG"];
   step = 1
   for i in [1, 2, 16, 40] :
       tdkTestObj.addParameter("ifIndex",i);
       #Execute the test case in DUT
       tdkTestObj.executeTestCase("expectedresult");
       #Get the result of execution
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();
       if expectedresult in actualresult:
           print" TEST STEP %d: Get the WebAccessLevel for %s"%(step, level_list[step-1])
           print" EXPECTED  RESULT %d: Should get the WebAccessLevel Successfully"%step
           print" ACTUAL RESULT %d: %s"%(step, details)
           print "[TEST EXECUTION RESULT] : SUCCESS";
           tdkTestObj.setResultStatus("SUCCESS");
       else:
           print" TEST STEP %d: Get the WebAccessLevel for %s"%(step, level_list[step-1])
           print" EXPECTED  RESULT %d: Should get the WebAccessLevel Successfully"%step
           print" ACTUAL RESULT %d: %s"%(step, details)
           print "[TEST EXECUTION RESULT] : FAILURE";
           tdkTestObj.setResultStatus("FAILURE");
       step = step + 1
   obj.unloadModule("halplatform");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");

