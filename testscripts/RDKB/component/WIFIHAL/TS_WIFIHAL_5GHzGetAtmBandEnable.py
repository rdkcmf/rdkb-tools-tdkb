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
  <name>TS_WIFIHAL_5GHzGetAtmBandEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To query wifi_getAtmBandEnable api and check the ATM Band status</synopsis>
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
    <test_case_id>TC_WIFIHAL_467</test_case_id>
    <test_objective>This  test case is to query Atm Band Enable and check ATM Band status</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getAtmBandEnable</api_or_interface_used>
    <input_parameters>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</input_parameters>
    <automation_approch>1.Load the wifihal module
2.Check if the device is ATM Capable using wifi_getATMCapable and Enable the ATM  using wifi_setATMEnable
2.Query the wifi_getAtmBandEnable  api
3.The api call should be success and  ATM Band should be enabled
4.Revert the ATM to previous state
5.Unload the module</automation_approch>
    <expected_output>wifi_getATMEnable api call  is expected to be  success and enabled  when ATM is enabled </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetAtmBandEnable</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *
radio = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetAtmBandEnable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
revertflag =0 ;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        #passing radio index as a place holder only
        radioIndex = idx
        getMethod = "getATMCapable"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

        if expectedresult in actualresult:
            enablestate = details.split(":")[1].strip()
            if 'Disabled' in enablestate:
                print "Device is not ATM capable"
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Check if device is ATMCapable";
                print "EXPECTED RESULT : ATM Capable status should be returned";
                print "ACTUAL RESULT 1: Device is not ATM capable";
                print "[TEST EXECUTION RESULT] : FAILURE";
            elif 'Enabled' in enablestate:
                print "Device is ATM Capable "
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Check if device is ATMCapable";
                print "EXPECTED RESULT : ATM Capable status should be returned";
                print "ACTUAL RESULT 1:Device is ATM %s"%enablestate;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                expectedresult="SUCCESS";
                getMethod = "getATMEnable"
                primitive = 'WIFIHAL_GetOrSetParamBoolValue'

                tdkTestObj, actualresult, default = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod);
                if expectedresult in actualresult:
                    default = default.split(":")[1].strip();
                    tdkTestObj.setResultStatus("SUCCESS");
                    if default != "Enabled" :
                        expectedresult="SUCCESS";
                        setMethod = "setATMEnable"
                        value_to_set =1;
                        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                        print "Enabling ATM via wifi_setATMEnable api";
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, value_to_set, setMethod)

                        if expectedresult in actualresult :
                            revertflag =1;
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                    if revertflag == 1 or default  == "Enabled":
                        expectedresult="SUCCESS";
                        getMethod = "getAtmBandEnable"
                        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                        print "Verify if wifi_getAtmBandEnable returns status as Enabled";
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, idx, 0, getMethod)
                        if expectedresult in actualresult and "Enabled" in details:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "call to wifi_getATMCapable api failed"
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Check if device is ATMCapable";
                print "EXPECTED RESULT : ATM Capable status should be returned";
                print "ACTUAL RESULT 1: getATMCapable function failed %s"%enablestate;
                print "[TEST EXECUTION RESULT] : FAILURE";

    if revertflag ==1:
       print "***Performing Revert operation*****";
       expectedresult="SUCCESS";
       setMethod = "setATMEnable"
       if default == "Enabled":
           value_to_set =1;
       else:
           value_to_set = 0;

       primitive = 'WIFIHAL_GetOrSetParamBoolValue'
       tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, value_to_set, setMethod)
       if expectedresult in actualresult :
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
       else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
