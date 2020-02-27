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
  <name>TS_EPONHAL_GetLlidForwardingState</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetLlidForwardingState</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Using dpoe_getLlidForwardingState get  current traffic state to check if Link state is  true/false and ID is a  number b/w 1 and total number of forwarding state instances.</synopsis>
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
    <test_case_id>TC_EPONHAL_19</test_case_id>
    <test_objective>To check if Link state is  true/false and ID is a  number b/w 1 and total number of forwarding state instances.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_getLlidForwardingState</api_or_interface_used>
    <input_parameters>numEntries</input_parameters>
    <automation_approch>1. Load eponhal module
2. Get the Llid Forwarding state count using dpoe_LlidForwardingStateGetEntryCount
3. Check if the count is greater than  0.
4.Invoke dpoe_getLlidForwardingState using the received numEntries.
5.Check if the values received equals to 1 for true or 0 for false.
6. Unload eponhal module</automation_approch>
    <expected_output>The Forwarding state  retrieved using dpoe_getLlidForwardingState  should be  either 0 for false and  1 for true.</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetLlidForwardingState</test_script>
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
obj.configureTestCase(ip,port,'TS_EPONHAL_GetLlidForwardingState');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
llid = [];
flag = 1;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #prerequisite for the api
    tdkTestObj = obj.createTestStep('EPONHAL_GetParamUlongValue');
    tdkTestObj.addParameter("paramName","LlidForwardingStateGetEntryCount");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    numEntries = " ";
    numEntries = tdkTestObj.getResultDetails();
    numEntries = int(numEntries)
    if expectedresult in actualresult and numEntries != " " and  numEntries >0:
       print "EXPECTED RESULT 1: Should get the Llid Forwarding state  count  value as greater than 0";
       print "ACTUAL RESULT 1: The  Llid Forwarding state  count  is :",numEntries;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj.setResultStatus("SUCCESS");

       #Script to load the configuration file of the component
       tdkTestObj = obj.createTestStep('EPONHAL_GetLlidForwardingState');
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("numEntries",numEntries);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       resultDetails = " ";
       resultDetails = tdkTestObj.getResultDetails();
       if expectedresult in actualresult and resultDetails != " " :

          print "TEST STEP 2: Check for successful invocation of dpoe_getLlidForwardingState";
          print "EXPECTED RESULT 2: Should succesfully invoke dpoe_getLlidForwardingState ";
          print "ACTUAL RESULT 2: successfully invoked dpoe_getLlidForwardingState";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
          tdkTestObj.setResultStatus("SUCCESS");


          #looping to get the Forwarding state's for the links id's from the details
          for i in range(numEntries):
              llid.append(resultDetails.split(':')[i+1].split(',')[0].strip());

          #checking if the value received is 0 or 1
          for j in range(numEntries):
              if (int(llid[j]) == 1) or (int(llid[j]) == 0):
                  pass
              else:
                   flag = 0;

          if flag == 1:
             print "TEST STEP 3: Get the Forwarding state for the corresponding link id's and check if the value corresponds to true or false";
             print "EXPECTED RESULT 3: Should get the Forwarding state for the corresponding link id's and the value must be a true or false";
             print "ACTUAL RESULT 3: The value returned is :" ,resultDetails;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
             tdkTestObj.setResultStatus("SUCCESS");
          else:
              print "TEST STEP 3: Get the Forwarding state for the corresponding link id's and check if the value corresponds to true or false";
              print "EXPECTED RESULT 3: Should get the Forwarding state for the corresponding link id's and the value must be a true or false";
              print "ACTUAL RESULT 3: The value returned is :",resultDetails;
              print "[TEST EXECUTION RESULT] : FAILURE";
              tdkTestObj.setResultStatus("FAILURE");
       else:
           print "TEST STEP 2: Check for successful invocation of dpoe_getLlidForwardingState";
           print "EXPECTED RESULT 2: Should succesfully invoke dpoe_getLlidForwardingState ";
           print "ACTUAL RESULT 2: Failed to  invoke dpoe_getLlidForwardingState";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
           tdkTestObj.setResultStatus("FAILURE");
    else:
        print "EXPECTED RESULT 1: Should get the Llid Forwarding state  count  value as greater than 0";
        print "ACTUAL RESULT 1: The  Llid Forwarding state  count  is :",numEntries;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] :FAILURE";
        tdkTestObj.setResultStatus("FAILURE");


    obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";




