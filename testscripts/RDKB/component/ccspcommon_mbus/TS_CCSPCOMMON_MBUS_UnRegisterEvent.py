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
  <version>4</version>
  <name>TS_CCSPCOMMON_MBUS_UnRegisterEvent</name>
  <primitive_test_id/>
  <primitive_test_name>CCSPMBUS_UnRegisterEvent</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_CCSPMBUS_4</test_case_id>
    <test_objective>To Validate Ccsp Interface UnRegister Event Function</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,
XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component"
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
CCSPMBUS_UnRegisterEvent
Input
eventName</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(CCSPMBUS_UnRegisterEvent - func name - "If not exists already"
 ccspcommon_mbus - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_CCSPCOMMON_MBUS_UnRegisterEvent.py)
3.Execute the generated Script(TS_CCSPCOMMON_MBUS_UnRegisterEvent.py) using execution page of  Test Manager GUI
4.mbusstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named CCSPMBUS_UnRegisterEvent through registered TDK mbusstub function along with necessary Entry Values as arguments
5.CCSPMBUS_UnRegisterEvent function will call ssp_mbus_int and ssp_mbus_register_event functions with necessary arguments,then it call ssp_mbus_unregister_event that inturn will call CCSP Base Interface Function named CcspBaseIf_UnRegister_Event which is under test to Un register event from Message bus
6.Responses(printf) from TDK Component,Ccsp Library function and mbusstub would be logged in Agent Console log based on the debug info redirected to agent console   
7.mbusstub will validate the available result (from ssp_mbus_unregister_event as CCSP_Message_Bus_OK [100] ) with expected result (CCSP_Message_Bus_OK [100] ) and the result is updated in agent console log and json output variable
8.ssp_mbus_exit function is invoked by CCSPMBUS_UnRegisterEvent to close the bus handle created by ssp_mbus_init and returns the updated results to Test Manager
8.TestManager will publish the result in GUI as PASS/FAILURE based on the response from CCSPMBUS_UnRegisterEvent function</automation_approch>
    <except_output>CheckPoint 1:
Message Bus Event Registered and UnRegistered success log from DUT should be available in Agent Console Log
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response which will be available in Test Manager Result ( XLS)
CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_CCSPCOMMON_MBUS_UnRegisterEvent</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''

#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("ccspcommon_mbus","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CCSPCOMMON_MBUS_UnRegisterEvent');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s\n" %loadModuleresult;

loadStatusExpected = "SUCCESS"

if loadStatusExpected not in loadModuleresult.upper():
        print "[Failed To Load MBUS Agent Stub from from env TDK_PATH]"
        print "[Exiting the Script]"
        exit();

#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CCSPMBUS_LoadCfg');

#Input Parameters
tdkTestObj.addParameter("cmpCfgFile","TDKB.cfg");

expectedresult = "SUCCESS";

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);


#Get the result of execution
actualresult = tdkTestObj.getResult();
print "\n[TEST ACTUAL RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
        print "\nMessage Bus Load Config is SUCCESS"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
        print "\nMessage Bus Load Config is FAILURE"
        obj.unloadModule("ccspcommon_mbus");
        exit();

print "\n[TEST EXECUTION RESULT] : %s\n" %resultDetails ;

#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CCSPMBUS_Init');

#Input Parameters
tdkTestObj.addParameter("cfgfileName","/tmp/ccsp_msg.cfg");

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "\n[TEST ACTUAL RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
        print "\nMessage Bus Initialization is SUCCESS"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
        print "\nMessage Bus Initialization is FAILURE"
        obj.unloadModule("ccspcommon_mbus");
        exit();

print "\n[TEST EXECUTION RESULT] : %s\n" %resultDetails ;


#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CCSPMBUS_RegisterPath');

#Input Parameters - Nil

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "\n[TEST ACTUAL RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
        print "\nMessage Bus Register Path Function is Success"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
        print "\nMessage Bus Register Path Function is FAILURE"
        obj.unloadModule("ccspcommon_mbus");
        exit();

print "\n[TEST EXECUTION RESULT] : %s\n" %resultDetails ;


#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CCSPMBUS_RegisterEvent');

#Input Parameters
tdkTestObj.addParameter("eventName","reboot");

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "\n[TEST ACTUAL RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
        print "\nMessage Bus Register Event Function is Success"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
        print "\nMessage Bus Register Event Function is FAILURE"
        obj.unloadModule("ccspcommon_mbus");
        exit();

print "\n[TEST EXECUTION RESULT] : %s\n" %resultDetails ;

#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CCSPMBUS_UnRegisterEvent');

#Input Parameters
tdkTestObj.addParameter("eventName","reboot");

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "\n[TEST ACTUAL RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
        print "\nMessage Bus UnRegister Event Function is Success"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
        print "\nMessage Bus UnRegister Event Function is FAILURE"
        obj.unloadModule("ccspcommon_mbus");
        exit();

print "\n[TEST EXECUTION RESULT] : %s\n" %resultDetails ;


#Primitive test case which associated to this Script
tdkTestObj = obj.createTestStep('CCSPMBUS_Exit');

#Input Parameters - Nil

#Execute the test case in STB
tdkTestObj.executeTestCase(expectedresult);

#Get the result of execution
actualresult = tdkTestObj.getResult();
print "\n[TEST ACTUAL RESULT] : %s" %actualresult ;

resultDetails = tdkTestObj.getResultDetails();

if expectedresult in actualresult:
	#Set the result status of execution as success
	tdkTestObj.setResultStatus("SUCCESS");
        print "\nMessage Bus De-Initialization/Exit is SUCCESS"
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
        print "\nMessage Bus De-Initialization/Exit is FAILURE"

print "\n[TEST EXECUTION RESULT] : %s\n" %resultDetails ;

obj.unloadModule("ccspcommon_mbus");	
