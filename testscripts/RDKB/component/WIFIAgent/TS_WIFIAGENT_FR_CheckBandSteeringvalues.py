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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_FR_CheckBandSteeringvalues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if bandsteering default values are restored after factory reset</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_69</test_case_id>
    <test_objective>Check if bandsteering default values are restored after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable
Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.IdleInactiveTime
Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.IdleInactiveTime
Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.OverloadInactiveTime
Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.OverloadInactiveTime
Device.WiFi.X_RDKCENTRAL-COM_BandSteering.APGroup</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Do a factory reset and get the bandsteering values
3. Check if it is restored to default value
4. Unload wifiagent module</automation_approch>
    <expected_output>After factory reset,bandsteering should be restored to default values</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_FR_CheckBandSteeringvalues</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
import tdkutility;
from tdkutility import *
from tdkbVariables import *


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_WIFIAGENT_FR_CheckBandSteeringvalues');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_FR_CheckBandSteeringvalues');
pamobj.configureTestCase(ip,port,'TS_WIFIAGENT_FR_CheckBandSteeringvalues');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =pamobj.getLoadModuleResult();


if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    obj.saveCurrentState();
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
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();
        time.sleep(180);

        paramList=["Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.IdleInactiveTime", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.IdleInactiveTime","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.OverloadInactiveTime","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.OverloadInactiveTime","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.APGroup"]
        print "TEST STEP 2: Should get the bandsteering values"
        tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
        bandSteeringEnable = orgValue[0]
        bandSteeringIdleInactiveTime1 = orgValue[1]
        bandSteeringIdleInactiveTime2 = orgValue[2]
        bandSteeringOverloadInactiveTime1 = orgValue[3]
        bandSteeringOverloadInactiveTime2 = orgValue[4]
        bandSteeringAPGroup = orgValue[5]


        if expectedresult in status and bandSteeringEnable != "" and bandSteeringIdleInactiveTime1 != "" and bandSteeringIdleInactiveTime2 != "" and bandSteeringOverloadInactiveTime1 != "" and  bandSteeringOverloadInactiveTime2 != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2:BandSteering Enable status: %s, 2.4GHZ BandSteeringIdleInactiveTime : %s ,5GHZ BandSteeringIdleInactiveTime :  %s ,2.4GHZ  BandSteeringOverloadInactiveTime :%s, 5GHZ BandSteeringOverloadInactiveTime: %s,BandSteeringAPGroup: %s" %(bandSteeringEnable,bandSteeringIdleInactiveTime1,bandSteeringIdleInactiveTime2,bandSteeringOverloadInactiveTime1,bandSteeringOverloadInactiveTime2,bandSteeringAPGroup);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            bandSteeringValues= "sh %s/tdk_utility.sh parseConfigFile DEFAULT_BANDSTEERING_VALUES" %TDK_PATH;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", bandSteeringValues);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            bandSteeringValuesList = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Should get the values from properties file"
                print "ACTUAL RESULT 3:Band steering value from properties file:%s" %bandSteeringValuesList;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                details=[]
                def Convert(string):
                    li = list(string.split("],"))
                    c=li
                    return li
                c=Convert(bandSteeringValuesList)
                for x in range(len(c)):
                    if '[' in c[x]:
                        if ']' in c[x]:
                                e=c[x].strip('[')
                                details.append(e.strip(']'))
                        else:
                                details.append(c[x].strip('['))

                if orgValue == details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Should get default bandsteering values after factory reset"
                    print "ACTUAL RESULT 4:Restored to default bandsteering values after factory reset";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Should get default bandsteering values after factory reset"
                    print "ACTUAL RESULT 4:Failed to restore to default bandsteering values after factory reset";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Should get the values from properties file"
                print "ACTUAL RESULT 3:Failed to get value from properties file ";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:Should get bandsteering values after factory reset";
            print "ACTUAL RESULT 2:Failed to get bandsteering values after factory reset";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("sysutil");
    pamobj.unloadModule("pam");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";


