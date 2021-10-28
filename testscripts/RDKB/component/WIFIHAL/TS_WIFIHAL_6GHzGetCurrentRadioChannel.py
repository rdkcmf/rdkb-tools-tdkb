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
  <name>TS_WIFIHAL_6GHzGetCurrentRadioChannel</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test if channel no: returned by wifi_getRadioChannel() is a subset of wifi_getRadioChannelsInUse() output.</synopsis>
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
    <test_case_id>TC_WIFIHAL_604</test_case_id>
    <test_objective>Test if channel no: returned by wifi_getRadioChannel() is a subset of wifi_getRadioChannelsInUse() output</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Boradband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioChannel()
wifi_getRadioChannelsInUse()</api_or_interface_used>
    <input_parameters>methodName : getRadioChannelsInUse
methodName : getRadioChannel</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioChannel() to find the current radio channel
3.Get the list of cahnnels in use using wifi_getRadioChannelsInUse() api
4.Check if current channel is a available in channelsInUse list
5. Unload wifihal module</automation_approch>
    <expected_output>current channel should be available in channelsInUse list</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetCurrentRadioChannel</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetCurrentRadioChannel');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            #Giving the method name to invoke the api for getting Radio Channel in use. ie,wifi_getRadioChannelsInUse()
            tdkTestObj.addParameter("methodName","getRadioChannelsInUse");
            tdkTestObj.addParameter("radioIndex",idx);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Get the Radio channel in use  for 6GHz";
                print "EXPECTED RESULT 1: Should get the Radio channel in use for 6GHz";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                channelInUse= details.split(":")[1];

                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                #Giving the method name to invoke the api for getting Radio Channel. ie,wifi_getRadioChannel()
                tdkTestObj.addParameter("methodName","getRadioChannel");
                tdkTestObj.addParameter("radioIndex",idx);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult :
                    #Set the result status of execution
                    print "TEST STEP 1: Get the Radio channel for 6GHz";
                    print "EXPECTED RESULT 1: Should get the Radio channel for 6GHz";
                    print "ACTUAL RESULT 1: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    CurrentChannel= details.split(":")[1];
                    ExpectedList = channelInUse.split(",");
                    if CurrentChannel in ExpectedList :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "SUCCESS: current channel is available in channels in use list"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "FAILURE: current channel is not available in channels in use list"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 1: Get the Radio channel for 6GHz";
                    print "EXPECTED RESULT 1: Should get the Radio channel for 6GHz";
                    print "ACTUAL RESULT 1: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Get the Radio channel in use for 6GHz";
                print "EXPECTED RESULT 1: Should get the Radio channel in use for 6GHz";
                print "ACTUAL RESULT 1: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
