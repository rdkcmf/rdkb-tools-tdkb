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
  <version>1</version>
  <name>TS_platform_stub_hal_SetFactoryCmVariant</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_setFactoryCmVariant</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the set and get functionality of  Factory Cm Variant</synopsis>
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
    <test_case_id>TC_HAL_Platform_39</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_To validate Platform HAL API platform_hal_setFactoryCmVariant() and  platform_hal_getFactoryCmVariant()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_setFactoryCmVariant()   platform_hal_getFactoryCmVariant()</api_or_interface_used>
    <input_parameters>CmVarient  value </input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_hal_getFactoryCmVariant() .
3. Check for successful Get.
4. Set the value using platform_hal_setFactoryCmVariant()
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>The set and get functonality should be successfull</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFORM</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetFactoryCmVariant</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetFactoryCmVariant');
obj1.configureTestCase(ip,port,'TS_platform_stub_hal_SetFactoryCmVariant');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):

   obj.setLoadModuleStatus("SUCCESS");
   obj1.setLoadModuleStatus("SUCCESS");

   #Get the initial value
   tdkTestObj = obj.createTestStep("platform_stub_hal_getFactoryCmVariant");
   expectedresult="SUCCESS";
   tdkTestObj.executeTestCase(expectedresult);
   actualresult = tdkTestObj.getResult();
   InitialCmVariant  = tdkTestObj.getResultDetails();
   if expectedresult in actualresult and InitialCmVariant != "":
      tdkTestObj.setResultStatus("SUCCESS");
      print "TEST STEP 1: Retrieve the platform_hal_getFactoryCmVariant";
      print "EXPECTED RESULT 1: Should retrieve the platform_hal_getFactoryCmVariant successfully";
      print "ACTUAL RESULT 1: %s" %InitialCmVariant;
      print "[TEST EXECUTION RESULT] : %s" %actualresult;

      tdkTestObj = obj.createTestStep("platform_stub_hal_setFactoryCmVariant");
      CmVariant="pc20"
      tdkTestObj.addParameter("CmVarient",CmVariant);
      expectedresult = "SUCCESS";
      tdkTestObj.executeTestCase(expectedresult);
      actualresult = tdkTestObj.getResult();
      SetCmVariant = tdkTestObj.getResultDetails();

      if expectedresult in  actualresult :
         tdkTestObj.setResultStatus("SUCCESS");
         print "TEST STEP 2: Set the CmVariant using  platform_hal_SetFactoryCmVariant";
         print "EXPECTED RESULT 2: Should set the CmVariant using  platform_hal_SetFactoryCmVariant successfully";
         print "ACTUAL RESULT 2: %s" %SetCmVariant;
         print "[TEST EXECUTION RESULT] : %s" %actualresult;

         tdkTestObj = obj.createTestStep("platform_stub_hal_getFactoryCmVariant");
         expectedresult="SUCCESS";
         tdkTestObj.executeTestCase(expectedresult);
         actualresult = tdkTestObj.getResult();
         GetCmVariant  = tdkTestObj.getResultDetails();
         if expectedresult in actualresult and GetCmVariant == CmVariant:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Check wether Set and get value for FactoryCmVariant are equal";
            print "EXPECTED RESULT 3: Set and get value for FactoryCmVariant should be equal";
            print "ACTUAL RESULT 3: Set and get value for FactoryCmVariant are equal"
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Revert the value to intial
            tdkTestObj = obj.createTestStep("platform_stub_hal_setFactoryCmVariant");
            tdkTestObj.addParameter("CmVarient",InitialCmVariant);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in  actualresult :
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 4: Revert  the CmVariant to  Initial  using  platform_hal_SetFactoryCmVariant";
               print "EXPECTED RESULT 4: Should revert the CmVariant to initial using  platform_hal_SetFactoryCmVariant successfully";
               print "ACTUAL RESULT 4: %s" %details;
               print "[TEST EXECUTION RESULT] : %s" %actualresult;

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Revert  the CmVariant to  Initial  using  platform_hal_SetFactoryCmVariant";
                print "EXPECTED RESULT 4: Should revert the CmVariant to initial using  platform_hal_SetFactoryCmVariant successfully";
                print "ACTUAL RESULT 4: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
         else:
             tdkTestObj.setResultStatus("FAILURE");
             print "TEST STEP 3: Check wether Set and get value for FactoryCmVariant are equal";
             print "EXPECTED RESULT 3: Set and get value for FactoryCmVariant should be equal";
             print "ACTUAL RESULT 3: Set and get value for FactoryCmVariant are not equal"
             print "[TEST EXECUTION RESULT] : FAILURE";

      else:
          tdkTestObj.setResultStatus("FAILURE");
          print "TEST STEP 2: Set the CmVariant using  platform_hal_SetFactoryCmVariant";
          print "EXPECTED RESULT 2: Should set the CmVariant using  platform_hal_SetFactoryCmVariant successfully";
          print "ACTUAL RESULT 2: %s" %SetCmVariant;
          print "[TEST EXECUTION RESULT] : %s" %actualresult;
   else:
       print "TEST STEP 1: Retrieve the platform_hal_getFactoryCmVariant";
       print "EXPECTED RESULT 1: Should retrieve the platform_hal_getFactoryCmVariant successfully";
       print "ACTUAL RESULT 1: %s" %InitialCmVariant;
       print "[TEST EXECUTION RESULT] : %s" %actualresult;


   obj.unloadModule("halplatform");
   obj1.unloadModule("sysutil");
else:
    print "Failed to load the module sysutil/halplatform";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

