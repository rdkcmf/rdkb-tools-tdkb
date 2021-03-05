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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>4</version>
  <name>TS_TR069PA_GetManagementServerURLAfterFactoryReset</name>
  <primitive_test_id/>
  <primitive_test_name>TR069Agent_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Management Server URL holds the default URL after a Factory reset on DUT</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TR069_19</test_case_id>
    <test_objective>This test case is to check if Management Server URL holds the default URL after a Factory reset on DUT</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand ,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.ManagementServer.URL</input_parameters>
    <automation_approch>1.Load the module 
2.Perform Factory reset on the DUT
3.Check if  Device.ManagementServer.URL hold the configured default value 
4.unload the module</automation_approch>
    <expected_output>On factory reset Device.ManagementServer.URL is expected to hold the Factory default value</expected_output>
    <priority>High</priority>
    <test_stub_interface>TR069</test_stub_interface>
    <test_script>TS_TR069PA_GetManagementServerURLAfterFactoryReset</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
from tr69Config import *
from time import sleep;
obj1 = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_GetManagementServerURLAfterFactoryReset');
obj1.configureTestCase(ip,port,'TS_TR069PA_GetManagementServerURLAfterFactoryReset');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
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
        obj.restorePreviousStateAfterReboot();
        sleep(180);
        
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.ManagementServer.URL");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            details = details.strip().replace("\\n", "");
            if details == SERVER_URL:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2 : Query Management Server URL after Factory reset";
                print "EXPECTED RESULT 2: Should get default Managment Server URL after Factory Reset";
                print "ACTUAL RESULT 2: The value received is the default URL";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                details = details.strip().replace("\\n", "");
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2 : Query Management Server URL after Factory reset";
                print "EXPECTED RESULT 2: Should get default Management Server URL after Factory Reset";
                print "ACTUAL RESULT 2: The value received is not the expected default URL";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] :FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("wifiagent");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
     obj1.setLoadModuleStatus("FAILURE");
