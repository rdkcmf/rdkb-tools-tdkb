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
  <name>TS_WIFIHAL_SetApMacAddressControlMode_FilterDisabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get the mac address filter control mode with filter disabled</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_175</test_case_id>
    <test_objective>To set and get the mac address filter control mode with filter disabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApMacAddressControlMode()
wifi_setApMacAddressControlMode()</api_or_interface_used>
    <input_parameters>methodName : getApMacAddressControlMode
methodName : setApMacAddressControlMode
ApIndex : 0 and 1
filterMode = 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamIntValue invoke wifi_getApMacAddressControlMode() and save the get value
3. Using  WIFIHAL_GetOrSetParamIntValue invoke wifi_setApMacAddressControlMode() and set filtermode as 0(disabled)
4. Invoke wifi_getApMacAddressControlMode() to get the previously set value.
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the MacAddressControlMode back to initial value
7. Unload wifihal module</automation_approch>
    <expected_output>Set and get values of MacAddressControlMode should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_SetApMacAddressControlMode_FilterDisabled</test_script>
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
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_SetApMacAddressControlMode_FilterDisabled');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    for apIndex in range(0,2):

        expectedresult="SUCCESS";
        getMethod = "getApMacAddressControlMode"
        primitive = 'WIFIHAL_GetOrSetParamIntValue'

        #Calling the method to execute wifi_getApMacAddressControlMode()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

        if expectedresult in actualresult:
            initMode = details.split(":")[1].strip()

            expectedresult="SUCCESS";
            setMethod = "setApMacAddressControlMode"
            primitive = 'WIFIHAL_GetOrSetParamIntValue'
            #0 == filter disabled, 1 == filter as whitelist, 2 == filter as blacklist
   	    setMode = 0

            #Calling the method to execute wifi_setApMacAddressControlMode()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

            if expectedresult in actualresult:
                expectedresult="SUCCESS";
                getMethod = "getApMacAddressControlMode"
                primitive = 'WIFIHAL_GetOrSetParamIntValue'

                #Calling the method to execute wifi_getApMacAddressControlMode()
                sleep(10);
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

                if expectedresult in actualresult:
                    finalMode = details.split(":")[1].strip()
                    if int(finalMode) == setMode:
                        print "TEST STEP: Setting the MacAddress filter ControlMode as filter disabled for apIndex %s"%apIndex
                        print "EXPECTED RESULT: Set and get values should be the same"
                        print "ACTUAL RESULT : Set and get values are the same"
                        print "Set value: %s"%setMode
                        print "Get value: %s"%finalMode
                        print "TEST EXECUTION RESULT :SUCCESS"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "TEST STEP: Setting the MacAddress filter ControlMode as filter disabled for apIndex %s"%apIndex
                        print "EXPECTED RESULT: Set and get values should be the same"
                        print "ACTUAL RESULT : Set and get values are NOT the same"
                        print "Set value: %s"%setMode
                        print "Get value: %s"%finalMode
                        print "TEST EXECUTION RESULT :FAILURE"
                        tdkTestObj.setResultStatus("FAILURE");

                    #Revert back to initial value
                    setMethod = "setApMacAddressControlMode"
                    primitive = 'WIFIHAL_GetOrSetParamIntValue'
                    setMode = int(initMode)
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Successfully reverted back to inital value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to revert to initial value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "getApMacAddressControlMode() function call failed after set operation"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "setApMacAddressControlMode() function call failed"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "getApMacAddressControlMode() function call failed"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

