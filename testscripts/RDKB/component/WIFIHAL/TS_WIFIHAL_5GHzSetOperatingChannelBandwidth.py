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
  <version>1</version>
  <name>TS_WIFIHAL_5GHzSetOperatingChannelBandwidth</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the operating channel bandwidth for 5GHz and verify the set value by getting it</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_106</test_case_id>
    <test_objective>To set the operating channel bandwidth for 5GHz and verify the set value by getting it</test_objective>
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
3.Invoke "WIFIHAL_GetOrSetParamStringValue" to set the current operating channel bandwidth to a different value
4.Invoke "WIFIHAL_GetOrSetParamStringValue" to get the previously set operating channel bandwidth
5.Check if the value returned is same as the value set or not
6. If not, return failure
7.Unload wifihal module</automation_approch>
    <except_output>Should successfullly set the operating channel bandwidth and successfully get it</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetOperatingChannelBandwidth</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetOperatingChannelBandwidth');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    bandWidthList = ['20MHz','40MHz','80MHz','160MHz','Auto'];
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
    #Giving the method name to invoke the api for getting current operating channel bandwidth, wifi_getRadioOperatingChannelBandwidth()
    tdkTestObj.addParameter("methodName","getChannelBandwidth");
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",1);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult :
        print "TEST STEP : Get current radio operating channel bandwidth"
        print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
        print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
        print "TEST EXECUTION RESULT :SUCCESS"
        getBandWidth = details.split(":")[1].strip()
        getBW=getBandWidth.split("\\n")[0];
        if getBW in bandWidthList:
            tdkTestObj.setResultStatus("SUCCESS");
            print "OperatingChannelBandwidth is from the list %s"%bandWidthList
            for setBW in bandWidthList:
                if getBW == setBW:
                    continue;
                else:
                    #Script to load the configuration file of the component
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                    #Giving the method name to invoke the api to set the operating channel bandwidth, wifi_setRadioOperatingChannelBandwidth()
                    tdkTestObj.addParameter("methodName","setChannelBandwidth");
                    #Radio index is 0 for 2.4GHz and 1 for 5GHz
                    tdkTestObj.addParameter("radioIndex",1);
                    tdkTestObj.addParameter("param",setBW);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult :
                        print "TEST STEP : Set radio operating channel bandwidth to new value :%s"%setBW;
                        print "EXPECTED RESULT: Should successfully set the radio operating channel bandwidth"
                        print "ACTUAL RESULT: setChannelBandwidth: %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS"
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Get the previously set Channel bandwidth
                        #Script to load the configuration file of the component
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                        #Giving the method name to invoke the api to get current operating channel bandwidth,wifi_getRadioOperatingChannelBandwidth()
                        tdkTestObj.addParameter("methodName","getChannelBandwidth");
                        #Radio index is 0 for 2.4GHz and 1 for 5GHz
                        tdkTestObj.addParameter("radioIndex",1);
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult :
                            print "TEST STEP : Get the previously set radio operating channel bandwidth"
                            print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
                            print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
                            print "TEST EXECUTION RESULT :SUCCESS"
                            getBandWidth = details.split(":")[1].strip()
                            tdkTestObj.setResultStatus("SUCCESS");
                            if setBW == getBandWidth:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "EXPECTED RESULT: Set and Get channel bandwidths should be the same"
                                print "ACTUAL RESULT: Set and Get channel bandwidths are the same"

                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "EXPECTED RESULT: Set and Get channel bandwidths should be the same"
                                print "ACTUAL RESULT: Set and Get channel bandwidths are not the same"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Get operation after set failed"

                        #Reverting back to inital channel bandwidth
                        #Script to load the configuration file of the component^M
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                        #Giving the method name to invoke the api to set the operating channel bandwidth, wifi_setRadioOperatingChannelBandwidth()^M
                        tdkTestObj.addParameter("methodName","setChannelBandwidth");
                        #Radio index is 0 for 2.4GHz and 1 for 5GHz^M
                        tdkTestObj.addParameter("radioIndex",1);
                        tdkTestObj.addParameter("param",getBW);
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        print "setting channel bandwidth to %s" %getBW;
                        if expectedresult in actualresult :
                            print "TEST STEP: Reverting to initial channel bandwidth"
                            print "setChannelBandwidth: %s" %details;
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Reverting to initial channel bandwidth SUCCESS"
                        else:
                            print "TEST STEP: Reverting to initial channel bandwidth"
                            print "setChannelBandwidth: %s" %details;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Reverting to initial channel bandwidth FAILED"

                    else:
                        print "TEST STEP : Set radio operating channel bandwidth to new value"
                        print "EXPECTED RESULT: Should successfully set the radio operating channel bandwidth"
                        print "ACTUAL RESULT: setChannelBandwidth: %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE"
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Failed to set the channel bandwidth as %s " %setBW;
                    break;
        else:
            print "OperatingChannelBandwidth is not from the list %s"%bandWidthList
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP : Get current radio operating channel bandwidth"
        print "EXPECTED RESULT: Should successfully get the radio operating channel bandwidth"
        print "ACTUAL RESULT: getChannelBandwidth : %s"%details;
        print "TEST EXECUTION RESULT :FAILURE"
        tdkTestObj.setResultStatus("FAILURE");
    
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

