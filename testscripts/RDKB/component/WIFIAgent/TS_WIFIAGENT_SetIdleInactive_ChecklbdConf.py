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
  <name>TS_WIFIAGENT_SetIdleInactive_ChecklbdConf</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if updating band steering idleactive time and overloadinactive time is reflected in lbd.conf</synopsis>
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
    <test_case_id>TC_WIFIAGENT_67</test_case_id>
    <test_objective>To check if updating band steering idleactive time and overloadinactive time is reflected in lbd.conf</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable,Device.WiFi.SSID.1.SSID,Device.WiFi.SSID.2.SSID</input_parameters>
    <automation_approch>1. Load wifiagent module
2.GET xfnity public values,WIFI SSID names,bandsteering enable status
3.Enable xfinity public wifi and band steering enable
4.Set same SSID for both 2.4GHZ and 5GHZ
5.Check if lbd.conf file is present
6.Update the idleactive time and and overloadinactive time
7.Check if values are updated in lbd.conf
8.Revert the values
9. Unload wifiagent module</automation_approch>
    <expected_output>Updating bandsteering idleactive time and overloadinactive time should be reflected in lbd.conf</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetIdleInactive_ChecklbdConf</test_script>
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
from xfinityWiFiLib import *
import tdkutility;
from tdkutility import *
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2 = tdklib.TDKScriptingLibrary("sysutil","1");
obj3 = tdklib.TDKScriptingLibrary("tad","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetIdleInactive_ChecklbdConf');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_SetIdleInactive_ChecklbdConf');
obj2.configureTestCase(ip,port,'TS_WIFIAGENT_SetIdleInactive_ChecklbdConf');
obj3.configureTestCase(ip,port,'TS_WIFIGENT_SetIdleInactive_ChecklbdConf');


#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =obj2.getLoadModuleResult();
loadmodulestatus4 =obj3.getLoadModuleResult();

SSID1 = "TESTSSID1"
idleInactveTime = 11
overloadInactiveTime = 11


if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper() and "SUCCESS" in loadmodulestatus4.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Get current values of public wifi params
    expectedresult="SUCCESS";
    tdkTestObj,actualresult,orgValue = getPublicWiFiParamValues(obj);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj3.createTestStep('TADstub_Get');

        paramList=["Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable", "Device.WiFi.SSID.1.SSID", "Device.WiFi.SSID.2.SSID","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.IdleInactiveTime","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.OverloadInactiveTime"]

        tdkTestObj,status,currValue = getMultipleParameterValues(obj3,paramList)
        if ((expectedresult in status) and (currValue[0] and currValue[1] and currValue[2] and currValue[3] and currValue[4]) != ""):
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the bandsteering enable status,SSID names ,IdleInActiveTime and OverloadInactiveTime";
            print "ACTUAL RESULT 2:Enable status:%s 2.4GHZ SSID:%s 5GHZ SSID:%s IdleInactiveTime:%s OverloadInactiveTime:%s" %(currValue[0],currValue[1],currValue[2],currValue[3],currValue[4]) ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Set values to enable public wifi
            setvalues = ["44","68.86.15.199","68.86.15.171","true","true","true"];
            tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,setvalues);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Enable public wifi"
                print "ACTUAL RESULT 3:%s" %details
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable|true|bool|Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.IdleInactiveTime|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.OverloadInactiveTime|%s|int|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(SSID1,SSID1,idleInactveTime,overloadInactiveTime));
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Set Bandsteering enable status,WIFI 2.4GHZ and 5GHZ SSID, IdleInactiveTime and OverloadInactiveTime"
                    print "ACTUAL RESULT 4 : %s" %details;
                    print "TEST EXECUTION RESULT :SUCCESS";
                    tdkTestObj = obj2.createTestStep('ExecuteCmd');
                    cmd = "[ -f /tmp/lbd.conf ] && echo \"File exist\" || echo \"File does not exist\"";
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if details == "File exist":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5:lbd conf file should be present";
                        print "ACTUAL RESULT 5:lbd conf file is present";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        cmd = "cat /tmp/lbd.conf | grep InactIdleThreshold -i";
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                        if expectedresult in actualresult and "11" in details:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6:Check if InactIdleThreshold is updated in conf file";
                            print "ACTUAL RESULT 6:IdleInactiveTime is updated in conf file :%s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            cmd = "cat /tmp/lbd.conf | grep InactOverloadThreshold -i";
                            tdkTestObj.addParameter("command",cmd);
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                            if expectedresult in actualresult and "13" in details:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7:Check if InactOverloadThreshold is updated in conf file ";
                                print "ACTUAL RESULT 7:InactOverloadThreshold is updated in conf file :%s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 7:Check if InactOverloadThreshold is updated in conf file ";
                                print "ACTUAL RESULT 7:InactOverloadThreshold is not updated in conf file ";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6:Check if InactIdleThreshold is updated in conf file";
                            print "ACTUAL RESULT 6:InactIdleThreshold is not updated in conf file :%s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Check if qualcomm bandsteering file is present";
                        tdkTestObj = obj2.createTestStep('ExecuteCmd');
                        cmd = "[ -f /rdklogs/logs/qtn_bsa.log ] && echo \"File exist\" || echo \"File does not exist\"";
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                        if details == "File exist":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6:qualcomm bandsteering is present";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6:qualcomm bandsteering and lbd.conf file is not present";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                    tdkTestObj.addParameter("paramList","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable|%s|bool|Device.WiFi.SSID.1.SSID|%s|string|Device.WiFi.SSID.2.SSID|%s|string|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.IdleInactiveTime|%s|int|Device.WiFi.X_RDKCENTRAL-COM_BandSteering.BandSetting.1.OverloadInactiveTime|%s|int|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(currValue[0],currValue[1],currValue[2],currValue[3],currValue[4]));
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP : Revert Bandsteering enable status,WIFI 2.4GHZ and 5GHZ SSID, IdleInactiveTime and OverloadInactiveTime"
                        print "ACTUAL RESULT  : %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP : Revert Bandsteering enable status,WIFI 2.4GHZ and 5GHZ SSID, IdleInactiveTime and OverloadInactiveTime"
                        print "ACTUAL RESULT  : %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Set Bandsteering enable status,WIFI 2.4GHZ and 5GHZ SSID, IdleInactiveTime and OverloadInactiveTime"
                    print "ACTUAL RESULT 4 : %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE";
                #Revert the values of public wifi params
                tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,orgValue);
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP :Revert the PublicWiFi param values"
                    print "TEST STEP  : Should revert the PublicWiFi values"
                    print "ACTUAL RESULT 4:%s" %details
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP :Revert the PublicWiFi param values"
                    print "TEST STEP : Should revert the PublicWiFi param values"
                    print "ACTUAL RESULT 4:%s" %details
                    print "[TEST EXECUTION RESULT] : FAILURE";

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Enable public wifi"
                print "ACTUAL RESULT 3:%s" %details
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the bandsteering enable status,SSID names ,IdleInActiveTime and OverloadInactiveTime";
            print "ACTUAL RESULT 2:Failed to get Enable status,2.4GHZ SSID,5GHZ SSID, IdleInactiveTime,OverloadInactiveTime";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    obj1.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
    obj3.unloadModule("tad");

else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";



