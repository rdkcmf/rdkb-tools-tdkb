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
  <version>12</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_CMHAL_HTTP_Download_InvalidFWName</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_GetParamUlongValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if firmware download triggered with cm_hal_HTTP_Download() fails  when invalid firmware name is set via cm_hal_Set_HTTP_Download_Url() api</synopsis>
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
    <test_case_id>TC_CMHAL_106</test_case_id>
    <test_objective>Check if firmware download triggered with cm_hal_HTTP_Download() fails  when invalid firmware name is set via cm_hal_Set_HTTP_Download_Url() api</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_HTTP_Download
cm_hal_Get_HTTP_Download_Status
cm_hal_Set_HTTP_Download_Url
cm_hal_Get_HTTP_Download_Url
cm_hal_Set_HTTP_Download_Interface
cm_hal_Get_HTTP_Download_Interface</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load  cmhal module
2. Get and save current download interface using cm_hal_Get_HTTP_Download_Interface()
3. Set the interface as 0 using cm_hal_Set_HTTP_Download_Interface()
4. Verify interface set using cm_hal_Get_HTTP_Download_Interface()
5. Set proper download url and an invalid firmware name using cm_hal_Set_HTTP_Download_Url()
6. Verify set in step 5 using cm_hal_Get_HTTP_Download_Url
7. Start the download with cm_hal_HTTP_Download()
8. Invoke cm_hal_Get_HTTP_Download_Status() and check if it returns download status as failure
9. Revert back download interface value
10. Unload  cmhal module</automation_approch>
    <expected_output>Download triggered with cm_hal_HTTP_Download() fails  when invalid firmware name is set via cm_hal_Set_HTTP_Download_Url() api</expected_output>
    <priority>High</priority>
    <test_stub_interface>cmhal</test_stub_interface>
    <test_script>TS_CMHAL_HTTP_Download_InvalidFWName</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from xconfVariables import *;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_HTTP_Download_InvalidFWName');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
        obj.setLoadModuleStatus("SUCCESS");

	tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
        tdkTestObj.addParameter("paramName","DownloadInterface");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        downInterface = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the Download interface";
            print "EXPECTED RESULT 1: Should get the Download interface sucessfully";
            print "ACTUAL RESULT 1: Download interface is %s" %downInterface;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            setInterface = 0
            if int(downInterface) != setInterface :
                tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Interface");
                tdkTestObj.addParameter("interface",setInterface);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Set the download interface";
                    print "EXPECTED RESULT 2: Should set the download interface";
                    print "ACTUAL RESULT 2:  ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
                    tdkTestObj.addParameter("paramName","DownloadInterface");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult and int(details) == setInterface:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Get the Download interface";
                        print "EXPECTED RESULT 3: Should get the Download interface sucessfully";
                        print "ACTUAL RESULT 3: Download interface is %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
            	    else:
            	        tdkTestObj.setResultStatus("FAILURE");
            	        print "TEST STEP 3: Get the Download interface to verify the set operation";
            	        print "EXPECTED RESULT 3: Should get the Download interface sucessfully";
            	        print "ACTUAL RESULT 3: Download interface is %s" %details;
            	        #Get the result of execution
            	        print "[TEST EXECUTION RESULT] : FAILURE";
                        obj.unloadModule("cmhal");
                        exit()
        	else:
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("FAILURE");
        	    print "TEST STEP 2: Set the download interface as ",setInterface;
        	    print "EXPECTED RESULT 2: Should set the download interface as ",setInterface;
        	    print "ACTUAL RESULT 2:  ",details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : FAILURE";
                    obj.unloadModule("cmhal");
                    exit()

            FirmwareFilename = "DUMMY_FW_NAME"
            #since CMHAL_GetHTTP_Download_Url() doesn't have an initial value, not saving it for revert
            tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Url");
            tdkTestObj.addParameter("httpURL",FIRMWARELOCATION);
            tdkTestObj.addParameter("filename",FirmwareFilename);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Set the Download url and and an invalid FW filename";
                print "EXPECTED RESULT 4: Should set the Download url and an invalid FW filename";
                print "ACTUAL RESULT 4: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep("CMHAL_GetHTTP_Download_Url");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                expectedOutput = "url is " + FIRMWARELOCATION + ", filename is " + FirmwareFilename

                if expectedresult in actualresult and details == expectedOutput:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Get the download url and filename";
                    print "EXPECTED RESULT 5: Should get the download url and filename";
                    print "ACTUAL RESULT 5: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj.createTestStep("CMHAL_HTTP_Download");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 6: Start the download using cm_hal_HTTP_Download() with invalid FW name";
                        print "EXPECTED RESULT 6: Should successfully invoke cm_hal_HTTP_Download()";
                        print "ACTUAL RESULT 6: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

	                #wait till download is complete
                        print "Waiting for download......";
	                time.sleep(60);

                        print "TEST STEP 7: Get the Download status using cm_hal_Get_HTTP_Download_Status()";
                        print "EXPECTED RESULT 7: Should get the Download status";
                        #Script to load the configuration file of the component
                        tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
                        tdkTestObj.addParameter("paramName","HTTP_Download_Status");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = int(tdkTestObj.getResultDetails());
                        if expectedresult in actualresult :
                            details = int(details)
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 7: cm_hal_Get_HTTP_Download_Status returned download status as ", details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] 7: SUCCESS";

                            success_status = "";
                            fail_status = "";
                            if 0<details<=100:
                                success_status = str(details),"% download completed";
                            elif details == 200:
                                success_status = "Download is completed and waiting for reboot";
                            elif details ==0 or details >100:
                                status_list = {0:"Download is not started",400:"Invalided Http server Url",401:"Cannot connect to Http server",402:"File is not found on Http server",403:"HW_Type_DL_Protection Failure",404:"HW Mask DL Protection Failure",405:"DL Rev Protection Failure",406:"DL Header Protection Failure",407:"DL CVC Failure",500:"General Download Failure"};
                                fail_status = status_list[details];
                            else:
                                status = "Invalid status", details

                            if fail_status:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 8: Check if cm_hal_Get_HTTP_Download_Status returned a failure status";
                                print "EXPECTED RESULT 8: Should get a Download failed status";
                                print "ACTUAL RESULT 8: Got the failure status: %s" %fail_status;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                	    else:
                	        #Set the result status of execution
                	        tdkTestObj.setResultStatus("FAILURE");
                	        print "TEST STEP 8: Check if cm_hal_Get_HTTP_Download_Status returned a failure status";
                	        print "EXPECTED RESULT 8: Should get a Download failed status";
                	        print "ACTUAL RESULT 8: ", details;
                	        #Get the result of execution
                	        print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 7: Failed to get download status using cm_hal_Get_HTTP_Download_Status";
                            print "Details: ", details
                            print "[TEST EXECUTION RESULT] 7: FAILURE";
                    else:
                	    #Set the result status of execution
                	    tdkTestObj.setResultStatus("FAILURE");
                	    print "TEST STEP 6: Start the download";
                	    print "EXPECTED RESULT 6: Should start the download successfully";
                	    print "ACTUAL RESULT 6: %s" %details;
                	    #Get the result of execution
                	    print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Get the download url and filename";
                    print "EXPECTED RESULT 5: Should get the download url and filename";
                    print "ACTUAL RESULT 5: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Set the Download url and and an invalid FW filename";
                print "EXPECTED RESULT 4: Should set the Download url and and an invalid FW filename";
                print "ACTUAL RESULT 4: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert the download interface
            if int(downInterface) != setInterface :
                tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Interface");
                tdkTestObj.addParameter("interface",int(downInterface));
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 9: Revert the download interface";
                    print "EXPECTED RESULT 9: Should revert the download interface";
                    print "ACTUAL RESULT 9:  ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 9: Revert the download interface";
                    print "EXPECTED RESULT 9: Should revert the download interface";
                    print "ACTUAL RESULT 9:  ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the Download interface";
            print "EXPECTED RESULT 1: Should get the Download interface sucessfully";
            print "ACTUAL RESULT 1: Download interface is %s" %downInterface;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
