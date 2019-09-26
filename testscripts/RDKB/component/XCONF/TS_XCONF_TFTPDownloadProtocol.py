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
  <version>1</version>
  <name>TS_XCONF_TFTPDownloadProtocol</name>
  <primitive_test_id/>
  <primitive_test_name>XCONF_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test if on configuring download protocol as tftp, client is going for retry 3 times</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_XCONF_10</test_case_id>
    <test_objective>Test if on configuring download protocol as tftp, client is going for retry 3 times</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>Make AUTO_SEARCH_IN_JENKINS true or false depending whether build name is to be fetched from jenkins or xconfVariables.py

If AUTO_SEARCH_IN_JENKINS is false,set proper firmware name in xconfVariables.py</pre_requisite>
    <api_or_interface_used>GetPlatformProperties
ExecuteCmd
getXCONFServerConfigCmd</api_or_interface_used>
    <input_parameters>"cat /version.txt | grep -i imagename | cut -d= -f 2 | tr \"\n\" \" \""
CDN_LOG
CDN_FILE
"rm " + cdnLog
"sh " + cdnFile + " &amp;"
grep \"RETRY is\" " + cdnLog + " | wc -l"</input_parameters>
    <automation_approch>1. Load sysutil module
3. Construct  and execute the curl command to configure server with download protocol as tftp
4. Get CDN_LOG and CDN_FILE values from the device
5. Remove previous logs, CDN_LOG
6. Execute CDN_FILE
7. In the response log of xconf server, check if retrial is happening thrice
8. Unload sysutil module</automation_approch>
    <except_output>In the response log of xconf server, retrial should happen thrice</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_XCONF_TFTPDownloadProtocol</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
import xconfUtilityLib;
from xconfUtilityLib import *
from xconfVariables import *
import time

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XCONF_TFTPDownloadProtocol');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    ####Override server url to be used as the mock server url
    actualresult, xconfFile = xconfUtilityLib.overrideServerUrl(obj, CDN_MOC_SERVER)

    ###get details of the current firmware in the device
    Old_FirmwareVersion, Old_FirmwareFilename = xconfUtilityLib.getCurrentFirmware(obj);

    #get firmware details from config file
    FirmwareVersion, FirmwareFilename = xconfUtilityLib.getFirmwareDetails(obj)

    ####form the curl command to set the configuration details of the device in the mock server
    Curl_CMD = xconfUtilityLib.getXCONFServerConfigCmd(obj, FirmwareVersion, FirmwareFilename, "tftp")
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
        ###########excute the shell script to download firware
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", cdnFile + " > /dev/null 2>&1 &");
        tdkTestObj.executeTestCase("SUCCESS");

        result = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        #wait till log updation
        time.sleep(300)
        if "SUCCESS" in result:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 5: Initiate firmware download"
            print "EXPECTED RESULT 5: firmware download should be initiated"
            print "ACTUAL RESULT 5: is %s " %details
            print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 5: Initiate firmware download"
            print "EXPECTED RESULT 5: firmware download should be initiated"
            print "ACTUAL RESULT 5: is %s " %details
            print "[TEST EXECUTION RESULT] : FAILURE"

    tdkTestObj = obj.createTestStep('ExecuteCmd');
    ######search in log whether retry is happening 3 times
    tdkTestObj.addParameter("command","grep \"RETRY is\" " + cdnLog + " | wc -l")
    tdkTestObj.executeTestCase("SUCCESS");

    result = tdkTestObj.getResult();
    print "[TEST EXECUTION RESULT] : %s" %result;
    details = tdkTestObj.getResultDetails();
    print "[TEST EXECUTION DETAILS] : %s" %details;
    if "3" in details.lower():
        print "TEST STEP 6: Search for pattern in logs"
        print "EXPECTED RESULT 6: Should find the pattern in the logs"
        print "ACTUAL RESULT 6: is %s " %details
        print "[TEST EXECUTION RESULT] : SUCCESS"
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 6: Search for pattern in logs"
        print "EXPECTED RESULT 6: Should find the pattern in the logs"
        print "ACTUAL RESULT 6: is %s " %details
        print "[TEST EXECUTION RESULT] : FAILURE"

    ###########restore the override file
    xconfUtilityLib.restoreOverrideFile(obj, xconfFile);

    obj.unloadModule("sysutil");
else:
    print"Load module failed";
    #Set the module loading status
    obj.setLoadModuleStatus("FAILURE");
