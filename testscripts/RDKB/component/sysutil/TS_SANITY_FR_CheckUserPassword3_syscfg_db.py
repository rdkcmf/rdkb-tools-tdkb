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
  <name>TS_SANITY_FR_CheckUserPassword3_syscfg_db</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if admin password from syscfg.db in /tmp and /nvram returns default password after factory reset</synopsis>
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
    <test_case_id>TC_SYSUTIL_21</test_case_id>
    <test_objective>To check if admin password from syscfg.db in /tmp and /nvram returns default password after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3,RPI</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset</input_parameters>
    <automation_approch>1.Initiate factory reset using Device.X_CISCO_COM_DeviceControl.FactoryReset
2.Get default password from properties file.
3.Using ExecuteCmd(),get user_password_3 from /tmp/syscfg.db
4.Using ExecuteCmd(),get user_password_3 from /nvram/syscfg.db
5.Check if user_password_3 from syscfg.db in /tmp and /nvram and default password are same
6.Responses from the sysutil stub function will be logged in Agent Console log.
7.Test Manager will publish the result in GUI as PASS/FAILURE</automation_approch>
    <except_output>user_password_3 in syscfg.db in /tmp and /nvram should return default password after factory reset</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_FR_CheckUserPassword3_syscfg_db</test_script>
    <skipped>No</skipped>
    <release_version>M66</release_version>
    <remarks/>
  </test_cases>
  <script_tags>
    <script_tag>BASIC</script_tag>
  </script_tags>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from tdkbVariables import *;


#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_SANITY_FR_CheckUserPassword3_syscfg_db');
sysobj.configureTestCase(ip,port,'TS_SANITY_FR_CheckUserPassword3_syscfg_db');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    #save device's current state before it goes for reboot
    sysobj.saveCurrentState();

    #Initiate Factory reset before checking the default value
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        sysobj.restorePreviousStateAfterReboot();
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        command= "sh %s/tdk_utility.sh parseConfigFile DEFAULT_ADMIN_LOGIN_PASSWORD" %TDK_PATH;
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command", command);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        default_password = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd= "cat /tmp/syscfg.db  | grep -i user_password_3";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        user_password_3_details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd= "cat /nvram/syscfg.db  | grep -i user_password_3";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        user_password_3_bkup_details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if user_password_3_details != "" and user_password_3_bkup_details != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Check if user_password_3 entry is present in syscfg.db in /tmp and /nvram";
            print "EXPECTED RESULT 2: user_password_3 entry is present in syscfg.db in /tmp and /nvram";
            print "ACTUAL RESULT 2: user_password_3 present in syscfg.db in /tmp and /nvram are : %s, %s" %(user_password_3_details, user_password_3_bkup_details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            user_password=(user_password_3_details.split('='))
            user_password_3 = user_password[1]
            user_password=(user_password_3_bkup_details.split('='))
            user_password_3_bkup = user_password[1]
            if user_password_3 == user_password_3_bkup and user_password_3 == default_password:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check user_password_3 from syscfg.db in /tmp and /nvram and default password are same";
                print "EXPECTED RESULT 3: user_password_3 from syscfg.db in /tmp and /nvram and default password should be same";
                print "ACTUAL RESULT 3:user_password_3 from syscfg.db in /tmp and /nvram and default password are same : %s" %user_password_3;
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Check user_password_3 from syscfg.db in /tmp and /nvram and default password are same";
                print "EXPECTED RESULT 3: user_password_3 from syscfg.db in /tmp and /nvram and default password should be same";
                print "ACTUAL RESULT 3:user_password_3 from syscfg.db in /tmp and /nvram and default password are not same : %s" %user_password_3;
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if user_password_3 entry is present in syscfg.db in /tmp and /nvram";
            print "EXPECTED RESULT 2: user_password_3 entry is present in syscfg.db in /tmp and /nvram";
            print "ACTUAL RESULT 2: user_password_3 entry is not present in syscfg.db in /tmp and /nvram";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
