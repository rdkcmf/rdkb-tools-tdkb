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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_2.4GHZ_PublicWiFi_GetModesSupported</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get Device.WiFi.AccessPoint.5.Security.ModesSupported and check whether it is in supported modes</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>4</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_60</test_case_id>
    <test_objective>Get Device.WiFi.AccessPoint.5.Security.ModesSupported and check whether it is in supported modes</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.5.Security.ModesSupported</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Using WIFIAgent_Get, get Device.WiFi.AccessPoint.5.Security.ModesSupported
3. Check if it is in supported modes or not
</automation_approch>
    <expected_output>Device.WiFi.AccessPoint.5.Security.ModesSupported should return supported modes</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHZ_PublicWiFi_GetModesSupported</test_script>
    <skipped>No</skipped>
    <release_version>M58</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHZ_PublicWiFi_GetModesSupported');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
   obj.setLoadModuleStatus("SUCCESS");

   #Get the modes supported for 2.4GHZ public wifi
   tdkTestObj = obj.createTestStep('WIFIAgent_Get');
   tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.5.Security.ModesSupported")
   expectedresult = "SUCCESS"
   tdkTestObj.executeTestCase(expectedresult);
   actualresult = tdkTestObj.getResult();
   details = tdkTestObj.getResultDetails();
   Mode = details.split("VALUE:")[1].split(' ')[0].split(',');
   expectedModes = ["None", "WEP-64", "WEP-128", "WPA-Personal","WPA2-Personal","WPA-WPA2-Personal","WPA-Enterprise","WPA2-Enterprise","WPA-WPA2-Enterprise","WPA3-Personal","WPA3-Enterprise","WPA3-Personal-Transition"]

   #Check if the get modes are all available in expectedModes
   result =  all(elem in expectedModes for elem in Mode)
   if result and expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 3: Get the modes supported";
        print "EXPECTED RESULT 3: Should get the supported Modes";
        print "ACTUAL RESULT 3: Supported Mode is %s" %Mode;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
   else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 3: Get the modes supported";
        print "EXPECTED RESULT 3: Should get the supported Modes";
        print "ACTUAL RESULT 3: Supported Mode is %s" %Mode;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
   obj.unloadModule("wifiagent");

else:
   print "Failed to load wifi module";
   obj.setLoadModuleStatus("FAILURE");
   print "Module loading failed";


