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
  <name>TS_WIFIAGENT_ForceDisable_DisableAndCheckRadioEnable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if 2.4G and 5G radio gets disabled when WiFi Force Disable is enabled .</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIAGENT_125</test_case_id>
    <test_objective>This test case is to check if  2.4G and 5G radio gets disabled when WiFi Force Disable is enabled .</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get
WIFIAgent_Set
</api_or_interface_used>
    <input_parameters>Device.WiFi.Radio.1.Enable
Device.WiFi.Radio.2.Enable
Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current status of Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable,Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable
3.Enable Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable
4.Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable  should be disabled
5.Revert the  Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable to previous
6.Verify that Device.WiFi.Radio.1.Enable and Device.WiFi.Radio.2.Enable also go to previous after revert operation
7.Unload the module</automation_approch>
    <expected_output>On Enabling Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable 2.4G and 5G radio should be disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_ForceDisable_DisableAndCheckRadioEnable</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_ForceDisable_DisableAndCheckRadioEnable');
#result of connection with test component and DUT
result =obj.getLoadModuleResult();
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult ="SUCCESS";
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    defaultRadio1 = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
       defaultRadio1 = defaultRadio1.split("VALUE:")[1].split(" ")[0].strip();
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Radio Enable status for 2.4GHz";
       print "EXPECTED RESULT 1: Should get the Radio Enable status for 2.4GHz";
       print "ACTUAL RESULT 1: Radio Enable status for 2.4GHz state is %s" %defaultRadio1;
       print "[TEST EXECUTION RESULT] : SUCCESS";

       tdkTestObj = obj.createTestStep('WIFIAgent_Get');
       tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Enable")
       tdkTestObj.executeTestCase("expectedresult");
       actualresult = tdkTestObj.getResult();
       defaultRadio2 = tdkTestObj.getResultDetails();
       if expectedresult in actualresult:
          defaultRadio2 = defaultRadio2.split("VALUE:")[1].split(" ")[0].strip();
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Get the Radio Enable status for 5GHz";
          print "EXPECTED RESULT 2: Should get the Radio Enable status for 5GHz";
          print "ACTUAL RESULT 2: Radio Enable status for 5GHz state is %s" %defaultRadio2;
          print "[TEST EXECUTION RESULT] : SUCCESS";

          tdkTestObj = obj.createTestStep('WIFIAgent_Get');
          tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
          tdkTestObj.executeTestCase("expectedresult");
          actualresult = tdkTestObj.getResult();
          default = tdkTestObj.getResultDetails();
          if expectedresult in actualresult:
             default = default.split("VALUE:")[1].split(" ")[0].strip();
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the current WiFi Force Disable state";
             print "EXPECTED RESULT 3: Should get current WiFi Force Disable state";
             print "ACTUAL RESULT 3: current WiFi Force Disable state is %s" %default;
             print "[TEST EXECUTION RESULT] : SUCCESS";

             tdkTestObj = obj.createTestStep('WIFIAgent_Set');
             tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
             tdkTestObj.addParameter("paramValue", "true");
             tdkTestObj.addParameter("paramType","boolean")
             tdkTestObj.executeTestCase("expectedresult");
             actualresult = tdkTestObj.getResult();
             details = tdkTestObj.getResultDetails();

             if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Enable the WiFi Force Disable";
                print "EXPECTED RESULT 4: Should enable Force Disable state";
                print "ACTUAL RESULT 4: %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                Radio1 = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and "false" in Radio1:
                   Radio1 = Radio1.split("VALUE:")[1].split(" ")[0].strip();
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 5: Get the Radio Enable status for 2.4GHz as false";
                   print "EXPECTED RESULT 5: Should get the Radio Enable status for 2.4GHz as false";
                   print "ACTUAL RESULT 5: Radio Enable status for 2.4GHz state is %s" %Radio1;
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                   tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Enable")
                   tdkTestObj.executeTestCase("expectedresult");
                   actualresult = tdkTestObj.getResult();
                   Radio2 = tdkTestObj.getResultDetails();
                   if expectedresult in actualresult and "false" in Radio2:
                      Radio2 = Radio2.split("VALUE:")[1].split(" ")[0].strip();
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 6: Get the Radio Enable status for 5GHz as false";
                      print "EXPECTED RESULT 6: Should get the Radio Enable status for 5GHz as false";
                      print "ACTUAL RESULT 6: Radio Enable status for 5GHz state is %s" %Radio2;
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 6: Get the Radio Enable status for 5GHz as false";
                       print "EXPECTED RESULT 6: Should get the Radio Enable status for 5GHz as false";
                       print "ACTUAL RESULT 6: Radio Enable status for 5GHz state is %s" %Radio2;
                       print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Get the Radio Enable status for 2.4GHz as false";
                    print "EXPECTED RESULT 5: Should get the Radio Enable status for 2.4GHz as false";
                    print "ACTUAL RESULT 5: Radio Enable status for 2.4GHz state is %s" %Radio1;
                    print "[TEST EXECUTION RESULT] : FAILURE";
                #Revert the value
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK-CENTRAL_COM_ForceDisable")
                tdkTestObj.addParameter("paramValue", default);
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 7: Revert the WiFi Force Disable status to previous";
                   print "EXPECTED RESULT 7: Should disable WiFi Force Disable status to %s" %default;
                   print "ACTUAL RESULT 7: %s" %details;
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                   tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable")
                   tdkTestObj.executeTestCase("expectedresult");
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();
                   if expectedresult in actualresult and defaultRadio1 in  details:
                      details = details.split("VALUE:")[1].split(" ")[0].strip();
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "TEST STEP 8: Check if Radio enable status for 2.4GHz is in previous state after reverting WiFi Force Disable";
                      print "EXPECTED RESULT 8: Radio enable status for 2.4GHz should be in previous state after reverting WiFi Force Disable";
                      print "ACTUAL RESULT 8: default value was :%s and after revertion %s" %(defaultRadio1,details)
                      print "[TEST EXECUTION RESULT] : SUCCESS";

                      tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                      tdkTestObj.addParameter("paramName","Device.WiFi.Radio.2.Enable")
                      tdkTestObj.executeTestCase("expectedresult");
                      actualresult = tdkTestObj.getResult();
                      details = tdkTestObj.getResultDetails();
                      if expectedresult in actualresult and defaultRadio2 in details:
                         details = details.split("VALUE:")[1].split(" ")[0].strip();
                         tdkTestObj.setResultStatus("SUCCESS");
                         print "TEST STEP 9: Check if Radio enable status for 5GHz is in previous state after reverting WiFi Force Disable";
                         print "EXPECTED RESULT 9: Radio enable status for 5GHz should be in previous state after reverting WiFi Force Disable";
                         print "ACTUAL RESULT 9: default value was :%s and after revertion %s" %(defaultRadio2,details)
                         print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                         tdkTestObj.setResultStatus("FAILURE");
                         print "TEST STEP 9: Check if Radio enable status for 5GHz is in previous state after reverting WiFi Force Disable";
                         print "EXPECTED RESULT 9: Radio enable status for 5GHz should be in previous state after reverting WiFi Force Disable";
                         print "ACTUAL RESULT 9: default value was :%s and after revertion %s" %(defaultRadio2,details)
                         print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print "TEST STEP 8: Check if Radio enable status for 2.4GHz is in previous state after reverting WiFi Force Disable";
                      print "EXPECTED RESULT 8: Radio enable status for 2.4GHz should be in previous state after reverting WiFi Force Disable";
                      print "ACTUAL RESULT 8: default value was :%s and after revertion %s" %(defaultRadio1,details)
                      print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 7: Revert the WiFi Force Disable status to previous";
                    print "EXPECTED RESULT 7: Should disable WiFi Force Disable status to %s" %default;
                    print "ACTUAL RESULT 7: %s" %details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Enable the WiFi Force Disable";
                 print "EXPECTED RESULT 4: Should enable Force Disable state";
                 print "ACTUAL RESULT 4: %s" %details;
                 print "[TEST EXECUTION RESULT] : FAILURE";
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Get the current WiFi Force Disable state";
              print "EXPECTED RESULT 3: Should get current WiFi Force Disable state";
              print "ACTUAL RESULT 3: current WiFi Force Disable state is %s" %default;
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Get the Radio Enable status for 5GHz";
           print "EXPECTED RESULT 2: Should get the Radio Enable status for 5GHz";
           print "ACTUAL RESULT 2: Radio Enable status for 5GHz state is %s" %defaultRadio2;
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Radio Enable status for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the Radio Enable status for 2.4GHz";
        print "ACTUAL RESULT 1: Radio Enable status for 2.4GHz state is %s" %defaultRadio1;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent")
else:
    print "Failed to load wifiagent module";
    obj.setLoadModuleStatus("FAILURE");
