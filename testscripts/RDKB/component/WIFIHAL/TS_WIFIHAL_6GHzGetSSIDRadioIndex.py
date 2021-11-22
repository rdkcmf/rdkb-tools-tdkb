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
  <name>TS_WIFIHAL_6GHzGetSSIDRadioIndex</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getSSIDRadioIndex() to retrieve the radio index corresponding to the 6GHz private SSID access point and check if the value is same as 6GHz radio index.</synopsis>
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
    <test_case_id>TC_WIFIHAL_676</test_case_id>
    <test_objective>Invoke the HAL API wifi_getSSIDRadioIndex() to retrieve the radio index corresponding to the 6GHz private SSID access point and check if the value is same as 6GHz radio index.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getSSIDRadioIndex()</api_or_interface_used>
    <input_parameters>methodname : getSSIDRadioIndex
radioIndex : 6G radio index
apIndex : 6G private access point from platform property file</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getSSIDRadioIndex() to retrieve the radio index corresponding to 6G private access point.
3. Check if the radio index retrieved is matching with the 6G default radio index.
4. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getSSIDRadioIndex() should be invoked successfully to retrieve the radio index corresponding to the 6GHz private SSID access point and the value should be the same as 6GHz radio index.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetSSIDRadioIndex</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetSSIDRadioIndex');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetSSIDRadioIndex');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
        tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

        if apIndex == -1:
            print "Failed to get the Access Point index";
            tdkTestObjTemp.setResultStatus("FAILURE");
        else:
            #Checking for 6Ghz private SSID index
            ssidIndex = apIndex
            getMethod = "getSSIDRadioIndex"

            #Get the radio index corresponding to the SSID index
            tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamIntValue');
            tdkTestObj.addParameter("methodName","getSSIDRadioIndex");
            tdkTestObj.addParameter("radioIndex",apIndex);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 2 : Invoke the HAL API wifi_getSSIDRadioIndex() for the 6G Private SSID index : %d" %apIndex;
            print "EXPECTED RESULT 2 : The HAL API should be invoked successfully";

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2 : The API was invoked successfully; Details : %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the SSID radio index is same as the 6G radio Index
                radioIndex = details.split(":")[1].strip();
                #Expected Radio Index for SSID Index is defaultRadioIndex
                defaultRadioIndex = idx;
                print "The expected Radio Index corresponding to the 6G private SSID index %d is : %s" %(apIndex, defaultRadioIndex);
                print "The actual Radio Index corresponding to the 6G private SSID index %d is : %s" %(apIndex, radioIndex);

                print "\nTEST STEP 3 : Check if the SSID radio index is same as the 6G radio Index";
                print "EXPECTED RESULT 3 : The SSID radio index should be the same as the 6G radio Index"

                if radioIndex.isdigit() and int(radioIndex) == defaultRadioIndex:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: The SSID radio index is same as the 6G radio Index";
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: The SSID radio index is not the same as the 6G radio Index";
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2 : The API was not invoked successfully; Details : %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
