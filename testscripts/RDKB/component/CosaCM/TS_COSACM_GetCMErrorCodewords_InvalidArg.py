##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_COSACM_GetCMErrorCodewords_InvalidArg</name>
  <primitive_test_id/>
  <primitive_test_name>COSACM_GetCMErrorCodewords_InvalidArg</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test case to validate CosaDmlCmGetCMErrorCodewords API with invalid parameters</synopsis>
  <groups_id>4</groups_id>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_COSACM_46</test_case_id>
    <test_objective>To Validate Cable Modem 
"CosaDmlCmGetCMErrorCodewords" API under Negative scenario</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator, XB3</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
COSACM_GetCMErrorCodewords_InvalidArg
Input
N/A</input_parameters>
    <automation_approch>"1.Configure the Function info in Test Manager GUI  which needs to be tested  
(COSACM_GetCMErrorCodewords_InvalidArg - func name - ""If not exists already"" ( This is considered as default Primitive test case)
 cosacm - module name
 Necessary I/P args if needed as Mentioned in Input)
2.Create a Python Script in Test Manager with default primitive test case through add new rdkb script option (TS_CosaCM_GetCMErrorCodewords_InvalidArg.py)
3.Customize the generated script template to handle load/unload and pass/fail scenarios
3.Execute the generated Script(TS_CosaCM_GetCMErrorCodewords_InvalidArg.py) using execution page of  Test Manager GUI
4.cosacmstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named COSACM_GetCMErrorCodewords_InvalidArg through registered TDK cosacmstub function along with necessary Entry Values as arguments
5.COSACM_GetCMErrorCodewords_InvalidArg function will call ssp_cosacm_getcmrrrorcodewords_invalid_arg with improper input argument say unallocated memory pointer,that inturn will call relevant cm hal Function to get/fetch CM data model value. In prior ssp_cosacm_create and ssp_coscm_initialize functions are called in sequence to allocate memory for CM datamodel and initialize with default values
6.Responses(printf) from TDK Component,Ccsp Library function and cosacmstub would be logged in Agent Console log based on the debug info redirected to agent console   
7.cosacmstub function COSACM_GetCMErrorCodewords_InvalidArg will validate the available result (return value from ssp_cosacm_getcmrrrorcodewords_invalid_arg as failure) with expected result (failure) and the output value is updated in agent console log and json output variable
8.TestManager will publish the result in GUI as PASS/FAILURE based on the response from COSACM_GetCMErrorCodewords_InvalidArg  function"</automation_approch>
    <except_output>"CheckPoint 1:
Cosa CM Get Error Code Words failure log from DUT should be available in Agent Console Log without any crash
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response which will be available in Test Manager Result ( XLS)
CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager"</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_COSACM_GetCMErrorCodewords_InvalidArg</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cosacm","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_COSACM_GetCMErrorCodewords_InvalidArg');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("COSACM_GetCMErrorCodewords_InvalidArg");
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details = tdkTestObj.getResultDetails();
            print "EXPECTED RESULT 1: Should return Error Status with respective Error code";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS" ; 
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "EXPECTED RESULT 1: Should return Error Status with respective Error code";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE" ;              
            
        obj.unloadModule("cosacm");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
