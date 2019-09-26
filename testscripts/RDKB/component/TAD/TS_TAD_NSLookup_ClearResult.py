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
  <name>TS_TAD_NSLookup_ClearResult</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check whether after a successful NSLookup,setting any writable parameter clears the result parameter</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_TAD_36</test_case_id>
    <test_objective>To check whether after a successful NSLookup,setting any writable parameter clears the result parameter</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Set,TADstub_Get,TADstub_SetDiagnosticsState,pam_GetParameterNames</api_or_interface_used>
    <input_parameters>Device.DNS.Diagnostics.NSLookupDiagnostics.Interface
Device.DNS.Diagnostics.NSLookupDiagnostics.HostName
Device.DNS.Diagnostics.NSLookupDiagnostics.DiagnosticsState</input_parameters>
    <automation_approch>1. Load  TAD modules
2.From script invoke pam_GetParameterNames to obtain the namespace to be set as the interface
3. From script invoke TADstub_Set to set  the interface and hostname of NSLookup and invoke TADstub_SetDiagnosticsState to set the diagnostics state 
4. If set returns success, check the ResultNumberOfEntries and Success Count
5. Check whether the ResultNumberOfEntries and Success Count are greater than zero
6.Again set any writable parameter of NSLook up and check if the  ResultNumberOfEntries is zero
7. Validation of  the result is done within the python script and send the result status to Test Manager.
8.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_TAD_NSLookup_ClearResult</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
import tdkutility;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_NSLookup_ClearResult');
pamObj.configureTestCase(ip,port,'TS_TAD_NSLookup_ClearResult');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =pamObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper()and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    host = tdkutility.readtdkbConfigFile(obj);
    tdkTestObj = obj.createTestStep('TADstub_Get');
    tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.TraceRoute.Host");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    if host == "NULL":
        tdkTestObj.setResultStatus("FAILURE");
        print "Host name not available in tdkb config file"
    else:
        tdkTestObj = pamObj.createTestStep('pam_GetParameterNames');
        tdkTestObj.addParameter("ParamName","Device.IP.Interface.");
        tdkTestObj.addParameter("ParamList","Device.IP.Interface.");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        interface = tdkTestObj.getResultDetails().strip();

        tdkTestObj = pamObj.createTestStep('pam_GetParameterNames');
        tdkTestObj.addParameter("ParamName","%sIPv4Address." %interface);
        tdkTestObj.addParameter("ParamList","%sIPv4Address." %interface);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        addrInstance = tdkTestObj.getResultDetails().strip();
        namespace=addrInstance+"IPAddress";
        print "%s" %namespace;
        tdkTestObj = obj.createTestStep('TADstub_Set');
        tdkTestObj.addParameter("ParamName","Device.DNS.Diagnostics.NSLookupDiagnostics.Interface");
        tdkTestObj.addParameter("ParamValue",namespace);
        tdkTestObj.addParameter("Type","string");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Set the interface of NSLookup";
            print "EXPECTED RESULT 1: Should set the interface of NSLookup";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep('TADstub_Set');
            tdkTestObj.addParameter("ParamName","Device.DNS.Diagnostics.NSLookupDiagnostics.HostName");
            tdkTestObj.addParameter("ParamValue",host);
            tdkTestObj.addParameter("Type","string");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set the host of NSLookup";
                print "EXPECTED RESULT 2: Should set the host of NSLookup";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep('TADstub_SetDiagnosticsState');
                tdkTestObj.addParameter("ParamName","Device.DNS.Diagnostics.NSLookupDiagnostics.DiagnosticsState");
                tdkTestObj.addParameter("ParamValue","Requested");
                tdkTestObj.addParameter("Type","string");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Set DiagnosticsState of NSLookup as Requested";
                    print "EXPECTED RESULT 3: Should set DiagnosticsState of NSLookup as Requested";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    time.sleep(50);
                    tdkTestObj = obj.createTestStep('TADstub_Get');
                    tdkTestObj.addParameter("paramName","Device.DNS.Diagnostics.NSLookupDiagnostics.ResultNumberOfEntries");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details_ResultNumberOfEntries = tdkTestObj.getResultDetails();
                    tdkTestObj = obj.createTestStep('TADstub_Get');
                    tdkTestObj.addParameter("paramName","Device.DNS.Diagnostics.NSLookupDiagnostics.SuccessCount");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details_SuccessCount = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult and int(details_ResultNumberOfEntries)>0 and int(details_SuccessCount)>0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Check if ResultNumberOfEntries and SuccessCount are greater than zero";
                        print "EXPECTED RESULT 4: Should get ResultNumberOfEntries and SuccessCount are greater than zero";
                        print "ACTUAL RESULT 4: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj = obj.createTestStep('TADstub_Set');
        		tdkTestObj.addParameter("ParamName","Device.DNS.Diagnostics.NSLookupDiagnostics.Interface");
        		tdkTestObj.addParameter("ParamValue",namespace);
         		tdkTestObj.addParameter("Type","string");
        		expectedresult="SUCCESS";
        		tdkTestObj.executeTestCase(expectedresult);
         		actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
            		    #Set the result status of execution
            		    tdkTestObj.setResultStatus("SUCCESS");
            		    print "TEST STEP 5: Set the interface of NSLookup";
            		    print "EXPECTED RESULT 5: Should set the interface of NSLookup";
            		    print "ACTUAL RESULT 5: %s" %details;
            		    #Get the result of execution
            		    print "[TEST EXECUTION RESULT] : SUCCESS";

            		    tdkTestObj = obj.createTestStep('TADstub_Get');
                    	    tdkTestObj.addParameter("paramName","Device.DNS.Diagnostics.NSLookupDiagnostics.ResultNumberOfEntries");
                    	    expectedresult="SUCCESS";
                    	    tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                    	    details = tdkTestObj.getResultDetails();
            		    if expectedresult in actualresult and int(details)==0:
                                #Set the result status of execution
                        	tdkTestObj.setResultStatus("SUCCESS");
                        	print "TEST STEP 6: Check if ResultNumberOfEntries of NSLookup is zero";
                        	print "EXPECTED RESULT 6: Should get ResultNumberOfEntries of NSLookup as zero";
                        	print "ACTUAL RESULT 6: %s" %details;
                        	#Get the result of execution
                       	        print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
            		        #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 6: Check if ResultNumberOfEntries of NSLookup is zero";
                                print "EXPECTED RESULT 6: Should get ResultNumberOfEntries of NSLookup as zero";
                                print "ACTUAL RESULT 6: %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                                

                        else:
            	            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Set the interface of NSLookup";
                            print "EXPECTED RESULT 5: Should set the interface of NSLookup";
                            print "ACTUAL RESULT 5: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";


                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Check if ResultNumberOfEntries and SuccessCount are greater than zero";
                        print "EXPECTED RESULT 4: Should get ResultNumberOfEntries and SuccessCount are greater than zero";
                        print "ACTUAL RESULT 4: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Set DiagnosticsState of NSLookup as Requested";
                    print "EXPECTED RESULT 3: Should set DiagnosticsState of NSLookup as Requested";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set the host of NSLookup";
                print "EXPECTED RESULT 2: Should set the host of NSLookup";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Set the interface of NSLookup";
            print "EXPECTED RESULT 1: Should set the interface of NSLookup";
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");
    pamObj.unloadModule("pam");
else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
