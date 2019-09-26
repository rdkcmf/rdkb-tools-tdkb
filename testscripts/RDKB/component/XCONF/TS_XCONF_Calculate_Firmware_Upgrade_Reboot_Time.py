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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_XCONF_Calculate_Firmware_Upgrade_Reboot_Time</name>
  <primitive_test_id/>
  <primitive_test_name>XCONF_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>40</execution_time>
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
    <test_case_id>TC_XCONF_18</test_case_id>
    <test_objective>Calculate the Reboot time taken for  firmware up gradation and ensure it is less than 4 minutes</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>Set proper values in tdk_platform.properties file and xconfVariables.py</pre_requisite>
    <api_or_interface_used>getFirmwareDetails
ExecuteCmd
GetPlatformProperties
removeLog</api_or_interface_used>
    <input_parameters>INTERFACE_FOR_ESTB_MAC
ifconfig " + interface + "| grep HWaddr | awk '{ print $NF }' | tr \"\n\" \" \""
CDN_LOG
CDN_FILE</input_parameters>
    <automation_approch>1. Load sysutil module
2)Store the firmwareVersion and firmwareName
as old firmwareVersion  and old firmwareName
3. Form the curl command for xconf configuration, by using getFirmwareDetails.
4. Get CDN_LOG and CDN_FILE values from the device
5. Remove previous logs, CDN_LOG
6. Execute CDN_FILE
7.Take Initial  time
8.Reboot The DUT
9.Take final Time
10.Ensure DUT has the diffrent  firmware  by comparing the new firmwareVersion and new firmwareName  with the old ones.The Reboot  time for the firmware up-gradation should be less than 4 minutes
11. Unload sysutil module</automation_approch>
    <except_output>The Reboot  time for the firmware up-gradation should be less than 4 minutes</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_XCONF_Calculate_Firmware_Upgrade_Reboot_Time</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import xconfUtilityLib;
from xconfUtilityLib import *
from xconfVariables import *
import time
import datetime
from datetime import datetime

obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_XCONF_Calculate_FW_Upgrade_Reboot_Time');
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"
    actualresult, xconfFile = xconfUtilityLib.overrideServerUrl(obj, CDN_MOC_SERVER);

    ###get details of the current firmware in the device
    Old_FirmwareVersion, Old_FirmwareFilename = xconfUtilityLib.getCurrentFirmware(obj);
    #get firmware details
    FirmwareVersion, FirmwareFilename = xconfUtilityLib.getFirmwareDetails(obj)

    #####create a list of FW names and versions to be flashed, including current image name for reverting back
    FwNames = [FirmwareVersion, FirmwareFilename, Old_FirmwareVersion, Old_FirmwareFilename]
    oldFw = [Old_FirmwareVersion, Old_FirmwareFilename, FirmwareVersion, FirmwareFilename]

    for i in range (0,3,2):
        ####form the curl command to set the configuration details of the device in the mock server
	Curl_CMD = xconfUtilityLib.getXCONFServerConfigCmd(obj, FwNames[i], FwNames[i+1], "http")
        tdkTestObj = obj.createTestStep('ExecuteCmd');

        print "Curl Request Formed:",Curl_CMD
        tdkTestObj.addParameter("command",Curl_CMD);
        tdkTestObj.executeTestCase("SUCCESS");

        #Get the result of execution
        result = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if "Successfully added configuration" in details:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Execute curl cmnd to  add device configuration"
            print "EXPECTED RESULT 3: Should add device configuration"
            print "ACTUAL RESULT 3: Status: %s " %details
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "SUCCESS:Executed Curl Command"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Execute curl cmnd to  add device configuration"
            print "EXPECTED RESULT 3: Should add device configuration"
            print "ACTUAL RESULT 3: Status: %s " %details
            print "[TEST EXECUTION RESULT] :FAILURE:Failed to execute Curl Command";

        ################get log file name from tdk_platform.properties
        actualresult, propVal = xconfUtilityLib.GetPlatformProperties(obj, "CDN_LOG");
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            cdnLog = propVal
            print "SUCCESS:get log file name"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "FAILURE:failed to get log file name"

        ################get CDN file name from tdk_platform.properties
        actualresult, propVal = xconfUtilityLib.GetPlatformProperties(obj, "CDN_FILE");
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "SUCCESS:get cdn file name"
            cdnFile = propVal
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "FAILURE:failed to get log file name"

        #Remove the exsisting logs
        result = xconfUtilityLib.removeLog(obj, cdnLog);
        if "SUCCESS" in result:
            	#Execute cdnFile
                    tdkTestObj.addParameter("command", cdnFile + " > /dev/null 2>&1 &");
                    tdkTestObj.executeTestCase("SUCCESS");

                    result = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if "SUCCESS" in result:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Initiate firmware download"
                        print "EXPECTED RESULT 5: firmware download should be initiated"
                        print "ACTUAL RESULT 5: is %s " %details
                        print "[TEST EXECUTION RESULT] : SUCCESS"

                         ###Sleeping till httpdownload completed 
                        time.sleep(240)
                        tdkTestObj = obj.createTestStep('ExecuteCmd');
                        ######search for patterns in Log
                        tdkTestObj.addParameter("command","grep -inr \"HTTP download Successful\" " + cdnLog + " ;echo $?")
                        tdkTestObj.executeTestCase("SUCCESS");

                        result = tdkTestObj.getResult();
                        print "[TEST EXECUTION RESULT] : %s" %result;
                        details = tdkTestObj.getResultDetails();
                        print "[TEST EXECUTION DETAILS] : %s" %details;
                        if "0" in details.lower():
                            print "TEST STEP 6: Search for pattern in logs"
                            print "EXPECTED RESULT 6: Should find the pattern in the logs"
                            print "ACTUAL RESULT 6: is %s " %details
                            print "[TEST EXECUTION RESULT] : SUCCESS"
                            tdkTestObj.setResultStatus("SUCCESS");
            	 	#Take the Initial time using datetime.now() and Store to Initial_Time varaible	
                            Initial_Time=datetime.now()
                            print "Initial_Time is ",Initial_Time
                            #Reboot the box
                            obj.initiateReboot();
            	 	#take the final time using datetime.now() and Store to Final_Time varaible.Take the diffrence between Final_Time nad Ini                         tial time in minutes
                            Final_Time = datetime.now()
                            print "Final_Time is ",Final_Time
                            Total_Time=Final_Time - Initial_Time
                            Grand_Total_Time=Total_Time.seconds
                            Grand_Total_Time=Grand_Total_Time/60
                            print "Total time taken for FW updation is :",Grand_Total_Time
            		
                            New_FirmwareVersion, New_FirmwareFilename = xconfUtilityLib.getCurrentFirmware(obj);
                            if (New_FirmwareFilename != oldFw[i+1] and Grand_Total_Time <= 4):
                            	tdkTestObj.setResultStatus("SUCCESS");
                                print "EXPECTED RESULT : The Latest FirmwareVersion and FirmwareFilename should not be same as the old and the reboot time for FW updation is less than 4 minutes"
            	                print "ACTUAL RESULT : The FirmwareVersion and FirmwareFilename are should not remains same.Time taken for FW updation reboot is less than 4 minutes"
                    	        print "[TEST EXECUTION RESULT] : SUCCESS"
                            else:
                            	tdkTestObj.setResultStatus("FAILURE");
                                print "EXPECTED RESULT : The Latest FirmwareVersion and FirmwareFilename should not be same as the old and the reboot time for FW updation is less than 4 minutes"
                                print "ACTUAL RESULT :The FirmwareVersion and FirmwareFilename are same or time taken for FW updation reboot is greater  than 4 minutes"
            	                print "[TEST EXECUTION RESULT] : FAILURE"


                        else:

                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Search for pattern in logs"
                            print "EXPECTED RESULT 6: Should find the pattern in the logs"
                            print "ACTUAL RESULT 6: is %s " %details
                            print "[TEST EXECUTION RESULT] : FAILURE"


                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Initiate firmware download"
                        print "EXPECTED RESULT 5: firmware download should be initiated"
                        print "ACTUAL RESULT 5: is %s " %details
                        print "[TEST EXECUTION RESULT] : FAILURE"

    xconfUtilityLib.restoreOverrideFile(obj, xconfFile);
    obj.unloadModule("sysutil");
else:
    print"Load module failed";
    #Set the module loading status
    obj.setLoadModuleStatus("FAILURE");

