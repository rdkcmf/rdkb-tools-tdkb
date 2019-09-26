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
  <name>TS_platform_stub_hal_SetWebUITimeout</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_SetWebUITimeout</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Validate HAL API platform_hal_SetWebUITimeout()</synopsis>
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
    <test_case_id>TC_HAL_Platform_21</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_SetWebUITimeout()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetWebUITimeout() platform_hal_GetWebUITimeout()</api_or_interface_used>
    <input_parameters>index - flag to be set</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_stub_hal_SetWebUITimeout().
3. Set the value
4. Invoke  platform_stub_hal_GetWebUITimeout
5. Get the value
6. Validate the value if it gets set properly
7. Validation of  the result is done within the python script and send the result status to Test Manager.
8. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <except_output>Value should be set properly</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetWebUITimeout</test_script>
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
testTimeout = 50
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetWebUITimeout');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetWebUITimeout");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        actualValue = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and int (actualValue) >= 0:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get timeout value from Platform_GetWebUITimeout";
            print "EXPECTED RESULT 1: Should get the value from Platform_GetWebUITimeout successfully";
            print "ACTUAL RESULT 1: %s" %actualValue;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;

            #Verify SET operation
            tdkTestObj = obj.createTestStep("platform_stub_hal_SetWebUITimeout");
            tdkTestObj.addParameter("index",testTimeout);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set timeout value from Platform_SetWebUITimeout";
                print "EXPECTED RESULT 2: Should set the value from Platform_SetWebUITimeout successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;

                #get timeout value after SET operation to cross verify
                tdkTestObj = obj.createTestStep("platform_stub_hal_GetWebUITimeout");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                valueAfterSet = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and int (valueAfterSet) >= 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get timeout value from Platform_GetWebUITimeout";
                    print "EXPECTED RESULT 3: Should get the value from Platform_GetWebUITimeout successfully";
                    print "ACTUAL RESULT 3: value = %s" %valueAfterSet;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;

                    if int (valueAfterSet) == testTimeout:
                        print "TEST STEP 4: Cross verifing the value";
                        print "EXPECTED RESULT 4: Timeout value should match";    
                        print "ACTUAL RESULT 4: Value is set successfully";
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;

                        #Reverting timeout value 
                        tdkTestObj = obj.createTestStep("platform_stub_hal_SetWebUITimeout");
                        tdkTestObj.addParameter("index", int(actualValue));
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 5: Set timeout value from Platform_SetWebUITimeout";
                            print "EXPECTED RESULT 5: Should set the value from Platform_SetWebUITimeout successfully";
                            print "ACTUAL RESULT 5: %s" %details;
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Set timeout value from Platform_SetWebUITimeout";
                            print "EXPECTED RESULT 5: Should set the value from Platform_SetWebUITimeout successfully";
                            print "ACTUAL RESULT 5: %s" %details;
                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Cross verifing the value";
                        print "EXPECTED RESULT 4: Timeout value should match";    
                        print "ACTUAL RESULT 4: Value is not set successfully";
                        print "[TEST EXECUTION RESULT] : FAILURE"; 
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get timeout value from Platform_GetWebUITimeout";
                    print "EXPECTED RESULT 3: Should get the value from Platform_GetWebUITimeout successfully";
                    print "ACTUAL RESULT 3: %s" %valueAfterSet;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set timeout value from Platform_SetWebUITimeout";
                print "EXPECTED RESULT 2: Should set the value from Platform_SetWebUITimeout successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get timeout value from Platform_GetWebUITimeout";
            print "EXPECTED RESULT 1: Should get the value from Platform_GetWebUITimeout successfully";
            print "ACTUAL RESULT 1: %s" %actualValue;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;

        obj.unloadModule("halplatform");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
