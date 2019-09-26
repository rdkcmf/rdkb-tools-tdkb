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
  <name>TS_TR069PA_SetManagementServerURL</name>
  <primitive_test_id/>
  <primitive_test_name>TR069Agent_SetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the SetManagementServer.URL value in gateway via ACS server</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_TR069_9</test_case_id>
    <test_objective>Set the SetManagementServer.URL value in gateway via ACS server</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.TR069 process should be up and running in the gateway
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>send_xml()</api_or_interface_used>
    <input_parameters>Device.ManagementServer.EnableCWMP</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Get and save the value of Device.ManagementServer.URL using ACS server
3. Set a new url value to Device.ManagementServer.URL using ACS server
4. Check if the status of set operation was 200 or not
5. Revert the value of Device.ManagementServer.URL
6. Unload tdkbtr181 module
</automation_approch>
    <except_output>Set operation on Device.ManagementServer.URL using ACS server should be success</except_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_TR069PA_SetManagementServerURL</test_script>
    <skipped>No</skipped>
    <release_version>M60</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
from tr69SoapUtil import *
from tr69Config import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TR069PA_SetManagementServerURL');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
    tdkTestObj.executeTestCase("SUCCESS")

    #get and save the current ManagementServer URL
    print "TEST STEP 1: get the current ManagementServer URI"
    parsedResponse = send_xml(SERVERURI_GET_XML, "get")
    if 200 in parsedResponse:
        tdkTestObj.setResultStatus("SUCCESS");
        print "[TEST EXECUTION RESULT] : SUCCESS"

        orgUri = parsedResponse[1];
        print "original firewall level: ",orgUri

        print "TEST STEP 2: set the current ManagementServer URI"
        parsedResponse = send_xml(SERVERURI_SET_XML, "set")
        if 200 in parsedResponse:
            tdkTestObj.setResultStatus("SUCCESS");
            print "[TEST EXECUTION RESULT] : SUCCESS"

            print "TEST STEP 3: revert the current ManagementServer URI"
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.ManagementServer.URL");
            tdkTestObj.addParameter("ParamValue",orgUri);
            tdkTestObj.addParameter("Type","string");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");

                print "TEST STEP 3: Revert the current ManagementServer URI"
                print "EXPECTED RESULT : Should revert the current ManagementServer URI"
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Revert the current ManagementServer URI"
                print "EXPECTED RESULT : Should revert the ManagementServer URI"
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "[TEST EXECUTION RESULT] : FAILURE"

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

