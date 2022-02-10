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
  <version>9</version>
  <name>TS_WIFIAGENT_CheckWiFiSSIDStatus_InBridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the WiFi SSID statuses is "down" when DUT is set to bridge-static mode.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_170</test_case_id>
    <test_objective>To check if the WiFi SSID statuses is "down" when DUT is set to bridge-static mode.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramValue : bridge-static
paramType : string
paramName : Device.WiFi.SSID.1.Status
paramName : Device.WiFi.SSID.2.Status
paramName : Device.WiFi.SSID.17.Status</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial lanmode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
3. Set to bridge-static if the lanmode was router initially. Cross check the SET with GET.
4. Check the WiFi SSID status for all applicable radios using Device.WiFi.SSID.1.Status, Device.WiFi.SSID.2.Status and Device.WiFi.SSID.17.Status for 2.4G, 5G and 6G respectively. All the statuses should be Down in bridge mode.
5. Revert to initial lanmode if required.
6. Unload the modules</automation_approch>
    <expected_output>The WiFi SSID statuses should be "down" when DUT is set to bridge-static mode.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckWiFiSSIDStatus_InBridgeMode</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getParameter(tdkTestObj, param):
    tdkTestObj.addParameter("paramName",param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    getValue = tdkTestObj.getResultDetails().strip();
    getValue = getValue.split("VALUE:")[1].split(" ")[0].strip();
    return actualresult, getValue;

def setLanMode(tdkTestObj, setValue):
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
    tdkTestObj.addParameter("paramValue",setValue);
    tdkTestObj.addParameter("paramType","string");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    sleep(120);
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *;
from time import sleep;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckWiFiSSIDStatus_InBridgeMode');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckWiFiSSIDStatus_InBridgeMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the current Lan Mode
    step = 1;
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    param = "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode";
    actualresult, lanmodeInitial = getParameter(tdkTestObj, param);

    print "\nTEST STEP %d: Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
    print "EXPECTED RESULT %d: Should get the initial Lan Mode successfully" %step;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: GET operation success; Lanmode is : %s" %(step, lanmodeInitial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set to bridge mode if not already in bridge mode
        revert_flag = 0;
        if lanmodeInitial == "router":
            step = step + 1;
            currLanMode = "router";
            setValue = "bridge-static";
            #Change the Lan Mode
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            actualresult, details = setLanMode(tdkTestObj, setValue);

            print "\nTEST STEP %d: Transition the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, setValue);
            print "EXPECTED RESULT %d: Should set the Lan Mode to %s successfully" %(step, setValue);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Lan Mode set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the Lan Mode is set properly
                sleep(20);
                step = step + 1;
                tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                param = "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode";
                actualresult, currLanMode = getParameter(tdkTestObj, param);

                print "\nTEST STEP %d: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
                print "EXPECTED RESULT %d: Should get the current Lan Mode as %s" %(step, setValue);

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: GET operation success; Lanmode is : %s" %(step, currLanMode);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if currLanMode == setValue :
                        revert_flag = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "SET does not reflects in GET";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: GET operation failed; Lanmode is : %s" %(step, currLanMode);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Lan Mode not set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("SUCCESS");
            print "Lanmode already is bridge-static";

        if lanmodeInitial == "bridge-static" or currLanMode == "bridge-static":
            step = step + 1;
            print "\nTEST STEP %d: Check the WiFi SSID status corresponding to the all the applicable radios in bridge mode" %step;
            print "EXPECTED RESULT %d: The WiFi SSID status corresponding to all the appliacable radios should be down in bridge mode" %step;

            #Get 2.4G WiFi SSID Status
            print "\nFetching the WiFi SSID Status for 2.4G...";
            param = "Device.WiFi.SSID.1.Status";
            actualresult1, ssid_1_status = getParameter(tdkTestObj, param);

            if expectedresult in actualresult1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Device.WiFi.SSID.1.Status : %s" %ssid_1_status;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Device.WiFi.SSID.1.Status not retrieved";

            #Get 5G WiFi SSID Status
            print "\nFetching the WiFi SSID Status for 5G...";
            param = "Device.WiFi.SSID.2.Status";
            actualresult2, ssid_2_status = getParameter(tdkTestObj, param);

            if expectedresult in actualresult2:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Device.WiFi.SSID.2.Status : %s" %ssid_2_status;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Device.WiFi.SSID.2.Status not retrieved";

            #Check if 6G is applicable
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "sh %s/tdk_utility.sh parseConfigFile RADIO_IF_6G" %TDK_PATH;
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            ssid_17_status = "";

            if expectedresult in actualresult and details != "":
                #Get 6G WiFi SSID Status
                applicable_6G = 1;
                print "\nFetching the WiFi SSID Status for 6G...";
                param = "Device.WiFi.SSID.17.Status";
                actualresult3, ssid_17_status = getParameter(tdkTestObj, param);

                if expectedresult in actualresult3:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Device.WiFi.SSID.17.Status : %s" %ssid_17_status;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Device.WiFi.SSID.17.Status not retrieved";
            else:
                print "\n6G not applicable...";
                applicable_6G = 0;

            if applicable_6G == 1:
                if ssid_1_status == "Down" and ssid_2_status == "Down" and ssid_17_status == "Down":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: All WiFi SSID statuses are down in bridge-mode" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: All WiFi SSID statuses are not down in bridge-mode" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                if ssid_1_status == "Down" and ssid_2_status == "Down" :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: All WiFi SSID statuses are down in bridge-mode" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: All WiFi SSID statuses are not down in bridge-mode" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert operation
            if revert_flag == 1:
                step = step + 1;
                setValue = "router";
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                actualresult, details = setLanMode(tdkTestObj, setValue);

                print "\nTEST STEP %d: Transition the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, setValue);
                print "EXPECTED RESULT %d: Should set the Lan Mode to %s successfully" %(step, setValue);

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Lan Mode set successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Lan Mode not set successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Revert operation not required";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "Lanmode could not be set to bridge-static";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: GET operation failed; Lanmode is : %s" %(step, lanmodeInitial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysobj.unloadModule("sysutil");
    obj.unloadModule("wifiagent");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");

