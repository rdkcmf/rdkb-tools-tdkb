##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_SANITY_ValidateCMTemperatureReading</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the CM Temperature reading stored in the file /tmp/thermal_cm becomes 0 when the file /tmp/CMTemperatureRpcDataFile is deleted and when /tmp/CMTemperatureRpcDataFile gets re-created the /tmp/thermal_cm file gives a valid non-zero reading.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_SANITY_66</test_case_id>
    <test_objective>Check if the CM Temperature reading stored in the file /tmp/thermal_cm becomes 0 when the file /tmp/CMTemperatureRpcDataFile is deleted and when /tmp/CMTemperatureRpcDataFile gets re-created the /tmp/thermal_cm file gives a valid non-zero reading.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the module
2. Check if the file /tmp/thermal_cm is present in DUT and if so read the CM Temperature value stored.
3. Check if the file /tmp/CMTemperatureRpcDataFile is present in the DUT and if so proceed to delete it.
4. Check the CM temperature reading from thermal_cm file and ensure that the value is 0.
5. Sleep for 60S and check if CMTemperatureRpcDataFile is recreated in the device.
6. Now the CM Temperature should be a non-zero value from thermal-cm file.
7. Unload the module.</automation_approch>
    <expected_output>The CM Temperature reading stored in the file /tmp/thermal_cm should become 0 when the file /tmp/CMTemperatureRpcDataFile is deleted and when /tmp/CMTemperatureRpcDataFile gets re-created the /tmp/thermal_cm file should give a valid non-zero reading.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_ValidateCMTemperatureReading</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def CheckFilePresence(tdkTestObj, step, file):
    expectedresult = "SUCCESS";
    cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
    print "Command : ", cmd;
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    print "\nTEST STEP %d: Check for %s file presence" %(step, file);
    print "EXPECTED RESULT %d: %s file should be present" %(step, file);

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: %s file is present" %(step, file);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: %s file is not present" %(step, file);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return details;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;
from tdkutility import *;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_ValidateCMTemperatureReading');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check if the file /tmp/thermal_cm is present
    step = 1;
    file = "/tmp/thermal_cm";
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    details = CheckFilePresence(tdkTestObj, step, file);

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "%s is found" %file;

        #Read the CM temperature value from the file
        step = step + 1;
        cmd = "cat " + file ;
        print "Command : ", cmd;
        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

        print "\nTEST STEP %d: Get the CM Temperarture reading from the %s" %(step, file);
        print "EXPECTED RESULT %d: Should get the CM Temperarture reading from the file %s" %(step, file);

        if expectedresult in actualresult and details.isdigit() :
            thermal_CM_Temp = int(details);
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: CM Temperature : %d" %(step, thermal_CM_Temp);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the file CMTemperatureRpcDataFile is found under /tmp
            step = step + 1;
            file = "/tmp/CMTemperatureRpcDataFile";
            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            details = CheckFilePresence(tdkTestObj, step, file);

            if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "%s is found" %file;

                #Remove the file from /tmp
                step = step + 1;
                cmd = "rm -rf " + file ;
                print "Command : ", cmd;
                actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);
                sleep(5);

                print "\nTEST STEP %d : Remove the file %s" %(step, file);
                print "EXPECTED RESULT %d : Remove the file %s" %(step, file);

                if expectedresult in actualresult and details == "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: The file is removed successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if /tmp/thermal_cm reads 0 value
                    step = step + 1;
                    file = "/tmp/thermal_cm";
                    cmd = "cat " + file ;
                    print "Command : ", cmd;
                    actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                    print "\nTEST STEP %d: Get the CM Temperarture reading from the %s" %(step, file);
                    print "EXPECTED RESULT %d: Should get the CM Temperarture reading from the file %s" %(step, file);

                    if expectedresult in actualresult and details.isdigit() :
                        thermal_CM_Temp_curr = int(details);
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: CM Temperature : %d" %(step, thermal_CM_Temp_curr);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        step = step + 1;
                        print "\nTEST STEP %d : Check if CM Temperature read error writes value 0 to %s" %(step, file);
                        print "EXPECTED RESULT %d : CM Temperature read error should write value 0 to %s" %(step, file);

                        if thermal_CM_Temp_curr == 0:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: CM Temperature read error writes value 0 to %s" %(step, file);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Check if /tmp/CMTemperatureRpcDataFile gets created again after 60s
                            print "sleeping 60s for /tmp/CMTemperatureRpcDataFile to be created again";
                            sleep(60);
                            step = step + 1;
                            file = "/tmp/CMTemperatureRpcDataFile";
                            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                            details = CheckFilePresence(tdkTestObj, step, file);

                            if details == "File exist":
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "%s is found" %file;

                                #Check if /tmp/thermal_cm holds a valid value
                                step = step + 1;
                                file = "/tmp/thermal_cm";
                                cmd = "cat " + file ;
                                print "Command : ", cmd;
                                actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                print "\nTEST STEP %d: Get the CM Temperarture reading from the %s" %(step, file);
                                print "EXPECTED RESULT %d: Should get the CM Temperarture reading from the file %s" %(step, file);

                                if expectedresult in actualresult and details.isdigit() :
                                    thermal_CM_Temp_new = int(details);
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: CM Temperature : %d" %(step, thermal_CM_Temp_new);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Check if the value is non-zero
                                    if thermal_CM_Temp_new > 0:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "CM Temperature reading a valid non-zero value";
                                    else:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "CM Temperature reading is not valid non-zero value";
                                else :
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: CM Temperature : %d" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "%s is not found" %file;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: CM Temperature read error does not write value 0 to %s" %(step, file);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: CM Temperature : %d" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: The file is not removed successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "%s is not found" %file;
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: CM Temperature : %d" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "%s is not found" %file;

    sysObj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed"
