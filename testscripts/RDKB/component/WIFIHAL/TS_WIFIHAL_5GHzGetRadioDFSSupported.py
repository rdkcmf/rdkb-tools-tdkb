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
  <version>3</version>
  <name>TS_WIFIHAL_5GHzGetRadioDFSSupported</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the api wifi_getRadioDfsSupport() for 5GHz and check whether the get value is proper.</synopsis>
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
    <test_case_id>TS_WIFIHAL_521</test_case_id>
    <test_objective>To invoke the api wifi_getRadioDfsSupport() for 5GHz and check whether the get value is proper.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDfsSupport()</api_or_interface_used>
    <input_parameters>methodName   :   getRadioDFSSupported
radioIndex   : 1</input_parameters>
    <automation_approch>1.Load Wifihal and sysutil Modules
2. Get whether DFS is supported or not for 5GHz using getRadioDFSSupported() API
3. Check if the device supports DFS by getting the value of DFS_SUPPORT variable in tdk_platform.properties
4. Check if the DFS support status from hal api is same as the value from tdk_platform.properties
3. Unload the Modules</automation_approch>
    <expected_output>wifi_getRadioDfsSupport() should return the device's DFS support status</expected_output>
    <priority>High</priority>
    <test_stub_interface>Wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioDFSSupported</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
from tdkbVariables import *;
radio2 = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioDFSSupported');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioDFSSupported');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio2);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        getMethod = "getRadioDFSSupported"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        #Calling the method from wifiUtility to check whether DFS is Supported or not
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
        if expectedresult in actualresult :
           print "TEST STEP 1: Get DFS Support for 5GHz via wifi_getRadioDfsSupport";
           print "EXPECTED RESULT: Should successfully get the DFS Support"
           print "ACTUAL RESULT: wifi_getRadioDFSSupported is success";
           print "TEST EXECUTION RESULT :SUCCESS"
           tdkTestObj.setResultStatus("SUCCESS");
           halResult = details.split(":")[1].strip()
           print "getRadioDFSSupport() returned DFS status as: %s"%halResult

	   tdkTestObj = sysobj.createTestStep('ExecuteCmd');
	   print "Get the DFS support status of the device from tdk_platform.properties";
	   getSupport = "sh %s/tdk_utility.sh parseConfigFile DFS_SUPPORT" %TDK_PATH;
	   tdkTestObj.addParameter("command", getSupport);
	   tdkTestObj.executeTestCase(expectedresult);
	   actualresult = tdkTestObj.getResult();
	   DFS_Support = tdkTestObj.getResultDetails().strip();
	   DFS_Support = DFS_Support.replace("\\n", "");
           if DFS_Support and DFS_Support == halResult:
               print "TEST STEP 2: Get DFS Support for 5GHz of this device and compare with hal api result"
               print "EXPECTED RESULT: DFS Support status from hal api and tdk_platform.properties should be the same";
               print "ACTUAL RESULT: DFS_Support from hal api and tdk_platform.properties are the same : %s"%DFS_Support;
               print "TEST EXECUTION RESULT :SUCCESS"
               tdkTestObj.setResultStatus("SUCCESS");
           else:
               print "TEST STEP 2: Get DFS Support for 5GHz of this device and compare with hal api result"
               print "EXPECTED RESULT: DFS Support status from hal api and tdk_platform.properties should be the same";
               print "ACTUAL RESULT: DFS_Support from hal api and tdk_platform.properties are not the same : %s"%DFS_Support;
               print "ACTUAL RESULT: DFS_Support from tdk_platform.properties : %s"%DFS_Support;
               print "TEST EXECUTION RESULT :FAILURE"
               tdkTestObj.setResultStatus("FAILURE");
        else:
           print "TEST STEP 1: Get DFS Support for 5GHz via wifi_getRadioDfsSupport"
           print "EXPECTED RESULT: Should successfully get the DFS Support"
           print "ACTUAL RESULT: getRadioDFSSupported is failure"
           print "TEST EXECUTION RESULT :FAILURE"
           print "getRadioDFSSupport() failed"
           tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

