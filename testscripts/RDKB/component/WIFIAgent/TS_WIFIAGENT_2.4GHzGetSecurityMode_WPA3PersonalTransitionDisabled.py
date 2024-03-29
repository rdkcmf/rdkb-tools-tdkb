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
  <name>TS_WIFIAGENT_2.4GHzGetSecurityMode_WPA3PersonalTransitionDisabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check security mode of 2.4Ghz Access point with WPA3 Personal Transition Disabled</synopsis>
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
    <test_case_id>TC_WIFIAGENT_134</test_case_id>
    <test_objective>This test case is to check security mode of 2.4Ghz Access point with WPA3 Personal Transition Disabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Set
WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable
Device.WiFi.AccessPoint.1.Security.ModeEnabled</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of WPA3 Personal Transition  enable parameter
3.Disable the WPA3 Personal Transition  status
4.Check the security mode enabled for Access point 2.4GHz and is expected to be WPA2-Personal
5.Revert the set value
5.Unload the module</automation_approch>
    <expected_output>with   WPA3 Personal Transition disabled  security mode  for Access point 2.4GHz  is expected to be WPA2-Personal </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHzGetSecurityMode_WPA3PersonalTransitionDisabled</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
#import statement
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHzGetSecurityMode_WPA3PersonalTransitionDisabled');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the load module status
    obj.setLoadModuleStatus("SUCCESS");

    revertflag =0;
    #Get the encryption method after set
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    value = tdkTestObj.getResultDetails();
    defvalue = value.split("VALUE:")[1].split(' ')[0]
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 :Get  the WPA3 Transition Enable statuts";
        print "EXPECTED RESULT 1: Should get the WPA3 Transition Enable statuts";
        print "ACTUAL RESULT 1: Status %s" %defvalue;
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if defvalue =="true":
           tdkTestObj = obj.createTestStep('WIFIAgent_Set');
           tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable");
           tdkTestObj.addParameter("paramValue","false");
           tdkTestObj.addParameter("paramType","bool");
           expectedresult="SUCCESS";

           #Execute the test case in DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails();
           if expectedresult in actualresult:
              revertflag =1;
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 2 : Disable the  WPA3 Transition Enable";
              print "EXPECTED RESULT 2: Should disable  WPA3 Transition Enable";
              print "ACTUAL RESULT 2: Status %s" %details;
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2 : Disable the  WPA3 Transition Enable";
               print "EXPECTED RESULT 2: Should disable  WPA3 Transition Enable";
               print "ACTUAL RESULT 2: Status %s" %details;
               print "[TEST EXECUTION RESULT] : FAILURE";
        if expectedresult in actualresult:
            #Get the encryption method after set
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            value = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and  value!= "":
                value = value.split("VALUE:")[1].split(' ')[0];
                if "WPA2-Personal" in value:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get the security mode of 2.4GHZ WIFI with WPA3 Transition disabled";
                    print "EXPECTED RESULT 3 Should get the security mode of 2.4GHZ WIFI as WPA2-Personal"
                    print "ACTUAL RESULT 3: Security Mode is %s" %value;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get the security mode of 2.4GHZ WIFI with WPA3 Transition disabled";
                    print "EXPECTED RESULT 3 Should get the security mode of 2.4GHZ WIFI as WPA2-Personal";
                    print "ACTUAL RESULT 3: Security Mode is %s" %value;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the security mode of 2.4GHZ WIFI with WPA3 Transition disabled";
                print "EXPECTED RESULT 3 Should get the security mode of 2.4GHZ WIFI as WPA2-Personal";
                print "ACTUAL RESULT 3: Security Mode is %s" %value;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
             print "WPA3 transition Disable operation failed";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 :Get  the WPA3 Transition Enable statuts";
        print "EXPECTED RESULT 1: Should get the WPA3 Transition Enable statuts";
        print "ACTUAL RESULT 1: Status %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    #Revert operations
    if revertflag ==1:
        tdkTestObj = obj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WPA3_Personal_Transition.Enable");
        tdkTestObj.addParameter("paramValue",defvalue);
        tdkTestObj.addParameter("paramType","bool");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 4:Revert  the  WPA3 Transition Enable";
            print "EXPECTED RESULT 4: Should revert  WPA3 Transition Enable";
            print "ACTUAL RESULT 4: Status %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Revert the  WPA3 Transition Enable";
            print "EXPECTED RESULT 4: Should revert  WPA3 Transition Enable";
            print "ACTUAL RESULT 4: Status %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
else:
    print "Failed to load wifi agent module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
