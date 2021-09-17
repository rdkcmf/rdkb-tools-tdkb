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
  <name>TS_WIFIAGENT_TelemetryMarker_WIFIConfigChange</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if RDKB_WIFI_CONFIG_CHANGED telemetry marker is logged when Security Mode Enabled is changed to new value</synopsis>
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
    <test_case_id>TC_WIFIAGENT_156</test_case_id>
    <test_objective>To check if RDKB_WIFI_CONFIG_CHANGED telemetry marker is logged when Security Mode Enabled is changed to new value</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.1.Security.ModeEnabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the current security mode enabled
3.Set the security mode enabled to "None"
4.Check if Telemetry marker RDKB_WIFI_CONFIG_CHANGED is logged
5.Revert the security mode Enabled value to the initial value
6.Unload the module</automation_approch>
    <expected_output>With change in Security mode RDKB_WIFI_CONFIG_CHANGED maker should be logged </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_TelemetryMarker_WIFIConfigChange</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
obj1= tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_TelemetryMarker_WIFIConfigChange');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_TelemetryMarker_WIFIConfigChange');

#result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        default = default.split("VALUE:")[1].split(" ")[0].strip();
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current WiFi Security mode enabled";
        print "EXPECTED RESULT 1: Should get current WiFi Security mode enabled";
        print "ACTUAL RESULT 1: current WiFi Security mode enabled is %s" %default;
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled")
        tdkTestObj.addParameter("paramValue", "None");
        tdkTestObj.addParameter("paramType","string")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the WiFi Security mode to None";
            print "EXPECTED RESULT 2: Should set the WiFi Security mode to None";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #wait for the logging to take place
            sleep(30);
            print "Check if the device is dual core or not since WiFi logging takes place on arm side"
            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            RPCCmd = "sh %s/tdk_utility.sh parseConfigFile RPC_CMD" %TDK_PATH;
            tdkTestObj.addParameter("command", RPCCmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            RPC_CMD = tdkTestObj.getResultDetails().strip();
            RPC_CMD = RPC_CMD.replace("\\n", "");
            if RPC_CMD:
               print "The device needs rpc command";
               cmd = RPC_CMD + " 'cat /rdklogs/logs/WiFilog.txt.0' | grep -rn \'RDKB_WIFI_CONFIG_CHANGED\' ";
            else:
                print "The device doesn't need rpc command"
                cmd = "cat /rdklogs/logs//WiFilog.txt.0 | grep -rn \"RDKB_WIFI_CONFIG_CHANGED\" ";

            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and "RDKB_WIFI_CONFIG_CHANGED"  in details:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if RDKB_WIFI_CONFIG_CHANGED is present in WiFilog.txt.0";
                print "EXPECTED RESULT 3: RDKB_WIFI_CONFIG_CHANGED should be present in WiFilog.txt.0 ";
                print "ACTUAL RESULT 3: %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if RDKB_WIFI_CONFIG_CHANGED is present in WiFilog.txt.0";
                print "EXPECTED RESULT 3: RDKB_WIFI_CONFIG_CHANGED should be present in WiFilog.txt.0 ";
                print "ACTUAL RESULT 3: %s" %details;
                print "[TEST EXECUTION RESULT] :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the WiFi Security mode to None";
            print "EXPECTED RESULT 2: Should set Security mode to None";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        #revert operation
        if default !="None":
           tdkTestObj = obj.createTestStep('WIFIAgent_Set');
           tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled")
           tdkTestObj.addParameter("paramValue", default);
           tdkTestObj.addParameter("paramType","string")
           tdkTestObj.executeTestCase("expectedresult");
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 4: Revert the WiFi Security mode to previous";
               print "EXPECTED RESULT 4: Should revert  Security mode enabled to %s" %default;
               print "ACTUAL RESULT 4: %s" %details;
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 4: Revert the WiFi Security mode to previous";
               print "EXPECTED RESULT 4: Should revert  Security mode enabled to %s" %default;
               print "ACTUAL RESULT 4: %s" %details;
               print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current WiFi Security mode enabled";
        print "EXPECTED RESULT 1: Should get current WiFi Security mode enabled";
        print "ACTUAL RESULT 1: current WiFi Security mode enabled is %s" %default;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent")
    obj1.unloadModule("sysutil");
else:
    print "Failed to load wifiagent/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
