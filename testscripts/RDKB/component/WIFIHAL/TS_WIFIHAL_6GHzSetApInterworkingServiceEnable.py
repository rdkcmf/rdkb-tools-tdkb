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
  <name>TS_WIFIHAL_6GHzSetApInterworkingServiceEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Interworking Service Enable status is successfully toggled using the HAL API wfi_setApInterworkingServiceEnable() for 6G Private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_735</test_case_id>
    <test_objective>To check if the Interworking Service Enable status is successfully toggled using the HAL API wfi_setApInterworkingServiceEnable() for 6G Private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApInterworkingServiceEnable()
wifi_setApInterworkingServiceEnable()</api_or_interface_used>
    <input_parameters>methodname : getApInterworkingServiceEnable
methodname : setApInterworkingServiceEnable
radioIndex : 6G private AP index
param : newEnable</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getApInterworkingServiceEnable() for 6G Private AP and store the initial enable state.
3. Toggle the enable state by invoking the HAL API wifi_setApInterworkingServiceEnable() for 6G private AP and check if the SET API returns success.
4. Invoke the GET API and check if the enable value SET is retrieved via GET.
5. Revert to initial state.
6. Unload the modules.</automation_approch>
    <expected_output>The Interworking Service Enable status should be successfully toggled using the HAL API wfi_setApInterworkingServiceEnable() for 6G Private AP.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetApInterworkingServiceEnable</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApInterworkingServiceEnable');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApInterworkingServiceEnable');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        print "\nTEST STEP 2: Invoke the wifi_getApInterworkingServiceEnable() api for 6G private AP";
        print "EXPECTED RESULT 2:Invocation of wifi_getApInterworkingServiceEnable() should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getApInterworkingServiceEnable")
        tdkTestObj.addParameter("radioIndex", apIndex)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getApInterworkingServiceEnable was success. Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            enable = details.split(":")[1].strip()

            if "Enabled" in enable:
                oldEnable = 1
                newEnable = 0
                newStatus = "Disabled"
            else:
                oldEnable = 0
                newEnable = 1
                newStatus = "Enabled"

            #Toggle the enable status
            print "\nTEST STEP 3: Toggle the enabled state using wifi_setApInterworkingServiceEnable() api for 6G private AP";
            print "EXPECTED RESULT 3: wifi_setApInterworkingServiceEnable() should successfully toggle Interworking Service Enable status to ",newStatus ;
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setApInterworkingServiceEnable")
            tdkTestObj.addParameter("radioIndex", apIndex)
            tdkTestObj.addParameter("param", newEnable)
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Validate the SET with GET
                print "\nTEST STEP 4: Invoke  wifi_getApInterworkingServiceEnable to verify toggling done by wifi_setApInterworkingServiceEnable() api";
                print "EXPECTED RESULT 4: wifi_getApInterworkingServiceEnable should return the value set by wifi_setApInterworkingServiceEnable()";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getApInterworkingServiceEnable")
                tdkTestObj.addParameter("radioIndex", apIndex)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: Invocation of wifi_getApInterworkingServiceEnable was success. Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    print "\nTEST STEP 5 : Verify if ApInterworkingServiceEnable set value and get value are same";
                    print "EXPECTED RESULT 5 : wifi_getApInterworkingServiceEnable() returned enable state same as the set value";
                    enable = details.split(":")[1].strip();
                    print "SET value : %s" %newStatus;
                    print "GET value : %s" %enable;

                    if enable == newStatus :
                        print "ACTUAL RESULT 5:  SET value maches with the GET value";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Revert ApInterworkingServiceEnable to initial value
                        print "\nTEST STEP 6: Revert the enabled state to %s using wifi_setApInterworkingServiceEnable api" %enable;
                        print "EXPECTED RESULT 6: wifi_setApInterworkingServiceEnable should successfully revert ApInterworkingServiceEnable status";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","setApInterworkingServiceEnable")
                        tdkTestObj.addParameter("radioIndex", apIndex)
                        tdkTestObj.addParameter("param", oldEnable)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6:  %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6: API invocation failed; Details :%s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "ACTUAL RESULT 5: SET value does not match with the GET value";
                        tdkTestObj.setResultStatus("FAILURE");
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: API invocation failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: API invocation failed; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
