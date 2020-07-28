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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TDKB_PlatformHAL_WEBPA_GetAllValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TDKB_HALStub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if all TR181 parameter values of Platform HAL (using WEBPA) matching with its corresponding HAL API Values</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TDKB_HAL_12</test_case_id>
    <test_objective>To Check if all TR181 parameter values of Platform HAL (using WEBPA) matching with its corresponding HAL API Values</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>TDK test agent should be running
PlatformHAL module's parameter xml should be available</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>
1. Load tdkbtr181 module, hal platform module and sysutil module
2. Set the validation type as WEBPA
3. Invoke prerequisite() by passing setup type as WEBPA and make sure all prerequisite are met
4. Invoke parseXML() by passing PlatformHAL as module name and get the Parameters and HAL API list
5. Invoke getTR181andHALAPIValue() by passing PlatformHAL as module name
6. Check if all TR181 parameters values are matching with HAL API values
7. Display the final status of get and the list of failed parameters, if any
8. Unload modules</automation_approch>
    <expected_output>All TR181 parameter values should match with its corresponding HAL API Values
</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbhal</test_stub_interface>
    <test_script>TDKB_PlatformHAL_WEBPA_GetAllValues</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
import xml.etree.ElementTree as ET
import os
from tdkbVariables import *;
import webpaUtility;
from webpaUtility import *;
import tdkbHalTr181Utility;

objhal = tdklib.TDKScriptingLibrary("halplatform","1");
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
objhal.configureTestCase(ip,port,'TDKB_PlatformHAL_WEBPA_GetAllValues');
obj.configureTestCase(ip,port,'TDKB_PlatformHAL_WEBPA_GetAllValues');
sysobj.configureTestCase(ip,port,'TDKB_PlatformHAL_WEBPA_GetAllValues');

#Get the result of connection with test component and DUT
loadmodulestatus1 = objhal.getLoadModuleResult();
loadmodulestatus2 = obj.getLoadModuleResult();
loadmodulestatus3 = sysobj.getLoadModuleResult();
print "[MoCA HAL LIB LOAD STATUS]  :  %s " %loadmodulestatus1 ;
print "[TDKBTR181 LIB LOAD STATUS]  :  %s " %loadmodulestatus2 ;
print "[SYSUTIL LIB LOAD STATUS]  :  %s " %loadmodulestatus3 ;

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper() and loadmodulestatus3.upper()):
    #Set the result status of execution
    objhal.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    setup_type = "WEBPA"
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    mainFunctionFailedParams = [];
    prerequisite_status = tdkbHalTr181Utility.prerequisite(sysobj,setup_type);
    if prerequisite_status == 1:
        print "Pre-requisite for Setup Type %s is SUCCESS"%setup_type

        xmlName = tdkbHalTr181Utility.getXMLNameUsingDeviceType(sysobj,"PlatformHAL");

        if xmlName != "Error":
            paramList,HALAPIList,tr181_ExpRes,hal_ExpRes = tdkbHalTr181Utility.parseXML(xmlName,"PlatformHAL",setup_type);

            for plist in range (0,len(paramList)):
                mainFunctionFailedParams = tdkbHalTr181Utility.getTR181andHALAPIValue(obj,objhal,sysobj,paramList[plist],HALAPIList[plist],tr181_ExpRes[plist],hal_ExpRes[plist],"PlatformHAL",setup_type);

            print "Failed Parameters are %s"%mainFunctionFailedParams;

        else:
            print "Failed to get the XML Name"
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "Pre-requisite Failed";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
    objhal.unloadModule("halplatform");
else:
    print "Failed to load PlatformHAL/TDKB-TR181 module";
    obj.setLoadModuleStatus("FAILURE");
    objhal.setLoadModuleStatus("FAILURE")
    sysobj.setLoadModuleStatus("FAILURE")
    print "Module loading failed";

