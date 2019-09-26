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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TAD_Download_SetHTTPSURL</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if setting download URL as https URL,the test fails .http and ftp are the only allowed values</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks>RDKB doesn't support Download Diagnostics feature till now</remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TAD_33</test_case_id>
    <test_objective>To check if setting download URL as https URL,the test fails .http and ftp are the only allowed values</test_objective>
    <test_type>Negative</test_type>
    <test_setup>XB3,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get</api_or_interface_used>
    <input_parameters>Device.IP.Diagnostics.DownloadDiagnostics.DiagnosticsState
Device.IP.Diagnostics.DownloadDiagnostics.Interface
Device.IP.Diagnostics.DownloadDiagnostics.DownloadURL</input_parameters>
    <automation_approch>1. Load TAD modules
2. From script invoke TADstub_Set to set all the writable parameters and set the download URL as https URL.
3. Check whether the download test is failing 
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_TAD_Download_HTTPSURL</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_Download_SetHTTPSURL');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TADstub_Set');
    tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.DownloadDiagnostics.Interface");
    tdkTestObj.addParameter("ParamValue","Interface_erouter0");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Set the interface of Download ";
        print "EXPECTED RESULT 1: Should set the interface of Download";
        print "ACTUAL RESULT 1: Interface of Download is %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('TADstub_Set');
        tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.DownloadDiagnostics.DownloadURL");
        tdkTestObj.addParameter("ParamValue","https://www.kernel.org/pub/linux/docs/man-pages/man-pages-posix/");
        tdkTestObj.addParameter("Type","string");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the download URL of Download";
            print "EXPECTED RESULT 2: Should set the download URL of Download ";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep('TADstub_Set');
            tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.DownloadDiagnostics.DiagnosticsState");
	    tdkTestObj.addParameter("ParamValue","Requested");
            tdkTestObj.addParameter("Type","string");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Set DiagnosticsState of Download as Requested";
                print "EXPECTED RESULT 3: Should set DiagnosticsState of Download as Requested";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                time.sleep(50);
                tdkTestObj = obj.createTestStep('TADstub_Get');
                tdkTestObj.addParameter("paramName"," Device.IP.Diagnostics.DownloadDiagnostics.TotalBytesReceived");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details_TotalBytesReceived= tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details_TotalBytesReceived>0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4 :Get TotalBytesReceived of download greater than zero";
                    print "EXPECTED RESULT 4 :Should get the TotalBytesReceived of download as greater than zero ";
                    print "ACTUAL RESULT 4 :The TotalBytesReceived of download is , details : %s" %details_TotalBytesReceived;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
		    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4 :Get TotalBytesReceived of download as greater than zero";
                    print "EXPECTED RESULT 4 :Should get the TotalBytesReceived of download as greater than zero";
                    print "ACTUAL RESULT 4 :The TotalBytesReceived of download is , details : %s" %details_TotalBytesReceived;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Set DiagnosticsState of Download as Requested";
                print "EXPECTED RESULT 3: Should set DiagnosticsState of Download as Requested";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the download URL of Download";
            print "EXPECTED RESULT 2: Should set the download URL of Download ";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	 #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Set the interface of Download ";
        print "EXPECTED RESULT 1: Should set the interface of Download";
        print "ACTUAL RESULT 1: Interface of Download is %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
	
    obj.unloadModule("tad");

else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
