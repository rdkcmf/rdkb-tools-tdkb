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
  <version>10</version>
  <name>TS_CMAGENT_CMStatus</name>
  <primitive_test_id/>
  <primitive_test_name>CMAgent_Get</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>TC_CMAGENT_16 - To Validate "CMStatus" Function Parameter and to check whether DOCSISUpstreamRanging is Complete</synopsis>
  <groups_id>4</groups_id>
  <execution_time>2</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_CMAGENT_12</test_case_id>
    <test_objective>To Validate "CMStatus" Function Parameter and  to check whether DOCSISUpstreamRanging is Complete</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
CMAgent_Get
Input
1.PathName ("paramName")
( eg: "Device.X_CISCO_COM_CableModem.CMStatus","Device.X_CISCO_COM_CableModem.DOCSISUpstreamRanging")</input_parameters>
    <automation_approch>1.1.Load the cmagent module
2.From script invoke CMAgent_Get to get the CMStatus and check if it returns OPERATIONAL
3.If it returns true, get the value of DOCSISUpstreamRanging
4.Response(s)(printf) from TDK Component,Ccsp Library function and cmagentstub would be logged in Agent Console log based on the debug info redirected to agent console.
5.cmagentstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result ("Values for Requested Param" ) and the same is updated to agent console log.
6.TestManager will publish the result in GUI as PASS/FAILURE based on the response from cmagentstub.</automation_approch>
    <except_output>CheckPoint 1:
TDK agent Test Function will log the test case result as PASS based on API response
CheckPoint 2:
TestManager GUI will publish the result as PASS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_CMAGENT_CMStatus</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMAGENT_CMStatus');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

loadStatusExpected = "SUCCESS"

if loadStatusExpected not in loadModuleresult.upper():
    print "[Failed To Load CM Agent Stub from env TDK Path]"
    print "[Exiting the Script]"
    exit();
		
#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CMAgent_Get');

#Input Parameters
tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_CableModem.CMStatus");

expectedresult = "SUCCESS";

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "[TEST EXECUTION RESULT] : %s" %actualresult ;

Details_cmstatus = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
    #Set the result status of execution as success
    tdkTestObj.setResultStatus("SUCCESS");
    print "TEST STEP 1: Get the CMStatus";
    print "EXPECTED RESULT 1: Should get value of CMStatus ";
    print "ACTUAL RESULT 1: %s" %Details_cmstatus;
    #Get the result of execution
    print "[TEST EXECUTION RESULT] : SUCCESS";

    #Primitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('CMAgent_Get');
    #Input Parameters
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_CableModem.DOCSISUpstreamRanging");
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);

    #Get the result of execution
    actualresult = tdkTestObj.getResult();
    #print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    Details = tdkTestObj.getResultDetails();
	
    if  expectedresult in actualresult and "OPERATIONAL" in Details_cmstatus  and "Complete" in Details:
        #Set the result status of execution as success
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 2: Get the DOCSISUpstreamRanging as complete";
    	print "EXPECTED RESULT 2: Should get the DOCSISUpstreamRanging as complete";
    	print "ACTUAL RESULT 2: %s" %Details;
    	#Get the result of execution
    	print "[TEST EXECUTION RESULT] : SUCCESS";
	    

    else:
        #Set the result status of execution as failure
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 2: Get the DOCSISUpstreamRanging as complete";
        print "EXPECTED RESULT 2: Should get the DOCSISUpstreamRanging as complete";
        print "ACTUAL RESULT 2: %s" %Details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";


else:
    #Set the result status of execution as failure
    tdkTestObj.setResultStatus("FAILURE");
    print "TEST STEP 1: Get the CMStatus";
    print "EXPECTED RESULT 1: Should get value of CMStatus ";
    print "ACTUAL RESULT 1: %s" %Details_cmstatus;
    #Get the result of execution
    print "[TEST EXECUTION RESULT] : FAILURE";

print "[TEST EXECUTION RESULT] : %s" %Details_cmstatus ;

obj.unloadModule("cmagent");
