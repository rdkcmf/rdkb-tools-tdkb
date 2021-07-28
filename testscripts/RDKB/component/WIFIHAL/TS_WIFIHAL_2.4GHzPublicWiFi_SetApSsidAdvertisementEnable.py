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
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetApSsidAdvertisementEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApSsidAdvertisementEnable() to get the ApSSIDAdvertisementEnable and toggle the value by invoking wifi_setApSsidAdvertisementEnable and check if the set and get values are same for 2.4GHz Public WiFi.</synopsis>
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
    <test_case_id>TC_WIFIHAL_599</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApSsidAdvertisementEnable() to get the ApSSIDAdvertisementEnable and toggle the value by invoking wifi_setApSsidAdvertisementEnable and check if the set and get values are same for 2.4GHz Public WiFi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamBoolValue</api_or_interface_used>
    <input_parameters>methodname : getApSsidAdvertisementEnable
methodname : setApSsidAdvertisementEnable
apIndex : fetched from platform properties
enable : 0 or 1</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Fetch the 2.4GHz Public WiFi index from platform properties file.
3. Invoke the function WIFIHAL_GetOrSetParamBoolValue which will in turn invoke wifi_getApSsidAdvertisementEnable() to fetch the current Enable state.
4. Toggle the enable state by invoking WIFIHAL_GetOrSetParamBoolValue which then invokes wifi_setApSsidAdvertisementEnable() .
5. Cross check if the value is set properly
6. Revert to initial enable state
7. Unload the module</automation_approch>
    <expected_output>The ApSsidAdvertisementEnable should be retrieved from the HAL API wifi_getApSsidAdvertisementEnable() and the value should be toggled with the API wifi_setApSsidAdvertisementEnable() successfully for 2.4GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetApSsidAdvertisementEnable</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApSsidAdvertisementEnable');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApSsidAdvertisementEnable');

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

        print "TEST STEP 2: Invoke the wifi_getApSsidAdvertisementEnable api";
        print "EXPECTED RESULT 2:Invocation of wifi_getApSsidAdvertisementEnable should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getApSsidAdvertisementEnable")
        tdkTestObj.addParameter("radioIndex", apIndex)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getApSsidAdvertisementEnable was success. %s" %details;
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

            print "TEST STEP 3: Toggle the enabled state using wifi_setApSsidAdvertisementEnable api";
            print "EXPECTED RESULT 3: wifi_setApSsidAdvertisementEnable should successfully toggle ApSsidAdvertisementEnable status to ",newStatus ;
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setApSsidAdvertisementEnable")
            tdkTestObj.addParameter("radioIndex", apIndex)
            tdkTestObj.addParameter("param", newEnable)
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "TEST STEP 4: Invoke  wifi_getApSsidAdvertisementEnable  to verify toggling done by wifi_setApSsidAdvertisementEnable api";
                print "EXPECTED RESULT 4: wifi_getApSsidAdvertisementEnable should be successfully invoked after set";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getApSsidAdvertisementEnable")
                tdkTestObj.addParameter("radioIndex", apIndex)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: Invocation of wifi_getApSsidAdvertisementEnable was success";
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    enable = details.split(":")[1].strip();

                    if enable == newStatus :
                        print "TEST STEP 5 : Verify if ApSsidAdvertisementEnable set value and get value are same"
                        print "EXPECTED RESULT 5 : wifi_getApSsidAdvertisementEnable() returned enable state same as the set value"
                        print "ACTUAL RESULT 5:  %s" %details;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Revert ApSsidAdvertisementEnable to initial value
                        print "TEST STEP 6: Revert the enabled state to %s using wifi_setApSsidAdvertisementEnable api" %initial_enable;
                        print "EXPECTED RESULT 6: wifi_setApSsidAdvertisementEnable should successfully revert ApSsidAdvertisementEnable status";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","setApSsidAdvertisementEnable")
                        tdkTestObj.addParameter("radioIndex", apIndex)
                        tdkTestObj.addParameter("param", oldEnable)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and details != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6:  %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6:  %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "TEST STEP 5 : Verify if ApSsidAdvertisementEnable set value and get value are same"
                        print "EXPECTED RESULT 5 : wifi_getApSsidAdvertisementEnable() returned enable state different from the set value"
                        print "ACTUAL RESULT 5:  %s" %details;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: Invocation of wifi_getApSsidAdvertisementEnable was failure";
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
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

