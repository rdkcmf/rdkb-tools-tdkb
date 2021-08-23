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
  <version>6</version>
  <name>TS_TelcoVoiceMgrHal_GetLineStats</name>
  <primitive_test_id/>
  <primitive_test_name>TELCOVOICEMgrHal_GetLineStats</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the statistics of Telco Voice Line using the parameter Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Stats.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_TELCOVOICEMGRHAL_02</test_case_id>
    <test_objective>To get the statistics of Telco Voice Line using the parameter Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Stats.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>json_hal_client_init
json_hal_client_run
json_hal_is_client_connected
json_hal_client_send_and_get_reply json_hal_add_param
json_hal_get_param</api_or_interface_used>
    <input_parameters>paramName : Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Stats.</input_parameters>
    <automation_approch>1. Load the Telco Voice HAL Module
2. Invoke the json_hal_client_init() JSON HAL API to initiate the connection to JSON HAL server with TELCO VOICE HAL Schema file
3. Invoke the json_hal_client_run() JSON HAL API to start the JSON HAL client service.
4. Invoke the json_hal_is_client_connected() to check whether JSON HAL client is connected to JSON HAL server or not
5. Return True if json hal client is connected to json hal server else failure
6. Invoke the json_hal_add_param with the parameter name "Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Stats."
7. Invoke the json_hal_client_send_and_get_reply API to send the request to JSON HAL server
8. Invoke the json_hal_get_param API to get the value of the parameter
9. Return the parameter values in the structure only if above API's are success else failure.
10. Unload the Telco Voice HAL Module</automation_approch>
    <expected_output>Should be able to successfully retrieve the Voice Statistics.</expected_output>
    <priority>High</priority>
    <test_stub_interface>telcovoicemgrhal</test_stub_interface>
    <test_script>TS_TelcoVoiceMgrHal_GetLineStats</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("telcovoicemgrhal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TelcoVoiceMgrHal_GetLineStats');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TELCOVOICEMgrHal_Init');
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate the TELCOVOICEMgrHal_Init operation";
        print "EXPECTED RESULT 1: TELCOVOICEMgrHal_Init Should be success";
        print "ACTUAL RESULT 1: TELCOVOICEMgrHal_Init was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        tdkTestObj = obj.createTestStep('TELCOVOICEMgrHal_GetLineStats');
        tdkTestObj.addParameter("paramName","Device.Services.VoiceService.1.VoiceProfile.1.Line.1.Stats.");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        line_stats = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Line Stats";
            print "EXPECTED RESULT 2: GetLineStats operation should be success ";
            print "ACTUAL RESULT 2: GetLineStats operation was success , Line Stats is: ",line_stats;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Line Stats";
            print "EXPECTED RESULT 2: GetLineStats operation should be success ";
            print "ACTUAL RESULT 2: GetLineStats operation was Failed ";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate the TELCOVOICEMgrHal_Init operation";
        print "EXPECTED RESULT 1: TELCOVOICEMgrHal_Init Should be Success";
        print "ACTUAL RESULT 1: TELCOVOICEMgrHal_Init was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    obj.unloadModule("telcovoicemgrhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
