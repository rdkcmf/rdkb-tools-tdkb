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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TDKB_TR181_SNMP_LOGAGENT_SetAllParameterValues</name>
  <primitive_test_id/>
  <primitive_test_name>TDKB_TR181Stub_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set all tr181 parameters in LOGAGENT module via SNMP</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TDKB_TR181_25</test_case_id>
    <test_objective>To set all tr181 parameters in LOGAGENT module via SNMP</test_objective>
    <test_type>Positive</test_type>
    <test_setup></test_setup>
    <pre_requisite>TDK test agent should be running
LOGAGENT module's parameter xml should be available</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load tdkbtr181 module and sysutil module
2. Set the validation type as SNMP
3. Invoke setAllParams() by passing LOGAGENT as module name
4. Display the final status of set and the list of failed parameters, if any
5. Unload modules</automation_approch>
    <expected_output>Set operation on all LOGAGENT parameters via SNMP should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TDKB_TR181_SNMP_LOGAGENT_SetAllParameterValues</test_script>
    <skipped>No</skipped>
    <release_version>M72</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkbSetAllParams
from tdkbVariables import *;
import os;
import ConfigParser;

#Test component to be tested
obj= tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TDKB_TR181_LOGAGENT_SetAllParameterValues');
obj1.configureTestCase(ip,port,'TDKB_TR181_LOGAGENT_SetAllParameterValues');

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

    print "The module to test is: LOGAGENT";

    setup_type = "SNMP"
    module = "LOGAGENT"

    #Invoke the utility function to set and validate the values for all configured tr181 params
    moduleStatus,failedParams= tdkbSetAllParams.setAllParams(module, setup_type, obj, obj1);

    print "Status of LOGAGENT module test is : ",moduleStatus, "\n";
    if moduleStatus == "FAILURE":
           print "The failed params are ", failedParams, "\n";
           tdkTestObj.setResultStatus("FAILURE");

    obj1.unloadModule("sysutil");
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
