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
  <name>TS_WIFIHAL_GetBandSteeringLog</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetBandSteeringLog</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check for the successful invocation of GetBandSteeringLog</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_357</test_case_id>
    <test_objective>To check for the successful invocation of
wifi_getBandSteeringLog</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringLog</api_or_interface_used>
    <input_parameters>methodName :'WIFIHAL_GetBandSteeringLog
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get the GetBandSteeringLog  using  wifi_getBandSteeringLog API.
3.Return SUCCESS for non empty value,else FAILURE.
4.Unload module.</automation_approch>
    <expected_output>Api should be invoked successfully and the values received from the api should be non empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_GetBandSteeringLog</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import re;
import time;
from wifiUtility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetBandSteeringLog');

#Get the result of connection with test component and DUT

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('WIFIHAL_GetBandSteeringLog');
    tdkTestObj.addParameter("record_index", 0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Details: %s"%details

    if expectedresult in actualresult :
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1:Check for successful invocation of API"
       print "EXPECTED RESULT 1:API should be invoked sucessfully"
       print "ACTUAL RESULT 1: %s"%details
       print "[TEST EXECUTION RESULT] : SUCCESS";
       
       pSteeringTime = details.split(':')[1].split(',')[0].strip()
       pSteeringReason = details.split(':')[2].strip()
       if pSteeringTime and pSteeringReason :
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2:Check for pSteeringTime and  pSteeringReason"
          print "EXPECTED RESULT 2 : Should get   pSteeringTime and  pSteeringReason non empty"
          print "ACTUAL RESULT 2: %s"%details
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Check for pSteeringTime and  pSteeringReason"
           print "EXPECTED RESULT 2 : Should get   pSteeringTime and  pSteeringReason non empty"
           print "ACTUAL RESULT 2 : %s"%details
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Check for successful invocation of wifi_getBandSteeringLog"
        print "EXPECTED RESULT 1 : Should successfully invoke wifi_getBandSteeringLog"
        print "ACTUAL RESULT 1: Failed to invoke wifi_getBandSteeringLog"
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";



    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";





