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
  <name>TS_Telemetry2_0_CheckMarker_XCONF_Dwld_failed</name>
  <primitive_test_id/>
  <primitive_test_name>Telemetry_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To simulate  XCONF_Dwld_failed  by giving a bad image name and triggering xconf http download</synopsis>
  <groups_id/>
  <execution_time>40</execution_time>
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
    <test_case_id>TC_TELEMETRY2_0_50</test_case_id>
    <test_objective>This test case is to simulate  XCONF_Dwld_failed  by giving a bad image name and triggering xconf http download</test_objective>
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
4. Set the Xconf http Url and Initiate a Xconf firmware download with a bad image name
5. Get the number of lines from the telemetry log file after simulation
6. Check if marker XCONF_Dwld_failed  is present in  telemetry log file (only between the initial line count and line count after simulation)
7. Make the script as success if the Marker is present else make it failure
8. Initiate  telemetry post process from telemetry2_0 library (to check if any revert operation required) and the function should return success
9. Unload the modules</automation_approch>
    <expected_output>The marker should be present in telemetry log file</expected_output>
    <priority>High</priority>
    <test_stub_interface>Telemetry2_0</test_stub_interface>
    <test_script>TS_Telemetry2_0_CheckMarker_XCONF_Dwld_failed</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkbTelemetry2_0Utility import *;
from time import sleep;
import xconfUtilityLib;
from xconfUtilityLib import *
from xconfVariables import *

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj= tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_XCONF_Dwld_failed');
tr181obj.configureTestCase(ip,port,'TS_Telemetry2_0_CheckMarker_XCONF_Dwld_failed');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_set = tr181obj .createTestStep('TDKB_TR181Stub_Set');

    expectedresult="SUCCESS";
    revertFlag = 0;
    initialStatus = "";
    initialVersion = "";
    initialURL = "";

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

            ####Override server url to be used as the mock server url
            actualresult, xconfFile = xconfUtilityLib.overrideServerUrl(sysobj, CDN_MOC_SERVER);

            #get firmware details from config file
            AUTO_SEARCH_IN_JENKINS='FALSE'
            FirmwareVersion = "Invalid_Firmware"
            FirmwareFilename = "Invalid_Firmware.bin"

            ####form the curl command to set the configuration details of the device in the mock server
            Curl_CMD = xconfUtilityLib.getXCONFServerConfigCmd(sysobj, FirmwareVersion, FirmwareFilename, "http");
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');

            print "Curl Request Formed:",Curl_CMD
            tdkTestObj.addParameter("command",Curl_CMD);
            tdkTestObj.executeTestCase("SUCCESS");

            #Get the result of execution
            result = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if "Successfully added configuration" in details:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 3: Execute curl cmnd to  add device configuration"
               print "EXPECTED RESULT 3: Should add device configuration"
               print "ACTUAL RESULT 3: Status: %s " %details
               print "[TEST EXECUTION RESULT] : SUCCESS";
               print "SUCCESS:Executed Curl Command"

               ################get log file name from tdk_platform.properties
               actualresult, propVal = xconfUtilityLib.GetPlatformProperties(sysobj, "CDN_LOG");
               if expectedresult in actualresult:
                  tdkTestObj.setResultStatus("SUCCESS");
                  cdnLog = propVal
                  print "SUCCESS:get log file name"
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "FAILURE:failed to get log file name"

               ################get CDN file name from tdk_platform.properties
               actualresult, propVal = xconfUtilityLib.GetPlatformProperties(sysobj, "CDN_FILE");
               if expectedresult in actualresult:
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "SUCCESS:get cdn file name"
                  cdnFile = propVal
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "FAILURE:failed to get log file name"

               #Remove the exsisting logs
               result = xconfUtilityLib.removeLog(sysobj, cdnLog);
               if "SUCCESS" in result:
                  ###########excute the shell script to download firmware
                  tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                  tdkTestObj.addParameter("command", cdnFile + " > /dev/null 2>&1 &");
                  tdkTestObj.executeTestCase("SUCCESS");

                  result = tdkTestObj.getResult();
                  details = tdkTestObj.getResultDetails();
                  #wait till log updation
                  sleep(50)
                  if "SUCCESS" in result:
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 4: Initiate firmware download"
                     print "EXPECTED RESULT 4: firmware download should be initiated"
                     print "ACTUAL RESULT 4: is %s " %details
                     print "[TEST EXECUTION RESULT] : SUCCESS"

                     sleep(20);

                     lineCountResult1, lineCountAfterSimu = getTelLogFileTotalLinesCount(tdkTestObj_Sys_ExeCmd);
                     if expectedresult in lineCountResult and  int(lineCountAfterSimu) > int(initialLinesCount):
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Get the line count of telemetry log file and compare the value with initialLinesCount";
                        print "EXPECTED RESULT 5: Line count After Simulation should be greater than the initialLinesCount";
                        print "ACTUAL RESULT 5: Line count After Simulation is greater than the initialLinesCount";
                        print "[TEST EXECUTION RESULT] 5: SUCCESS";

                        print "Line count of Telemetry Log File After Simulation is ",lineCountAfterSimu

                        query = "sed -n -e %s,%sp /rdklogs/logs/telemetry2_0.txt.0 | grep -i \"Received eventInfo : XCONF_Dwld_failed\"" %(initialLinesCount,lineCountAfterSimu)
                        print "query:%s" %query
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        tdkTestObj.addParameter("command", query);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                        print "Marker Detail Found from log file is: %s "%details;

                        if expectedresult in actualresult and details!="" and (len(details) > 0) and "XCONF_Dwld_failed" in details:
                           tdkTestObj.setResultStatus("SUCCESS");
                           markervalue = details.split("XCONF_Dwld_failed value : ")[1]
                           print "TEST STEP 6: XCONF_Dwld_failed  Marker should be present";1
                           print "EXPECTED RESULT 6: XCONF_Dwld_failed Marker should be present";
                           print "ACTUAL RESULT 6: XCONF_Dwld_failed  Marker Value is %s" %markervalue;
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] 6: SUCCESS";
                           print "***************************************************************"
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: XCONF_Dwld_failed  Marker should be present";
                            print "EXPECTED RESULT 6: XCONF_Dwld_failed Marker should be present";
                            print "ACTUAL RESULT 6: XCONF_Dwld_failed  Marker is %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                            print "***************************************************************"
                     else:
                         tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                         print "TEST STEP 5: Get the line count of telemetry log file and compare the value with initialLinesCount";
                         print "EXPECTED RESULT 5: Line count After Simulation should be greater than the initialLinesCount";
                         print "ACTUAL RESULT 5: Line count After Simulation is NOT greater than the initialLinesCount";
                         print "[TEST EXECUTION RESULT] : FAILURE";

                     ###########restore the override file
                     xconfUtilityLib.restoreOverrideFile(sysobj, xconfFile);

                  else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print "TEST STEP 4: Initiate firmware download"
                      print "EXPECTED RESULT 4: firmware download should be initiated"
                      print "ACTUAL RESULT 4: is %s " %details
                      print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Execute curl cmnd to  add device configuration"
                print "EXPECTED RESULT 3: Should add device configuration"
                print "ACTUAL RESULT 3: Status: %s " %details
                print "[TEST EXECUTION RESULT] :FAILURE:Failed to execute Curl Command";
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
