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
  <version>1</version>
  <name>TS_WEBPA_EPON_GetDefault_FirmwareDownloadStatus</name>
  <primitive_test_id/>
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Using webpa check if the default FirmwareDownloadStatus is "failed"</synopsis>
  <groups_id/>
  <execution_time>25</execution_time>
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
    <test_case_id>TC_WEBPA_25</test_case_id>
    <test_objective>Using webpa check if the default FirmwareDownloadStatus is "failed"</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>If SAT token is to be used, token should be created and made available in test manager. Also the config variables SAT_REQUIRED, SAT_TOKEN_FILE, SERVER_URI should be updated in webpaVariables.py</pre_requisite>
    <api_or_interface_used>webpaQuery
parseWebpaResponse</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus</input_parameters>
    <automation_approch>1. Load sysutil module
2. Configure WEBPA server to send get request for Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus
3. Parse the WEBPA response
4. If webpa response status is SUCCESS, get operation was success otherwise failure
5. Check if the default firmware download status returned is "Failure" or not
6. Unload sysutil module</automation_approch>
    <except_output>The default firmware download status returned should be "Failure" </except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_WEBPA_EPON_GetDefault_FirmwareDownloadStatus</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from webpaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBPA_EPON_GetDefault_FirmwareDownloadStatus');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:

        queryParam = {"name":"Device.DeviceInfo.X_RDKCENTRAL-COM_FirmwareDownloadStatus"}
        queryResponse = webpaQuery(obj, queryParam)

        parsedResponse = parseWebpaResponse(queryResponse, 1)
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "[TEST EXECUTION RESULT] : SUCCESS"

            fwDwnldStatus = parsedResponse[1]
            if fwDwnldStatus == "Failed":
                tdkTestObj.setResultStatus("SUCCESS");
                print "[TEST EXECUTION RESULT] : SUCCESS"
                print "Got Default FirmwareDownloadStatus as Failed"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "[TEST EXECUTION RESULT] : FAILURE"
                print "Got Default FirmwareDownloadStatus as ", fwDwnldStatus
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"

    obj.unloadModule("sysutil");

else:
    print "FAILURE to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
