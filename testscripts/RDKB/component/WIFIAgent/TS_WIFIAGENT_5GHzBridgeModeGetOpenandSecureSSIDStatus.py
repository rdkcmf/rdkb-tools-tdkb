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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_5GHzBridgeModeGetOpenandSecureSSIDStatus</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To enable public wifi  and get the SSID status for 5GHz open and secure public wifi  in bridge mode</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIAGENT_159</test_case_id>
    <test_objective>To enable public wifi  and get the SSID status for 5GHz open and secure public wifi  in bridge mode</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.6.SSID
Device.WiFi.SSID.10.SSID</input_parameters>
    <automation_approch>1.Load the module
2.Get the current values of public wifi parameters
3.Enable public wifi and check for CcspHotspot process
4.Set the device to bridge mode
5.Get the SSID status for 5G open and secure public wifi and check the status is up
6.Revert back the public wifi parameters
7.Unload the module</automation_approch>
    <expected_output>With public wifi enabled and device in bridge mode 5G open and secure public wifi are expected to be up</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzBridgeMoodeGetOpenandSecureSSIDStatus</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
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
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzBridgeMode_GetOpenandSecureSSIDStatus');
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzBridgeMode_GetOpenandSecureSSIDStatus');
#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=wifiobj.getLoadModuleResult();


def setLanMode(mode, obj):
    expectedresult = "SUCCESS"
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.addParameter("paramValue", mode)
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        sleep(90)
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        newValue = details.split("VALUE:")[1].split(' ')[0];
        if expectedresult in actualresult and newValue==mode:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT : Lannmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : SUCCESS";
            return_status="SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT : Lanmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : FAILURE";
            return_status= "FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
        return_status="FAILURE"
    return return_status;

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

                    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
                    tdkTestObj.executeTestCase("expectedresult");
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    orgLanMode = details.split("VALUE:")[1].split(' ')[0];
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP : Get the current lanMode"
                        print "EXPECTED RESULT : Should retrieve the current lanMode"
                        print "ACTUAL RESULT : Lanmode is %s" %orgLanMode;
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #if bridge mode is enabled, disable it before trying to enable mesh
                        if "bridge-static" != orgLanMode:
                             actualresult = setLanMode("bridge-static", wifiobj)

                    if expectedresult in actualresult:
                        secureSSID="Device.WiFi.SSID.6.Enable";
                        publicSSID="Device.WiFi.SSID.10.Enable";
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
                        if expectedresult in (actualresult1 and actualresult2)  and "true" in (details1 and value):
                            details2 = value.split("VALUE:")[1].split(' ')[0];
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 5 :Get the SSID status for Secure and Open 5GHz public wifi";
                            print "EXPECTED RESULT 5: Should get the SSID status of Secure and Open 5GHz public wifi as true";
                            print "ACTUAL RESULT 5: SSID status received are %s and %s"%(details1,details2);
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5 :Get the SSID status for Secure and Open 5GHz public wifi";
                            print "EXPECTED RESULT 5: Should get the SSID statusof  Secure and Open 5GHz public wifi as true";
                            print "ACTUAL RESULT 5: SSID status received are %s and %s"%(details1,details2);
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

                        if orgLanMode != "bridge-static":
                            print "Revert lanmode to original value"
                            status = setLanMode(orgLanMode,wifiobj)
                            if "SUCCESS" in status:
                               print "Revert lan mode success";
                            else:
                                 print "Revert lan mode failure";
                    else:
                        print "Failed to change lan mode to bridge";
                        tdkTestObj.setResultStatus("FAILURE");
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
