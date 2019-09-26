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
  <version>15</version>
  <name>TS_TR069PA_SetParam_Attributes</name>
  <primitive_test_id/>
  <primitive_test_name>TR069Agent_SetParameterAttr</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>TC_TR069_5 - To Validate Set Param Attributes API for TR069 PA</synopsis>
  <groups_id>4</groups_id>
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
    <test_case_id>TC_TR069_5</test_case_id>
    <test_objective>To Validate Set Param Attributes API for 
TR069 PA</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
6.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used/>
    <input_parameters>Json Interface:
API Name
TR069Agent_SetParameterAttr
Input
1.Parameter Path (paramName)( eg: "Device." )
2.Parameter Value (eg. "bbb")
3.Paramter Type (eg. String)</input_parameters>
    <automation_approch>1.Create a fucntion named TR069Agent_SetParameterAttr in Test Manager GUI. 
2.Configure the info of the  function under test in function and create a python script
3.Execute the generated Script(TS_TR069PA_SetParam_Attributes.py) using execution page of  Test Manager GUI 
4.This script will in turn call TR069Agent stub in TDK Agent 
5.TR069Agent_SetParameterAttr function will call CCSP Base Interface Function named "CcspBaseIf_setParameterAttributes" , that inturn will call TR069PA Agent Library Function "CcspManagementServer_SetParameterAttributes" 
6.Then TR069Agent stub will call CCSP Base Interface Function named "CcspBaseIf_getParameterAttributes" for the same inputs to check whether the attributes have been updated .
7.Responses(printf) from TDK Component and TR069 agentstub would be logged in Agent Console log 
8.Based on the log set the result as SUCCESS or FAILURE</automation_approch>
    <except_output>CheckPoint 1:
String comapre the set attributes using a proper Get of the same.Attributes of Requested Path  should be available in Agent Console Log.Also 
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response
CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_TR069PA_SetParam_Attributes</test_script>
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
obj = tdklib.TDKScriptingLibrary("TR069Pa","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_SetParam_Attributes');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
		
    tdkTestObj = obj.createTestStep('TR069Agent_SetParameterAttr');  
    tdkTestObj.addParameter("ParamName","Device.ManagementServer.STUNPassword");
    tdkTestObj.addParameter("AccessControl","acs");
    tdkTestObj.addParameter("Notify","active");

		
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
		
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");

        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
	print "%s" %details;
	 
    else:   
        tdkTestObj.setResultStatus("FAILURE"); 
	print "[TEST EXECUTION RESULT] : %s" %actualresult ;	
        print "%s" %details;
    obj.unloadModule("TR069Pa");
   		 
else:   
        print "Failed to load TR069PA module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";				
				
