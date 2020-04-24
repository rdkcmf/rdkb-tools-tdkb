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
  <version>5</version>
  <name>TS_EPONHAL_SetClearOnuLinkStatistics</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_SetClearOnuLinkStatistics</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Onu Link statistics value for Tx and Rx frame rate are cleared on performing dpoe_setClearOnuLinkStatistics.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_EPONHAL_26</test_case_id>
    <test_objective>Check the functonality of dpoe_setClearOnuLinkStatistics</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_setClearOnuLinkStatistics</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load eponhal module
2. Get the initial  tx frame rate and Rx frame rate
3. invoke dpoe_setClearOnuLinkStatistics from the script
4. Invoke dpoe_getOnuLinkStatistics  and get the tx and Rx frame rate.
5. The frame rate for Tx and Rx value should decrease after dpoe_setClearOnuLinkStatistics
6. Unload eponhal module</automation_approch>
    <expected_output>The dpoe_setClearOnuLinkStatistics should clear the onu link statistics</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_SetClearOnuLinkStatistics</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_SetClearOnuLinkStatistics');
tr181obj.configureTestCase(ip,port,'TS_EPONHAL_SetClearOnuLinkStatistics');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
tr181loadmodulestatus =tr181obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %tr181loadmodulestatus ;

if "SUCCESS" in (loadmodulestatus.upper() and  tr181loadmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = tr181obj.createTestStep("TDKB_TR181Stub_Get");
    tdkTestObj.addParameter("ParamName","Device.DPoE.DPoE_OnuLinkStatisticsNumberOfEntries");
    expectedresult ="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    numEntries = " ";
    numEntries = tdkTestObj.getResultDetails();
    numEntries = int(numEntries)
    if expectedresult in actualresult and numEntries != " " and  numEntries >0:
       print "TEST STEP 1: Get the Number of entries for OnuLinkStatistics";
       print "EXPECTED RESULT 1: Should get the OnuLinkStatistics  value as greater than 0";
       print "ACTUAL RESULT 1: The OnuLinkStatistics  value  is :",numEntries;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj.setResultStatus("SUCCESS");


       tdkTestObj = tr181obj.createTestStep("TDKB_TR181Stub_Get");
       tdkTestObj.addParameter("ParamName","Device.DPoE.DPoE_OnuLinkStatistics.1.rxUnicastFrames");
       expectedresult ="SUCCESS"
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       RxFrames = " ";
       RxFrames = tdkTestObj.getResultDetails();
       RxFrames = int(RxFrames);

       if expectedresult in actualresult:
          print "TEST STEP 2: Get the Number of entries for Rx Unicast Frames";
          print "EXPECTED RESULT 2: Should get the number of Rx Unicast Frames  ";
          print "ACTUAL RESULT 2: The number of Rx Unicast Frames  is :",RxFrames;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
          tdkTestObj.setResultStatus("SUCCESS");


          tdkTestObj = tr181obj.createTestStep("TDKB_TR181Stub_Get");
          tdkTestObj.addParameter("ParamName","Device.DPoE.DPoE_OnuLinkStatistics.1.txUnicastFrames");
          expectedresult ="SUCCESS"
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          TxFrames = " ";
          TxFrames = tdkTestObj.getResultDetails();
          TxFrames = int(TxFrames);

          if expectedresult in actualresult:
             print "TEST STEP 3: Get the Number of entries for Tx Unicast Frames";
             print "EXPECTED RESULT 3: Should get the number of Tx Unicast Frames  ";
             print "ACTUAL RESULT 3: The number of Tx Unicast Frames  is :",TxFrames;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";
             tdkTestObj.setResultStatus("SUCCESS");

             #Script to load the configuration file of the component
             tdkTestObj = obj.createTestStep('EPONHAL_SetClearOnuLinkStatistics');
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();

             if expectedresult in actualresult :
                print "TEST STEP 4: Check for successful invocation of dpoe_setClearOnuLinkStatistics";
                print "EXPECTED RESULT 4: Should succesfully invoke dpoe_setClearOnuLinkStatistics";
                print "ACTUAL RESULT 4:Sucessfully invoke dpoe_setClearOnuLinkStatistics";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");


                tdkTestObj = obj.createTestStep('EPONHAL_GetOnuLinkStatistics');
                expectedresult="SUCCESS";
                tdkTestObj.addParameter("numEntries",1);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                resultDetails = " ";
                resultDetails = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 5: check for successful  invocation of dpoe_getOnuLinkStatistics";
                   print "EXPECTED RESULT 5: Should successfully invoke dpoe_getOnuLinkStatistics";
                   print "ACTUAL RESULT 5: Succesfully invoke dpoe_getOnuLinkStatistics";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";
                   #no of entries in the structure
                   n =23;
                   minonu = [];
                   for i in range(n):
                       minonu.append(resultDetails.split(':')[i+2].split(',')[0].strip())

                   print"Rx Frame rate after  dpoe_setClearOnuLinkStatistics :",minonu[0]
                   print"Tx Frame rate after  dpoe_setClearOnuLinkStatistics :",minonu[1]

                   if int(minonu[1]) < TxFrames or int(minonu[1]) == 0:
                      print "TEST STEP 6: Check if TxFrame rate is decreased after dpoe_setClearOnuLinkStatistics";
                      print "EXPECTED RESULT 6: The TxFrame rate  should decreased after dpoe_setClearOnuLinkStatistics";
                      print "ACTUAL RESULT 6: TxFrame rate  is : ",minonu[1];
                      #Get the result of execution
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                      tdkTestObj.setResultStatus("SUCCESS");

                      if int(minonu[0]) < RxFrames or int(minonu[0]) == 0:
                         print "TEST STEP 7: Check if RxFrame rate is decreased after dpoe_setClearOnuLinkStatistics";
                         print "EXPECTED RESULT 7: The RxFrame rate  should decreased after dpoe_setClearOnuLinkStatistics";
                         print "ACTUAL RESULT 7:  RxFrame rate  is : ",minonu[0];
                         #Get the result of execution
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                         tdkTestObj.setResultStatus("SUCCESS");

                      else:
                          print "TEST STEP 7: Check if RxFrame rate is decreased after dpoe_setClearOnuLinkStatistics";
                          print "EXPECTED RESULT 7: The RxFrame rate  should decreased after dpoe_setClearOnuLinkStatistics";
                          print "ACTUAL RESULT 7:  Failed to decrement the RxFrame rate value is: ",minonu[0];
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                          tdkTestObj.setResultStatus("FAILURE");
                   else:
                       print "TEST STEP 6: Check if TxFrame rate is decreased after dpoe_setClearOnuLinkStatistics";
                       print "EXPECTED RESULT 6: The TxFrame rate  should decreased after dpoe_setClearOnuLinkStatistics";
                       print "ACTUAL RESULT 6: Failed to decrement the TxFrame rate : ",minonu[1];
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                       tdkTestObj.setResultStatus("FAILURE");
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: check for successful  invocation of dpoe_getOnuLinkStatistics";
                    print "EXPECTED RESULT 5: Should successfully invoke dpoe_getOnuLinkStatistics";
                    print "ACTUAL RESULT 5: Failed to invoke dpoe_getOnuLinkStatistics";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 print "TEST STEP 4: Check for successful invocation of dpoe_setClearOnuLinkStatistics";
                 print "EXPECTED RESULT 4: Should succesfully invoke dpoe_setClearOnuLinkStatistics";
                 print "ACTUAL RESULT 4: Failed to invoke dpoe_setClearOnuLinkStatistics";
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
                 tdkTestObj.setResultStatus("FAILURE");
          else:
              print "TEST STEP 3: Get the Number of entries for Tx Unicast Frames";
              print "EXPECTED RESULT 3: Should get the number of Tx Unicast Frames  ";
              print "ACTUAL RESULT 3: The number of Tx Unicast Frames  is :",TxFrames;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] :FAILURE";
              tdkTestObj.setResultStatus("FAILURE");
       else:
           print "TEST STEP 2: Get the Number of entries for Rx Unicast Frames";
           print "EXPECTED RESULT 2: Should get the number of Rx Unicast Frames  ";
           print "ACTUAL RESULT 2: The number of Rx Unicast Frames  is :",RxFrames;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
           tdkTestObj.setResultStatus("FAILURE");

    else:
        print "TEST STEP 1: Get the Number of entries for OnuLinkStatistics";
        print "EXPECTED RESULT 1: Should get the OnuLinkStatistics  value as greater than 0";
        print "ACTUAL RESULT 1: The OnuLinkStatistics  value  is :",numEntries;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj.setResultStatus("FAILURE")


    obj.unloadModule("eponhal");
    tr181obj.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
