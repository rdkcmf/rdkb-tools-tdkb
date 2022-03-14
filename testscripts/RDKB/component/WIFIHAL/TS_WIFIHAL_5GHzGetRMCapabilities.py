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
  <name>TS_WIFIHAL_5GHzGetRMCapabilities</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRMCapabilities</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRMCapabilities() with 5GHz connected client MAC address and check if the RM Capabilities values retrieved are valid and non-empty.</synopsis>
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
    <test_case_id>TC_WIFIHAL_760</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRMCapabilities() with 5GHz connected client MAC address and check if the RM Capabilities values retrieved are valid and non-empty.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Connect a wifi client to 5G private AP</pre_requisite>
    <api_or_interface_used>wifi_getRMCapabilities()
wifi_getApAssociatedDeviceDiagnosticResult3()</api_or_interface_used>
    <input_parameters>apIndex : 5G private AP
peer : MAC address of 5G connected client</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult3() to get the MAC address of the 5G connected client.
3. Invoke the HAL API wifi_getRMCapabilities() with the obtained MAC address. The API should be invoked successfully.
4. Check if the Capabilities values retrieved are non-empty and valid.
5. Unload the modules</automation_approch>
    <expected_output>The HAL API wifi_getRMCapabilities() with 5GHz connected client MAC address should be invoked successfully and the RM Capabilities values retrieved should be valid and non-empty.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRMCapabilities</test_script>
    <skipped>No</skipped>
    <release_version>M99</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRMCapabilities');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult3');
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "Details: %s"%details

        print "\nTEST STEP 1: Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult3()";
        print "EXPECTED RESULT 1: Should successfully invoke wifi_getApAssociatedDeviceDiagnosticResult3()";

        if expectedresult in actualresult and details != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1 : wifi_getApAssociatedDeviceDiagnosticResult3() invoked successfully";
            size = details.split(":")[1].strip();
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            output_array_size = size.split("=")[1].split(",")[0].strip();

            print "\nTEST STEP 2: The number of associated clients should be greater than 0";
            print "EXPECTED RESULT 2: The number of associated clients should be greater than 0";

            if int(output_array_size) > 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Number of associated clients : %d" %(int(output_array_size));
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Get the MAC address of the client
                mac = details.split("MAC")[1].split(",")[0].split("=")[1].strip();

                if mac != " ":
                    print "MAC Address of the client : %s" %mac;

                    #Get the AP associated client diagnostic result
                    tdkTestObj = obj.createTestStep('WIFIHAL_GetRMCapabilities');
                    tdkTestObj.addParameter("peer", mac);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP 3: Invoke the HAL API wifi_getRMCapabilities() with the MAC Address : %s" %mac;
                    print "EXPECTED RESULT 3: wifi_getRMCapabilities() should be invoked successfully";

                    if expectedresult in actualresult and "operation success" in details:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3 : wifi_getRMCapabilities() invoked successfully";
                        print "RM Capabilities details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if valid values are retrieved for the RM Capabilities
                        capabilities_0 = details.split("capabilities[0] : ")[1].split(",")[0];
                        capabilities_1 = details.split("capabilities[1] : ")[1].split(",")[0];
                        capabilities_2 = details.split("capabilities[2] : ")[1].split(",")[0];
                        capabilities_3 = details.split("capabilities[3] : ")[1].split(",")[0];
                        capabilities_4 = details.split("capabilities[4] : ")[1];

                        print "\nTEST STEP 4: Check if non-empty values are retrieved for each of RM Capabilities";
                        print "EXPECTED RESULT 4: Non-empty values should be retrieved for each of RM Capabilities";
                        print "Capbilities[0] : ", capabilities_0;
                        print "Capbilities[1] : ", capabilities_1;
                        print "Capbilities[2] : ", capabilities_2;
                        print "Capbilities[3] : ", capabilities_3;
                        print "Capbilities[4] : ", capabilities_4;

                        if capabilities_0 != "" and capabilities_1 != "" and capabilities_2 != "" and capabilities_3 != "" and capabilities_4 != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 4 : All RM Capabilities values are valid";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 4 : Not all RM Capabilities values are valid";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3 : wifi_getRMCapabilities() not invoked successfully";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "MAC Address is not fetched successfully";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Number of associated clients : %d" %(int(output_array_size));
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: Failed to invoke wifi_getApAssociatedDeviceDiagnosticResult3()";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
