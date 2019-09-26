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
  <name>TS_TR069PA_Disable_CWMP_ConnectToACS</name>
  <primitive_test_id/>
  <primitive_test_name>TR069Agent_SetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check connectivity of CPE and ACS after disabling CWMP</synopsis>
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
    <test_case_id>TC_TR069_8</test_case_id>
    <test_objective>Check connectivity of CPE and ACS after disabling CWMP</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.TR069 process should be up and running in the gateway
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>send_xml()</api_or_interface_used>
    <input_parameters>Device.ManagementServer.EnableCWMP</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Get and save the value of Device.ManagementServer.EnableCWMP
3. Set the value of Device.ManagementServer.EnableCWMP as false
4. Try to do a get operation in gateway using the TR069 ACS server
5. Check if connection between ACS server and gateway is failure or not
6. Revert the value of Device.ManagementServer.EnableCWMP
7. unload tdkbtr181 module</automation_approch>
    <except_output>Connection attempt between ACS server and gateway should fail when Device.ManagementServer.EnableCWMP is false</except_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_TR069PA_Disable_CWMP_ConnectToACS</test_script>
    <skipped>No</skipped>
    <release_version>M60</release_version>
    <remarks>None</remarks>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_TR069PA_Enable_CWMP_ConnectToACS');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.ManagementServer.EnableCWMP");

    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);

    actualresult = tdkTestObj.getResult();
    orgStatus = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");

        print "TEST STEP 1: Get the current EnableCWMP status";
        print "EXPECTED RESULT : Should get the current EnableCWMP status"
        print "ACTUAL RESULT :%s" %orgStatus
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');

        tdkTestObj.addParameter("ParamName","Device.ManagementServer.EnableCWMP");
        tdkTestObj.addParameter("ParamValue","false");
        tdkTestObj.addParameter("Type","boolean");

        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);

        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");

            print "TEST STEP 2: Set the current EnableCWMP status as enabled";
            print "EXPECTED RESULT : Should set the current EnableCWMP status"
            print "ACTUAL RESULT :%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Try to connect to ACS server and do a get operation
            print "TEST STEP 3: check the ACS connectivity after enabling EnableCWMP"
            parsedResponse = send_xml(Enable_CWMP_XML, "get")

            if 200 not in parsedResponse:
                tdkTestObj.setResultStatus("SUCCESS");
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "[TEST EXECUTION RESULT] : FAILURE"

            #Revert EnableCWMP status
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.ManagementServer.EnableCWMP");
            tdkTestObj.addParameter("ParamValue",orgStatus);
            tdkTestObj.addParameter("Type","boolean");

            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);

            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");

                print "TEST STEP 3: Revert the current EnableCWMP status as the original value"
                print "EXPECTED RESULT : Should revert the current EnableCWMP status"
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Revert the current EnableCWMP status as the original value"
                print "EXPECTED RESULT : Should revert the current EnableCWMP status"
                print "ACTUAL RESULT :%s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the current EnableCWMP status as enabled";
            print "EXPECTED RESULT : Should set the current EnableCWMP status"
            print "ACTUAL RESULT :%s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current EnableCWMP status";
        print "EXPECTED RESULT : Should get the current EnableCWMP status"
        print "ACTUAL RESULT :%s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");

else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

