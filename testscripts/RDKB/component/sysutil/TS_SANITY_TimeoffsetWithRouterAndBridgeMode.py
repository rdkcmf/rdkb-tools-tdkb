##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_SANITY_TimeoffsetWithRouterAndBridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Time offset value received is a non-zero value in  router and bridge mode</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_SYSUTIL_53</test_case_id>
    <test_objective>This test case is to check if Time offset value received is a non-zero value in  router and bridge mode</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
Device.Time.TimeOffset</input_parameters>
    <automation_approch>1.Load the module
2.Get the current lan mode of the device
3.Get the Time offset  with current mode and is expected to be a non-zero value
4.Toggle the lan mode to a opposite ,router or bridge mode
5.Time offset  with current mode also is expected to be a non-zero value
6.Unload the module</automation_approch>
    <expected_output>Timeoffset is expected to be a non-zero value in both router and bridge mode</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_TimeoffsetWithRouterAndBridgeMode</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_TimeoffsetWithRouterAndBridgeMode');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanmodeInitial = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the lanmode";
        print "EXPECTED RESULT 1: Should get the lanmode";
        print "ACTUAL RESULT 1: Lanmode is :",lanmodeInitial;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.Time.TimeOffset");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and details!= "0":
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Get the non-zero TimeOffset value with current mode";
           print "EXPECTED RESULT 2: Should get non-zero TimeOffset";
           print "ACTUAL RESULT 2: TimeOffset value is %s" %details;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";

           if lanmodeInitial == "bridge-static":
               setValue = "router";
           else:
                setValue = "bridge-static";

           tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
           tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
           tdkTestObj.addParameter("ParamValue",setValue);
           tdkTestObj.addParameter("Type","string");
           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Changing the lanmode to %s"%setValue;
              print "EXPECTED RESULT 3: Should set the lanmode";
              print "ACTUAL RESULT 3: %s" %details;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";

              tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
              tdkTestObj.addParameter("ParamName","Device.Time.TimeOffset");
              expectedresult="SUCCESS";
              sleep(20);
              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details  = tdkTestObj.getResultDetails();

              if expectedresult in actualresult and details != "0":
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 4: Get the non-zero TimeOffset value with current mode";
                  print "EXPECTED RESULT 4: Should get non-zero TimeOffset";
                  print "ACTUAL RESULT 4: TimeOffset value is %s" %details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 4: Get the non-zero TimeOffset value with current mode";
                  print "EXPECTED RESULT 4: Should get non-zero TimeOffset";
                  print "ACTUAL RESULT 4: TimeOffset value is %s" %details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";

              #Set lan mode to previous value
              tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
              tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
              tdkTestObj.addParameter("ParamValue",lanmodeInitial);
              tdkTestObj.addParameter("Type","string");

              #Execute the test case in DUT
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details = tdkTestObj.getResultDetails();

              if expectedresult in actualresult:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 5: Set the lanmode to previous value";
                  print "EXPECTED RESULT 5: Should set the lanmode to previous value";
                  print "ACTUAL RESULT 5: %s" %details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 5: Set the lanmode to previous value";
                  print "EXPECTED RESULT 5: Should set the lanmode to previous value";
                  print "ACTUAL RESULT 5: %s" %details;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Changing the lanmode to %s"%setValue;
               print "EXPECTED RESULT 3: Should set the lanmode";
               print "ACTUAL RESULT 3: %s" %details;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the non-zero TimeOffset value with current mode";
           print "EXPECTED RESULT 2: Should get non-zero TimeOffset";
           print "ACTUAL RESULT 2: TimeOffset value is %s" %details;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the lanmode";
        print "EXPECTED RESULT 1: Should get the lanmode";
        print "ACTUAL RESULT 1: Lanmode is :",lanmodeInitial;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed"
