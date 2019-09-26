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
  <name>TS_LMLite_NWDeviceStatus_Enabled_SetHigherReportingPeriod</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>LMLiteStub_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>The new reporting period cannot be greater than current reporting period if the Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled is true</synopsis>
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
    <test_case_id>TC_LMLite_04</test_case_id>
    <test_objective>The new reporting period cannot be greater than current reporting period</test_objective>
    <test_type>Negative</test_type>
    <test_setup>XB3,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>LMLiteStub_Get,LMLiteStub_Set</api_or_interface_used>
    <input_parameters>Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod
Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled</input_parameters>
    <automation_approch>1. Load Lmlite modules
2. From script invoke LMLiteStub_Get to get the reportingperiod and network device status
3. If the status is true, set the value of the new reporting period greater than current reporting period.
4.If the status is false,set the status as true and then set the value of the new reporting period greater than current reporting period.
5. Set NetworkDevicesStatus to default value.
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
    <test_script>TS_LMLite_NWDeviceStatus_Enabled_SetHigherReportingPeriod</test_script>
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
obj.configureTestCase(ip,port,'TS_LMLite_NWDeviceStatus_Enabled_SetHigherReportingPeriod');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('LMLiteStub_Get');
    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
    expectedresult="SUCCESS";

    ReportingPeriod_list=['5','10','15','30','60','300','900','1800','3600','10800','21600','43200','86400'];
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the ReportingPeriod of NetworkDevicesStatus";
        print "EXPECTED RESULT 1: Should get a valid ReportingPeriod for NetworkDevicesStatus";
        print "ACTUAL RESULT 1: ReportingPeriod of NetworkDevicesStatus :%s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
	Index = ReportingPeriod_list.index(details);

	tdkTestObj = obj.createTestStep('LMLiteStub_Get');
    	tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
    	expectedresult="SUCCESS";

    	tdkTestObj.executeTestCase(expectedresult);
    	actualresult = tdkTestObj.getResult();
        default = tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the NetworkDevicesStatus ";
            print "EXPECTED RESULT 2: Should get NetworkDevicesStatus ";
            print "ACTUAL RESULT 2: NetworkDeviceStatus is :%s" %default;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    if "true" in details:
	        if Index != 0:
                    reportingperiod = ReportingPeriod_list[Index+1];
		    print "reporting period to be set :%s" %reportingperiod;
		    tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            	    tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
            	    tdkTestObj.addParameter("ParamValue",reportingperiod);
                    tdkTestObj.addParameter("Type","unsignedint");
		    expectedresult="FAILURE";

            	    tdkTestObj.executeTestCase(expectedresult);
            	    actualresult = tdkTestObj.getResult();
            	    details = tdkTestObj.getResultDetails();

		    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Set new ReportingPeriod as greater than current ReportingPeriod";
                        print "EXPECTED RESULT 3: Should not  set new ReportingPeriod as greater than current ReportingPeriod for NetworkDevicesStatus";
                        print "ACTUAL RESULT 3: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

		    else:
		        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Set new ReportingPeriod as greater than current ReportingPeriod";
                        print "EXPECTED RESULT 3: Should not  set new ReportingPeriod as greater than current ReportingPeriod for NetworkDevicesStatus";
                        print "ACTUAL RESULT 3: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";


            else:
	        tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            	tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
            	tdkTestObj.addParameter("ParamValue","true");
            	tdkTestObj.addParameter("Type","boolean");
            	expectedresult="SUCCESS";

            	tdkTestObj.executeTestCase(expectedresult);
            	actualresult = tdkTestObj.getResult();
            	details = tdkTestObj.getResultDetails();

	    	if Index != 0:
                    reportingperiod = ReportingPeriod_list[Index+1];
		    print "reporting period to be set :%s" %reportingperiod;
	       	    tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            	    tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.ReportingPeriod");
            	    tdkTestObj.addParameter("ParamValue",reportingperiod);
            	    tdkTestObj.addParameter("Type","unsignedint");
            	    expectedresult="FAILURE";

            	    tdkTestObj.executeTestCase(expectedresult);
            	    actualresult = tdkTestObj.getResult();
            	    details = tdkTestObj.getResultDetails();

            	    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Set new ReportingPeriod as greater than current ReportingPeriod";
                        print "EXPECTED RESULT 3: Should not  set new ReportingPeriod as greater than current ReportingPeriod for NetworkDevicesStatus";
                        print "ACTUAL RESULT 3: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";


                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Set new ReportingPeriod as greater than current ReportingPeriod";
                        print "EXPECTED RESULT 3: Should not  set new ReportingPeriod as greater than current ReportingPeriod for NetworkDevicesStatus";
                        print "ACTUAL RESULT 3: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

            tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.NetworkDevicesStatus.Enabled");
            tdkTestObj.addParameter("ParamValue",default);
            tdkTestObj.addParameter("Type","boolean");
            expectedresult="SUCCESS";

            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Set the NetworkDevicesStatus to default value";
                print "EXPECTED RESULT 4: Should set NetworkDevicesStatus to default value";
                print "ACTUAL RESULT 4: NetworkDeviceStatus is :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Set the NetworkDevicesStatus to default value ";
                print "EXPECTED RESULT 4: Should set NetworkDevicesStatus to default value";
                print "ACTUAL RESULT 4: NetworkDeviceStatus is :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";


        else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the NetworkDevicesStatus ";
            print "EXPECTED RESULT 2: Should get NetworkDevicesStatus ";
            print "ACTUAL RESULT 2: NetworkDeviceStatus is :%s" %default;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the ReportingPeriod of NetworkDevicesStatus";
        print "EXPECTED RESULT 1: Should get a valid ReportingPeriod for NetworkDevicesStatus";
        print "ACTUAL RESULT 1: ReportingPeriod of NetworkDevicesStatus :%s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("lmlite");

else:
        print "Failed to load lmlite module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
