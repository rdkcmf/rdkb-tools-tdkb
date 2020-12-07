##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_SANITY_QueryLTime</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the LTime gives the time in  HH:MM:SS format</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_45</test_case_id>
    <test_objective>This test case is to check if the LTime gives the time in  HH:MM:SS format</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>LTime</input_parameters>
    <automation_approch>1.Load the sysutil module
2.Query LTime from the DUT
3.Check if the LTime is in HH:MM:SS format
4.Unload the module</automation_approch>
    <expected_output>The Ltime should be in the expected format of HH:MM:SS</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_QueryLTime</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_QueryLTime');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    expectedresult ="SUCCESS";
    command = "LTime";
    print "command:",command;
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip();
    details = details.replace("\\n", "");
    if expectedresult in actualresult and "" != details:
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Query the LTime of the DUT";
       print "EXPECTED RESULT 1:  Should Query the LTime of the DUT";
       print "ACTUAL RESULT 1: " ,details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS"
       if re.match ("(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)" ,details):
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Check if the LTime is in HH:MM:SS format";
          print "EXPECTED RESULT 2 :LTime should be in HH:MM:SS format";
          print "ACTUAL RESULT 2: LTime is in HH:MM:SS format ";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS"
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Check if the LTime is in HH:MM:SS format";
           print "EXPECTED RESULT 2 :LTime should be in HH:MM:SS format";
           print "ACTUAL RESULT 2: LTime is not in HH:MM:SS format ";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Query the LTime of the DUT";
        print "EXPECTED RESULT 1:  Should Query the LTime of the DUT";
        print "ACTUAL RESULT 1: ", details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
