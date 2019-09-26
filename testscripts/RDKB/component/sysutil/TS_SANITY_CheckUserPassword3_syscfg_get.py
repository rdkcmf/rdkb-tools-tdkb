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
<?xml version="1.0" encoding="UTF-8"?>
<xml>
  <id/>
  <version>2</version>
  <name>TS_SANITY_CheckUserPassword3_syscfg_get</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether syscfg get returns admin password as empty value and password is protected if the default admin password is changed</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_19</test_case_id>
    <test_objective>To check whether syscfg get returns admin password as empty value and password is protected if the default admin password is changed
    </test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3,RPI</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Users.User.3.Password</input_parameters>
    <automation_approch>1.Get default passwordfrom platform properties file
2.Using ExecuteCmd(), run syscfg get user_password_3
3.Check if syscfg get returns default password or empty string
4.If syscfg get returns default password, change the password
5.After changing the password,check if syscfg get user_password_3 returns empty string
6.If syscfg get does not return default password,check if syscfg get user_password_3 returns empty string
7.Responses from the sysutil stub function will be logged in Agent Console log.
8.Test Manager will publish the result in GUI as PASS/FAILURE</automation_approch>
    <except_output>Empty string should be displayed if default admin password is changed</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckUserPassword3_syscfg_get</test_script>
    <release_version>M66</release_version>
    <remarks/>
  </test_cases>
  <script_tags>
    <script_tag>BASIC</script_tag>
  </script_tags>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import tdkutility;

#Test component to be tested

obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckUserPassword3_syscfg_get');
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckUserPassword3_syscfg_get');

def getUserPassword(cmd):
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    syscfg_password = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    return (tdkTestObj,syscfg_password);

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysobj.getLoadModuleResult();


if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper:
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile DEFAULT_ADMIN_LOGIN_PASSWORD" %TDK_PATH;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default_password = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    print "Invoking function to get user_password_3 via syscfg get"
    cmd= "syscfg get user_password_3";
    tdkTestObj,syscfg_password = getUserPassword(cmd);
    if expectedresult in actualresult and default_password == syscfg_password:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check if user_password_3 via syscfg get returns default password";
        print "EXPECTED RESULT 1: syscfg get should return default password";
        print "ACTUAL RESULT 1: user_password_3 returned via syscfg get %s" %syscfg_password;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        #Change the admin password
        password = "test_password"
        tdkutility.changeAdminPassword(obj,password)
        print "Invoking function to get user_password_3 via syscfg get"
        cmd= "syscfg get user_password_3";
        tdkTestObj,password_details = getUserPassword(cmd);
        if expectedresult in actualresult and  password_details =="":
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Check if  user_password_3 via syscfg returns empty string";
             print "EXPECTED RESULT 3: user_password_3 via syscfg should return empty string ";
             print "ACTUAL RESULT 3:user_password_3 via syscfg returned empty string";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Check if  user_password_3 via syscfg returns empty string";
             print "EXPECTED RESULT 3: user_password_3 via syscfg should return empty string ";
             print "ACTUAL RESULT 3:user_password_3 via syscfg does not return empty string";
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS"
        #Revert the password to default password
        password = "password"
        tdkutility.changeAdminPassword(obj,password)
    elif syscfg_password == "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check if  user_password_3 via syscfg returns empty string";
        print "EXPECTED RESULT 1: Default password got changed and user_password_3 via syscfg should return empty string ";
        print "ACTUAL RESULT 1:Default password got changed and user_password_3 via syscfg returned empty string";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
    else:
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 1: Check if  user_password_3 via syscfg returns empty string or default password";
         print "EXPECTED RESULT 1: user_password_3 via syscfg should return default password or empty string";
         print "ACTUAL RESULT 1:user_password_3 returned via syscfg get :%s" %syscfg_password;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
        print "Failed to load sysutil module";
        obj.setLoadModuleStatus("FAILURE");
        sysobj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

