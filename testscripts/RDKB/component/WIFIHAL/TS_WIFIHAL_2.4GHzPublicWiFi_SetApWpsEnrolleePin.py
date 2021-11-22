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
  <version>2</version>
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetApWpsEnrolleePin</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the HAL API wifi_setApWpsEnrolleePin() and set the Enrollee PIN for 2.4GHz Public WiFi after ensuring that WPS is enabled for the corresponding AP using the HAL API wifi_setApWpsEnable() and wifi_getApWpsEnable().</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_600</test_case_id>
    <test_objective>To invoke the HAL API wifi_setApWpsEnrolleePin() and set the Enrollee PIN for 2.4GHz Public WiFi    after ensuring that WPS is enabled for the corresponding AP using the HAL API wifi_setApWpsEnable() and wifi_getApWpsEnable().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApWpsEnrolleePin
wifi_getApWpsEnable
wifi_setApWpsEnable</api_or_interface_used>
    <input_parameters>methodName : getApWpsEnable
methodName : setApWpsEnable
methodNmae : setApWpsEnrolleePin
apIndex : retrieved from the platform property file
PIN: 12345670</input_parameters>
    <automation_approch>1. Load the modules
2. Retrieve the 2.4GHz Public WiFi AP index from the platform property file.
3. Invoke the function WIFIHAL_GetOrSetParamBoolValue which in turn will invoke the HAL API wifi_getApWpsEnable.
4. If the WPS Enable is Disabled, then invoke the function WIFIHAL_GetOrSetParamBoolValue which in turn will invoke the HAL API wifi_setApWpsEnable to set the WPS to Enabled state.
5. After cross checking the WPS Enable state with the get API, invoke the HAL API wifi_setApWpsEnrolleePin and set a valid Enrolle Pin. The API should return success.
6. Revert the WPS Enable state if required
7. Unload the modules.</automation_approch>
    <expected_output>The HAL API wifi_setApWpsEnrollePin() should be invoked successfully after enabling WPS using wifi_setApWpsEnable() for 2.4GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetApWpsEnrolleePin</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApWpsEnrolleePin');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApWpsEnrolleePin');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

def EnrolleePinWPS(idx, step):
    print "\n*******************Setting AP WPS Enrollee Pin**********************";
    status = 1;
    PIN = "12345670";
    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamStringValue');
    tdkTestObj.addParameter("radioIndex", idx);
    tdkTestObj.addParameter("methodName", "setApWpsEnrolleePin");
    tdkTestObj.addParameter("param", PIN);

    expectedresult="SUCCESS";

    print "\nTEST STEP %d: Invoke the function wifi_setApWpsEnrolleePin() for 2.4 GHz Public WiFi" %step;
    print "EXPECTED RESULT %d: The API invocation should be success" %step;
    print "Enrollee PIN to be set : %s" %PIN;
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    time.sleep(20);
    print "Sleeping 20s for the change to get reflected";

    if expectedresult in actualresult :
        status = 0;
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: %s " %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: %s " %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
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
        print "\nTEST STEP 1: Get APINDEX_2G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_2G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        #Check if WPS is enabled or not
        print "\nTEST STEP 2: Check if WPS is enabled by invoking the wifi_getApWpsEnable API for 2.4GHz Public WiFi";
        print "EXPECTED RESULT 2:Invocation of wifi_getApWpsEnable should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getApWpsEnable");
        tdkTestObj.addParameter("radioIndex", apIndex);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getApWpsEnable was success. Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            ApWPSEnable = details.split(":")[1].strip();
            print "ApWPSEnable received : %s" %ApWPSEnable;
            step = 3;

            if "Enabled" in ApWPSEnable:
                print "Access point WPS is enabled";
                status = EnrolleePinWPS(apIndex, step);

                if status == 0:
                    print "Set WPS EnrolleePin operation success";
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "Set WPS EnrolleePin operation failed";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "Access point WPS is Disabled"
                oldEnable = 0
                newEnable = 1

                #Enable WPS
                print "\nInvoke setApWpsEnable() to enable WPS"
                print "\nTEST STEP %d: Toggle the enabled state using wifi_setApWPSEnable API for 2.4GHz Public WiFi" %step;
                print "EXPECTED RESULT %d: wifi_setApWpsEnable should successfully toggle ApWPSEnable status to Enabled" %step;
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","setApWpsEnable")
                tdkTestObj.addParameter("radioIndex", apIndex)
                tdkTestObj.addParameter("param", newEnable)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                time.sleep(20);
                print "Sleeping 20s for set to get reflected....";

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d:  %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if WPS is enabled
                    step = step + 1;
                    print "\nTEST STEP %d: Check if WPS is enabled by invoking the wifi_getApWpsEnable API for 2.4GHz Public WiFi" %step;
                    print "EXPECTED RESULT %d:Invocation of wifi_getApWpsEnable should be success" %step;
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                    tdkTestObj.addParameter("methodName","getApWpsEnable");
                    tdkTestObj.addParameter("radioIndex", apIndex);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Invocation of wifi_getApWpsEnable was success. Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        ApWPSEnable = details.split(":")[1].strip();
                        print "ApWPSEnable received : %s" %ApWPSEnable;

                        if "Enabled" in ApWPSEnable:
                            print "Access point WPS is enabled";
                            step = step + 1;
                            status = EnrolleePinWPS(apIndex, step);

                            if status == 0:
                                print "Set WPS EnrolleePin operation success";
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "Set WPS EnrolleePin operation failed";
                                tdkTestObj.setResultStatus("FAILURE");

                            #Revert the WPS to initial value
                            step = step + 1;
                            print "\nTEST STEP %d: Revert the enabled state using wifi_setApWPSEnable API for 2.4GHz Public WiFi" %step;
                            print "EXPECTED RESULT %d: wifi_setApWpsEnable should successfully revert ApWPSEnable status to Disabled" %step;
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                            tdkTestObj.addParameter("methodName","setApWpsEnable")
                            tdkTestObj.addParameter("radioIndex", apIndex)
                            tdkTestObj.addParameter("param", oldEnable)
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            time.sleep(20);
                            print "Sleeping 20s for set to get reflected....";

                            if expectedresult in actualresult and details != "":
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Revert operation success" %(step);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Revert operation success" %(step);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            print "setApWpsEnable has returned false success"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "getApWpsEnable operation failed"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "ACTUAL RESULT 2: Invocation of wifi_setApWpsEnable operation failed";
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST EXECUTION RESULT : FAILURE";
        else:
            print "ACTUAL RESULT 2: Invocation of wifi_getApWpsEnable operation failed"
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST EXECUTION RESULT : FAILURE";
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

