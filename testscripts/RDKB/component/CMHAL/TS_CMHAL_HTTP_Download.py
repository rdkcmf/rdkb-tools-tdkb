##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>2</version>
  <name>TS_CMHAL_HTTP_Download</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetParamUlongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To download the firmware in the device</synopsis>
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
    <test_case_id>TC_CMHAL_58</test_case_id>
    <test_objective>To download the firmware in the device</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_Set_HTTP_Download_Url()
cm_hal_Get_HTTP_Download_Url()
cm_hal_Set_HTTP_Download_Interface()
cm_hal_HTTP_Download()
cm_hal_Get_HTTP_Download_Status()
cm_hal_HTTP_Download_Reboot_Now()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the CMHAL module
2. Get and save the firmware filename and location
3. Get and save the download interface
4. Set the download interface
5. Set the download url and filename
6. Start the download using cm_hal_HTTP_Download()
7. Check the status of download
8. Revert the values
9. Unload module</automation_approch>
    <except_output>The specified file should be downloaded successfully in the device</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_HTTP_Download</test_script>
    <skipped>No</skipped>
    <release_version>M62</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from tdkbVariables import *;
from xconfVariables import *;
import xconfUtilityLib;
from xconfUtilityLib import *
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_HTTP_Download');
obj1.configureTestCase(ip,port,'TS_CMHAL_HTTP_Download');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");

    FirmwareVersion, FirmwareFilename = xconfUtilityLib.getFirmwareDetails(obj1)
    print FirmwareFilename;
    if FirmwareFilename:
	tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
        tdkTestObj.addParameter("paramName","DownloadInterface");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        downInterface = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Download interface";
            print "EXPECTED RESULT 2: Should get the Download interface sucessfully";
            print "ACTUAL RESULT 2: Download interface is %s" %downInterface;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    tdkTestObj = obj.createTestStep("CMHAL_GetHTTP_Download_Url");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            downURL = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the download url and filename";
                print "EXPECTED RESULT 3: Should get the download url and filename";
                print "ACTUAL RESULT 3: %s" %downURL;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Interface");
                tdkTestObj.addParameter("interface",0);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Set the download interface";
                    print "EXPECTED RESULT 4: Should set the download interface";
                    print "ACTUAL RESULT 4:  ",details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
                    tdkTestObj.addParameter("paramName","DownloadInterface");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult and int(details) == 0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Get the Download interface";
                        print "EXPECTED RESULT 5: Should get the Download interface sucessfully";
                        print "ACTUAL RESULT 5: Download interface is %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

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
                            print "TEST STEP 6: Set the Download url and filename";
                            print "EXPECTED RESULT 6: Should set the Download url and filename";
                            print "ACTUAL RESULT 6: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            tdkTestObj = obj.createTestStep("CMHAL_GetHTTP_Download_Url");
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            if expectedresult in actualresult :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7: Get the download url and filename";
                                print "EXPECTED RESULT 7: Should get the download url and filename";
                                print "ACTUAL RESULT 7: %s" %details;
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
                                    print "TEST STEP 8: Start the download";
                                    print "EXPECTED RESULT 8: Should start the download successfully";
                                    print "ACTUAL RESULT 8: %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

			            #wait till download is complete
			            time.sleep(300);
        	                    #Script to load the configuration file of the component
        	                    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
        	                    tdkTestObj.addParameter("paramName","HTTP_Download_Status");
        	                    expectedresult="SUCCESS";
        	                    tdkTestObj.executeTestCase(expectedresult);
        	                    actualresult = tdkTestObj.getResult();
        	                    details = int(tdkTestObj.getResultDetails());
            		            success_status = "";
            		            fail_status = "";
				    print details;
        	                    if 0<details<=100:
        	                        success_status = str(details),"% download completed";
            		            elif details == 200:
            		                success_status = "Download is completed and waiting for reboot";
        	                    elif details ==0 or details >100:
        	                        status_list = {0:"Download is not started",400:"Invalided Http server Url",401:"Cannot connect to Http server",402:"File is not found on Http server",403:"HW_Type_DL_Protection Failure",404:"HW Mask DL Protection Failure",405:"DL Rev Protection Failure",406:"DL Header Protection Failure",407:"DL CVC Failure",500:"General Download Failure"};
        	                        fail_status = status_list[details];
        	                    else:
        	                        status = "Invalid status", details
        	                    if expectedresult in actualresult and success_status :
        	                        #Set the result status of execution
        	                        tdkTestObj.setResultStatus("SUCCESS");
        	                        print "TEST STEP 9: Get the Download status";
        	                        print "EXPECTED RESULT 9: Should get the Download status successfully";
        	                        print "ACTUAL RESULT 9: %s" %success_status;
        	                        #Get the result of execution
        	                        print "[TEST EXECUTION RESULT] : SUCCESS";

        	            	    else:
            		    	        #Set the result status of execution
                            	        tdkTestObj.setResultStatus("FAILURE");
                            	        print "TEST STEP 9: Get the Download status";
                            	        print "EXPECTED RESULT 9: Should get the Download status successfully";
                            	        print "ACTUAL RESULT 9: %s" %fail_status;
                            	        #Get the result of execution
                            	        print "[TEST EXECUTION RESULT] : FAILURE";
        	      	        else:
            		    	    #Set the result status of execution
                            	    tdkTestObj.setResultStatus("FAILURE");
                            	    print "TEST STEP 8: Start the download";
                            	    print "EXPECTED RESULT 8: Should start the download successfully";
                            	    print "ACTUAL RESULT 8: %s" %details;
                            	    #Get the result of execution
                            	    print "[TEST EXECUTION RESULT] : FAILURE";
                    	    else:
                    	        tdkTestObj.setResultStatus("FAILURE");
            	    	        print "TEST STEP 7: Get the download url and filename";
                    	        print "EXPECTED RESULT 7: Should get the download url and filename";
                    	        print "ACTUAL RESULT 7: %s" %details;
                    	        #Get the result of execution
                    	        print "[TEST EXECUTION RESULT] : FAILURE";
                	else:
            		    tdkTestObj.setResultStatus("FAILURE");
            		    print "TEST STEP 6: Set the Download url and filename";
                	    print "EXPECTED RESULT 6: Should set the Download url and filename";
                	    print "ACTUAL RESULT 6: %s" %details;
                	    #Get the result of execution
            		    print "[TEST EXECUTION RESULT] : FAILURE";
            	    else:
            	        tdkTestObj.setResultStatus("FAILURE");
            	        print "TEST STEP 5: Get the Download interface";
            	        print "EXPECTED RESULT 5: Should get the Download interface sucessfully";
            	        print "ACTUAL RESULT 5: Download interface is %s" %details;
            	        #Get the result of execution
            	        print "[TEST EXECUTION RESULT] : FAILURE";
        	else:
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("FAILURE");
        	    print "TEST STEP 4: Set the download interface";
        	    print "EXPECTED RESULT 4: Should set the download interface";
        	    print "ACTUAL RESULT 4:  ",details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : FAILURE";
		#revert Download URL value
        	URL=downURL.split(" ")[2].replace(",","");
        	print URL;
        	fileName=downURL.split(" ")[5];
        	print fileName;
        	tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Url");
        	tdkTestObj.addParameter("httpURL",URL);
        	tdkTestObj.addParameter("filename",fileName);
        	expectedresult="SUCCESS";
        	tdkTestObj.executeTestCase(expectedresult);
        	actualresult = tdkTestObj.getResult();
        	details = tdkTestObj.getResultDetails();

        	if expectedresult in actualresult :
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("SUCCESS");
        	    print "TEST STEP : Set the Download url and filename";
        	    print "EXPECTED RESULT : Should set the Download url and filename";
        	    print "ACTUAL RESULT : %s" %details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP : Set the Download url and filename";
                    print "EXPECTED RESULT : Should set the Download url and filename";
                    print "ACTUAL RESULT : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
        	#Revert the download interface
		tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Interface");
        	tdkTestObj.addParameter("interface",int(downInterface));
        	expectedresult="SUCCESS";
        	tdkTestObj.executeTestCase(expectedresult);
        	actualresult = tdkTestObj.getResult();
        	details = tdkTestObj.getResultDetails();

        	if expectedresult in actualresult :
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("SUCCESS");
        	    print "TEST STEP : Set the download interface";
        	    print "EXPECTED RESULT : Should set the download interface";
        	    print "ACTUAL RESULT :  ",details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : SUCCESS";
        	else:
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("FAILURE");
        	    print "TEST STEP : Set the download interface";
        	    print "EXPECTED RESULT : Should set the download interface";
        	    print "ACTUAL RESULT :  ",details;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
	        #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the download url and filename";
                print "EXPECTED RESULT 3: Should get the download url and filename";
                print "ACTUAL RESULT 3: %s" %downURL;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Download interface";
            print "EXPECTED RESULT 2: Should get the Download interface sucessfully";
            print "ACTUAL RESULT 2: Download interface is %s" %downInterface;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	print "Failed to get the firmware details"
    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
