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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_SetBandSteeringValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set bandsteering values and get the values and validate them</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_70</test_case_id>
    <test_objective>To set bandsteering values and get the values and validate them</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.UtilizationThreshold,Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.RSSIThreshold, Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.PhyRateThreshold, Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.UtilizationThreshold, Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.RSSIThreshold,Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.PhyRateThreshold</input_parameters>
    <automation_approch>1. Load wifiagent module
2.Get the current bandsteering values
3.Set the bandsteering values
4.Get the bandsteering values after set
5.Validate the set and get values
6.Revert the  bandsteering values
7. Unload wifiagent module</automation_approch>
    <expected_output>Set and get values of BandSteering should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetBandSteeringValues</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
import tdkutility
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetBandSteeringValues');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_SetBandSteeringValues');

set_UtilzationThreshold1 = "80";
set_SignalThreshold1 = "10";
set_PhysicalRateThreshold1 = "60000";
set_UtilzationThreshold2 = "60";
set_SignalThreshold2 = "20";
set_PhysicalRateThreshold2 = "5000";
set_ThresholdValues = ['80','10','60000','60','20','5000']


#Get the result of connection with test component and DUT
loadmodulestatus1=obj.getLoadModuleResult();
loadmodulestatus2=obj1.getLoadModuleResult();


if "SUCCESS" in loadmodulestatus1.upper() and  "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('TADstub_Get');

    paramList=["Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.UtilizationThreshold" ,"Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.RSSIThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.PhyRateThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.UtilizationThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.RSSIThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.PhyRateThreshold"]
    print "TEST STEP 1: Should get the bandsteering values"
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "" and orgValue[3] != "" and orgValue[4] != "" and orgValue[5] != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1:  2.4GHZ BandSteering UtilizationThreshold: %s,2.4GHZ BandSteering RSSIThreshold: %s, 2.4GHZ BandSteering PhyRateThreshold  : %s ,5GHZ BandSteering UtilizationThreshold: %s,5GHZ BandSteering RSSIThreshold: %s,5GHZ BandSteering PhyRateThreshold  : %s  " %(orgValue[0],orgValue[1],orgValue[2],orgValue[3],orgValue[4],orgValue[5]);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
        tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.UtilizationThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.RSSIThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.PhyRateThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.UtilizationThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.RSSIThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.PhyRateThreshold|%s|int" %(set_UtilzationThreshold1,set_SignalThreshold1,set_PhysicalRateThreshold1,set_UtilzationThreshold2,set_SignalThreshold2,set_PhysicalRateThreshold2));
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Should set bandsteering values"
            print "ACTUAL RESULT 2: %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS";
            paramList=["Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.UtilizationThreshold","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.RSSIThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.PhyRateThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.UtilizationThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.RSSIThreshold", "Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.PhyRateThreshold"]
            print "TEST STEP 3: Should get the bandsteering values after set"
            tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)

            if expectedresult in status and setValue[0] != "" and setValue[1] != "" and setValue[2] != "" and setValue[3] != "" and setValue[4] != "" and setValue[5] != "" :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3:2.4GHZ BandSteering UtilizationThreshold: %s,2.4GHZ BandSteering RSSIThreshold: %s, 2.4GHZ BandSteering PhyRateThreshold  : %s ,5GHZ BandSteering UtilizationThreshold: %s,5GHZ BandSteering RSSIThreshold: %s,5GHZ BandSteering PhyRateThreshold  : %s  " %(setValue[0],setValue[1],setValue[2],setValue[3],setValue[4],setValue[5]);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                if set_ThresholdValues == setValue:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4:Set and get values should be same"
                    print "ACTUAL RESULT 4:Set and get bandsteering values are validated successfully" ;
                    print "TEST EXECUTION RESULT :SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4:Set and get values should be same"
                    print "ACTUAL RESULT 4:Set and get bandsteering values are not same" ;
                    print "TEST EXECUTION RESULT 4:FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Should get bandsteering values after set";
                print "ACTUAL RESULT 3:Failed to get  bandsteering values after set";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.UtilizationThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.RSSIThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.PhyRateThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.UtilizationThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.RSSIThreshold|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.2.PhyRateThreshold|%s|int" %(orgValue[0],orgValue[1],orgValue[2],orgValue[3],orgValue[4],orgValue[5]));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP:Should revert bandsteering values"
                print "ACTUAL RESULT: %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Should revert bandsteering values"
                print "ACTUAL RESULT: %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Should set bandsteering values"
            print "ACTUAL RESULT 2: %s" %details;
            print "TEST EXECUTION RESULT :FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Should get Bandsteering values"
        print "ACTUAL RESULT 1:Failed to get Bandsteering values ";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

