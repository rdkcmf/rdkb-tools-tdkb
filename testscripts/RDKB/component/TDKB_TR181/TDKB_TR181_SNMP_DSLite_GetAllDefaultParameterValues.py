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
  <name>TDKB_TR181_SNMP_DSLite_GetAllDefaultParameterValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TDKB_TR181Stub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check via SNMP, whether all tr181 parameters of DSLite are having the default values after factory reset</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TDKB_TR181_106</test_case_id>
    <test_objective>Check via SNMP, whether all tr181 parameters of DSLite  are having the default values after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>TDK test agent should be running
DSLite  module's parameter xml should be available</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load tdkbtr181 module and sysutil module
2. Set the validation type as SNMP
3. Set the factoryReset flag as true
4. Do the factory reset of device via SNMP
5. Invoke getAllParams() by passing DSLite as module name
6. Check if all parameters are having their default values
7. Display the final status of get and the list of failed parameters, if any
8. Unload modules</automation_approch>
    <expected_output>Get operation for default values on all DSLite parameters via SNMP should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TDKB_TR181_SNMP_DSLite_GetAllDefaultParameterValues</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkbSetAllParams
from tdkbVariables import *;
import snmplib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TDKB_TR181_SNMP_DSLite_GetAllDefaultParameterValues');
obj1.configureTestCase(ip,port,'TDKB_TR181_SNMP_DSLite_GetAllDefaultParameterValues');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);

    #save device's current state before it goes for reboot
    obj1.saveCurrentState();
    tdkTestObj.setResultStatus("SUCCESS");
    print "TEST STEP : Initiate factory reset ";
    print "EXPECTED RESULT : Should initiate factory reset";

    # Resetting device using snmp command
    #Get the Community String
    communityString = snmplib.getCommunityString(obj1,"snmpset");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj1);
    ########## Script to Execute the snmp command ###########
    actResponse =snmplib.SnmpExecuteCmd("snmpset", communityString, "-v 2c", "1.3.6.1.4.1.17270.50.2.1.1.1002.0 i 1", ipaddress);
    if "INTEGER" in actResponse:
        print "Factory reset : SUCCESS";
        #Restore the device state saved before reboot
        obj1.restorePreviousStateAfterReboot();

        setup_type = "SNMP"
        factoryReset = "true"

        #Invoke the utility function to get and validate the values for all configured tr181 params
        moduleStatus,failedParams = tdkbSetAllParams.getAllParams("DSLite", setup_type, factoryReset, obj, obj1);

        print "Status of DSLite validation is ", moduleStatus, "\n";
        if moduleStatus == "FAILURE":
            print "The failed params are ", failedParams, "\n";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "[Factory Reset] : FAILURE";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

