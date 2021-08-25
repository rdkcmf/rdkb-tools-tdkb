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
  <version>4</version>
  <name>TS_SANITY_CheckCaptivePortalLog_AfterFR</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the expected Captive Portal log line "Enter_WiFi_Personalization_captive_mode" is present in Consolelog.txt.0 when the device comes up after Factory Reset.</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_45</test_case_id>
    <test_objective>To check if the expected Captive Portal log line "Enter_WiFi_Personalization_captive_mode" is present in Consolelog.txt.0 when the device comes up after Factory Reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.X_CISCO_COM_DeviceControl.FactoryReset
ParamValue : Router,Wifi,VoIP,Dect,MoCA
Type : string</input_parameters>
    <automation_approch>1. Load the pam tad and sysutil modules
2. Initiate a Factory Reset
3. Check if the Captive Portal Mode is enabled by querying Device.DeviceInfo.X_RDKCENTRAL-COM_CaptivePortalEnable, Device.DeviceInfo.X_RDKCENTRAL-COM_ConfigureWiFi, Device.DeviceInfo.X_RDKCENTRAL-COM_WiFiNeedsPersonalization and checking if the values are true after FR.
4. Check if the log line "Enter_WiFi_Personalization_captive_mode" in present in Consolelog.txt.0</automation_approch>
    <expected_output>Captive Portal log line "Enter_WiFi_Personalization_captive_mode" should be present in Consolelog.txt.0 when the device comes up after FR.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckCaptivePortalLog_AfterFR</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *;
from time import sleep;

#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tadobj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_SANITY_CheckCaptivePortalLog_AfterFR');
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckCaptivePortalLog_AfterFR');
tadobj.configureTestCase(ip,port,'TS_SANITY_CheckCaptivePortalLog_AfterFR');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();
tadloadmodulestatus=tadobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper() and "SUCCESS" in tadloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    tadobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Initiate a device FR
    pamobj.saveCurrentState();
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "\nTEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        pamobj.restorePreviousStateAfterReboot();

        #After the device comes up check if the Captive Portal Mode is enabled
        paramList = ["Device.DeviceInfo.X_RDKCENTRAL-COM_CaptivePortalEnable", "Device.DeviceInfo.X_RDKCENTRAL-COM_ConfigureWiFi", "Device.DeviceInfo.X_RDKCENTRAL-COM_WiFiNeedsPersonalization"];
        tdkTestObj,actualresult,orgValue = getMultipleParameterValues(tadobj,paramList);
        print "\nTEST STEP 2: Check if the Captive Portal Mode is enabled";
        print "EXPECTED RESULT 2: The Captive Portal Mode should be enabled; Get the Values of the parameters : ", paramList;

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2 : The values of the parameters are : Device.DeviceInfo.X_RDKCENTRAL-COM_CaptivePortalEnable - %s, Device.DeviceInfo.X_RDKCENTRAL-COM_ConfigureWiFi - %s, Device.DeviceInfo.X_RDKCENTRAL-COM_WiFiNeedsPersonalization - %s" %(orgValue[0], orgValue[1], orgValue[2]);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if orgValue[0] == "true" and orgValue[1] == "true" and orgValue[2] == "true":
                tdkTestObj.setResultStatus("SUCCESS");
                print "\nThe Captive Portal Mode is Enabled";

                #Check if the required logs are present in the Consolelog.txt.0
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "grep -ire \"Enter_WiFi_Personalization_captive_mode\" /rdklogs/logs/Consolelog.txt.0";
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                print "\nTEST STEP 3: Check if the log line \"Enter_WiFi_Personalization_captive_mode\" is present in Consolelog.txt.0";
                print "EXPECTED RESULT 3: The required log line should be present in Consolelog.txt.0";

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Required log line is present, Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Required log line is not present, Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "\nThe Captive Portal Mode is not Enabled";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Get operation failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset"
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
    tadobj.unloadModule("tad");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    tadobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

