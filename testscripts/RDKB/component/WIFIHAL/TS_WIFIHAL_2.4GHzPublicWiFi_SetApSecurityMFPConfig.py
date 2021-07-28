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
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityMFPConfig</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApSecurityMFPConfig() to obtain the current config value and check if the value is from the expected list : ["Disabled", "Optional", "Required"]. Set each of the config values using wifi_setApSecurityMFPConfig() and cross check with the get API for 2.4GHz Public WiFi.</synopsis>
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
    <test_case_id>TC_WIFIHAL_602</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApSecurityMFPConfig() to obtain the current config value and check if the value is from the expected list : ["Disabled", "Optional", "Required"]. Set each of the config values using wifi_setApSecurityMFPConfig() and cross check with the get API for 2.4GHz Public WiFi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamStringValue</api_or_interface_used>
    <input_parameters>methodname : getApSecurityMFPConfig
methodname : setApSecurityMFPConfig
apIndex : fetched from platform properties
setConfigValues : fetched from the expected list</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Fetch the 2.4GHz Public WiFi Access Point index from platform properties file.
3. Invoke the function WIFIHAL_GetOrSetParamStringValue which in turn will invoke the HAL API wifi_getApSecurityMFPConfig() to get the MFP Config value.
4. Check if the value retrieved is from the expected list : ["Disabled", "Optional", "Required"]
5. Invoke the function WIFIHAL_GetOrSetParamStringValue to invoke the HAL API wifi_setApSecurityMFPConfig() to set the Config values other than the initial values.
6. Cross check and verify if the values are set properly.
7. Revert to initial value
8. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getApSecurityMFPConfig() should retrieve a valid MPF Config value and the HAL API wifi_setApSecurityMFPConfig() should successfully set different config values from the list ["Disabled", "Optional", "Required"] successfully for 2.4GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityMFPConfig</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityMFPConfig');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityMFPConfig');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

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

        print "\nTEST STEP 2: Invoke the wifi_getApSecurityMFPConfig api";
        print "EXPECTED RESULT 2:Invocation of wifi_getApSecurityMFPConfig should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        tdkTestObj.addParameter("methodName","getApSecurityMFPConfig")
        tdkTestObj.addParameter("radioIndex", apIndex)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getApSecurityMFPConfig was success. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            initialConfigValue = details.split(":")[1].strip();
            print "Initial Access Point Security MFP Config : %s" %initialConfigValue;

            #Check if the MFPConfig value is from the expected list
            mfpConfigValues = ["Disabled", "Optional", "Required"]
            print "\nTEST STEP 3: The ApSecurityMFPConfig should be from the expected list : ", mfpConfigValues;
            print "EXPECTED RESULT 3: The ApSecurityMFPConfig should be from the expected list";

            if initialConfigValue in mfpConfigValues:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: ApSecurityMFPConfig is from the expected list";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Setting Values
                print "MFP Config Values to be set : ", mfpConfigValues;
                step = 3;
                for i,word in enumerate(mfpConfigValues):
                    step = step + 1;
                    setConfigValue = mfpConfigValues[i];
                    print "\nTEST STEP %d: Set the MFP Config to %s by invoking the API wifi_setApSecurityMFPConfig" %(step, setConfigValue);
                    print "EXPECTED RESULT %d: The value should be set successfully" %step ;
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                    tdkTestObj.addParameter("methodName","setApSecurityMFPConfig")
                    tdkTestObj.addParameter("radioIndex", apIndex)
                    tdkTestObj.addParameter("param", setConfigValue)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d:  %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        step = step + 1;
                        print "\nTEST STEP %d: Invoke  wifi_getApSecurityMFPConfig  to verify set operation done by wifi_setApSecurityMFPConfig api" %step;
                        print "EXPECTED RESULT %d: wifi_getApSecurityMFPConfig should be successfully invoked after set" %step;
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                        tdkTestObj.addParameter("methodName","getApSecurityMFPConfig")
                        tdkTestObj.addParameter("radioIndex", apIndex)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and details != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Invocation of wifi_getApSecurityMFPConfig was success" %step;
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            getConfigValue = details.split(":")[1].strip();
                            print "getConfigValue : %s" %getConfigValue;
                            print "setConfigValue : %s" %setConfigValue;
                            step = step + 1;

                            if getConfigValue == setConfigValue:
                                print "\nTEST STEP %d : Verify if ApSecurityMFPConfig set value and get value are same" %step;
                                print "EXPECTED RESULT %d : wifi_getApSecurityMFPConfig() returned same value as the set value" %step;
                                print "ACTUAL RESULT %d:  %s" %(step, details);
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "TEST STEP %d : Verify if ApSecurityMFPConfig set value and get value are same" %step;
                                print "EXPECTED RESULT %d : wifi_getApSecurityMFPConfig() returned different value than the set value" %step;
                                print "ACTUAL RESULT %d:  %s" %(step, details);
                                print "[TEST EXECUTION RESULT] : FAILURE";
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Invocation of wifi_getApSecurityMFPConfig was failure" %step;
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d:  %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                step = step + 1;
                #Revert ApSecurityMFPConfig to initial value
                if initialConfigValue != getConfigValue:
                    print "\nTEST STEP %d: Revert the ApSecurityMFPConfig to %s using wifi_setApSecurityMFPConfig api" %(step, initialConfigValue);
                    print "EXPECTED RESULT %d: wifi_setApSecurityMFPConfig should successfully revert ApSecurityMFPConfig" %step;
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                    tdkTestObj.addParameter("methodName","setApSecurityMFPConfig")
                    tdkTestObj.addParameter("radioIndex", apIndex)
                    tdkTestObj.addParameter("param", initialConfigValue)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d:  %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d:  %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Revert operation is not required";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: ApSecurityMFPConfig is not from the expected list";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
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
    print "Module loading failed";

