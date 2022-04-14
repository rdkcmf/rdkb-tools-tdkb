##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_WIFIHAL_6GHzSetApWpsConfiguration_WithWPSEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_SetApWpsConfiguration</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke the HAL API wifi_setApWpsConfiguration() and set the WPS Mode to enabled, WPS PIN to a valid value and WPS Methods to Display and PushButton and cross check if the WPS configuration SET is reflected in the GET API wifi_getApWpsConfiguration() for 6G private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_781</test_case_id>
    <test_objective>Invoke the HAL API wifi_setApWpsConfiguration() and set the WPS Mode to enabled, WPS PIN to a valid value and WPS Methods to Display and PushButton and cross check if the WPS configuration SET is reflected in the GET API wifi_getApWpsConfiguration() for 6G private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApWpsConfiguration()
wifi_getApWpsConfiguration()</api_or_interface_used>
    <input_parameters>apIndex : 6G private AP index
radioIndex : 6G radio index
enable : WPS Enabled or Disabled(1/0)
pin : WPS PIN(8 digit numeral)
methods : WPS methods combined value </input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getApWpsConfiguration() for 6G private access point.
3. If the API invocation is success store the initial values of WPS Mode, WPS PIN and WPS Methods if WPS Mode is enabled.
4. Check if the values retrieved are valid(if WPS Mode is enabled) : The WPS PIN should be a valid numeral and WPS Methods hexadecimal values should be from {'0x0001' : "USB_FLASHDRIVE", '0x0002' : "ETHERNET", '0x0004' : "LABEL", '0x0008' : "DISPLAY", '0x0010' : "EXTERNAL_NFC_TOKEN", '0x0020' : "INTEGRATED_NFC_TOKEN", '0x0040' : "NFC_INTERFACE", '0x0080' : "PUSH_BUTTON", '0x0100' : "PIN", '0x0200' : "PHYSICAL_PUSHBUTTON", '0x0400' : "PHYSICAL_DISPLAY", '0x0800' : "VIRTUAL_PUSH_BUTTON", '0x1000' : "VIRTUAL_DISPLAY", '0x2000' : "EASY_CONNECT"}. If WPS Mode is disabled, WPS PIN and WPS Methods will not be retrieved.
5. Invoke the HAL API wifi_setApWpsConfiguration() and set WPS Mode to enabled, WPS PIN to a new valid 8 digit numeral and WPS Methods to a Bitwise OR result of the values of Push Button and Display Methods(the combination that allows for PIN setting).
6. Check if the SET API returns success.
7. If the SET API returns success, invoke wifi_getApWpsConfiguration() to retrieve the current WPS configuration values.
8. Cross check if the WPS Mode, PIN and Methods GET matches with the values SET.
9. Revert to initial state
10. Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_setApWpsConfiguration() to set the WPS Mode to enabled, WPS PIN to a valid value and WPS Methods to Display and PushButton should be invoked successfully and the WPS configuration SET should be reflected in the GET API wifi_getApWpsConfiguration() for 6G private AP.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetApWpsConfiguration_WithWPSEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def getApWpsConfiguration(obj, apIndex):
    expectedresult = "SUCCESS";
    primitive = 'WIFIHAL_GetApWpsConfiguration';
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("apIndex", apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details, tdkTestObj;

def setApWpsConfiguration(obj, apIndex, radioIndex, setvalues):
    expectedresult = "SUCCESS";
    primitive = 'WIFIHAL_SetApWpsConfiguration'
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("apIndex", apIndex);
    tdkTestObj.addParameter("radioIndex", radioIndex);
    tdkTestObj.addParameter("enable", setvalues[0]);

    #Additional parameters can only be set if the WPS mode is enabled
    if setvalues[0] == 1:
        tdkTestObj.addParameter("pin", setvalues[1]);
        tdkTestObj.addParameter("methods", setvalues[2]);

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details, tdkTestObj;

def getApWpsConfigurationDetails(details):
    status = "FAILURE";
    #To store the WPS Configutration values
    values = [];
    wps_mode = details.split("WPS Mode : ")[1].split(",")[0];
    print "WPS Mode : %s" %wps_mode;
    values.append(wps_mode);

    #If WPS mode is enabled, get the WPS PIN and WPS Methods
    if "Enabled" in wps_mode:
        wps_pin = details.split("WPS device PIN: ")[1].split(",")[0];
        print "WPS PIN : %s" %wps_pin;
        values.append(wps_pin);

        if wps_pin != "" and wps_pin.isdigit():
            wps_methods = [];
            method = "";
            wps_configuration_method = "";
            invalid_flag = 0;
            wps_methods = details.split("WPS enabled configuration methods : ")[1].strip().split(" ");

            if len(wps_methods) > 0:
                print "WPS Methods are :-";
                #Map the WPS Methods Hex values to the corresponding WPS Configuration Method
                wps_method_dict = {'0x0001' : "USB_FLASHDRIVE", '0x0002' : "ETHERNET", '0x0004' : "LABEL", '0x0008' : "DISPLAY", '0x0010' : "EXTERNAL_NFC_TOKEN", '0x0020' : "INTEGRATED_NFC_TOKEN", '0x0040' : "NFC_INTERFACE", '0x0080' : "PUSH_BUTTON", '0x0100' : "PIN", '0x0200' : "PHYSICAL_PUSHBUTTON", '0x0400' : "PHYSICAL_DISPLAY", '0x0800' : "VIRTUAL_PUSH_BUTTON", '0x1000' : "VIRTUAL_DISPLAY", '0x2000' : "EASY_CONNECT"};

                for method in wps_methods :
                    if method in wps_method_dict :
                        wps_configuration_method = wps_method_dict[method];
                        values.append(method);
                    else :
                        invalid_flag = 1;
                        wps_configuration_method = "Invalid WPS Configuration Method";

                    print "%s : %s" %(method, wps_configuration_method);

                if invalid_flag == 1:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "WPS Configuration Methods lists invalid values";
                else:
                    status = "SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "WPS Configuration Methods are valid values";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "WPS Configuration Methods not retrieved";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "WPS PIN retrieved is not valid";
    else:
        tdkTestObj.setResultStatus("SUCCESS");
        print "As WPS Enable Mode is Disabled, cannot retrieve the WPS PIN and WPS Methods";
    return values, status;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApWpsConfiguration_WithWPSEnabled');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApWpsConfiguration_WithWPSEnabled');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if an invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
        tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

        if apIndex == -1:
            print "Failed to get the Access Point index";
            tdkTestObjTemp.setResultStatus("FAILURE");
        else:
            #Invoke the Get AP WPS Configuration
            actualresult, details, tdkTestObj = getApWpsConfiguration(obj, apIndex);

            print "\nTEST STEP 2: Invoke the HAL API wifi_getApWpsConfiguration() for 6G private AP";
            print "EXPECTED RESULT 2: Should invoke the HAL API successfully";

            if expectedresult in actualresult and "getApWpsConfiguration invoked successfully" in details:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: API was invoked successfully; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the WPS configuration details
                initial_values, status = getApWpsConfigurationDetails(details);
                print "\nTEST STEP 3: Get the Access Point WPS Configuration and check if the initial values are valid";
                print "EXPECTED RESULT 3: Should get the Access Point WPS Configuration successfully and the initial values should be valid";

                if status == "SUCCESS":
                    print "ACTUAL RESULT 3: The Access Point WPS Configuration are retrieved and all initial values are valid";
                    print "TEST EXECUTION RESULT 3: SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");

                    #Set AP WPS Configuration
                    #Enable status of new WPS mode is Enabled
                    new_mode = 1;
                    new_enable = "Enabled";

                    #Get the 8 digit WPS PIN to be set
                    cmd= "sh %s/tdk_utility.sh parseConfigFile WPS_PIN" %TDK_PATH;
                    print cmd;
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    new_pin = tdkTestObj.getResultDetails().replace("\\n", "");

                    print "\nTEST STEP 4: Get the 8 digit WPS PIN to be set from property file";
                    print "EXPECTED RESULT 4: Should get the 8 digit WPS PIN from property file"

                    if expectedresult in actualresult and new_pin.isdigit():
                        print "ACTUAL RESULT 4: WPS PIN retrieved from the platform property file";
                        print "TEST EXECUTION RESULT :SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Set the new WPS Configuration modes as Display(0x0008) PushButton(0x0080) - Combine the Hex values of the 2 configurations using Bitwise OR
                        Display = 0x0008;
                        PushButton = 0x0080;
                        new_methods = PushButton | Display;
                        setvalues = [new_mode, new_pin, new_methods];
                        radioIndex = idx;

                        actualresult, details, tdkTestObj = setApWpsConfiguration(obj, apIndex, radioIndex, setvalues);
                        print "\nTEST STEP 5 : Invoke the HAL API wifi_setApWpsConfiguration() for 6G private AP with WPS Mode : %s, WPS PIN : %s and WPS Methods : %s(After combining Display-0x0008 and PushButton-0x0080 methods)" %(setvalues[0], setvalues[1], setvalues[2]);
                        print "EXPECTED RESULT 5 : The HAL API wifi_setApWpsConfiguration() should be invoked successfully";

                        if expectedresult in actualresult:
                            print "ACTUAL RESULT 5: The wifi_setApWpsConfiguration() API returned success; Details : %s" %details;
                            print "TEST EXECUTION RESULT 5: SUCCESS";
                            tdkTestObj.setResultStatus("SUCCESS");

                            #Cross check the SET with GET
                            actualresult, details, tdkTestObj = getApWpsConfiguration(obj, apIndex);
                            print "\nTEST STEP 6: Invoke the HAL API wifi_getApWpsConfiguration() for 6G private AP after the SET operation";
                            print "EXPECTED RESULT 6: Should successfully invoke wifi_getApWpsConfiguration()";

                            if expectedresult in actualresult and "getApWpsConfiguration invoked successfully" in details:
                                print "ACTUAL RESULT 6: wifi_getApWpsConfiguration() invoked successfully";
                                print "TEST EXECUTION RESULT 6: SUCCESS";
                                tdkTestObj.setResultStatus("SUCCESS");

                                #Get the access point WPS details and check if the values SET are GET
                                final_values, status = getApWpsConfigurationDetails(details);
                                print "\nTEST STEP 7: Get the Access Point WPS Configuration and check if the retrieved values are valid";
                                print "EXPECTED RESULT 7: Should get the Access Point WPS Configuration successfully and the retrieved values should be valid";

                                if status == "SUCCESS":
                                    print "ACTUAL RESULT 7: The Access Point WPS Configuration details are retrieved and all retrieved values are valid";
                                    print "TEST EXECUTION RESULT 7: SUCCESS";
                                    tdkTestObj.setResultStatus("SUCCESS");

                                    print "WPS Mode SET : %s" %new_enable;
                                    print "WPS Mode GET : %s" %final_values[0];
                                    print "WPS PIN SET : %s" %setvalues[1];
                                    print "WPS PIN GET : %s" %final_values[1];

                                    #Convert the WPS Methods GET to its equivalent decimal representation
                                    final_wps_methods = 0;
                                    for num_of_methods in range(2, len(final_values)):
                                        final_wps_methods = final_wps_methods | int(final_values[num_of_methods], 16);

                                    print "WPS Methods SET : %s" %setvalues[2];
                                    print "WPS Methods GET : %s" %final_wps_methods;

                                    if (new_enable == final_values[0]) and (setvalues[1] == final_values[1]) and (setvalues[2] == final_wps_methods):
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "The GET values match with the SET values";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "The GET values do not match with the SET values";
                                else:
                                    print "ACTUAL RESULT 7: The Access Point Security details are retrieved and all retrieved values are not valid";
                                    print "TEST EXECUTION RESULT 7: FAILURE";
                                    tdkTestObj.setResultStatus("FAILURE");
                            else:
                                print "ACTUAL RESULT 6: wifi_getApWpsConfiguration() not invoked successfully";
                                print "TEST EXECUTION RESULT 6: FAILURE";
                                tdkTestObj.setResultStatus("FAILURE");

                            #Revert operation
                            initial_wps_methods = 0;
                            if initial_values[0] == "Enabled":
                                initial_mode = 1;
                            else:
                                initial_mode = 0;

                            for num_of_methods in range(2, len(initial_values)):
                                initial_wps_methods = initial_wps_methods | int(initial_values[num_of_methods], 16);

                            setvalues = [initial_mode, initial_values[1], initial_wps_methods];
                            actualresult, details, tdkTestObj = setApWpsConfiguration(obj, apIndex, radioIndex, setvalues);
                            print "\nTEST STEP 8 : Revert to initial AP WPS Configuration";
                            print "EXPECTED RESULT 8: Revert operation should be success";

                            if expectedresult in actualresult:
                                print "ACTUAL RESULT 8: The SET API returned success; Details : %s" %details;
                                print "TEST EXECUTION RESULT 8: SUCCESS";
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "ACTUAL RESULT 8: The SET API returned failure; Details : %s" %details;
                                print "TEST EXECUTION RESULT 8: FAILURE";
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            print "ACTUAL RESULT 5: The wifi_setApWpsConfiguration() API returned failure; Details : %s" %details;
                            print "TEST EXECUTION RESULT 5: FAILURE";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "ACTUAL RESULT 4: 8-digit WPS PIN not retrieved from platform property file : ", new_pin ;
                        print "TEST EXECUTION RESULT 4:FAILURE";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "ACTUAL RESULT 3: All Access Point WPS Configuration details are not valid";
                    print "TEST EXECUTION RESULT 3: FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
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
