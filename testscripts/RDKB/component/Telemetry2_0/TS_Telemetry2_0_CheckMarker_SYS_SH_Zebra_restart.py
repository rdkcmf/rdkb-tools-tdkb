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
  <version>19</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_Telemetry2_0_CheckMarker_SYS_SH_Zebra_restart</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>Telemetry_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To simulate SYS_SH_Zebra_restart telemetry2_0 marker by restarting the zebra process</synopsis>
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
    <test_case_id>TC_TELEMETRY2_0_21</test_case_id>
    <test_objective>To simulate SYS_SH_Zebra_restart telemetry2_0 marker by restarting the zebra process</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL</input_parameters>
    <automation_approch>1. Load the tr181 and sysutil Modules
2. Initiate the Telemetry2_0 Pre requisite function from telemetry2_0 library, The function should return success along with revert flag and initial values
3. Get the number of lines from the telemetry log file and store the value
4. Get the PID value of the Zebra Process and kill the process using the pid value
5. Execute the script task_health_monitor.sh from TAD module
6. Get the number of lines from the telemetry log file after simulation
7. Check if marker SYS_SH_Zebra_restart is present in  telemetry log file (only between the initial line count and line count after simulation)
8. Make the script as success if the Marker is present else make it failure
9. Get the PID value of zebra process to make sure the process is running after restart
10. Initiate  telemetry post process from telemetry2_0 library (to check if any revert operation required) and the function should return success
11. Unload the modules</automation_approch>
    <expected_output>The marker should be present in telemetry log file </expected_output>
    <priority>High</priority>
    <test_stub_interface>telemetry2_0</test_stub_interface>
    <test_script>TS_Telemetry2_0_CheckMarker_SYS_SH_Zebra_restart</test_script>
    <skipped>No</skipped>
    <release_version>M80</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbTelemetry2_0Utility import *;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_SYS_SH_Zebra_restart');
tr181obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_SYS_SH_Zebra_restart');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_set = tr181obj .createTestStep('TDKB_TR181Stub_Set');

    revertFlag = 0;
    initialStatus = "";
    initialVersion = "";
    initialURL = "";

    print "***************************************************************"
    print "TEST STEP 1: Initiating Pre-Requisite Check for Telemetry2_0";
    print "EXPECTED RESULT 1:Pre-Requisite Check for Telemetry2_0 Should be Success";

    preReq_Status,revertFlag,initialStatus,initialVersion,initialURL = telemetry2_0_Prerequisite(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_set);

    if preReq_Status == 1:
        print "ACTUAL RESULT 1: Pre-Requisite for Telemetry2_0 was successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "***************************************************************"
        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");

        lineCountResult, initialLinesCount = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);

        if expectedresult in lineCountResult:
            print "Initial Line count of Telemetry Log File is ",initialLinesCount
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the initial Line count of Telemetry Log file";
            print "EXPECTED RESULT 2 : Should get the initial line count of Telemetry Log file";
            print "ACTUAL RESULT 2: Line count retrieved Successfully";
            print "[TEST EXECUTION RESULT] : SUCCESS";

            details,actualresult = getPID(tdkTestObj_Sys_ExeCmd,"zebra");
            if expectedresult in actualresult and details != "":
               initialPID = int(details);
               tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
               print "TEST STEP 3: Check if zebra process is running";
               print "EXPECTED RESULT 3:zebra  process should be running";
               print "ACTUAL RESULT 3: pid of zebra:",details;
               print "[TEST EXECUTION RESULT] : SUCCESS";

               actualresult =killProcess(tdkTestObj_Sys_ExeCmd,initialPID,"/usr/ccsp/tad/task_health_monitor.sh");
               if expectedresult in actualresult :
                  tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                  print "TEST STEP 4: Kill zebra process and run task_health_monitor.sh script";
                  print "EXPECTED RESULT 4:Should Kill the zebra  process and run task_health_monitor.sh script";
                  print "ACTUAL RESULT 4: zebra process killed and run task_health_monitor.sh script successfully";
                  print "[TEST EXECUTION RESULT] : SUCCESS";

                  sleep(45);

                  lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);
                  if expectedresult in lineCountResult and  int(lineCountAfterSimu) > int(initialLinesCount):
                     print "Line count of Telemetry Log File After Simulation is ",lineCountAfterSimu
                     tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                     print "TEST STEP 5: Get the line count of telemetry log file and compare the value with initialLinesCount";
                     print "EXPECTED RESULT 5: Line count After Simulation should be greater than the initialLinesCount";
                     print "ACTUAL RESULT 5: Line count After Simulation is greater than the initialLinesCount";
                     print "[TEST EXECUTION RESULT] : SUCCESS";

                     query = "sed -n -e %s,%sp /rdklogs/logs/telemetry2_0.txt.0 | grep -i \"Received eventInfo : SYS_SH_Zebra_restart\"" %(initialLinesCount,lineCountAfterSimu)
                     print "query:%s" %query
                     tdkTestObj_Sys_ExeCmd.addParameter("command", query);
                     tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
                     actualresult = tdkTestObj_Sys_ExeCmd.getResult();
                     details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n","");
                     print "Marker Detail Found from log file is: %s "%details;

                     if expectedresult in actualresult and details!="" and (len(details) > 0) and "SYS_SH_Zebra_restart" in details:
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                        markervalue = details.split("SYS_SH_Zebra_restart value : ")[1]
                        print "TEST STEP 6:SYS_SH_Zebra_restart  Marker should be present";1
                        print "EXPECTED RESULT 6: SYS_SH_Zebra_restart Marker should be present";
                        print "ACTUAL RESULT 6: SYS_SH_Zebra_restart  Marker Value is %s" %markervalue;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        actualresult,pid = checkProcessRestarted(tdkTestObj_Sys_ExeCmd,"zebra");
                        if expectedresult in actualresult and pid != "" and pid != initialPID:
                           tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                           print "TEST STEP 7: Check if the zebra proccess restarted";
                           print "EXPECTED RESULT 7:zebra proccess should restart ";
                           print "ACTUAL RESULT 7: zebra restarted successfully";
                           print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                            print "TEST STEP 7: Check if the zebra proccess restarted";
                            print "EXPECTED RESULT 7:zebra proccess should restart ";
                            print "ACTUAL RESULT 7: Failed to Restart Zebra Process";
                            print "[TEST EXECUTION RESULT] : FAILURE";
                     else:
                         tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                         print "TEST STEP 6:SYS_SH_Zebra_restart  Marker should be present";
                         print "EXPECTED RESULT 6: SYS_SH_Zebra_restart Marker should be present";
                         print "ACTUAL RESULT 6: SYS_SH_Zebra_restart  Marker is %s" %details;
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : FAILURE";
                  else:
                      tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                      print "TEST STEP 5: Get the line count of telemetry log file and compare the value with initialLinesCount";
                      print "EXPECTED RESULT 5: Line count After Simulation should be greater than the initialLinesCount";
                      print "ACTUAL RESULT 5: Line count After Simulation is NOT greater than the initialLinesCount";
                      print "[TEST EXECUTION RESULT] : FAILURE";
               else:
                   tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                   print "TEST STEP 4: Kill zebra process and run task_health_monitor.sh script";
                   print "EXPECTED RESULT 4:Should Kill the zebra  process and run task_health_monitor.sh script";
                   print "ACTUAL RESULT 4: Failed to kill zebra process and run task_health_monitor.sh script";
                   print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                print "TEST STEP 3: Check if zebra process is running";
                print "EXPECTED RESULT 3:zebra  process should be running";
                print "ACTUAL RESULT 3: pid of zebra:",details;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the initial Line count of Telemetry Log file";
            print "EXPECTED RESULT 2 : Should get the initial line count of Telemetry Log file";
            print "ACTUAL RESULT 2: Failed to retrive Line count";
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
        print "ACTUAL RESULT 8 : Post Process for Telemetry2_0 was Successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 8: Post Process for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
