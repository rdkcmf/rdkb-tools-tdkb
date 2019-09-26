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
  <version>2</version>
  <name>TS_WIFIAGENT_SetAttributes</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_SetAttr</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set Attributes API Validation</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Emulator</box_type>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_7</test_case_id>
    <test_objective>To Validate Set Param Attribute Function for WIFI Agent</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
WIFIAgent_SetAttr
Input
1.paramname ( eg: "Device.WiFi.SSIDNumberOfEntries" )
2.Notification type 
(eg:"notification" as passive) 
(eg:pasive)
3.Access Control Change type 
(eg:"accessControlChanged" as anybody)</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(WIFIAgent_SetAttr  - func name - "If not exists already"
 wifiagent - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIAGENT_SetAttributes.py)
3.Execute the generated Script(TS_WIFIAGENT_SetAttributes.py) using execution page of  Test Manager GUI
4.wifiagentstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIAgent_SetAttr through registered TDK wifiagentstub function along with necessary Path Name as arguments
5.WIFIAgent_SetAttr function will call Ccsp Base Function named "CcspBaseIf_setParameterAttributes" , that inturn will call WIFI Agent Library Function "CcspCcMbi_SetParameterAttributes" along with provided path name and Value
6.Response(s)(printf) from TDK Component,Ccsp Library function and wifiagentstub would be logged in Agent Console log based on the debug info redirected to agent console.
7.wifiagentstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result (eg:"Attributes of Requested Path is updated" along with info) and  the same is updated to agent console log.
8.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifiagentstub.</automation_approch>
    <except_output>CheckPoint 1:
Attributes info from DUT should be available in Agent Console Log
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response
CheckPoint 3:
Test Manager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetAttributes</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetAttributes');

#Get the result of connection with test component and STB
loadModuleresult=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

loadStatusExpected = "SUCCESS";

if loadStatusExpected not in loadModuleresult.upper():
        print "[Failed To Load WIFI Agent Stub or its supporting libraries probably from /usr/lib/]"
        print "[Exiting the Script]"
        exit();

#Prmitive test case which associated to this Script
tdkTestObj = obj.createTestStep('WIFIAgent_SetAttr');

#Input Parameters
tdkTestObj.addParameter("paramname","Device.WiFi.SSIDNumberOfEntries");
tdkTestObj.addParameter("notification","passive");
tdkTestObj.addParameter("accessControlChanged","anybody");

expectedresult = "SUCCESS";

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "[TEST EXECUTION RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");

print "[TEST EXECUTION RESULT] : %s" %resultDetails ;

obj.unloadModule("wifiagent");
