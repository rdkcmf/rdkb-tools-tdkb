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
  <version>4</version>
  <name>TS_WIFIHAL_5GHzGetInterworkingAccessNetworkType</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke wifi_getInterworkingAccessNetworkType() HAL API and retrieve the Interworking Network Access Type.</synopsis>
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
    <test_case_id>TC_WIFIHAL_544</test_case_id>
    <test_objective>To invoke wifi_getInterworkingAccessNetworkType() HAL API and retrieve the Interworking Network Access Type.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamUIntValue</api_or_interface_used>
    <input_parameters>methodname : getInterworkingAccessNetworkType
radioIndex : 1</input_parameters>
    <automation_approch>1. Load the wifihal module
2. With the help of the function WIFIHAL_GetOrSetParamUIntValue invoke the HAL API wifi_getInterworkingAccessNetworkType. The GET should be success.
3. Validation of  the result is done within the python script and send the result status to Test Manager.
4. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from the WIFIHAL Stub.
5. Unload the module</automation_approch>
    <expected_output>wifi_getInterworkingAccessNetworkType() HAL API should be invoked successfully and the Interworking Network Access Type retrieved</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetInterworkingAccessNetworkType</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetInterworkingAccessNetworkType');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Script to load the configuration file of the component
        print "TEST STEP 1: Invoke the wifi_getInterworkingAccessNetworkType api";
        print "EXPECTED RESULT 1:Invocation of wifi_getInterworkingAccessNetworkType should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamUIntValue");
        tdkTestObj.addParameter("methodName","getInterworkingAccessNetworkType")
        tdkTestObj.addParameter("radioIndex", idx)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getInterworkingAccessNetworkType was success.";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "TEST STEP 2: Get the value of InterworkingAccessNetworkType";
            print "EXPECTED RESULT 2 : Should get the InterworkingAccessNetworkType in the range 0 to 15";
            type = int(details.split(":")[1].strip());
            network = get_NetworkType(type);

            if type in range(0,16):
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "ACTUAL RESULT 2: InterworkingAccessNetworkType = %d" %type;
                 print "The Network Type corresponds to :%s" %network;
                 print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "ACTUAL RESULT 2: InterworkingAccessNetworkType = %d" %type;
                 print "The Type is not withn the range :%s" %network;
                 print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

