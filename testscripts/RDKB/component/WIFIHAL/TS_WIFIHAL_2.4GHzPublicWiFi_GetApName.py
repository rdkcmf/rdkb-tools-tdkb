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
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_GetApName</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the public WiFi access point name for 2.4GHz Public WiFi</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_574</test_case_id>
    <test_objective>To get the access point name for 2.4GHz Public WiFi</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApName()</api_or_interface_used>
    <input_parameters>methodName : getApName
ApIndex : 8</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getApName()
3. The api returns a string of access point name succeeded by the ApIndex
4. Depending upon the values return SUCCESS or FAILURE
5. Unload wifihal module</automation_approch>
    <expected_output>should return Public WiFi Access Point</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_GetApName</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_GetApName');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_GetApName');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    accesspointname = "sh %s/tdk_utility.sh parseConfigFile AP_IF_NAME_8_2G" %TDK_PATH;
    print "query:%s" %accesspointname
    tdkTestObj.addParameter("command", accesspointname);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    accesspointname= tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and accesspointname != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the 2.4GHZ Access Point name from properties file";
        print "ACTUAL RESULT 1: %s" %accesspointname;
        print "EXPECTED RESULT 1: Function Should return valid AP name";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        getMethod = "getApName"
        apIndex = apIndex_2G_Public_Wifi;
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
        print "TEST STEP 2: Get the 2.4GHZ Access Point name";
        print "EXPECTED RESULT 2: Function Should return valid AP name";
        apName = details.split(":")[1].strip()
        if expectedresult in actualresult and accesspointname == apName:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: %s" %apName;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: %s" %apName;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "FAILURE: Failed to get the value of 2.4 GHZ access point name from tdk_platform.properties file"

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
