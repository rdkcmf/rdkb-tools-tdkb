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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_GetInterworkingAccessNetworkType</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To invoke wifi_getInterworkingAccessNetworkType() HAL API for 2.4GHz Public WiFi and retrieve the Interworking Network Access Type.</synopsis>
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
    <test_case_id>TC_WIFIHAL_561</test_case_id>
    <test_objective>To invoke wifi_getInterworkingAccessNetworkType() HAL API for 2.4GHz Public WiFi and retrieve the Interworking Network Access Type.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamUIntValue</api_or_interface_used>
    <input_parameters>methodname : getInterworkingAccessNetworkType
apIndex : fetched from platform properties file</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Get the 2.4GHz Public WiFi AP Index from platform.properties file
3. With the help of the function WIFIHAL_GetOrSetParamUIntValue invoke the HAL API wifi_getInterworkingAccessNetworkType for 2.4GHz Public WiFi. The GET should be success.
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from the WIFIHAL Stub.
6. Unload the module</automation_approch>
    <expected_output>wifi_getInterworkingAccessNetworkType() HAL API should be invoked successfully for 2.4GHz Public WiFi and the Interworking Network Access Type retrieved</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_GetInterworkingAccessNetworkType</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def get_NetworkType(type):
    #From 8.4.2.94 of IEEE Std 802.11-2012 - Possible values are: 0 - Private network;1 - Private network with guest access;2 - Chargeable public network;3 - Free public network;4 - Personal device network;5 - Emergency services only network;6-13 - Reserved;14 - Test or experimental;15 - Wildcard

    if type == 0:
        network = "Private network";
    elif type == 1:
        network = "Private network with guest access";
    elif type == 2:
        network = "Chargeable public network";
    elif type == 3:
        network = "Free public network";
    elif type == 4:
        network = "Personal device network";
    elif type == 5:
        network = "Emergency services only network";
    elif (type >= 6) and (type <= 13):
        network = "Reserved";
    elif type == 14:
        network = "Test or experimental";
    elif type == 15:
        network = "Wildcard";
    else:
        network = "Invalid Network Type";
    return network;


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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_GetInterworkingAccessNetworkType');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_GetInterworkingAccessNetworkType');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

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

        print "TEST STEP 2: Invoke the wifi_getInterworkingAccessNetworkType api for 2.4GHz Public WiFi";
        print "EXPECTED RESULT 2:Invocation of wifi_getInterworkingAccessNetworkType should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamUIntValue");
        tdkTestObj.addParameter("methodName","getInterworkingAccessNetworkType")
        tdkTestObj.addParameter("radioIndex", apIndex)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Invocation of wifi_getInterworkingAccessNetworkType was success.";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            print "TEST STEP 3: Get the value of InterworkingAccessNetworkType";
            print "EXPECTED RESULT 3 : Should get the InterworkingAccessNetworkType in the range 0 to 15";
            type = int(details.split(":")[1].strip());
            network = get_NetworkType(type);

            if type in range(0,16):
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: InterworkingAccessNetworkType = %d" %type;
                print "The Network Type corresponds to :%s" %network;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: InterworkingAccessNetworkType = %d" %type;
                print "The Type is not within the range :%s" %network;
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
    print "Module loading FAILURE";

