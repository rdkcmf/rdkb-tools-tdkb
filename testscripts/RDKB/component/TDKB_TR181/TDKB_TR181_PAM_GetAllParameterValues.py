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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TDKB_TR181_PAM_GetAllParameterValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TDKB_TR181Stub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get all the tr181 parameters of PAM</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_TDKB_TR181_05</test_case_id>
    <test_objective>Get all the tr181 parameters of PAM</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>TDK test agent should be running
PAM module's parameter xml should be available</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load tdkbtr181 module and sysutil module
2. Set the validation type as TDK
3. Invoke getAllParams() by passing PAM as module name
4. Display the final status of get and the list of failed parameters, if any
5. Unload modules</automation_approch>
    <expected_output>Get operation on all PAM parameters should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TDKB_TR181_PAM_GetAllParameterValues</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
import tdkbSetAllParams
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TDKB_TR181_PAM_GetAllParameterValues');
obj1.configureTestCase(ip,port,'TDKB_TR181_PAM_GetAllParameterValues');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj1.createTestStep('ExecuteCmd')
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);

    print "The modules to test is: PAM ";

    setup_type = "TDK"
    factoryReset = "false"

    #Invoke the utility function to get and validate the values for all configured tr181 params
    moduleStatus,failedParams = tdkbSetAllParams.getAllParams("PAM", setup_type, factoryReset, obj, obj1);
        
    print "Status of PAM validation is ", moduleStatus, "\n";
    if moduleStatus == "FAILURE":
        print "The failed params are ", failedParams, "\n";
	tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
