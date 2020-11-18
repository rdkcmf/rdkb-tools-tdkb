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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>11</version>
  <name>TS_RBUS_AddElementAfterObjectUnregister</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_RegisterOperation</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the RBUS API rbus_addElement by adding the element with unregistered object</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_RBUS_46</test_case_id>
    <test_objective>To validate the RBUS API rbus_addElement by adding the element with unregistered object</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_addElement
rbus_unregisterObj</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the rbus module
2. Open the rbus broker connection using rbus_openBrokerConnection API
3. The rbus_openBrokerConnection should be success
4. Register the object in the RBUS using rbus_registerObj API ,return status should be success
5. Add the element in the object using rbus_addElement API, return status should be success
6. Remove the element in the object using rbus_removeElement API, return status should be success
7. Unregister the object in the RBUS using rbus_unregisterObj API, return status should be success
8. Try to add the element in the unregistered object, the return status should be failure since the object is unregistered
9. Close the rbus broker connection using rbus_closeBrokerConnection API
10. The rbus_closeBrokerConnection should be success
11.Unload the rbus module</automation_approch>
    <expected_output>Adding Element in the unregistered object should fail</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_AddElementAfterObjectUnregister</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
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
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_RBUS_AddElementAfterObjectUnregister');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[RBUS LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    print "\n*************Start of Broker Connection*******************************";
    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
    tdkTestObj.addParameter("operation","openBrokerConnection");
    tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
    tdkTestObj.addParameter("methodName","CloseConnectionBeforeOpen");#Close the connection before open if any
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "RBUS openBrokerConnection Detail is ",details

    obj_name = "test_Server_TDK"
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS Broker connection ";
        print "EXPECTED RESULT 1: rbus_openBrokerConnection Should be success";
        print "ACTUAL RESULT 1: rbus_openBrokerConnection was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "\n*************Start of Registering Object *******************************";
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","registerObj");
        tdkTestObj.addParameter("objectName",obj_name);
        tdkTestObj.addParameter("methodName","dummy");   #Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS register Obj Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Register the object with RBUS, Object Name is ",obj_name;
            print "EXPECTED RESULT 2: rbus_registerObj should be success";
            print "ACTUAL RESULT 2: rbus_registerObj was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "\nAdding Element Before UnRegistering Object";
            element_name = "element1"
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","addElement");
            tdkTestObj.addParameter("objectName",obj_name);
            tdkTestObj.addParameter("methodName",element_name); # methodName will be converted as Element name in stub
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS add Element Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Add element with object, Element_Name is ",element_name;
                print "EXPECTED RESULT 3: rbus_addElement should be success if object is registered";
                print "ACTUAL RESULT 3: rbus_addElement was successful";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                print "\nRemoving the added Element Before UnRegistering Object";
                element_name = "element1"
                tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                tdkTestObj.addParameter("operation","removeElement");
                tdkTestObj.addParameter("objectName",obj_name);
                tdkTestObj.addParameter("methodName",element_name); # methodName will be converted as Element name in stub
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "RBUS Remove Element Detail is ",details

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Remove element with object, Element_Name is ",element_name;
                    print "EXPECTED RESULT 3: rbus_removeElement should be success if object is registered";
                    print "ACTUAL RESULT 3: rbus_removeElement was successful";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Remove element with object, Element_Name is ",element_name;
                    print "EXPECTED RESULT 3: rbus_removeElement should be success if object is registered";
                    print "ACTUAL RESULT 3: rbus_removeElement was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Add element with object, Element_Name is ",element_name;
                print "EXPECTED RESULT 3: rbus_addElement should be success if object is registered";
                print "ACTUAL RESULT 3: rbus_addElement was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE" ;

            print "\n*************Start of unregistering Object *******************************";
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","unregisterObj");
            tdkTestObj.addParameter("objectName",obj_name);
            tdkTestObj.addParameter("methodName","dummy");       #Dummy Value
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS unregister Obj Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: UnRegister the object with RBUS, Object name is ",obj_name;
                print "EXPECTED RESULT 4: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 4: rbus_unregisterObj was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "\nAddElement After unregistering the object - Negative Scenario"
                element_name = "element3"
                tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                tdkTestObj.addParameter("operation","addElement");
                tdkTestObj.addParameter("objectName",obj_name);
                tdkTestObj.addParameter("methodName",element_name); # methodName will be converted as Element name in stub
                expectedresult="FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "RBUS add Element Detail is ",details

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Adding the element with object, Element_Name is ",element_name;
                    print "EXPECTED RESULT 5: rbus_addElement should FAIL, if object is unregistered";
                    print "ACTUAL RESULT 5: rbus_addElement was Failed as expected";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Adding the element with object, Element_Name is ",element_name;
                    print "EXPECTED RESULT 5: rbus_addElement should FAIL, if object is unregistered";
                    print "ACTUAL RESULT 5: rbus_addElement was NOT Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: UnRegister the object with RBUS, Object name is ",obj_name;
                print "EXPECTED RESULT 4: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 4: rbus_unregisterObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Register the object with RBUS, Object Name is ",obj_name;
            print "EXPECTED RESULT 2: rbus_registerObj should be success";
            print "ACTUAL RESULT 2: rbus_registerObj was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "\nClose The Broker Connection..."
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","closeBrokerConnection");
        tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
        tdkTestObj.addParameter("methodName","dummy");   #Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS closeBrokerConnection Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 6: Close the RBUS Broker connection";
            print "EXPECTED RESULT 6: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 6: rbus_closeBrokerConnection was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 6: Close the RBUS Broker connection";
            print "EXPECTED RESULT 6: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 6: rbus_closeBrokerConnection was Failed";
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

    print "*************End of Broker Connection*******************************\n"
    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

