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
  <name>TS_SANITY_FR_CheckUserPassword3_syscfg_get</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether syscfg get returns default password after factory reset</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_SYSUTIL_20</test_case_id>
    <test_objective>To check whether syscfg get returns default value after factory reset</test_objective>
    <test_type>Positive</test_type>
    <test_setup></test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset</input_parameters>
    <automation_approch>1.Initiate a factory reset using Device.X_CISCO_COM_DeviceControl.FactoryReset
2.Get the default password from properties file
3.Using ExecuteCmd(), run syscfg get user_password_3
4.Check if syscfg get user_password_3 and default password from configuration file returns same value
5.Responses from the sysutil stub function will be logged in Agent Console log.
6.Test Manager will publish the result in GUI as PASS/FAILURE</automation_approch>
    <except_output>Default password should be returned via syscfg get after factory reset</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_FR_CheckUserPassword3_syscfg_get</test_script>
    <skipped>No</skipped>
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


#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_SANITY_FR_CheckUserPassword3_syscfg_get');
sysobj.configureTestCase(ip,port,'TS_SANITY_FR_CheckUserPassword3_syscfg_get');

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
        #Get the syscfg value after factory reset
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        command= "sh %s/tdk_utility.sh parseConfigFile DEFAULT_ADMIN_LOGIN_PASSWORD" %TDK_PATH;
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command", command);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        default_password = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd= "syscfg get user_password_3";
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        syscfg_password = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult and syscfg_password == default_password:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Admin password via syscfg get";
            print "EXPECTED RESULT 2: Should get the default admin password via syscfg get";
            print "ACTUAL RESULT 2: user_password_3 returned via syscfg get:%s" %syscfg_password;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Admin password via syscfg get ";
            print "EXPECTED RESULT 2: Should get the default admin password via syscfg get";
            print "ACTUAL RESULT 2: user_password_3 returned via syscfg get:%s" %syscfg_password;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
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
