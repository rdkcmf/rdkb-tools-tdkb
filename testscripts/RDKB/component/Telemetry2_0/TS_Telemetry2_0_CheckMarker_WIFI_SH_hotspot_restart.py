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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_Telemetry2_0_CheckMarker_WIFI_SH_hotspot_restart</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>Telemetry_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To simulate WIFI_SH_hotspot_restart marker by restarting the CcspHotspot process</synopsis>
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
    <test_case_id>TC_TELEMETRY2_0_11</test_case_id>
    <test_objective>This test case is to simulate WIFI_SH_hotspot_restart marker by restarting the CcspHotspot process</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Version
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.ConfigURL</input_parameters>
    <automation_approch>1. Load the tr181,wifiagent and sysutil Modules
2. Initiate the Telemetry2_0 Pre requisite function from telemetry2_0 library, The function should return success along with revert flag and initial values
3. Get the number of lines from the telemetry log file and store the value
4. Get the default public wifi parameter value and Enable the public wifi
5. Restart the CcspHotspot  process
5. Get the number of lines from the telemetry log file after simulation
6. Check if marker WIFI_SH_hotspot_restart  is present in  telemetry log file (only between the initial line count and line count after simulation)
7. Revert the public wifi to previous state
8. Make the script as success if the Marker is present else make it failure
9. Initiate  telemetry post process for telemetry2_0 (to check if any revert operation required) and the function should return success
10. Unload the module</automation_approch>
    <expected_output>On simulation by restarting the CcspHotspot process WIFI_SH_hotspot_restart  marker should be present.</expected_output>
    <priority>High</priority>
    <test_stub_interface>Telemetry2_0</test_stub_interface>
    <test_script>TS_Telemetry2_0_CheckMarker_WIFI_SH_hotspot_restart</test_script>
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
from xfinityWiFiLib import *
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_WIFI_SH_hotspot_restart');
tr181obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_WIFI_SH_hotspot_restart');
wifiobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_WIFI_SH_hotspot_restart');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();
loadmodulestatus2=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
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

            tdkTestObj,actualresult,orgValue = GetPublicWiFiParamValues(wifiobj);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Get values of PublicWiFi params"
                print "ACTUAL RESULT 3:%s" %orgValue
                print "[TEST EXECUTION RESULT] : SUCCESS";

                setvalues,tdkTestObj,actualresult  = parsePublicWiFiConfigValues(sysobj);

                if expectedresult in actualresult:
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 4:Get the set values to enable PublicWiFi"
                   print "ACTUAL RESULT 4:Get was successful";
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   values = [setvalues[0],setvalues[1],setvalues[2],setvalues[3],setvalues[3],"true","true","true","true",setvalues[3],"true","true",setvalues[4],setvalues[5],setvalues[6],setvalues[7],setvalues[8],setvalues[7],setvalues[8],setvalues[3],"true","true",setvalues[4],setvalues[5],setvalues[6],setvalues[7],setvalues[8],setvalues[7],setvalues[8],"true"];
                   tdkTestObj, actualresult, details = SetPublicWiFiParamValues(wifiobj,values);
                   #Execute the test case in DUT
                   tdkTestObj.executeTestCase(expectedresult);

                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();
                   if expectedresult in actualresult:
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 5 : Should enable PublicWiFi"
                      print "ACTUAL RESULT 5:%s" %details
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                      sleep(30);

                      details,actualresult = getPID(tdkTestObj_Sys_ExeCmd,"CcspHotspot");
                      if expectedresult in actualresult and details != "":
                         Initialpid = int(details);
                         tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                         print "TEST STEP 6: Check if CcspHotspot process is running";
                         print "EXPECTED RESULT 6:CcspHotspot  process should be running";
                         print "ACTUAL RESULT 6: pid of CcspHotspot:",details;
                         print "[TEST EXECUTION RESULT] : SUCCESS";

                         actualresult =killProcess(tdkTestObj_Sys_ExeCmd,Initialpid,"");
                         if expectedresult in actualresult :
                            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                            print "TEST STEP 7: Kill CcspHotspot process";
                            print "EXPECTED RESULT 7:Should Kill the CcspHotspot  process ";
                            print "ACTUAL RESULT 7: CcspHotspot process killed successfully";
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #WIFI_SH_hotspot_restart marker comes up once the GRE tunnel is created hence doing a sleep for marker to be uploaded
                            sleep(900);

                            lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);
                            if expectedresult in lineCountResult and  int(lineCountAfterSimu) > int(initialLinesCount):
                               print "Line count of Telemetry Log File After Simulation is ",lineCountAfterSimu
                               tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                               print "TEST STEP 8: Get the line count of telemetry log file and compare the value with initialLinesCount";
                               print "EXPECTED RESULT 8: Line count After Simulation should be greater than the initialLinesCount";
                               print "ACTUAL RESULT 8: Line count After Simulation is greater than the initialLinesCount";
                               print "[TEST EXECUTION RESULT] : SUCCESS";

                               query = "sed -n -e %s,%sp /rdklogs/logs/telemetry2_0.txt.0 | grep -i \"Received eventInfo : WIFI_SH_hotspot_restart\"" %(initialLinesCount,lineCountAfterSimu)
                               print "query:%s" %query
                               tdkTestObj_Sys_ExeCmd.addParameter("command", query);
                               tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
                               actualresult = tdkTestObj_Sys_ExeCmd.getResult();
                               details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n","");
                               print "Marker Detail Found from log file is: %s "%details;

                               if expectedresult in actualresult and details!="" and (len(details) > 0) and "WIFI_SH_hotspot_restart" in details:
                                  tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                                  markervalue = details.split("WIFI_SH_hotspot_restart value :")[1]
                                  print "TEST STEP 9:WIFI_SH_hotspot_restart  Marker should be present";1
                                  print "EXPECTED RESULT 9: WIFI_SH_hotspot_restart Marker should be present";
                                  print "ACTUAL RESULT 9: WIFI_SH_hotspot_restart  Marker Value is %s" %markervalue;
                                  #Get the result of execution
                                  print "[TEST EXECUTION RESULT] : SUCCESS";

                                  actualresult,pid = checkProcessRestarted(tdkTestObj_Sys_ExeCmd,"CcspHotspot");
                                  if expectedresult in actualresult and pid != "" and pid != Initialpid:
                                     tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                                     print "TEST STEP 7: Check if the CcspHotspot proccess restarted";
                                     print "EXPECTED RESULT 7:CcspHotspot proccess should restart ";
                                     print "ACTUAL RESULT 7: CcspHotspot restarted successfully";
                                     print "[TEST EXECUTION RESULT] : SUCCESS";
                                  else:
                                      tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                                      print "TEST STEP 7: Check if the CcspHotspot proccess restarted";
                                      print "EXPECTED RESULT 7:CcspHotspot proccess should restart ";
                                      print "ACTUAL RESULT 7: CcspHotspot restart failed";
                                      print "[TEST EXECUTION RESULT] : FAILURE";
                               else:
                                   tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                                   print "TEST STEP 9:WIFI_SH_hotspot_restart  Marker should be present";
                                   print "EXPECTED RESULT 9: WIFI_SH_hotspot_restart Marker should be present";
                                   print "ACTUAL RESULT 9: WIFI_SH_hotspot_restart  Marker is %s" %details;
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                                print "TEST STEP 8: Get the line count of telemetry log file and compare the value with initialLinesCount";
                                print "EXPECTED RESULT 8: Line count After Simulation should be greater than the initialLinesCount";
                                print "ACTUAL RESULT 8: Line count After Simulation is NOT greater than the initialLinesCount";
                                print "[TEST EXECUTION RESULT] : FAILURE";
                         else:
                             tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                             print "TEST STEP 7: Kill CcspHotspot process";
                             print "EXPECTED RESULT 7:Should Kill the CcspHotspot  process ";
                             print "ACTUAL RESULT 7: Failed to kill CcspHotspot process";
                             print "[TEST EXECUTION RESULT] : FAILURE";
                      else:
                          tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                          print "TEST STEP 6: Check if CcspHotspot process is running";
                          print "EXPECTED RESULT 6:CcspHotspot  process should be running";
                          print "ACTUAL RESULT 6: pid of CcspHotspot:",details;
                          print "[TEST EXECUTION RESULT] : FAILURE";
                      #Revert the values of public wifi params
                      tdkTestObj, actualresult, details = SetPublicWiFiParamValues(wifiobj,orgValue);
                      if expectedresult in actualresult:
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 11:Revert the PublicWiFi param values"
                         print "ACTUAL RESULT 11:%s" %details
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 11:Revert the PublicWiFi param values"
                          print "ACTUAL RESULT 11:%s" %details
                          print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 5 : Should enable PublicWiFi"
                       print "ACTUAL RESULT 5:%s" %details
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4:Get the set values to enable PublicWiFi"
                    print "ACTUAL RESULT 4:Get failed";
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Get values of PublicWiFi params"
                print "ACTUAL RESULT 3:%s" %orgValue
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
    print "TEST STEP 11: Initiating Post Process for Telemetry2_0";
    print "EXPECTED RESULT 11: Post Process should be success";

    postprocess_Status = telemetry2_0_PostProcess(sysobj,tdkTestObj_Sys_ExeCmd,tdkTestObj_Tr181_set,revertFlag,initialStatus,initialVersion,initialURL);
    if postprocess_Status == 1:
        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 11 : Post Process for Telemetry2_0 was Successful";
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
        print "ACTUAL RESULT 11: Post Process for Telemetry2_0 was Failed";
        print "[TEST EXECUTION RESULT] : FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
