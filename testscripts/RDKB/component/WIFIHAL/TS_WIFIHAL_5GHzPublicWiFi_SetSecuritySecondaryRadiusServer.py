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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzPublicWiFi_SetSecuritySecondaryRadiusServer</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetSecurityRadiusServer</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To  set and get the SecuritySecondaryRadiusServer details  for 5GHz Public WiFi</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_572</test_case_id>
    <test_objective>To set and get the SecuritySecondaryRadiusServer details  for 5GHz Public WiFi</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecuritySecondaryRadiusServer()
wifi_setApSecuritySecondaryRadiusServer()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : getApSecuritySecondaryRadiusServer
methodName : setApSecuritySecondaryRadiusServer
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
ApIndex : fetched from platform properties file</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the 5GHz Public WiFi AP Index from platform.properties file
3. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApSecurityModeEnabled() and save the get value
4. If the mode is any Enterprise Modes : "WPA-Enterprise", "WPA2-Enterprise", "WPA-WPA2-Enterprise",  go to step 5
5. If mode is not Enterprise mode, invoke wifi_setApSecurityModeEnabled using  WIFIHAL_GetOrSetParamStringValue and set WPA-Enterprise mode
6. Using  WIFIHAL_GetOrSetSecurityRadiusServer invoke wifi_getApSecuritySecondaryRadiusServer() and save the value
7. Using  WIFIHAL_GetOrSetSecurityRadiusServer invoke wifi_setApSecuritySecondaryRadiusServer() and set any values for IPaddress, port and RadiusSecret
8. Invoke wifi_getApSecuritySecondaryRadiusServer() to get the previously set value.
9. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
10. Revert the SecondaryRadiusServer and ModeEnabled back to initial value
11. Unload wifihal module</automation_approch>
    <expected_output>Set and get values of SecondaryRadiusServer (IP address, port and RadiusSecret) should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_SetSecuritySecondaryRadiusServer</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def GetorSetApSecuritySecondaryRadiusServer(obj, primitive, apIndex, IPAddress, port, RadiusSecret, methodname):
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex",apIndex);
    tdkTestObj.addParameter("methodName", methodname);
    tdkTestObj.addParameter("IPAddress", IPAddress);
    tdkTestObj.addParameter("port", port);
    tdkTestObj.addParameter("RadiusSecret", RadiusSecret);
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "details : %s"%details;
    return (tdkTestObj, actualresult, details);

def checkApSecuritySecondaryRadiusServer(apIndex):
    getMethod = "getApSecuritySecondaryRadiusServer"
    primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
    #Calling the method to execute wifi_getApSecuritySecondaryRadiusServer()
    tdkTestObj, actualresult, details = GetorSetApSecuritySecondaryRadiusServer(obj, primitive, apIndex, "0", 0, "0", getMethod)

    output  = details.split(":")[1].strip()
    initDetails = output.split(",")
    initValues = [i.split("=",1)[1] for i in initDetails]
    #Checking if all the output values are non emtpy

    if all(initValues):
        print "TEST STEP 1: Get the ApSecuritySecondaryRadiusServer details"
        print "EXPECTED RESULT 1: Should get the IPAddress, port and RadiusSecret as non empty values"
        print "ACTUAL RESULT 1: Obtained the IPAddress, port and RadiusSecret as a NON EMPTY values"
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "ApSecuritySecondaryRadiusServer details : %s"%output
        tdkTestObj.setResultStatus("SUCCESS");
        setMethod = "setApSecuritySecondaryRadiusServer"
        primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
        IPAddress = "1.1.2.2"
        port = 1234
        RadiusSecret = "12345"
        #Calling the method to execute wifi_setApSecuritySecondaryRadiusServer()
        tdkTestObj, actualresult, details = GetorSetApSecuritySecondaryRadiusServer(obj, primitive, apIndex, IPAddress, port, RadiusSecret, setMethod)

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the ApSecuritySecondaryRadiusServer details"
            print "EXPECTED RESULT 2: Should set the IPAddress, port and RadiusSecret"
            print "ACTUAL RESULT 2: Successfully set the IPAddress, port and RadiusSecret"
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"
            getMethod = "getApSecuritySecondaryRadiusServer"
            primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
            #Calling the method to execute wifi_getApSecuritySecondaryRadiusServer()
            tdkTestObj, actualresult, details = GetorSetApSecuritySecondaryRadiusServer(obj, primitive, apIndex, "0", 0, "0", getMethod)

            output  = details.split(":")[1].strip()
            outputDetails = output.split(",")
            outputValues = [i.split("=",1)[1] for i in outputDetails]

            if outputValues == [IPAddress, str(port), RadiusSecret]:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Comparing the set and get values of ApSecuritySecondaryRadiusServer deatils"
                print "EXPECTED RESULT 3: Set and get values should be the same"
                print "ACTUAL RESULT 3: Set and get values are the same"
                print "[TEST EXECUTION RESULT] : SUCCESS";
                print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"
                print "Get values: IPAddress = ",outputValues[0],"port = ",outputValues[1],"RadiusSecret = ",outputValues[2]

                #Reverting the values to previous value
                if initValues[0] != "0.0.0.0":
                    setMethod = "setApSecuritySecondaryRadiusServer"
                    primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
                    IPAddress = initValues[0];
                    port = int(initValues[1]);
                    RadiusSecret = initValues[2];
                    #Calling the method to execute wifi_setApSecuritySecondaryRadiusServer()
                    tdkTestObj, actualresult, details = GetorSetApSecuritySecondaryRadiusServer(obj, primitive, apIndex, IPAddress, port, RadiusSecret, setMethod)

                    if expectedresult in actualresult:
                        print "Successfully reverted to initial values"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Unable to revert to initial value"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "Revert operation is not required as initial IP address is 0.0.0.0";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Comparing the set and get values of ApSecuritySecondaryRadiusServer deatils"
                print "EXPECTED RESULT 3: Set and get values should be the same"
                print "ACTUAL RESULT 3: Set and get values are NOT the same"
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"
                print "Get values: IPAddress = ",outputValues[0],"port = ",outputValues[1],"RadiusSecret = ",outputValues[2]
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the ApSecuritySecondaryRadiusServer details"
            print "EXPECTED RESULT 2: Should set the IPAddress, port and RadiusSecret"
            print "ACTUAL RESULT 2: Failed to set the IPAddress, port and RadiusSecret"
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "TEST STEP 1: Get the ApSecuritySecondaryRadiusServer details"
        print "EXPECTED RESULT 1: Should get the IPAddress, port and RadiusSecret as non empty values"
        print "ACTUAL RESULT 1: Obtained the IPAddress, port and RadiusSecret as an EMPTY values"
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "ApSecuritySecondaryRadiusServer details : %s"%output
        tdkTestObj.setResultStatus("FAILURE");

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_SetSecuritySecondaryRadiusServer');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_SetSecuritySecondaryRadiusServer');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Getting APINDEX_5G_PUBLIC_WIFI value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile APINDEX_5G_PUBLIC_WIFI" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and details != "":
        apIndex = int(details);
        print "TEST STEP : Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT : Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT : APINDEX_5G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        compatibleModes = ["WPA-Enterprise", "WPA2-Enterprise", "WPA-WPA2-Enterprise"]
        expectedresult="SUCCESS";
        getMethod = "getApSecurityModeEnabled"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'
        #Calling the method to execute wifi_getApSecurityModeEnabled()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
            initMode = details.split(":")[1].strip()
            print "Initial Security Mode : %s"%initMode;

            if initMode not in compatibleModes:
                expectedresult="SUCCESS";
                setMethod = "setApSecurityModeEnabled"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'
                setMode = compatibleModes[0]
                #Calling the method to execute wifi_setApSecurityModeEnabled()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ModeEnabled is changed to an WPA-Enterprise type"
                    #Calling the function to perform the settings and getting and verification of SecuritySecondaryRadiusServer
                    checkApSecuritySecondaryRadiusServer(apIndex);

                    #Revert to initial mode
                    setMethod = "setApSecurityModeEnabled"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                    setMode = initMode
                    #Calling the method to execute wifi_setApSecurityModeEnabled()
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

                    if expectedresult in actualresult:
                        print "Successfully reverted the SecurityMode to initial value"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Unable to revert the SecurityMode to initial value"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Unable to change ModeEnabled to Enterprise type"
            else:
                #Calling the function to perform the settings and getting and verification of SecuritySecondaryRadiusServer
                checkApSecuritySecondaryRadiusServer(apIndex);
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "wifi_getApSecurityModeEnabled()call failed"
    else:
        print "TEST STEP : Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT : Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT : APINDEX_5G_PUBLIC_WIFI from property file :", details ;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

