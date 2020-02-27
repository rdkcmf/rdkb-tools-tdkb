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
  <name>TS_EPONHAL_GetOnuPacketBufferCapabilities</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetOnuPacketBufferCapabilities</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis> Using dpoe_getOnuPacketBufferCapabilities get the packet buffer capabilities and  check if the  structure value received after a successful call has a value greater than zero.</synopsis>
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
    <test_case_id>TC_EPONHAL_22</test_case_id>
    <test_objective>Check if the  structure value received after a successful call has a value greater than zero.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_getOnuPacketBufferCapabilities</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load eponhal module
2.Invoke dpoe_getOnuPacketBufferCapabilities
3.Check if the values received are greater than zero
4. Unload eponhal module</automation_approch>
    <expected_output>Check if the  packet buffer capabilities from structure after the successful call are be greater than zero</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetOnuPacketBufferCapabilities</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetOnuPacketBufferCapabilities');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep('EPONHAL_GetOnuPacketBufferCapabilities');
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    resultDetails = " ";
    resultDetails = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and resultDetails != " " :
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Invoke dpoe_getOnuPacketBufferCapabilities";
       print "EXPECTED RESULT 1: Should invoke dpoe_getOnuPacketBufferCapabilities";
       print "ACTUAL RESULT 1: Succesfully invoked dpoe_getOnuPacketBufferCapabilities";
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       UpstreamQueues = resultDetails.split(':')[2].split(',')[0].strip()
       print"UpstreamQueues:",UpstreamQueues
       UpQueuesMaxPerLink = resultDetails.split(':')[3].split(',')[0].strip()
       print"UpQueuesMaxPerLink:",UpQueuesMaxPerLink
       UpQueueIncrement = resultDetails.split(':')[4].split(',')[0].strip()
       print"UpQueueIncrement:",UpQueueIncrement
       DownstreamQueues = resultDetails.split(':')[5].split(',')[0].strip()
       print"DownstreamQueues: ",DownstreamQueues
       DnQueuesMaxPerPort = resultDetails.split(':')[6].split(',')[0].strip()
       print"DnQueuesMaxPerPort:",DnQueuesMaxPerPort
       DnQueueIncrement =  resultDetails.split(':')[7].split(',')[0].strip()
       print"DnQueueIncrement:",DnQueueIncrement
       TotalPacketBuffer = resultDetails.split(':')[8].split(',')[0].strip()
       print "TotalPacketBuffer:",TotalPacketBuffer
       UpPacketBuffer = resultDetails.split(':')[9].split(',')[0].strip()
       print"UpPacketBuffer:",UpPacketBuffer
       if int(UpQueuesMaxPerLink)  > 0 and int(UpQueueIncrement) > 0 and int(DownstreamQueues) > 0 and int(DnQueuesMaxPerPort) > 0 and int(DnQueueIncrement) > 0 and int(TotalPacketBuffer) > 0 and int(UpPacketBuffer)  > 0 :
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 1: The values returned by dpoe_getOnuPacketBufferCapabilities should be greater than zer0";
          print "EXPECTED RESULT 1: Should get the  values returned by dpoe_getOnuPacketBufferCapabilities greater tha zer0";
          print "ACTUAL RESULT 1:The received values are : %s "%resultDetails;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 1: The values returned by dpoe_getOnuPacketBufferCapabilities should be greater than zer0";
           print "EXPECTED RESULT 1: Should get the  values returned by dpoe_getOnuPacketBufferCapabilities greater tha zer0";
           print "ACTUAL RESULT 1:The received values are : %s "%resultDetails;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        print "TEST STEP 1: Invoke dpoe_getOnuPacketBufferCapabilities";
        print "EXPECTED RESULT 1: Should invoke dpoe_getOnuPacketBufferCapabilities";
        print "ACTUAL RESULT 1: Succesfully invoked dpoe_getOnuPacketBufferCapabilities";
        tdkTestObj.setResultStatus("FAILURE");
        print "[TEST EXECUTION RESULT] : FAILURE";


    obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";




