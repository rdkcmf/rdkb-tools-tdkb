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
  <name>TS_WIFIHAL_6GHzGetWiFiTrafficStats</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetWifiTrafficStats</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getWiFiTrafficStats for 6Ghz private access point and check if the stats values are greater than or equal to 0.</synopsis>
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
    <test_case_id>TC_WIFIHAL_667</test_case_id>
    <test_objective>Invoke the HAL API wifi_getWiFiTrafficStats for 6Ghz private access point and check if the stats values are greater than or equal to 0.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getWiFiTrafficStats</api_or_interface_used>
    <input_parameters>apIndex : fetched from platform property file</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getWiFiTrafficStats() to retrieve the wifi traffic stats.
3. Check if all the stat values are integral values greater than or equal to 0.
4. Unload the modules</automation_approch>
    <expected_output>The HAL APIwifi_getWiFiTrafficStats() should be invoked successfully and all the WiFi Traffic Stats should be integral values greater than or equal to 0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetWiFiTrafficStats</test_script>
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
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetWiFiTrafficStats');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetWiFiTrafficStats');

#Get the result of connection with test component and DUT
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
        primitive = 'WIFIHAL_GetWifiTrafficStats'
        tdkTestObj = obj.createTestStep(primitive);
        tdkTestObj.addParameter("apIndex",apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2: Get the Wifi Traffic statistics for 6GHz using the HAL API wifi_getWifiTrafficStats()";
        print "EXPECTED RESULT 2: wifi_getWifiTrafficStats should return the wifi traffic statistics for 6GHz";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: wifi_getWifiTrafficStats() invoked successfully";
            print "Actual result is :",details;
            print "[TEST EXECUTION RESULT] 2: SUCCESS";

            trafficStats =  details.rstrip('\n').split('-')[1]
            wifi_ErrorsSent = trafficStats.split(',')[0].split(' ')[2]
            wifi_ErrorsReceived = trafficStats.split(',')[1].split(' ')[2]
            wifi_UnicastPacketsSent = trafficStats.split(',')[2].split(' ')[2]
            wifi_UnicastPacketsReceived = trafficStats.split(',')[3].split(' ')[2]
            wifi_DiscardedPacketsSent= trafficStats.split(',')[4].split(' ')[2]
            wifi_DiscardedPacketsReceived = trafficStats.split(',')[5].split(' ')[2]
            wifi_MulticastPacketsSent = trafficStats.split(',')[6].split(' ')[2]
            wifi_MulticastPacketsReceived = trafficStats.split(',')[7].split(' ')[2].replace("\\n", "")

            print "Errors Sent : ", wifi_ErrorsSent;
            print "Errors Received : ", wifi_ErrorsReceived;
            print "Unicast Packets Sent : ", wifi_UnicastPacketsSent;
            print "Unicast Packets Received : ", wifi_UnicastPacketsReceived;
            print "Discarded Packets Sent : ", wifi_DiscardedPacketsSent;
            print "Discarded Packets Received : ", wifi_DiscardedPacketsReceived;
            print "Multicast Packets Sent : ", wifi_MulticastPacketsSent;
            print "Multicast Packets Received : ", wifi_MulticastPacketsReceived;

            print "\nTEST STEP 3: Check if the Wifi Traffic statistics values for 6GHz are greater than or equal to 0";
            print "EXPECTED RESULT 3: Wifi Traffic statistics values for 2.4GHz should be greater than or equal to 0";

            if wifi_ErrorsSent.isdigit() and wifi_ErrorsReceived.isdigit() and wifi_UnicastPacketsSent.isdigit() and wifi_UnicastPacketsReceived.isdigit() and wifi_DiscardedPacketsSent.isdigit() and wifi_DiscardedPacketsReceived.isdigit() and wifi_MulticastPacketsSent.isdigit() and wifi_MulticastPacketsReceived.isdigit():
                tdkTestObj.setResultStatus("SUCCESS");
                print "All WiFi Traffic stats are valid numerical values";

                if int(wifi_ErrorsSent) >= 0 and int(wifi_ErrorsReceived) >=0 and int(wifi_UnicastPacketsSent) >=0 and int(wifi_UnicastPacketsReceived) >=0 and int(wifi_DiscardedPacketsSent) >=0 and int(wifi_DiscardedPacketsReceived) >=0 and int(wifi_MulticastPacketsSent) >=0 and int(wifi_MulticastPacketsReceived) >=0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: All Wifi Traffic statistics values for 6GHz are greater than or equal to 0";
                    print "[TEST EXECUTION RESULT] 3: SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: All Wifi Traffic statistics values for 6GHz are not greater than or equal to 0";
                    print "[TEST EXECUTION RESULT] 3: FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: All WiFi Traffic stats are not valid numerical values";
                print "[TEST EXECUTION RESULT] 3: FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: wifi_getWifiTrafficStats() not invoked successfully";
            print "[TEST EXECUTION RESULT] 2: FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
