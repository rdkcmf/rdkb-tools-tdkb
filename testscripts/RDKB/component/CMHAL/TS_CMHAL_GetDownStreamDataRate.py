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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_CMHAL_GetDownStreamDataRate</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the downstream Data rate and check whether it is in the valid/allowable range.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_CMHAL_17</test_case_id>
    <test_objective>To get the downstream Data rate and check whether it is from the valid/allowable range.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetDOCSISInfo</api_or_interface_used>
    <input_parameters>paramName : "DS_DataRate"</input_parameters>
    <automation_approch>1. Load  cmhal module
2. From script invoke CMHAL_GetParamCharValue() 
3. Get the Downstream data rate
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>The downstream data rate should be within valid/allowable range</except_output>
    <priority>High</priority>
    <test_stub_interface>CosaCM</test_stub_interface>
    <test_script>TS_CMHAL_GetDownStreamDataRate</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_CMHAL_GetDownStreamDataRate');
obj1.configureTestCase(ip,port,'TS_CMHAL_GetDownStreamDataRate');

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    DownStreamDataRateRange = "sh %s/tdk_utility.sh parseConfigFile DS_DATARATE_RANGE" %TDK_PATH;
    
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", DownStreamDataRateRange);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    DownStreamDataRateRange = tdkTestObj.getResultDetails().strip();
    DownStreamDataRateRange = DownStreamDataRateRange.replace("\\n", "");
    if DownStreamDataRateRange and expectedresult in actualresult:
        DownStreamDataRateRange_list = DownStreamDataRateRange.replace("Mbps", "").split("-");
        DownStreamDataRateRange_lower = DownStreamDataRateRange_list[0];
        DownStreamDataRateRange_upper = DownStreamDataRateRange_list[1];
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 : Get the range of Downstream DateRate";
        print "EXPECTED RESULT 1 : Should get the range of Downstream DateRate";
        print "ACTUAL RESULT 1 : Got the range of Downstream DateRate as %s" %DownStreamDataRateRange;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
        tdkTestObj.addParameter("paramName","DS_DataRate");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        dataRate = tdkTestObj.getResultDetails();
        dataRate = dataRate.split(" ")[0];

        #convert dataRate from bps to mbps
        dataRate = float(dataRate)/1000000;

        if expectedresult in actualresult and float(DownStreamDataRateRange_lower) <= dataRate <= float(DownStreamDataRateRange_upper):
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Downstream data rate in the allowable range";
            print "EXPECTED RESULT 2: Should get the Downstream datarate in the allowable range successfully";
            print "ACTUAL RESULT 2: Downstream data rate is ",dataRate,"Mbps is in the allowable range";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Downstream data rate in the allowable range";
            print "EXPECTED RESULT 2: Should get the Downstream data rate in the allowable range successfully";
            print "ACTUAL RESULT 2: Downstream data rate is ",dataRate,"Mbps not in the allowable range";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 : Get the range of allowable Downstream DateRate";
        print "EXPECTED RESULT 1 : Should get the range of allowable Downstream DateRate";
        print "ACTUAL RESULT 1 : Failed to get the allowable range of Downstream DateRate";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        
    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
