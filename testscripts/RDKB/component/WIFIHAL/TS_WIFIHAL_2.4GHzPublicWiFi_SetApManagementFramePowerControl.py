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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetApManagementFramePowerControl</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the ApManagementFramePowerControl for 2.4GHz Public WiFi</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_583</test_case_id>
    <test_objective>To set and get the ApManagementFramePowerControl for 2.4GHz Public WiFi</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApManagementFramePowerControl()
wifi_setApManagementFramePowerControl()</api_or_interface_used>
    <input_parameters>methodName : getApManagementFramePowerControl
methodName : setApManagementFramePowerControl
ApIndex : fetched from platform properties file</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the 2.4GHz Public WiFi AP Index from platform properties file
3. Using WIFIHAL_GetOrSetParamIntValue invoke wifi_getApManagementFramePowerControl() for 2.4GHz and save the get value
4. Choose a Power within -20 dBm and 0 dBm and using  WIFIHAL_GetOrSetParamIntValue invoke wifi_setApManagementFramePowerControl()
5. Invoke wifi_getApManagementFramePowerControl() to get the previously set value.
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the Power back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>Set and get values of Power should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetApManagementFramePowerControl</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks/>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApManagementFramePowerControl');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApManagementFramePowerControl');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Getting APINDEX_2G_PUBLIC_WIFI value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile APINDEX_2G_PUBLIC_WIFI" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and details != "":
        apIndex = int(details);
        print "TEST STEP 1: Get APINDEX_2G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_2G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        getMethod = "getApManagementFramePowerControl"
        primitive = 'WIFIHAL_GetOrSetParamIntValue'
        #Calling the method to execute wifi_getApManagementFramePowerControl()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

        if expectedresult in actualresult:
            initFPC = details.split(":")[1].strip()
            #ApManagementFramePowerControl varies in the range -20dBm to 0dBm
            r = range(-20,0)
            setFPC = random.choice(r)
            setMethod = "setApManagementFramePowerControl"
            primitive = 'WIFIHAL_GetOrSetParamIntValue'
            #Calling the method to execute wifi_setApManagementFramePowerControl()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setFPC, setMethod)

            if expectedresult in actualresult:
                getMethod = "getApManagementFramePowerControl"
                primitive = 'WIFIHAL_GetOrSetParamIntValue'
                #Calling the method to execute wifi_getApManagementFramePowerControl()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

                if expectedresult in actualresult:
                    finalFPC = details.split(":")[1].strip()

                    if int(finalFPC) == setFPC:
                        print "TEST STEP: Comparing set and get values of ApManagementFramePowerControl for 2.4GHz Public WiFi"
                        print "EXPECTED RESULT: Set and get values should be the same"
                        print "ACTUAL RESULT : Set and get values are the same"
                        print "Set value: %s"%setFPC
                        print "Get value: %s"%finalFPC
                        print "TEST EXECUTION RESULT :SUCCESS"
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Revert back to initial value
                        setMethod = "setApManagementFramePowerControl"
                        primitive = 'WIFIHAL_GetOrSetParamIntValue'
                        setFPC = int(initFPC)
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setFPC, setMethod)

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Successfully reverted back to inital value"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Unable to revert to initial value"
                    else:
                        print "TEST STEP: Comparing set and get values of ApManagementFramePowerControl for 2.4GHz Public WiFi"
                        print "EXPECTED RESULT: Set and get values should be the same"
                        print "ACTUAL RESULT : Set and get values are NOT the same"
                        print "Set value: %s"%setFPC
                        print "Get value: %s"%finalFPC
                        print "TEST EXECUTION RESULT :FAILURE"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "getApManagementFramePowerControl() function call failed after set operation"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "setApManagementFramePowerControl() function call failed"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "getApManagementFramePowerControl() function call failed"
    else:
        print "TEST STEP 1: Get APINDEX_2G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_2G_PUBLIC_WIFI from property file :", details ;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

