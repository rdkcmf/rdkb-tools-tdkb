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
  <name>TS_WIFIHAL_5GHzSetRadioAMSDUEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get Radio AMSDU Enable status for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_117</test_case_id>
    <test_objective>To set AMSDU Enable status using wifi_setRadioAMSDUEnable() and verify it by getting with wifi_getRadioAMSDUEnable for 5 GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>wifi_setRadioAMSDUEnable
wifi_getRadioAMSDUEnable</api_or_interface_used>
    <input_parameters>methodName: setRadioAMSDUEnable
methodName: getRadioAMSDUEnable
radioIndex: 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using getRadioAMSDUEnable() get and save current AMSDU enable state
3.Toggle AMSDU enable state using setRadioAMSDUEnable()
4. Verify whether the set was success by getting the channel value using getRadioAMSDUEnable()
5. Revert back to the initial AMSDU enable state
6. Unload wifihal module
</automation_approch>
    <except_output>Setting AMSDU enable state using  setRadioAMSDUEnable() should be success and the enable state should be toggled
</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioAMSDUEnable</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioAMSDUEnable');

def RadioAMSDUEnable(methodName,param):
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
    #Giving the method name to invoke the api for getting RadioAMSDU Enable status
    tdkTestObj.addParameter("methodName",methodName);
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",1);
    tdkTestObj.addParameter("param",param);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj, actualresult, details);

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    methodName = "getRadioAMSDUEnable";
    #Dummy param for get method
    param = 0;
    tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,param);
    if expectedresult in actualresult :
        print "TEST STEP: Get the initial Radio AMSDU Enable status"
        print "EXPECTED RESULT : Should return either Enabled or Disabled"
        print "ACTUAL RESULT : %s" %details;
        print "TEST EXECUTION RESULT :SUCCESS"
        tdkTestObj.setResultStatus("SUCCESS");
        enable = details.split(":")[1].strip()
        print "enable:" ,enable;
        if "Enabled" in enable:
            print "AMSDU is Enabled"
            tdkTestObj.setResultStatus("SUCCESS");
            oldEnable = 1
            newEnable = 0
        else:
            print "AMSDU is Disabled"
            oldEnable = 0
            newEnable = 1

        #Toggle the enable status using set
        methodName = "setRadioAMSDUEnable"
        tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,newEnable);
        if expectedresult in actualresult :
            print "TEST STEP: Set the Radio AMSDU Enable status"
            print "EXPECTED RESULT : Should return SUCCESS"
            print "ACTUAL RESULT : %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");

            # Get the New AP enable status
            methodName = "getRadioAMSDUEnable";
            #Dummy param for get method
            param = 0;
            tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,param);
            print "details: %s" %details;
            if expectedresult in actualresult and enable not in details.split(":")[1].strip():
                print "TEST STEP: Get the previously set Radio AMSDU Enable status and compare with the initial get value"
                print "EXPECTED RESULT : Should return a status otherthan the initial get value"
                print "ACTUAL RESULT : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS"
                print "getRadioAMSDUEnable Success, verified with setRadioAMSDUEnable() api"
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "TEST STEP: Get the previously set Radio AMSDU Enable status and compare with the initial get value"
                print "EXPECTED RESULT : Should return a status otherthan the initial get value"
                print "ACTUAL RESULT : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE"
                print "getRadioAMSDUEnable failed after set"
                tdkTestObj.setResultStatus("FAILURE");

            #Revert back to original Enable status
            methodName = "setRadioAMSDUEnable"
            tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,oldEnable);
            print "details: %s" %details;
            if expectedresult in actualresult :
                print "Enable status reverted back";
                tdkTestObj.setResultStatus("SUCCESS");

            else:
                print "Couldn't revert enable status"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "TEST STEP: Set the Radio AMSDU Enable status"
            print "EXPECTED RESULT : Should return SUCCESS"
            print "ACTUAL RESULT : %s" %details;
            print "TEST EXECUTION RESULT :FAILURE"
            print "setRadioAMSDUEnable failed"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP: Get the initial Radio AMSDU Enable status"
        print "EXPECTED RESULT : Should return either Enabled or Disabled"
        print "ACTUAL RESULT : %s" %details;
        print "TEST EXECUTION RESULT :FAILURE"
        print "getRadioAMSDUEnable failed"
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");


