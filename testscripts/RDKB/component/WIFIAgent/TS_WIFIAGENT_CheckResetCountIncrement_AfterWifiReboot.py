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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>6</version>
  <name>TS_WIFIAGENT_CheckResetCountIncrement_AfterWifiReboot</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the radio reset count for all applicable radios are incremented by 1 when wifi reboot operation is done using Device.X_CISCO_COM_DeviceControl.RebootDevice.</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
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
    <test_case_id>TC_WIFIAGENT_193</test_case_id>
    <test_objective>To check if the radio reset count for all applicable radios are incremented by 1 when wifi reboot operation is done using Device.X_CISCO_COM_DeviceControl.RebootDevice.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.Radio.{i}.RadioResetCount
paramName : Device.X_CISCO_COM_DeviceControl.RebootDevice
paramValue : Wifi
Type : string
</input_parameters>
    <automation_approch>1. Load the modules
2. Retrieve the number of applicable radios
3. Get the initial reset counts using Device.WiFi.Radio.{i}.RadioResetCount
4. Perform wifi reboot using Device.X_CISCO_COM_DeviceControl.RebootDevice
5. Sleep for 90s for the wifi reboot to take effect
6. Retrieve the final reset counts using Device.WiFi.Radio.{i}.RadioResetCount
7. Check if the reset counts are incremented by 1
8. Unload the modules</automation_approch>
    <expected_output>The radio reset count for all applicable radios should be incremented by 1 when wifi reboot is done using Device.X_CISCO_COM_DeviceControl.RebootDevice</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckResetCountIncrement_AfterWifiReboot</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getValues(obj, num_of_radios):
    Value = [];
    status = 0;
    for index in range(1, num_of_radios+1):
        param = "Device.WiFi.Radio." + str(index) + ".RadioResetCount";
        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName",param)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        if expectedresult in actualresult and details != "":
            details = details.split("VALUE:")[1].split(" ")[0].strip();
            Value.append(details);
            print "\n%s : %s" %(param, Value[index-1]);

            if Value[index-1].isdigit():
                print "Radio Reset Count retrieved is a valid integer";
                continue;
            else:
                print "Radio Reset Count retrieved is not a valid integer";
                status = 1;
                break;
        else :
            status = 1;
            print "%s : %s" %(param, details);
            break;
    return status, Value;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckResetCountIncrement_AfterWifiReboot');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckResetCountIncrement_AfterWifiReboot');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Check if 6G is applicable
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    cmd = "sh %s/tdk_utility.sh parseConfigFile PRIVATE_6G_AP_INDEX" %TDK_PATH;
    tdkTestObj.addParameter("command", cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and details != "":
        print "\n6G applicable for the DUT...";
        num_of_radios = 3;
    else:
        print "\n6G not applicable for the DUT...";
        num_of_radios = 2;

    #Get the initial reset counts
    print "\nTEST STEP 1 : Get the Initial Radio Reset Count for all applicable radios";
    print "EXPECTED RESULT 1 : Should get the Radio Reset Count for all applicable radios";

    status, initialValue = getValues(obj, num_of_radios);

    if status == 0 :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1 : Initial Radio Reset Counts are retrieved successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Reboot Wifi
        tdkTestObj = obj.createTestStep("WIFIAgent_Set");
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.RebootDevice");
        tdkTestObj.addParameter("paramValue","Wifi");
        tdkTestObj.addParameter("paramType","string");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "\nTEST STEP 2 : Initiate WiFi reboot using Device.X_CISCO_COM_DeviceControl.RebootDevice";
        print "EXPECTED RESULT 2 : The WiFi reboot operation should be successful";

        if expectedresult in actualresult and details != "" :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2 : WiFi reboot operation was success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Sleep for 90s for the WiFi reboot operation to take effect
            print "Sleeping 90s for the WiFi reboot operation...";
            sleep(90);

            #Get the final reset counts
            print "\nTEST STEP 3 : Get the Radio Reset Count for all applicable radios after WiFi reboot";
            print "EXPECTED RESULT 3 : Should get the Radio Reset Count for all applicable radios after WiFi reboot";

            status, finalValue = getValues(obj, num_of_radios);

            if status == 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3 : Final Radio Reset Counts are retrieved successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the reset counts are incremented by 1
                print "\nTEST STEP 4 : Check if the Radio Reset Counts are incremented by 1";
                print "EXPECTED RESULT 4 : The Radio Reset counts should be incremented by 1";

                result = 0;
                for index in range(1, num_of_radios+1):
                    param = "Device.WiFi.Radio." + str(index) + ".RadioResetCount";
                    print "\nFor %s, initial reset count : %s, final reset count : %s" %(param, initialValue[index-1], finalValue[index-1]);

                    if int(finalValue[index-1]) == int(initialValue[index-1]) + 1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "%s is incremented by 1" %param;
                    else:
                        result = 1;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "%s is NOT incremented by 1" %param;

                if result == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4 : The Radio Reset Counts are incremented by 1";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4 : The Radio Reset Counts are NOT incremented by 1";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3 : Final Radio Reset Counts are NOT retrieved successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2 : WiFi reboot operation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1 : Initial Radio Reset Counts are NOT retrieved successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
