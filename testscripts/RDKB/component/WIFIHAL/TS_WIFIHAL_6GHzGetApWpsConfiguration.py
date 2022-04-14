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
  <name>TS_WIFIHAL_6GHzGetApWpsConfiguration</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApWpsConfiguration</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApWpsConfiguration() for 6G private AP and check if the WPS enabled is retrieved successfully and WPS PIN and WPS Methods are valid if WPS mode is enabled.</synopsis>
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
    <test_case_id>TC_WIFIHAL_778</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApWpsConfiguration() for 6G private AP and check if the WPS enabled is retrieved successfully and WPS PIN and WPS Methods are valid if WPS mode is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApWpsConfiguration()</api_or_interface_used>
    <input_parameters>apIndex : 6G private access point index</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getApWpsConfiguration() for 6G private access point.
3. If the API is invoked successfully, retrieve the WPS Mode(enabled/disabled) parameter value.
4. If the WPS Mode is retrieved as enabled, fetch the WPS PIN and WPS Methods parameter values. The WPS PIN should be a valid numeral and WPS Methods hexadecimal values should be from {'0x0001' : "USB_FLASHDRIVE", '0x0002' : "ETHERNET", '0x0004' : "LABEL", '0x0008' : "DISPLAY", '0x0010' : "EXTERNAL_NFC_TOKEN", '0x0020' : "INTEGRATED_NFC_TOKEN", '0x0040' : "NFC_INTERFACE", '0x0080' : "PUSH_BUTTON", '0x0100' : "PIN", '0x0200' : "PHYSICAL_PUSHBUTTON", '0x0400' : "PHYSICAL_DISPLAY", '0x0800' : "VIRTUAL_PUSH_BUTTON", '0x1000' : "VIRTUAL_DISPLAY", '0x2000' : "EASY_CONNECT"}
5. If WPS Mode is disabled WPS PIN and WPS Methods will not be retrieved.
6. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getApWpsConfiguration() should be invoked successfully for 6G private AP and the WPS PIN and WPS Methods should be retrieved if WPS Mode is enabled and not retrieved when it is disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApWpsConfiguration</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
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
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApWpsConfiguration');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApWpsConfiguration');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    #Check if an invalid index is returned
    if apIndex == -1:
        print "Failed to get the 6G access point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep("WIFIHAL_GetApWpsConfiguration");
        tdkTestObj.addParameter("apIndex", apIndex);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2: Invoke the HAL API wifi_getApWpsConfiguration() for 5G private AP";
        print "EXPECTED RESULT 2: Should invoke the HAL API successfully";

        if expectedresult in actualresult and "getApWpsConfiguration invoked successfully" in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: API was invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check the enable status of WPS
            print "\nTEST STEP 3: Check the enable status of WPS Enable";
            print "EXPECTED RESULT 3 : Should retrieve the enable status of WPS successfully";
            wps_mode = details.split("WPS Mode : ")[1].split(",")[0];

            if "Enabled" in wps_mode or "Disabled" in wps_mode:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: WPS Enable Mode = %s" %wps_mode;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #If WPS mode is enabled, get the WPS PIN and WPS Methods
                if "Enabled" in wps_mode:
                    print "\nTEST STEP 4: Get the WPS PIN";
                    print "EXPECTED RESULT 4 : Should retrieve the WPS PIN successfully";
                    wps_pin = details.split("WPS device PIN: ")[1].split(",")[0];

                    if wps_pin != "" and wps_pin.isdigit():
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: WPS PIN = %s" %wps_pin;
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        wps_methods = [];
                        method = "";
                        wps_configuration_method = "";
                        invalid_flag = 0;
                        print "\nTEST STEP 4: Get the WPS Methods";
                        print "EXPECTED RESULT 4 : Should retrieve the WPS Methods successfully";
                        wps_methods =  details.split("WPS enabled configuration methods : ")[1].strip().split(" ");

                        if len(wps_methods) > 0:
                            #Map the WPS Methods Hex values to the corresponding WPS Configuration Method
                            wps_method_dict = {'0x0001' : "USB_FLASHDRIVE", '0x0002' : "ETHERNET", '0x0004' : "LABEL", '0x0008' : "DISPLAY", '0x0010' : "EXTERNAL_NFC_TOKEN", '0x0020' : "INTEGRATED_NFC_TOKEN", '0x0040' : "NFC_INTERFACE", '0x0080' : "PUSH_BUTTON", '0x0100' : "PIN", '0x0200' : "PHYSICAL_PUSHBUTTON", '0x0400' : "PHYSICAL_DISPLAY", '0x0800' : "VIRTUAL_PUSH_BUTTON", '0x1000' : "VIRTUAL_DISPLAY", '0x2000' : "EASY_CONNECT"};

                            for method in wps_methods :
                                if method in wps_method_dict :
                                    wps_configuration_method = wps_method_dict[method];
                                else :
                                    invalid_flag = 1;
                                    wps_configuration_method = "Invalid WPS Configuration Method";
                                print "%s : %s" %(method, wps_configuration_method);

                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: WPS Methods = ", wps_methods;
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if invalid_flag == 1:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "WPS Configuration Methods lists invalid values";
                            else:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "WPS Configuration Methods are valid values";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: WPS Methods = ", wps_methods;
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: WPS PIN = %s; Value retrieved is invalid" %wps_pin;
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "As WPS Enable Mode is Disabled, cannot retrieve the WPS PIN and WPS Methods";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: WPS Enable Mode = %s; Value retrieved is invalid" %wps_mode;
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
