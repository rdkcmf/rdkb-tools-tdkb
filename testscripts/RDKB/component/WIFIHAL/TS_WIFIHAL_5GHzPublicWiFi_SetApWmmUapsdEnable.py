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
  <version>3</version>
  <name>TS_WIFIHAL_5GHzPublicWiFi_SetApWmmUapsdEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApUAPSDCapability() to retrieve the ApUAPSDCapability. If the ApUAPSDCapability is enabled toggle ApWmmUapsdEnable using the API wifi_setApWmmUapsdEnable() and confirm if the value is set properly using wifi_getApWmmUapsdEnable() for 5GHz Public WiFi.</synopsis>
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
    <test_case_id>TC_WIFIHAL_597</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApUAPSDCapability() to retrieve the ApUAPSDCapability. If the ApUAPSDCapability is enabled toggle ApWmmUapsdEnable using the API wifi_setApWmmUapsdEnable() and confirm if the value is set properly using wifi_getApWmmUapsdEnable() for 5GHz Public WiFi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamBoolValue</api_or_interface_used>
    <input_parameters>methodname : getApUAPSDCapability
methodname : getApWmmUapsdEnable
methodname : setApWmmUapsdEnable
enable : 0 or 1
apIndex : fetched from platform properties</input_parameters>
    <automation_approch>1.Load the wifihal module
2. Fetch the 5GHz Public WiFi Access Point index from platform property file.
3. Invoke the function WIFIHAL_GetOrSetParamBoolValue which will invoke the HAL API wifi_getApUAPSDCapability().
4. If ApUAPSDCapability is Enabled, then invoke WIFIHAL_GetOrSetParamBoolValue which will in turn invoke the HAL API wifi_getApWmmUapsdEnable() and get the current enable status.
5. Toggle the enable status by invoking WIFIHAL_GetOrSetParamBoolValue which in turn calls wifi_setApWmmUapsdEnable().
6. Cross check if the value is set properly
7. Revert to initial enable state
8. Unload module</automation_approch>
    <expected_output>If ApUAPSDCapability is Enabled then the HAL API  wifi_setApWmmUapsdEnable() should successfully toggle the value retrieved via  wifi_getApWmmUapsdEnable() for 2.4GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_SetApWmmUapsdEnable</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_SetApWmmUapsdEnable');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_SetApWmmUapsdEnable');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

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

        print "TEST STEP 2: Check if ApUAPSDCapability is enabled by invoking the wifi_getApUAPSDCapability api";
        print "EXPECTED RESULT 2:Invocation of wifi_getApUAPSDCapability should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getApUAPSDCapability");
        tdkTestObj.addParameter("radioIndex", apIndex);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getApUAPSDCapability was success. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            ApUAPSDCapability = details.split(":")[1].strip();
            print "ApUAPSDCapability received : %s" %ApUAPSDCapability;

            if ApUAPSDCapability == "Enabled":
                #Get ApWmmUapsdEnable
                print "TEST STEP 3: Invoke the wifi_getApWmmUapsdEnable api";
                print "EXPECTED RESULT 3:Invocation of wifi_getApWmmUapsdEnable should be success";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getApWmmUapsdEnable")
                tdkTestObj.addParameter("radioIndex", apIndex)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_getApWmmUapsdEnable was success. %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    initial_enable = details.split(":")[1].strip()

                    if "Enabled" in initial_enable:
                        oldEnable = 1
                        newEnable = 0
                        newStatus = "Disabled"
                    else:
                        oldEnable = 0
                        newEnable = 1
                        newStatus = "Enabled"

                    print "TEST STEP 4: Toggle the enabled state using wifi_setApWmmUapsdEnable api";
                    print "EXPECTED RESULT 4: wifi_setApWmmUapsdEnable should successfully toggle ApWmmUapsdEnable status to ",newStatus ;
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                    tdkTestObj.addParameter("methodName","setApWmmUapsdEnable")
                    tdkTestObj.addParameter("radioIndex", apIndex)
                    tdkTestObj.addParameter("param", newEnable)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4:  %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        print "TEST STEP 5: Invoke  wifi_getApWmmUapsdEnable to verify toggling done by wifi_setApWmmUapsdEnable api";
                        print "EXPECTED RESULT 5: wifi_getApWmmUapsdEnable should be successfully invoked after set";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","getApWmmUapsdEnable")
                        tdkTestObj.addParameter("radioIndex", apIndex)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and details != "":
                            enable = details.split(":")[1].strip();
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: Invocation of wifi_getApWmmUapsdEnable was success";
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if enable == newStatus :
                                print "TEST STEP 6 : Verify if ApWmmUapsdEnable set value and get value are same"
                                print "EXPECTED RESULT 6 : wifi_getApWmmUapsdEnable() returned enable state same as the set value"
                                print "ACTUAL RESULT 6:  %s" %details;
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                tdkTestObj.setResultStatus("SUCCESS");

                                #Revert ApWmmUapsdEnable to initial value
                                print "TEST STEP 7: Revert the enabled state to %s using wifi_setApWmmUapsdEnable api" %initial_enable;
                                print "EXPECTED RESULT 7: wifi_setApWmmUapsdEnable should successfully revert ApWmmUapsdEnable status";
                                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                                tdkTestObj.addParameter("methodName","setApWmmUapsdEnable")
                                tdkTestObj.addParameter("radioIndex", apIndex)
                                tdkTestObj.addParameter("param", oldEnable)
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                if expectedresult in actualresult and details != "":
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 7:  %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 7:  %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                print "TEST STEP 6 : Verify if ApWmmUapsdEnable set value and get value are same"
                                print "EXPECTED RESULT 6 : wifi_getApWmmUapsdEnable() returned enable state different from the set value"
                                print "ACTUAL RESULT 6:  %s" %details;
                                tdkTestObj.setResultStatus("FAILURE");
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: Invocation of wifi_getApWmmUapsdEnable was failure";
                            print "[TEST EXECUTION RESULT] : FAILURE"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4:  %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ApUAPSDCapability is disabled"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Invocation of wifi_getApUAPSDCapability failed. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
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
    print "Module loading failed";

