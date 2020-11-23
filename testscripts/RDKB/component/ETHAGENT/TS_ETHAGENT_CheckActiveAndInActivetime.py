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
  <version>2</version>
  <name>TS_ETHAGENT_CheckActiveAndInActivetime</name>
  <primitive_test_id/>
  <primitive_test_name>ETHAgent_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the active LAN client is having valid active and inactive time </synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_ETHAGENT_10</test_case_id>
    <test_objective>This test case is to check if the active LAN client is having valid active and inactive time</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.Hosts.HostNumberOfEntries
Device.Hosts.Host.{i}.Layer1Interface
Device.Hosts.Host.{i}.Active
Device.Hosts.Host.{i}.X_CISCO_COM_ActiveTime
Device.Hosts.Host.{i}.X_CISCO_COM_InactiveTime</input_parameters>
    <automation_approch>1.Load the module
2.Get the number of clients connected using Device.Hosts.HostNumberOfEntries
3.Check if the client is Ethernet using Device.Hosts.Host.{i}.Layer1Interface
4.Check if the device is active
5.Get the active and inactive time of client using Device.Hosts.Host.{i}.X_CISCO_COM_ActiveTime and
Device.Hosts.Host.{i}.X_CISCO_COM_InactiveTime and the value recieved  should be greater than zero
6.Unload the module</automation_approch>
    <expected_output>Device.Hosts.Host.{i}.X_CISCO_COM_ActiveTime and
Device.Hosts.Host.{i}.X_CISCO_COM_InactiveTime should not hold a negative value of time</expected_output>
    <priority>High</priority>
    <test_stub_interface>ETHAGENT</test_stub_interface>
    <test_script>TS_ETHAGENT_CheckActiveAndInActivetime</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_ETHAGENT_CheckActiveAndInActivetime');

#Get the result of connection with test component and DUT
loadmodulestatus=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj1.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Hosts.HostNumberOfEntries");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoofHost=tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and int(NoofHost) >0:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the number of clients connected";
       print "EXPECTED RESULT 1: Should get the no of clients connected"
       print "ACTUAL RESULT 1:%s" %NoofHost
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       Ethclientfound = 0;
       for i in range (1,int(NoofHost)+1):
           expectedresult="SUCCESS";
           tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
           tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Layer1Interface"%(i));
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
           print "Device.Hosts.Host.%s.Layer1Interface value is %s" %(i,details);
           if expectedresult in actualresult and details == "Ethernet":
              tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
              tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Active"%(i));
              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
              print "Device.Hosts.Host.%s.Active value is %s" %(i,details);
              if  expectedresult in actualresult and details == "true":
                  Ethclientfound = 1;
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP : Check if the connected LAN client is active";
                  print "EXPECTED RESULT : Should get the connected client as active";
                  print "ACTUAL RESULT :%s" %details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";
                  break;
       if Ethclientfound == 1:
          tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
          tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.X_CISCO_COM_ActiveTime"%(i));
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
          if expectedresult in actualresult  and int(details)>=0:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 2: Check if the Active time is greater than zero";
             print "EXPECTED RESULT 2: Should get the Active time greater than zero";
             print "ACTUAL RESULT 2:%s" %details;
             #Get the result of execution
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
             tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.X_CISCO_COM_InactiveTime"%(i));
             #Execute the test case in DUT
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
             if expectedresult in actualresult  and int(details)>=0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Check if the Inactive time is greater than zero";
                print "EXPECTED RESULT 3: Should get the Inactive time greater than zero";
                print "ACTUAL RESULT 3:%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 3: Check if the Inactive time is greater than zero";
                 print "EXPECTED RESULT 3: Should get the Inactive time greater than zero";
                 print "ACTUAL RESULT 3:%s" %details;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 2: Check if the Active time is greater than zero";
              print "EXPECTED RESULT 2: Should get the Active time greater than zero";
              print "ACTUAL RESULT 2:%s" %details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Check if the Active LAN Client is present";
            print "EXPECTED RESULT 2: Should Check if Active LAN Client is Associated with DUT";
            print "ACTUAL RESULT 2:No LAN Client is Associated with DUT";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of LAN clients connected";
        print "EXPECTED RESULT 1: Should get the number of LAN clients connected";
        print "ACTUAL RESULT 1:No clients associated with DUT %s" %NoofHost
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
