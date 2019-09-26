##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzSetInvalidOperatingChannelBandwidth</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set Operating Channel Bandwidth with a value not in the list and check whether the set operation is failing for 2.4GHz</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_210</test_case_id>
    <test_objective>To set Operating Channel Bandwidth with a value not in the list and check whether the set operation is failing</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getChannelBandwidth()
wifi_setChannelBandwidth()</api_or_interface_used>
    <input_parameters>methodName  : getChannelBandwidth
methodName  : setChannelBandwidth
radioIndex :0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get the current operating channel bandwidth for 2.4GHz
3.Invoke "WIFIHAL_GetOrSetParamStringValue" to set the current operating channel bandwidth to a different value which is not in the acceptable bandwidth list.
4. The set operation should fail as we are trying to set the value not in the acceptable bandwidth list.
5.Unload wifihal module</automation_approch>
    <except_output>Set operation should fail as we are trying to set the value not in the acceptable bandwidth list.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetInvalidOperatingChannelBandwidth</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetInvalidOperatingChannelBandwidth');

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
    tdkTestObj.addParameter("radioIndex",0);
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
	    setBW = '50MHz';
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            #Giving the method name to invoke the api to set the operating channel bandwidth, wifi_setRadioOperatingChannelBandwidth()
            tdkTestObj.addParameter("methodName","setChannelBandwidth");
            #Radio index is 0 for 2.4GHz and 1 for 5GHz

            tdkTestObj.addParameter("radioIndex",0);
            tdkTestObj.addParameter("param",setBW);
            expectedresult="FAILURE";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if setBW not in bandWidthList:
		if expectedresult in actualresult :
                    print "TEST STEP : Set radio operating channel bandwidth to new value :%s"%setBW;
                    print "EXPECTED RESULT: Should not set the radio operating channel bandwidth"
                    print "ACTUAL RESULT: setChannelBandwidth: %s is not in the acceptable bandwidthList" %details;
                    print "TEST EXECUTION RESULT :SUCCESS"
                    tdkTestObj.setResultStatus("SUCCESS");
		else:
		    print "TEST STEP : Set radio operating channel bandwidth to new value :%s"%setBW;
                    print "EXPECTED RESULT: Should successfully set the radio operating channel bandwidth"
                    print "ACTUAL RESULT: setChannelBandwidth: %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE"
                    tdkTestObj.setResultStatus("FAILURE");
	            #Reverting back to inital channel bandwidth
                    #Script to load the configuration file of the component
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                    #Giving the method name to invoke the api to set the operating channel bandwidth, wifi_setRadioOperatingChannelBandwidth()
                    tdkTestObj.addParameter("methodName","setChannelBandwidth");
                    #Radio index is 0 for 2.4GHz and 1 for 5GHz
                    tdkTestObj.addParameter("radioIndex",0);
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
                print"OperatingChannelBandwidth is from the list %s"%bandWidthList
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

