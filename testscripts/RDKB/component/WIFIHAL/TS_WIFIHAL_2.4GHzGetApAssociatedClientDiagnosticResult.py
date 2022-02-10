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
  <name>TS_WIFIHAL_2.4GHzGetApAssociatedClientDiagnosticResult</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAssociatedClientDiagnosticResult</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApAssociatedClientDiagnosticResult() with the connected client MAC address and check if the client diagnostic results are retrieved successfully for 2.4G Private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_737</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApAssociatedClientDiagnosticResult() with the connected client MAC address and check if the client diagnostic results are retrieved successfully for 2.4G Private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script
3.Connect a wifi client to 2.4G private AP.</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedClientDiagnosticResult()
wifi_getApAssociatedDeviceDiagnosticResult3()</api_or_interface_used>
    <input_parameters>apIndex : 2.4G private AP index
mac_addr : MAC address of the client connected to 2.4G Private AP.</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult3() to retrieve the MAC Address of an associated client of 2.4G private AP.
3. Invoke the HAL API wifi_getApAssociatedClientDiagnosticResult() with the connected client MAC Address and check if the API invocation is success.
4. Unload the modules</automation_approch>
    <expected_output>The HAL API wifi_getApAssociatedClientDiagnosticResult() with the connected client MAC address should be invoked successfully and the client diagnostic results should be retrieved for 2.4G Private AP.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAssociatedClientDiagnosticResult</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from time import sleep;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAssociatedClientDiagnosticResult');

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

            if int(output_array_size) != 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Number of associated clients : %d" %(int(output_array_size));
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Get the MAC address of the client
                mac = details.split("MAC")[1].split(",")[0].split("=")[1].strip();

                if mac != " ":
                    #Modify the MAC to remove the colon symbols
                    mac_addr = mac.split(":");
                    mac_addr = mac_addr[0]+mac_addr[1]+mac_addr[2]+mac_addr[3]+mac_addr[4]+mac_addr[5];
                    print "MAC Address of the client : %s" %mac_addr;

                    #Get the AP associated client diagnostic result
                    tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedClientDiagnosticResult');
                    tdkTestObj.addParameter("apIndex", idx);
                    tdkTestObj.addParameter("mac_addr", mac_addr);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP 3: Invoke the HAL API wifi_getApAssociatedClientDiagnosticResult() with the MAC Address : %s" %mac_addr;
                    print "EXPECTED RESULT 3: wifi_getApAssociatedClientDiagnosticResult() should be invoked successfully";

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3 : wifi_getApAssociatedClientDiagnosticResult() invoked successfully";
                        print "Client Diagnostic Result : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3 : wifi_getApAssociatedClientDiagnosticResult() not invoked successfully";
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
