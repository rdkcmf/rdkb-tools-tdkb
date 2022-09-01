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
  <name>TS_WIFIHAL_5GHzSetOperatingChannelBandwidth_20MHz</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the operating channel bandwidth to 20MHz</synopsis>
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
    <test_case_id>TS_WIFIHAL_106</test_case_id>
    <test_objective>To set the operating channel bandwidth to 20MHz for 5GHz and verify the set value by getting it</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getChannelBandwidth()
wifi_setChannelBandwidth()</api_or_interface_used>
    <input_parameters>methodName  : getChannelBandwidth
methodName  : setChannelBandwidth
radioIndex :1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get the current operating channel bandwidth for 5GHz
3.Invoke "WIFIHAL_GetOrSetParamStringValue" to set the current operating channel bandwidth to 20MHz
4.Invoke "WIFIHAL_GetOrSetParamStringValue" to get the previously set operating channel bandwidth
5.Check if the value returned is same as the value set or not
6. If not, return failure
7. Revert if the value has changed from initial value
8.Unload wifihal module</automation_approch>
    <expected_output>Should successfully set the operating channel bandwidth to 20MHz and successfully get it for 5GHz radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>Wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetOperatingChannelBandwidth_20MHz</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetOperatingChannelBandwidth_20MHz');
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        setBW = '20MHz';
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        #Giving the method name to invoke the api for getting current operating channel bandwidth, wifi_getRadioOperatingChannelBandwidth()
        tdkTestObj.addParameter("methodName","getChannelBandwidth");
        tdkTestObj.addParameter("radioIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            print "TEST STEP 1: Get current radio operating channel bandwidth"
            print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
            print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
            print "TEST EXECUTION RESULT :SUCCESS"
            tdkTestObjTemp.setResultStatus("SUCCESS");
            getBandWidth = details.split(":")[1].strip()
            CurrBW=getBandWidth.split("\\n")[0];
            print "Current OperatingChannelBandwidth is  %s"%CurrBW
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            #Giving the method name to invoke the api to set the operating channel bandwidth, wifi_setRadioOperatingChannelBandwidth()
            tdkTestObj.addParameter("methodName","setRadioOperatingChannelBandwidth");
            tdkTestObj.addParameter("radioIndex",idx);
            tdkTestObj.addParameter("param",setBW);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult :
                print "TEST STEP 2: Set radio operating channel bandwidth to new value: %s" %setBW;
                print "EXPECTED RESULT: Should successfully set the radio operating channel bandwidth"
                print "ACTUAL RESULT: setChannelBandwidth: %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS"
                tdkTestObj.setResultStatus("SUCCESS");
                #Check if the operating channel bandwidth is set properly
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                #Giving the method name to invoke the api for getting current operating channel bandwidth, wifi_getRadioOperatingChannelBandwidth()
                tdkTestObj.addParameter("methodName","getChannelBandwidth");
                tdkTestObj.addParameter("radioIndex",idx);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult :
                    print "TEST STEP 3: Get radio operating channel bandwidth after the set operation"
                    print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
                    print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
                    print "TEST EXECUTION RESULT :SUCCESS"
                    tdkTestObjTemp.setResultStatus("SUCCESS");
                    getBandWidth = details.split(":")[1].strip()
                    CheckBW=getBandWidth.split("\\n")[0];
                    print " OperatingChannelBandwidth is  %s"%CheckBW
                    if CheckBW == setBW :
                        print "TEST STEP 4 : Get radio operating channel bandwidth after the set and compare"
                        print "EXPECTED RESULT: The operating channel bandwidth after the set and get should be same"
                        print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
                        print "TEST EXECUTION RESULT :SUCCESS"
                        print "The Set and Get values for Operating Channel bandwidth are same"
                        tdkTestObjTemp.setResultStatus("SUCCESS");
                        if CheckBW != CurrBW :
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                            #Giving the method name to invoke the api to set the operating channel bandwidth, wifi_setRadioOperatingChannelBandwidth()
                            tdkTestObj.addParameter("methodName","setRadioOperatingChannelBandwidth");
                            tdkTestObj.addParameter("radioIndex",idx);
                            tdkTestObj.addParameter("param",CurrBW);
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            print "setting channel bandwidth to %s" %CurrBW;
                            if expectedresult in actualresult :
                                print "TEST STEP 5: Reverting to initial channel bandwidth"
                                print "EXPECTED RESULT : Should successfully set the operating channel bandwidth"
                                print "ACTUAL RESULT : setchannelbandwidth : %s"%details;
                                print "TEST EXECUTION RESULT : SUCCESS"
                                tdkTestObj.setResultStatus("SUCCESS");
                            else :
                                print "TEST STEP 5: Reverting to initial channel bandwidth"
                                print "EXPECTED RESULT : Should successfully set the operating channel bandwidth"
                                print "ACTUAL RESULT : setchannelbandwidth : %s"%details;
                                print "TEST EXECUTION RESULT : FAILURE"
                                tdkTestObj.setResultStatus("FAILURE");
                        else :
                            print "Revert Operation is not required"
                    else :
                        print "TEST STEP 4: Get radio operating channel bandwidth after the set and compare"
                        print "EXPECTED RESULT: The operating channel bandwidth after the set and get should be same"
                        print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
                        print "TEST EXECUTION RESULT :FAILURE"
                        tdkTestObjTemp.setResultStatus("FAILURE");
                else :
                    print "TEST STEP 3: Get current radio operating channel bandwidth"
                    print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
                    print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
                    print "TEST EXECUTION RESULT :FAILURE"
                    tdkTestObjTemp.setResultStatus("FAILURE");
            else :
                print "TEST STEP 2: Set radio operating channel bandwidth to new value"
                print "EXPECTED RESULT: Should successfully set the radio operating channel bandwidth"
                print "ACTUAL RESULT: setChannelBandwidth: %s" %details;
                print "TEST EXECUTION RESULT :FAILURE"
                tdkTestObj.setResultStatus("FAILURE");
                print "Failed to set the channel bandwidth as %s " %setBW;
        else :
            print "TEST STEP 1: Get current radio operating channel bandwidth"
            print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
            print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
            print "TEST EXECUTION RESULT :FAILURE"
            tdkTestObjTemp.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

