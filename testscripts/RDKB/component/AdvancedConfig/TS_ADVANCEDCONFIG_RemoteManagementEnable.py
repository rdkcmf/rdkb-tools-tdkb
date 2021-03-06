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
  <name>TS_ADVANCEDCONFIG_RemoteManagementEnable</name>
  <primitive_test_id/>
  <primitive_test_name>AdvancedConfig_Set</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>RPI</box_type>
    <box_type>Emulator</box_type>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_ADVANCEDCONFIG_19</test_case_id>
    <test_objective>To verify, Enable Remote management</test_objective>
    <test_type>Possitive</test_type>
    <test_setup>Emulator,
XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name:
AdvancedConfig_Set
Input:
1.PathName ("paramName")
( eg: "Device.NAT.X_CISCO_COM_PortTriggers.Enable" )
2.Type: bool, Value: true</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(AdvancedConfig_Set - func name - "If not exists already"
 advancedconfig - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_ADVANCEDCONFIG_RemoteManagementEnable.py)
3.Execute the generated Script(TS_ADVANCEDCONFIG_RemoteManagementEnable.py) using execution page of  Test Manager GUI
4.advancedconfigstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named AdvancedConfig_Set, AdvancedConfig_AddObject through registered TDK advancedconfigstub function along with necessary Entry Values as arguments
5.AdvancedConfig_Set function will call ssp_setParameterValue,that inturn will call CCSP Base Interface Function named CcspBaseIf_setParameterValues.
6.Responses(printf) from TDK Component,Ccsp Library function and advancedcongifstub would be logged in Agent Console log based on the debug info redirected to agent console   
7.advancedconfigstub will validate the available result (from ssp_setParameterValue as zero) with expected result (zero) and the result is updated in agent console log and json output variable
8.TestManager will publish the result in GUI as SUCCESS/FAILURE based on the response from AdvancedConfig_Set functions.</automation_approch>
    <except_output>Checkpoint 1:
Check if Remote management is enabled.
CheckPoint 2:
Success log should be available in Agent Console Log
CheckPoint 3:
TDK agent Test Function will log the test case result as SUCCESS based on API response 
CheckPoint 4:
TestManager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>none</test_stub_interface>
    <test_script>TS_ADVANCEDCONFIG_RemoteManagementEnable</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("advancedconfig","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ADVANCEDCONFIG_RemoteManagementEnable');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

loadStatusExpected = "SUCCESS"

if loadStatusExpected not in loadModuleresult.upper():
        print "[Failed To Load Advanced config Stub from /opt/TDK/libs/]"
        print "[Exiting the Script]"
        exit();

#Prmitive test case which associated to this Script
tdkTestObj = obj.createTestStep('AdvancedConfig_Set');

#Input Parameters
tdkTestObj.addParameter("paramName","Device.UserInterface.X_CISCO_COM_RemoteAccess.Enable");
tdkTestObj.addParameter("paramValue","true");
tdkTestObj.addParameter("paramType","boolean");
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
        print "[STEP 1]: Set the boolean value to true ";
        print "[EXPECTED RESLUT 1]: Should set the boolean value to true ";
        print "[ACTUAL RESULT 1]: Successfully set the boolean value, %s" %resultDetails;
        print "[TEST EXECUTION RESULT] :%s" %actualresult;
else:
	#Set the result status of execution as failure
	tdkTestObj.setResultStatus("FAILURE");
	print "[STEP 1]: Set the boolean value to true";
	print "[EXPECTED RESLUT 1]: Should set the boolean value to true ";
        print "[ACTUAL RESULT 1]: Failed to set the boolean value, %s" %resultDetails;
        print "[TEST EXECUTION RESULT] :%s" %actualresult;

obj.unloadModule("advancedconfig");
