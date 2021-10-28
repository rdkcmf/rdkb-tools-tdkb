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
  <name>TS_WIFIHAL_6GHzGetOperatingChannelBandwidth</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the values returned by wifi_getRadioOperatingChannelBandwidth() is in the enumeration list.</synopsis>
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
    <test_case_id>TC_WIFIHAL_605</test_case_id>
    <test_objective>Check if the values returned by wifi_getRadioOperatingChannelBandwidth() is in the enumeration list</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioOperatingChannelBandwidth()</api_or_interface_used>
    <input_parameters>methodName : getChannelBandwidth</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioOperatingChannelBandwidth() to get channel banwidth
3.Check if the bandwidth is from the enumeration list [20MHz, 40MHz, 80MHz, 160MHz, Auto]
5. Unload wifihal module</automation_approch>
    <expected_output>Operating bandwidth should be from the enumeration list [20MHz, 40MHz, 80MHz, 160MHz, Auto]</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetOperatingChannelBandwidth</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetOperatingChannelBandwidth');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:

            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            #Giving the method name to invoke the api for getting Radio Channel bandwidth. ie,wifi_getRadioOperatingChannelBandwidth()
            tdkTestObj.addParameter("methodName","getChannelBandwidth");
            #Radio index is 0 for 6GHz and 1 for 5GHz
            tdkTestObj.addParameter("radioIndex",idx);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            ExpectedList = ["20MHz", "40MHz", "80MHz", "160MHz", "Auto"];
            if expectedresult in actualresult :
                Bandwidth= details.split(":")[1];
                Bandwidth=Bandwidth.split("\\n")[0];
                print Bandwidth;
                if Bandwidth in ExpectedList:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 1: Get the Radio channel bandwidth for 6GHz";
                    print "EXPECTED RESULT 1: Should get the Radio channel bandwidth for 6GHz";
                    print "ACTUAL RESULT 1: %s" %Bandwidth;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Operating Channel bandwidth is not from the expected list"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Get the Radio channel bandwidth for 6GHz";
                print "EXPECTED RESULT 1: Should get the Radio channel bandwidth for 6GHz";
                print "ACTUAL RESULT 1: %s" %Bandwidth;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
