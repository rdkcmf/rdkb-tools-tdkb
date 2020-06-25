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
  <name>TS_WIFIAGENT_CheckTelemetryMarkerVAPPERCENTUP</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check for telemetry marker WIFI_VAP_PERCENT_UP  and it should return non empty values and VAP PERCENT should be within the range by changing the Log interval.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_109</test_case_id>
    <test_objective>This test case is to check if the telemetry marker WIFI_VAP_PERCENT_UP  percent  listed  are within the range by changing the Log Interval</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a WiFi client to DUT</pre_requisite>
    <api_or_interface_used>NA</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable</input_parameters>
    <automation_approch>1.Load the module.
2.Check if telemetry markers are enabled ,if not enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
3.Change the log interval to 300 sec i,e 5min using Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
4.Check whether wifihealth.txt file is present or not
5.Grep WIFI_VAP_PERCENT_UP  in wifihealth.txt file and it should be non empty values
6.Loop through and check all the 16 instances present in marker are within the range.
7.Revert the log interval value and telemetry enable status to original
8.Unload module</automation_approch>
    <expected_output>WIFI_VAP_PERCENT_UP should be present  and it's all the 16 instances percentage should be within the range </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerVAPPERCENTUP</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerVAPPERCENTUP');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerVAPPERCENTUP');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
revertflag = 0;
flag =1;
VAPflag = 1;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    logEnable  = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Telemetry Enable state ";
       print "EXPECTED RESULT 1: Should get the TELEMETRY Enable state";
       print "ACTUAL RESULT 1: TELEMETRY Enable state :",logEnable;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       if logEnable == "false":
          tdkTestObj = obj.createTestStep('pam_SetParameterValues');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable");
          tdkTestObj.addParameter("ParamValue","true");
          tdkTestObj.addParameter("Type","bool");
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();
          if expectedresult in actualresult:
             flag =1;
             revertflag =1;
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Set the Telemetry Enable state to true";
             print "EXPECTED RESULT 2: Should set the TELEMETRY Enable state to true";
             print "ACTUAL RESULT 2: TELEMETRY Enable state :",details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
          else:
              flag =0;
              revertflag =0;
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Set the Telemetry Enable state to true";
              print "EXPECTED RESULT 2: Should set the TELEMETRY Enable state to true";
              print "ACTUAL RESULT 2: TELEMETRY Enable state :",details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";

       if flag == 1:
          tdkTestObj = obj.createTestStep('pam_GetParameterValues');
          tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          DeflogInt = tdkTestObj.getResultDetails();
          if expectedresult in actualresult:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Get the TELEMETRY LogInterval";
             print "EXPECTED RESULT 2: Should get the TELEMETRY LogInterval";
             print "ACTUAL RESULT 2: TELEMETRY LogInterval:",DeflogInt;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = obj.createTestStep('pam_SetParameterValues');
             tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval");
             tdkTestObj.addParameter("ParamValue","300");
             tdkTestObj.addParameter("Type","int");
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails();
             if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Set the TELEMETRY LogInterval to 5 min";
                print "EXPECTED RESULT 3: Should set the TELEMETRY LogInterval to 5 min";
                print "ACTUAL RESULT 3: TELEMETRY LogInterval:",details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check whether the wifihealth.txt file is present or not
                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
                tdkTestObj.addParameter("command",cmd);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if details == "File exist":
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 4: Check for wifihealth log file presence";
                   print "EXPECTED RESULT 4:wifihealth log file should be present";
                   print "ACTUAL RESULT 4:wifihealth log file is present";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   markerfound = 0;
                   for i in range(1,6):
                       if markerfound == 1:
                          break;
                       else:
                           #Query for the Telemetry Marker
                           query="cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_VAP_PERCENT_UP:\""
                           print "query:%s" %query
                           tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                           tdkTestObj.addParameter("command", query)
                           expectedresult="SUCCESS";
                           tdkTestObj.executeTestCase(expectedresult);
                           actualresult = tdkTestObj.getResult();
                           details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                           print "Marker Detail Found fromLog file is: %s "%details;

                           if (len(details) == 0) or details.endswith(":") or "WIFI_VAP_PERCENT_UP" not in details:
                              markerfound = 0;
                              sleep(60);
                           else:
                               tel_vap = details.split("WIFI_VAP_PERCENT_UP:")[1].split(',')[0].strip().replace("\\n","");
                               markerfound = 1;

                   if expectedresult in actualresult and markerfound == 1 and tel_vap!="":
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 5:WIFI_VAP_PERCENT_UP  Marker should be present";
                      print "EXPECTED RESULT 5: WIFI_VAP_PERCENT_UP Marker should be present";
                      print "ACTUAL RESULT 5:WIFI_VAP_PERCENT_UP Marker is %s" %tel_vap;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                      inst  =0;
                      Flist =[];
                      for inst in range (1,17):
                          checkvalue = int(details.split(",")[inst].split(";")[0].strip().replace("\\n",""));
                          print "Checking if WIFIVAP :%d is within the range "%inst;

                          if 0 <= checkvalue <= 100:
                             print "WIFIVAP:%d is %d is within the range"%(inst,checkvalue);
                             VAPflag =1;
                          else:
                              print "WIFIVAP:%d is %d is not within the range" %(inst,checkvalue);
                              VAPflag =0;
                              Flist.append(inst);
                      if VAPflag == 1:
                         print "TEST STEP 6: Check  if WIFI_VAP 's are within the range";
                         print "EXPECTED RESULT 6: WIFI_VAP should be within the range";
                         print "ACTUAL RESULT 6: All WIFI_VAP_PERCENT's are within the range"
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                         print "TEST STEP 6: Check  if WIFI_VAP 's are within the range";
                         print "EXPECTED RESULT 6: WIFI_VAP should be within the range";
                         print "ACTUAL RESULT 6: WIFI_VAP_PERCENT's are not within the range at :",Flist;
                         tdkTestObj.setResultStatus("FAILURE");
                         print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 5: WIFI_VAP_PERCENT_UP Marker should be present";
                       print "EXPECTED RESULT 5: WIFI_VAP_PERCENT_UP  Marker should be present";
                       print "ACTUAL RESULT 5:WIFI_VAP_PERCENT_UP not present"
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Check for wifihealth log file presence";
                    print "EXPECTED RESULT 4:wifihealth log file should be present";
                    print "ACTUAL RESULT 4:wifihealth log file is not present";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                #Revert the Value
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval");
                tdkTestObj.addParameter("ParamValue",DeflogInt);
                tdkTestObj.addParameter("Type","int");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 7: Revert the TELEMETRY LogInterval to previous";
                   print "EXPECTED RESULT 7: Should revert the TELEMETRY LogInterval to previous";
                   print "ACTUAL RESULT 7: Revert successfull";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 7: Revert the TELEMETRY LogInterval to previous";
                    print "EXPECTED RESULT 7: Should revert the TELEMETRY LogInterval to previous";
                    print "ACTUAL RESULT 7: Revertion failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Set the TELEMETRY LogInterval to 5 min";
                 print "EXPECTED RESULT 3: Should set the TELEMETRY LogInterval to 5 min";
                 print "ACTUAL RESULT 3: TELEMETRY LogInterval:",details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Get the TELEMETRY LogInterval";
              print "EXPECTED RESULT 2: Should get the TELEMETRY LogInterval";
              print "ACTUAL RESULT 2: TELEMETRY LogInterval:",DeflogInt;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] :FAILURE";
          if revertflag == 1:
             #Revert the value
             tdkTestObj = obj.createTestStep('pam_SetParameterValues');
             tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable");
             tdkTestObj.addParameter("ParamValue",logEnable);
             tdkTestObj.addParameter("Type","bool");
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails();
             if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 8: Revert the Telemetry Enable status to previous";
                print "EXPECTED RESULT 8: Should revert the Telemetry Enable status to previous";
                print "ACTUAL RESULT 8: Revert successfull";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 8: Revert the Telemetry Enable status to previous";
                 print "EXPECTED RESULT 8: Should revert the Telemetry Enable status to previous";
                 print "ACTUAL RESULT 8: Revertion failed";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           print " Telemetry logger was disbled and failed on enabling"
           tdkTestObj.setResultStatus("FAILURE");
           print "[TEST EXECUTION RESULT] :FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Telemetry Enable state ";
        print "EXPECTED RESULT 1: Should get the TELEMETRY Enable state";
        print "ACTUAL RESULT 1: TELEMETRY Enable state :",logEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam")
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
