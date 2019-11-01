##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WIFIAGENT_CheckBandsteeringProcess</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>40</execution_time>
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
    <test_case_id>TC_WIFIAGENT_64</test_case_id>
    <test_objective>To check whether bandsteering process is running with same SSID after a factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable,Device.WiFi.SSID.1.SSID,Device.WiFi.SSID.2.SSID</input_parameters>
    <automation_approch>1. Load wifiagent module
2.Do a factory reset
3.After factory reset,get the current bandsteering enable status,SSID names
4.Enable the bandsteering and set different SSID names for 2.4GHZ and 5 GHZ
5.Check if lbd process is running
6. set same SSID names for 2.4GHZ and 5 GHZ
7.Check if lbd process is running
8. Unload wifiagent module</automation_approch>
    <expected_output> bandsteering process should be running with same SSID after a factory reset</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckBandsteeringProcess</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
import tdkutility;
from tdkutility import *
from tdkbVariables import *;


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2 = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckBandsteeringProcess');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckBandsteeringProcess');
obj2.configureTestCase(ip,port,'TS_WIFIAGENT_CheckBandsteeringProcess');
pamobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckBandsteeringProcess');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =obj2.getLoadModuleResult();
loadmodulestatus4 =pamobj.getLoadModuleResult();
SSID1 = "TESTSSID1"
SSID2 = "TESTSSID2"

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper() and "SUCCESS" in loadmodulestatus4.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"
    obj.saveCurrentState();
    #Initiate Factory reset before checking the default value
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();
        time.sleep(180);


        tdkTestObj = obj.createTestStep('TADstub_Get');

        paramList=["Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable", "Device.WiFi.SSID.1.SSID", "Device.WiFi.SSID.2.SSID"]

        tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
        if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the bandtsteering enable status and SSID names";
            print "ACTUAL RESULT 2: Bandstering enable status and SSID names: %s %s %s" %(orgValue[0],orgValue[1],orgValue[2]) ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable|true|bool|Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(SSID1,SSID2));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Set BandSteering enable status as true and different wifi SSID names for 2.4GHZ and 5 GHZ"
                print "ACTUAL RESULT 3: %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";
                #check whether the process is running or not
                query="pidof lbd"
                print "query:%s" %query
                tdkTestObj = obj2.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                pid = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and pid == "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4:lbd process should not be running";
                    print "ACTUAL RESULT 4: lbd process is not running";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                    tdkTestObj.addParameter("paramList","Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(SSID1,SSID1));
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Set same SSID for 2.4GHZ and 5GHZ"
                        print "ACTUAL RESULT 5 : %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS";
                        #check whether the process is running or not
                        query="pidof lbd"
                        print "query:%s" %query
                        tdkTestObj = obj2.createTestStep('ExecuteCmd');
                        tdkTestObj.addParameter("command", query)
                        tdkTestObj.executeTestCase("SUCCESS");
                        actualresult = tdkTestObj.getResult();
                        pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
                        if expectedresult in actualresult and pid:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6:lbd process should be running";
                            print "ACTUAL RESULT 6: PID of lbd %s" %pid;
                            print "TEST EXECUTION RESULT :SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6:lbd process should be running";
                            print "ACTUAL RESULT 6: PID of lbd %s" %pid;
                            print "TEST EXECUTION RESULT :FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Set same SSID for 2.4GHZ and 5GHZ"
                        print "ACTUAL RESULT 5 : %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4:Check if lbd process is running";
                    print "ACTUAL RESULT 4: lbd process is running";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable|%s|bool|Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(orgValue[0],orgValue[1],orgValue[2]));
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP :Revert BandSteering enable status and different wifi SSID names for 2.4GHZ and 5 GHZ"
                    print "ACTUAL RESULT : %s" %details;
                    print "TEST EXECUTION RESULT :SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP :Set BandSteering enable status and different wifi SSID names for 2.4GHZ and 5 GHZ"
                    print "ACTUAL RESULT : %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Set BandSteering enable status as true and different wifi SSID names for 2.4GHZ and 5 GHZ"
                print "ACTUAL RESULT 3: %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the enable status of bandsteering and SSID names";
            print "ACTUAL RESULT 2: Failed to get Bandsteering enable status and SSID names";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
    pamobj.unloadModule("pam");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";



