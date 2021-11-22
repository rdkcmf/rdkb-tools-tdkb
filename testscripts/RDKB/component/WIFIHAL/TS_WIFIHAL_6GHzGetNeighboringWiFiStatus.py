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
  <name>TS_WIFIHAL_6GHzGetNeighboringWiFiStatus</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetNeighboringWiFiStatus</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_startNeighborScan() to start the neighbourhood WiFi scan for 6GHz private access point and then invoke wifi_getNeighboringWiFiStatus() for 6Ghz radio to retrieve the neighbouring WiFi status details.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_678</test_case_id>
    <test_objective>Invoke the HAL API wifi_startNeighborScan() to start the neighbourhood WiFi scan for 6GHz private access point and then invoke wifi_getNeighboringWiFiStatus() for 6Ghz radio to retrieve the neighbouring WiFi status details.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_startNeighborScan()
wifi_getNeighboringWiFiStatus()
</api_or_interface_used>
    <input_parameters>radioIndex : 6G radio index
apIndex : 6G private access point index</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_startNeighborScan() for 6G private access point index to start the neighbourhood scan. The API should return success after the scanning.
3. Invoke the HAL API wifi_getNeighboringWiFiStatus() for 6G radio to retrieve the neighbouring wifi status. The API should return success.
4. Unload the module
</automation_approch>
    <expected_output>The HAL API wifi_startNeighborScan() should successfully scan the neighbourhood and the API wifi_getNeighboringWiFiStatus() should successfully retrieve the neighbouring wifi status for 6G radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetNeighboringWiFiStatus</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import random;
import time;
from wifiUtility import *;
from tdkbVariables import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetNeighboringWiFiStatus');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetNeighboringWiFiStatus');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
        tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

        if apIndex == -1:
            print "Failed to get the Access Point index";
            tdkTestObjTemp.setResultStatus("FAILURE");
        else:
            #Prmitive test case which is associated to this Script
            tdkTestObj = obj.createTestStep('WIFIHAL_StartNeighborScan');
            tdkTestObj.addParameter("apIndex", apIndex);
            tdkTestObj.addParameter("scan_mode", 1);
            value = random.randrange(10,20);
            tdkTestObj.addParameter("dwell_time", value);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 2: Successfully start the neighbor scan by invoking wifi_startNeighborScan()"
            print "EXPECTED RESULT 2: Should successfully start the wifi_startNeighborScan";

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Successfully started wifi_startNeighborScan; Details : %s"%details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                time.sleep(10)
                #Script to load the configuration file of the component
                tdkTestObj = obj.createTestStep("WIFIHAL_GetNeighboringWiFiStatus");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 3: Get the neighboring wifi status by invoking wifi_getNeighboringWiFiStatus() for 6GHz ";
                print "EXPECTED RESULT 3: Should get the neighboring wifi status for 6GHz";

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: wifi_getNeighboringWiFiStatus invoked successfully; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: wifi_getNeighboringWiFiStatus not invoked successfully; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Failed to get the result of wifi_startNeighborScan; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
