##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_5GHzGetRadioSupportedStandards</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the supported standards of 5GHZ and check whether the value is within the valid supported standard list</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_16</test_case_id>
    <test_objective>To get the supported standards of 5GHZ and check whether the value is within the valid supported standard list</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioSupportedStandards()
wifi_getRadioOperatingFrequencyBand()</api_or_interface_used>
    <input_parameters>methodName : getRadioSupportedStandards
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get the Supported Standards for 5GHz
3.Check if the value returned is valid or not
4. If not, return failure
5.Unload wifihal module</automation_approch>
    <except_output>If the operating frequency is 5 GHz, then Supported Standard should be [a, n, ac]</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioSupportedStandards</test_script>
    <skipped>No</skipped>
    <release_version/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioSupportedStandards');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
    #Giving the method name to invoke the api for getting Supported standards. ie,wifi_getRadioSupportedStandards()
    tdkTestObj.addParameter("methodName","getRadioSupportedStandards");
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",1);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    SupportedStandards = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        SplitList = SupportedStandards.split(":")[1].split(",");
	ActualList = [s.strip() for s in SplitList];
        print "TEST STEP 1: Get the Radio Supported Standards for 5GHz";
        print "EXPECTED RESULT 1: Should get the Radio Supported Standards for 5GHz";
        print "ACTUAL RESULT 1: %s" %SupportedStandards;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        ExpectedStdList = ['a','n','ac'];
        for item in ActualList:
            if item in ExpectedStdList:
                returnStatus = "0";
            else:
                returnStatus = "1";
                break;
        if "0" in returnStatus:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Validate the Supported standards with operating Freq";
            print "EXPECTED RESULT 2: Supported standards should be in ['a','n','ac'] when radioIndex is 1";
            print "ACTUAL RESULT 2: Supported standards : ", ActualList;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Validate the Supported standards with operating Freq";
            print "EXPECTED RESULT 2: Supported standards should be in ['a','n','ac'] when radioIndex is 1";
            print "ACTUAL RESULT 2: Supported standards : ", ActualList;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Radio Supported Standards for 5GHz";
        print "EXPECTED RESULT 1: Should get the Radio Supported Standards 5GHz";
        print "ACTUAL RESULT 1: %s" %SupportedStandards;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
