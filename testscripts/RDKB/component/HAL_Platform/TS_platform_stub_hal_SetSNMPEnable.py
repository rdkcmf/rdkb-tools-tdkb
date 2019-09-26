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
  <name>TS_platform_stub_hal_SetSNMPEnable</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_SetSNMPEnable</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Validate HAL API platform_hal_SetSNMPEnable()</synopsis>
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
    <test_case_id>TC_HAL_Platform_24</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_SetSNMPEnable()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetSNMPEnable() platform_hal_GetSNMPEnable()</api_or_interface_used>
    <input_parameters>index - flag to be set</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_stub_hal_SetSNMPEnable().
3. Set the value
4. Invoke  platform_stub_hal_GetSNMPEnable()
5. Get the value
6. Validate the value if it gets set properly
7. Validation of  the result is done within the python script and send the result status to Test Manager.
8. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <except_output>Value should be set properly</except_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Platform</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetSNMPEnable</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#Library funtions
import tdklib;
import time;

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetSNMPEnable');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        tdkTestObj = obj.createTestStep("platform_stub_hal_GetSNMPEnable");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details and (details == "started" or details == "stopped"):
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the Platform_GetSNMPEnable";
            print "EXPECTED RESULT 1: Should retrieve the Platform_GetSNMPEnable successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
            print "details of snmp is %s" %details;

            if details == "started":
	        currentSnmp = 1;
                #Disable SNMP using SET API
                Enable_snmp = 0;
            else:
                #Enable SNMP using SET API
	        currentSnmp = 0;
                Enable_snmp = 1;

            tdkTestObj = obj.createTestStep("platform_stub_hal_SetSNMPEnable");
            tdkTestObj.addParameter("index", Enable_snmp);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 2: Retrieve the Platform_SetSNMPEnable";
                print "EXPECTED RESULT 2: Should retrieve the Platform_SetSNMPEnable successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                time.sleep(20);
                tdkTestObj = obj.createTestStep("platform_stub_hal_GetSNMPEnable");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details and (details == "started" or details == "stopped"):
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Retrieve the Platform_GetSNMPEnable";
                    print "EXPECTED RESULT 3: Should retrieve the Platform_GetSNMPEnable successfully";
                    print "ACTUAL RESULT 3: %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    if details == "started":
                        snmpAfterSet = 1;
                    else:
                        snmpAfterSet = 0;
                    print "Enable_snmp = %s, snmpAfterSet = %s" %(Enable_snmp, snmpAfterSet);
                    if Enable_snmp == snmpAfterSet:
                        print "TEST STEP 4: Check whether SNMP Enable value is same as expected";
                        print "EXPECTED RESULT 4: Should retrieve the Platform_GetSNMPEnable successfully";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";         
                        print "SNMP Enable value is %s" %details;

                        time.sleep(90);
                        tdkTestObj = obj.createTestStep("platform_stub_hal_SetSNMPEnable");
                        tdkTestObj.addParameter("index", currentSnmp);
                        expectedresult = "SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            details = tdkTestObj.getResultDetails();
                            print "TEST STEP 5: Retrieve the Platform_SetSNMPEnable";
                            print "EXPECTED RESULT 5: Should retrieve the Platform_SetSNMPEnable successfully";
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                            print "Get Value Re-Setted successfully"; 
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Retrieve the Platform_SetSNMPEnable";
                            print "EXPECTED RESULT 5: Should retrieve the Platform_SetSNMPEnable successfully";
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                            print "Resetting SNMP to original got failed"; 
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4:  Check SNMP Enable value is same as expected";
                        print "EXPECTED RESULT 4: Should retrieve the Platform_GetSNMPEnable successfully";
                        print "ACTUAL RESULT 4: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "Set and Get value are Same";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    details = tdkTestObj.getResultDetails();
                    print "TEST STEP 3: Retrieve the Platform_GetSNMPEnable";
                    print "EXPECTED RESULT 3: Should retrieve the Platform_GetSNMPEnable successfully";
                    print "ACTUAL RESULT 3: %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
            else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 2: Retrieve the Platform_SetSNMPEnable";
                print "EXPECTED RESULT 2: Should retrieve the Platform_SetSNMPEnable successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Retrieve the Platform_GetSNMPEnable";
            print "EXPECTED RESULT 1: Should retrieve the Platform_GetSNMPEnable successfully";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult;
        obj.unloadModule("halplatform");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
