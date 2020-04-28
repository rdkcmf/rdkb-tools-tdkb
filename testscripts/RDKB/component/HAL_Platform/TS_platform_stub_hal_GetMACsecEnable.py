#########################################################################
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
  <name>TS_platform_stub_hal_GetMACsecEnable</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_GetMACsecEnable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the platfrom HAL API platform_hal_GetMACsec Enable by passing the NULL value</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_HAL_Platform_45</test_case_id>
    <test_objective>To get the MACsec  Enable Status using platform_hal_GetMACsecEnable() by passing a NULL value.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Device under test should have ethwan setup.</pre_requisite>
    <api_or_interface_used>platform_hal_GetMACsecEnable()</api_or_interface_used>
    <input_parameters>ethport- Give the Ethernet port number
index - indicates negative or positive scenario.
</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_hal_GetMACsecEnable() by passing the index value as 1 for negative scenario validation.
3. The Get operation should fail for the NULL value.
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>Get operation should fail for the NULL value.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFROM</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetMACsecEnable</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

# component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetMACsecEnable');
obj1.configureTestCase(ip,port,'TS_platform_stub_hal_GetMACsecEnable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    #Get the default value from properties file
    tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
    cmd = "sh %s/tdk_utility.sh parseConfigFile ETHWAN_ETH_PORT" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj1.addParameter("command", cmd);
    tdkTestObj1.executeTestCase(expectedresult);
    actualresult = tdkTestObj1.getResult();
    details = ""
    details = tdkTestObj1.getResultDetails().strip();
    ethPort = ""
    ethPort = details.replace("\\n", "");
    print" ETHWAN ETHERNET PORT:",ethPort
    if ethPort != "" and ( expectedresult in  actualresult):
       tdkTestObj1.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the ETHERNET PORT  from  tdk_platform properties file";
       print "EXPECTED RESULT 1: Should Get the default ETHERNET PORT form tdk_platfrom properties file";
       print "ACTUAL RESULT 1: The ETHERNET PORT from tdk_pltaform properties file : %s" % ethPort;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS"

       tdkTestObj = obj.createTestStep("platform_stub_hal_GetMACsecEnable");
       tdkTestObj.addParameter("ethPort",int(ethPort));
       #indicates negative scenario
       flag = 1;
       tdkTestObj.addParameter("index",flag);
       expectedresult="FAILURE";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       MACsecState= tdkTestObj.getResultDetails();
       print "MACsec Enable status is %s"%MACsecState;

       if expectedresult in  actualresult:
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Retrieve the GetMACsecEnable by passing NULL value";
          print "EXPECTED RESULT 2: Should not retrive the  GetMACsecEnable successfully by passing NULL value";
          print "ACTUAL RESULT 2: GetMACsecEnable is : %s" %MACsecState;
          print "[TEST EXECUTION RESULT] :SUCCESS";

       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Retrieve the GetMACsecEnable by passing NULL value";
           print "EXPECTED RESULT 2: Should not retrive the  GetMACsecEnable successfully by passing NULL value";
           print "ACTUAL RESULT 2: GetMACsecEnable is : %s" %MACsecState;
           print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        tdkTestObj1.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the ETHERNET PORT  from  tdk_platform properties file";
        print "EXPECTED RESULT 1: Should Get the default ETHERNET PORT form tdk_platfrom properties file";
        print "ACTUAL RESULT 1: Failed to get ETHERNET PORT from tdk_pltaform properties file : %s" % ethPort;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("halplatform");
    obj1.unloadModule("sysutil");

else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

