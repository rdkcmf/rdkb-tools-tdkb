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
  <version>2</version>
  <name>TS_WIFIAGENT_CheckRadioUpTimeReset_AfterWifiReboot</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the radio uptimes of all applicable radios are getting reset after wifi reboot using Device.X_CISCO_COM_DeviceControl.RebootDevice.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIAGENT_194</test_case_id>
    <test_objective>To check if the radio uptimes of all applicable radios are getting reset after wifi reboot using Device.X_CISCO_COM_DeviceControl.RebootDevice.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.Radio.{i}.X_COMCAST_COM_RadioUpTime
paramName : Device.X_CISCO_COM_DeviceControl.RebootDevice
paramValue : Wifi
Type : string
</input_parameters>
    <automation_approch>1. Load the modules
2. Retrieve the number of applicable radios
3. Get the initial uptime of all radios using Device.WiFi.Radio.{i}.X_COMCAST_COM_RadioUpTime
4. If the initial uptime is less than 100s, sleep for a 100s duration to increase the uptime
5. Get the final uptime values for all the radios.
6. Perform wifi reboot operation using Device.X_CISCO_COM_DeviceControl.RebootDevice
7. Sleep for 90s for the wifi reboot operation to take effect
8. Retrieve the uptimes of all radios using Device.WiFi.Radio.{i}.X_COMCAST_COM_RadioUpTime
9. Check if the final uptime is less than the uptime before the wifi reboot operation
10. Unload the modules</automation_approch>
    <expected_output>The radio uptimes of all applicable radios should get reset after wifi reboot operation using Device.X_CISCO_COM_DeviceControl.RebootDevice.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckRadioUpTimeReset_AfterWifiReboot</test_script>
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
        param = "Device.WiFi.Radio." + str(index) + ".X_COMCAST_COM_RadioUpTime";
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
                print "Radio Uptime retrieved is a valid integer";
                continue;
            else:
                print "Radio Uptime retrieved is not a valid integer";
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckRadioUpTimeReset_AfterWifiReboot');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckRadioUpTimeReset_AfterWifiReboot');

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

    #Get the initial radio uptimes
    step = 1;
    print "\nTEST STEP %d : Get the Initial Radio Uptime for all applicable radios" %step;
    print "EXPECTED RESULT %d : Should get the Radio Uptime for all applicable radios" %step;

    status, initialValue = getValues(obj, num_of_radios);

    if status == 0 :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Initial Radio Uptimes are retrieved successfully" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #If initial uptimes are less than 100s, sleep for 100s so that uptime increases
        sleep_flag = 0;
        proceed_flag = 0;
        if num_of_radios == 2:
            if int(initialValue[0]) < 100 or int(initialValue[1]) < 100 :
                print "Sleeping 100s for increasing radio uptime";
                sleep(100);
                sleep_flag = 1;
        else:
            if int(initialValue[0]) < 100 or int(initialValue[1]) < 100 or int(initialValue[2]) < 100:
                print "Sleeping 100s for increasing radio uptime";
                sleep(100);
                sleep_flag = 1;

        if sleep_flag == 1:
            step = step + 1;
            #Get the current radio uptimes
            print "\nTEST STEP %d : Get the Radio Uptime for all applicable radios after 100s sleep" %step;
            print "EXPECTED RESULT %d : Should get the Radio Uptime for all applicable radios" %step;

            status, initialValue = getValues(obj, num_of_radios);

            if status == 0 :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Current Radio Uptimes are retrieved successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else :
                proceed_flag = 1;
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Current Radio Uptimes are NOT retrieved successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Additional sleep time not required as initial radio uptimes are > 100s";

        if proceed_flag == 0:
            #Wifi reboot
            step = step + 1;
            tdkTestObj = obj.createTestStep("WIFIAgent_Set");
            tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.RebootDevice");
            tdkTestObj.addParameter("paramValue","Wifi");
            tdkTestObj.addParameter("paramType","string");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d : Initiate WiFi reboot using Device.X_CISCO_COM_DeviceControl.RebootDevice" %step;
            print "EXPECTED RESULT %d : The WiFi reboot operation should be successful" %step;

            if expectedresult in actualresult and details != "" :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : WiFi reboot operation was success; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Sleep for 90s for the WiFi reboot operation to take effect
                print "Sleeping 90s for the WiFi reboot operation...";
                sleep(90);

                #Get the final radio uptimes
                step = step + 1;
                print "\nTEST STEP %d : Get the Radio Uptime for all applicable radios after WiFi reboot" %step;
                print "EXPECTED RESULT %d : Should get the Radio Uptime for all applicable radios after WiFi reboot" %step;

                status, finalValue = getValues(obj, num_of_radios);

                if status == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Final Radio Uptimes are retrieved successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the radio uptimes are reset
                    step = step + 1;
                    print "\nTEST STEP %d : Check if the Radio Uptimes are reset" %step;
                    print "EXPECTED RESULT %d : The Radio Reset counts should be reset" %step;

                    result = 0;
                    for index in range(1, num_of_radios+1):
                        param = "Device.WiFi.Radio." + str(index) + ".X_COMCAST_COM_RadioUpTime";
                        print "\nFor %s, initial radio uptime : %s, final radio uptime : %s" %(param, initialValue[index-1], finalValue[index-1]);

                        #After wifi reboot the radio uptime should be reset, the final uptime value should be less than the uptime before wifi reboot
                        if int(finalValue[index-1]) < int(initialValue[index-1]) :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "%s is reset" %param;
                        else:
                            result = 1;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "%s is NOT reset" %param;

                    if result == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : The Radio Uptimes after wifi reboot are reset" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : The Radio Uptimes after wifi reboot are NOT reset" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Final Radio Uptimes are NOT retrieved successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : WiFi reboot operation failed; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "Current Uptime values not retrieved..."
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1 : Initial Radio Uptimes are NOT retrieved successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
