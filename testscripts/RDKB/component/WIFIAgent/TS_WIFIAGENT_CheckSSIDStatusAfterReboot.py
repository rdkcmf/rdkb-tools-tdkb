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
  <name>TS_WIFIAGENT_CheckSSIDStatusAfterReboot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Validate the persistent of Private, Home security and Public SSID Enable status across reboots</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WIFIAGENT_92</test_case_id>
    <test_objective>Validate the persistence of Private, Home security and Public SSID Enable status across reboots</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.1.Enable ,
Device.WiFi.SSID.2.Enable ,
Device.WiFi.SSID.3.Enable ,
Device.WiFi.SSID.4.Enable,
Device.WiFi.SSID.5.Enable,
Device.WiFi.SSID.6.Enable
	</input_parameters>
    <automation_approch>1.Load the module.
2. Get and save the current SSID enable status values of private,home security and public wifi
3. Set the SSID enable as false for  private,home security and public wifi and return SUCCESS for non empty value,else FAILURE.
4. Reboot the device
5. Verify the SSID status after reboot, return SUCCESS for Disabled case , else FAILURE
6. Revert back the SSID enable status value for private , home security and public wifi
7.Unload module.</automation_approch>
    <expected_output>Private, Home security and Public SSID Enable status should be persistent across reboots</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckSSIDStatusAfterReboot</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from xfinityWiFiLib import *

#Test component to be tested
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckSSIDStatusAfterReboot');

def wifi_SSID_Set_Call(parameterName,parameterValue):
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName",parameterName);
    tdkTestObj.addParameter("paramValue",parameterValue);
    tdkTestObj.addParameter("paramType","boolean");
    expectedresult="SUCCESS"
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresultSet = tdkTestObj.getResult();
    detailsSet = tdkTestObj.getResultDetails();
    if expectedresult in actualresultSet:
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        tdkTestObj.setResultStatus("FAILURE");
    return actualresultSet, detailsSet;

def wifi_SSID_Get_Call(parameterName):
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName",parameterName);
    expectedresult="SUCCESS"
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    detailsGet = tdkTestObj.getResultDetails();
    ssidStatus = detailsGet.split("VALUE:")[1].split(' ')[0];
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        tdkTestObj.setResultStatus("FAILURE");
    return actualresult, ssidStatus;

#Get the result of connection with test component and DUT
wifiloadmodulestatus=wifiobj.getLoadModuleResult();

if "SUCCESS" in wifiloadmodulestatus.upper():
    #Set the result status of execution
    wifiobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS"
    ssid1Result,orgSSID1Status = wifi_SSID_Get_Call("Device.WiFi.SSID.1.Enable");
    ssid2Result,orgSSID2Status = wifi_SSID_Get_Call("Device.WiFi.SSID.2.Enable");

    if expectedresult in ssid1Result and  expectedresult in ssid2Result:
        #Set the result status of execution
        print "TEST STEP 1 : Get Private SSID's Enable Status";
        print "EXPECTED RESULT 1: Should Get the Private SSID's Enable status";
        print "ACTUAL RESULT 1: Get Function for Private SSID's Enable status Success %s and %s"%(orgSSID1Status,orgSSID2Status);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        ssid3Result,orgSSID3Status = wifi_SSID_Get_Call("Device.WiFi.SSID.3.Enable");
        ssid4Result,orgSSID4Status = wifi_SSID_Get_Call("Device.WiFi.SSID.4.Enable");

        if expectedresult in ssid3Result and  expectedresult in ssid4Result:
            #Set the result status of execution
            print "TEST STEP 2: Get Home Security SSID's Enable status";
            print "EXPECTED RESULT 2: Should Get Home Security SSID's Enable status";
            print "ACTUAL RESULT 2: Get Home Security SSID's Enable status success %s and %s"%(orgSSID3Status,orgSSID4Status);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            # Get current values of public wifi params
            tdkTestObj,publicWiFiGetResult,orgValue = getPublicWiFiParamValues(wifiobj);

            if expectedresult in publicWiFiGetResult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Get values of PublicWiFi params"
                print "TEST STEP 3 : Should get values of PublicWiFi params"
                print "ACTUAL RESULT 3:%s" %orgValue
                print "[TEST EXECUTION RESULT] : SUCCESS";
                ssid1SetResult,detailsSSID1 = wifi_SSID_Set_Call("Device.WiFi.SSID.1.Enable","false");
                ssid2SetResult,detailsSSID2 = wifi_SSID_Set_Call("Device.WiFi.SSID.2.Enable","false");

                if expectedresult in ssid1SetResult and expectedresult in ssid2SetResult:
                    #Set the result status of execution
                    print "TEST STEP 4: Disable Private WiFi SSID";
                    print "EXPECTED RESULT 4: Should disable WiFi";
                    print "ACTUAL RESULT 4: SSID 1:%s and SSID 2:%s" %(detailsSSID1,detailsSSID2);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    ssid3SetResult,detailsSSID3 = wifi_SSID_Set_Call("Device.WiFi.SSID.3.Enable","false");
                    ssid4SetResult,detailsSSID4 = wifi_SSID_Set_Call("Device.WiFi.SSID.4.Enable","false");

                    if expectedresult in ssid3SetResult and expectedresult in ssid4SetResult:
                        #Set the result status of execution
                        print "TEST STEP 5: Disable Home Seurity WiFi SSID's";
                        print "EXPECTED RESULT 5: Should disable WiFi";
                        print "ACTUAL RESULT 5: SSID 3:%s and SSID 4:%s" %(detailsSSID3,detailsSSID4);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Set false to xfinitywifiEnable
                        setvalues = ["44","68.86.15.199","68.86.15.171","true","true","false"];
                        tdkTestObj, publicWiFiSetResult, details = setPublicWiFiParamValues(wifiobj,setvalues);
                        if expectedresult in publicWiFiSetResult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Disable public wifi "
                            print "TEST STEP 6 : Should disable PublicWiFi"
                            print "ACTUAL RESULT 6:%s" %details
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #rebooting the device
                            wifiobj.initiateReboot();
                            sleep(300);
                            tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
                            ssid1GetResult,newSSID1Status = wifi_SSID_Get_Call("Device.WiFi.SSID.1.Enable");
                            ssid2GetResult,newSSID2Status = wifi_SSID_Get_Call("Device.WiFi.SSID.2.Enable");
                            if expectedresult in ssid1GetResult and expectedresult in ssid2GetResult and "false" == newSSID1Status and  "false" == newSSID2Status:
                                print "TEST STEP 7: Check if Private SSID's SSID1 and SSID2 are Disabled";
                                print "EXPECTED RESULT 7: SSID1 and SSID2 staus should be Disabled";
                                print "ACTUAL RESULT 7: Status is %s %s" %(newSSID1Status,newSSID2Status);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                ssid3GetResult,newSSID3Status  = wifi_SSID_Get_Call("Device.WiFi.SSID.3.Enable");
                                ssid4GetResult,newSSID4Status  = wifi_SSID_Get_Call("Device.WiFi.SSID.4.Enable");

            	                if expectedresult in ssid3GetResult and expectedresult in ssid4GetResult and "false" == newSSID3Status and  "false" == newSSID4Status:
                                    print "TEST STEP 8: Check if Home security SSID's SSID3 and SSID4 are Disabled";
                                    print "EXPECTED RESULT 8: SSID3 and SSID4 staus should be Disabled";
                                    print "ACTUAL RESULT 8: Status is %s %s" %(newSSID3Status,newSSID4Status);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                    ssid5GetResult,newSSID5Status = wifi_SSID_Get_Call("Device.WiFi.SSID.5.Enable");
                                    ssid6GetResult,newSSID6Status = wifi_SSID_Get_Call("Device.WiFi.SSID.6.Enable");

                                    if expectedresult in ssid5GetResult and expectedresult in ssid6GetResult and "false" == newSSID5Status and  "false" == newSSID6Status:
                                        print "TEST STEP 9: Check if Publi WiFi SSID's SSID5 and SSID6 are Disabled";
                                        print "EXPECTED RESULT 9: SSID6 and SSID6 status should be Disabled";
                                        print "ACTUAL RESULT 9: Status is %s %s" %(newSSID5Status,newSSID6Status);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else:
                                        print "TEST STEP 9: Check if Public SSID's SSID5 and SSID6 are Disabled";
                                        print "EXPECTED RESULT 9: SSID5 and SSID6 status should be Disabled";
                                        print "ACTUAL RESULT 9: Status is %s %s" %(newSSID5Status,newSSID6Status);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
            	                else:
                                    print "TEST STEP 8: Check if Home Security SSIDs SSID3 and SSID4 are Disabled";
                                    print "EXPECTED RESULT 8: SSID3 and SSID4 status should be Disabled";
                                    print "ACTUAL RESULT 8: Status is %s %s" %(newSSID3Status,newSSID4Status);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                print "TEST STEP 7: Check if SSID1 and SSID2 is Disabled";
                                print "EXPECTED RESULT 7: SSID1 and SSID2 status should be Disabled";
                                print "ACTUAL RESULT 7: Status is %s %s" %(newSSID1Status,newSSID2Status);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";

                            #Revert the values of public wifi params
                            tdkTestObj, publicWiFirevertSetResult, details = setPublicWiFiParamValues(wifiobj,orgValue);
		            if expectedresult in publicWiFirevertSetResult:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 10:Revert the Public WiFi param values"
           		        print "EXPECTED RESULT 10 : Should revert the PublicWiFi values"
            		        print "ACTUAL RESULT 10 :%s" %details
                                print "[TEST EXECUTION RESULT] : SUCCESS";
		            else:
               		        tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 10 : Revert the PublicWiFi param values"
                                print "TEST STEP 10 : Should revert the PublicWiFi param values"
                	        print "ACTUAL RESULT 10 :%s" %details
                	        print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Disable public wifi "
                            print "TEST STEP 6 : Should disable PublicWiFi"
                            print "ACTUAL RESULT 6 :%s" %details
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";

                        ssid3RevertSetResult,ssid3RevertSetDetails = wifi_SSID_Set_Call("Device.WiFi.SSID.3.Enable",orgSSID3Status);
                        ssid4RevertSetResult,ssid4RevertSetDetails = wifi_SSID_Set_Call("Device.WiFi.SSID.4.Enable",orgSSID4Status);
                        if expectedresult in ssid3RevertSetResult and expectedresult in ssid4RevertSetResult:
                            print "TEST STEP 11: Set the Home security WIFI SSID's Enable with Original value";
                            print "EXPECTED RESULT 11: Should set the Home security WiFi SSID's Enable value";
                            print "ACTUAL RESULT 11: Home security SSID Enable with original value - Success %s and %s"%(ssid3RevertSetDetails,ssid4RevertSetDetails);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            print "TEST STEP 11: Set the Home security WIFI SSID's Enable with Original value";
                            print "EXPECTED RESULT 11: Should set the Home security WiFi SSID's Enable value";
                            print "ACTUAL RESULT 11: Home security SSID Enable with original value - Failure  %s and %s"%(ssid3RevertSetDetails,ssid4RevertSetDetails);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "TEST STEP 5: Disable Home Seurity WiFi SSID's";
                        print "EXPECTED RESULT 5: Should disable WiFi";
                        print "ACTUAL RESULT 5: SSID 3:%s and SSID 4:%s" %(newSSID3Status,newSSID4Status);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Revert the Private SSID values to original
                    ssid1RevertSetResult,ssid1RevertSetDetails = wifi_SSID_Set_Call("Device.WiFi.SSID.1.Enable",orgSSID1Status);
                    ssid2RevertSetResult,ssid2RevertSetDetails = wifi_SSID_Set_Call("Device.WiFi.SSID.2.Enable",orgSSID2Status);

                    if expectedresult in ssid1RevertSetResult and expectedresult in ssid2RevertSetResult:
                        print "TEST STEP 12: Set the private SSID's Enable with Original value";
                        print "EXPECTED RESULT 12: Should set the private SSID's Enable value";
                        print "ACTUAL RESULT 12: Private SSID Enable with original value - Success %s and %s"%(ssid1RevertSetDetails,ssid2RevertSetDetails);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        print "TEST STEP 12: Set the private SSID's Enable with Original value";
                        print "EXPECTED RESULT 12: Should set the private SSID's Enable value";
                        print "ACTUAL RESULT 12: Private SSID Enable with original value - Failure  %s and %s"%(ssid1RevertSetDetails,ssid2RevertSetDetails);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "TEST STEP 4: Disable Private WiFi SSID";
                    print "EXPECTED RESULT 4: Should disable WiFi";
                    print "ACTUAL RESULT 4: SSID 1:%s and SSID 2:%s" %(newSSID1Status,newSSID2Status);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "TEST STEP 3: Get Xfinity WiFi SSID's Enable status";
                print "EXPECTED RESULT 3: Should get Xfinity WiFi SSID's Enable status ";
                print "ACTUAL RESULT 3: Get Xfinity WiFi SSID's Enable status : Failed %s" %orgValue;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "TEST STEP 2: Get Home Security SSID's Enable status";
            print "EXPECTED RESULT 2: Should Get Home Security SSID's Enable status";
            print "ACTUAL RESULT 2: Get Home Security SSID's Enable status Failed %s and %s"%(orgSSID3Status,orgSSID4Status);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "TEST STEP 1 : Get Private SSID's Enable Status";
        print "EXPECTED RESULT 1: Should Get the Private SSID's Enable status";
        print "ACTUAL RESULT 1: Get Function for Private SSID's Enable status Failed %s and %s"%(orgSSID1Status,orgSSID2Status);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load wifiagent module";
    wifiobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
