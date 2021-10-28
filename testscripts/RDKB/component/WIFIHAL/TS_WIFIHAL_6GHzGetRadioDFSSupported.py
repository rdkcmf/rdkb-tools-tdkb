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
  <version>6</version>
  <name>TS_WIFIHAL_6GHzGetRadioDFSSupported</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the HAL API  wifi_getRadioDfsSupport() for 6GHz and check whether the DFS support is Enabled.</synopsis>
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
    <test_case_id>TC_WIFIHAL_638</test_case_id>
    <test_objective>To invoke the HAL API  wifi_getRadioDfsSupport() for 6GHz and check whether the DFS support is Enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDfsSupport()</api_or_interface_used>
    <input_parameters>methodName  :  getRadioDFSSupported
radioIndex  : index corresponding to 6G radio</input_parameters>
    <automation_approch>1.Load Wifihal Module
2. Get whether DFS is supported for 6GHz using wifi_getRadioDFSSupport() API. Check if DFS Supported returns false for 6Ghz.
3. Unload Module</automation_approch>
    <expected_output>The DFS Supported value should be successfully retrieved using the HAL API wifi_getRadioDFSSupport() and it should be enabled for 6GHz radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioDFSSupported</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioDFSSupported');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        getMethod = "getRadioDFSSupported"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        #Calling the method from wifiUtility to check whether DFS is Supported or not
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)

        print "\nTEST STEP 1 : Get DFS Support for 6GHz"
        print "EXPECTED RESULT 1: Should successfully get the DFS Support"

        if expectedresult in actualresult :
            print "ACTUAL RESULT 1: getRadioDFSSupported is success"
            print "TEST EXECUTION RESULT : SUCCESS"
            print "getRadioDFSSupport() is success"
            tdkTestObj.setResultStatus("SUCCESS");
            enable = details.split(":")[1].strip()

            print "\nTEST STEP 2 : Get DFS Support for 6GHz"
            print "EXPECTED RESULT 2: Should successfully get the DFS Support as Disabled for 6GHz"

            if "Disabled" in enable:
                print "ACTUAL RESULT 2: getRadioDFSSupported : %s"%details;
                print "TEST EXECUTION RESULT :SUCCESS"
                print "DFS is Disabled for 6GHz"
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "ACTUAL RESULT 2: getRadioDFSSupported : %s"%details;
                print "TEST EXECUTION RESULT :FAILURE"
                print "DFS is not Disabled for 6GHz"
                tdkTestObj.setResultStatus("FAILURE");
        else:
           print "ACTUAL RESULT 1: getRadioDFSSupported is failure";
           print "TEST EXECUTION RESULT :FAILURE"
           print "getRadioDFSSupport() failed"
           tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

