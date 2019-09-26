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
  <version>1</version>
  <name>TS_CMHAL_US_OFDM_GetSymbolsPerFrame</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetUsOfdmChanTable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get Number of SymbolsPerFrame for upstream. The number of symboles per frame should be in the range of [18,36] for 2K FFT mode and [9,18] for 4K FFT mode.</synopsis>
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
    <test_case_id>TC_CMHAL_72</test_case_id>
    <test_objective>Get Number of SymbolsPerFrame for upstream. The number of symboles per frame should be in the range of [18,36] for 2K FFT mode and [9,18] for 4K FFT mode.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetUsOfdmaChanTable</api_or_interface_used>
    <input_parameters>paramNme : "US_OFDM_NumSymbolsPerFrame"</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Invoke docsis_GetUsOfdmaChanTable to get the number of symbols per frame
3. Validate the value
4. Unload cmhal module</automation_approch>
    <except_output>The number of symboles per frame should be in the range of [18,36] for 2K FFT mode and [9,18] for 4K FFT mode.</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_US_OFDM_GetSymbolsPerFrame</test_script>
    <skipped>No</skipped>
    <release_version>M67</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_US_OFDM_GetSymbolsPerFrame');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetUsOfdmChanTable");
    tdkTestObj.addParameter("paramName","US_OFDM_NumSymbolsPerFrame");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print details;

    if expectedresult in actualresult:
	NoOfEntries = details.split(";")[0].split(":")[1];
        if int(NoOfEntries) > 0:
	    #min and max number of symbols per frame for 2K FFT mode
 	    minValue_2K = 18;
	    maxValue_2K = 36;
	    #min and max number of symbols per frame for 4K FFT mode
 	    minValue_4K = 9;
	    maxValue_4K = 18;
	    NoOfSymbols = details.split(";")[1].split(":")[1];
	    if minValue_2K <= NoOfSymbols <= maxValue_2K or minValue_4K <= NoOfSymbols <= maxValue_4K:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Get the number of symbols per frame";
                print "EXPECTED RESULT 1: Should get the number of symbols per frame in the expected range";
                print "ACTUAL RESULT 1: NoOfSymbols is %s" %NoOfSymbols;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
	        #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1: Get the number of symbols per frame";
                print "EXPECTED RESULT 1: Should get the number of symbols per frame in the expected range";
                print "ACTUAL RESULT 1: NoOfSymbols is %s" %NoOfSymbols;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "There are no entries in US OFDM channel table"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
	print "Failed to get the values from api";
    obj.unloadModule("cmhal");

else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
