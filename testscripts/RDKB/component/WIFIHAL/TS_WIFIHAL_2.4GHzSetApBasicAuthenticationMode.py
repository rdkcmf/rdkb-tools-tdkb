##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the ApSecurityModeEnabled to "None" and check if the BasicAuthenticationMode for 2.4GHz is changed to "None"<synopsis>
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
    <test_case_id>TC_WIFIHAL_135</test_case_id>
    <test_objective>To set the ApSecurityModeEnabled to "None" and check if the BasicAuthenticationMode for 2.4GHz is changed to "None"</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBasicAuthenticationMode()
wifi_setApBasicAuthenticationMode()</api_or_interface_used>
    <input_parameters>methodName : getApBasicAuthenticationMode()
methodName : getApSecurityModeEnabled()
methodName : setApSecurityModeEnabled()
methodName : getApBeaconType()
ApIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal and sysutil modules
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApBasicAuthenticationMode() and check if the value is from the supported modes list
3. Set the ApSecurityModeEnabled to "None" and validate the SET with GET
4. Invoke wifi_getApBasicAuthenticationMode() and check if the value is changed to "None".
5. Invoke wifi_getApBeaconType() and check if the value is "None"
6. Revert the ApSecurityModeEnabled back to initial value
7. Unload wifihal and sysutil modules</automation_approch>
    <except_output>Setting  ApSecurityModeEnabled to "None" should change the BasicAuthenticationMode to "None"</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode</test_script>
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
from tdkbVariables import *;
from time import sleep;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

def setApSecurityMode(obj,apIndex,setMode):
    expectedresult="SUCCESS";
    getMethod = "getApSecurityModeEnabled"
    setMethod = "setApSecurityModeEnabled"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    initialApSecurity = "";

    #Calling the method to execute wifi_getApSecurityModeEnabled()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
        initialApSecurity = details.split(":")[1].strip()
        tdkTestObj.setResultStatus("SUCCESS");

        #Calling the method to execute wifi_setApSecurityModeEnabled()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

        if expectedresult in actualresult:
            sleep(10);
            #Calling the method to execute wifi_getApSecurityModeEnabled()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

            if expectedresult in actualresult:
                finalMode = details.split(":")[1].strip()
                if finalMode == setMode:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP: Compare the set and get values of ApSecurityMode"
                    print "EXPECTED RESULT: Set and get values of ApSecurityMode should be same"
                    print "ACTUAL RESULT: Set and get values of ApSecurityMode are the same"
                    print "setApSecurityMode = ",setMode
                    print "getApSecurityMode = ",finalMode
                    print "TEST EXECUTION RESULT : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP: Compare the set and get values of ApSecurityMode"
                    print "EXPECTED RESULT: Set and get values of ApSecurityMode should be same"
                    print "ACTUAL RESULT: Set and get values of ApSecurityMode are NOT the same"
                    print "setApSecurityMode = ",setMode
                    print "getApSecurityMode = ",finalMode
                    print "TEST EXECUTION RESULT : FAILURE"
            else:
                print "wifi_getApSecurityModeEnabled() call failed"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "wifi_setApSecurityModeEnabled() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "wifi_getApSecurityModeEnabled() call failed"
        tdkTestObj.setResultStatus("FAILURE");

    return (initialApSecurity);


if "SUCCESS" in loadmodulestatus.upper()and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd = "sh %s/tdk_utility.sh parseConfigFile SUPPORTED_AUTH_MODES" %TDK_PATH;
        tdkTestObj.addParameter("command", cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        supportedAuthModes = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        if expectedresult in actualresult and supportedAuthModes != "":
            tdkTestObj.setResultStatus("SUCCESS");
            supportedModes = supportedAuthModes.split(",");
            print "\nTEST STEP 1: Get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
            print "EXPECTED RESULT 1: Should get the list of supported Authentication Modes";
            print "ACTUAL RESULT 1: Got the list of supported Authentication Modes as %s" %supportedModes;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            apIndex = idx;
            getMethod = "getApBasicAuthenticationMode"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
            #Calling the method to execute wifi_getApBasicAuthenticationMode()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

            if expectedresult in actualresult:
                initialMode = details.split(":")[1].strip();
                if initialMode in supportedModes:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Initial Mode is in the supported modes list"

                    #Calling the function to set the ApSecurity mode to 'None'
                    mode = 'None';
                    initialSecurityMode = setApSecurityMode(obj,idx,mode);

                    if initialSecurityMode != "":
                        getMethod = "getApBasicAuthenticationMode"
                        primitive = 'WIFIHAL_GetOrSetParamStringValue'

                        #Calling the method to execute wifi_getApBasicAuthenticationMode()
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                        if expectedresult in actualresult:
                            finalMode = details.split(":")[1].strip()
                            if finalMode == 'None':
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP: Check if ApBasicAuthenticationMode is changed to None when the Security Mode enabled is None"
                                print "EXPECTED RESULT: ApBasicAuthenticationMode should be changed to None when the Security Mode enabled is None"
                                print "ACTUAL RESULT: ApBasicAuthenticationMode is None as expected"
                                print "TEST EXECUTION RESULT : SUCCESS"

                                #Calling the method to execute wifi_getApBeaconType()
                                getMethod = "getApBeaconType"
                                primitive = 'WIFIHAL_GetOrSetParamStringValue'
                                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                                if expectedresult in actualresult:
                                    beaconType = details.split(":")[1].strip()
                                    if beaconType == 'None':
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "TEST STEP: Check if ApBeaconType is changed to None when the Security Mode enabled is None"
                                        print "EXPECTED RESULT: ApBeaconType should be changed to None when the Security Mode enabled is None"
                                        print "ACTUAL RESULT: ApBeaconType is None as expected"
                                        print "TEST EXECUTION RESULT : SUCCESS"
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "TEST STEP: Check if ApBeaconType is changed to None when the Security Mode enabled is None"
                                        print "EXPECTED RESULT: ApBeaconType should be changed to None when the Security Mode enabled is None"
                                        print "ACTUAL RESULT: ApBeaconType is NOT None as expected"
                                        print "TEST EXECUTION RESULT : FAILURE"
                                else:
                                    print "wifi_getApBeaconType() call failed"
                                    tdkTestObj.setResultStatus("FAILURE");
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP: Check if ApBasicAuthenticationMode is changed to None when the Security Mode enabled is None"
                                print "EXPECTED RESULT: ApBasicAuthenticationMode should be changed to None when the Security Mode enabled is None"
                                print "ACTUAL RESULT: ApBasicAuthenticationMode is NOT None as expected"
                                print "TEST EXECUTION RESULT : FAILURE"
                        else:
                            print "wifi_getApBasicAuthenticationMode() call failed"
                            tdkTestObj.setResultStatus("FAILURE");

                        #Revert the security mode
                        securityMode = setApSecurityMode(obj,idx,initialSecurityMode);
                    else:
                        print "wifi_getApSecurityModeEnabled() call failed"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Initial Mode is NOT in the supported modes list"
            else:
                print "wifi_getApBasicAuthenticationMode() call failed"
                tdkTestObj.setResultStatus("FAILURE");
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
            print "EXPECTED RESULT : Should get the list of supported Authentication Modes";
            print "ACTUAL RESULT : Failed to get the list of supported AuthenticationModes from /etc/tdk_platform.properties file";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

