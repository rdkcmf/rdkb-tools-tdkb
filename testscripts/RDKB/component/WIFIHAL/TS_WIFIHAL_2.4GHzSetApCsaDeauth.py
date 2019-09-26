##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzSetApCsaDeauth</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate wifi_setApCsaDeauth() HAL API by trying to switch between different modes and check the return status of the API for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_317</test_case_id>
    <test_objective>To validate wifi_setApCsaDeauth() HAL API by trying to switch between different modes and check the return status of the API fo 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApCsaDeauth()</api_or_interface_used>
    <input_parameters>methodName : setApCsaDeauth
radioIndex : 0
mode : 0(none) , 1(unicast), 2(broadcast)</input_parameters>
    <automation_approch>1. Load the wifihal module.
2. Switch the ApCsaDeauth mode to None by invoking wifi_setApCsaDeauth() HAL API.
3. If API return status is SUCCESS, switch the mode to unicast by invoking wifi_setApCsaDeauth() HAL API.
4. If API return status is SUCCESS, switch the mode to broadcast by invoking wifi_setApCsaDeauth() HAL API.
5. Finally, set the mode back to default mode : broadcast
6. Unload the module.
</automation_approch>
    <except_output>Should successfully switch between the modes for 2.4GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApCsaDeauth</test_script>
    <skipped>No</skipped>
    <release_version>M66</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApCsaDeauth');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;


def setApCsaDeauth(obj,mode) :
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamIntValue");
    tdkTestObj.addParameter("methodName","setApCsaDeauth");
    tdkTestObj.addParameter("radioIndex",0);
    #mode is 0:none;1:unicast;2:broadcast
    tdkTestObj.addParameter("param",mode);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj,actualresult,details)

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj,actualresult,details = setApCsaDeauth(obj,0);
    expectedresult="SUCCESS";
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "**************************************************";
        print "TEST STEP 1: To switch the ApCsaDeauth mode to None for 2.4GHz";
        print "EXPECTED RESULT 1: Should successfully switch the ApCsaDeauth mode to None for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "**************************************************";
        tdkTestObj,actualresult,details = setApCsaDeauth(obj,1);
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "**************************************************";
            print "TEST STEP 2: To switch the ApCsaDeauth mode to unicast for 2.4GHz";
            print "EXPECTED RESULT 2: Should successfully switch the ApCsaDeauth to unicast for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "**************************************************";
            tdkTestObj,actualresult,details = setApCsaDeauth(obj,2);
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "**************************************************";
                print "TEST STEP 3: To switch the ApCsaDeauth mode to broadcast for 2.4GHz";
                print "EXPECTED RESULT 3: Should successfully switch the broadcast to broadcast for 2.4GHz";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                print "**************************************************";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "**************************************************";
                print "TEST STEP 3: To switch the ApCsaDeauth mode to broadcast for 2.4GHz";
                print "EXPECTED RESULT 3: Should successfully switch the broadcast to broadcast for 2.4GHz";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "**************************************************";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "**************************************************";
            print "TEST STEP 2: To switch the ApCsaDeauth mode to unicast for 2.4GHz";
            print "EXPECTED RESULT 2: Should successfully switch the ApCsaDeauth to unicast for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
            print "**************************************************";

            #Revert the mode to default mode(broadcast)
            tdkTestObj,actualresult,details = setApCsaDeauth(obj,2);
            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "Successfully reverted the mode to default mode:broadcast for 2.4GHz";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "Unable to revert the mode to default mode:broadcast for 2.4GHz";
    else :
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "**************************************************";
        print "TEST STEP 1: To switch the ApCsaDeauth mode to None for 2.4GHz";
        print "EXPECTED RESULT 1: Should successfully switch the ApCsaDeauth mode to None for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "**************************************************";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
