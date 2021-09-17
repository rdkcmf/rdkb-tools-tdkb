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
  <version>3</version>
  <name>TS_WIFIAGENT_2.4GHzSetManagementFramePowerControl</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the Management Frame Power Control to all possible values for 2.4GHz WiFi.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIAGENT_152</test_case_id>
    <test_objective>To set the Management Frame Power Control to all possible values for 2.4GHz WiFi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.1.X_RDKCENTRAL-COM_ManagementFramePowerControl</input_parameters>
    <automation_approch>1.Load the module
2.Get the current value of Managment Frame power control
3.Set all the possible values between 0 to -20 db
4.Revert the set value
5. unload the module
</automation_approch>
    <expected_output>All the supported values should be set successfully</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHzSetManagementFramePowerControl</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# tdklib library,which provides a iwrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHzSetManagementFramePowerControl');

loadmodulestatus = obj.getLoadModuleResult();
flag = 0;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.1.X_RDKCENTRAL-COM_ManagementFramePowerControl");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the ManagementFrame PowerControl value";
        print "EXPECTED RESULT 1: Should get  ManagementFrame PowerControl value";
        print "ACTUAL RESULT 1: ManagementFrame PowerControl :%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        framePower_list=[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20];
        # getting length of list
        length = len(framePower_list)
        print "Supported Values for  ManagementFrame PowerControl is ",framePower_list

        for i in range(length):
            print "Setting the ManagementFrame PowerControl to ",framePower_list[i]

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.1.X_RDKCENTRAL-COM_ManagementFramePowerControl");
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("ParamValue",str(framePower_list[i]));
            tdkTestObj.addParameter("Type","int");

            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Setresult = tdkTestObj.getResultDetails();

            SetValue =framePower_list[i];
            if expectedresult in actualresult:
               flag =0;
               print " Value set successfully to ",framePower_list[i];

            else:
                flag =1;
                break;

        if flag == 0:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Set the ManagementFrame PowerControl to all supported Values";
           print "EXPECTED RESULT 2: Should set  ManagementFrame PowerControl value to all supported Values";
           print "ACTUAL RESULT 2: Successfully set the all the supported  ManagementFrame PowerControl value" ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Set the ManagementFrame PowerControl to all supported Values";
           print "EXPECTED RESULT 2: Should set  ManagementFrame PowerControl value to all supported Values";
           print "ACTUAL RESULT 2: Failed to set the ",SetValue,"  ManagementFrame PowerControl value" ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] :FAILURE";

        #Reverting to default
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.1.X_RDKCENTRAL-COM_ManagementFramePowerControl");
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("ParamValue",default);
        tdkTestObj.addParameter("Type","int");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        result = tdkTestObj.getResultDetails();

        if expectedresult in  expectedresult:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 3: Revert the ManagementFrame PowerControl to its default";
           print "EXPECTED RESULT 3: Revert   ManagementFrame PowerControl value to previous value";
           print "ACTUAL RESULT 3: Revert Operation sucesss:",result ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 3: Revert the ManagementFrame PowerControl to its default";
           print "EXPECTED RESULT 3: Revert   ManagementFrame PowerControl value to previous value";
           print "ACTUAL RESULT 3: Revert Operation failed:",result ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the ManagementFrame PowerControl value";
        print "EXPECTED RESULT 1: Should get  ManagementFrame PowerControl value";
        print "ACTUAL RESULT 1: ManagementFrame PowerControl :%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
