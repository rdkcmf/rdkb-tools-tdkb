##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>12</version>
  <name>TS_RBUS_SetValidLogLevels</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_SetLogLevel</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the RBUS API rbus_setLogLevel and check if setting of all valid log levels : [0,1,2,3,4] is success.</synopsis>
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
    <test_case_id>TC_RBUS_55</test_case_id>
    <test_objective>Invoke the RBUS API rbus_setLogLevel and check if setting of all valid log levels : [0,1,2,3,4] is success.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_setLogLevel</api_or_interface_used>
    <input_parameters>level : 0,1,2,3,4</input_parameters>
    <automation_approch>1. Load the rbus module
2. With the device in rbus mode invoke rbus_setLogLevel() with valid levels such as RBUS_LOG_DEBUG = 0, RBUS_LOG_INFO = 1, RBUS_LOG_WARN  = 2, RBUS_LOG_ERROR = 3, RBUS_LOG_FATAL = 4. The API should return success for all the valid levels.
3. Unload the module
</automation_approch>
    <expected_output>rbus_setLogLevel() API should return success for all valid log levels : [0,1,2,3,4] </expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_SetValidLogLevels</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RBUS_SetValidLogLevels');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    #Valid log level in range 0 to 4
    print "\n Valid Log Levels are : RBUS_LOG_DEBUG = 0, RBUS_LOG_INFO = 1, RBUS_LOG_WARN  = 2, RBUS_LOG_ERROR = 3, RBUS_LOG_FATAL = 4";
    for level in range(0,5) :
        print "\nSetting to Level : %d" %level;
        tdkTestObj = obj.createTestStep('RBUS_SetLogLevel');
        tdkTestObj.addParameter("level", level);
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "\nTEST STEP 1: rbus_setLogLevel should be invoked successfully with log level value = %d" %level;
            print "EXPECTED RESULT 1: rbus_setLogLevel should be success";
            print "ACTUAL RESULT 1: rbus_setLogLevel was success; Details %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "\nTEST STEP 1: rbus_setLogLevel should be invoked successfully with log level value = %d" %level;
            print "EXPECTED RESULT 1: rbus_setLogLevel should be success";
            print "ACTUAL RESULT 1: rbus_setLogLevel was Failed; Details %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

