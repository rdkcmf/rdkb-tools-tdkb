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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_PAM_Activate_AdvancedParentalControl</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if Advanced Parental Control is enabled, Advanced Parental Control should be activated and if advanced parental control activate status is 1 via syscfg</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_PAM_162</test_case_id>
    <test_objective>To check if Advanced Parental Control is enabled, Advanced Parental Control should be activated and if advanced parental control activate status is 1 via syscfg</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedParentalControl.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_AdvancedParentalControl.Activate</input_parameters>
    <automation_approch>1.Laod module
2.Enable AdvancedParentalControl
3.Check if AdvancedParentalControl can be activated
4.Get AdvancedParentalControl Activate value via syscfg
5.Check if AdvancedParentalControl Activate value is 1
6.Unload module</automation_approch>
    <expected_output>If Advanced Parental Control is enabled,we can set true to Device.DeviceInfo.X_RDKCENTRAL-COM_AdvancedParentalControl.Activate and AdvancedParentalControl Activate value via syscfg should be 1</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_Activate_AdvancedParentalControl</test_script>
    <skipped>No</skipped>
    <release_version>M71</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_Activate_AdvancedParentalControl');
obj1.configureTestCase(ip,port,'TS_PAM_Activate_AdvancedParentalControl');


#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;


if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedParentalControl.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj.getResult();
    enabledetails = tdkTestObj.getResultDetails();
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_AdvancedParentalControl.Activate");

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult2 = tdkTestObj.getResult();
    activatedetails = tdkTestObj.getResultDetails();

    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult3 = tdkTestObj.getResult();
    rabiddetails = tdkTestObj.getResultDetails();

    if expectedresult in (actualresult1 and actualresult2 and actualresult3):
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 :Get the Advanced ParentalControl Enable status and AdvancedParentalControl Activate status";
        print "ACTUAL RESULT 1:Advanced ParentalControl Enable status:%s  AdvancedParentalControl Activate status :%s RabidFramework Enable status: %s" %(enabledetails,activatedetails,rabiddetails);
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetMultiple');
        tdkTestObj.addParameter("paramList","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedParentalControl.Enable|true|bool|Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable|true|bool");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Enable Advanced ParentalControl";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_AdvancedParentalControl.Activate");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","bool");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if AdvancedParentalControl can be activated if Advanced ParentalControl is enabled";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj = obj1.createTestStep('ExecuteCmd');
                cmd = "syscfg show | grep Adv_PCActivate | cut -d = -f 2";
                tdkTestObj.addParameter("command",cmd);

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and details == "1":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4:Check if AdvancedParental Control Activate is 1";
                    print "ACTUAL RESULT 4:AdvancedParental Control Activate is 1";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4:Check if AdvancedParental Control Activate is 1";
                    print "ACTUAL RESULT 4:AdvancedParental Control Activate is not 1";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Check if AdvancedParentalControl can be activated if Advanced ParentalControl is enabled";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedParentalControl.Enable|%s|bool|Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RabidFramework.Enable|%s|bool" %(enabledetails,rabiddetails));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP:Revert the values"
                print "ACTUAL RESULT : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_AdvancedParentalControl.Activate");
                tdkTestObj.addParameter("ParamValue",activatedetails);
                tdkTestObj.addParameter("Type","bool");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP :Activate the AdvancedParentalControl Activate status";
                    print "ACTUAL RESULT : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP :Activate the AdvancedParentalControl Activate status";
                    print "ACTUAL RESULT : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP:Revert the values"
                print "ACTUAL RESULT : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Enable Advanced ParentalControl";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 :Get the Advanced ParentalControl Enable status and AdvancedParentalControl Activate status";
        print "ACTUAL RESULT 1:Failed to get Advanced ParentalControl Enable status and AdvancedParentalControl Activate status ";
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");

else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
