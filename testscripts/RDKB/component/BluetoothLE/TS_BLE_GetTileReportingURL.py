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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_BLE_GetTileReportingURL</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>BLE_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL and check if the url is non-empty</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_BluetoothLE_1</test_case_id>
    <test_objective>Get Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL and check if the url is non-empty</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>TDK agent should be running in the DUT and DUT should be online in TDK test manager</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL
3. Check if url from Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL is non-empty
4. Unload tdkbtr181 module</automation_approch>
    <expected_output>Url from Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL should be non-empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_BLE_GetTileReportingURL</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_BLE_GetTileReportingURL');
sysobj.configureTestCase(ip,port,'TS_BLE_GetTileReportingURL');
#Get the result of connection with test component and STB
loadmodulestatus=obj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS"
    cmd= "cat /tmp/rfc_configdata.txt  | grep -i tr181.Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLERadio#~";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "details:",details
    if details != "":
       Mode = details.split("#~")[1].split(' ')[0].rstrip(" ");
       print "Mode:",Mode
    
       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
       tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BLE.Tile.ReportingURL");
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       tileReportingURL = tdkTestObj.getResultDetails().strip().replace("\\n", "")

       if expectedresult in actualresult :
          if Mode == "true":
             if tileReportingURL != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1: Get the BLE TileReportingURL";
                print "EXPECTED RESULT 1: Should get a non-empty BLE TileReportingURL";
                print "ACTUAL RESULT 1: BLE TileReportingURL is %s" %tileReportingURL;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 1: Get the BLE TileReportingURL";
                 print "EXPECTED RESULT 1: Should get a non empty BLE TileReportingURL";
                 print "ACTUAL RESULT 1: BLE TileReportingURL is %s" %tileReportingURL;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";

          else:

              if tileReportingURL == "":

                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 1: Get the BLE TileReportingURL";
                 print "EXPECTED RESULT 1: Should get a empty BLE TileReportingURL";
                 print "ACTUAL RESULT 1: BLE TileReportingURL is %s" %tileReportingURL;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";               
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 1: Get the BLE TileReportingURL";
                  print "EXPECTED RESULT 1: Should get the empty BLE TileReportingURL";
                  print "ACTUAL RESULT 1: BLE TileReportingURL is %s" %tileReportingURL;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
    else:
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 1: Get  whether the  BLE is enabled form rfc_configdata.txt";
         print "EXPECTED RESULT 1: Should get whether BLE feature is enabled from the logs ";
         print "ACTUAL RESULT 1: BLE radio status is :" %details;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";


    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";



