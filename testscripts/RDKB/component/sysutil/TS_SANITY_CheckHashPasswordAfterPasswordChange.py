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
  <name>TS_SANITY_CheckHashPasswordAfterPasswordChange</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether hash_password_3 from syscfg.db in /tmp returns hashed password if the default admin password is changed</synopsis>
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
    <test_case_id>TC_SYSUTIL_25</test_case_id>
    <test_objective>To check whether hash_password_3 from syscfg.db in /tmp is changed if the default admin password is changed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3,RPI</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Users.User.3.Password</input_parameters>
    <automation_approch>1.Check if user_password_3 or hash_password_3 entry is present in syscfg.db in /tmp
2.If hash_password_3 entry is present in syscfg.db  in /tmp, get hash_password_3 from syscfg.db in /tmp
3.Change the password and get hash_password_3 from syscfg.db in /tmp
4.Check if hash_password_3 is changed in syscfg.db in /tmp after password change
5.If user_password_3 entry is present in syscfg.db in /tmp, change the password
6.After changing the password,get hash_password_3 from syscfg.db in /tmp
7.Change the password and get hash_password_3 from syscfg.db in /tmp
8..Check if hash_password_3 is changed in syscfg.db in /tmp after password change
8.Responses from the sysutil stub function will be logged in Agent Console log.
9.Test Manager will publish the result in GUI as PASS/FAILURE</automation_approch>
    <except_output>hash_password_3 from syscfg.db in /tmp should be changed if the default admin password is changed</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckHashPasswordAfterPasswordChange</test_script>
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
import time;
from tdkbVariables import *;
import tdkutility;

#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_SANITY_CheckHashPasswordAfterPasswordChange');
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckHashPasswordAfterPasswordChange');

def getHashPassword(cmd):
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    hash_password_3_details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    return (tdkTestObj,hash_password_3_details);

def checkHashPassword(hash_password_3, hash_password_3_change):
    if hash_password_3 != hash_password_3_change :
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Check if hash_password_3 value in syscfg.db in /tmp is changed after changing password";
        print "EXPECTED RESULT : hash_password_3 value in syscfg.db in /tmp should be changed after changing password";
        print "ACTUAL RESULT : hash_password_3 value in syscfg.db in /tmp is changed after changing password";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Check if hash_password_3 value in syscfg.db in /tmp is changed after changing password";
        print "EXPECTED RESULT : hash_password_3 value in syscfg.db in /tmp should be changed after changing password";
        print "ACTUAL RESULT : hash_password_3 value in syscfg.db in /tmp is not changed after changing password";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";
    print "Invoking function to get hash password"
    cmd= "cat /tmp/syscfg.db  | grep -i hash_password_3";
    tdkTestObj,hash_password_3_details = getHashPassword(cmd);

    if hash_password_3_details != "" :
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check if hash_password_3 entry is present in syscfg.db in /tmp";
        print "EXPECTED RESULT 1: hash_password_3 entry should be present in syscfg.db in /tmp";
        print "ACTUAL RESULT 1: hash_password_3 entry is present in syscfg.db in /tmp : %s" %(hash_password_3_details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        hash_password=(hash_password_3_details.split('='))
        hash_password_3 = hash_password[1]

        #Change the admin password
        password = "testPassword1"
        tdkutility.changeAdminPassword(pamobj,password)

        print "Invoking function to get hash password"
        cmd= "cat /tmp/syscfg.db  | grep -i hash_password_3";
        tdkTestObj,hash_password_3_change_details = getHashPassword(cmd);

        if hash_password_3_change_details != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Check if hash_password_3 entry is present in syscfg.db in /tmp";
            print "EXPECTED RESULT 2:Password got changed. hash_password_3 entry should be present in syscfg.db in /tmp";
            print "ACTUAL RESULT 2: Password got changed.hash_password_3 entry is present in syscfg.db in /tmp";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            hash_password=(hash_password_3_change_details.split('='))
            hash_password_3_change = hash_password[1]
            #Function to check if hash_password_3 is different after changing the password
            print "Invoking function to check hash_password_3 is changed after password is changed";
            checkHashPassword(hash_password_3,hash_password_3_change);
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if hash_password_3 entry is present in syscfg.db in /tmp";
            print "EXPECTED RESULT 2:Password got changed. hash_password_3 entry should be present in syscfg.db in /tmp";
            print "ACTUAL RESULT 2: Password got changed.hash_password_3 entry is not present in syscfg.db in /tmp";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"

        #Revert password to default password
        password = "password"
        tdkutility.changeAdminPassword(pamobj,password)
    else:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check if user_password_3 entry is present in syscfg.db in /tmp";
        print "EXPECTED RESULT 1: user_password_3 entry is present in syscfg.db in /tmp";
        print "ACTUAL RESULT 1: user_password_3 entry is present in syscfg.db in /tmp";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #Change the admin password
        password = "testPassword1"
        tdkutility.changeAdminPassword(pamobj,password);

        print "Invoking function to get hash password"
        cmd= "cat /tmp/syscfg.db  | grep -i hash_password_3";
        tdkTestObj,hash_password_3_details = getHashPassword(cmd);

        if hash_password_3_details != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Check if hash_password_3 entry is present in syscfg.db in /tmp";
            print "EXPECTED RESULT 3: hash_password_3 entry should be present in syscfg.db in /tmp";
            print "ACTUAL RESULT 3: hash_password_3 entry is present in syscfg.db in /tmp";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            hash_password=(hash_password_3_details.split('='))
            hash_password_3 = hash_password[1]

            #Change the admin password
            password = "testPassword2"
            tdkutility.changeAdminPassword(pamobj,password);

            print "Invoking function to get hash password"
            cmd= "cat /tmp/syscfg.db  | grep -i hash_password_3";
            tdkTestObj,hash_password_3_change_details = getHashPassword(cmd);

            if hash_password_3_change_details != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Check if hash_password_3 entry is present in syscfg.db in /tmp";
                print "EXPECTED RESULT 4:Password got changed. hash_password_3 entry should be present in syscfg.db in /tmp";
                print "ACTUAL RESULT 4: Password got changed.hash_password_3 entry is present in syscfg.db in /tmp: %s" %(hash_password_3_change_details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
                hash_password=(hash_password_3_change_details.split('='))
                hash_password_3_change = hash_password[1]
                print "Invoking function to check hash_password_3 is changed after password is changed";
                checkHashPassword(hash_password_3,hash_password_3_change);
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Check if hash_password_3 entry is present in syscfg.db in /tmp";
                print "EXPECTED RESULT 4:Password got changed. hash_password_3 entry should be present in syscfg.db in /tmp";
                print "ACTUAL RESULT 4: Password got changed.hash_password_3 entry is not present in syscfg.db in /tmp";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Check if hash_password_3 entry is present in syscfg.db in /tmp";
            print "EXPECTED RESULT 3: hash_password_3 entry should be present in syscfg.db in /tmp";
            print "ACTUAL RESULT 3: hash_password_3 entry is not present in syscfg.db in /tmp";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"

        #Revert the admin password to default password
        password ="password"
        tdkutility.changeAdminPassword(pamobj,password)

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
