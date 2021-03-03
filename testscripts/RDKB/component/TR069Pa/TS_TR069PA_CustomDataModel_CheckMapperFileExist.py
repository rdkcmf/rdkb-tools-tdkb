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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TR069PA_CustomDataModel_CheckMapperFileExist</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if custom_mapper.xml file exists in the DUT</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TR069_12</test_case_id>
    <test_objective>This test case is to check if custom_mapper.xml file exists in the DUT</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>Filepath of mapper file</input_parameters>
    <automation_approch>1.Load the module 
2.Get the data_model_file_name using syscfg
3.Check if the same file exists in the DUT
4.Unload the module</automation_approch>
    <expected_output>The file name received via syscfg should exist in the DUT</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_TR069PA_CustomDataModel_CheckMapperFileExist</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
obj1 = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
obj2= tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_CheckMapperFileExist');
obj2.configureTestCase(ip,port,'TS_TR069PA_CustomDataModel_CheckMapperFileExist');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 =obj2.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2 ;

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj1.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    #save device's current state before it goes for reboot
    tdkTestObj = obj1.createTestStep('WIFIAgent_Set');
    obj1.saveCurrentState();
    #Initiate Factory reset before checking the default value
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("paramType","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj1.restorePreviousStateAfterReboot();
        sleep(180);

        tdkTestObj = obj2.createTestStep('ExecuteCmd');
        cmd = "syscfg get custom_data_model_file_name";
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult and details== "/usr/ccsp/tr069pa/custom_mapper.xml":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Query the Custom Data Model file name";
            print "EXPECTED RESULT 2:Should get Custom Data Model File Name as /usr/ccsp/tr069pa/custom_mapper.xml";
            print "ACTUAL RESULT 2: The value received is %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj2.createTestStep('ExecuteCmd');
            cmd = "[ -f /usr/ccsp/tr069pa/custom_mapper.xml ] && echo \"File exist\" || echo \"File does not exist\"";
            tdkTestObj.addParameter("command",cmd);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check for custom_mapper.xml file presence";
                print "EXPECTED RESULT 3:custom_mapper.xml file should be present";
                print "ACTUAL RESULT 3:custom_mapper.xml file is present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check for custom_mapper.xml file presence";
                print "EXPECTED RESULT 3:custom_mapper.xml file should be present";
                print "ACTUAL RESULT 3:custom_mapper.xml file is not present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Query the Custom Data Model file name";
            print "EXPECTED RESULT 2:Should get Custom Data Model File Name as /usr/ccsp/tr069pa/custom_mapper.xml";
            print "ACTUAL RESULT 2: The value received is %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj1.unloadModule("wifiagent");
    obj2.unloadModule("sysutil");
else:
     print "Failed to load module";
     obj1.setLoadModuleStatus("FAILURE");
     obj2.setLoadModuleStatus("FAILURE");
