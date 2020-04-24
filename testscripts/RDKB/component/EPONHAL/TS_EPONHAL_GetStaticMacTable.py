#########################################################################
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
  <version>1</version>
  <name>TS_EPONHAL_GetStaticMacTable</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetStaticMacTable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Using dpoe_getStaticMacTable get the static  mac and for each entries check if  the MAC address is valid .</synopsis>
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
    <test_case_id>TC_EPONHAL_25</test_case_id>
    <test_objective>Get the no of Static  Mac Table  entry.For each entries check if  the MAC address is valid </test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_getStaticMacTable</api_or_interface_used>
    <input_parameters>numentries</input_parameters>
    <automation_approch>1. Load eponhal module
2. Get the no of Dynamic Mac Table  entry.using Device.DPoE.DPoE_StaticMacTableNumberOfEntries
3. Check if the count is greater than  0.
4.Invoke dpoe_getStaticMacTable using the received numEntries.
5.Check if the mac  received is valid one .
6. Unload eponhal module</automation_approch>
    <expected_output>Each of the dynamically learned MAC address should have a valid mac address.</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetStaticMacTable</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetStaticMacTable');
tr181obj.configureTestCase(ip,port,'TS_EPONHAL_GetStaticMacTable');
#Get the result of connection with test component and DUT
mac =[];
flag =1;
loadmodulestatus =obj.getLoadModuleResult();
tr181loadmodulestatus =tr181obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %tr181loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS")
    #prerequisite for the api
    tdkTestObj = tr181obj.createTestStep("TDKB_TR181Stub_Get");
    tdkTestObj.addParameter("ParamName","Device.DPoE.DPoE_StaticMacTableNumberOfEntries");
    expectedresult ="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    numEntries = " ";
    numEntries = tdkTestObj.getResultDetails();
    numEntries = int(numEntries)
    if expectedresult in actualresult and numEntries != " " and  numEntries >0:
       print "TEST STEP 1: Get the Number of entries for StaticMacTable";
       print "EXPECTED RESULT 1: Should get the StaticMacTable  value as greater than 0";
       print "ACTUAL RESULT 1: The StaticMacTable value  is :",numEntries;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj.setResultStatus("SUCCESS");

       #Script to load the configuration file of the component
       tdkTestObj = obj.createTestStep('EPONHAL_GetStaticMacTable');
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("numEntries",numEntries);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       resultDetails = " ";
       resultDetails = tdkTestObj.getResultDetails();

       if expectedresult in actualresult and resultDetails != " ":
          print "TEST STEP 2: Check for successful invocation of dpoe_getStaticMacTable";
          print "EXPECTED RESULT 2: Should succesfully invoke dpoe_getStaticMacTable";
          print "ACTUAL RESULT 2:Sucessfully invoked  dpoe_getStaticMacTable";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
          tdkTestObj.setResultStatus("SUCCESS");

          #looping to get the MAC  from the details
          for i in range(numEntries):
              mac.append(resultDetails.split(':')[i+1].split(',')[0].strip());
          #checking if the value received is a valid mac
          for j in range(numEntries):
              if re.match("[0-9a-f]{2}([-: ])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$",mac[j].lower()) :
                 pass
              else:
                   flag = 0;

          if expectedresult in actualresult  and flag == 1:
             print "TEST STEP 3: Check if the received MAC is valid";
             print "EXPECTED RESULT 3: Should receive a valid MAC";
             print "ACTUAL RESULT 3: value returned is :",mac;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS"
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
          else:
              print "TEST STEP 3: Check if the received MAC is valid";
              print "EXPECTED RESULT 3: Should receive a valid MAC";
              print "ACTUAL RESULT 3: value returned is :",mac;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE"
              tdkTestObj.setResultStatus("FAILURE");
       else:
          print "TEST STEP 2: Check for successful invocation of dpoe_getStaticMacTable";
          print "EXPECTED RESULT 2: Should succesfully invoke dpoe_getStaticMacTable";
          print "ACTUAL RESULT 2: Failed to invoke dpoe_getStaticMacTable";
          #Get the result of execution
          print "[TEST EXECUTION RESULT] :FAILURE";
          tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1: Get the Number of entries for StaticMacTable";
        print "EXPECTED RESULT 1: Should get the StaticMacTable  value as greater than 0";
        print "ACTUAL RESULT 1: The StaicMacTable value  is :",numEntries;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] :FAILURE";
        tdkTestObj.setResultStatus("FAILURE");


    obj.unloadModule("eponhal");
    tr181obj.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

