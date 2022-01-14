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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>10</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckLighttpdProcess_OnLanModeTransition</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if lighttpd process is running in the DUT when the Lan Mode is changed from Router to Bridge-Static or vice-versa.</synopsis>
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
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SANITY_65</test_case_id>
    <test_objective>To check if lighttpd process is running in the DUT when the Lan Mode is changed from Router to Bridge-Static or vice-versa.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramValue : mode(router or bridge-static)
paramType : string
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial LanMode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and store it.
3. Check if lighttpd process is running in the DUT
4. Change the Lan Mode to bridge-static if initial mode is router or vice-versa and cross check the SET with a GET.
5. Check if the lighttpd process is still running in DUT after the Lan Mode transition.
6. Revert the Lan Mode to initial value
7. Unload the modules.</automation_approch>
    <expected_output>lighttpd processs should be running in the DUT when the Lan Mode is changed from Router to Bridge-Static or vice-versa.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckLighttpdProcess_OnLanModeTransition</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def getLanMode(tdkTestObj):
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanmode = tdkTestObj.getResultDetails().strip();
    return actualresult, lanmode;

def setLanMode(tdkTestObj, setValue):
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","string");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    sleep(120);
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckLighttpdProcess_OnLanModeTransition');
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckLighttpdProcess_OnLanModeTransition');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the current Lan Mode
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    actualresult, lanmodeInitial = getLanMode(tdkTestObj);

    print "\nTEST STEP 1: Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode";
    print "EXPECTED RESULT 1: Should get the initial Lan Mode successfully";

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: GET operation success; Lanmode is : ",lanmodeInitial;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the PID of lighttpd process
        tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
        actualresult, details = getPID(tdkTestObj_Sys_ExeCmd,"lighttpd");

        print "\nTEST STEP 2 : Check if lighttpd process is running in %s mode" %lanmodeInitial;
        print "EXPECTED RESULT 2 : lighttpd  process should be running in %s mode" %lanmodeInitial;

        if expectedresult in actualresult and details.isdigit():
            pid_initial = int(details);
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2 : pid of lighttpd : %s" %(pid_initial);
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if lanmodeInitial == "bridge-static":
                setValue = "router";
            else:
                setValue = "bridge-static";

            #Change the Lan Mode
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            actualresult, details = setLanMode(tdkTestObj, setValue);

            print "\nTEST STEP 3: Transition the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %setValue;
            print "EXPECTED RESULT 3: Should set the Lan Mode to %s successfully" %setValue;

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Lan Mode set successfully; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the Lan Mode is set properly
                sleep(20);
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                actualresult, currLanMode = getLanMode(tdkTestObj)

                print "\nTEST STEP 4: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode";
                print "EXPECTED RESULT 4: Should get the current Lan Mode as %s" %setValue;

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: GET operation success; Lanmode is : ",currLanMode;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if currLanMode == setValue :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "SET reflects in GET";

                        #Verify if lighttpd is running in the current Lan Mode
                        tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
                        actualresult, details = getPID(tdkTestObj_Sys_ExeCmd,"lighttpd");

                        print "\nTEST STEP 5 : Check if lighttpd process is running in %s mode" %(setValue);
                        print "EXPECTED RESULT 5 : lighttpd  process should be running in %s mode" %(setValue);

                        if expectedresult in actualresult and details.isdigit():
                            pid_curr = int(details);
                            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5 : pid of lighttpd : %s" %(pid_curr);
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5 : pid of lighttpd : %s" %(details);
                            print "[TEST EXECUTION RESULT] : FAILURE";

                        #Revert to initial state
                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                        actualresult, details = setLanMode(tdkTestObj, lanmodeInitial);

                        print "\nTEST STEP 6 : Revert the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(lanmodeInitial);
                        print "EXPECTED RESULT 6: Should revert the Lan Mode to %s successfully" %(lanmodeInitial);

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6: Lan Mode reverted successfully; Details : %s" %(details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6: Lan Mode not reverted successfully; Details : %s" %(details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "SET does not reflect in GET";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: GET operation failed; Lanmode is : ",currLanMode;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Lan Mode not set successfully; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2 : pid of lighttpd : %s" %(details);
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: GET operation failed; Lanmode is : ",lanmodeInitial;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed"
