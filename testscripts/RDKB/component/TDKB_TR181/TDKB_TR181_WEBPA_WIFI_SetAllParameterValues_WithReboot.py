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
  <name>TDKB_TR181_WEBPA_WIFI_SetAllParameterValues_WithReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TDKB_TR181Stub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set all tr181 parameters in WIFI  module using WEBPA and check if the values that are set persist after a reboot.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>140</execution_time>
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
    <test_case_id>TC_TDKB_TR181_94</test_case_id>
    <test_objective>To set all tr181 parameters in WIFI  module using WEBPA and check if the values that are set persist after a reboot.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>TDK test agent should be running
WIFI module's parameter xml should be available</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load tdkbtr181 module and sysutil module
2. Set the validation type as WEBPA
3. Invoke setAllParams() by passing WIFI as module name and rebootTest flag as true
4. Do the reboot
5. Check if all parameters are having set value and revert parameters to original values
6. Display the final status of set and the list of failed parameters, if any
7. Unload modules</automation_approch>
    <expected_output>Parameters should persist on reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdktr181</test_stub_interface>
    <test_script>TDKB_TR181_WEBPA_WIFI_SetAllParameterValues_WithReboot</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkbSetAllParams
from tdkbVariables import *;
import webpaUtility;
from webpaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TDKB_TR181_WEBPA_WIFI_SetAllParameterValues_WithReboot');
obj1.configureTestCase(ip,port,'TDKB_TR181_WEBPA_WIFI_SetAllParameterValues_WithReboot');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj1);
    if "SUCCESS" in preRequisiteStatus:
        print "The module to test is: WIFI";
        setup_type = "WEBPA"

        #Invoke the utility function to set and validate the values for all configured tr181 params
        moduleStatus,failedParams= tdkbSetAllParams.setAllParams("WIFI", setup_type, obj, obj1,"true");

        print "Status of WIFI module is : ",moduleStatus, "\n";
        if moduleStatus == "FAILURE":
                print "The failed params are ", failedParams, "\n";
                tdkTestObj.setResultStatus("FAILURE");
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

