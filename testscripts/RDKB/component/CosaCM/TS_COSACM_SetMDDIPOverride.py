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
  <version>12</version>
  <name>TS_COSACM_SetMDDIPOverride</name>
  <primitive_test_id/>
  <primitive_test_name>COSACM_SetMDDIPOverride</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_COSACM_35</test_case_id>
    <test_objective>To Validate Cable Modem 
"CosaDmlCMSetMDDIPOverride" API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,
XB3</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script


</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
COSACM_SetMDDIPOverride
Input
N/A



</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(COSACM_SetMDDIPOverride - func name - "If not exists already" ( This is considered as default Primitive test case)
 cosacm - module name
 Necessary I/P args if needed as Mentioned in Input)
2.Create a Python Script in Test Manager with default primitive test case through add new rdkb script option (TS_COSACM_SetMDDIPOverride.py)
3.Customize the generated script template to handle load/unload and pass/fail scenarios
3.Execute the generated Script(TS_COSACM_SetMDDIPOverride.py) using execution page of  Test Manager GUI
4.cosacmstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named COSACM_SetMDDIPOverride through registered TDK cosacmstub function along with necessary Entry Values as arguments
5.COSACM_SetMDDIPOverride function will call ssp_cosacm_set_mddipoverride,that inturn will call relevant cm hal Function to update CM data model value. In prior ssp_cosacm_create and ssp_coscm_initialize functions are called in sequence to allocate memory for CM datamodel and initialize with default values
6.Responses(printf) from TDK Component,Ccsp Library function and cosacmstub would be logged in Agent Console log based on the debug info redirected to agent console   
7.cosacmstub function COSACM_SetMDDIPOverride will validate the available result (return value from ssp_cosacm_set_mddipoverride as success(0)) with expected result (success(0)) and the output argument value is updated in agent console log and json output variable along with return value
8.TestManager will publish the result in GUI as PASS/FAILURE based on the response from COSACM_SetMDDIPOverride function</automation_approch>
    <except_output>CheckPoint 1:
Cosa CM Set MDD Override success log from DUT should be available in Agent Console Log
CheckPoint 2:
TDK agent Test Function will log the test case result as PASS based on API response which will be available in Test Manager Result ( XLS)
CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_COSACM_SetMDDIPOverride</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
																																																
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cosacm","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_COSACM_SetMDDIPOverride');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("CosaCM_SetMDDIPOverride");
        tdkTestObj.addParameter("value","IPV4");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            details = tdkTestObj.getResultDetails();
            print "TEST STEP 1: Set the MDDIP Override value to IPv4";
            print "EXPECTED RESULT 1: Should successfully set the value to IPv4";
            print "ACTUAL RESULT 1: %s" %details;
            #Script to load the configuration file of the component
            tdkTestObj = obj.createTestStep("COSACM_GetMDDIPOverride");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 2: Retrieve the MDD IP Override Status";
                print "EXPECTED RESULT 2: Should retrieve the MDD IP Override Status successfully";
                print "ACTUAL RESULT 2: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                tdkTestObj = obj.createTestStep("CosaCM_SetMDDIPOverride");
                tdkTestObj.addParameter("value","IPV6");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    details = tdkTestObj.getResultDetails();
                    print "TEST STEP 3: Set the MDDIP Override value to IPv6";
                    print "EXPECTED RESULT 3: Should successfully set the value to IPv6";
                    print "ACTUAL RESULT 3: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    tdkTestObj = obj.createTestStep("COSACM_GetMDDIPOverride");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        details = tdkTestObj.getResultDetails();
                        print "TEST STEP 4: Retrieve the MDD IP Override Status";
                        print "EXPECTED RESULT 4: Should retrieve the MDD IP Override Status successfully";
                        print "ACTUAL RESULT 4: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                        tdkTestObj = obj.createTestStep("CosaCM_SetMDDIPOverride");
                        tdkTestObj.addParameter("value","HONOR");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            details = tdkTestObj.getResultDetails();
                            print "TEST STEP 5: Set the MDDIP Override value to Honor";
                            print "EXPECTED RESULT 5: Should successfully set the value to Honor";
                            print "ACTUAL RESULT 5: %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                            tdkTestObj = obj.createTestStep("COSACM_GetMDDIPOverride");
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                details = tdkTestObj.getResultDetails();
                                print "TEST STEP 6: Retrieve the MDD IP Override Status";
                                print "EXPECTED RESULT 6: Should retrieve the MDD IP Override Status successfully";
                                print "ACTUAL RESULT 6: %s" %details;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : %s" %actualresult ; 
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                details = tdkTestObj.getResultDetails();
                                print "TEST STEP 6: Retrieve the MDD IP Override Status";
                                print "EXPECTED RESULT 6: Should retrieve the MDD IP Override Status successfully";
                                print "ACTUAL RESULT 6: %s" %details;
                                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            details = tdkTestObj.getResultDetails();
                            print "TEST STEP 5: Set the MDDIP Override value to Honor";
                            print "EXPECTED RESULT 5: Should successfully set the value to Honor";
                            print "ACTUAL RESULT 5: %s" %details;
                            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        details = tdkTestObj.getResultDetails();
                        print "TEST STEP 4: Retrieve the MDD IP Override Status";
                        print "EXPECTED RESULT 4: Should retrieve the MDD IP Override Status successfully";
                        print "ACTUAL RESULT 4: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    details = tdkTestObj.getResultDetails();
                    print "TEST STEP 3: Set the MDDIP Override value to IPv6";
                    print "EXPECTED RESULT 3: Should successfully set the value to IPv6";
                    print "ACTUAL RESULT 3: %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    tdkTestObj = obj.createTestStep("CosaCM_SetMDDIPOverride");
                    tdkTestObj.addParameter("value","HONOR");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
            else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 2: Retrieve the MDD IP Override Status";
                print "EXPECTED RESULT 2: Should retrieve the MDD IP Override Status successfully";
                print "ACTUAL RESULT 2: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            details = tdkTestObj.getResultDetails();
            print "TEST STEP 1: Set the MDDIP Override value to IPv4";
            print "EXPECTED RESULT 1: Should successfully set the value to IPv4";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            tdkTestObj = obj.createTestStep("CosaCM_SetMDDIPOverride");
            tdkTestObj.addParameter("value","HONOR");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);

        obj.unloadModule("cosacm");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";	
