##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_SANITY_CheckFor4PhpInstances</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if 4 php.ini processes are running in the DUT</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_52</test_case_id>
    <test_objective>To check if 4 php.ini processes are running in the DUT.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband </test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.check if 4 php.ini processes are running in DUT
3. Mark the script as Success in case there 4 processes else mark the script as failiure
4.unload the module</automation_approch>
    <expected_output>4 php.ini processes are expected to be up and running</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckFor4PhpInstances</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckFor4PhpInstances');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
   #Set the result status of execution
   obj.setLoadModuleStatus("SUCCESS");

   query="ps | grep -i \"php.ini\" | grep -v \"grep\" | wc -l";
   print "query:%s" %query
   tdkTestObj = obj.createTestStep('ExecuteCmd');
   tdkTestObj.addParameter("command", query)
   expectedresult="SUCCESS";
   tdkTestObj.executeTestCase(expectedresult);
   actualresult = tdkTestObj.getResult();
   details = tdkTestObj.getResultDetails().strip().replace("\\n","");
   if expectedresult in actualresult and details =="":
      tdkTestObj.setResultStatus("FAILURE");
      print "TEST STEP 1 : Check if php.ini has 4 instances running";
      print "EXPECTED RESULT 1 : 4 instances of php.ini should be running";
      print "ACTUAL RESULT 1 :Search Result :%s "%details;
      print "[TEST EXECUTION RESULT] : FAILURE";
   else:
       if int(details) == 4:
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 1 : Check if php.ini has 4 instances running";
          print "EXPECTED RESULT 1 : 4 instances of php.ini should be running";
          print "ACTUAL RESULT 1 :Search Result :%s "%details;
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 1 : Check if php.ini has 4 instances running";
           print "EXPECTED RESULT 1 : 4 instances of php.ini should be running";
           print "ACTUAL RESULT 1 :Search Result :%s "%details;
           print "[TEST EXECUTION RESULT] : FAILURE";
   obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
