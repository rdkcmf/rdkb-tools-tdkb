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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzSetSSIDName</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set SSID Name using wifi_setSSIDName() and verify by getting with wifi_getSSIDName()</synopsis>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_129</test_case_id>
    <test_objective>To set SSID Name using wifi_setSSIDName() and verify by getting with wifi_getSSIDName()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setSSIDName
wifi_getSSIDName</api_or_interface_used>
    <input_parameters>methodName: getSSIDName
methodName :setSSIDName
apIndex: 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using getSSIDName get and save current SSIDName
3.Set the SSIDName using setSSIDName()
4.Get the above set value using getSSIDName
5. Verify whether the set and get values are the same.
6. Revert back to the initial SSIDName
7. Unload wifihal module</automation_approch>
    <expected_output>Set and get values of the SSID Names should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetSSIDName</test_script>
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

radio = "2.4G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetSSIDName');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Checking for AP Index 0, Similar way we can check for other APs
    tdkTestObjTemp, idx = getIndex(obj, radio);

    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");

    else:
        expectedresult="SUCCESS";
        apIndex = idx;
        getMethod = "getSSIDName"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            initialName = details.split(":")[1].strip()

            expectedresult="SUCCESS";
            apIndex = idx;
            setMethod = "setSSIDName"
            setName = "ssid_0_name"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setName, setMethod)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                apIndex = idx;
                getMethod = "getSSIDName"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
                tdkTestObj.setResultStatus("SUCCESS");
                finalName = details.split(":")[1].strip()

                if expectedresult in actualresult:
                    if finalName == setName:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP : Compare set and get values of SSID Name"
                        print "EXPECTED RESULT : Set and get values of SSID Name should be the same"
                        print "ACTUAl RESULT : Set and get values of SSID Name are the same"
                        print "setSSIDName = ",setName
                        print "getSSIDName = ",finalName
                        print "TEST EXECUTION RESULT :SUCCESS"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP : Compare set and get values of SSID Name"
                        print "EXPECTED RESULT : Set and get values of SSID Name should be the same"
                        print "ACTUAl RESULT : Set and get values of SSID Name are NOT the same"
                        print "setSSIDName = ",setName
                        print "getSSIDName = ",finalName
                        print "TEST EXECUTION RESULT :FAILURE"

                    #Revert the SSID NAme back o initial value
                    apIndex = idx;
                    setMethod = "setSSIDName"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                    #Calling the method from wifiUtility to execute test case and set result status for the test.
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialName, setMethod)

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Successfully reverted back to initial value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to revert to initial value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "wifi_getSSIDName() function failed"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "wifi_setSSIDName function failed";
        else:
            print "wifi_getSSIDName function failed";
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

