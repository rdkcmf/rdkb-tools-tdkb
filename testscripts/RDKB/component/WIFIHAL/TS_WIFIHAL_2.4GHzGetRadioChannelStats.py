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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzGetRadioChannelStats</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioChannelStats</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>This test script is to find the radichannelstats of wifi_getRadioChannelStats() of 2.4ghz</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_315</test_case_id>
    <test_objective>This test script is to find the radichannelstats of wifi_getRadioChannelStats() of 2.4ghz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioChannelStats()</api_or_interface_used>
    <input_parameters>methodName =getRadioChannelStats
radioIndex = 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the radio channel stats of wifihal
3. Unload wifihal module</automation_approch>
    <except_output>It should return the wifihal radiochannel stats</except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetRadioChannelStats</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioChannelStats');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else: 

	    #Prmitive test case which is associated to this Script
	    tdkTestObj = obj.createTestStep('WIFIHAL_GetRadioChannelStats');
	    tdkTestObj.addParameter("radioIndex",idx);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();

	    if expectedresult in actualresult :
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP : Get the Radio Channel Stats info"
		print "EXPECTED RESULT : Should successfully get the Radio Channel Stats info"
		print "ACTUAL RESULT : Successfully got the Radio Channel Stats info"
		print "Details: %s"%details
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP : Get the Radio Channel Stats info"
		print "EXPECTED RESULT : Should successfully get the Radio Channel Stats info"
		print "ACTUAL RESULT : Failed to get the Radio Channel Stats info"
		print "Details: %s"%details
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
