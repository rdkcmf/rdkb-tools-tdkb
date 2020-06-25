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
  <version>3</version>
  <name>TS_WIFIAGENT_CheckTelemetryMarkerWith5GhzRetryAndMultipleRetryCount</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if  Retry  and Multiple Retry count via TR-181 and telemetry marker are greater than or equal to zero by Changing the Log Interval.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_113</test_case_id>
    <test_objective>This test case is to check if the Retry and Multiple Retry count via TR-181 and telemetry marker are greater than or equal to  zero by changing the log interval to 5 min</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a WiFi client to 5Ghz private SSID of DUT</pre_requisite>
    <api_or_interface_used>NA</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.2.AssociatedDevice.1.Stats.RetryCount
Device.WiFi.AccessPoint.2.AssociatedDevice.1.Stats.MultipleRetryCount Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable</input_parameters>
    <automation_approch>1.Load the module.
2.Check if telemetry markers are enabled ,if not enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.Telemetry.Enable
3.Change the log interval to 300 sec i,e 5min using Device.DeviceInfo.X_RDKCENTRAL-COM_WIFI_TELEMETRY.LogInterval
4.Check for telemetry marker WIFI_RETRYCOUNT_2 and get the bytes sent using Device.WiFi.AccessPoint.2.AssociatedDevice.1.Stats.RetryCount
5.Check if the values received are greater than or equal to zero
6.Check for telemetry marker WIFI_MULTIPLERETRYCOUNT_2 and get the bytes sent using Device.WiFi.AccessPoint.2.AssociatedDevice.1.Stats.MultipleRetryCount
7.Check if the values received are greater than or equal to zero
8. Revert the log interval value and telemetry enable status to original
9.Unload the Module
</automation_approch>
    <expected_output>The Retry and Multiple Retry count via TR-181 and telemetry marker should be greater than or equal to zero</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerWith5GhzRetryAndMultipleRetryCount</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerWith5GhzRetryAndMultipleRetryCount');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerWith5GhzRetryAndMultipleRetryCount');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
revertflag = 0;
flag =1;
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
                           query="cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_RETRYCOUNT_2:\""
                           print "query:%s" %query
                           tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                           tdkTestObj.addParameter("command", query)
                           expectedresult="SUCCESS";
                           tdkTestObj.executeTestCase(expectedresult);
                           actualresult = tdkTestObj.getResult();
                           details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                           print "Marker Detail Found fromLog file is: %s "%details;

                           if (len(details) == 0) or details.endswith(":") or "WIFI_RETRYCOUNT_2" not in details:
                              markerfound = 0;
                              sleep(60);
                           else:
                               tel_retrycount  = details.split("WIFI_RETRYCOUNT_2:")[1].split(',')[0].strip().replace("\\n","");
                               markerfound = 1;

                   if expectedresult in actualresult and markerfound == 1 and tel_retrycount != "":
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 5:WIFI_RETRYCOUNT_2 Marker should be present";
                      print "EXPECTED RESULT 5: WIFI_RETRYCOUNT_2 Marker should be present";
                      print "ACTUAL RESULT 5:WIFI_RETRYCOUNT_2 Marker is %s" %tel_retrycount;
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";


                      tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                      tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.2.AssociatedDevice.1.Stats.RetryCount");
                      expectedresult="SUCCESS";
                      #Execute the test case in DUT
                      tdkTestObj.executeTestCase(expectedresult);
                      actualresult = tdkTestObj.getResult();
                      tr181_retrycount = tdkTestObj.getResultDetails();
                      if expectedresult in actualresult:
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 6: Get the Retry count via TR-181 parameter";
                         print "EXPECTED RESULT 6: Should get the Retry count via TR-181 parameter";
                         print "ACTUAL RESULT 6:Retry count  via TR-181 parmeter:",tr181_retrycount;
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";

                         if int(tel_retrycount) >= 0 and  int(tr181_retrycount) >= 0 :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 7: Check if Retry count via TR-181 parameter and telemetry marker are greater than or equal to zero";
                            print "EXPECTED RESULT 7: Should get the Retry count  via TR-181 parameter and telemetry marker greater than or equal to zero";
                            print "ACTUAL RESULT 7: Retry count  via TR-181 parmeter:",tr181_retrycount,"Retry count in telemetry marker: ",tel_retrycount;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            markerfound = 0;
                            for i in range(1,6):
                                if markerfound == 1:
                                   break;
                                else:
                                    #Query for the Telemetry Marker
                                    query="cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_MULTIPLERETRYCOUNT_2:\""
                                    print "query:%s" %query
                                    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                                    tdkTestObj.addParameter("command", query)
                                    expectedresult="SUCCESS";
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                                    print "Marker Detail Found fromLog file is: %s "%details;
                                    if (len(details) == 0) or details.endswith(":") or "WIFI_MULTIPLERETRYCOUNT_2" not in details:
                                       markerfound = 0;
                                       sleep(60);
                                    else:
                                        tel_mretrycount = details.split("WIFI_MULTIPLERETRYCOUNT_2:")[1].split(',')[0].strip().replace("\\n","");
                                        markerfound = 1;

                            if expectedresult in actualresult and markerfound == 1 and tel_mretrycount != "":
                               tdkTestObj.setResultStatus("SUCCESS");
                               print "TEST STEP 8: WIFI_MULTIPLERETRYCOUNT_2  Marker should be present";
                               print "EXPECTED RESULT 8: WIFI_MULTIPLERETRYCOUNT_2  Marker should be present";
                               print "ACTUAL RESULT 8:WIFI_MULTIPLERETRYCOUNT_2 is %s" %tel_mretrycount;
                               #Get the result of execution
                               print "[TEST EXECUTION RESULT] : SUCCESS";

                               tdkTestObj = obj.createTestStep('pam_GetParameterValues');
                               tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.2.AssociatedDevice.1.Stats.MultipleRetryCount");
                               expectedresult="SUCCESS";
                               #Execute the test case in DUT
                               tdkTestObj.executeTestCase(expectedresult);
                               actualresult = tdkTestObj.getResult();
                               tr181_mretrycount  = tdkTestObj.getResultDetails();
                               if expectedresult in actualresult:
                                  tdkTestObj.setResultStatus("SUCCESS");
                                  print "TEST STEP 9: Get the no of Multiple Retry count via TR-181 parameter";
                                  print "EXPECTED RESULT 9: Should get the Multiple Retry count via TR-181 parameter";
                                  print "ACTUAL RESULT 9: Multiple Retry count via TR-181 parmeter:",tr181_mretrycount;
                                  #Get the result of execution
                                  print "[TEST EXECUTION RESULT] : SUCCESS";

                                  if int(tel_mretrycount) >= 0 and  int(tr181_mretrycount) >= 0 :
                                     tdkTestObj.setResultStatus("SUCCESS");
                                     print "TEST STEP 10: Check if  Multiple Retry count via TR-181 parameter and telemetry marker are greater than or equal to zero";
                                     print "EXPECTED RESULT 10: Should get  Multiple Retry count via TR-181 parameter and telemetry marker greater than or equal to zero";
                                     print "ACTUAL RESULT 10:  Multiple Retry count via TR-181 parmeter:",tr181_mretrycount," Multiple Retry count in telemetry marker: ",tel_mretrycount;
                                     #Get the result of execution
                                     print "[TEST EXECUTION RESULT] : SUCCESS";
                                  else:
                                      tdkTestObj.setResultStatus("FAILURE");
                                      print "TEST STEP 10: Check if Multiple Retry count via TR-181 parameter and telemetry marker are greater than or equal to zero";
                                      print "EXPECTED RESULT 10: Should get Multiple Retry count via TR-181 parameter and telemetry marker greater than or equal to zero";
                                      print "ACTUAL RESULT 10: Multiple Retry count via TR-181 parmeter:",tr181_mretrycount,"Multiple Retry count in telemetry marker:",tel_mretrycount;
                                      #Get the result of execution
                                      print "[TEST EXECUTION RESULT] : FAILURE";
                               else:
                                   tdkTestObj.setResultStatus("FAILURE");
                                   print "TEST STEP 9: Get the Multiple Retry count via TR-181 parameter";
                                   print "EXPECTED RESULT 9: Should get theMultiple Retry count via TR-181 parameter";
                                   print "ACTUAL RESULT 9: Multiple Retry count via TR-181 parmeter:",tr181_mretrycount;
                                   #Get the result of execution
                                   print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 8: WIFI_MULTIPLERETRYCOUNT_2  Marker should be present";
                                print "EXPECTED RESULT 8: WIFI_MULTIPLERETRYCOUNT_2  Marker should be present";
                                print "ACTUAL RESULT 8:WIFI_MULTIPLERETRYCOUNT_2 is not present"
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                         else:
                             tdkTestObj.setResultStatus("FAILURE");
                             print "TEST STEP 7: Check if Retry count via TR-181 parameter and telemetry marker are greater than or equal to zero";
                             print "EXPECTED RESULT 7: Should get the Retry count  via TR-181 parameter and telemetry marker greater than or equal to zero";
                             print "ACTUAL RESULT 7: Retry count via TR-181 parmeter:",tr181_retrycount,"Retry count in telemetry marker: ",tel_retrycount;
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] : FAILURE";
                      else:
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 6: Get the Retry count via TR-181 parameter";
                          print "EXPECTED RESULT 6: Should get the Retry count via TR-181 parameter";
                          print "ACTUAL RESULT 6: Retry count via TR-181 parmeter:",tr181_retrycount;
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 5: WIFI_RETRYCOUNT_2 Marker should be present";
                       print "EXPECTED RESULT 5: WIFI_RETRYCOUNT_2 Marker should be present";
                       print "ACTUAL RESULT 5:WIFI_RETRYCOUNT_2 Marker not present"
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
                   print "TEST STEP 11: Revert the TELEMETRY LogInterval to previous";
                   print "EXPECTED RESULT 11: Should revert the TELEMETRY LogInterval to previous";
                   print "ACTUAL RESULT 11: Revert successfull";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 11: Revert the TELEMETRY LogInterval to previous";
                    print "EXPECTED RESULT 11: Should revert the TELEMETRY LogInterval to previous";
                    print "ACTUAL RESULT 11: Revertion failed";
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
                print "TEST STEP 12: Revert the Telemetry Enable status to previous";
                print "EXPECTED RESULT 12: Should revert the Telemetry Enable status to previous";
                print "ACTUAL RESULT 12: Revert successfull";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 12: Revert the Telemetry Enable status to previous";
                 print "EXPECTED RESULT 12: Should revert the Telemetry Enable status to previous";
                 print "ACTUAL RESULT 12: Revertion failed";
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
    obj.unloadModule("pam");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
