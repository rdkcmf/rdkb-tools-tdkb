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
  <name>TS_RBUS_RegisterObjectsBeyondLimit</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_RegisterOperation</primitive_test_name>
  <!--  -->
  <primitive_test_version>4</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the RBUS API rbus_registerObj by registering Objects beyond the limit (63)</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_RBUS_41</test_case_id>
    <test_objective>To validate the RBUS API rbus_registerObj by registering Objects beyond the limit (63)</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode
</pre_requisite>
    <api_or_interface_used>rbus_registerObj
rbus_unregisterObj</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the rbus module
2. open the rbus broker connection using rbus_openBrokerConnection API with component name as "tdk_b"
3. The rbus_openBrokerConnection should be success
4. Register multiple objects (63 objects) in RBUS using rbus_registerObj API and the return status should be success
5. Try to Register the 64th object using rbus_registerObj and the return status should be failure since its beyond the limit
6. Unregister one Object from RBUS and the return status should be success
7. Now try to register the same Method again and return status should be success
8. UnRegister all registered objects using rbus_unregisterObj API and the return status should be success
9. Close the rbus broker connection using rbus_closeBrokerConnection API
10.The rbus_closeBrokerConnection should be success
11.Unload the rbus module</automation_approch>
    <expected_output>Registering Objects should be allowed only within the accepted limit</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_RegisterObjectsBeyondLimit</test_script>
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

obj.configureTestCase(ip,port,'TS_RBUS_RegisterObjectsBeyondLimit');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[RBUS LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    print "\n*************** Start of Broker Connection ********************************************"
    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
    tdkTestObj.addParameter("operation","openBrokerConnection");
    tdkTestObj.addParameter("objectName","tdkb_object"); #This Will be converted to Component name in Wrapper code
    tdkTestObj.addParameter("methodName","CloseConnectionBeforeOpen");#Close the connection before open if any

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

        print "\n*************** Start of Registering  Objects ********************************************"

        max_object = 63;
        object_name = "";
        counter = 0;

        for object in range (0,max_object):
            object_name = "tdkb_object.obj"+str(object);

            print "Registering Object with object name ",object_name
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","registerObj");
            tdkTestObj.addParameter("objectName",object_name);
            tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value

            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS register Obj Detail is ",details

            if expectedresult in actualresult:
                counter = counter + 1;
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Register the object with RBUS ";
                print "EXPECTED RESULT 2: rbus_registerObj should be success";
                print "ACTUAL RESULT 2: rbus_registerObj was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Register the object with RBUS ";
                print "EXPECTED RESULT 2: rbus_registerObj should be success";
                print "ACTUAL RESULT 2: rbus_registerObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                break;  #Break the Loop if registering is failed
        print "*************** End of Registering  Objects ************************************************\n"

        print "\nRegistering Object Beyond the limit (More than  Objects)"
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","registerObj");
        tdkTestObj.addParameter("objectName","tdkb_object.obj64");
        tdkTestObj.addParameter("methodName","dummy");#Dummy Value
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS register Obj Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Register the object beyond the limits";
            print "EXPECTED RESULT 3: rbus_registerObj should should fail if 63 objects already registered";
            print "ACTUAL RESULT 3: rbus_registerObj was Failed as expected";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Register the object beyond the limits";
            print "EXPECTED RESULT 3: rbus_registerObj should should fail if 63 objects already registered";
            print "ACTUAL RESULT 3: rbus_registerObj was NOT Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE" ;

        print "\nUnRegister one Object(tdkb_object.obj0) to free up the object queue"
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","unregisterObj");
        tdkTestObj.addParameter("objectName","tdkb_object.obj0");
        tdkTestObj.addParameter("methodName","dummy");#Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS register Obj Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 4: Unregister the first object";
            print "EXPECTED RESULT 4: rbus_registerObj should success";
            print "ACTUAL RESULT 4: rbus_registerObj was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            print "\nRegsiter the object (tdkb_object.obj0) again after unregistering from RBUS"
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","registerObj");
            tdkTestObj.addParameter("objectName","tdkb_object.obj0");
            tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS unregister Obj Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: Register the object with RBUS again ";
                print "EXPECTED RESULT 5: rbus_registerObj should be success";
                print "ACTUAL RESULT 5: rbus_registerObj was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 5: Register the object with RBUS again";
                print "EXPECTED RESULT 5: rbus_registerObj should be success";
                print "ACTUAL RESULT 5: rbus_registerObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Unregister the first object";
            print "EXPECTED RESULT 4: rbus_registerObj should success";
            print "ACTUAL RESULT 4: rbus_registerObj was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE" ;

        print "\n*************** Start of UnRegistering 62 Objects ********************************************"
        object_name = "";
        for object in range (0,counter):
            object_name = "tdkb_object.obj"+str(object);
            print "UnRegistering Object with object name ",object_name

            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","unregisterObj");
            tdkTestObj.addParameter("objectName",object_name);
            tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS unregister Obj Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 6: UnRegister the object with RBUS ";
                print "EXPECTED RESULT 6: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 6: rbus_unregisterObj was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 6: UnRegister the object with RBUS ";
                print "EXPECTED RESULT 6: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 6: rbus_unregisterObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                break;

        print "*************** End of UnRegistering 62 Object ********************************************\n"

        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","closeBrokerConnection");
        tdkTestObj.addParameter("objectName","tdkb_object"); #This Will be converted to Component name in Wrapper code
        tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS closeBrokerConnection Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 7: Close the RBUS Broker connection";
            print "EXPECTED RESULT 7: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 7: rbus_closeBrokerConnection was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 7: Close the RBUS Broker connection";
            print "EXPECTED RESULT 7: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 7: rbus_closeBrokerConnection was Failed";
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

    print "*************** End of Broker Connection ********************************************\n"
    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
