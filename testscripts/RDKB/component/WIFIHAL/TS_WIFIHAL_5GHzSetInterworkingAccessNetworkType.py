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
  <version>5</version>
  <name>TS_WIFIHAL_5GHzSetInterworkingAccessNetworkType</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set Interworking Network Access Type using the HAL API wifi_setInterworkingAccessNetworkType() and cross check the set value with wifi_getInterworkingAccessNetworkType() HAL API for all applicable Types.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_546</test_case_id>
    <test_objective>To set Interworking Network Access Type using the HAL API wifi_setInterworkingAccessNetworkType() and cross check the set value with wifi_getInterworkingAccessNetworkType() HAL API for all applicable Types.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamUIntValue</api_or_interface_used>
    <input_parameters>methodname : getInterworkingAccessNetworkType
methodname : setInterworkingAccessNetworkType
paramType : interger
param : setvalue
radioIndex : 1</input_parameters>
    <automation_approch>1. Load the wifihal module
2. With the help of the function WIFIHAL_GetOrSetParamUIntValue invoke the HAL API wifi_getInterworkingAccessNetworkType. The GET should be success. Store this initial value.
3. With the help of the function WIFIHAL_GetOrSetParamUIntValue invoke the HAL API wifi_setInterworkingAccessNetworkType, set the different types and validate with wifi_getInterworkingAccessNetworkType.
4. Revert to initial value
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from the WIFIHAL Stub.
7. Unload the module</automation_approch>
    <expected_output>Setting Interworking Network Access Type using the HAL API wifi_setInterworkingAccessNetworkType() and cross checking the set value with wifi_getInterworkingAccessNetworkType() HAL API for all applicable Types should be success.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetInterworkingAccessNetworkType</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def get_NetworkAccessType(tdkTestObj, idx, step):
    type = -1;
    tdkTestObj.addParameter("methodName","getInterworkingAccessNetworkType")
    tdkTestObj.addParameter("radioIndex", idx)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "TEST STEP %d: Invoke the wifi_getInterworkingAccessNetworkType api and retrieve the Type" %step;
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

def set_NetworkAccessType(tdkTestObj, idx, setvalue, step):
    tdkTestObj.addParameter("methodName","setInterworkingAccessNetworkType")
    tdkTestObj.addParameter("radioIndex", idx)
    tdkTestObj.addParameter("paramType", "integer")
    tdkTestObj.addParameter("param", setvalue)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "TEST STEP %d: Invoke the wifi_setInterworkingAccessNetworkType api and set the type" %step;
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

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetInterworkingAccessNetworkType');

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
        #Retrieve the initial Type
        step = 1;
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamUIntValue");
        initial_type = get_NetworkAccessType(tdkTestObj, idx, step);
        print "Initial Interworking Network Access Type is :%d" %initial_type;

        if initial_type != -1:
            #Valid Network Types
            valid_types = range(0,16);
            for settype in valid_types :
                step = step + 1;
                network = get_NetworkType(settype);
                print "\n*****Setting Network Type to %d : %s*****" %(settype, network);
                set_NetworkAccessType(tdkTestObj, idx, settype, step);
                step = step + 1;
                get_type = get_NetworkAccessType(tdkTestObj, idx, step);

                if get_type == settype:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The Set Type and Get Type are the same";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "The Set Type and Get Type are not the same";
            #Revert Operation
            print "\nRevert to Initial Network Access Type";
            step = step + 1;
            set_NetworkAccessType(tdkTestObj, idx, initial_type, step);
        else:
            print "Invocation of wifi_getInterworkingAccessNetworkType is failure";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

