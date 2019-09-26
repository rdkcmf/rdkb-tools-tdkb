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
  <name>TS_XCONF_VerifyServerConfig</name>
  <primitive_test_id/>
  <primitive_test_name>XCONF_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the values we set for server configuration itself is returned as the response for the query from client.Skipping as the execution causes bad state in the device</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>true</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_XCONF_16</test_case_id>
    <test_objective>Check if the values we set for server configuration itself is returned as the response	for the query from client</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>Set proper values in tdk_platform.properties file and   xconfVariables.py</pre_requisite>
    <api_or_interface_used>GetPlatformProperties
ExecuteCmd
getXCONFServerConfigCmd</api_or_interface_used>
    <input_parameters>FWDL_RESPONSE
CDN_LOG
CDN_FILE
"rm " + cdnLog
"sh " + cdnFile + " &amp;"
"cat " + responseFile</input_parameters>
    <automation_approch>1. Load sysutil module
2. Remove the existing response file
3. Construct  and execute the curl command to configure server with the same image name as the device
4. Get CDN_LOG and CDN_FILE values from the device
5. Remove previous logs, CDN_LOG
6. Execute CDN_FILE
7. In the json response inside the response file, check if the values are the same as we passed in the curl command
8. Unload sysutil module</automation_approch>
    <except_output>Json values inside the response file should match the values we configured using curl command</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_XCONF_VerifyServerConfig</test_script>
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
from xconfUtilityLib import *;
from xconfVariables import *;
import time;
import ast;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XCONF_VerifyServerConfig');

result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    ####Override server url to be used as the mock server url
    actualresult, xconfFile = xconfUtilityLib.overrideServerUrl(obj, CDN_MOC_SERVER);

    ################get JSON response file name from tdk_platform.properties
    actualresult, propVal = xconfUtilityLib.GetPlatformProperties(obj, "FWDL_RESPONSE");
    if expectedresult in actualresult:
        print "SUCCESS:JSON response file name"
        responseFile = propVal
    else:
        print "FAILURE:failed to get log file name"

    ##########remove the previous response file
    result = xconfUtilityLib.removeLog(obj, responseFile);

    ###get details of the current firmware in the device
    FirmwareVersion, FirmwareFilename = xconfUtilityLib.getCurrentFirmware(obj);

    ####form the curl command to set the configuration details of the device in the mock server
    Curl_CMD = xconfUtilityLib.getXCONFServerConfigCmd(obj, FirmwareVersion, FirmwareFilename, "http")
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

    ################get JSON response file name from tdk_platform.properties
    actualresult, propVal = xconfUtilityLib.GetPlatformProperties(obj, "FWDL_RESPONSE");
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "SUCCESS:JSON response file name"
        responseFile = propVal
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "FAILURE:failed to get log file name"

    #Remove the exsisting logs
    result = xconfUtilityLib.removeLog(obj, cdnLog);
    if "SUCCESS" in result:
        tdkTestObj.addParameter("command", cdnFile + " &");
        tdkTestObj.executeTestCase("SUCCESS");

        result = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        #wait till log updation
        time.sleep(20)
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
    ######search for patterns in Log
    tdkTestObj.addParameter("command","cat " + responseFile)
    tdkTestObj.executeTestCase("SUCCESS");

    result = tdkTestObj.getResult();
    print "[TEST EXECUTION RESULT] : %s" %result;
    details = tdkTestObj.getResultDetails().strip();
    print "[TEST EXECUTION DETAILS] : %s" %details;
    if "SUCCESS" in result and details:
        print "TEST STEP 6: Get contents of response file"
        print "EXPECTED RESULT 6: Should Get contents of response file"
        print "ACTUAL RESULT 6: is %s " %details
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #####converting the json response string to a dictionary
        responseDict = ast.literal_eval(details.replace('\\', ''))

        if responseDict["firmwareFilename"] == FirmwareFilename and responseDict["firmwareDownloadProtocol"] == "http" and responseDict["firmwareLocation"] == FIRMWARELOCATION and responseDict["firmwareVersion"] == FirmwareVersion and responseDict["rebootImmediately"] == "false":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 6: Check if values in response are the same as the ones configured"
            print "EXPECTED RESULT 6: values in response should be the same as the ones configured"
            print "ACTUAL RESULT 6: values in response are the same as the ones configured"
            print "[TEST EXECUTION RESULT] : SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 6: Check if values in response are the same as the ones configured"
            print "EXPECTED RESULT 6: values in response should be the same as the ones configured"
            print "ACTUAL RESULT 6: values in response are not the same as the ones configured"
            print "[TEST EXECUTION RESULT] : FAILURE"
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

