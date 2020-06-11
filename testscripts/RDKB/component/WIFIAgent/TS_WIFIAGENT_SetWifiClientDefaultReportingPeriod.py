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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_SetWifiClientDefaultReportingPeriod</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the Wifi Client Default Reporting Period with all the supported values</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <test_case_id>TC_WIFIAGENT_102</test_case_id>
    <test_objective>This test case is to check if  Wifi Client Default Reporting Period  can be set with  all  its  supported periods</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get
TDKB_TR181Stub_Set</api_or_interface_used>
    <input_parameters>ParamName -Device.WiFi.X_RDKCENTRALCOM_Report.WifiClient.Default.ReportingPeriod
ParamValues - 1,5,15,30,60,300,900,1800,3600,10800,21600,43200,86400
</input_parameters>
    <automation_approch>1.Load tdkbtr181 module.
2.Do a get on Device.WiFi.X_RDKCENTRALCOM_Report.WifiClient.Default.ReportingPeriod  and store the initial value.
3.loop through the list of supported values and set one after the other.
4.TM will print the result as Success if all the values were set successfully else failure.
5.Now revert back to the initial value.
6.Unload the module</automation_approch>
    <expected_output>All the supported values to Device.WiFi.X_RDKCENTRALCOM_Report.WifiClient.Default.ReportingPeriod  should be set successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>TDKB-TR181</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetWifiClientDefaultReportingPeriod</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetWifiClientDefaultReportingPeriod');

loadmodulestatus = obj.getLoadModuleResult();
flag = 0;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.Default.ReportingPeriod");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the WifiClient Default ReportingPeriod";
        print "EXPECTED RESULT 1: Should get WifiClient Default ReportingPeriod";
        print "ACTUAL RESULT 1: WifiClient Default ReportingPeriod:%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        ReportingPeriod_list=[1,5,15,30,60,300,900,1800,3600,10800,21600,43200,86400];
        # getting length of list
        length = len(ReportingPeriod_list)
        print "Supported Values for  Wifi Client Default ReportingPeriod is ",ReportingPeriod_list

        for i in range(length):
            print "Setting the Wifi Client Default ReportingPeriod to ",ReportingPeriod_list[i]

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.Default.ReportingPeriod");
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("ParamValue",str(ReportingPeriod_list[i]));
            tdkTestObj.addParameter("Type","unsignedint");

            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Setresult = tdkTestObj.getResultDetails();

            SetValue =ReportingPeriod_list[i];
            if expectedresult in actualresult:
               flag =0;
               print " Value set successfully to ",ReportingPeriod_list[i];

            else:
                flag =1;
                break;

        if flag == 0:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Set the WifiClient Default ReportingPeriod  to all supported Values";
           print "EXPECTED RESULT 2: Should set WifiClient Default ReportingPeriod to all supported Values";
           print "ACTUAL RESULT 2: Successfully set the WifiClient Default ReportingPeriod" ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Set the WifiClient Default ReportingPeriod to all supported Values";
           print "EXPECTED RESULT 2: Should set WifiClient Default ReportingPeriod to all supported Values";
           print "ACTUAL RESULT 2: Failed to set the ",SetValue,"WifiClient Default ReportingPeriod " ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] :FAILURE";

        #Reverting to default
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.Default.ReportingPeriod");
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("ParamValue",default);
        tdkTestObj.addParameter("Type","unsignedint");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        result = tdkTestObj.getResultDetails();

        if expectedresult in  expectedresult:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 3: Revert the ReportingPeriod Default  WifiClient to its default";
           print "EXPECTED RESULT 3: Revert  ReportingPeriod Default WifiClient to previous value";
           print "ACTUAL RESULT 3: Revert Operation sucesss:",result ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 3: Revert the ReportingPeriod Default WifiClient to its default";
           print "EXPECTED RESULT 3: Revert  ReportingPeriod Default WifiClient to previous value";
           print "ACTUAL RESULT 3: Revert Operation failed:",result ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the WifiClient Default ReportingPeriod";
        print "EXPECTED RESULT 1: Should get WifiClient Default ReportingPeriod";
        print "ACTUAL RESULT 1: WifiClient Default ReportingPeriod  :%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
