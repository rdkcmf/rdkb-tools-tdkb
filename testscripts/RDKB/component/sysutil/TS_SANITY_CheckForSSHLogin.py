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
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckForSSHLogin</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if ssh to DUT is possible and the dropbear process is running</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_SYSUTIL_40</test_case_id>
    <test_objective>This test case is to check if  ssh to DUT is possible and the dropbear process is running</test_objective>
    <test_type>Positive</test_type>
    <test_setup>RPI,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the module
2. Get the wan interface name from property file
3. Get the wan ip address of the device using ifconfig
4. Try to do ssh to the ip using pxssh
5. Check if the dropbear process is running
6. Unload the module</automation_approch>
    <expected_output>Successful ssh to gateway should be possible with  dropbear process running</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckForSSHLogin</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from pexpect import pxssh
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckForSSHLogin');
#Get the result of connection with test component and DUT
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

        #Execute the test case in DUT
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
                  isSessionActive = session.login(ipaddress,"root")
            except Exception, e:
                   print e;
                   status = "SSH to gateway failed"

            print "SSH to gateway is :%s" %status;
            if expectedresult in status:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 3: Check if ssh to gateway is possible"
               print "EXPECTED RESULT 3: Should be able to ssh to gateway";
               print "ACTUAL RESULT 3: SSH is success";
               print "[TEST EXECUTION RESULT] : SUCCESS";

               tdkTestObj = obj.createTestStep('ExecuteCmd');
               tdkTestObj.addParameter("command", "ps -ef  | grep \"dropbear\" | grep -v \"grep\"");
               expectedresult="SUCCESS";
               #Execute the test case in DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               details = tdkTestObj.getResultDetails().strip();

               if expectedresult in actualresult and  details!= "":
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 4: Check if dropbear process is running"
                  print "EXPECTED RESULT 4: dropbear process should be running ";
                  print "ACTUAL RESULT 4:",details;
                  print "[TEST EXECUTION RESULT] : SUCCESS";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "TEST STEP 4: Check if dropbear process is running";
                   print "EXPECTED RESULT 4: dropbear process should be running ";
                   print "ACTUAL RESULT 4:",details;
                   print "[TEST EXECUTION RESULT] : FAILURE";
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
