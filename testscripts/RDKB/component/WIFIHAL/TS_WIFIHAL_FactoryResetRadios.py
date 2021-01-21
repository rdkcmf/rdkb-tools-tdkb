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
  <version>9</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_FactoryResetRadios</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_FactoryReset</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To invoke the api wifi_factoryResetRadio() and check whether the get values are default values after factory reset radio for both 2.4GHz and 5GHz.</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_289</test_case_id>
    <test_objective>To invoke the api wifi_factoryResetRadio() and check whether the get values are default values after factory reset radio for both 2.4GHz and 5GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioOperatingChannelBandwidth()
wifi_getRadioGuardInterval()
wifi_setRadioOperatingChannelBandwidth()
wifi_setRadioGuardInterval()
wifi_factoryResetRadios()</api_or_interface_used>
    <input_parameters>methodName : getChannelBandwidth
methodName : getRadioGuardInterval
methodName : setChannelBandwidth
methodName : setRadioGuardInterval
methodName : factoryResetRadios
radioIndex : 0
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get thechannel bandwidth  and radio guard interval using wifi_getRadioOperatingChannelBandwidth() and wifi_getRadioGuardInterval() apis respectively for both 2.4GHz and 5GHz.
3.Set these two values to other values using wifi_setRadioOperatingChannelBandwidth()
wifi_setRadioGuardInterval() apis respectively for both 2.4GHz and 5GHz.
4.Invoke the wifi_factoryResetRadio() api.
5.Get the values after reset.
6.Get values should be equal to default values for both 2.4GHz and 5GHz. If so,return SUCCESS,else FAILURE.
7.Revert the values back to the initial values.
8.Unload the module.</automation_approch>
    <expected_output>To invoke the api wifi_factoryResetRadio() and check whether the get values are default values after factory reset radio for both 2.4GHz and 5GHz.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_FactoryResetRadios</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import time;
from tdkbVariables import *;
radio0 = "2.4G"
radio1 = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_FactoryResetRadios');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_FactoryResetRadios');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

def InvokeGetSetMethod(primitive,radioIndex,Value,MethodName):
    expectedresult="SUCCESS";
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, Value, MethodName)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        return details;
    else:
	tdkTestObj.setResultStatus("FAILURE");

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
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
        details_Enable0 = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"0","getChannelBandwidth");
        Channel_Bandwidth_initial0 = details_Enable0.split(":")[1].strip(" ");
        details_Enable1 = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"0","getChannelBandwidth");
        Channel_Bandwidth_initial1 = details_Enable1.split(":")[1].strip(" ");
        details_interval0 = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"0","getRadioGuardInterval");
        GuardInterval_initial0 = details_interval0.split(":")[1].strip(" ");
        details_interval1 = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"0","getRadioGuardInterval");
        GuardInterval_initial1 = details_interval1.split(":")[1].strip(" ");

        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"160MHz","setChannelBandwidth");
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"160MHz","setChannelBandwidth");
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"800nsec","setRadioGuardInterval");
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"800nsec","setRadioGuardInterval");
        time.sleep(5);
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"0","getChannelBandwidth");
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"0","getChannelBandwidth");
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"0","getRadioGuardInterval");
        InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"0","getRadioGuardInterval");
        #call the factory reset radio api
        #Primitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_FactoryReset');
        #Giving the method name to invoke the api wifi_factoryResetRadios()
        tdkTestObj.addParameter("methodName","factoryResetRadios");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
	    tdkTestObj.setResultStatus("SUCCESS");
	    time.sleep(5);
            details_Enable0_reset = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"0","getChannelBandwidth");
            Channel_Bandwidth_0_reset = details_Enable0_reset.split(":")[1].strip(" ");
            details_Enable1_reset = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"0","getChannelBandwidth");
            Channel_Bandwidth_1__reset = details_Enable1_reset.split(":")[1].strip(" ");


            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            expectedresult="SUCCESS";
            defaults= "sh %s/tdk_utility.sh parseConfigFile DEFAULT_CHANNEL_BANDWIDTH" %TDK_PATH;
            print defaults;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", defaults);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            defaultValues = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and defaultValues!= "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 7: Should get the values from properties file"
                print "ACTUAL RESULT 7:Default values from properties file:%s" %defaultValues;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                List= defaultValues.split(",");
                print List[0]
                print List[1]

            if Channel_Bandwidth_0_reset== List[0] and Channel_Bandwidth_1__reset  == List[1]:
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP 1:To invoke wifi_factoryResetRadio() api and check whether the ChannelBandwidth  for 2.4GHz and 5 Ghz has default values";
                print"EXPECTED RESULT 1: ChannelBandwidth  for 2.4GHz and 5 Ghz   must have default values";
                print"ACTUAL RESULT 1:ChannelBandwidth  for 2.4GHz and 5 Ghz has default values";
                print"[TEST EXECUTION RESULT 1]:SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP 1:To invoke wifi_factoryResetRadio() api and check whether the ChannelBandwidth  for 2.4GHz and 5 Ghz has default values";
                print"EXPECTED RESULT 1:ChannelBandwidth  for 2.4GHz and 5 Ghz must have default values";
                print"ACTUAL RESULT 1:ChannelBandwidth  for 2.4GHz and 5 Ghz does not have default values";
                print"[TEST EXECUTION RESULT 1]:FAILURE"
            #Reverting the values back to initial values
            print "REVERTING  CHANNEL BANDWIDTH  TO INITIAL VALUE";
            InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,Channel_Bandwidth_initial0,"setChannelBandwidth");
            InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,Channel_Bandwidth_initial1,"setChannelBandwidth");
            details_interval0_reset = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,"0","getRadioGuardInterval");
            GuardInterval0 = details_interval0_reset.split(":")[1].strip(" ");
            details_interval1_reset = InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,"0","getRadioGuardInterval");
            GuardInterval1 = details_interval1_reset.split(":")[1].strip(" ");
            if GuardInterval0 == "Auto" and GuardInterval1 == "Auto" :
                tdkTestObj.setResultStatus("SUCCESS");
                print"TEST STEP 2:To invoke wifi_factoryResetRadios() api and check whether the GuardInterval is Auto for both 2.4GHz and 5GHz";
                print"EXPECTED RESULT 2:GuardInterval should be Auto for 2.4GHz and 5GHz";
                print"ACTUAL RESULT 2:GuardInterval value is Auto for 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT 2]:SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"TEST STEP 2:To invoke wifi_factoryResetRadios() api and check whether the GuardInterval is Auto for both 2.4GHz and 5GHz";
                print"EXPECTED RESULT 2:GuardInterval should be Auto for 2.4GHz and 5GHz";
                print"ACTUAL RESULT 2:GuardInterval value is NOT Auto for 2.4GHz and 5GHz";
                print"[TEST EXECUTION RESULT 2]:FAILURE";
            #Reverting the values back to initial values
            print "REVERTING GUARDINTERVAL TO INITIAL VALUE";
            InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx0,GuardInterval_initial0,"setRadioGuardInterval");
            InvokeGetSetMethod('WIFIHAL_GetOrSetParamStringValue',idx1,GuardInterval_initial1,"setRadioGuardInterval");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"wifi_factoryResetRadios() operation";
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");