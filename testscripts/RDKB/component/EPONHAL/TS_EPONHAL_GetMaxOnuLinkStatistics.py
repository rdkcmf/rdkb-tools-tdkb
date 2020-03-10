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
  <version>4</version>
  <name>TS_EPONHAL_GetMaxOnuLinkStatistics</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetOnuLinkStatistics</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Using dpoe_getOnuStatistics get the list of all LLID port traffic statistics and check if the values retrieved are greater than or equal to zero</synopsis>
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
    <test_case_id>TC_EPONHAL_24</test_case_id>
    <test_objective>Giving  the maximum numentries using dpoe_getMaxLogicalLinks and check if the values retrieved are greater than or equal to zero</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_getOnuLinkStatistics</api_or_interface_used>
    <input_parameters>numEntries</input_parameters>
    <automation_approch>1. Load eponhal module
2.Invoke dpoe_getOnuLinkStatistics using the dpoe_getMaxLogicalLinks number of  numEntries.
3.Check if the values received are greater than or equal to zero.
4. Unload eponhal module</automation_approch>
    <expected_output>Received list of all LLID port traffic statistics after the succesful call should be greater than or equal to zero.</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetMaxOnuLinkStatistics</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;
import re;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetMaxOnuLinkStatistics');
maxonu = [];
flag = 1;
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep('EPONHAL_GetOnuLinkStatistics');
        expectedresult="SUCCESS";
        #passing a dummy value as the numEntries is derived from dpoe_getMaxLogicalLinks
        tdkTestObj.addParameter("numEntries",500);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        resultDetails = " ";
        resultDetails = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 1: check for successful  invocation of dpoe_getMaxLogicalLinks";
           print "EXPECTED RESULT 1: Should successfully invoke dpoe_getMaxLogicalLinks";
           print "ACTUAL RESULT 1: Succesfully invoke dpoe_getMaxLogicalLinks";
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
           #no of entries in the structure
           n =23;
           for i in range(n):
               maxonu.append(resultDetails.split(':')[i+2].split(',')[0].strip())
           print "maxonu :",maxonu;
           #checking if the value received is greater than 0
           for j in range(n):
               if int(maxonu[j]) >=0:
                  pass
               else:
                   flag = 0;
           if flag == 1:
              print "TEST STEP 2: check if the value received is greater than or equal to 0";
              print "EXPECTED RESULT 2: The value received must be greater than or equal to 0";
              print "ACTUAL RESULT 2: The values received are:",resultDetails;
              tdkTestObj.setResultStatus("SUCCESS");
              print "[TEST EXECUTION RESULT] : SUCCESS";

           else:
               print "TEST STEP 2: check if the value received is greater than or equal to 0";
               print "EXPECTED RESULT 2: The value received must be greater than or equal to 0";
               print "ACTUAL RESULT 2: The values received are:",resultDetails;
               tdkTestObj.setResultStatus("FAILURE");
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "TEST STEP 1: check for successful  invocation of dpoe_getOnuLinkStatistics";
            print "EXPECTED RESULT 1: Should successfully invoke dpoe_getOnuLinkStatistics";
            print "ACTUAL RESULT 1: Failed to  invoke dpoe_getOnuLinkStatistics";
            print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj.setResultStatus("FAILURE");

        obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";





