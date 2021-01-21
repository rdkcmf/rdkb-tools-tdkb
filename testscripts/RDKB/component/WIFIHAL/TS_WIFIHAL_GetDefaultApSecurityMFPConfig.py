##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_GetDefaultApSecurityMFPConfig</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get default ApSecurity MFPConfig as Disabled for both 2.4GHZ and 5GHZ</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>40</execution_time>
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
    <test_case_id>TC_WIFIHAL_362</test_case_id>
    <test_objective>To get default ApSecurity MFPConfig as Disabled for both 2.4GHZ and 5GHZ</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityMFPConfig()</api_or_interface_used>
    <input_parameters>methodName: getApSecurityMFPConfig</input_parameters>
    <automation_approch>1.Load wifihal module
2.Do a factory reset
3.Invoke "WIFIHAL_GetOrSetParamStringValue" to get the MFP config value  for 2.4GHz and 5GHZ
4.Check if it is disabled for both 2.4GHZ and 5GHZ</automation_approch>
    <expected_output>Default value of ApSecurityMFPConfig should be disabled for both 2.4GHZ and 5GHZ</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_GetDefaultApSecurityMFPConfig</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");
radio0 = "2.4G"
radio1 = "5G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_GetDefaultApSecurityMFPConfig');
pamobj.configureTestCase(ip,port,'TS_WIFIHAL_GetDefaultApSecurityMFPConfig');


loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =pamobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2


if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx0 = getIndex(obj, radio0);
    tdkTestObjTemp, idx1 = getIndex(obj, radio1);
    ## Check if a invalid index is returned
    if idx0 == -1 or idx1 == -1:
        if idx0 == -1 :
            print "Failed to get radio index for radio %s\n" %radio0;
        if idx1 == -1:
	    print "Failed to get radio index for radio %s\n" %radio1;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #save device's current state before it goes for reboot
        pamobj.saveCurrentState();
        #Initiate Factory reset before checking the default value
        tdkTestObj = pamobj.createTestStep('pam_Setparams');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
        tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
        tdkTestObj.addParameter("Type","string");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Initiate factory reset ";
            print "EXPECTED RESULT 1: Should inititate factory reset";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            #Restore the device state saved before reboot
            pamobj.restorePreviousStateAfterReboot();

            apIndex = idx0
            getMethod = "getApSecurityMFPConfig"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
            ConfigValue1 = details.split(":")[1].strip()

            if expectedresult in actualresult and "Disabled" in ConfigValue1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2:Should get default 2.4GHZ ApSecurityMFPConfig as disabled";
                print "ACTUAL RESULT 2:Default 2.4GHZ ApSecurityMFPConfig: %s" %ConfigValue1;

                apIndex = idx1
                getMethod = "getApSecurityMFPConfig"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

                ConfigValue2 = details.split(":")[1].strip()

                if expectedresult in actualresult and "Disabled" in ConfigValue2:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3:Should get default 5GHZ ApSecurityMFPConfig as disabled";
                    print "ACTUAL RESULT 3:Default 5GHZ ApSecurityMFPConfig: %s" %ConfigValue2;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3:Failed to get 5GHZ ApSecurityMFPConfig as disabled";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Failed to get 2.4GHZ ApSecurityMFPConfig as disabled";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Initiate factory reset ";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    pamobj.unloadModule("pam");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");