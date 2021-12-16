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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_6GHzGetRadioExtChannel</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke the HAL API wifi_getRadioExtChannel() to get the 6G radio extension channel and check if it is a value from the expected list of ['AboveControlChannel', 'BelowControlChannel', 'Auto'].</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_683</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRadioExtChannel() to get the 6G radio extension channel and check if it is a value from the expected list of ['AboveControlChannel', 'BelowControlChannel', 'Auto'].</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioExtChannel()</api_or_interface_used>
    <input_parameters>methodname : getRadioExtChannel
radioIndex : 6G radio index</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getRadioExtChannel() to get the 6G radio extension channel.
3. Check if the value retrieved is one of the accepted values : ['AboveControlChannel', 'BelowControlChannel', 'Auto'].
4. Unload the modules
</automation_approch>
    <expected_output>The HAL API wifi_getRadioExtChannel() to get the 6G radio extension channel should be invoked successfully and its value should be from the expected list of ['AboveControlChannel', 'BelowControlChannel', 'Auto'].</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioExtChannel</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioExtChannel');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamStringValue');
        tdkTestObj.addParameter("methodName","getRadioExtChannel");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1 : Invoke the HAL API wifi_getRadioExtChannel() to retrieve the extension channel for 6G radio";
        print "EXPECTED RESULT 1 : The HAL API wifi_getRadioExtChannel() should be invoked successfully";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: wifi_getRadioExtChannel() invocation is success; Details : %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Expected extension channel values
            success_values = ['AboveControlChannel', 'BelowControlChannel', 'Auto'];
            print "Expected extension channel values : ", success_values;
            status_received = details.split(":")[1].strip();

            print "\nTEST STEP 2 : Check if the extension channel recieved is from the expected extension channel values";
            print "EXPECTED RESULT 2 : The extension channel should be from the expected values list";

            if status_received in success_values :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Extension Channel value string received: %s"%status_received;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Extension Channel receieved is not from the expected values list : %s"%status_received;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: wifi_getRadioExtChannel() invocation failed; Details : %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
