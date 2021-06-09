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
  <version>9</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_Telemetry2_0_CheckMarker_SYS_ERROR_LoadAbove8</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>Telemetry_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To simulate SYS_ERROR_LoadAbove8 telemetry2_0 marker by loading CPU Load value more than 8</synopsis>
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
    <test_case_id>TC_TELEMETRY2_0_32</test_case_id>
    <test_objective>To simulate SYS_ERROR_LoadAbove8 telemetry2_0 marker by loading CPU Load value more than 8
</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL
</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil Modules
2. Initiate the Telemetry2_0 Pre requisite function from telemetry2_0 library, The function should return success along with revert flag and initial values
3. Get the number of lines from the telemetry log file and store the value
4. Load the cpu value gradually
5. If the CPULoad value hits 8, then execute the script log_mem_cpu_info.sh from TAD module
6. Kill all the processes used to increase the CPU value
7. Get the number of lines from the telemetry log file after simulation
8. Check if marker SYS_ERROR_LoadAbove8 is present in telemetry log file (only between the initial line count and line count after simulation)
9. Make the script as success if the Marker is present else make it failure
10. Reboot the device if revert flag was not enabled, to reduce the CPU Load value immediately
11. Initiate  telemetry post process from telemetry2_0 library (to check if any revert operation required) and the function should return success
12. Unload the modules</automation_approch>
    <expected_output>The marker should be present in telemetry log file
</expected_output>
    <priority>High</priority>
    <test_stub_interface>telemetry2_0</test_stub_interface>
    <test_script>TS_Telemetry2_0_CheckMarker_SYS_ERROR_LoadAbove8</test_script>
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
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_SYS_ERROR_LoadAbove8');
tr181obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_SYS_ERROR_LoadAbove8');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

def getCPULoadfromUptime(tdkTestObj):
    cmd = "uptime | awk -F'[a-z]:' '{ print $2}' | sed 's/^ *//g' | sed 's/,//g' | sed 's/ /:/g' | cut -f3 -d: | cut -f1 -d.";
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    cpuload = int(details);
    return actualresult,cpuload;

def increaseCPULoad(tdkTestObj):
    cmd = "for i in `seq 1 5`; do yes > /dev/null & done";
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    return actualresult,details;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    revertFlag = 0;
    initialStatus = "";
    initialVersion = "";
    initialURL = "";
    expectedresult="SUCCESS";
    flag_reboot_to_dec_cpuload = 1; #Decide whether to reboot the DUT in the end to reduce the CPUload quickly
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

            print "TEST STEP 3: Increase the CPU Load";
            print "EXPECTED RESULT 3: CPULOAD average should be increased to value 8";

            cpuloadabove8 = 0;
            #Wait for 2 min to load the CPU value
            for loop in range (1,24):
                cpuloadres,cpuload = getCPULoadfromUptime(tdkTestObj_Sys_ExeCmd);
                print "Value of CPULOAD is",cpuload;
                if int(cpuload) == 8:
                    cpuloadabove8 = 1;
                    tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                    print "EXPECTED RESULT 3: CPULOAD average increased to value 8";
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    break;
                elif int(cpuload) > 8:
                    print "EXPECTED RESULT 3: CPULOAD average value was more than 8";
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    cpuloadabove8 = 0;
                    break;
                else:
                    increaseCPULoad(tdkTestObj_Sys_ExeCmd);
                    sleep(5);

            if cpuloadabove8 == 1:
                cmd = "sh /usr/ccsp/tad/log_mem_cpu_info.sh &";
                tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
                tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
                actualresult = tdkTestObj_Sys_ExeCmd.getResult();
                details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult:
                    tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Execute the log_mem_cpu_info script in background";
                    print "EXPECTED RESULT 4: log_mem_cpu_info script should be running";
                    print "ACTUAL RESULT 4: log_mem_cpu_info Script is Running";
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    cmd = "killall yes";
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Kill all processes used to increase CPULoad";
                        print "EXPECTED RESULT 5: All yes processes should be killed";
                        print "ACTUAL RESULT 5: All yes process Killed Successfully";
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        sleep(30);

                        lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);
                        if expectedresult in lineCountResult and  int(lineCountAfterSimu) > int(initialLinesCount):
                            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Get the line count of telemetry log file and compare the value with initialLinesCount";
                            print "EXPECTED RESULT 6: Line count After Simulation should be greater than the initialLinesCount";
                            print "ACTUAL RESULT 6: Line count After Simulation is greater than the initialLinesCount";
                            print "Line count of Telemetry Log File After Simulation is ",lineCountAfterSimu
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            query = "sed -n -e %s,%sp /rdklogs/logs/telemetry2_0.txt.0 | grep -i \"Received eventInfo : SYS_ERROR_LoadAbove8\"" %(initialLinesCount,lineCountAfterSimu)
                            print "query:%s" %query
                            tdkTestObj_Sys_ExeCmd.addParameter("command", query);
                            tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
                            actualresult = tdkTestObj_Sys_ExeCmd.getResult();
                            details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n","");
                            print "Marker Detail Found from log file is: %s "%details;

                            if expectedresult in actualresult and details!="" and (len(details) > 0) and "SYS_ERROR_LoadAbove8" in details:
                                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                                markervalue = details.split("SYS_ERROR_LoadAbove8 value : ")[1]
                                print "TEST STEP 7: SYS_ERROR_LoadAbove8  Marker should be present";1
                                print "EXPECTED RESULT 7: SYS_ERROR_LoadAbove8 Marker should be present";
                                print "ACTUAL RESULT 7: SYS_ERROR_LoadAbove8  Marker Value is %s" %markervalue;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                                print "TEST STEP 7: SYS_ERROR_LoadAbove8  Marker should be present";
                                print "EXPECTED RESULT 7: SYS_ERROR_LoadAbove8 Marker should be present";
                                print "ACTUAL RESULT 7: SYS_ERROR_LoadAbove8  Marker is %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                            print "TEST STEP 6: Get the line count of telemetry log file and compare the value with initialLinesCount";
                            print "EXPECTED RESULT 6: Line count After Simulation should be greater than the initialLinesCount";
                            print "ACTUAL RESULT 6: Line count After Simulation is NOT greater than the initialLinesCount",lineCountAfterSimu
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Kill all processes used to increase CPULoad";
                        print "EXPECTED RESULT 5: All yes processes should be killed";
                        print "ACTUAL RESULT 5: Failed to Kill All yes processes";
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                    print "TEST STEP 4: Execute the log_mem_cpu_info script in background";
                    print "EXPECTED RESULT 4: log_mem_cpu_info script should be running";
                    print "ACTUAL RESULT 4: Script is NOT Running";
                    print "[TEST EXECUTION RESULT] : FAILURE";

                if revertFlag == 1:
                    print "Revert Flag was set, No need for reboot DUT to reduce CPULOAD"
                elif flag_reboot_to_dec_cpuload == 1:
                    print "******************************************************"
                    print "Initiating Reboot, To reduce the CPULOAD Average value";
                    print"*******************************************************"
                    sysobj .initiateReboot();
                    sleep(300);
            else:
                print "CPULOAD average value is not 8, Exiting Script"
                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
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
    print "TEST STEP 8: Initiating Post Process for Telemetry2_0";
    print "EXPECTED RESULT 8: Post Process should be success";
    postprocess_Status = telemetry2_0_PostProcess(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_set,revertFlag,initialStatus,initialVersion,initialURL);
    if postprocess_Status == 1:
        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 8: Post Process for Telemetry2_0 was Successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "***************************************************************"

        if flag_reboot_to_dec_cpuload == 1:
            cpuloadres,cpuload = getCPULoadfromUptime(tdkTestObj_Sys_ExeCmd);

            if expectedresult in cpuloadres and cpuload <= 2:
                tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                print "TEST STEP 9: Check CPULOAD Decreased to Normal Value";
                print "EXPECTED RESULT 9: CPULOAD value  should be below 2";
                print "ACTUAL RESULT 9: CPULOAD decreased to 2";
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                print "TEST STEP 9: Check CPULOAD Decreased to Normal Value";
                print "EXPECTED RESULT 9: CPULOAD value  should be below 2";
                print "ACTUAL RESULT 9: CPULOAD value NOT decreased to 2";
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 8: Post Process for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "***************************************************************"

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
