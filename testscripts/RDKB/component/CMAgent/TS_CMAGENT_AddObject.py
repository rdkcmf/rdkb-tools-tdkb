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
  <version>7</version>
  <name>TS_CMAGENT_AddObject</name>
  <primitive_test_id/>
  <primitive_test_name>CMAgent_AddObject</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>TC_CMAGENT_2 - Add Object API Validation for read only Parameter</synopsis>
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
    <test_case_id>TC_CMAGENT_2</test_case_id>
    <test_objective>To Validate 
"Add Tbl Row" Function</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component"
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
CMAgent_AddObject
Input
1.Parameter Path (paramName as Device.X_CISCO_COM_CableModem.UpstreamChannel)</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(CMAgent_AddObject  - func name - "If not exists already"
 cmagent - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_CMAGENT_AddObject.py)
3.Execute the generated Script(TS_CMAGENT_AddObject.py) using excution page of  Test Manager GUI
4.cmagentstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named CMAgent_AddObject through registered TDK cmagentstub function along with necessary Entry Values as arguments
5.CMAgent_AddObject function will call CCSP Base Interface Function named CcspBaseIf_AddTblRow, that inturn will call "CcspCcMbi_AddTblRow" along with  provided input arguments to add Table row info to Dynamic Table List of CM Agent
6.Responses(printf) from TDK Component,Ccsp Library function and cmagentstub would be logged in Agent Console log based on the debug info redirected to agent console   
7.cmagentstub will validate the available result (from agent console log and Pointer to instance as non null ) with expected result (Eg:"Table added Succesfully") and the same is updated in agent console log
8.TestManager will publish the result in GUI as PASS/FAILURE based on the response from cmagentstub</automation_approch>
    <except_output>CheckPoint 1:
Table Instance Added log from DUT should be available in Agent Console Log
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response 
CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_CMAGENT_AddObject</test_script>
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
obj.configureTestCase(ip,port,'TS_CMAGENT_AddObject');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

loadStatusExpected = "SUCCESS"

if loadStatusExpected not in loadModuleresult.upper():
        print "[Failed To Load CM Agent Stub from from env TDK_PATH]"
        print "[Exiting the Script]"
        exit();

#Prmitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CMAgent_AddObject');

#Input Parameters
tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_CableModem.UpstreamChannel");

expectedresult = "FAILURE";

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);


#Get the result of execution
actualresult = tdkTestObj.getResult();
print "[TEST EXECUTION RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
	print "Cannot add a row to a READONLY table object"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
	print "Added a row to a READONLY table object"	

print "[TEST EXECUTION RESULT] : %s" %resultDetails ;

obj.unloadModule("cmagent");
