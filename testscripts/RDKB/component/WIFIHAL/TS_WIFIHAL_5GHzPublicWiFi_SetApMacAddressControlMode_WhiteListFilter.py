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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzPublicWiFi_SetApMacAddressControlMode_WhiteListFilter</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke wifi_setApMacAddressControlMode HAL API to set the filter control mode to WhiteList for 5GHz Public WiFi and check if the set value is getting reflected to the get API wifi_getApMacAddressControlMode.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_593</test_case_id>
    <test_objective>Invoke wifi_setApMacAddressControlMode HAL API to set the filter control mode to WhiteList for 5GHz Public WiFi and check if the set value is getting reflected to the get API wifi_getApMacAddressControlMode.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApMacAddressControlMode
wifi_setApMacAddressControlMode</api_or_interface_used>
    <input_parameters>methodname : getApMacAddressControlMode
methodname : setApMacAddressControlMode
apIndex : retrieved from platform property file
setMode : 1</input_parameters>
    <automation_approch>1. Load the modules
2. Retrieve the 5GHz Public WiFi AP index from the platform property file.
3. Invoke the function WIFIHAL_GetOrSetParamIntValue which in turn invokes the HAL API wifi_getApMacAddressControlMode() to retrieve the initial filter control mode and store it.
4. Invoke the function WIFIHAL_GetOrSetParamIntValue which in turn invokes the HAL API wifi_setApMacAddressControlMode() to set the filter control mode to 1 - WhiteList Filter.
5. Cross check if the filter mode set is retrieved with a get operation.
6. Revert to the initial filter control mode if required.
7. Unload the modules.</automation_approch>
    <expected_output>The WhiteList filter control mode set using the HAL API wifi_setApMacAddressControlMode for 2.4GHz Public WiFi should be successful and the value should get reflected when the get API wifi_getApMacAddressControlMode is invoked.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_SetApMacAddressControlMode_WhiteListFilter</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_SetApMacAddressControlMode_WhiteListFilter');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_SetApMacAddressControlMode_WhiteListFilter');

#Get the loadmodule status
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Getting APINDEX_5G_PUBLIC_WIFI value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile APINDEX_5G_PUBLIC_WIFI" %TDK_PATH;
    print cmd;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and details != "":
        apIndex = int(details);
        print "\nTEST STEP 1: Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_5G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        #Invoke the API
        print "\n*****************************Get the initial Filter Control mode*******************************";
        filter = ["Disabled", "WhiteList", "BlackList"];
        print "\nThe different Filter Control modes are, 0 : %s, 1 : %s, 2 : %s" %(filter[0], filter[1], filter[2]);

        print "\nTEST STEP 2: Invoke the wifi_getApMacAddressControlMode API for 5GHz Public WiFi";
        print "EXPECTED RESULT 2:Invocation of wifi_getApMacAddressControlMode should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
        tdkTestObj.addParameter("methodName","getApMacAddressControlMode")
        tdkTestObj.addParameter("radioIndex", apIndex)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details != "":
            initMode = int(details.split(":")[1].strip());
            print "Initial Mac Address Control Mode is : %d" %initMode;

            #Check if the Mode is valid
            if initMode == 0 or initMode == 1 or initMode == 2:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Invocation of wifi_getApMacAddressControlMode was success. Initial Mode : %s" %filter[initMode];
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #For Blacklist Filter, setMode = 1
                print "\n*****************************Set to WhiteList Filter Control mode*******************************";
                setMode = 1;
                print "\nTEST STEP 3: Set to Whitelist filter mode by invoking the API wifi_setApMacAddressControlMode for 5GHz Public WiFi";
                print "EXPECTED RESULT 3:Invocation of wifi_setApMacAddressControlMode should be success";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                tdkTestObj.addParameter("methodName","setApMacAddressControlMode")
                tdkTestObj.addParameter("radioIndex", apIndex)
                tdkTestObj.addParameter("param", setMode)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_setApMacAddressControlMode was success. Details : %s" %(details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Get the Mode
                    sleep(10);
                    print "\nTEST STEP 4: Invoke the wifi_getApMacAddressControlMode API for 5GHz Public WiFi";
                    print "EXPECTED RESULT 4: Invocation of wifi_getApMacAddressControlMode should be success";
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                    tdkTestObj.addParameter("methodName","getApMacAddressControlMode")
                    tdkTestObj.addParameter("radioIndex", apIndex)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        finalMode = details.split(":")[1].strip();
                        print "Final Mac Address Control Mode is : %s" %finalMode;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: Invocation of wifi_getApMacAddressControlMode was success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Cross check whether the filter control mode is same as the mode set
                        print "\nTEST STEP 5: Check if the Filter Control mode set is same as the get value for 5GHz Public WiFi";
                        print "EXPECTED RESULT 5: Set and get values should be the same" ;
                        print "Set value: %d" %setMode;
                        print "Get value: %d" %int(finalMode);

                        if int(finalMode) == setMode:
                            print "ACTUAL RESULT 5: Set and get values are the same";
                            print "TEST EXECUTION RESULT :SUCCESS"
                            tdkTestObj.setResultStatus("SUCCESS");

                            #Revert to initial value
                            print "\n****************************Revert to initial Filter Control Mode************************";
                            print "\nTEST STEP 6: Revert to initial filter mode by invoking the API wifi_setApMacAddressControlMode for 2.4GHz Public WiFi" ;
                            print "EXPECTED RESULT 6:Invocation of wifi_setApMacAddressControlMode should be success";
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
                            tdkTestObj.addParameter("methodName","setApMacAddressControlMode")
                            tdkTestObj.addParameter("radioIndex", apIndex)
                            tdkTestObj.addParameter("param", initMode)
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            if expectedresult in actualresult:
                                print "ACTUAL RESULT 6 : Successfully reverted to initial mode";
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                print "ACTUAL RESULT 6 : Failed to revert to initial mode";
                                tdkTestObj.setResultStatus("FAILURE");
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            print "ACTUAL RESULT 5: Set and get values are NOT the same";
                            print "TEST EXECUTION RESULT :FAILURE"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: Invocation of wifi_getApMacAddressControlMode was failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Invocation of wifi_setApMacAddressControlMode was failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Invocation of wifi_getApMacAddressControlMode was success. Initial Mode is invalid: %d" %initMode;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Invocation of wifi_getApMacAddressControlMode() function call failed"
            print "TEST EXECUTION RESULT : FAILURE";
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
    print "Module loading FAILURE";

