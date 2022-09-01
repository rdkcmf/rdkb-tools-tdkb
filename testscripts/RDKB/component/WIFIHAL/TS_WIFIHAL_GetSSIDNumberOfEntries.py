##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_GetSSIDNumberOfEntries</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the SSID number of entries</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_167</test_case_id>
    <test_objective>To get the SSID number of entries</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI </test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSSIDNumberOfEntries()</api_or_interface_used>
    <input_parameters>methodName : getSSIDNumberOfEntries</input_parameters>
    <automation_approch>1. Load wifihal and sysutil modules
2. From platform properties file retrieve the expected SSID number of entries for the DUT
3. Using  WIFIHAL_GetOrSetParamULongValue invoke wifi_getSSIDNumberOfEntries()
4. The api returns the number of ssid entries and check if the value match with the value from platform properties
5. Depending upon the values return SUCCESS else return FAILURE
6. Unload wifihal and sysutil modules</automation_approch>
    <except_output>Should return a ulong value as the number of ssid entires</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_GetSSIDNumberOfEntries</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetSSIDNumberOfEntries');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_GetSSIDNumberOfEntries ');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Getting SSID_NUMBER_OF_ENTRIES value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile SSID_NUMBER_OF_ENTRIES" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().replace("\\n", "");

    print "\nTEST STEP 1 : Get the Number of SSID entries from platform properties";
    print "EXPECTED RESULT 1 : Should get the number of SSID entries from platform properties successfully";

    if expectedresult in actualresult and details != "":
        print "ACTUAL RESULT 1: SSID Number of Entries :", details ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
        tdkTestObj.addParameter("methodName", "getSSIDNumberOfEntries");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        ssiddetails = tdkTestObj.getResultDetails().replace("\\n", "");

        print "\nTEST STEP 2: Invoke the HAL API wifi_getSSIDNumberOfEntries()";
        print "EXPECTED RESULT 2: wifi_getSSIDNumberOfEntries() API should be invoked successfully and the ";

        if expectedresult in actualresult:
            print "ACTUAL RESULT 2: API invoked successfully : ", ssiddetails;
            print "TEST EXECUTION RESULT :SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");
            ssidnumber = ssiddetails.split(":")[1].strip();

            print "\nTEST STEP 3 : Check if the value retrieved from API is same as the value in platform properties";
            print "EXPECTED RESULT 3 : The value retrieved from the API should be the same as the value in platform properties";

            if ssidnumber.isdigit() and int(ssidnumber) == int(details):
                print "ACTUAL RESULT 3: The value retrieved from the API is the same as the value in platform properties";
                print "TEST EXECUTION RESULT :SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "ACTUAL RESULT 3: The value retrieved from the API is NOT the same as the value in platform properties";
                print "TEST EXECUTION RESULT :FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "ACTUAL RESULT 2: API NOT invoked successfully";
            print "TEST EXECUTION RESULT :FAILURE";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "ACTUAL RESULT 1: SSID Number of Entries :", details ;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failure";
