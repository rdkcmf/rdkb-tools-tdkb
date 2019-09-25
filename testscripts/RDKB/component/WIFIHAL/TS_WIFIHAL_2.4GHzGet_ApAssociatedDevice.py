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
  <version>19</version>
  <name>TS_WIFIHAL_2.4GHzGet_ApAssociatedDevice</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAssociatedDevice</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the functionality of getApAssociatedDevice() WIFIHAL api.</synopsis>
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
    <test_case_id>TS_WIFIHAL_337</test_case_id>
    <test_objective>Get the List of associated devices mac adresses.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.A wifi client should be connected to the GW while testing</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDevice()</api_or_interface_used>
    <input_parameters>apIndex =  0
methodName = getApAssociatedDevice</input_parameters>
    <automation_approch>1.Load the module.
2.Get the the list of associated devices by invoking wifi_getApAssociatedDevice() API.
4.Unload the module.</automation_approch>
    <expected_output>Should get the list of associated devices for 2.4GHz</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGet_ApAssociatedDevice</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>nil</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;
import re;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGet_ApAssociatedDevice');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    #calling own primitive function
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDevice');
    tdkTestObj.addParameter("apIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Details: ",details    
    if expectedresult in actualresult:
        print "TEST STEP 1: Get the AssociatedDevices"
        print "EXPECTED RESULT 1: Should get the total number of associated devices"
        print "ACTUAL RESULT 1: wifi_getApAssociatedDevices call success"
        print "TEST EXECUTION RESULT :SUCCESS"

        tdkTestObj.setResultStatus("SUCCESS");
        outputList = details.split("=")[1].strip()
        if "," in outputList:
            outputValue = outputList.split(",")[0].strip()
        else:
            outputValue = outputList.split(":Value")[0].strip()

        if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", outputValue.lower()):

            print "TEST STEP 2: Check associated devices MAC"
            print "EXPECTED RESULT 2: Should get the list of associated devices MAC"
            print "ACTUAL RESULT 2: List of Associated Devices MAC:",outputList.split(":Value")[0].strip()
            print "TEST EXECUTION RESULT :SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");
        else:           
            print "TEST STEP 2: Check associated devices MAC"
            print "EXPECTED RESULT 2: Should get the list of associated devices MAC"
            print "ACTUAL RESULT 2: List of Associated Devices:",outputList
            print "No Device Connected or Invalid Format"
            print "TEST EXECUTION RESULT :FAILURE"
            tdkTestObj.setResultStatus("FAILURE");

    else:
        print "TEST STEP 1: Get the AssociatedDevices"
        print "EXPECTED RESULT 1: Should get the total number of associated devices"
        print "ACTUAL RESULT 1: wifi_getApAssociatedDevices call failed"
        print "TEST EXECUTION RESULT :FAILURE"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
