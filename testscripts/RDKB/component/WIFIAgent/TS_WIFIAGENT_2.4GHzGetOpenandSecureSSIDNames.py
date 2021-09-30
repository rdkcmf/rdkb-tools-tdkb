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
  <name>TS_WIFIAGENT_2.4GHzGetOpenandSecureSSIDNames</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To enable public wifi  and get the SSID names for 2.4GHz open and secure public wifi</synopsis>
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
    <test_case_id>TC_WIFIAGENT_154</test_case_id>
    <test_objective>To enable public wifi  and get the SSID names for 2.4GHz open and secure public wifi</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadnand</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.5.SSID
Device.WiFi.SSID.9.SSID</input_parameters>
    <automation_approch>1.Load the module
2.Get the current values of public wifi parameters
3.Enable public wifi and check for CcspHotspot process
4.Get the SSID name for 2.4G open and secure public wifi and check the name are not OutOfService
5.Revert back the public wifi parameters
6.Unload the module</automation_approch>
    <expected_output>After enabling public wifi open and secure public wifi should not have OutOfService as thier SSID Name.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHzGetOpenandSecureSSIDNames</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbTelemetry2_0Utility import *;
from time import sleep;
from xfinityWiFiLib import *

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHzGetOpenandSecureSSIDNames');
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHzGetOpenandSecureSSIDNames');
#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=wifiobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj,actualresult,orgValue = GetPublicWiFiParamValues(wifiobj);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Get values of PublicWiFi params";
        print "EXPECTED RESULT 1: Should get PublicWiFi param values";
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : SUCCESS";

        setvalues,tdkTestObj,actualresult  = parsePublicWiFiConfigValues(sysobj);
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2:Get the set values to enable PublicWiFi";
            print "EXPECTED RESULT2: Shouls get the set values to enable PublicWiFi";
            print "ACTUAL RESULT 2:Get was successful";
            print "[TEST EXECUTION RESULT] : SUCCESS";
            values = [setvalues[0],setvalues[1],setvalues[2],setvalues[3],setvalues[3],"true","true","true","true",setvalues[3],"true","true",setvalues[4],setvalues[5],setvalues[6],setvalues[7],setvalues[8],setvalues[7],setvalues[8],setvalues[3],"true","true",setvalues[4],setvalues[5],setvalues[6],setvalues[7],setvalues[8],setvalues[7],setvalues[8],"true"];

            tdkTestObj, actualresult, details = SetPublicWiFiParamValues(wifiobj,values);
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Enable PublicWiFi"
                print "EXPECTED RESULT 3: Should enable PublicWiFi";
                print "ACTUAL RESULT 3:%s" %details
                print "[TEST EXECUTION RESULT] : SUCCESS";
                sleep(30);

                tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
                details,actualresult = getPID(tdkTestObj_Sys_ExeCmd,"CcspHotspot");
                if expectedresult in actualresult and details != "":
                    tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Check if CcspHotspot process is running";
                    print "EXPECTED RESULT 4:CcspHotspot  process should be running";
                    print "ACTUAL RESULT 4: pid of CcspHotspot:",details;
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    secureSSID="Device.WiFi.SSID.5.SSID";
                    publicSSID="Device.WiFi.SSID.9.SSID";
                    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName",secureSSID);
                    expectedresult="SUCCESS";
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult1 = tdkTestObj.getResult();
                    value = tdkTestObj.getResultDetails();
                    details1 = value.split("VALUE:")[1].split(' ')[0];

                    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName",publicSSID);
                    expectedresult="SUCCESS";
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult2 = tdkTestObj.getResult();
                    value = tdkTestObj.getResultDetails();
                    if expectedresult in (actualresult1 and actualresult2)  and "OutofService"  not in (details1 and value):
                        details2 = value.split("VALUE:")[1].split(' ')[0];
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5 :Get the SSID name for Secure and Open 2.4GHz public wifi";
                        print "EXPECTED RESULT 5: Should not get the name of Secure and Open 2.4GHz public wifi as OutofService";
                        print "ACTUAL RESULT 5: SSID name received are %s and %s"%(details1,details2);
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5 :Get the SSID name for Secure and Open 2.4GHz public wifi";
                        print "EXPECTED RESULT 5: Should not get the name of Secure and Open 2.4GHz public wifi as OutofService";
                        print "ACTUAL RESULT 5: SSID name received are %s and %s"%(details1,details2);
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Revert the values of public wifi params
                    tdkTestObj, actualresult, details = SetPublicWiFiParamValues(wifiobj,orgValue);
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 6:Revert the PublicWiFi param values"
                        print "ACTUAL RESULT 6:%s" %details
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                         tdkTestObj.setResultStatus("FAILURE");
                         print "TEST STEP 6:Revert the PublicWiFi param values"
                         print "ACTUAL RESULT 6:%s" %details
                         print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                    print "TEST STEP 4: Check if CcspHotspot process is running";
                    print "EXPECTED RESULT 4:CcspHotspot  process should be running";
                    print "ACTUAL RESULT 4: pid of CcspHotspot:",details;
                    print "[TEST EXECUTION RESULT] :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Enable PublicWiFi"
                print "EXPECTED RESULT 3: Should enable PublicWiFi";
                print "ACTUAL RESULT 3:%s" %details
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:Get the set values to enable PublicWiFi";
            print "EXPECTED RESULT2: Shouls get the set values to enable PublicWiFi";
            print "ACTUAL RESULT 2:Get was successful";
            print "[TEST EXECUTION RESULT] :FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Get values of PublicWiFi params";
        print "EXPECTED RESULT 1: Should get PublicWiFi param values";
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysobj.unloadModule("sysutil");
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    wifiobj.setLoadModuleStatus("FAILURE");
