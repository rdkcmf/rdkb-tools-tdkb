##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_WIFIAGENT_5GHZ_ChannelBandwidth</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if OperatingChannelBandwidth value is in the enumeration list 20MHz, 40MHz, 80MHz, 160MHz, Auto</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIAGENT_30</test_case_id>
    <test_objective>Check if OperatingChannelBandwidth value is in the enumeration list 20MHz, 40MHz, 80MHz, 160MHz, Auto</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.WiFi.Radio.2.OperatingChannelBandwidth</input_parameters>
    <automation_approch>1. Load wifiagent module
2.Using WIFIAgent_Get, get value of Device.WiFi.Radio.2.OperatingChannelBandwidth
3. Check if operating channel bandwidth retreived is from the list {"20MHz,40MHz,80MHz,160MHz,Auto"}
4. Unload wifiagent module</automation_approch>
    <except_output>OperatingChannelBandwidth should be a value from the list {"20MHz,40MHz,80MHz,160MHz,Auto"}</except_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHZ_ChannelBandwidth</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHZ_ChannelBandwidth');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Get the list of supported security modes
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.OperatingChannelBandwidth")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    expectedBandwidth = "20MHz,40MHz,80MHz,160MHz,Auto"
    expectedBandwidth = expectedBandwidth.split(',');
    bandwidth = details.split("VALUE:")[1].split(' ')[0]
    flag = 0;

    for index in range(len(expectedBandwidth)):
        if bandwidth in expectedBandwidth[index]:
            flag = 1;
	    break;

    if expectedresult in actualresult and flag == 1:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of operating channel bandwidth"
        print "EXPECTED RESULT 1: operating channel bandwidth should be from the expected list of values"
        print "ACTUAL RESULT 1: bandwidth is %s " %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the list of operating channel bandwidth"
        print "EXPECTED RESULT 1: operating channel bandwidth should be from the expected list of values"

        print "ACTUAL RESULT 1: bandwidth is %s " %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");

else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

