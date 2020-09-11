##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_MOCA_InterfaceDisabledCheckStatus</name>
  <primitive_test_id/>
  <primitive_test_name>Mocastub_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether the status is "Down" irrespective of the number of clients connected if the Interface is disabled.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_MOCA_04</test_case_id>
    <test_objective>To check whether the status is "Down" irrespective of the number of clients connected if the Interface is disabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Mocastub_Set, Mocastub_Get</api_or_interface_used>
    <input_parameters>Device.MoCA.Interface.1.X_CISCO_COM_NumberOfConnectedClients
Device.MoCA.Interface.1.Enable
Device.MoCA.Interface.1.Status
Device.DeviceInfo.X_RDKCENTRAL-COM_EnableMoCAforXi5</input_parameters>
    <automation_approch>1. Load MOCA modules
2. From script invoke Mocastub_Get to get the number of clients connected
3. Disable the MoCAforXi5 if NoofClients connected are greater than zero by invoking Mocastub_Set
4.Disable the MoCA interface by invoking Mocastub_Set
5. Get the status and check whether it is "Down"
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from Moca stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log
CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log
CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_MOCA_InterfaceDisabledCheckStatus</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("moca","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MOCA_InterfaceDisabledCheckStatus');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
revertflag =0;

def DisableMocaInterface():
    tdkTestObj = obj.createTestStep('Mocastub_Get');
    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.Enable");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default= tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP : Get Moca Interface status";
       print "EXPECTED RESULT : Should get  Moca Interface status";
       print "ACTUAL RESULT : %s" %default;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       flag =0;
       if default!="false":
          tdkTestObj = obj.createTestStep('Mocastub_Set');
          tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.Enable");
          tdkTestObj.addParameter("ParamValue","false");
          tdkTestObj.addParameter("Type","bool");
          expectedresult="SUCCESS";
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details= tdkTestObj.getResultDetails();
          if expectedresult in actualresult:
             #Set the result status of execution
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP : Disable Moca Interface";
             print "EXPECTED RESULT : Should disable Moca Interface";
             print "ACTUAL RESULT : %s" %details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             CheckStatus();
             flag =1;
             #Revert the value
             tdkTestObj = obj.createTestStep('Mocastub_Set');
             tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.Enable");
             tdkTestObj.addParameter("ParamValue",default);
             tdkTestObj.addParameter("Type","bool");
             expectedresult="SUCCESS";
             #Execute the test case in DUT
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details= tdkTestObj.getResultDetails();
             if  expectedresult in actualresult :
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP : Revert the  Moca Interface status";
                 print "EXPECTED RESULT : Should revert  Moca Interface status";
                 print "ACTUAL RESULT : %s" %details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP : Revert the  Moca Interface status";
                 print "EXPECTED RESULT : Should revert  Moca Interface status";
                 print "ACTUAL RESULT : %s" %details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              #Set the result status of execution
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP : Disable Moca Interface";
              print "EXPECTED RESULT : Should disable Moca Interface";
              print "ACTUAL RESULT : %s" %details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       #In case the Moca Interafce was disabled by default
       if flag!=1:
          CheckStatus();
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Get Moca Interface status";
        print "EXPECTED RESULT : Should get  Moca Interface status";
        print "ACTUAL RESULT : %s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    return;

def CheckStatus():
    tdkTestObj = obj.createTestStep('Mocastub_Get');
    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.Status");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Status = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and "Down" in Status:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP : Check if status is Down irrescpective of the number of conencted clients";
       print "EXPECTED RESULT :Status should be Down irrescpective of the number of conencted clients";
       print "ACTUAL RESULT : %s" %Status;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Check if status is Down irrescpective of the number of conencted clients";
        print "EXPECTED RESULT :Status should be Down irrescpective of the number of conencted clients";
        print "ACTUAL RESULT5: %s" %Status;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('Mocastub_Get');
    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.X_CISCO_COM_NumberOfConnectedClients");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoOfClients= tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the number of connected clients";
        print "EXPECTED RESULT 1: Should get the number of connected clients";
        print "ACTUAL RESULT 1: Number of connected clients is :%s" %NoOfClients;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if  int(NoOfClients) > 0 :
            tdkTestObj = obj.createTestStep('Mocastub_Get');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableMoCAforXi5");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            defaultXi5 = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 2: Get the status of MoCAforXi5";
               print "EXPECTED RESULT 2: Should get the status of MoCAforXi5";
               print "ACTUAL RESULT 2: Status of MoCAforXi5 is :%s" %defaultXi5;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";

               if defaultXi5 != "false":
                  tdkTestObj = obj.createTestStep('Mocastub_Set');
                  tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableMoCAforXi5");
                  tdkTestObj.addParameter("ParamValue","false");
                  tdkTestObj.addParameter("Type","bool");
                  expectedresult="SUCCESS";
                  #Execute the test case in DUT
                  tdkTestObj.executeTestCase(expectedresult);
                  actualresult = tdkTestObj.getResult();
                  details= tdkTestObj.getResultDetails();
                  if expectedresult in actualresult:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 3: Disable MocaforXi5";
                     print "EXPECTED RESULT 3: Should disable MocaforXi5";
                     print "ACTUAL RESULT 3: %s" %details;
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                     revertflag =1;
                     DisableMocaInterface();
                  else:
                      #Set the result status of execution
                      tdkTestObj.setResultStatus("FAILURE");
                      print "TEST STEP 3: Disable MocaforXi5";
                      print "EXPECTED RESULT 3: Should disable MocaforXi5";
                      print "ACTUAL RESULT 3: %s" %details;
                      print "[TEST EXECUTION RESULT] : FAILURE";

               #In case the MoCAforXi5 was disabled by default
               if revertflag !=1:
                  DisableMocaInterface();
            else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2: Get the status of MoCAforXi5";
               print "EXPECTED RESULT 2: Should get the status of MoCAforXi5";
               print "ACTUAL RESULT 2: Status of MoCAforXi5 is :%s" %defaultXi5;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            DisableMocaInterface();

        if revertflag ==1:
           tdkTestObj = obj.createTestStep('Mocastub_Set');
           tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableMoCAforXi5");
           tdkTestObj.addParameter("Type","bool");
           tdkTestObj.addParameter("ParamValue",defaultXi5);
           expectedresult="SUCCESS";
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details= tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 4: Revert  MocaforXi5 to previous ";
              print "EXPECTED RESULT 4: Should revert MocaforXi5 to previous";
              print "ACTUAL RESULT 4: %s" %details;
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 4: Revert  MocaforXi5 to previous ";
               print "EXPECTED RESULT 4: Should revert MocaforXi5 to previous";
               print "ACTUAL RESULT 4: %s" %details;
               print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of connected clients";
        print "EXPECTED RESULT 1: Should get the number of connected clients";
        print "ACTUAL RESULT 1: Number of connected clients is :%s" %NoOfClients;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("moca");
else:
    print "Failed to load moca module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
