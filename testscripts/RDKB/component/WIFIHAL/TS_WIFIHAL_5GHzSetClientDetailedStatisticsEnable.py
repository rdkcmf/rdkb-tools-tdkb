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
  <name>TS_WIFIHAL_5GHzSetClientDetailedStatisticsEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setClientDetailedStatisticsEnable() to enable and disable the client detailed statistics and check if the set operation returns success as expected.</synopsis>
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
    <rdk_version>RDK3</rdk_version>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_592</test_case_id>
    <test_objective>Invoke the HAL API wifi_setClientDetailedStatisticsEnable() to enable and disable the client detailed statistics and check if the set operation returns success as expected.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamBoolValue</api_or_interface_used>
    <input_parameters>methodname : setClientDetailedStatisticsEnable
radioIndex : 1
param : enable(0 or 1)</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Invoke the function WIFIHAL_GetOrSetParamBoolValue with method name as setClientDetailedStatisticsEnable to invoke the HAL API wifi_setClientDetailedStatisticsEnable() and enable the client detailed statistics. The API should return success.
3. Then invoke the same API and disable the client detailed statistics. The API should return success.
4. Unload the wifihal module.</automation_approch>
    <expected_output>The HAL API wifi_setClientDetailedStatisticsEnable() to enable and disable the client detailed statistics should be invoked successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetClientDetailedStatisticsEnable</test_script>
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

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetClientDetailedStatisticsEnable');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    expectedresult = "SUCCESS";

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Enable the ClientDetailedStatistics
        enable = 1;
        print "TEST STEP 1: Enable the ClientDetailedStatistics by invoking the HAL API wifi_setClientDetailedStatisticsEnable()";
        print "EXPECTED RESULT 1: wifi_setClientDetailedStatisticsEnable() should be invoked successfully and set to Enabled";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","setClientDetailedStatisticsEnable");
        tdkTestObj.addParameter("radioIndex", idx);
        tdkTestObj.addParameter("param", enable);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1:  %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Disable the ClientDetailedStatistics
            enable = 0;
            print "TEST STEP 2: Disable the ClientDetailedStatistics by invoking the HAL API wifi_setClientDetailedStatisticsEnable()";
            print "EXPECTED RESULT 2: wifi_setClientDetailedStatisticsEnable() should be invoked successfully and set to Disabled";
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setClientDetailedStatisticsEnable");
            tdkTestObj.addParameter("radioIndex", idx);
            tdkTestObj.addParameter("param", enable);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
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

