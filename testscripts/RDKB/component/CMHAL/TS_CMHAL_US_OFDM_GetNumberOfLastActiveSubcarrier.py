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
  <name>TS_CMHAL_US_OFDM_GetNumberOfLastActiveSubcarrier</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetUsOfdmChanTable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the number of the last non-excluded subcarrier. The valid range is 74 to 3947</synopsis>
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
    <test_case_id>TC_CMHAL_70</test_case_id>
    <test_objective>Get the number of the last non-excluded subcarrier. The valid range is 74 to 3947</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetUsOfdmaChanTable</api_or_interface_used>
    <input_parameters>paramName : "US_OFDM_LastActiveSubcarrierNum"</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Invoke docsis_GetUsOfdmaChanTable to get the number of last active subcarriers
3. Validate the value
4. Unload cmhal module</automation_approch>
    <except_output>The number of last active subcarriers must be in range of  74 to 3947</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_US_OFDM_GetNumberOfLastActiveSubcarrier</test_script>
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
obj.configureTestCase(ip,port,'TS_CMHAL_US_OFDM_GetNumberOfLastActiveSubcarrier');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetUsOfdmChanTable");
    tdkTestObj.addParameter("paramName","US_OFDM_LastActiveSubcarrierNum");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print details;
    if expectedresult in actualresult:
	NoOfEntries = details.split(";")[0].split(":")[1];
        if int(NoOfEntries) > 0:
 	    minValue = 74;
	    maxValue = 3947;
	    ActiveSubcarrier = details.split(";")[1].split(":")[1];
    	    if minValue <= int(ActiveSubcarrier) <= maxValue:
    	        #Set the result status of execution
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        print "TEST STEP 1: Get the ActiveSubcarrier";
    	        print "EXPECTED RESULT 1: Should get the ActiveSubcarrier in the expected range";
    	        print "ACTUAL RESULT 1: ActiveSubcarrier is %s and is in the range of [%d,%d]" %(ActiveSubcarrier,minValue,maxValue);
    	        #Get the result of execution
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
    	    else:
    	        tdkTestObj.setResultStatus("FAILURE");
    	        print "TEST STEP 1: Get the ActiveSubcarrier";
    	        print "EXPECTED RESULT 1: Should get the ActiveSubcarrier in the expected range";
    	        print "ACTUAL RESULT 1: ActiveSubcarrier is %s and is not in the range of [%d,%d]" %(ActiveSubcarrier,minValue,maxValue);
    	        print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "There are no entries in US OFDM channel table"
    else:
	tdkTestObj.setResultStatus("FAILURE");
	print "Failed to get the value of LastActiveSubcarrier"
    obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
