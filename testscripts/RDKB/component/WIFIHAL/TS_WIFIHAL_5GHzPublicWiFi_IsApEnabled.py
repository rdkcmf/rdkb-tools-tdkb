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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzPublicWiFi_IsApEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check given Public WiFi Access point enable status using wifi_getApEnable() HAL API</synopsis>
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
    <test_case_id>TC_WIFIHAL_576</test_case_id>
    <test_objective>Check given Access point enable status using wifi_getApEnable() HAL API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApEnable()</api_or_interface_used>
    <input_parameters>methodName   :  getApEnable
methodName   :  setApEnable
apIndex   :  fetched from platform properties file</input_parameters>
    <automation_approch>1.Load the wifihal module
2. Get the 5GHz Public WiFi AP Index from platform.properties file
3.wifihalstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIHAL_GetOrSetParamBoolValue through registered TDK wifihalstub function along with necessary arguments
4.WIFIHAL_GetOrSetParamBoolValue function will call Ccsp Base Function named "ssp_WIFIHALGetOrSetParamBoolValue", that inturn will call WIFIHAL Library Functions wifi_setApEnable() and wifi_getApEnable()
5.Response(s)(printf) from TDK Component,Ccsp Library function and wifihalstub would be logged in Agent Console log based on the debug info redirected to agent console
6.wifihalstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result
7.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifihalstub</automation_approch>
    <expected_output>Public WiFi Access point enable status should return TRUE</expected_output>
    <priority>High</priority>
    <test_stub_interface>WiFiHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_IsApEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_IsApEnabled');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_IsApEnabled');

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
        print "TEST STEP 1: Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_5G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        getMethod = "getApEnable"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        #Get current AP Enable status
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            enable = details.split(":")[1].strip()

            if "Enabled" in enable:
                print "Public WiFi Access Point is Enabled"
                tdkTestObj.setResultStatus("SUCCESS");
                oldEnable = 1
                newEnable = 0
            else:
                print "Public WiFi Access Point is Enabled"
                oldEnable = 0
                newEnable = 1

            setMethod = "setApEnable"
            #Toggle the enable status using set
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, newEnable, setMethod)

            if expectedresult in actualresult :
                print "Public WiFi Access Point Enable state toggled using set"
                # Get the New AP enable status
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

                if expectedresult in actualresult and enable not in details.split(":")[1].strip():
                    print "Public WiFi Access Point getEnable Success, verified with setEnable() api"

                    #Revert back to original Enable status
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, oldEnable, setMethod)

                    if expectedresult in actualresult :
                        print "Enable status reverted back";
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "Couldn't revert enable status"
                        tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "getApEnable() failed"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "setApEnable() failed"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "getApEnable() failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1: Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_5G_PUBLIC_WIFI from property file :", details ;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

