##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_StartOrStopHostApd</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_StartorStopHostApd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To start or stop Host Apd using wifi_startHostApd() and wifi_stopHostApd() and validate the same using wifi_getApStatus() api.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_284</test_case_id>
    <test_objective>To start or stop Host Apd using wifi_startHostApd() and wifi_stopHostApd() and validate the same using wifi_getApStatus() api.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_startHostApd()
wifi_stopHostApd()
wifi_getApStatus()
wifi_getApEnable()
wifi_setApEnable()</api_or_interface_used>
    <input_parameters>methodName : startHostApd
methodName : stopHostApd
methodName : getApStatus
methodName : getApEnable
methodName : setApEnable
radioIndex : 0
radioIndex : 1</input_parameters>
    <automation_approch>1.Get the ApEnable value using wifi_getApEnable() for both 2.4GHz and 5GHz.
2.If the value is Enabled,get the Ap Status for both 2.4GHz and 5GHz using wifi_getApStatus() api.
3.If the value is not Enabled,set the ApEnable to Enabled using wifi_setApEnable() api and get the Ap Status for both 2.4GHz and 5GHz.
4.If the Ap status is 'Up' for either 2.4GHz or 5GHz, call the wifi_stopHostApd() api else call the wifi_startHostApd() api.
5.Get the Ap status and check whether the status is changed after calling   wifi_startHostApd() or wifi_stopHostApd() api for both 2.4GHz and 5GHz.
6.If changed,return SUCCESS,else FAILURE.
7.Unload the module.</automation_approch>
    <except_output>Ap Status should change after invoking wifi_startHostApd() and wifi_stopHostApd() for both  2.4GHz and 5GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_StartOrStopHostApd</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_StartOrStopHostApd');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

def GetApStatus(radioIndex):
    expectedresult="SUCCESS";
    getMethod = "getApStatus"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'
    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
	return (details.split(":")[1].strip());
    else:
        tdkTestObj.setResultStatus("FAILURE");

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    status0_initial = GetApStatus(0);
    print"InitialApStatus for 2.4GHz = ",status0_initial;
    status1_initial = GetApStatus(1);
    print"InitialApStatus for 5GHz = ",status1_initial;
    if status0_initial == 'Up' or status1_initial == 'Up':
	print"********INVOKING wifi_stopHostApd() api********";
        #Primitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_StartorStopHostApd');
        #Giving the method name to invoke the api wifi_stopHostApd()
        tdkTestObj.addParameter("methodName","stopHostApd");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            time.sleep(5);
            status0_final = GetApStatus(0);
            status1_final = GetApStatus(1);
            print"ApStatus for 2.4GHz after calling stopHostApd is  ",status0_final;
            print"ApStatus for 5GHz after calling stopHostApd is  ",status1_final;
            if status0_final == 'Disable' and status1_final == 'Disable':
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP:To stop the HostApd using wifi_stopHostApd() api and check whether the Apstatus is changed";
                print"EXPECTED RESULT:The ApStatus should be changed to 'Disable' for both 2.4GHz and 5GHz";
                print"ACTUAL RESULT:The ApStatus is changed to 'Disable' for both 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT]:SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP:To stop the HostApd using wifi_stopHostApd() api and check whether the Apstatus is changed";
                print"EXPECTED RESULT:The ApStatus should be changed to 'Disable' for both 2.4GHz and 5GHz";
                print"ACTUAL RESULT:The ApStatus is not changed to 'Disable' for both 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT]:FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"StopHostApd() operation failed";
    elif status0_initial == 'Disable' or status1_initial == 'Disable':
        print"********INVOKING wifi_startHostApd() api********";
        #Primitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_StartorStopHostApd');
        #Giving the method name to invoke the api wifi_startHostApd()
        tdkTestObj.addParameter("methodName","startHostApd");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            time.sleep(5);
            status0_final = GetApStatus(0);
            status1_final = GetApStatus(1);
            print"ApStatus for 2.4GHz after calling startHostApd is  ",status0_final;
            print"ApStatus for 5GHz after calling startHostApd is  ",status1_final;
            if status0_final == 'Up' and status1_final == 'Up':
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP:To start the HostApd using wifi_startHostApd() api and check whether the Apstatus is changed";
                print"EXPECTED RESULT:The ApStatus should be changed to 'Up' for both 2.4GHz and 5GHz";
                print"ACTUAL RESULT:The ApStatus is changed to 'Up' for both 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT]:SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP:To start the HostApd using wifi_startHostApd() api and check whether the Apstatus is changed";
                print"EXPECTED RESULT:The ApStatus should be changed to 'Up' for both 2.4GHz and 5GHz";
                print"ACTUAL RESULT:The ApStatus is not changed to 'Up' for both 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT]:FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"StartHostApd() operation failed";
    else:
        print "wifi_getApStatus is returning invalid status";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
