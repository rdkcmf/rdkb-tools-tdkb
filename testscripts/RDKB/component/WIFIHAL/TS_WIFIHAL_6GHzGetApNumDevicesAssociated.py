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
  <name>TS_WIFIHAL_6GHzGetApNumDevicesAssociated</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApNumDevicesAssociated() and check if it returns a valid non-empty value for 6GHz Private access point associated number of devices.</synopsis>
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
    <test_case_id>TC_WIFIHAL_664</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApNumDevicesAssociated() and check if it returns a valid non-empty value for 6GHz Private access point associated number of devices.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApNumDevicesAssociated</api_or_interface_used>
    <input_parameters>methodname : wifi_getApNumDevicesAssociated
apIndex : fetched from platform property file</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getApNumDevicesAssociated() to get the number of devices associated to the 6Ghz private access point.
3. Check if the value is a valid integer.
4. Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_getApNumDevicesAssociated() should be invoked successfully and the number of devices connected to the 6GHz private access point fetched.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApNumDevicesAssociated</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApNumDevicesAssociated');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApNumDevicesAssociated');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);
    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the Access Point number of devices associated
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
        tdkTestObj.addParameter("methodName","getApNumDevicesAssociated");
        tdkTestObj.addParameter("radioIndex",apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2 : Invoke the HAL API wifi_getApNumDevicesAssociated";
        print "EXPECTED RESULT 2 : The HAL API wifi_getApNumDevicesAssociated should be invoked successfully";

        if expectedresult in actualresult :
            ApNumDevices = details.split(":")[1].strip();
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: wifi_getApNumDevicesAssociated invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            print "\nTEST STEP 3: Get the number of Ap Associated Devices"
            print "EXPECTED RESULT 3: Should get the number of Ap Associated Devices as a valid value"

            if ApNumDevices.isdigit():
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Received the number of Ap Associated Devices as a valid value"
                print "ApNumDevicesAssociated : %s"%ApNumDevices
                print "TEST EXECUTION RESULT: SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Received the number of Ap Associated Devices as an invalid value"
                print "ApNumDevicesAssociated : %s"%ApNumDevices
                print "TEST EXECUTION RESULT: FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: wifi_getApNumDevicesAssociated() call failed"
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
