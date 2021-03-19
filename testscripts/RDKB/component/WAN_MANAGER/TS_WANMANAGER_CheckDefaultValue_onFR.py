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
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_CheckDefaultValue_onFR</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the default value of Device.X_RDK_WanManager.Enable is true ,Device.X_RDK_WanManager.Policy is PRIMARY_PRIORITY and
Device.X_RDK_WanManager.IdleTimeout is 0</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WANMANAGER_09</test_case_id>
    <test_objective>Check if the default value of Device.X_RDK_WanManager.Enable is true ,Device.X_RDK_WanManager.Policy is PRIMARY_PRIORITY and
Device.X_RDK_WanManager.IdleTimeout is 0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>WIFIAgent_Set
TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset
Device.X_RDK_WanManager.Policy
Device.X_RDK_WanManager.Enable
Device.X_RDK_WanManager.IdleTimeout</input_parameters>
    <automation_approch>1] Load the module
2] Perform Factory reset on the DUT
3] Check if the default value of Device.X_RDK_WanManager.Enable is true ,Device.X_RDK_WanManager.Policy is PRIMARY_PRIORITY and
Device.X_RDK_WanManager.IdleTimeout is 0
4]Unload the module</automation_approch>
    <expected_output> Default value of Device.X_RDK_WanManager.Enable is true ,Device.X_RDK_WanManager.Policy is PRIMARY_PRIORITY and
Device.X_RDK_WanManager.IdleTimeout is 0</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckDefaultValue_onFR</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
obj1 = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_CheckDefaultValue_onFR');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_CheckDefaultValue_onFR');

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
    tdkTestObj.addParameter("paramName", "Device.X_CISCO_COM_DeviceControl.FactoryReset");
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
        tdkTestObj.addParameter("ParamName", "Device.X_RDK_WanManager.Policy");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details == "PRIMARY_PRIORITY":
            details = details.strip().replace("\\n", "");
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 : Default WANMANAGER policy value after Factory reset";
            print "EXPECTED RESULT 2: Should get WANMANAGER policy default value after Factory reset";
            print "ACTUAL RESULT 2: The value received is %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName", "Device.X_RDK_WanManager.Enable");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            details = details.strip().replace("\\n", "");
            if expectedresult in actualresult and details == "true":
                details = details.strip().replace("\\n", "");
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2 : Default WANMANAGER Enable value after Factory reset";
                print "EXPECTED RESULT 2: Should get WANMANAGER Enable default value after Factory reset";
                print "ACTUAL RESULT 2: The value received is %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName", "Device.X_RDK_WanManager.IdleTimeout");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult :
                    if int(details) == 0:
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "TEST STEP 2 : Default WANMANAGERIdleTimeout value after Factory reset";
                       print "EXPECTED RESULT 2: Should get WANMANAGER IdleTimeout default value after Factory reset";
                       print "ACTUAL RESULT 2: The value received is %s" %details;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 2 :  Default WANMANAGERIdleTimeout value after Factory reset";
                        print "EXPECTED RESULT 2: Should get WANMANAGER IdleTimeout default value after Factory reset";
                        print "ACTUAL RESULT 2: The value received is %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 2 : Get Default WANMANAGERIdleTimeout value after Factory reset";
                        print "EXPECTED RESULT 2: Should get WANMANAGER IdleTimeout default value after Factory reset";
                        print "ACTUAL RESULT 2: Failed to fetch idle timeout after Factory reset";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2 : Default WANMANAGER Enable value after Factory reset";
                print "EXPECTED RESULT 2: Should get WANMANAGER Enable default value after Factory reset";
                print "ACTUAL RESULT 2: The value received is %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 :  Default WANMANAGER policy value after Factory reset";
            print "EXPECTED RESULT 2: Should get WANMANAGER policy default value after Factory reset";
            print "ACTUAL RESULT 2: The value received is %s" %details;
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
