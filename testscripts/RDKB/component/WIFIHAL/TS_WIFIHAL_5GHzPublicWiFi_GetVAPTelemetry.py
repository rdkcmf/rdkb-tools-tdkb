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
  <version>1</version>
  <name>TS_WIFIHAL_5GHzPublicWiFi_GetVAPTelemetry</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetVAPTelemetry</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getVAPTelemetry() to retrieve the Tx Overflow value for 5GHz Public WiFi and cross check the value with the TR181 parameter Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_TXOverflow.</synopsis>
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
    <test_case_id>TC_WIFIHAL_589</test_case_id>
    <test_objective>Invoke the HAL API wifi_getVAPTelemetry() to retrieve the Tx Overflow value for 5GHz Public WiFi and cross check the value with the TR181 parameter Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_TXOverflow.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getVAPTelemetry</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_TXOverflow
apIndex : retrieved from platform property file</input_parameters>
    <automation_approch>1. Load the modules
2. Retrieve the AP index of 5GHz Public WiFi from the platform property file.
3. Invoke the function WIFIHAL_GetVAPTelemetry which in turn invokes the HAL API wifi_getVAPTelemetry() and get the value for Tx Overflow.
4. Query the TR181 parameter Device.WiFi.AccessPoint.10.X_COMCAST-COM_TXOverflow and get the Tx Overflow value.
5. Compare the Tx overflow values returned from HAL layer and DML layer. Return success if they are equal.
6. Unload the modules</automation_approch>
    <expected_output>The Tx Overflow value retrieved via the HAL API wifi_getVAPTelemetry and the TR181 parameter Device.WiFi.AccessPoint.{i}.X_COMCAST-COM_TXOverflow should be equal for 5GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_GetVAPTelemetry</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_GetVAPTelemetry');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_GetVAPTelemetry');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_GetVAPTelemetry');

#Get the module loading status
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
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
        print "\nTEST STEP 1: Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_5G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        #Get the VAPTelemetry details
        print "\nTEST STEP 2: Invoke the HAL API wifi_getVAPTelemetry() for 5GHz Public WiFi";
        print "EXPECTED RESULT 2: Should invoke wifi_getVAPTelemetry() successfully";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetVAPTelemetry");
        tdkTestObj.addParameter("apIndex", apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: wifi_getVAPTelemetry() invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            print "\nTEST STEP 3: Get the value of VAP Tx Overflow";
            print "EXPECTED RESULT 3: Should get the value of VAP Tx Overflow";

            if details != "":
                print "Details : %s" %details;
                tx_overflow = int(details.split("= ")[1]);
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Value of Tx Overflow is : %d" %tx_overflow;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the value with TR-181 parameter
                index = apIndex + 1;
                param = "Device.WiFi.AccessPoint." + str(index) + ".X_COMCAST-COM_TXOverflow";
                print "\nTEST STEP 4: Get the TR181 value of %s" %param;
                print "EXPECTED RESULT 4: Should get the TR181 value of %s" %param;
                tdkTestObj = obj1.createTestStep('WIFIAgent_Get');
                tdkTestObj.addParameter("paramName",param);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult and details != "":
                    value = int(details.split("VALUE:")[1].split(' ')[0]);
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: The TR181 value is fetched successfully : %d" %value;
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
                    print "ACTUAL RESULT 4: The TR181 value is not fetched successfully";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Value of Tx Overflow is : %d" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: wifi_getVAPTelemetry() was not invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "TEST STEP 1: Get APINDEX_5G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_5G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_5G_PUBLIC_WIFI from property file :", details ;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

