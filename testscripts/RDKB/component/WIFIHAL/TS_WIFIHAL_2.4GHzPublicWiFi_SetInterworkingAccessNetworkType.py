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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetInterworkingAccessNetworkType</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set Interworking Network Access Type using the HAL API wifi_setInterworkingAccessNetworkType() and cross check the set value with wifi_getInterworkingAccessNetworkType() HAL API for all applicable Types for 2.4GHz Public WiFi.</synopsis>
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
    <test_case_id>TC_WIFIHAL_565</test_case_id>
    <test_objective>To set Interworking Network Access Type using the HAL API wifi_setInterworkingAccessNetworkType() and cross check the set value with wifi_getInterworkingAccessNetworkType() HAL API for all applicable Types for 2.4GHz Public WiFi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamUIntValue</api_or_interface_used>
    <input_parameters>methodname : getInterworkingAccessNetworkType
methodname : setInterworkingAccessNetworkType
paramType : interger
param : setvalue
apIndex : fetched from platform properties file</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Get the 2.4GHz Public WiFi AP Index from platform.properties file
3. With the help of the function WIFIHAL_GetOrSetParamUIntValue invoke the HAL API wifi_getInterworkingAccessNetworkType for 2.4GHz Public WiFi. The GET should be success. Store this initial value.
4. With the help of the function WIFIHAL_GetOrSetParamUIntValue invoke the HAL API wifi_setInterworkingAccessNetworkType, set the different types and validate with wifi_getInterworkingAccessNetworkType for 2.4GHz Public WiFi.
5. Revert to initial value
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from the WIFIHAL Stub.
8. Unload the module</automation_approch>
    <expected_output>Setting Interworking Network Access Type using the HAL API wifi_setInterworkingAccessNetworkType() and cross checking the set value with wifi_getInterworkingAccessNetworkType() HAL API for all applicable Types should be success for 2.4GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetInterworkingAccessNetworkType</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def get_NetworkAccessType(tdkTestObj, apIndex, step):
    type = -1;
    tdkTestObj.addParameter("methodName","getInterworkingAccessNetworkType")
    tdkTestObj.addParameter("radioIndex", apIndex)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "TEST STEP %d: Invoke the wifi_getInterworkingAccessNetworkType api and retrieve the Type for 2.4GHz Public WiFi" %step;
    print "EXPECTED RESULT %d:Invocation of wifi_getInterworkingAccessNetworkType should be success and Type should be retrieved" %step;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        type = int(details.split(":")[1].strip());

        if type in range(0,16):
            tdkTestObj.setResultStatus("SUCCESS");
            print "InterworkingAccessNetworkType = %d" %type;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "InterworkingAccessNetworkType = %d" %type;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return type;

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

def set_NetworkAccessType(tdkTestObj, apIndex, setvalue, step):
    tdkTestObj.addParameter("methodName","setInterworkingAccessNetworkType")
    tdkTestObj.addParameter("radioIndex", apIndex)
    tdkTestObj.addParameter("paramType", "integer")
    tdkTestObj.addParameter("param", setvalue)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "TEST STEP %d: Invoke the wifi_setInterworkingAccessNetworkType api and set the type for 2.4GHz Public WiFi" %step;
    print "EXPECTED RESULT %d:Invocation of wifi_setInterworkingAccessNetworkType should be success and type set successfully" %step;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return;

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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetInterworkingAccessNetworkType');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetInterworkingAccessNetworkType');

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

        step = 2;
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamUIntValue");
        initial_type = get_NetworkAccessType(tdkTestObj, apIndex, step);
        print "Initial Interworking Network Access Type is :%d" %initial_type;

        if initial_type != -1:
            #Valid Network Types
            valid_types = range(0,16);

            for settype in valid_types :
                step = step + 1;
                network = get_NetworkType(settype);
                print "\n*****Setting Network Type to %d : %s*****" %(settype, network);
                set_NetworkAccessType(tdkTestObj, apIndex, settype, step);
                step = step + 1;
                get_type = get_NetworkAccessType(tdkTestObj, apIndex, step);

                if get_type == settype:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The Set Type and Get Type are the same";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "The Set Type and Get Type are not the same";

            #Revert Operation
            print "\nRevert to Initial Network Access Type";
            step = step + 1;
            set_NetworkAccessType(tdkTestObj, apIndex, initial_type, step);
        else:
            print "Invocation of wifi_getInterworkingAccessNetworkType is failure";
            tdkTestObj.setResultStatus("FAILURE");
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

