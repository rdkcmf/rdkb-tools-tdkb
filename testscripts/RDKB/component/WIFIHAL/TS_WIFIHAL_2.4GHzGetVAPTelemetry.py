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
  <name>TS_WIFIHAL_2.4GHzGetVAPTelemetry</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetVAPTelemetry</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getVAPTelemetry() to fetch the Tx Overflow and compare the value retrieved with the TR-181 parameter Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow.</synopsis>
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
    <test_case_id>TC_WIFIHAL_593</test_case_id>
    <test_objective>Invoke the HAL API wifi_getVAPTelemetry() to fetch the Tx Overflow and compare the value retrieved with the TR-181 parameter Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetVAPTelemetry
WIFIAgent_Get</api_or_interface_used>
    <input_parameters>apIndex : 0
paramName : Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow</input_parameters>
    <automation_approch>1. Load the wifihal and wifiagent modules.
2. Invoke the function WIFIHAL_GetVAPTelemetry which in turn invokes wifi_getVAPTelemetry() HAL API and retrieve the value of the Tx Overflow. The API should return success and the value should be valid.
3. Get the TR-181 parameter Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow. The value should be fetched successfully.
4. Cross verify the values retrieved by HAL API and the TR181 parameter. They are expected to be equal.
5. Unload the modules.</automation_approch>
    <expected_output>Invocation of the HAL API wifi_getVAPTelemetry() should be successful and the Tx Overflow value retrieved should be equal to the value of the TR-181 parameter Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetVAPTelemetry</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetVAPTelemetry');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetVAPTelemetry');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    expectedresult = "SUCCESS";

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the VAPTelemetry details
        print "TEST STEP 1: Invoke the HAL API wifi_getVAPTelemetry() successfully";
        print "EXPECTED RESULT 1: Should invoke wifi_getVAPTelemetry() successfully";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetVAPTelemetry");
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: wifi_getVAPTelemetry() invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            print "TEST STEP 2: Get the value of VAP Tx Overflow";
            print "EXPECTED RESULT 2: Should get the value of VAP Tx Overflow";

            if details != "":
                print "Details : %s" %details;
                tx_overflow = int(details.split("= ")[1]);
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Value of Tx Overflow is : %d" %tx_overflow;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the value with TR-181 parameter
                print "TEST STEP 3: Get the TR181 value of Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow";
                print "EXPECTED RESULT 3: Should get the TR181 value of Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow";
                tdkTestObj = obj1.createTestStep('WIFIAgent_Get');
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.X_COMCAST-COM_TXOverflow");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details != "":
                    value = int(details.split("VALUE:")[1].split(' ')[0]);
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: The TR181 value is fetched successfully : %d" %value;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Compare the values retrieved via HAL API and TR-181
                    if value == tx_overflow :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "The TR181 value is the same as the value retrieved from HAL API";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "The TR181 value is not the same as the value retrieved from HAL API";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: The TR181 value is not fetched successfully";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Value of Tx Overflow is : %d" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: wifi_getVAPTelemetry() was not invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    obj.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

