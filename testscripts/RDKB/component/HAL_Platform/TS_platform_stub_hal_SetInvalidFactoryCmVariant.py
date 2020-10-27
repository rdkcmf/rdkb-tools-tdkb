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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_platform_stub_hal_SetInvalidFactoryCmVariant</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_setFactoryCmVariant</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check the set and get functionality of  Factory Cm Variant using an invalid value</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_HAL_Platform_72</test_case_id>
    <test_objective>To check the set and get functionality of  Factory Cm Variant using an invalid value</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_setFactoryCmVariant
platform_hal_getFactoryCmVariant</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  platform_hal module.
2. Get and save the current cmvariant using platform_hal_getFactoryCmVariant()
3. Set an invalid cmvariant using platform_hal_setFactoryCmVariant()
4. Check if set operation returned failure status. If not revert back to the initial cmvariant value
5. Unload platform_hal module
</automation_approch>
    <expected_output>platform_hal_setFactoryCmVariant() should return failure status on setting an invalid cmvariant value</expected_output>
    <priority>High</priority>
    <test_stub_interface>platformhal</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetInvalidFactoryCmVariant</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetInvalidFactoryCmVariant');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
   obj.setLoadModuleStatus("SUCCESS");

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
      CmVariant="dummy"
      tdkTestObj.addParameter("CmVarient",CmVariant);
      expectedresult = "FAILURE";
      tdkTestObj.executeTestCase(expectedresult);
      actualresult = tdkTestObj.getResult();
      SetCmVariant = tdkTestObj.getResultDetails();

      if expectedresult in  actualresult :
         tdkTestObj.setResultStatus("SUCCESS");
         print "TEST STEP 2: Invoke platform_hal_SetFactoryCmVariant() using an invalid value";
         print "EXPECTED RESULT 2: platform_hal_SetFactoryCmVariant() invocation should fail";
         print "ACTUAL RESULT 2: %s" %SetCmVariant;
         print "[TEST EXECUTION RESULT] : SUCCESS";
      else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Invoke platform_hal_SetFactoryCmVariant() using an invalid value";
           print "EXPECTED RESULT 2: platform_hal_SetFactoryCmVariant() invocation should fail";
           print "ACTUAL RESULT 2: %s" %SetCmVariant;
           print "[TEST EXECUTION RESULT] : FAILURE";

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
       print "TEST STEP 1: Retrieve the platform_hal_getFactoryCmVariant";
       print "EXPECTED RESULT 1: Should retrieve the platform_hal_getFactoryCmVariant successfully";
       print "ACTUAL RESULT 1: %s" %InitialCmVariant;
       print "[TEST EXECUTION RESULT] : %s" %actualresult;

   obj.unloadModule("halplatform");
else:
    print "Failed to load the module halplatform";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
