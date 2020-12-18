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
  <name>TS_WIFIAGENT_ForceDisable_CheckForLogs</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if expected log messages are present on toggling WiFi Force Disable</synopsis>
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
    <test_case_id>TC_WIFIAGENT_124</test_case_id>
    <test_objective>This test case is to check if expected log messages are present on toggling WiFi Force Disable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get
WIFIAgent_Set</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
3.Toggle the Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable   vlaue
4.Check if WIFI_FORCE_DISABLE_CHANGED_TO_TRUE on enabling and WIFI_FORCE_DISABLE_CHANGED_TO_FALSE on disabling are present in WiFilog.txt.0
4.Revert the Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to previous value
5.unload the module</automation_approch>
    <expected_output>The expected log message should be present when Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable is toggled</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_ForceDisable_CheckForLogs</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
obj1= tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_ForceDisable_CheckForLogs');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_ForceDisable_CheckForLogs');

#result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

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

        if "false" in default:
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
                 cmd = RPC_CMD + " 'tail -l  /rdklogs/logs/WiFilog.txt.0' | grep -rn \'WIFI_FORCE_DISABLE_CHANGED_TO_TRUE\' ";
              else:
                  print "The device doesn't need rpc command"
                  cmd = "tail -1 /rdklogs/logs//WiFilog.txt.0 | grep -rn \"WIFI_FORCE_DISABLE_CHANGED_TO_TRUE\" ";

              tdkTestObj.addParameter("command", cmd);
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
              if expectedresult in actualresult and "WIFI_FORCE_DISABLE_CHANGED_TO_TRUE"  in details:
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 3: Check if WIFI_FORCE_DISABLE_CHANGED_TO_TRUE is present in WiFilog.txt.0";
                 print "EXPECTED RESULT 3: WIFI_FORCE_DISABLE_CHANGED_TO_TRUE should be present in WiFilog.txt.0 ";
                 print "ACTUAL RESULT 3: %s" %details;
                 print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 3: Check if WIFI_FORCE_DISABLE_CHANGED_TO_TRUE is present in WiFilog.txt.0";
                  print "EXPECTED RESULT 3: WIFI_FORCE_DISABLE_CHANGED_TO_TRUE should be present in WiFilog.txt.0 ";
                  print "ACTUAL RESULT 3: %s" %details;
                  print "[TEST EXECUTION RESULT] :FAILURE";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2: Enable the WiFi Force Disable";
               print "EXPECTED RESULT 2: Should enable Force Disable state";
               print "ACTUAL RESULT 2: %s" %details;
               print "[TEST EXECUTION RESULT] : FAILURE";

        else:
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
            tdkTestObj.addParameter("paramValue", "false");
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 2: Disable the WiFi Force Disable";
               print "EXPECTED RESULT 2: Should Disable Force Disable state";
               print "ACTUAL RESULT 2: %s" %details;
               print "[TEST EXECUTION RESULT] : SUCCESS";

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
                  cmd = RPC_CMD + " 'tail -1 /rdklogs/logs/WiFilog.txt.0' | grep -rn \'WIFI_FORCE_DISABLE_CHANGED_TO_FALSE\' ";
               else:
                   print "The device doesn't need rpc command"
                   cmd = "tail -1 /rdklogs/logs//WiFilog.txt.0 | grep -rn \"WIFI_FORCE_DISABLE_CHANGED_TO_FALSE\" ";

               tdkTestObj.addParameter("command", cmd);
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
               if expectedresult in actualresult and "WIFI_FORCE_DISABLE_CHANGED_TO_FALSE" in details:
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 3: Check if WIFI_FORCE_DISABLE_CHANGED_TO_FALSE is present in WiFilog.txt.0";
                  print "EXPECTED RESULT 3: WIFI_FORCE_DISABLE_CHANGED_TO_FALSE should be present in WiFilog.txt.0 ";
                  print "ACTUAL RESULT 3: %s" %details;
                  print "[TEST EXECUTION RESULT] : SUCCESS";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "TEST STEP 3: Check if WIFI_FORCE_DISABLE_CHANGED_TO_FALSE is present in WiFilog.txt.0";
                   print "EXPECTED RESULT 3: WIFI_FORCE_DISABLE_CHANGED_TO_FALSE should be present in WiFilog.txt.0 ";
                   print "ACTUAL RESULT 3: %s" %details;
                   print "[TEST EXECUTION RESULT] :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Disable the WiFi Force Disable";
                print "EXPECTED RESULT 2: Should Disable Force Disable state";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE";

        #revert operation
        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
        tdkTestObj.addParameter("paramValue", default);
        tdkTestObj.addParameter("paramType","boolean")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 4: Revert the WiFi Force Disable to previous";
           print "EXPECTED RESULT 4: Should revert  Force Disable state to %s" %default;
           print "ACTUAL RESULT 4: %s" %details;
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Revert the WiFi Force Disable to previous";
            print "EXPECTED RESULT 4: Should revert  Force Disable state to %s" %default;
            print "ACTUAL RESULT 4: %s" %details;
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
