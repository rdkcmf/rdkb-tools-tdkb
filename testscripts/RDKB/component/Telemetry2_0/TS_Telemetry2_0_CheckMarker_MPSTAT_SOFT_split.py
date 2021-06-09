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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_Telemetry2_0_CheckMarker_MPSTAT_SOFT_split</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>Telemetry_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To simulate MPSTAT_SOFT_split telemetry2_0 marker by running the log_mem_cpu_info.sh script from TAD</synopsis>
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
    <test_case_id>TC_TELEMETRY2_0_15</test_case_id>
    <test_objective>To simulate MPSTAT_SOFT_split telemetry2_0 marker by running the log_mem_cpu_info.sh script from TAD</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL
</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil Modules
2. Initiate the Telemetry2_0 Pre requisite function from telemetry2_0 library, The function should return success along with revert flag and initial values
3. Get the number of lines from the telemetry log file and store the value
4. Execute the script log_mem_cpu_info.sh from TAD module
5. Get the number of lines from the telemetry log file after simulation
6. Check if marker MPSTAT_SOFT_split is present in  telemetry log file (only between the initial line count and line count after simulation)
7. Make the script as success if the Marker is present else make it failure
8. Initiate  telemetry post process from telemetry2_0 library (to check if any revert operation required) and the function should return success
9. Unload the modules</automation_approch>
    <expected_output>The marker should be present in telemetry log file </expected_output>
    <priority>High</priority>
    <test_stub_interface>telemetry2_0</test_stub_interface>
    <test_script>TS_Telemetry2_0_CheckMarker_MPSTAT_SOFT_split</test_script>
    <skipped>No</skipped>
    <release_version>M80</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from  tdkbTelemetry2_0Utility import *;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_MPSTAT_SOFT_split');
tr181obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_MPSTAT_SOFT_split');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    revertFlag = 0;
    initialStatus = "";
    initialVersion = "";
    initialURL = "";
    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_set = tr181obj .createTestStep('TDKB_TR181Stub_Set');

    print "***************************************************************"
    print "TEST STEP 1: Initiating Pre-Requisite Check for Telemetry2_0";
    print "EXPECTED RESULT 1:Pre-Requisite Check for Telemetry2_0 Should be Success";

    preReq_Status,revertFlag,initialStatus,initialVersion,initialURL = telemetry2_0_Prerequisite(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_set);

    if preReq_Status == 1:
        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");

        print "ACTUAL RESULT 1: Pre-Requisite for Telemetry2_0 was successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "***************************************************************"

        lineCountResult, initialLinesCount = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);

        if expectedresult in lineCountResult:
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the initial Line count of Telemetry Log file";
            print "EXPECTED RESULT 2: Should get the initial line count of Telemetry Log file";
            print "ACTUAL RESULT 2: Line count retrieved Successfully";
            print "[TEST EXECUTION RESULT] 2: SUCCESS";

            print "Initial Line count of Telemetry Log File is ",initialLinesCount

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "sh /usr/ccsp/tad/log_mem_cpu_info.sh &";
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Execute the log_mem_cpu_info script in background";
                print "EXPECTED RESULT 3: log_mem_cpu_info script should be running";
                print "ACTUAL RESULT 3: Script is Running";
                print "[TEST EXECUTION RESULT] 3: SUCCESS";

                sleep(45);

                lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);
                if expectedresult in lineCountResult and  int(lineCountAfterSimu) > int(initialLinesCount):
                    tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the line count of telemetry log file and compare the value with initialLinesCount";
                    print "EXPECTED RESULT 4: Line count After Simulation should be greater than the initialLinesCount";
                    print "ACTUAL RESULT 4: Line count After Simulation is greater than the initialLinesCount";
                    print "[TEST EXECUTION RESULT] 4: SUCCESS";

                    print "Line count of Telemetry Log File After Simulation is ",lineCountAfterSimu

                    query = "sed -n -e %s,%sp /rdklogs/logs/telemetry2_0.txt.0 | grep -i \"Received eventInfo : MPSTAT_SOFT_split\"" %(initialLinesCount,lineCountAfterSimu)
                    print "query:%s" %query
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", query);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                    print "Marker Detail Found from log file is: %s "%details;

                    if expectedresult in actualresult and details!="" and (len(details) > 0) and "MPSTAT_SOFT_split" in details:
                        tdkTestObj.setResultStatus("SUCCESS");
                        markervalue = details.split("MPSTAT_SOFT_split value : ")[1]
                        print "TEST STEP 5: MPSTAT_SOFT_split  Marker should be present";1
                        print "EXPECTED RESULT 5: MPSTAT_SOFT_split Marker should be present";
                        print "ACTUAL RESULT 5: MPSTAT_SOFT_split  Marker Value is %s" %markervalue;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] 5: SUCCESS";
                        print "***************************************************************"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: MPSTAT_SOFT_split  Marker should be present";
                        print "EXPECTED RESULT 5: MPSTAT_SOFT_split Marker should be present";
                        print "ACTUAL RESULT 5: MPSTAT_SOFT_split  Marker is %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                        print "***************************************************************"
                else:
                    tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the line count of telemetry log file and compare the value with initialLinesCount";
                    print "EXPECTED RESULT 4: Line count After Simulation should be greater than the initialLinesCount";
                    print "ACTUAL RESULT 4: Line count After Simulation is NOT greater than the initialLinesCount";
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Execute the log_mem_cpu_info script in background";
                print "EXPECTED RESULT 3: log_mem_cpu_info script should be running";
                print "ACTUAL RESULT 3: Script is NOT Running";
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the initial Line count of Telemetry Log file";
            print "EXPECTED RESULT 2: Should get the initial line count of Telemetry Log file";
            print "ACTUAL RESULT 2: Failed to get the Line count";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Pre-Requisite for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "***************************************************************"

    print "***************************************************************"
    print "TEST STEP 6: Initiating Post Process for Telemetry2_0";
    print "EXPECTED RESULT 6: Post Process should be success";
    postprocess_Status = telemetry2_0_PostProcess(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_set,revertFlag,initialStatus,initialVersion,initialURL);
    if postprocess_Status == 1:
        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 6: Post Process for Telemetry2_0 was Successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "***************************************************************"
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 6: Post Process for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "***************************************************************"

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
