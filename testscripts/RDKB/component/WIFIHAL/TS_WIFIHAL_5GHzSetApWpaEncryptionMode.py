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
  <name>TS_WIFIHAL_5GHzSetApWpaEncryptionMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get the ApWpaEncryptionMode for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_140</test_case_id>
    <test_objective>To set and get the WpaEncryptionMode for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpaEncryptionMode()
wifi_setApWpaEncryptionMode()</api_or_interface_used>
    <input_parameters>methodName : getApWpaEncryptionMode
methodName : setApWpaEncryptionMode
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApWpaEncryptionMode() and save the get value
3. Choose a EncryptionMode from supported Encryption Mode list and using  WIFIHAL_GetOrSetParamStringValue invoke wifi_setApWpaEncryptionMode()
4. Invoke wifi_getApWpaEncryptionMode() to get the previously set value.
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the EncryptionMode back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of EncryptionMode should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApWpaEncryptionMode</test_script>
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApWpaEncryptionMode');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApWpaEncryptionMode');

loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    supportedApWpaEncryptionModes = "sh %s/tdk_utility.sh parseConfigFile SUPPORTED_APWPA_ENCRYPTIONMODES" %TDK_PATH;
    tdkTestObj.addParameter("command", supportedApWpaEncryptionModes);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    supportedApWpaEncryptionModes = tdkTestObj.getResultDetails().strip();
    supportedApWpaEncryptionModes = supportedApWpaEncryptionModes.replace("\\n", "");

    if supportedApWpaEncryptionModes and expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        supportedModes = supportedApWpaEncryptionModes.split(",");
        print "TEST STEP : Get the list of supported ApWpaEncryption Modes from /nvram/TDK/tdk_platform.properties file";
        print "EXPECTED RESULT : Should get the list of supported ApWpaEncryption Modes";
        print "ACTUAL RESULT : Got the list of supported ApWpaEncryption Modes as %s" %supportedModes;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        expectedresult="SUCCESS";
        apIndex = 1
        getMethod = "getApWpaEncryptionMode"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
            initialMode = details.split(":")[1].strip()
            if initialMode in supportedModes:
                print "ApWpaEncryptionMode function successful and returned valid Encryption Mode"
                tdkTestObj.setResultStatus("SUCCESS");

                for setEncMode in supportedModes:
                    if initialMode == setEncMode:
                        continue;
                    else:
                        expectedresult="SUCCESS";
                        apIndex = 1
                        setMethod = "setApWpaEncryptionMode"
                        primitive = 'WIFIHAL_GetOrSetParamStringValue'

                        #Calling the method from wifiUtility to execute test case and set result status for the test.
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setEncMode, setMethod)

                        if expectedresult in actualresult:
                            expectedresult="SUCCESS";
                            apIndex = 1
                            getMethod = "getApWpaEncryptionMode"
                            primitive = 'WIFIHAL_GetOrSetParamStringValue'

                            #Calling the method from wifiUtility to execute test case and set result status for the test.
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
                            finalMode = details.split(":")[1].strip()

                            if expectedresult in actualresult:
                                if finalMode == setEncMode:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP: Compare the set and get valus of ApWpaEncryptionMode"
                                    print "EXPECTED RESULT: Set and get values of ApWpaEncryptionMode should be same"
                                    print "ACTUAL RESULT: Set and get values of ApWpaEncryptionMode are the same"
                                    print "setApWpaEncryptionMode = ",setEncMode
                                    print "getApWpaEncryptionMode = ",finalMode
                                    print "TEST EXECUTION RESULT : SUCCESS"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP: Compare the set and get valus of ApWpaEncryptionMode"
                                    print "EXPECTED RESULT: Set and get values of ApWpaEncryptionMode should be same"
                                    print "ACTUAL RESULT: Set and get values of ApWpaEncryptionMode are NOT the same"
                                    print "setApWpaEncryptionMode = ",setEncMode
                                    print "getApWpaEncryptionMode = ",finalMode
                                    print "TEST EXECUTION RESULT : FAILURE"
                            else:
                                print "wifi_getApWpaEncryptionMode() call failed"
                                tdkTestObj.setResultStatus("FAILURE");

                            #Revert the ApWpaEncryptionMode back to initial value
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialMode, setMethod)
                            if expectedresult in actualresult:
                                print "Successfully reverted back to initial value"
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "Unable to revert to initial value"
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            print "wifi_setApWpaEncryptionMode() call failed"
                            tdkTestObj.setResultStatus("FAILURE");
                        break;
            else:
                print "ApWpaEncryptionMode returned is not a valid Encryption "
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "wifi_getApWpaEncryptionMode() failed"
            tdkTestObj.setResultStatus("FAILURE");
    else :
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP : Get the list of supported ApWpaEncryption Modes from /nvram/TDK/tdk_platform.properties file";
         print "EXPECTED RESULT : Should get the list of supported ApWpaEncryption Modes";
         print "ACTUAL RESULT : Failed to get the list of supported ApWpaEncryption Modes from /nvram/TDK/tdk_platform.properties file"
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
