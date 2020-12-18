##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_WIFIAGENT_ForceDisable_SetWiFiSSIDParams</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if VAP 1-6 SSID's are not writable when WiFi Force Disable is enabled</synopsis>
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
    <test_case_id>TC_WIFIAGENT_131</test_case_id>
    <test_objective>This test case is to check if VAP 1-6 SSID's are not writable when WiFi Force Disable is enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get
WIFIAgent_Set
</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.1.SSID
Device.WiFi.SSID.2.SSID
Device.WiFi.SSID.3.SSID
Device.WiFi.SSID.4.SSID
Device.WiFi.SSID.5.SSID
Device.WiFi.SSID.6.SSID
Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value for Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
3.Enable Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
4.Do a write operation on the following parameters
"Device.WiFi.SSID.1.SSID","Device.WiFi.SSID.2.SSID","Device.WiFi.SSID.3.SSID","Device.WiFi.SSID.4.SSID","Device.WiFi.SSID.5.SSID","Device.WiFi.SSID.6.SSID" ,and this write operation is expected to fail
5.Check if log message WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED" is present in WiFilog.txt.0 each time write operation is done
6.Unload the module</automation_approch>
    <expected_output>Write operation on the listed wifi parameters should fail and
"WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED " message should be present in WiFilog.txt.0  each time a set operation is done when WiFi Force Disable is enabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_ForceDisable_SetWiFiSSIDParams</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
obj1= tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_ForceDisable_SetWiFiSSIDParams');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_ForceDisable_SetWiFiSSIDParams');

#result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

def getTelLogFileTotalLinesCount(tdkTestObj):
    expectedresult="SUCCESS";
    linecount =0;
    RPCCmd = "sh %s/tdk_utility.sh parseConfigFile RPC_CMD" %TDK_PATH;
    tdkTestObj.addParameter("command", RPCCmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    RPC_CMD = tdkTestObj.getResultDetails().strip()
    RPC_CMD = RPC_CMD.replace("\\n", "");
    if RPC_CMD:
       print "The device needs rpc command";
       cmd = RPC_CMD + " \"cat /rdklogs/logs/WiFilog.txt.0 | wc -l \" | grep -v \"*\" | sed -r \"/^\s*$/d\" ";
    else:
        cmd = "cat /rdklogs/logs/WiFilog.txt.0| wc -l";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult:
       print "current WiFilog.txt.0 line count:",details;
       if details.isdigit():
          linecount = int(details);
    return actualresult,linecount;

def SetOperation(tdkTestObj,parameter):
    expectedresult="FAILURE";
    tdkTestObj.addParameter("paramName",parameter)
    tdkTestObj.addParameter("paramValue", "tdkbtestcase");
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,expectedresult;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        default = default.split("VALUE:")[1].split(" ")[0].strip();
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current WiFi Force Disable state";
        print "EXPECTED RESULT 1: Should get current WiFi Force Disable state";
        print "ACTUAL RESULT 1: current WiFi Force Disable state is %s" %default;
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
        tdkTestObj.addParameter("paramValue", "true");
        tdkTestObj.addParameter("paramType","boolean")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Enable the WiFi Force Disable";
           print "EXPECTED RESULT 2: Should enable Force Disable state";
           print "ACTUAL RESULT 2: %s" %details;
           print "[TEST EXECUTION RESULT] : SUCCESS";

           params = ["Device.WiFi.SSID.1.SSID","Device.WiFi.SSID.2.SSID","Device.WiFi.SSID.3.SSID","Device.WiFi.SSID.4.SSID","Device.WiFi.SSID.5.SSID","Device.WiFi.SSID.6.SSID"]
           for parameter in params:
               tdkTestObj = obj1.createTestStep('ExecuteCmd');
               lineCountResult, initialLinesCount = getTelLogFileTotalLinesCount(tdkTestObj);
               if expectedresult in lineCountResult:
                  tdkTestObj.setResultStatus("SUCCESS");
                  tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                  print "***performing write operation on  %s ****" %parameter;
                  actualresult,expectedResult= SetOperation(tdkTestObj,parameter);
                  if expectedResult in actualresult:
                     sleep(10);
                     tdkTestObj = obj1.createTestStep('ExecuteCmd');
                     lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj);
                     if expectedresult in lineCountResult1:
                        tdkTestObj = obj1.createTestStep('ExecuteCmd');
                        RPCCmd = "sh %s/tdk_utility.sh parseConfigFile RPC_CMD" %TDK_PATH;
                        tdkTestObj.addParameter("command", RPCCmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        RPC_CMD = tdkTestObj.getResultDetails().strip();
                        RPC_CMD = RPC_CMD.replace("\\n", "");
                        if RPC_CMD:
                           print "The device needs rpc command";
                           cmd = RPC_CMD + " 'sed -n -e %s,%sp /rdklogs/logs/WiFilog.txt.0 | grep -i \"WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED\" ' "%(initialLinesCount,lineCountAfterSimu);
                        else:
                            cmd = "sed -n -e %s,%sp /rdklogs/logs/WiFilog.txt.0 | grep -i \"WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED\"" %(initialLinesCount,lineCountAfterSimu) ;
                        print "cmd:",cmd;
                        print "WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED log message should be present in WiFilog.txt.0";
                        tdkTestObj.addParameter("command", cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                        if expectedresult in actualresult and "WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED"  in details:
                           tdkTestObj.setResultStatus("SUCCESS");
                           print details;
                           print "[TEST EXECUTION RESULT] :SUCCESS";
                           print "********************************************";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "WIFI_ATTEMPT_TO_CHANGE_CONFIG_WHEN_FORCE_DISABLED  didnot populate when trying to set %s in WiFilog.txt.0" %parameter;
                            print "[TEST EXECUTION RESULT] :FAILURE";
                            print "*****************************************";
                     else:
                         tdkTestObj.setResultStatus("FAILURE");
                         print "*******Failed get the line count of the log file*****";
                  else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print "%s set was success even with Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable  being enabled";
                      print "*********************************************"
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "*******Failed get the line count of the log file*****";
           #Revertion
           tdkTestObj = obj.createTestStep('WIFIAgent_Set');
           tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
           tdkTestObj.addParameter("paramValue", default);
           tdkTestObj.addParameter("paramType","boolean")
           tdkTestObj.executeTestCase("expectedresult");
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails();

           if expectedresult in actualresult:
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP : Revert the WiFi Force Disable to previous";
              print "EXPECTED RESULT : Should revert  Force Disable state to %s" %default;
              print "ACTUAL RESULT : %s" %details;
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP : Revert the WiFi Force Disable to previous";
               print "EXPECTED RESULT : Should revert  Force Disable state to %s" %default;
               print "ACTUAL RESULT : %s" %details;
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Disable the WiFi Force Disable";
            print "EXPECTED RESULT 2: Should Disable Force Disable state";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current WiFi Force Disable state";
        print "EXPECTED RESULT 1: Should get current WiFi Force Disable state";
        print "ACTUAL RESULT 1: current WiFi Force Disable state is %s" %default;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent")
    obj1.unloadModule("sysutil");
else:
    print "Failed to load wifiagent/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
