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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetApWpsDevicePIN</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get the  WpsDevicePIN for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_190</test_case_id>
    <test_objective>To set and get the  WpsDevicePIN for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsDevicePIN()
wifi_setApWpsDevicePIN()</api_or_interface_used>
    <input_parameters>methodName : getApWpsDevicePIN
methodName : setApWpsDevicePIN
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_getApWpsDevicePIN() and save the initial value
3. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_setApWpsDevicePIN() and set a value
4. Using WIFIHAL_GetOrSetParamULongValue invoke wifi_getApWpsDevicePIN() and get the previously set value
5. If the set and get values are the same, return SUCCESS, else return FAILURE
6. Revert to initial value
7. Unload wifihal module</automation_approch>
    <expected_output>Set and get values of DevicePIn should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApWpsDevicePIN</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio = "5G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApWpsDevicePIN');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #get the ApWpsDevicePIN
        expectedresult="SUCCESS";
        radioIndex = idx
        getMethod = "getApWpsDevicePIN"
        primitive = 'WIFIHAL_GetOrSetParamULongValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

        if expectedresult in actualresult :
            initPIN = int(details.split(":")[1].strip())

            #set the ApWpsDevicePIN
            expectedresult="SUCCESS";
            setMethod = "setApWpsDevicePIN"
            setPIN = 23344556
            primitive = 'WIFIHAL_GetOrSetParamULongValue'
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setPIN, setMethod)

            if expectedresult in actualresult :
                #get the ApWpsDevicePIN
                expectedresult="SUCCESS";
                getMethod = "getApWpsDevicePIN"
                primitive = 'WIFIHAL_GetOrSetParamULongValue'
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

                if expectedresult in actualresult :
                    getPIN = int(details.split(":")[1].strip())
                    if setPIN == getPIN:
                        print "TEST STEP: Get the previously set DevicePIN and check if it is same as set value"
                        print "EXPECTED RESULT : Should return the previously set DevicePIN"
                        print "ACTUAL RESULT : Set and get values of DevicePIN are the same"
                        print "Set DevicePIN :",setPIN
                        print "Get DevicePIN :",getPIN
                        print "TEST EXECUTION RESULT :SUCCESS"
                        tdkTestObj.setResultStatus("SUCCESS");
                    else:
                        print "TEST STEP: Get the previously set DevicePIN and check if it is same as set value"
                        print "EXPECTED RESULT : Should return the previously set DevicePIN"
                        print "ACTUAL RESULT : Set and get values of DevicePIN are NOT the same"
                        print "Set DevicePIN :",setPIN
                        print "Get DevicePIN :",getPIN
                        print "TEST EXECUTION RESULT :FAILURE"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "getApWpsDevicePIN() call failed after set operation"
                    tdkTestObj.setResultStatus("FAILURE");

	        #Revert the pin to initial value
	        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initPIN, setMethod)
	        if expectedresult in actualresult :
		    print "Successfully reverted to initial pin"
		    tdkTestObj.setResultStatus("SUCCESS");
	        else:
		    print "Unable to revert to initial value"
		    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "setApWpsDevicePIN() call failed"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "getApWpsDevicePIN() call failed"
            tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
