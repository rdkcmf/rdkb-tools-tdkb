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
  <version>4</version>
  <name>TS_CMHAL_GetUpStreamDataRate</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the upstream data rate and check whether it is in the valid/allowable range.</synopsis>
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
    <test_case_id>TC_CMHAL_39</test_case_id>
    <test_objective>To get the upstream data rate and check whether it is in the valid/allowable range.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetDOCSISInfo</api_or_interface_used>
    <input_parameters>paramName : "US_DataRate"</input_parameters>
    <automation_approch>1. Load  cmhal module
2. From script invoke CMHAL_GetParamCharValue() 
3. Get the Upstream data rate
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>The upstream data rate should be within the valid/allowable range.</except_output>
    <priority>High</priority>
    <test_stub_interface>CosaCM</test_stub_interface>
    <test_script>TS_CMHAL_GetUpStreamDataRate</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetUpStreamDataRate');
obj1.configureTestCase(ip,port,'TS_CMHAL_GetUpStreamDataRate');

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    UpStreamDataRateRange = "sh %s/tdk_utility.sh parseConfigFile US_DATARATE_RANGE" %TDK_PATH;
    
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", UpStreamDataRateRange);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    UpStreamDataRateRange = tdkTestObj.getResultDetails().strip();
    UpStreamDataRateRange = UpStreamDataRateRange.replace("\\n", "");
    if UpStreamDataRateRange and expectedresult in actualresult :
        UpStreamDataRateRange_list = UpStreamDataRateRange.replace("Mbps", "").split("-");
        UpStreamDataRateRange_lower = UpStreamDataRateRange_list[0];
        UpStreamDataRateRange_upper = UpStreamDataRateRange_list[1];
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 : Get the range of Upstream DateRate";
        print "EXPECTED RESULT 1 : Should get the range of Upstream DateRate";
        print "ACTUAL RESULT 1 : Got the range of Upstream DateRate as %s" %UpStreamDataRateRange;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
        tdkTestObj.addParameter("paramName","US_DataRate");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        dataRate = tdkTestObj.getResultDetails();
        dataRate = dataRate.split(" ")[0];

        #convert dataRate from bps to mbps
        dataRate = float(dataRate)/1000000;

        if expectedresult in actualresult and float(UpStreamDataRateRange_lower) <= dataRate <= float(UpStreamDataRateRange_upper):
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Upstream data rate in the allowable range";
            print "EXPECTED RESULT 2: Should get the Upstream datarate in the allowable range successfully";
            print "ACTUAL RESULT 2: Upstream data rate is ",dataRate,"Mbps is in the allowable range";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Upstream data rate in the allowable range";
            print "EXPECTED RESULT 2: Should get the Upstream data rate in the allowable range successfully";
            print "ACTUAL RESULT 2: Upstream data rate is ",dataRate,"Mbps not in the allowable range";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 : Get the range of allowable Upstream DateRate";
        print "EXPECTED RESULT 1 : Should get the range of allowable Upstream DateRate";
        print "ACTUAL RESULT 1 : Failed to get the allowable range of Upstream DateRate";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        
    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
