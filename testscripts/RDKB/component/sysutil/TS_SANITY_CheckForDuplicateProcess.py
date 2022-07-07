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
  <name>TS_SANITY_CheckForDuplicateProcess</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if  any two instances of the process is running</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_40</test_case_id>
    <test_objective>This test case is to check if  any  two instances of the process is running</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,EMU</test_setup>
    <pre_requisite>1.TDK Agent should be in running state or invoke it through StartTdk.sh script
2.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem</pre_requisite>
    <api_or_interface_used>ExecuteCmd</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the module
2. Get the list of process which are expected to have a single instance
3. Check the number of instances the processes is running
4. The processes are expected to have a single instance
5. Mark the script as success if only one instance is present else Mark the script as Failure
6.Unload the Module</automation_approch>
    <expected_output>The listed processes are expected to have a single instance </expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckForDuplicateProcess</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import time;
from tdkutility import *;
from xfinityWiFiLib import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckForDuplicateProcess');
obj1.configureTestCase(ip,port,'TS_SANITY_CheckForDuplicateProcess');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    step = 1;
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    process= "sh %s/tdk_utility.sh parseConfigFile LIST_OF_PROCESSES" %TDK_PATH;
    print process;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", process);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    ProcessList = tdkTestObj.getResultDetails().strip();
    ProcessList = ProcessList.replace("\\n", "");

    if "Invalid Argument passed" not in ProcessList:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the list of processes ";
        print "EXPECTED RESULT 1: Should get the list of processes";
        print "ACTUAL RESULT 1: %s" %ProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        ProcessList = ProcessList.split(",");

        #If CcspTr069PaSsp in ProcessList, check if the TR069 RFC is enabled
        revert_flag = 0;
        if "CcspTr069PaSsp" in ProcessList :
            step = step + 1;
            #Get current values of public wifi params
            tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get');
            actualresult,enable = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");

            print "\nTEST STEP %d : Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable" %step;
            print "EXPECTED RESULT %d : Should get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable" %step;

            if expectedresult in actualresult and enable != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is : %s" %(step, enable);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if enable != "true":
                    #Set TR69 RFC to true
                    step = step + 1;
                    tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_SetOnly');
                    actualresult, details = setTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable", "true", "boolean");

                    print "\nTEST STEP %d : Set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to true" %step;
                    print "EXPECTED RESULT %d : Should set the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to true" %step;

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable enabled successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Cross check with GET
                        time.sleep(10);
                        tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get');
                        actualresult,new_enable = getTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");

                        if expectedresult in actualresult and new_enable == "true":
                            revert_flag = 1;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TR069 RFC enabled successfully";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TR069 RFC NOT enabled successfully";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable NOT enabled successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "TR69 RFC is enabled already...SET operation not required";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is not retrieved" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

        for item in ProcessList:
            if item == "CcspHotspot":
                step = step + 1;
                #Get current values of public wifi params
                tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable");
                expectedresult="SUCCESS";
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in  actualresult and details == "true":
                    command1 = "ps  | grep  %s  | grep -v \"grep\"| wc -l" %item
                    tdkTestObj = obj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", command1);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip();
                    details = details.replace("\\n", "");

                    print "\nTEST STEP %d: Check if two instances of %s process is running " %(step, item);
                    print "EXPECTED RESULT %d: %s process is expected to have a single instances" %(step, item);

                    if expectedresult in actualresult and int(details) == 1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: %s is having %s instance" %(step,item,details);
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: %s is having %s instance" %(step,item,details);
                        print "[TEST EXECUTION RESULT] : FAILURE"
                else:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Since xfinitywifi is disabled CcspHotspot is not running"
                    print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                step = step + 1;
                command1 =  "ps  | grep  %s  | grep -v \"grep\"| wc -l" %item
                tdkTestObj = obj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", command1);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip();
                details = details.replace("\\n", "");

                print "\nTEST STEP %d: Check if two instances of %s process is running " %(step,item);
                print "EXPECTED RESULT %d: %s process is expected to have a single instances" %(step,item);

                if expectedresult in actualresult and int(details) == 1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: %s is having %s instance" %(step,item,details);
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: %s is having %s instance" %(step,item,details);
                    print "[TEST EXECUTION RESULT] : FAILURE"

        #Revert operation
        if revert_flag == 1:
            step = step + 1;
            tdkTestObj= obj1.createTestStep('TDKB_TR181Stub_SetOnly');
            actualresult, details = setTR181Value(tdkTestObj, "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable", enable, "boolean");

            print "\nTEST STEP %d : Revert the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable" %step;
            print "EXPECTED RESULT %d : Should revert the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable" %step;

            if expectedresult in actualresult and details != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable reverted successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable NOT reverted successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the list of processes ";
        print "EXPECTED RESULT 1: Should get the list of processes";
        print "ACTUAL RESULT 1: %s" %ProcessList;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
else:
     print "Failed to load sysutil module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
