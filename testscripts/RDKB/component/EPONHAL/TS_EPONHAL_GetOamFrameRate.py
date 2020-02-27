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
  <name>TS_EPONHAL_GetOamFrameRate</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetOamFrameRate</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Using dpoe_getOamFrameRate get the  maximum and manimum rate at which OAM PDUs are transmitted and  for each link_id get the maximum-rate and minimum -rate and check if  its greater than or equal to zero</synopsis>
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
    <test_case_id>TC_EPONHAL_20</test_case_id>
    <test_objective>For each  link_id get the , max rate and min rate OAM Frame rate instances. max-rate and min-rate should be greater than or equal to zero </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh scrip</pre_requisite>
    <api_or_interface_used>dpoe_getOamFrameRate</api_or_interface_used>
    <input_parameters>numEntries</input_parameters>
    <automation_approch>1. Load eponhal module
2. Get the Oam Frame Rate Count  using dpoe_OamFrameRateGetEntryCount
3. Check if the count is greater than  0.
4.Invoke dpoe_getOamFrameRate using the received numEntries.
5.Check if the values received are greater than or equal to zero.
6. Unload eponhal module</automation_approch>
    <expected_output> For each of the OAM PDUs  max-rate and min-rate should be greater than or equal to zero </expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetOamFrameRate</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetOamFrameRate');
oam =[];
flag = 1;
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #prerequisite for the api
    tdkTestObj = obj.createTestStep('EPONHAL_GetParamUlongValue');
    tdkTestObj.addParameter("paramName","OamFrameRateGetEntryCount");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    numEntries = " ";
    numEntries = tdkTestObj.getResultDetails();
    numEntries = int(numEntries)
    if expectedresult in actualresult and numEntries != " " and  numEntries >0:
       print "TEST STEP 1: Get the OamFrameRate count";
       print "EXPECTED RESULT 1: Should get the OamFrameRate count  value as greater than 0";
       print "ACTUAL RESULT 1: The OamFrameRate count  is :",numEntries;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj.setResultStatus("SUCCESS");


       #Script to load the configuration file of the component
       tdkTestObj = obj.createTestStep('EPONHAL_GetOamFrameRate');
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("numEntries",numEntries);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       resultDetails = " ";
       resultDetails = tdkTestObj.getResultDetails();
       if expectedresult in actualresult and resultDetails != " ":
          print "TEST STEP 2: Check for successful invocation of dpoe_getOamFrameRate";
          print "EXPECTED RESULT 2: Should successfully invoke dpoe_getOamFrameRate";
          print "ACTUAL RESULT 2: successfully invoked dpoe_getOamFrameRate";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
          tdkTestObj.setResultStatus("SUCCESS");

          #looping to get the max and min rate from the details

          #multiplying numEntries by 2 as each link has two entries
          for i in range(2*numEntries):
              oam.append(resultDetails.split(':')[i+1].split(',')[0].strip());

          #checking if the value received is greater than or equal to 0
          for j in range(numEntries):
             if (int(oam[j]) >= 0):
                flag = 1;
             else:
                 flag = 0;

          if flag == 1:
            print "TEST STEP 3: Get the max and min rate for the corresponding link id's and check if the value is greater than or equal to zero";
            print "EXPECTED RESULT 3: Should get the  max and min rate for the corresponding link id's and the value must be greater than or equal to zero";
            print "ACTUAL RESULT 3: The value returned is :" ,oam;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");
          else:
              print "TEST STEP 3: Get the max and min rate for the corresponding link id's and check if the value is greater than or equal to zero";
              print "EXPECTED RESULT 3: Should get the  max and min rate for the corresponding link id's and the value must be greater than or equal to zero";
              print "ACTUAL RESULT 3: The value returned is :" ,oam;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
              tdkTestObj.setResultStatus("FAILURE");
       else:
           print "TEST STEP 2: Check for successful invocation of dpoe_getOamFrameRate";
           print "EXPECTED RESULT 2: Should successfully invoke of dpoe_getOamFrameRate";
           print "ACTUAL RESULT 2: Failed to  invoke dpoe_getOamFrameRate";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
           tdkTestObj.setResultStatus("FAILURE");
    else:
       print "TEST STEP 1: Get the OamFrameRate count";
       print "EXPECTED RESULT 1: Should get the OamFrameRate count  value as greater than 0";
       print "ACTUAL RESULT 1: The OamFrameRate count  is :",numEntries;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : FAILURE";
       tdkTestObj.setResultStatus("FAILURE");


    obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";





