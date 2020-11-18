##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_RegisterMethodWithSameName</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_RegisterOperation</primitive_test_name>
  <!--  -->
  <primitive_test_version>4</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the RBUS APIs rbus_registerMethod and rbus_unregisterMethod by registering and unregistering with duplicate names</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_RBUS_38</test_case_id>
    <test_objective>To validate the RBUS APIs rbus_registerMethod and rbus_unregisterMethod by registering and unregistering with duplicate names</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_registerMethod
rbus_unregisterMethod</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the rbus module
2. open the rbus broker connection using rbus_openBrokerConnection API
3. The rbus_openBrokerConnection should be success
4. Register Method with RBUS using rbus_regsisterMethod API and the return status should be success
5. Try to Register the Method with same name again using rbus_regsisterMethod API and return status should be failure
6. UnRegister the first Method using rbus_unregisterMethod API and the return status should be success
7. Try to UnRegister the same method again using rbus_unregisterMethod APU and return status should be failure
8. Try to unregister the method which is not registered with the object, and return status should be failure
9. Close the rbus broker connection using rbus_closeBrokerConnection API
10.The rbus_closeBrokerConnection should be success
11.Unload the rbus module</automation_approch>
    <expected_output>Registering or Unregistering Methods with duplicate name should be failed</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_RegisterMethodWithSameName</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbRBUS_Utility import *;
from tdkutility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_RBUS_RegisterMethodWithSameName');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[RBUS LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    print "*************Start of Broker Connection*******************************";
    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
    tdkTestObj.addParameter("operation","openBrokerConnection");
    tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
    tdkTestObj.addParameter("methodName","CloseConnectionBeforeOpen");#Close connection if any Before opening the new connection
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "RBUS openBrokerConnection Detail is ",details

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS Broker connection";
        print "EXPECTED RESULT 1: rbus_openBrokerConnection Should be success";
        print "ACTUAL RESULT 1: rbus_openBrokerConnection was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "*************Start of Registering Object*****************************"
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","registerObj");
        tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
        tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS register Obj Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Register the object with RBUS ";
            print "EXPECTED RESULT 2: rbus_registerObj should be success";
            print "ACTUAL RESULT 2: rbus_registerObj was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "*************Start of Registering Method*****************************"

            print "Registering the first method (Method1) - Positive Scenario"
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","registerMethod");
            tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
            tdkTestObj.addParameter("methodName","Method1");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS register Method Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Register the Method with RBUS ";
                print "EXPECTED RESULT 3: rbus_registerMethod should be success";
                print "ACTUAL RESULT 3: rbus_registerMethod was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "Registering the method with same name (Method1) - Negative Scenario";
                tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                tdkTestObj.addParameter("operation","registerMethod");
                tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
                tdkTestObj.addParameter("methodName","Method1");
                expectedresult="FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "Duplicate RBUS register Method Detail is ",details

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Register the Method with Same Name";
                    print "EXPECTED RESULT 3: rbus_registerMethod should Fail for Duplicate Entry";
                    print "ACTUAL RESULT 3: rbus_registerMethod was Failed for Duplicate Entry";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS" ;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Register the Method with Same Name";
                    print "EXPECTED RESULT 3: rbus_registerMethod should Fail for Duplicate Entry";
                    print "ACTUAL RESULT 3: rbus_registerMethod was NOT Failed for Duplicate Entry";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE" ;

                print "UnRegister the first method (Method1) - Positive Scenario";
                tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                tdkTestObj.addParameter("operation","unregisterMethod");
                tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
                tdkTestObj.addParameter("methodName","Method1");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "RBUS unregister Method Detail is ",details

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: UnRegister the Method with RBUS ";
                    print "EXPECTED RESULT 4: rbus_unregisterMethod should be success";
                    print "ACTUAL RESULT 4: rbus_unregisterMethod was success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                    print "UnRegister the method for second time - Negative Scenario";
                    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                    tdkTestObj.addParameter("operation","unregisterMethod");
                    tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
                    tdkTestObj.addParameter("methodName","Method1");
                    expectedresult="FAILURE";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    print "Duplicate RBUS unregister Method Detail is ",details

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: UnRegister the Method with RBUS for second time ";
                        print "EXPECTED RESULT 5: rbus_unregisterMethod should Fail for second time unregister operation";
                        print "ACTUAL RESULT 5: rbus_unregisterMethod was Failed for second time unregister operation";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: UnRegister the Method with RBUS for second time ";
                        print "EXPECTED RESULT 5: rbus_unregisterMethod should Fail for second time unregister operation";
                        print "ACTUAL RESULT 5: rbus_unregisterMethod was NOT Failed for second time unregister operation";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    print "UnRegister the method which is not registered - Negative Scenario"
                    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                    tdkTestObj.addParameter("operation","unregisterMethod");
                    tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
                    tdkTestObj.addParameter("methodName","Method3"); # Method3 is not registered
                    expectedresult="FAILURE";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    print "Duplicate RBUS unregister Method Detail is ",details

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 6: UnRegister the Method which is not registered before ";
                        print "EXPECTED RESULT 6: rbus_unregisterMethod should Fail for method which is not registered before";
                        print "ACTUAL RESULT 6: rbus_unregisterMethod was Failed for method which is not registered before";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: UnRegister the Method which is not registered before ";
                        print "EXPECTED RESULT 6: rbus_unregisterMethod should Fail for method which is not registered before";
                        print "ACTUAL RESULT 6: rbus_unregisterMethod was NOT Failed for method which is not registered before";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: UnRegister the Method with RBUS ";
                    print "EXPECTED RESULT 4: rbus_unregisterMethod should be success";
                    print "ACTUAL RESULT 4: rbus_unregisterMethod was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Register the Method with RBUS ";
                print "EXPECTED RESULT 3: rbus_registerMethod should be success";
                print "ACTUAL RESULT 3: rbus_registerMethod was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "*************End of Registering Method*******************************"

            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","unregisterObj");
            tdkTestObj.addParameter("objectName","tdkb_server1.obj1");
            tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS unregister Obj Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 7: UnRegister the object with RBUS ";
                print "EXPECTED RESULT 7: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 7: rbus_unregisterObj was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 7: UnRegister the object with RBUS ";
                print "EXPECTED RESULT 7: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 7: rbus_unregisterObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 5: Register the object with RBUS ";
            print "EXPECTED RESULT 5: rbus_registerObj should be success";
            print "ACTUAL RESULT 5: rbus_registerObj was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "*************End of Registering Object*******************************"
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","closeBrokerConnection");
        tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
        tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS closeBrokerConnection Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 8: Close the RBUS Broker connection";
            print "EXPECTED RESULT 8: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 8: rbus_closeBrokerConnection was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 8: Close the RBUS Broker connection";
            print "EXPECTED RESULT 8: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 8: rbus_closeBrokerConnection was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Open the RBUS Broker connection";
        print "EXPECTED RESULT 1: rbus_openBrokerConnection Should be success";
        print "ACTUAL RESULT 1: rbus_openBrokerConnection was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    print "*************End of Broker Connection*******************************"
    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
