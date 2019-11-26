##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_WIFIAGENT_CheckPublicWifiEnableStatusPersistence_OnReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Enable public wifi and check it persists on reboot</synopsis>
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
    <test_case_id>TC_WIFIAGENT_71</test_case_id>
    <test_objective>Enable public wifi and check it persists on reboot</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load module
2.Get values of public wifi
3.Enable public wifi
4.Do a reboot
5.Check if pubilic wifi values persists on reboot
6.Unload module</automation_approch>
    <expected_output>Public wifi values should persist on reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckPublicWifiEnableStatusPersistence_OnReboot</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from xfinityWiFiLib import *
from tdkbVariables import *;


#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");
obj2 = tdklib.TDKScriptingLibrary("sysutil","1");
obj3 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPublicWifiEnableStatusPersistence_OnReboot');
obj2.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPublicWifiEnableStatusPersistence_OnReboot');
obj3.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPublicWifiEnableStatusPersistence_OnReboot');


#Get the result of connection with test component and DUT
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 =obj2.getLoadModuleResult();
loadmodulestatus3 =obj3.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus3


if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    obj1.setLoadModuleStatus("SUCCESS");

    #Get current values of public wifi params
    expectedresult="SUCCESS";
    tdkTestObj,actualresult,orgValue = getPublicWiFiParamValues(obj1);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj2.createTestStep('ExecuteCmd');
        details1 = "sh %s/tdk_utility.sh parseConfigFile DSCPMARKPOLICY" %TDK_PATH;
        details2 = "sh %s/tdk_utility.sh parseConfigFile PRIMARYREMOTEENDPOINT" %TDK_PATH;
        details3 = "sh %s/tdk_utility.sh parseConfigFile SECONDARYREMOTEENDPOINT" %TDK_PATH;
        print details1;
        print details2;
        print details3;

        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command", details1);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        DSCPMarkPolicy = tdkTestObj.getResultDetails().replace("\\n", "");
        tdkTestObj.addParameter("command", details2);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        PrimaryRemoteEndpoint = tdkTestObj.getResultDetails().replace("\\n", "");
        tdkTestObj.addParameter("command", details3);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        SecondaryRemoteEndpoint = tdkTestObj.getResultDetails().replace("\\n", "");


        setValues = [DSCPMarkPolicy,PrimaryRemoteEndpoint,SecondaryRemoteEndpoint,"true","true","true"];
        tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj1,setValues);
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 : Should enable PublicWiFi"
            print "ACTUAL RESULT 2:%s" %details
            print "[TEST EXECUTION RESULT] : SUCCESS";
            time.sleep(30);
            obj1.initiateReboot();
            time.sleep(300);
            tdkTestObj,actualresult,newValue = getPublicWiFiParamValues(obj1);
            if newValue == setValues:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check public wifi values persist on reboot"
                print "ACTUAL RESULT 3:Public wifi values persist on reboot"
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Check public wifi values persist on reboot"
                print "ACTUAL RESULT 3:Public wifi values does not persist on reboot"
                print "[TEST EXECUTION RESULT] : FAILURE";
            #Revert the values of public wifi params
            tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj1,orgValue);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP :Revert the PublicWiFi param values"
                print "ACTUAL RESULT :%s" %details
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP :Revert the PublicWiFi param values"
                print "ACTUAL RESULT :%s" %details
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:Enable PublicWiFi"
            print "ACTUAL RESULT 2:%s" %details
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj1.unloadModule("wifiagent");
    obj2.unloadModule("sysutil");
    obj3.unloadModule("tdkbtr181");

else:
    print "Failed to load wifi module";
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";


