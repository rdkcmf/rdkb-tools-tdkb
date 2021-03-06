#  ===========================================================================
#  Copyright 2016-2018 Intel Corporation

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#  ===========================================================================

'''
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>8</version>
  <name>TS_platform_stub_hal_SetTelnetEnable</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_SetTelnetEnable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Validate HAL API platform_hal_SetTelnetEnable()</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks></remarks>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_HAL_Platform_22</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_SetTelnetEnable()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetTelnetEnable() platform_hal_GetTelnetEnable()</api_or_interface_used>
    <input_parameters>index - flag to be set</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_stub_hal_SetTelnetEnable().
3. Set the value
4. Invoke  platform_stub_hal_GetTelnetEnable()
5. Get the value
6. Validate the value if it gets set properly
7. Validation of  the result is done within the python script and send the result status to Test Manager.
8. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <except_output>Value should be set properly</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetTelnetEnable</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#Library functions
import tdklib;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetTelnetEnable');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetTelnetEnable");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the Platform_GetTelnetEnable";
            print "EXPECTED RESULT 1: Should retrieve the Platform_GetTelnetEnable successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
 
            if details == "1":
                Enable_telnet = 0;
                Enable_reset = 1;
            else:
                Enable_telnet = 1;
                Enable_reset = 0;

            print "Present Telnet value is : %d, and Telnet value to be set is %d" %(Enable_reset, Enable_telnet);
            tdkTestObj = obj.createTestStep("platform_stub_hal_SetTelnetEnable");
            tdkTestObj.addParameter("index",Enable_telnet);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 2: Retrieve the Platform_SetTelnetEnable";
                print "EXPECTED RESULT 2: Should retrieve the Platform_SetTelnetEnable successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
 
                tdkTestObj = obj.createTestStep("platform_stub_hal_GetTelnetEnable");
                expectedresult = "SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Retrieve the Platform_GetTelnetEnable";
                    print "EXPECTED RESULT 3: Should retrieve the Platform_GetTelnetEnable successfully";
                    print "ACTUAL RESULT 3: %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    valueAfterSet = details;
                    if int(valueAfterSet) == Enable_telnet:
                        print "TEST STEP 4: Retrieve the Platform_SetTelnetEnable";
                        print "EXPECTED RESULT 4: Retrieved value should be same as expected SET value";
                        print "ACTUAL RESULT 4: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;

                        tdkTestObj = obj.createTestStep("platform_stub_hal_SetTelnetEnable");
                        tdkTestObj.addParameter("index", int(Enable_reset));
                        expectedresult = "SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            details = tdkTestObj.getResultDetails();
                            print "TEST STEP 5: Retrieve the Platform_SetTelnetEnable";
                            print "EXPECTED RESULT 5: Should retrieve the Platform_SetTelnetEnable successfully";
                            print "ACTUAL RESULT 5: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                            print "Get value is successfully Re-Setted";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Retrieve the Platform_SetTelnetEnable";
                            print "EXPECTED RESULT 5: Should retrieve the Platform_SetTelnetEnable successfully";
                            print "ACTUAL RESULT 5: %s" %details;
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                            print "Resetting Telnet value failed";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Retrieve the Platform_SetTelnetEnable";
                        print "EXPECTED RESULT 4: Retrieved value should be same as expected SET value";
                        print "ACTUAL RESULT 4: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    details = tdkTestObj.getResultDetails();
                    print "TEST STEP 3: Retrieve the Platform_GetTelnetEnable";
                    print "EXPECTED RESULT 3: Should retrieve the Platform_GetTelnetEnable successfully";
                    print "ACTUAL RESULT 3: %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 2: Retrieve the Platform_SetTelnetEnable";
                print "EXPECTED RESULT 2: Should retrieve the Platform_SetTelnetEnable successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Retrieve the Platform_GetTelnetEnable";
            print "EXPECTED RESULT 1: Should retrieve the Platform_GetTelnetEnable successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
        obj.unloadModule("halplatform");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
