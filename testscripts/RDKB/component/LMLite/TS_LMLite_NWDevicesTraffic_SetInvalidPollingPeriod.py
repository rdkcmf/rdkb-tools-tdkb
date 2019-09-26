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
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_LMLite_NWDevicesTraffic_SetInvalidPollingPeriod</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>LMLiteStub_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check whether the NetworkDevicesTraffic.PollingPeriod is a valid value. ie,[30,60,300,900,1800,3600,10800,21600,43200,86400]. Then try to set an invalid value to it</synopsis>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_LMLite_18</test_case_id>
    <test_objective>To check whether the NetworkDevicesTraffic.PollingPeriod is a valid value. ie,[30,60,300,900,1800,3600,10800,21600,43200,86400]. Then try to set an invalid value to it</test_objective>
    <test_type>Negative</test_type>
    <test_setup>XB3,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>LMLiteStub_Get,LMLiteStub_Set</api_or_interface_used>
    <input_parameters>Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod</input_parameters>
    <automation_approch>1. Load Lmlite modules
2. From script invoke LMLiteStub_Get to get the polling period
3. Set an invalid value for the polling period
4. Set polling period to default value.
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from lmlite stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_LMLite_NWDevicesTraffic_SetInvalidPollingPeriod</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_NWDevicesTraffic_SetInvalidPollingPeriod');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('LMLiteStub_Get');
    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod");
    expectedresult="SUCCESS";

    PollingPeriod_list={'30','60','300','900','1800','3600','10800','21600','43200','86400'};
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details_polling = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details_polling in PollingPeriod_list:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the PollingPeriod of NetworkDevicesTraffic";
        print "EXPECTED RESULT 1: Should get a valid PollingPeriod for NetworkDevicesTraffic";
        print "ACTUAL RESULT 1: PollingPeriod of NetworkDevicesTraffic :%s" %details_polling;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
	tdkTestObj = obj.createTestStep('LMLiteStub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod");
        tdkTestObj.addParameter("ParamValue","100");
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set an invalid PollingPeriod of NetworkDevicesTraffic";
            print "EXPECTED RESULT 2: Should not set an invalid PollingPeriod for NetworkDevicesTraffic";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set an invalid PollingPeriod of NetworkDevicesTraffic";
            print "EXPECTED RESULT 2: Should not set an invalid PollingPeriod for NetworkDevicesTraffic";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesTraffic.PollingPeriod");
        tdkTestObj.addParameter("ParamValue",details_polling);
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Set the PollingPeriod of NetworkDevicesTraffic to default value";
            print "EXPECTED RESULT 3: Should set a valid PollingPeriod for NetworkDevicesTraffic to default value";
            print "ACTUAL RESULT 3: PollingPeriod of NetworkDevicesTraffic :%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Set the PollingPeriod of NetworkDevicesTraffic to default value";
            print "EXPECTED RESULT 3: Should set a valid PollingPeriod for NetworkDevicesTraffic to default value";
            print "ACTUAL RESULT 3: PollingPeriod of NetworkDevicesTraffic :%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
	print "TEST STEP 1: Get the PollingPeriod of NetworkDevicesTraffic";
        print "EXPECTED RESULT 1: Should get a valid PollingPeriod for NetworkDevicesTraffic";
        print "ACTUAL RESULT 1: PollingPeriod of NetworkDevicesTraffic :%s" %details_polling;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("lmlite");
else:
        print "Failed to load lmlite module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
