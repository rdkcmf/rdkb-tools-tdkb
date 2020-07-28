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
  <version>2</version>
  <name>TS_WIFIHAL_5GHzGetApIndexFromName</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApIndexFromName</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate wifi_getApIndexFromName for 5GHz with a valid SSID</synopsis>
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
    <test_case_id>TC_WIFIHAL_380</test_case_id>
    <test_objective>This test case is to validate wifi_getApIndexFromName for 5GHz with a valid SSID</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApIndexFromName</api_or_interface_used>
    <input_parameters>SSIDName</input_parameters>
    <automation_approch>1. Load the module
2. Using wifiUtility.getIndex() get the index for "5G"
3. Using wifi_getSSIDName() get the ssid name for above index and save it .
4. Set a new ssid name for above index using wifi_setSSIDName()
5. Invoke wifi_getApIndexFromName() with new ssid name as param and see whether the index value equals to the index for "5G"
6. Revert the ssid name to previous value.
7.Unload the module</automation_approch>
    <expected_output>With SSIDName wifi_getApIndexFromName() should return Apindex equal to the index for "5G"</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetApIndexFromName</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

radio = "5G"
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApIndexFromName');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);

    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");

    else:
            apIndex = idx;
            expectedresult="SUCCESS";
            getMethod = "getSSIDName"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

            if expectedresult in actualresult:
                initialName = details.split(":")[1].strip()

                expectedresult="SUCCESS";
                setMethod = "setSSIDName"
                setName = "5GWIFI"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setName, setMethod)

                if expectedresult in actualresult:
                    getMethod = "getSSIDName"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'

                    #Calling the method from wifiUtility to execute test case and set result status for the test.
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
                    finalName = details.split(":")[1].strip()

                    if expectedresult in actualresult:
                        if finalName == setName:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP : Compare set and get values of SSID Name"
                            print "EXPECTED RESULT : Set and get values of SSID Name should be the same"
                            print "ACTUAl RESULT : Set and get values of SSID Name are the same"
                            print "setSSIDName = ",setName
                            print "getSSIDName = ",finalName
                            print "TEST EXECUTION RESULT :SUCCESS"

                            tdkTestObj = obj.createTestStep("WIFIHAL_GetApIndexFromName");
                            tdkTestObj.addParameter("param",setName);
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            if expectedresult in actualresult:
                               print "wifi_getApIndexFromName call success";
                               index = details.split(":")[1].strip()
                               if int(idx) == int(index):
                                  #Set the result status of execution
                                  tdkTestObj.setResultStatus("SUCCESS");
                                  print "TEST STEP: Get the index from ssid name";
                                  print "EXPECTED RESULT: Should get the index as ",idx;
                                  print "ACTUAL RESULT: %s" %details;
                                  #Get the result of execution
                                  print "[TEST EXECUTION RESULT] : SUCCESS";
                               else:
                                   #Set the result status of execution
                                   tdkTestObj.setResultStatus("FAILURE");
                                   print "TEST STEP: Get the index from ssid name";
                                   print "EXPECTED RESULT: Should get the index as",idx;
                                   print "ACTUAL RESULT: %s" %details;
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "wifi_getApIndexFromName() call failed"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP : Compare set and get values of SSID Name"
                            print "EXPECTED RESULT : Set and get values of SSID Name should be the same"
                            print "ACTUAl RESULT : Set and get values of SSID Name are not the same"
                            print "setSSIDName = ",setName
                            print "getSSIDName = ",finalName
                            print "TEST EXECUTION RESULT :FAILURE"
                    else:
                        print "wifi_getSSIDName() function failed";
                        tdkTestObj.setResultStatus("FAILURE");
                    #Revert the SSID NAme back to initial value
                    setMethod = "setSSIDName"
                    primitive = 'WIFIHAL_GetOrSetParamStringValue'
                    #Calling the method from wifiUtility to execute test case and set result status for the test.
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialName, setMethod)

                    if expectedresult in actualresult:
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "Successfully reverted back to initial value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to revert to initial value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "wifi_setSSIDName function failed";
            else:
                print "wifi_getSSIDName function failed";
                tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
