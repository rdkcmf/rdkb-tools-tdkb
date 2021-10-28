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
  <name>TS_WIFIHAL_6GHzSetApWmmEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApWmmCapability() to retrieve the ApWmmCapability. If the ApWmmCapability is enabled toggle ApWmmEnable using the API wifi_setApWmmEnable() and confirm if the value is set properly using wifi_getApWmmEnable() for 6GHz radio.</synopsis>
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
    <test_case_id>TC_WIFIHAL_645</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApWmmCapability() to retrieve the ApWmmCapability. If the ApWmmCapability is enabled toggle ApWmmEnable using the API wifi_setApWmmEnable() and confirm if the value is set properly using wifi_getApWmmEnable() for 6GHz radio.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWmmCapability()
wifi_getApWmmEnable()
wifi_setApWmmEnable()</api_or_interface_used>
    <input_parameters>methodname : getApWmmCapability
methodname : getApWmmEnable
methodname : setApWmmEnable
enable : 0 or 1
apIndex : fetched from platform properties</input_parameters>
    <automation_approch>1.Load the wifihal module
2. Fetch the 6GHz WiFi Access Point index from platform property file.
3. Invoke the function WIFIHAL_GetOrSetParamBoolValue which will invoke the HAL API wifi_getApWmmCapability().
4. If ApWmmCapability is Enabled, then invoke WIFIHAL_GetOrSetParamBoolValue which will in turn invoke the HAL API wifi_getApWmmEnable() and get the current enable status.
5. Toggle the enable status by invoking WIFIHAL_GetOrSetParamBoolValue which in turn calls wifi_setApWmmEnable().
6. Cross check if the value is set properly
7. Revert to initial enable state
8. Unload module</automation_approch>
    <expected_output>If ApWmmCapability is Enabled then the HAL API  wifi_setApWmmEnable() should successfully toggle the value retrieved via  wifi_getApWmmEnable() for 6GHz radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetApWmmEnable</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApWmmEnable');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApWmmEnable');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS";
    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        print "\nTEST STEP 2: Check if ApWMMCapability is enabled by invoking the wifi_getApWMMCapability api";
        print "EXPECTED RESULT 2:Invocation of wifi_getApWMMCapability should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getApWMMCapability");
        tdkTestObj.addParameter("radioIndex", apIndex);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getApWMMCapability was success. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            ApWMMCapability = details.split(":")[1].strip();
            print "ApWMMCapability received : %s" %ApWMMCapability;

            if ApWMMCapability == "Enabled":
                #Get ApWmmEnable
                print "\nTEST STEP 3: Invoke the wifi_getApWmmEnable api";
                print "EXPECTED RESULT 3:Invocation of wifi_getApWmmEnable should be success";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getApWmmEnable")
                tdkTestObj.addParameter("radioIndex", apIndex)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_getApWmmEnable was success. %s" %details;
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

                    print "\nTEST STEP 4: Toggle the enabled state using wifi_setApWmmEnable api";
                    print "EXPECTED RESULT 4: wifi_setApWmmEnable should successfully toggle ApWmmEnable status to ",newStatus ;
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                    tdkTestObj.addParameter("methodName","setApWmmEnable")
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

                        print "\nTEST STEP 5: Invoke  wifi_getApWmmEnable to verify toggling done by wifi_setApWmmEnable api";
                        print "EXPECTED RESULT 5: wifi_getApWmmEnable should be successfully invoked after set";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","getApWmmEnable")
                        tdkTestObj.addParameter("radioIndex", apIndex)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and details != "":
                            enable = details.split(":")[1].strip();
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: Invocation of wifi_getApWmmEnable was success";
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if enable == newStatus :
                                print "\nTEST STEP 6 : Verify if ApWmmEnable set value and get value are same"
                                print "EXPECTED RESULT 6 : wifi_getApWmmEnable() returned enable state same as the set value"
                                print "ACTUAL RESULT 6:  %s" %details;
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                tdkTestObj.setResultStatus("SUCCESS");

                                #Revert ApWmmEnable to initial value
                                print "\nTEST STEP 7: Revert the enabled state to %s using wifi_setApWmmEnable api" %initial_enable;
                                print "EXPECTED RESULT 7: wifi_setApWmmEnable should successfully revert ApWmmEnable status";
                                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                                tdkTestObj.addParameter("methodName","setApWmmEnable")
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
                                print "TEST STEP 6 : Verify if ApWmmEnable set value and get value are same"
                                print "EXPECTED RESULT 6 : wifi_getApWmmEnable() returned enable state different from the set value"
                                print "ACTUAL RESULT 6:  %s" %details;
                                tdkTestObj.setResultStatus("FAILURE");
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: Invocation of wifi_getApWmmEnable was failure";
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
                print "ApWMMCapability is disabled"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Invocation of wifi_getApWMMCapability failed. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

