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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckBandsteeringEnable_WithSplitSSID</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the set operation of Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable returns failure when the SSIDs Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID are split.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIAGENT_157</test_case_id>
    <test_objective>Check if the set operation of Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable returns failure when the SSIDs Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID are split.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable
Device.WiFi.SSID.1.SSID
Device.WiFi.SSID.2.SSID
Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting
Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting
</input_parameters>
    <automation_approch>1. Load the module.
2. Get the initial values of Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable, Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID
3. If the SSIDs are not split, set them to new values and check if the Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable can be set to "true". The script should return failure if the SET operation succeeds.
4. If the SSIDs are split, check if Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable is false as expected.
5. Unload the module</automation_approch>
    <expected_output>The set operation of Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable should return failure when the SSIDs Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID are split.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckBandsteeringEnable_WithSplitSSID</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckBandsteeringEnable_WithSpliSSID');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckBandsteeringEnable_WithSplitSSID');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
SSID1 = "TESTSSID1"
SSID2 = "TESTSSID2"

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    paramList=["Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable", "Device.WiFi.SSID.1.SSID", "Device.WiFi.SSID.2.SSID"]
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)

    print "\nTEST STEP 1: Get the values of Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable, Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID";
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: BandStering enable status and SSID names are respectively : %s, %s, %s" %(orgValue[0],orgValue[1],orgValue[2]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if the SSID names are same
        if orgValue[1] == orgValue[2]:
            print "As SSID names are same, changing to Split SSID";
            tdkTestObj = obj1.createTestStep("WIFIAgent_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string" %(SSID1,SSID2));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 2 : Set Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID to different values";
            print "EXPECTED RESULT 2 : Should successfully set Device.WiFi.SSID.1.SSID to %s and Device.WiFi.SSID.2.SSID to %s" %(SSID1, SSID2);

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Set operation success; Details : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";

                #Validate the SET with GET
                paramList=["Device.WiFi.SSID.1.SSID", "Device.WiFi.SSID.2.SSID"]
                tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)

                print "\nTEST STEP 3: Get the values of Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID";
                print "EXPECTED RESULT 3: The values should be retrieved successfully and should be the same as set values";

                if expectedresult in status and setValue[0] == SSID1 and setValue[1] == SSID2 :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: SSID values after the GET are same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Set Band Steering Enable to true, the set should fail
                    expectedresult = "FAILURE"
                    tdkTestObj = obj1.createTestStep("WIFIAgent_SetMultiple");
                    tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable|true|bool");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP 4 : Set Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable to true after Split SSID";
                    print "EXPECTED RESULT 4 : Setting Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable to true after Split SSID should return failure";

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: Set operation failed; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: Set operation success; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Revert to initial SSID values
                    expectedresult = "SUCCESS"
                    tdkTestObj = obj1.createTestStep("WIFIAgent_SetMultiple");
                    tdkTestObj.addParameter("paramList","Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string" %(orgValue[1],orgValue[2]));
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP 5 : Set Device.WiFi.SSID.1.SSID and Device.WiFi.SSID.2.SSID to initial values";
                    print "EXPECTED RESULT 5 : Should successfully set Device.WiFi.SSID.1.SSID to %s and Device.WiFi.SSID.2.SSID to %s" %(orgValue[1], orgValue[2]);

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5 : Set operation success; Details : %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5 : Set operation failed; Details : %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: SSID values after the GET are not same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:Set operation failed; Details : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            print "As the SSIDs are split, the Band Steering Enable should return false";
            if orgValue[0] == "false":
                tdkTestObj.setResultStatus("SUCCESS");
                print "As the SSIDs are split, the Band Steering Enable return false";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "The Band Steering Enable does not return false even when the SSID is split";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Failed to get BandSteering enable status and SSID names; Details : %s" %details;
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

