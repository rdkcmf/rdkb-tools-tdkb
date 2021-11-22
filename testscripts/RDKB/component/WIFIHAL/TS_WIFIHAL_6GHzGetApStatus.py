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
  <name>TS_WIFIHAL_6GHzGetApStatus</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the HAL API wifi_getApStatus() for 6GHz Private Access Point and check if the access point status is from the expected list of : Up, Disable, Disabled.</synopsis>
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
    <test_case_id>TC_WIFIHAL_666</test_case_id>
    <test_objective>To invoke the HAL API wifi_getApStatus() for 6GHz Private Access Point and check if the access point status is from the expected list of : Up, Disable, Disabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApStatus</api_or_interface_used>
    <input_parameters>methodname : getApStatus
apIndex : fetched from platform property file</input_parameters>
    <automation_approch>1.Load the modules
2. Invoke the HAL API wifi_getApStatus() to get the 6GHz private access point status.
3. Check if the value retrieved is from the expected list : Up, Disable, Disabled.
4. Unload the modules</automation_approch>
    <expected_output>Invoking the HAL API  wifi_getApStatus() for 6GHz Private Access Point should be success and the access point status should be from the expected list of : Up, Disable, Disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApStatus</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApStatus');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApStatus');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);
    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the Access Point Status using the API wifi_getApStatus
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        tdkTestObj.addParameter("methodName","getApStatus");
        tdkTestObj.addParameter("radioIndex",apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2 : Invoke the HAL API wifi_getApStatus and get the 6GHz Private Access Point Status";
        print "EXPECTED RESULT 2 : The HAL API wifi_getApStatus should be invoked successfully";

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: The HAL API wifi_getApStatus invoked successfully"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            status_received = details.split(":")[1].strip();
            #List of AP status
            success_values = ['Up', 'Disable','Disabled'];
            print "\nPermitted Status values : ", success_values;

            print "\nTEST STEP 3: Validate the wifi_getApStatus Function";
            print "EXPECTED RESULT 3: wifi_getApStatus should return a string which should be from the permitted values list";

            if status_received in success_values:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: AP Status string received: %s is from the permitted values list"%status_received;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: AP Status string received: %s is not from the permitted values list"%status_received;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: The HAL API wifi_getApStatus is not invoked successfully"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
