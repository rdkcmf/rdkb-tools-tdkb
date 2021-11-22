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
  <name>TS_WIFIHAL_6GHzGetRadioStandard</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the current radio standard for 6GHz using the HAL API wifi_getRadioStandard() and to check whether it one of the supported standards for 6GHz as per wifi_getRadioSupportedStandards()</synopsis>
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
    <test_case_id>TC_WIFIHAL_673</test_case_id>
    <test_objective>To get the current radio standard for 6GHz using the HAL API wifi_getRadioStandard() and to check whether it one of the supported standards for 6GHz as per wifi_getRadioSupportedStandards()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioSupportedStandards()
wifi_getRadioStandard()
</api_or_interface_used>
    <input_parameters>methodname : getRadioSupportedStandards
methodname : getRadioStandard
radioIndex : 6G radio index</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRadioSupportedStandards() and retrieve the supported standards for 6G radio.
3. Invoke the HAL API wifi_getRadioStandard() to get the current 6G radio standard and check if the current standard is a subset of the supported standards.
4. Unload the module.</automation_approch>
    <expected_output>The current radio standard for 6GHz using the HAL API wifi_getRadioStandard() should be from the supported standards for 6GHz as per wifi_getRadioSupportedStandards().</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioStandard</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioStandard');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    #Script to load the configuration file of the component
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Invoke the HAL API to get the radio supported standards
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        tdkTestObj.addParameter("methodName","getRadioSupportedStandards");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        SupportedStandards = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Get the Radio Supported Standards for 6GHz using the HAL API wifi_getRadioSupportedStandards()";
        print "EXPECTED RESULT 1: Should get the Radio Supported Standards for 6GHz";

        if expectedresult in actualresult:
            SplitList = SupportedStandards.split(":")[1].split(",")
            ActualList = [standard.strip() for standard in SplitList];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: The radio supported standards are : %s" %SupportedStandards;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the current radio standard using wifi_getRadioStandard()
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetRadioStandard");
            tdkTestObj.addParameter("methodName","getRadioStandard")
            tdkTestObj.addParameter("radioIndex",idx);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 2: Get the current Radio standard for 6GHz using the HAL API wifi_getRadioStandard()";
            print "EXPECTED RESULT 2: Should get the Radio standard for 6GHz";

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: The current radio standard is : %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if current standard is from the supported list
                print "\nTEST STEP 3: Check if the current standard is from the supported list of standards";
                print "EXPECTED RESULT 3: The current standard should be from the supported list of standards";
                CurrStandard = details.split(":")[1].split(" ")[0];

                if CurrStandard in ActualList :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: The current radio standard from the supported list is : %s" %CurrStandard;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: The current radio standard is : %s which is not from supported list" %CurrStandard;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: The current radio standard is : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: The radio supported standards are : %s" %SupportedStandards;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
