##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>3</version>
  <name>TS_SANITY_SSHtoGateway</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether we are able to do ssh to the gateway device</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_9</test_case_id>
    <test_objective>To check whether we are able to do ssh to the gateway device</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,RPI</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Get the wan interface name from property file
2. Get the wan ip address of the device using ifconfig
3. Try to do ssh to that ip using pxssh
</automation_approch>
    <except_output>SSH to the device should be success</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_SSHtoGateway</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks/>
  </test_cases>
  <script_tags>
    <script_tag>BASIC</script_tag>
  </script_tags>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
from pexpect import pxssh 
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_SSHtoGateway');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile INTERFACE" %TDK_PATH;
    print command;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    interface = tdkTestObj.getResultDetails().strip();
    interface = interface.replace("\\n", "");
    if "Invalid Argument passed" not in interface:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the wan interface of device";
        print "EXPECTED RESULT 1: Should get the wan interface of device";
        print "ACTUAL RESULT 1: %s" %interface;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        tdkTestObj.addParameter("command", "ifconfig | grep -A 1 %s | grep \"inet addr\" | cut -f2 -d ':' | cut -f1 -d ' '| tr \"\n\" \" \"" %interface);
        expectedresult="SUCCESS";

        #Execute the test case in STB
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip();

        if expectedresult in actualresult and details:
            ipaddress = details;
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Check if wan interface is up"
            print "EXPECTED RESULT 2: wan interface should be up";
            print "ACTUAL RESULT 2: wan interface is up with ip %s" %ipaddress;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            try:
                status = "SUCCESS";
                print "Connect to Gateway Device"
                session = pxssh.pxssh(options={
                            "StrictHostKeyChecking": "no",
                            "UserKnownHostsFile": "/dev/null"})
                #session.setwinsize(24, session.maxread)
                isSessionActive = session.login(ipaddress,"root")
            except Exception, e:
                print e;
                status = "Connection to client machine failed"

            print "Connection to client machine:%s" %status;
            if expectedresult in status:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if ssh to gateway is possible"
                print "EXPECTED RESULT 3: Should be able to ssh to gateway";
                print "ACTUAL RESULT 3: SSH is success";
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if ssh to gateway is possible"
                print "EXPECTED RESULT 3: Should be able to ssh to gateway";
                print "ACTUAL RESULT 3: SSH is failed";
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if wan interface is up"
            print "EXPECTED RESULT 2: wan interface should be up";
            print "ACTUAL RESULT 2: wan interface is up with ip %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the wan interface of device";
        print "EXPECTED RESULT 1: Should get the wan interface of device";
        print "ACTUAL RESULT 1: %s" %inteface;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");

else:
        print "Failed to load sysutil module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
