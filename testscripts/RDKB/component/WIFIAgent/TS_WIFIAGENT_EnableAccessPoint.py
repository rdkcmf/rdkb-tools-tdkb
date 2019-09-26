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
  <name>TS_WIFIAGENT_EnableAccessPoint</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
     <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_13</test_case_id>
    <test_objective>To validate AccessPoint Enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
WIFIAgent_Set_Get
Input
1.PathName ("paramName")
( eg: "Device.WiFi.AccessPoint.1.Enable" )
2.Type: bool, Value: true</input_parameters>
    <automation_approch>"1.Configure the Function info in Test Manager GUI  which needs to be tested  
(WIFIAgent_Set_Get  - func name - """"If not exists already""""
 wifiagent - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_WIFIAGENT_EnableAccessPoint.py)
3.Execute the generated Script(TS_WIFIAGENT_EnableAccessPoint.py) using excution page of  Test Manager GUI
4.wifiagentstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIAgent_Set_Get through registered TDK wifiagentstub function along with necessary Path Name and Values as arguments
5.WIFIAgent_Set_Get function will call Ccsp Base Function named """"CcspBaseIf_setParameterValues"""" to set given input parameter Values and Ccsp Base Function named """"CcspBaseIf_getParameterValues"""", that inturn will execute  get functionality of parameter 
6.Response(s)(printf) from TDK Component,Ccsp Library function and cmagentstub would be logged in Agent Console log based on the debug info redirected to agent console.
7.wifiagentstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result (""""Values for Requested Param"""" ) and the same is updated to agent console log.
8.TestManager will publish the result in GUI as PASS/FAILURE based on the response from wifiagentstub.

"</automation_approch>
    <except_output>CheckPoint 1:
TDK agent Test Function will log the test case result as PASS based on API response
CheckPoint 2:
TestManager GUI will publish the result as PASS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_WIFIAGENT_EnableAccessPoint</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
						
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_EnableAccessPoint');

#Get the result of connection with test component
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    
    #### Set and Get Values ####
    tdkTestObj = obj.createTestStep("WIFIAgent_Set_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.1.Enable");
    tdkTestObj.addParameter("paramValue","true");
    tdkTestObj.addParameter("paramType","bool");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        details = tdkTestObj.getResultDetails();
        print "EXPECTED RESULT 1: Should Set the Access Point Enable Value to True";
        print "ACTUAL RESULT DETAILS 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult;
        print "Enable Access Point Function is SUCCESS"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        details = tdkTestObj.getResultDetails();
        print "EXPECTED RESULT 1: Should Set the Access Point Enable Value to True";
        print "ACTUAL RESULT DETAILS 1: %s" %details;
        print "[TEST EXECUTION RESULT] : %s" %actualresult;
        print "Enable Access Point Function is FAILURE"        
    obj.unloadModule("wifiagent");
else:
        print "FAILURE to load wifiagent module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";

					
