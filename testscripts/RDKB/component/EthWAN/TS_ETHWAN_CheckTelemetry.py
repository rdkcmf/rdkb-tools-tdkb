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
  <name>TS_ETHWAN_CheckTelemetry</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>EthWAN_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check whether Telemetry works in ethwan mode</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>40</execution_time>
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
    <test_case_id>TC_ETHWAN_13</test_case_id>
    <test_objective>Check whether Telemetry works in ethwan mode</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. The broadband device should be in ETHWAN setup
2. The EthWAN mode should be enabled
3. TDK Agent must be up and running</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled</input_parameters>
    <automation_approch>1. Load module
2. Get the ethwan mode and check if it is true or not
3. If ethwan is enabled, reboot the device
4.Once device comes online, wait for 20 mins
5.Check if Telemetry works in ethwan mode
4. Unload module</automation_approch>
    <expected_output>Telemetry should work in ethwan mode</expected_output>
    <priority>High</priority>
    <test_stub_interface>ETHWAN</test_stub_interface>
    <test_script>TS_ETHWAN_CheckTelemetry</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHWAN_CheckTelemetry');
obj1.configureTestCase(ip,port,'TS_ETHWAN_CheckTelemetry');


#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")


    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    ethwanEnable = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Should Get the enable status of Ethwan";
        print "ACTUAL RESULT 1: Ethwan Enable status is %s" %ethwanEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if "true" == ethwanEnable:
            tdkTestObj.setResultStatus("SUCCESS");
            print "The device is in ethwan mode."
            #rebooting the device
            obj.initiateReboot();
            print "Wait till box comes up"
            sleep(600);
            print "Wait for 20 minutes after box comes online"
            sleep(1200);
            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            cmd = "[ -f /rdklogs/logs/dcmscript.log ] && echo \"File exist\" || echo \"File does not exist\"";
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2:dcmscript log file should be present";
                print "ACTUAL RESULT 2:dcmscript log file is present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                query="cat /rdklogs/logs/dcmscript.log | grep -i \"HTTP RESPONSE CODE\" | cut -d':' -f5 |tr -d \"\r\n\" |tr ' ' '\n' | uniq |tr -d \"\n\""
                print "query:%s" %query
                tdkTestObj = obj1.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                if expectedresult in actualresult and details == "200":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: HTTP RESPONSE CODE should be 200 for each CURL query in dcmscript.log";
                    print "ACTUAL RESULT 3:HTTP RESPONSE CODE is 200 for each CURL query in dcmscript.log" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: HTTP RESPONSE CODE should be 200 for each CURL query in dcmscript.log";
                    print "ACTUAL RESULT 3:Failed to get HTTP RESPONSE CODE as 200 for each CURL query in dcmscript.log" ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:dcmscript log file should be present";
                print "ACTUAL RESULT 2:dcmscript log file is not present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "The device is not in ethwan mode. Please check the device setup"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Should get the enable status of Ethwan";
        print "ACTUAL RESULT 1: Ethwan Enable status is %s" %ethwanEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

