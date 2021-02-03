##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzGetAtmBandDistributionType</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To query wifi_getAtmBandDistributionType api and check whether expected Distribution Type is received</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_464</test_case_id>
    <test_objective>This  test case is to query Atm Band Distribution Type and check whether expected Distribution Type is received</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getAtmBandDistributionType</api_or_interface_used>
    <input_parameters>radioIndex</input_parameters>
    <automation_approch>1.Load wifihal module
2.Query the wifi_getAtmBandDistributionType check if the api call is success
3.Check if the Band Distribution Type  value is equal to the configured value
4.Unload the module</automation_approch>
    <expected_output>wifi_getAtmBandDistributionType api call should be success and expected Band Distribution Type has to be received</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetAtmBandDistributionType</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from wifiUtility import *
radio = "2.4G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetAtmBandDistributionType');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetAtmBandDistributionType');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        getMethod = "getAtmBandDistributionType"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'

        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details =details.split(":")[1];
            details = int(details.replace("\\n", "").strip());

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            expectedresult="SUCCESS";
            cmd = "sh %s/tdk_utility.sh parseConfigFile ATM_BAND_DISTRIBUTION_TYPE" %TDK_PATH;
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            bandDistribution = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult  and bandDistribution != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Get the ATM Band Distribution from /etc/tdk_platform.properties file";
                print "EXPECTED RESULT 1: Should get the ATM Band Distribution";
                print "ACTUAL RESULT 1: Got the ATM Band Distribution as %s" %bandDistribution;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                if int(details) == int(bandDistribution):
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Check if the current ATM Band Distribution Type is %s" %bandDistribution;
                    print "EXPECTED RESULT 2: Should get the current ATM Band Distribution Type as %s" %bandDistribution;
                    print "ACTUAL RESULT 2: The current ATM Band Distribution Type is :",details;
                    print "TEST EXECUTION RESULT : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Check if the current ATM Band Distribution Type is %s" %bandDistribution;
                    print "EXPECTED RESULT 2: Should get the current ATM Band Distribution Type as %s" %bandDistribution;
                    print "ACTUAL RESULT 2: The current ATM Band Distribution Type is :",details;
                    print "TEST EXECUTION RESULT : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Get the ATM Band Distribution from /etc/tdk_platform.properties file";
                print "EXPECTED RESULT 1: Should get the ATM Band Distribution";
                print "ACTUAL RESULT 1: Got the ATM Band Distribution as %s" %bandDistribution;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
