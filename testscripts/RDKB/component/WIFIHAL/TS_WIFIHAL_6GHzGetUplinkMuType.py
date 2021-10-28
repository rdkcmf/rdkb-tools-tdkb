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
  <name>TS_WIFIHAL_6GHzGetUplinkMuType</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke wifi_getUplinkMuType() and check if it returns a value from the expected list for 6GHz radio [WIFI_UL_MU_TYPE_NONE, WIFI_UL_MU_TYPE_HE].</synopsis>
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
    <test_case_id>TC_WIFIHAL_641</test_case_id>
    <test_objective>Invoke wifi_getUplinkMuType() and check if it returns a value from the expected list for 6GHz radio [WIFI_UL_MU_TYPE_NONE, WIFI_UL_MU_TYPE_HE].</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getUplinkMuType()</api_or_interface_used>
    <input_parameters>methodname : getUplinkMuType
radioIndex : index corresponding to 6G radio</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getUplinkMuType() for 6GHz and check if its return was success
3. Check if output of wifi_getUplinkMuType() is one from the list {
    WIFI_UL_MU_TYPE_NONE,
    WIFI_UL_MU_TYPE_HE,
}
4. Unload wifihal module</automation_approch>
    <expected_output>The HAL API wifi_getUplinkMuType() should successfully retrieve the Uplink MuType value within the expected values range for 6GHz radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetUplinkMuType</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetUplinkMuType');

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
        #Script to load the configuration file of the component
        print "TEST STEP 1: Invoke the wifi_getUplinkMuType api";
        print "EXPECTED RESULT 1:Invocation of wifi_getUplinkMuType should be success";

        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
        tdkTestObj.addParameter("methodName","getUplinkMuType")
        tdkTestObj.addParameter("radioIndex", idx)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getUplinkMuType was success. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            muTypeList = {"0":"WIFI_UL_MU_TYPE_NONE", "1":"WIFI_UL_MU_TYPE_HE"};
            print "TEST STEP 2: Check if value returned by wifi_getUplinkMuType api is from the list ",muTypeList;
            print "EXPECTED RESULT 2 : The value returned by wifi_getUplinkMuType api should be from the above list";
            upMuType= details.split(":")[1].strip()

            if upMuType.isdigit() and 0 <= int(upMuType) and int(upMuType) <= 1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: UplinkMuType = %s. Value is from the expected list" %muTypeList[upMuType]
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: UplinkMuType = %s. Value is not within the expected range" %upMuType
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

