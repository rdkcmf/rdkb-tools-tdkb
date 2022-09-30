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
  <version>7</version>
  <name>TS_WIFIAGENT_5GHzOffChannelTScanValidation</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if time taken for a single channel scan, Device.WiFi.Radio.2.X_RDK_OffChannelTscan, returns a valid value in range 0-63 msec and setting it to another valid value, 0 (Off channel scan disabled state) returns success and setting to out of bounds value fails when the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable value is enabled.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIAGENT_218</test_case_id>
    <test_objective>To check if time taken for a single channel scan, Device.WiFi.Radio.2.X_RDK_OffChannelTscan, returns a valid value in range 0-63 msec and setting it to another valid value, 0 (Off channel scan disabled state) returns success and setting to out of bounds value fails when the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable value is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.Radio.2.X_RDK_OffChannelTscan
paramValue : values in range [0, 63], randomly generated invalid values &gt; 63
paramType : unsigned int</input_parameters>
    <automation_approch>1. Load the wifiagent module
2. As pre-requisite enable the off channel scan controlling RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable if not already enabled.
3. Get the initial value of T scan parameter Device.WiFi.Radio.2.X_RDK_OffChannelTscan which represents the time in msec during which a channel is scanned.
4. Check if the T scan value is within the acceptable range of 0 to 63.
5. Set the parameter to a new value within the acceptable range excluding the initial value and  validate with get.
6. Set T scan to 0, which implies that off channel scan is disabled and validate with get.
7. Set T scan to an invalid value that is out of range and check if the set operation fails.
9. Revert T scan to initial value
10. Revert the controlling RFC if required.
11. Unload the wifiagent module.</automation_approch>
    <expected_output>Device.WiFi.Radio.2.X_RDK_OffChannelTscan should return a valid value in range 0-63 msec and setting it to another valid value, 0 (Off channel scan disabled state) should return success and setting to out of bounds value should fail when the Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable value is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzOffChannelTScanValidation</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getParameter(obj, param, expectedresult):
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName", param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

def setParameter(obj, param, setValue, type, expectedresult):
    tdkTestObj = obj.createTestStep('WIFIAgent_Set_Get');
    tdkTestObj.addParameter("paramName",param);
    tdkTestObj.addParameter("paramValue",setValue);
    tdkTestObj.addParameter("paramType",type);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;
from tdkutility import *;
from random import choice;
from random import randint;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzOffChannelTScanValidation');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Set the pre-requisites
    step = 1;
    print "\n*************Set Pre-requisite Start*****************";
    tdkTestObj, pre_req_set, revert_flag, step = WiFiOffChannelScanEnable_PreReq(obj, step);

    if pre_req_set == 0:
        print "\n*************Set Pre-requisite Complete*****************";
        #Get the initial T scan value
        step = step + 1;
        param = "Device.WiFi.Radio.2.X_RDK_OffChannelTscan"

        print "\nTEST STEP %d: Get the initial value of time that a single channel is scanned using Device.WiFi.Radio.2.X_RDK_OffChannelTscan" %step;
        print "EXPECTED RESULT %d: Should get the value of Device.WiFi.Radio.2.X_RDK_OffChannelTscan successfully" %step;
        actualresult, details = getParameter(obj, param, expectedresult);

        if expectedresult in actualresult and details != "":
            tscan_initial = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Off channel T scan : %s" %(step, tscan_initial);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the T scan is in the valid range of 0 to 63
            step = step + 1;
            print "\nTEST STEP %d: Check if the value retrieved for Device.WiFi.Radio.2.X_RDK_OffChannelTscan is within the valid range of 0 to 63" %step;
            print "EXPECTED RESULT %d: The value of Device.WiFi.Radio.2.X_RDK_OffChannelTscan should be within the valid range of 0 to 63" %step;

            if tscan_initial.isdigit() and (int(tscan_initial) >= 0) and (int(tscan_initial) <= 63):
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Off Channel T scan is within the valid range of [0, 63]" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Set Device.WiFi.Radio.2.X_RDK_OffChannelTscan to a valid value within the range and validate the set
                step = step + 1;
                paramName = "Device.WiFi.Radio.2.X_RDK_OffChannelTscan";
                set_val = str(choice([val for val in range(1,64) if val not in [int(tscan_initial)]]))
                print "\nTEST STEP %d: Set Device.WiFi.Radio.2.X_RDK_OffChannelTscan to %s within the valid range" %(step, set_val);
                print "EXPECTED RESULT %d: Device.WiFi.Radio.2.X_RDK_OffChannelTscan should be set successfully" %step;
                actualresult, details = setParameter(obj, paramName, set_val, "unsignedint", expectedresult);

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: T scan set successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Set Device.WiFi.Radio.2.X_RDK_OffChannelTscan to 0 - to disable off channel scan
                    step = step + 1;
                    set_val = "0";
                    print "\nTEST STEP %d: Set Device.WiFi.Radio.2.X_RDK_OffChannelTscan to %s to disable off channel scan" %(step, set_val);
                    print "EXPECTED RESULT %d: Device.WiFi.Radio.2.X_RDK_OffChannelTscan should be set successfully" %step;
                    actualresult, details = setParameter(obj, paramName, set_val, "unsignedint", expectedresult);

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: T scan set successfully to disable off channel scan; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Set Device.WiFi.Radio.2.X_RDK_OffChannelTscan to out of range value and check if set operation fails
                        step = step + 1;
                        set_val = randint(64,100);
                        expectedresult = "FAILURE";
                        print "\nTEST STEP %d: Set Device.WiFi.Radio.2.X_RDK_OffChannelTscan to %d to out of range value" %(step, set_val);
                        print "EXPECTED RESULT %d: Device.WiFi.Radio.2.X_RDK_OffChannelTscan should not be set successfully" %step;
                        actualresult, details = setParameter(obj, paramName, str(set_val), "unsignedint", expectedresult);

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: T scan set failed for out of range value; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: T scan set success for out of range value; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: T scan NOT set successfully to disable off channel scan; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Revert T scan to initial value
                    expectedresult = "SUCCESS";
                    step = step + 1;
                    set_val = tscan_initial;
                    print "\nTEST STEP %d: Revert Device.WiFi.Radio.2.X_RDK_OffChannelTscan to %s" %(step, set_val);
                    print "EXPECTED RESULT %d: Device.WiFi.Radio.2.X_RDK_OffChannelTscan should be reverted successfully" %step;
                    actualresult, details = setParameter(obj, paramName, set_val, "unsignedint", expectedresult);

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: T scan revert is success; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: T scan revert failed; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: T scan NOT set successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Off Channel T scan is NOT within the valid range of [0, 63]" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Off channel T scan : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Revert the pre-requisites
        step = step + 1;
        print "\n*************Revert Pre-requisite Start*****************";
        WiFiOffChannelScanEnable_Revert(obj, revert_flag, step);
        print "\n*************Revert Pre-requisite Complete*****************";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Unable to enable the pre-requisites, cannot proceed..";

    obj.unloadModule("wifiagent")
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
