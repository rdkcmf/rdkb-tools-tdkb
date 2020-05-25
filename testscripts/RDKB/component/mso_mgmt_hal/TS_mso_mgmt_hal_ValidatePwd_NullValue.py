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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_mso_mgmt_hal_ValidatePwd_NullValue</name>
  <primitive_test_id/>
  <primitive_test_name>mso_mgmt_hal_MsoValidatePwd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate mso_validatepwd by passing Null pointer as password</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_mso_mgmt_hal_5</test_case_id>
    <test_objective>To validate the Null value  password using mso_validatepwd()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mso_validatepwd()</api_or_interface_used>
    <input_parameters>password</input_parameters>
    <automation_approch>1.Load mso_mgmt_hal module
2.Pass the Null password to mso_validatepwd()
3.Get the status of mso_validatepwd()
4.Check whether status of mso_validatepwd() is Invalid_PWD
5.Unload mso_mgmt_hal module</automation_approch>
    <expected_output>To get the status of mso validate password as Invalid_PWD</expected_output>
    <priority>High</priority>
    <test_stub_interface>MSO_MGMT_HAL</test_stub_interface>
    <test_script>TS_mso_mgmt_hal_ValidatePwd_NullValue</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mso_mgmt_hal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_mso_mgmt_hal_ValidatePwd_NullValue');
Invalid_password = "abc12345678"

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep("mso_mgmt_hal_MsoValidatePwd");
    tdkTestObj.addParameter("paramType", "NULL")
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Status = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and Status == "Invalid_PWD":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Should validate the password for NULL value";
        print "EXPECTED RESULT 1: Should get the status of password validation as Invalid_PWD";
        print "ACTUAL RESULT 1: Status of password validation is %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Should validate the password for NULL value";
        print "EXPECTED RESULT 1:Should get the status of password validation as Invalid_PWD";
        print "ACTUAL RESULT 1: Status of password validation is %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("mso_mgmt_hal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
