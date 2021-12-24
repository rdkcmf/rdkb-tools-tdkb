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
  <version>2</version>
  <name>TS_WIFIHAL_5GHzGetRadioNumofVaps</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioVapInfoMap</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the Radio number of vaps  for 5G  wifi using wifi_getRadioVapInfoMap.</synopsis>
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
    <test_case_id>TC_WIFIHAL_690</test_case_id>
    <test_objective>To get the Radio number of vaps  for 5G  wifi using wifi_getRadioVapInfoMap</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioVapInfoMap</api_or_interface_used>
    <input_parameters>radioindex : 1</input_parameters>
    <automation_approch>1.Load the module
2.Get the num of vaps  by calling wifi_getRadioVapInfoMap
3.Check if the value received is int and greater than zero
4.Unload the module</automation_approch>
    <expected_output>The num of vaps should be fetched successfully</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioNumofVaps</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioNumofVaps');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioNumofVaps');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    expectedresult = "SUCCESS";

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the VAPTelemetry details
        print "TEST STEP 1: Invoke the HAL API wifi_getetRadioVapInfoMap() successfully";
        print "EXPECTED RESULT 1: Should invoke wifi_getetRadioVapInfoMap() successfully";

        tdkTestObj = obj.createTestStep("WIFIHAL_GetRadioVapInfoMap");
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details!= "":
            details =  details.split(":")[1].split(",")[0].strip();
            if details.isdigit() and int (details) > 0:
               tdkTestObj.setResultStatus("SUCCESS");
               print "ACTUAL RESULT 1: wifi_getetRadioVapInfoMap() invoked successfully";
               print "The num of vaps is :",details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 1: wifi_getetRadioVapInfoMap() was not invoked successfully";
                print "The num of vaps is :",details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: wifi_getetRadioVapInfoMap() was not invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    obj1.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
