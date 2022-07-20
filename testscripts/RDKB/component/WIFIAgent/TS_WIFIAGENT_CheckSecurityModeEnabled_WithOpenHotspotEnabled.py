##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckSecurityModeEnabled_WithOpenHotspotEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_SetMultiple</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if Device.WiFi.AccessPoint.5.Security.ModeEnabled and Device.WiFi.AccessPoint.6.Security.ModeEnabled are open by default and does not toggle to any of the secured modes when Open Xfinity WiFi is configured.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_209</test_case_id>
    <test_objective>To check if Device.WiFi.AccessPoint.5.Security.ModeEnabled and Device.WiFi.AccessPoint.6.Security.ModeEnabled are open by default and does not toggle to any of the secured modes when Open Xfinity WiFi is configured.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.FactoryReset
paramValue : Router,Wifi,VoIP,Dect,MoCA
paramType : string
paramName : Device.WiFi.AccessPoint.{i}.Security.ModeEnabled</input_parameters>
    <automation_approch>1. Load the module
2. Initiate a device factory reset
3. Once the DUT comes up, query the open xfinity wifi vAPs security modes using Device.WiFi.AccessPoint.5.Security.ModeEnabled and Device.WiFi.AccessPoint.6.Security.ModeEnabled.
4. It should be "None" by default.
5. Get the default values of Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy, Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint, Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint, Device.WiFi.SSID.5.SSID, Device.WiFi.SSID.6.SSID and Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable.
6. Enable the Open Xfinity WiFi by setting the config values retrieved from platform properties to the above mentioned parameters and validate with GET.
7. Once it is enabled, check if the security mode enabled for the access points 5,6 reamin unchanged as "None" and does to toggle to any of the secured modes.
8. Revert the enabling parameters of Open Xfinity WiFi to initial values.
9. Unload the module.</automation_approch>
    <expected_output>Device.WiFi.AccessPoint.5.Security.ModeEnabled and Device.WiFi.AccessPoint.6.Security.ModeEnabled should be open by default and should not toggle to any of the secured modes when Open Xfinity WiFi is configured.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckSecurityModeEnabled_WithOpenHotspotEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

def getParam(wifiobj, paramName):
    expectedresult = "SUCCESS";
    value = "";
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName",paramName);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details != "":
        value = details.split("VALUE:")[1].split(" ")[0].strip();
        print "%s : %s" %(paramName, value);
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "%s is not retrieved successfully" %paramName;
        tdkTestObj.setResultStatus("FAILURE");
    return actualresult, value;

def getPublicWiFiConfigValues(sysobj):
    expectedresult = "SUCCESS";
    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    cmd1 = "sh %s/tdk_utility.sh parseConfigFile DSCPMARKPOLICY" %TDK_PATH;
    cmd2 = "sh %s/tdk_utility.sh parseConfigFile PRIMARYREMOTEENDPOINT" %TDK_PATH;
    cmd3 = "sh %s/tdk_utility.sh parseConfigFile SECONDARYREMOTEENDPOINT" %TDK_PATH;

    print cmd1;
    tdkTestObj_Sys_ExeCmd.addParameter("command", cmd1);
    tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj_Sys_ExeCmd.getResult();
    DSCPMarkPolicy = tdkTestObj_Sys_ExeCmd.getResultDetails().replace("\\n", "");

    print cmd2;
    tdkTestObj_Sys_ExeCmd.addParameter("command", cmd2);
    tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
    actualresult2 = tdkTestObj_Sys_ExeCmd.getResult();
    PrimaryRemoteEndpoint = tdkTestObj_Sys_ExeCmd.getResultDetails().replace("\\n", "");

    print cmd3;
    tdkTestObj_Sys_ExeCmd.addParameter("command", cmd3);
    tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
    actualresult3 = tdkTestObj_Sys_ExeCmd.getResult();
    SecondaryRemoteEndpoint = tdkTestObj_Sys_ExeCmd.getResultDetails().replace("\\n", "");

    if expectedresult in actualresult1 and expectedresult in actualresult2 and expectedresult in actualresult3 and DSCPMarkPolicy != "" and PrimaryRemoteEndpoint!= "" and SecondaryRemoteEndpoint!= "" :
        actualresult = "SUCCESS"
    else:
        actualresult = "FAILURE"

    setvalues = [DSCPMarkPolicy, PrimaryRemoteEndpoint, SecondaryRemoteEndpoint];
    return setvalues, tdkTestObj_Sys_ExeCmd, actualresult;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *;
from time import sleep;
from xfinityWiFiLib import *

#Test component to be tested
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckSecurityModeEnabled_WithOpenHotspotEnabled');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckSecurityModeEnabled_WithOpenHotspotEnabled');

#Get the result of connection with test component and DUT
wifiloadmodulestatus=wifiobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus ;

if "SUCCESS" in wifiloadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    wifiobj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Initiate a device FR
    wifiobj.saveCurrentState();
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("paramType","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Initiate a factory reset";
    print "EXPECTED RESULT 1: Factory reset should be initiated successfully";

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Factory reset is initiated successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #Restore the device state saved before reboot
        wifiobj.restorePreviousStateAfterReboot();
        #Sleep for 60s
        sleep(60);

        #Get the security mode enabled for Open Hotspot vAPs 5, 6
        paramList = ["Device.WiFi.AccessPoint.5.Security.ModeEnabled", "Device.WiFi.AccessPoint.6.Security.ModeEnabled"];
        print "\nTEST STEP 2 : Get the default values of Security Mode Enabled for the Open Hotspot vAPs and check if they are \"None\"";
        print "EXPECTED RESULT 2 : The default values of Security Mode Enabled for the Open Hotspot vAPs should be retrieved successfully as \"None\"";
        actualresult1, modeenabled_5 = getParam(wifiobj, paramList[0]);
        actualresult2, modeenabled_6 = getParam(wifiobj, paramList[1]);

        if actualresult1 in expectedresult and 	actualresult2 in expectedresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: The default values are retrived successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            #Check if the default value is "None"
            if modeenabled_5 == "None" and modeenabled_6 == "None":
                print "The initial security modes are open by default";
                tdkTestObj.setResultStatus("SUCCESS");

                #Enable the open xfinity SSID
                print "\nTEST STEP 3 : Get the default values of Open Xfinity WiFi";
                print "TEST STEP 3 : Should get the default values of Open Xfinity WiFi";
                tdkTestObj,actualresult,orgValue = getPublicWiFiParamValues(wifiobj);

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3 : The default values for DSCPMarkPolicy, PrimaryRemoteEndpoint, SecondaryRemoteEndpoint, SSID 5 Enable, SSID 6 Enable and Xfinity WiFi Enable are ", orgValue;
                    print "[TEST EXECUTION RESULT]: SUCCESS";

                    #Set values to enable Open Xfinity WiFi
                    print "\nTEST STEP 4 : Enable the Open Xfinity WiFi";
                    print "EXPECTED RESULT 4 : Should enable the Open Xfinity WiFi successfully";
                    configValues, tdkTestObj ,actualresult = getPublicWiFiConfigValues(sysobj);

                    if expectedresult in actualresult :
                        setvalues = [configValues[0],configValues[1],configValues[2],"true","true","true"];
                        tdkTestObj, actualresult2, details = setPublicWiFiParamValues(wifiobj,setvalues);

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 4: Details : %s" %details;
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Cross check if values are set successfully
                            print "\nTEST STEP 5 : Get the current values of Open Xfinity WiFi";
                            print "TEST STEP 5 : Should get the current values of Open Xfinity WiFi";
                            tdkTestObj,actualresult,currValue = getPublicWiFiParamValues(wifiobj);

                            if expectedresult in actualresult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 5 : The current values for DSCPMarkPolicy, PrimaryRemoteEndpoint, SecondaryRemoteEndpoint, SSID 5 Enable, SSID 6 Enable and Xfinity WiFi Enable are ", currValue;
                                print "[TEST EXECUTION RESULT]: SUCCESS";

                                if currValue[0] == setvalues[0] and currValue[1] == setvalues[1] and currValue[2] == setvalues[2] and currValue[3] == setvalues[3] and currValue[4] == setvalues[4]:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "GET values match with SET; Open Xfinity WiFi is enabled successfully";

                                    #Check if the security mode remains as open and does not change to secured modes
                                    print "\nTEST STEP 6 : Get the current values of Security Mode Enabled for the Open Hotspot vAPs and check if they are \"None\"";
                                    print "EXPECTED RESULT 6 : The current values of Security Mode Enabled for the Open Hotspot vAPs should be retrieved successfully as \"None\"";
                                    actualresult1, modeenabled_5_curr = getParam(wifiobj, paramList[0]);
                                    actualresult2, modeenabled_6_curr = getParam(wifiobj, paramList[1]);

                                    if actualresult1 in expectedresult and 	actualresult2 in expectedresult:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT 6: The default values are retrived successfully";
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS"

                                        #Check if the default value is "None"
                                        if modeenabled_5_curr == "None" and modeenabled_6_curr == "None":
                                            print "The current security modes are open after enabling the Open Xfinity WiFi";
                                            tdkTestObj.setResultStatus("SUCCESS");
                                        else:
                                            print "The current security modes are NOT open after enabling the Open Xfinity WiFi";
                                            tdkTestObj.setResultStatus("FAILURE");
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT 6: The default values are NOT retrived successfully";
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE"

                                    #Revert the Open Xfinity WiFi enable
                                    print "\nTEST STEP 7 : Revert the Open Xfinity WiFi to initial state";
                                    print "EXPECTED RESULT 7 : Should revert the Open Xfinity WiFi to initial state successfully";
                                    tdkTestObj, actualresult, details = setPublicWiFiParamValues(wifiobj,orgValue);

                                    if expectedresult in actualresult:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT 7: Details : %s" %details;
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT 7: Details : %s" %details;
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "GET values does NOT match with SET; Open Xfinity WiFi is NOT enabled successfully";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 5 : The current values for DSCPMarkPolicy, PrimaryRemoteEndpoint, SecondaryRemoteEndpoint, SSID 5 Enable, SSID 6 Enable and Xfinity WiFi Enable are ", currValue;
                                print "[TEST EXECUTION RESULT]: FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 4: Details : %s" %details;
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: Open Xfinity WiFi Configuration values are not retrieved successfully";
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3 : The default values for DSCPMarkPolicy, PrimaryRemoteEndpoint, SecondaryRemoteEndpoint, SSID 5 Enable, SSID 6 Enable and Xfinity WiFi Enable are ", orgValue;
                    print "[TEST EXECUTION RESULT]: FAILURE";
            else:
                print "The initial security modes are NOT open by default";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: The default values are NOT retrived successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Factory reset is not initiated successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    wifiobj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    wifiobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
