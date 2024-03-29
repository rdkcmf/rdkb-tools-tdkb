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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the default Beacon Period (Time interval between transmitting beacons) for 2.4GHz radio using wifi_getRadioBeaconPeriod HAL API and validate the same</synopsis>
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
    <test_case_id>TC_WIFIHAL_46</test_case_id>
    <test_objective>To get the default Beacon Period value (Time interval between transmitting beacons) for 2.4GHz radio using wifi_getRadioBeaconPeriod HAL API and validate the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3. XB6, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioBeaconPeriod()</api_or_interface_used>
    <input_parameters>methodName   :   getRadioBeaconPeriod
radioIndex   :   0</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested (WIFIHAL_GetOrSetParamUIntValue  - func name - "If not exists already" WIFIHAL - module name Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod.py)
3.Execute the generated Script(TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod.py) using execution page of  Test Manager GUI
4.wifihalstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIHAL_GetOrSetParamUIntValue through registered TDK wifihalstub function along with necessary Path Name as arguments
5.The default beacon Period value is parsed from tdk platform properties file
6. Do a factory reset of the DUT
7.WIFIHAL_GetOrSetParamUIntValue function will call Ccsp Base Function named "ssp_WIFIHALGetOrSetParamUIntValue", that inturn will call WIFIHAL Library Function wifi_getRadioBeaconPeriod() function
8.The value received form WIFIHAL_GetOrSetParamUIntValue and the one received from platform properties should be same.
9.Response(s)(printf) from TDK Component,Ccsp Library function and wifihalstub would be logged in Agent Console log based on the debug info redirected to agent console
10.wifihalstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result
11.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifihalstub</automation_approch>
    <expected_output>CheckPoint
1:wifi_getRadioBeaconPeriod log and the value received by platform properties file  from DUT should be available in Agent Console LogCheckPoint
2:TDK agent Test Function will log the test case result as PASS based on API response CheckPoint
3:Test Manager GUI will publish the result as SUCCESS in Execution page"""</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
pamobj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod');
pamobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioBeaconPeriod');

loadmodulestatus =obj.getLoadModuleResult();
sysutilmodulestatus =obj1.getLoadModuleResult();
pamloadmodulestatus =pamobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[SYSUTIL  LOAD STATUS]  :  %s" %sysutilmodulestatus
print "[PAM LOAD STATUS]  :  %s" %pamloadmodulestatus 

if "SUCCESS" in (loadmodulestatus.upper() and  sysutilmodulestatus.upper() and pamloadmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    pamobj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
	radioIndex = idx
	getMethod = "getRadioBeaconPeriod"
	primitive = 'WIFIHAL_GetOrSetParamUIntValue'
        #Get the default value from properties file
    	tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
    	cmd = "sh %s/tdk_utility.sh parseConfigFile DEFAULT_BEACON_PERIOD" %TDK_PATH;
    	print cmd;
    	expectedresult="SUCCESS";
        tdkTestObj1.addParameter("command", cmd);
        tdkTestObj1.executeTestCase(expectedresult);
        actualresult = tdkTestObj1.getResult();
    	details = ""
    	details = tdkTestObj1.getResultDetails().strip();
    	defaultValue = ""
        defaultValue = details.replace("\\n", ""); 
    	print "Default Beacon Period:",defaultValue
    	if defaultValue != "" and ( expectedresult in  actualresult):
       	    tdkTestObj1.setResultStatus("SUCCESS");
       	    print "TEST STEP 1: Get the default beacon period from tdk_platfrom properties file";
            print "EXPECTED RESULT 1: Should Get the default beacon period form platform properties file";
            print "ACTUAL RESULT 1:The default beacon period from tdk_platform properties file is : %s" % defaultValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            expectedresult="SUCCESS";

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
                print "TEST STEP 2: Initiate factory reset ";
                print "EXPECTED RESULT 2: Should inititate factory reset";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Restore the device state saved before reboot
                pamobj.restorePreviousStateAfterReboot()
       
                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                if expectedresult in actualresult:
                    print "getRadioBeaconPeriod function successful: %s"%details
                    tdkTestObj.setResultStatus("SUCCESS");
                    beaconPeriodValue = details.split(":")[1].strip()
                    if int(beaconPeriodValue) == int(defaultValue):
                        tdkTestObj.setResultStatus("SUCCESS");
                 	print "TEST STEP 3: Compare the default value with received beacon period";
                 	print "EXPECTED RESULT 3:Default value and  Received beacon period should be equal";
                 	print "ACTUAL RESULT 3: Default value and  Received beacon period are equal: %s"%beaconPeriodValue;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Compare the default value with received beacon period";
                  	print "EXPECTED RESULT 3:Default value and  Received beacon period should be equal";
                  	print "ACTUAL RESULT 3: Default value and  Received beacon period are not equal:  %s"%beaconPeriodValue;
                  	print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "getRadioBeaconPeriod function failed";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Initiate factory reset ";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj1.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the default beacon period from tdk_platfrom properties file";
            print "EXPECTED RESULT 1: Should Get the default beacon period form platform properties file";
            print "ACTUAL RESULT 1: Failed to get the default beacon period : %s" % defaultValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("wifihal");
    obj1.unloadModule("sysutil");
    pamobj.unloadModule("pam");
else:
    print "Failed to load wifi module/ sysutil module";
    obj.setLoadModuleStatus("FAILURE");

