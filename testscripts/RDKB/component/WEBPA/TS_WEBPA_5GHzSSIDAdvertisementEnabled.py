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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>4</version>
  <name>TS_WEBPA_5GHzSSIDAdvertisementEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Check the enable and disable feature  of  5GHz SSID Advertisement.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WEBPA_33</test_case_id>
    <test_objective>Using WEBPA get and set  the state of  5Ghz SSID advertisment</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI, Emulator</test_setup>
    <pre_requisite>If SAT token is to be used, token should be created and made available in test manager. Also the config variables SAT_REQUIRED, SAT_TOKEN_FILE, SERVER_URI should be updated in webpaVariables.py</pre_requisite>
    <api_or_interface_used>webpaQuery
parseWebpaResponse
webpaPreRequisite</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled</input_parameters>
    <automation_approch>1. Load sysutil module
2. Configure WEBPA server to send get request for Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled.
3. Parse the WEBPA response
4. Using sysutil ExecuteCmd command get the current state 
5. If webpa response status is SUCCESS, get operation was success otherwise failure
6. Toggle the value using set based on the response received.
7. Using sysutil ExecuteCmd command set the state.
8.If webpa response status is SUCCESS, set operation was success otherwise failure.
9.set the value back to original .
10. Unload sysutil module</automation_approch>
    <expected_output>WEBPA response status should be SUCCESS</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_WEBPA_5GHzSSIDAdvertisementEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
import time;
from webpaUtility import *
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBPA_5GHzSSIDAdvertisementEnabled');
#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;
if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:
        #get the current state of SSID advertisent for 5GHz
        print "TEST STEP 1: Get and save the state of SSID Advertisment for 5GHz "
        queryParam = {"name":"Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled"}
        queryResponse = webpaQuery(obj,queryParam)
        parsedResponse = parseWebpaResponse(queryResponse, 1)
        print "parsedResponse : %s" %parsedResponse;
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        #Checking if the response value is not null
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
              tdkTestObj.setResultStatus("SUCCESS");
              print "[TEST EXECUTION RESULT] : SUCCESS"
              OrgValue = parsedResponse[1];
              print "SSID Advertisment for 5GHz's  State: ",OrgValue;
              #toggling by using set
              print "TEST STEP 2: Toggling the value"
              if parsedResponse[1] == "false":
                 flag="true"
                 queryParam = {"name":"Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled","value":flag,"dataType":3}
                 queryResponse = webpaQuery(obj, queryParam,"set")
                 setResponse = parseWebpaResponse(queryResponse, 1,"set")
                 tdkTestObj.executeTestCase("SUCCESS");
              else:
                 flag="false"
                 queryParam = {"name":"Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled","value":flag,"dataType":3}
                 queryResponse = webpaQuery(obj, queryParam,"set")
                 setResponse = parseWebpaResponse(queryResponse, 1,"set")
                 tdkTestObj.executeTestCase("SUCCESS");
              time.sleep(30)
              #getting the set value which is toggled
              print "TEST STEP 3: Getting the toggled value"
              queryParam = {"name":"Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled"}
              queryResponse = webpaQuery(obj, queryParam)
              getResponse = parseWebpaResponse(queryResponse, 1)
              tdkTestObj.executeTestCase("SUCCESS");
              #check for successful set
              if "SUCCESS" in getResponse[0] and getResponse[1] != "" and getResponse[1]== flag:
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "[TEST EXECUTION RESULT] : SUCCESS"
                 Value = parsedResponse[1];
                 print "Ethernet SSID Advertisment for 5GHz State: ",Value;
              else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "[TEST EXECUTION RESULT] : FAILURE"
              #Setting back to original
              print "TEST STEP 4: Setting back to original value"
              queryParam = {"name":"Device.WiFi.AccessPoint.10101.SSIDAdvertisementEnabled","value":OrgValue,"dataType":3}
              queryResponse = webpaQuery(obj, queryParam,"set")
              setResponse = parseWebpaResponse(queryResponse, 1,"set")
              tdkTestObj.executeTestCase("SUCCESS");
              if "SUCCESS" in setResponse[0]:
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 4 [TEST EXECUTION RESULT] : SUCCESS"
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4[TEST EXECUTION RESULT] : FAILURE"
        else:
           tdkTestObj.setResultStatus("FAILURE");
           print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"
    obj.unloadModule("sysutil");
else:
    print "FAILURE to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

