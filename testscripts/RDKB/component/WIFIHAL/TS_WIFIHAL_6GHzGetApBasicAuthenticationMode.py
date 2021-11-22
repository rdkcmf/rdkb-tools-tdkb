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
  <name>TS_WIFIHAL_6GHzGetApBasicAuthenticationMode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the Authentication mode in device for 6GHz radio using wifi_getApBasicAuthenticationMode HAL API and validate the same.</synopsis>
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
    <test_case_id>TC_WIFIHAL_649</test_case_id>
    <test_objective>To set the  Authentication mode in device for 6GHz radio using wifi_getApBasicAuthenticationMode HAL API and validate the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBasicAuthenticationMode()</api_or_interface_used>
    <input_parameters>methodName : getApBasicAuthenticationMode</input_parameters>
    <automation_approch>1.Load the module
2.Get the supported auth modes configured from platform property file
3.perform a get operation for  wifi_ getApBasicAuthenticationMode
4 Check if the received mode is among the configured modes
5.unload the module</automation_approch>
    <expected_output>The received mode from wifi_getApBasicAuthenticationMode is expected to be one among configured modes</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApBasicAuthenticationMode</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
from tdkbVariables import *;
radio2 = "6G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApBasicAuthenticationMode');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApBasicAuthenticationMode');
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, idx = getApIndexfor6G(sysobj, TDK_PATH);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
         sysobj.setLoadModuleStatus("SUCCESS");
         tdkTestObj = sysobj.createTestStep('ExecuteCmd');
         expectedresult="SUCCESS";
         supportedAuthModes = "sh %s/tdk_utility.sh parseConfigFile SUPPORTED_AUTH_MODES" %TDK_PATH;
         tdkTestObj.addParameter("command", supportedAuthModes);
         tdkTestObj.executeTestCase(expectedresult);
         actualresult = tdkTestObj.getResult();
         supportedAuthModes = tdkTestObj.getResultDetails().strip();
         supportedAuthModes = supportedAuthModes.replace("\\n", "");
         if supportedAuthModes and expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            supportedModes = supportedAuthModes.split(",");
            print "**************************************************";
            print "TEST STEP 1: Get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
            print "EXPECTED RESULT 1: Should get the list of supported Authentication Modes";
            print "ACTUAL RESULT 1: Got the list of supported Authentication Modes as %s" %supportedModes;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "**************************************************";
            expectedresult="SUCCESS";
            getMethod = "getApBasicAuthenticationMode"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, "0", getMethod)
            if expectedresult in actualresult :
               tdkTestObj.setResultStatus("SUCCESS");
               receivedMode = details.split(":")[1].strip()
               print "**************************************************";
               print "TEST STEP 2: Get the Ap Basic Authentication mode for 6GHz";
               print "EXPECTED RESULT 2: Should successfully get the Ap Basic Authentication mode for 6GHz";
               print "ACTUAL RESULT 2: Successfully got the Ap Basic Authentication mode as %s for 6GHz"%receivedMode;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
               print "**************************************************";
               if receivedMode in supportedModes:
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "**************************************************";
                  print "TEST STEP 3: To check whether the received Ap Basic Authentication mode is from the list of supported Authentication Modes";
                  print "EXPECTED RESULT 3: The received Ap Basic Authentication mode should be from the list of supported Authentication Modes";
                  print "ACTUAL RESULT 3: The received Ap Basic Authentication mode is from the list of supported Authentication Modes";
                  print "[TEST EXECUTION RESULT] : SUCCESS";
                  print "**************************************************";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "**************************************************";
                   print "TEST STEP 3: To check whether the received Ap Basic Authentication mode is from the list of supported Authentication Modes";
                   print "EXPECTED RESULT 3: The received Ap Basic Authentication mode should be from the list of supported Authentication Modes";
                   print "ACTUAL RESULT 3: The received Ap Basic Authentication mode is NOT from the list of supported Authentication Modes";
                   print "[TEST EXECUTION RESULT] : FAILURE";
                   print "**************************************************";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "**************************************************";
                print "TEST STEP 2: Get the Ap Basic Authentication mode for 6GHz";
                print "EXPECTED RESULT 2: Should successfully get the Ap Basic Authentication mode for 6GHz";
                print "ACTUAL RESULT 2: Failed to get the Ap Basic Authentication mode for 6GHz";
                print details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "**************************************************";
         else:
             tdkTestObj.setResultStatus("FAILURE");
             print "**************************************************";
             print "TEST STEP 1: Get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
             print "EXPECTED RESULT 1: Should get the list of supported Authentication Modes";
             print "ACTUAL RESULT 1: Failed to get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : FAILURE";
             print "**************************************************";
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
