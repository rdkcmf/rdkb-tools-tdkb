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
  <name>TS_WIFIHAL_6GHzGetRadioGuardInterval</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRadioGuardInterval() for 6GHz and check if the guard interval retrieved is Auto or an interval between 100-800 nsec.</synopsis>
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
    <test_case_id>TC_WIFIHAL_671</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRadioGuardInterval() for 6GHz and check if the guard interval retrieved is Auto or an interval between 100-800 nsec.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioGuardInterval()</api_or_interface_used>
    <input_parameters>methodname : getRadioGuardInterval
radioIndex : 6G radio index</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRadioGuardInterval() for 6G radio.
3. Check the guard interval retrieved is either Auto or a value between 100-800nsec.
4. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getRadioGuardInterval() should be retrieved successfully and the guard interval should be either Auto or a valid value between 100nsec-800nsec for 6G radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioGuardInterval</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioGuardInterval');

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
        tdkTestObj.addParameter("methodName","getRadioGuardInterval");
        tdkTestObj.addParameter("radioIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getRadioGuardInterval() for 6GHz radio";
        print "EXPECTED RESULT 1 : The API should be invoked successfully";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            interval = details.split(":")[1].strip("nsec");
            print "ACTUAL RESULT 1 : The API was invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            print "\nTEST STEP 2 : Check if the radio guard interval is a valid value from : [Auto, value between 100 - 800]";
            print "EXPECTED RESULT 2 : The radio guard interval should be a valid value";

            if (interval == "Auto" or (interval.isdigit() and (100 <= int(interval) <= 800))):
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Radio guard interval : %s" %interval;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Radio guard interval : %s" %interval;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1 : The API was not invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
