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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_SetParamValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set Parameter Values API Validation</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_8</test_case_id>
    <test_objective>To Validate Set Param Values Function for \WIFI Agent</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
WIFIAgent_Set
Input
1.PathName ("paramName")( eg: "Device.WiFi.AccessPoint.1.X_CISCO_COM_KickAssocDevices" )
2.Parameter Value 
 ("paramValue" as true)
3.Parameter Type ("paramType" as bool)</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(WIFIAgent_Set  - func name - "If not exists already"
 wifiagent - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIAGENT_SetParamValues.py)
3.Execute the generated Script(TS_WIFIAGENT_SetParamValues.py) using execution page of  Test Manager GUI
4.wifiagentstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIAgent_Set through registered TDK wifiagentstub function along with necessary Path Name as arguments
5.WIFIAgent_Set function will call Ccsp Base Function named "CcspBaseIf_setParameterValues" , that inturn will call WIFI Agent Library Function "CcspCcMbi_SetParameterValues" along with provided path name and Value
6.Response(s)(printf) from TDK Component,Ccsp Library function and wifiagentstub would be logged in Agent Console log based on the debug info redirected to agent console.
7.wifiagentstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result ( eg:"Values of Requested Path is updated" along with info) and  the same is updated to agent console log.
8.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifiagentstub.</automation_approch>
    <except_output>CheckPoint 1:
Set Execution succeded log from DUT should be available in Agent Console Log
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response
CheckPoint 3:
Test Manager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetParamValues</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#import statement
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetParamValues');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the load module status
    obj.setLoadModuleStatus("SUCCESS");
    #Set the encryption method
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod");
    tdkTestObj.addParameter("paramValue","AES");
    tdkTestObj.addParameter("paramType","string");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 Set the encryption method as AES for 2.4GHZ WIFI";
        print "EXPECTED RESULT 1: Should set the encryption method as AES for 2.4GHZ WIFI";
        print "ACTUAL RESULT 1: Status %s" %details;
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the encryption method after set
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.X_CISCO_COM_EncryptionMethod");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        value = tdkTestObj.getResultDetails();
        value = value.split("VALUE:")[1].split(' ')[0]

        if expectedresult in actualresult and "AES" in value:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the encryption method of 2.4GHZ WIFI";
            print "EXPECTED RESULT 2: Should get the encryption method of 2.4GHZ WIFI";
            print "ACTUAL RESULT 2: Encryption Method is %s" %value;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the encryption method of 2.4GHZ WIFI";
            print "EXPECTED RESULT 2: Should get the encryption method of 2.4GHZ WIFI";
            print "ACTUAL RESULT 2: Encryption Method is %s" %value;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Set the encryption method as AES for 2.4GHZ WIFI";
        print "EXPECTED RESULT 1: Should set the encryption method as AES for 2.4GHZ WIFI";
        print "ACTUAL RESULT 1: Status %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
else:
        print "Failed to load wifi agent module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
