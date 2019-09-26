##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetApBeaconType</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get beacon type using the api's wifi_setApBeaconType() and wifi_getApBeaconType() with the corresponding Ap SecurityModeEnabled value</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_133</test_case_id>
    <test_objective>To set and get beacon type using the api's wifi_setApBeaconType() and wifi_getApBeaconType() with the corresponding Ap SecurityModeEnabled value for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBeaconType()
wifi_setApBeaconType()
wifi_getApSecurityModesSupported()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : getApBeaconType
methodName : setApBeaconType
methodName : getApSecurityModesSupported
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
ApIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getApSecurityModesSupported() api to get the ApSecurityModesSupported
3. Get the initial ApBeaconType and ApSecurityModeEnabled values
4. Set the ApBeaconType with the corresponding ApSecurityModeEnabled value.
5. Check whether the set and get values of  ApBeaconType and ApSecurityModeEnabled are equal.
6. If equal return SUCCESS, else FAILURE.
7. Revert the BeaconType and ApSecurityModeEnabled values back to initial values
8. Unload wifihal module</automation_approch>
    <except_output>Set and get values of BeaconType and the corresponding ApSecurityModeEnabled should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApBeaconType</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApBeaconType');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

def GetSetFunction(obj,param,Method) :
    apIndex = 1;
    primitive = 'WIFIHAL_GetOrSetParamStringValue';
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex", apIndex);
    #'param' is valid for only set operations. It isdummy attribute for get functions
    tdkTestObj.addParameter("param", param);
    tdkTestObj.addParameter("methodName", Method);
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj,actualresult,details);

def RevertFunction():
     #Revert the ApSecurityModeEnabled and ApBeaconType back to initial value
     tdkTestObj, actualresultn1, details = GetSetFunction(obj,initMode,"setApSecurityModeEnabled");
     tdkTestObj, actualresultn2, details = GetSetFunction(obj,initialBeaconType,"setApBeaconType");
     if expectedresult in actualresultn1 and actualresultn2 :
         tdkTestObj.setResultStatus("SUCCESS");
         print "Successfully reverted ApSecurityModeEnabled and ApBeaconType back to initial values";
     else :
         tdkTestObj.setResultStatus("FAILURE");
         print "Unable to revert ApSecurityModeEnabled and ApBeaconType back to initial values";


if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObj, actualresult, details = GetSetFunction(obj,"0","getApSecurityModesSupported");
    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
	supportedModes = details.split(":")[1].strip();
        print "**************************************************";
        print "TEST STEP 1: Get list of Ap Security Modes Supported"
        print "EXPECTED RESULT 1: Should get the list of Ap Security Modes Supported successfully";
	print "ACTUAL RESULT 1: Successfully got the Ap Security Modes Supported as %s" %supportedModes;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "**************************************************";
        tdkTestObj, actualresult, details = GetSetFunction(obj,"0","getApSecurityModeEnabled");
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            initMode = details.split(":")[1].strip();
            print "**************************************************";
            print "TEST STEP 2: Get the initial Ap Security Mode Enabled value";
            print "EXPECTED RESULT 2: Should get the initial Ap Security Mode Enabled value successfully";
            print "ACTUAL RESULT 2: Successfully got the Ap Security Mode Enabled value as %s" %initMode;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "**************************************************";
            tdkTestObj, actualresult, details = GetSetFunction(obj,"0","getApBeaconType");
            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                initialBeaconType = details.split(":")[1].strip();
                print "**************************************************";
                print "TEST STEP 3: Get the initial Ap BeaconType";
                print "EXPECTED RESULT 3: Should get the initial Ap BeaconType value successfully";
                print "ACTUAL RESULT 3: Successfully got the Ap BeaconType value as %s" %initialBeaconType;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                print "**************************************************";
                dict_valid = {'None':'None','WPA-Personal':'WPA','WPA-WPA2-Personal':'WPAand11i','WPA2-Personal':'11i'}

                for setMode in supportedModes.split(','):
                    if setMode == initMode :
                        continue;
                    else :
                        print "Ap Security Mode Enabled value to be set is %s" %setMode;
                        if setMode in dict_valid :
                            print "Ap Security Mode Enabled value to be set is within the valid securityMode:beaconType mapping list";
                            setBeaconType = dict_valid.get(setMode);
                            print "Ap BeaconType to be set is %s for the corresponding Ap Security Mode Enabled value : %s"%(setBeaconType,setMode);
                            tdkTestObj, actualresult1, details1 = GetSetFunction(obj,setMode,"setApSecurityModeEnabled");
                            tdkTestObj, actualresult2, details2 = GetSetFunction(obj,setBeaconType,"setApBeaconType");
                            if expectedresult in actualresult1 and actualresult2 :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "**************************************************";
                                print "TEST STEP 4: To set Ap Security Mode Enabled and Ap BeaconType to other values";
                                print "EXPECTED RESULT 4: To successfully set the Ap Security Mode Enabled and Ap BeaconType to other values";
                                print "ACTUAL RESULT 4: Successfully set the Ap Security Mode Enabled and Ap BeaconType to other values";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                print "**************************************************";
                                time.sleep(10);
                                tdkTestObj, actualresult3, details3 = GetSetFunction(obj,"0","getApSecurityModeEnabled");
                                tdkTestObj, actualresult4, details4 = GetSetFunction(obj,"0","getApBeaconType");
                                if expectedresult in actualresult3 and actualresult4 :
                                    finalMode = details3.split(":")[1].strip();
                                    finalBeaconType = details4.split(":")[1].strip();
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "**************************************************";
                                    print "TEST STEP 5: To get Ap Security Mode Enabled and Ap BeaconType values after the set operation";
                                    print "EXPECTED RESULT 5: To successfully get the Ap Security Mode Enabled and Ap BeaconType values";
                                    print "ACTUAL RESULT 5: Successfully got the Ap Security Mode Enabled and Ap BeaconType values as %s and %s"%(finalMode,finalBeaconType);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                    print "**************************************************";
                                    print "setMode : ",setMode;
                                    print "getMode : ",finalMode;
                                    print "setBeaconType : ",setBeaconType;
                                    print "getBeaconType : ",finalBeaconType;
                                    if setMode == finalMode and setBeaconType == finalBeaconType :
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "**************************************************";
                                        print "TEST STEP 6: Compare the set and get values of Ap Security Mode Enabled and Ap BeaconType";
                                        print "EXPECTED RESULT 6: Set and get values of Ap Security Mode Enabled and Ap BeaconType should be same";
                                        print "ACTUAL RESULT 6:  Set and get values of Ap Security Mode Enabled and Ap BeaconType are equal";
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                        print "**************************************************";
                                    else :
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "**************************************************";
                                        print "TEST STEP 6: Compare the set and get values of Ap Security Mode Enabled and Ap BeaconType";
                                        print "EXPECTED RESULT 6: Set and get values of Ap Security Mode Enabled and Ap BeaconType should be same";
                                        print "ACTUAL RESULT 6:  Set and get values of Ap Security Mode Enabled and Ap BeaconType are NOT equal";
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                        print "**************************************************";
                                    #Revert the ApSecurityModeEnabled and ApBeaconType back to initial value
                                    RevertFunction();
                                else :
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "**************************************************";
                                    print "TEST STEP 5: To get Ap Security Mode Enabled and Ap BeaconType values after the set operation";
                                    print "EXPECTED RESULT 5: To successfully get the Ap Security Mode Enabled and Ap BeaconType values";
                                    print "ACTUAL RESULT 5: Failed to get the Ap Security Mode Enabled and Ap BeaconType values after set operation";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                                    print "**************************************************";
                                    RevertFunction();
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "**************************************************";
                                print "TEST STEP 4: To set Ap Security Mode Enabled and Ap BeaconType to other values";
                                print "EXPECTED RESULT 4: To successfully set the Ap Security Mode Enabled and Ap BeaconType to other values";
                                print "ACTUAL RESULT 4: Failed to set the Ap Security Mode Enabled and Ap BeaconType to other values";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                                print "**************************************************";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Ap Security Mode Enabled value to be set is not within the valid securityMode:beaconType mapping list";
                    break;
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "**************************************************";
                print "TEST STEP 3: Get the initial Ap BeaconType";
                print "EXPECTED RESULT 3: Should get the initial Ap BeaconType value successfully";
                print "ACTUAL RESULT 3: Failed to get the Ap BeaconType value";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "**************************************************";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "**************************************************";
            print "TEST STEP 2: Get the initial Ap Security Mode Enabled value";
            print "EXPECTED RESULT 2: Should get the initial Ap Security Mode Enabled value successfully";
            print "ACTUAL RESULT 2: Failed to get the Ap Security Mode Enabled value";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
            print "**************************************************";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get list of Ap Security Modes Supported"
        print "EXPECTED RESULT 1: Should get the list of Ap Security Modes Supported successfully";
        print "ACTUAL RESULT 1: Failed to get the Ap Security Modes Supported";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "**************************************************";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
