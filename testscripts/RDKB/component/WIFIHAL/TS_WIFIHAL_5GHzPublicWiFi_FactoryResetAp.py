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
  <version>14</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzPublicWiFi_FactoryResetAp</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_ParamApIndex</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Restore Public WiFi AP parameters to default without changing other AP or Radio parameters.</synopsis>
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
    <test_case_id>TC_WIFIHAL_573</test_case_id>
    <test_objective>To Restore Public WiFi AP parameters to default without changing other AP nor Radio parameters</test_objective>
    <test_type>Positive</test_type>
    <test_setup>braodband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setSSIDName
wifi_getSSIDName
wifi_factoryResetAP</api_or_interface_used>
    <input_parameters>methodName : setSSIDName
methodName : getSSIDName
methodName : factoryResetAP
apIndex : fetched from platform properties file</input_parameters>
    <automation_approch>1.Load the module.
2. Get the 5GHz Public WiFi AP Index from platform.properties file
3. Modify current ssid name by passing the parameters apindex and ssid using wifi_setSSIDName() API by  invoking WIFIHAL_GetOrSetParamStringValue4. Confirm that this ssid has been set properly by using wifi_getSSIDName() API  by  invoking WIFIHAL_GetOrSetParamStringValue
5. The factory reset API should be now invoked using wifi_factoryResetAP() API.
6. If factoryResetAP call is success , then the SSID name should be set to default value.
7. To confirm that the API  has worked, check the SSID by using  wifi_getSSIDName() API  which  invokes WIFIHAL_GetOrSetParamStringValue.
8.Compare the SSID set before and after factory reset and confirm that this should be different.
9.Check if the api call is success, else return FAILURE from the script
10.Unload the module.</automation_approch>
    <expected_output>The SSID before and after the factory reset should be different.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_FactoryResetAp</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
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
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_FactoryResetAp');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_FactoryResetAp');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

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

        getMethod = "getSSIDName"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'
        #Calling the method from wifiUtility to execute test case and set result status for the test.
        print "TEST STEP 2 : Get the initial SSID";
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

        if expectedresult in actualresult:
            SSIDName_initial = details.split(":")[1].strip()
            print "SSIDName_initial:", SSIDName_initial

            setMethod = "setSSIDName"
            SSIDName_beforeFactoryReset = "wifi_ssid"
            print "TEST STEP 3 : Setting SSIDName";
            print "Trying to set a new SSIDName = ",SSIDName_beforeFactoryReset
            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, SSIDName_beforeFactoryReset, setMethod)

            if expectedresult in actualresult:
                print "TEST STEP 4: Get the current SSID name and compare with the set valule"
                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                if expectedresult in actualresult:
                    SSIDName_set = details.split(":")[1].strip()
                    print "SSIDName_set = ",SSIDName_set

                    if SSIDName_set == SSIDName_beforeFactoryReset:
                        print "Set and Get values are the same";
                        #Prmitive test case which associated to this Script
                        print "Invoking wifi_factroryResetAP()"
                        print "TEST STEP 5: Invoke wifi_factoryResetAP";
                        print "EXPECTED RESULT 5: wifi_factoryResetAP should be invoked successfully";
                        tdkTestObj = obj.createTestStep('WIFIHAL_ParamApIndex');
                        tdkTestObj.addParameter("apIndex", apIndex);
                        tdkTestObj.addParameter("methodName", 'factoryResetAP');
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        sleep(5);

                        if expectedresult in actualresult:
                            print "ACTUAL RESULT 5 : wifi_factoryResetAP invocation success"
                            print "Get the SSID name after invocation of wifi_factoryResetAP"
                            #Calling the method from wifiUtility to execute test case and set result status for the test.
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                            if expectedresult in actualresult:
                                SSIDName_afterFactoryReset = details.split(":")[1].strip()
                                print "Get SSID name operation is success"
                                print "TEST STEP 6: Compare values of SSID Name before and after wifi_factoryResetAP"
                                print "EXPECTED RESULT 6: The values of SSID Name should be different"
                                print "SSIDName_beforeFactoryReset = ",SSIDName_beforeFactoryReset
                                print "SSIDName_afterFactoryReset = ",SSIDName_afterFactoryReset

                                if SSIDName_afterFactoryReset !=  SSIDName_beforeFactoryReset:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAl RESULT 6: The values of SSID Name are different"
                                    print "TEST EXECUTION RESULT :SUCCESS"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAl RESULT 6: The values of SSID Names are the same"
                                    print "TEST EXECUTION RESULT :FAILURE"
                            else:
                                print "wifi_getSSIDName() function failed"
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            print "wifi_factoryResetAP() function failed"
                            print "TEST EXECUTION RESULT 5:FAILURE"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "The Get and Set values are not the same"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "wifi_getSSIDName() function failed"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "wifi_setSSIDName() function failed"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "wifi_getSSIDName() function before factoryResetAP failed"
            tdkTestObj.setResultStatus("FAILURE");
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

