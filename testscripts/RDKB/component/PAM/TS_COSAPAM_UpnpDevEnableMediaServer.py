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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_COSAPAM_UpnpDevEnableMediaServer</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>This test case is to enable UpnpDev Media Server</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>RPI</box_type>
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>Emulator</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_COSAPAM_16</test_case_id>
    <test_objective>To Validate PAM API CosaDmlUpnpDevEnableMediaServer</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CosaDmlUpnpDevEnableMediaServer</api_or_interface_used>
    <input_parameters>Input:

1.Value -valid</input_parameters>
    <automation_approch>1.Function which needs to be tested will be configured in Test Manager GUI.
2.Python Script will be generated by Test Manager with arguments provided in configure page.
3.Test manager will load the COSAPAM library via Test agent
4.From python script, invoke COSAPAM_UpnpEnable() stub function to set UPNP MediaServer enable
5.COSAPAM stub function will call the ssp_CosaDmlUpnpEnable function in TDK component which in turn will call cosa api CosaDmlUpnpDevEnableMediaServer() of the PAM Agent in RDKB stack.
6.Responses from Cosa API, TDK Component and COSAPAM stub function will be logged in Agent Console log.
7.COSAPAM stub will validate the actual result with the expected result and send the result status to Test Manager.
8.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from COSAPAM stub.</automation_approch>
    <except_output>CheckPoint 1:
Values associated with the parameter specified should be logged in the Agent console/Component log and Should set UPNP MediaServer enable successfully


CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log</except_output>
    <priority>High</priority>
    <test_stub_interface>COSAPAM_UpnpEnable</test_stub_interface>
    <test_script>TS_COSAPAM_UpnpDevEnableMediaServer</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
												#import statement
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_COSAPAM_UpnpDevEnableMediaServer');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('COSAPAM_UpnpGetState');
    tdkTestObj.addParameter("MethodName","UpnpMediaServer");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if "enable" in details:
        org_value=1;
    else:
        org_value=0;
    #setting the enable value
    tdkTestObj = obj.createTestStep('COSAPAM_UpnpEnable');
    tdkTestObj.addParameter("MethodName","UpnpDevMediaServer");
    tdkTestObj.addParameter("Value",1);
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if "enable" in details:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
	details = tdkTestObj.getResultDetails();
	print "TEST STEP 1: Should set the UpnpDev MediaServer enable";
        print "EXPECTED RESULT 1: Should set the UpnpDev MediaServer enable successfully";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
	print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        details = tdkTestObj.getResultDetails();
        print "TEST STEP 1: Should set the UpnpDev MediaServer enable";
        print "EXPECTED RESULT 1: Should set the UpnpDev MediaServer enable successfully";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    #setting the default value
    tdkTestObj = obj.createTestStep('COSAPAM_UpnpEnable');
    tdkTestObj.addParameter("MethodName","UpnpDevMediaServer");
    tdkTestObj.addParameter("Value",org_value);
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if org_value==1 and "enable" in details:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Should set the Upnp Mediaserver enable";
        print "EXPECTED RESULT 1: Should set the Upnp Mediaserver enable successfully";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    elif org_value==0 and "disable" in details:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Should set the Upnp Mediaserver disable";
        print "EXPECTED RESULT 1: Should set the Upnp Mediaserver disable successfully";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Should set the Upnp Mediaserver to default value";
        print "EXPECTED RESULT 1: Should set the Upnp Mediaserver to default value successfully";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    obj.unloadModule("pam");

else:
        print "Failed to load pam module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";








