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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAgent_FRCheckDefaultWPSPIN</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if default WPS PIN is present after factory reset</synopsis>
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
    <test_case_id>TC_WIFIAgent_160</test_case_id>
    <test_objective>To check if default WPS PIN is present after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.1.WPS.X_CISCO_COM_Pin</input_parameters>
    <automation_approch>1.Load the modules
2.Perform Factory reset on the DUT
3.Get the Default WPS PIN using tr181 parameter Device.WiFi.AccessPoint.1.WPS.X_CISCO_COM_Pin
4.Get the one configured in factory defaults value
5.mark the script as success if values match else mark script as failure
6.Unload the module</automation_approch>
    <expected_output>The WPS PIN configured in factory defaults and one from tr181 parameter on FR should be equal</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAgent</test_stub_interface>
    <test_script>TS_WIFIAgent_FRCheckDefaultWPSPIN</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
sysobj=tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_WIFIAgent_FRCheckDefaultSecurityPassword');
sysobj.configureTestCase(ip,port,'TS_WIFIAgent_FRCheckDefaultSecurityPassword');

#Get the result of connection with test component
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    obj.saveCurrentState();

    #Initiate Factory reset before checking the default value
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
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
        print "EXPECTED RESULT 1: Should initiate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();
        tdkTestObj = obj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.WPS.X_CISCO_COM_Pin");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        if expectedresult in actualresult:
            #Set the result status of execution
            details = tdkTestObj.getResultDetails();
            pin = details.split("VALUE:")[1].split(' ')[0];
            print "TEST STEP 2: Get the WPS PIN ";
            print "EXPECTED RESULT 2: Should get the WPS Pin value successfully";
            print "ACTUAL RESULT 2: %s" %pin;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            path= "sh %s/tdk_utility.sh parseConfigFile PATH_FACTORY_DEFAULTS" %TDK_PATH;
            print path;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", path);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            path_to_defaults = tdkTestObj.getResultDetails().strip().replace("\\n","")
            if expectedresult in actualresult and path_to_defaults !="":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the path to default value";
                print "EXPECTED RESULT 3: Should Get the path to default";
                print "ACTUAL RESULT 3: Default value path : %s" %path_to_defaults;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                query="cat %s | grep -i \"Default WPS Pin\""%path_to_defaults;
                print "query:%s" %query
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult1 = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                if expectedresult in actualresult and details !="":
                    defaults= details.split(":")[1].strip().replace("\\n","");
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the factory default value stored";
                    print "EXPECTED RESULT 4: Should Get the factory default value stored";
                    print "ACTUAL RESULT 4: Default value is : %s" %defaults;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    if pin == defaults:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Compare the WPS PIN  and the one configured in factory defaults file";
                        print "EXPECTED RESULT 5: Should get WPS PIN and the one configured in factory defaults file equal";
                        print "ACTUAL RESULT 5:Values are equal: Validated %s" %defaults;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Compare the WPS PIN  and the one configured in factory defaults file";
                        print "EXPECTED RESULT 5: Should get WPS PIN and the one configured in factory defaults file equal";
                        print "ACTUAL RESULT 5:Values are equal: Validated %s" %defaults;
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the factory default value stored";
                    print "EXPECTED RESULT 4: Should Get the factory default value stored";
                    print "ACTUAL RESULT 4: Default value is : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the path to default value";
                print "EXPECTED RESULT 3: Should Get the path to default";
                print "ACTUAL RESULT 3: Default value path : %s" %path_to_defaults;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "TEST STEP 2: Get the WPS PIN ";
            print "EXPECTED RESULT 2: Should get the WPS Pin value successfully";
            print "ACTUAL RESULT 2: %s" %pin;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should initiate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "FAILURE to load wifiagent module";
    sysobj.setLoadModuleStatus("FAILURE");
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
