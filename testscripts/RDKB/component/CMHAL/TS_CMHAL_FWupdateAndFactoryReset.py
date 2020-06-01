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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_CMHAL_FWupdateAndFactoryReset</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_FWupdateAndFactoryReset</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the functionality of cmhal_FWupdateAndFactoryReset .</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_CMHAL_78</test_case_id>
    <test_objective>To download the firmware in the device using cm_hal_FWupdateAndFactoryReset</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_Set_HTTP_Download_Url()
cm_hal_Get_HTTP_Download_Url()
cm_hal_Set_HTTP_Download_Interface()
cm_hal_HTTP_Download()
cm_hal_Get_HTTP_Download_Status()
cm_hal_HTTP_Download_Reboot_Now()
cm_hal_FWupdateAndFactoryReset()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the CMHAL module
2. Get and save the firmware filename and location
3. Get and save the download interface
4. Set the download interface
5. Set the download url and filename
6. Start the download using cm_hal_HTTP_Download()
7. Once the download is completed successfully call for cm_hal_FWupdateAndFactoryReset()
8. Check the status of download
9. Revert to previous image if the download was successful
10. Unload module</automation_approch>
    <expected_output>The specified file should be downloaded successfully in the device and  the device should go for a factory rest</expected_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_FWupdateAndFactoryReset</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_CMHAL_FWUpdateAndFactoryReset');
obj1.configureTestCase(ip,port,'TS_CMHAL_FWUpdateAndFactoryReset');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

def GetDownloadInterface():

    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
    tdkTestObj.addParameter("paramName","DownloadInterface");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    downInterface = tdkTestObj.getResultDetails();

    return tdkTestObj,actualresult ,downInterface

def GetHTTP_Download_Url():

    tdkTestObj = obj.createTestStep("CMHAL_GetHTTP_Download_Url");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    downURL = tdkTestObj.getResultDetails();

    return tdkTestObj,actualresult,downURL

def SetHTTP_Download_Interface(interface):

    tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Interface");
    tdkTestObj.addParameter("interface",interface);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    return tdkTestObj,actualresult,details

def SetHTTP_Download_Url(FIRMWARELOCATION,FirmwareFilename):

    tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Url");
    tdkTestObj.addParameter("httpURL",FIRMWARELOCATION);
    tdkTestObj.addParameter("filename",FirmwareFilename);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    return tdkTestObj,actualresult,details


if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():

    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    actualresult, xconfFile = xconfUtilityLib.overrideServerUrl(obj1, CDN_MOC_SERVER);
    ###get details of the current firmware in the device
    Old_FirmwareVersion, Old_FirmwareFilename = xconfUtilityLib.getCurrentFirmware(obj1);
    FirmwareVersion, FirmwareFilename = xconfUtilityLib.getFirmwareDetails(obj1)
    print FirmwareFilename;

    #####create a list of FW names and versions to be flashed, including current image name for reverting back
    FwNames = [FirmwareFilename,Old_FirmwareFilename]
    oldFw = [Old_FirmwareFilename,FirmwareFilename]

    if FirmwareFilename:

        for i in range (0,2):
            tdkTestObj,actualresult,downInterface = GetDownloadInterface();
            if expectedresult in actualresult:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 2: Get the Download interface";
               print "EXPECTED RESULT 2: Should get the Download interface sucessfully";
               print "ACTUAL RESULT 2: Download interface is %s" %downInterface;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";

               tdkTestObj,actualresult,downURL =GetHTTP_Download_Url();
               if expectedresult in actualresult :
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("SUCCESS");
                  print "TEST STEP 3: Get the download url and filename";
                  print "EXPECTED RESULT 3: Should get the download url and filename";
                  print "ACTUAL RESULT 3: %s" %downURL;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : SUCCESS";

                  interface = 1;
                  tdkTestObj,actualresult,details = SetHTTP_Download_Interface(interface);
                  if expectedresult in actualresult :
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 4: Set the download interface";
                     print "EXPECTED RESULT 4: Should set the download interface";
                     print "ACTUAL RESULT 4:  ",details;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";

                     tdkTestObj,actualresult,details =  GetDownloadInterface();
                     if expectedresult in actualresult and int(details) == 1:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Get the Download interface";
                        print "EXPECTED RESULT 5: Should get the Download interface sucessfully";
                        print "ACTUAL RESULT 5: Download interface is %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        tdkTestObj,actualresult,SetURL = SetHTTP_Download_Url(FIRMWARELOCATION,FwNames[i]);
                        if expectedresult in actualresult :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Set the Download url and filename";
                            print "EXPECTED RESULT 6: Should set the Download url and filename";
                            print "ACTUAL RESULT 6: %s" %SetURL;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            tdkTestObj,actualresult,details = GetHTTP_Download_Url();
                            URL = details.split(",")[0].split("is")[1].strip();
                            firmwarename = details.split(",")[1].split("is")[1].strip();

                            if expectedresult in actualresult  and FIRMWARELOCATION == URL and FwNames[i] == firmwarename:
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

                                    while 1:
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
                                          sleep(2);
                                          success_status = str(details),"% download completed";
                                       elif details == 200:
                                            success_status = "Download is completed and waiting for reboot";
                                            break;
                                       elif details ==0 or details >100:
                                            status_list = {0:"Download is not started",400:"Invalided Http server Url",401:"Cannot connect to Http server",402:"File is not found on Http server",403:"HW_Type_DL_Protection Failure",404:"HW Mask DL Protection Failure",405:"DL Rev Protection Failure",406:"DL Header Protection Failure",407:"DL CVC Failure",500:"General Download Failure"};
                                            fail_status = status_list[details];
                                            break;
                                       else:
                                           status = "Invalid status", details
                                           break;

                                    if expectedresult in actualresult and success_status :
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "TEST STEP 9: Get the Download status";
                                        print "EXPECTED RESULT 9: Should get the Download status successfully";
                                        print "ACTUAL RESULT 9: %s" %success_status;
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";

                                        obj.saveCurrentState();

                                        tdkTestObj = obj.createTestStep("CMHAL_FWupdateAndFactoryReset");
                                        expectedresult="SUCCESS";
                                        tdkTestObj.executeTestCase(expectedresult);
                                        actualresult = tdkTestObj.getResult();
                                        details= tdkTestObj.getResultDetails();
                                        if expectedresult in actualresult :
                                           #Set the result status of execution
                                           tdkTestObj.setResultStatus("SUCCESS");
                                           print "TEST STEP 10: Invoke cm_hal_FWupdateAndFactoryReset";
                                           print "EXPECTED RESULT 10: Should Invoke cm_hal_FWupdateAndFactoryReset";
                                           print "ACTUAL RESULT 10: %s" %details;
                                           #Get the result of execution
                                           print "[TEST EXECUTION RESULT] : SUCCESS";
                                           obj.restorePreviousStateAfterReboot();

                                           New_FirmwareVersion, New_FirmwareFilename = xconfUtilityLib.getCurrentFirmware(obj1);
                                           if New_FirmwareFilename != oldFw[i]:
                                              tdkTestObj.setResultStatus("SUCCESS");
                                              print "EXPECTED RESULT : The new FirmwareFilename should not be same as the old FirmwareFilename"
                                              print "ACTUAL RESULT : The new FirmwareFilename is not the same as the old FirmwareFilename"
                                              print "[TEST EXECUTION RESULT] : SUCCESS"
                                           else:
                                               tdkTestObj.setResultStatus("FAILURE");
                                               print "EXPECTED RESULT : The new FirmwareFilename should not be same as the old FirmwareFilename"
                                               print "ACTUAL RESULT :The new FirmwareFilename is not the same as the old FirmwareFilename"
                                               print "[TEST EXECUTION RESULT] : FAILURE"

                                        else:
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "TEST STEP 10: Invoke cm_hal_FWupdateAndFactoryReset";
                                            print "EXPECTED RESULT 10: Should Invoke cm_hal_FWupdateAndFactoryReset";
                                            print "ACTUAL RESULT 10: %s" %details;
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] :FAILURE";
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "TEST STEP 9: Get the Download status";
                                        print "EXPECTED RESULT 9: Should get the Download status successfully";
                                        print "ACTUAL RESULT 9: %s" %fail_status;
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";

                                        # The loop should continue if the image was downloaded  successful
                                        print "******************************************************************************"
                                        print "The image download was not successful hence exiting out of the loop as no revertion required"
                                        print "********************************************************************************"
                                        break;
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
                            print "ACTUAL RESULT 6: %s" %SetURL;
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

    xconfUtilityLib.restoreOverrideFile(obj1, xconfFile);
    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
