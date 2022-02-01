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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_AddElementsWithMultipleObjects</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_RegisterOperation</primitive_test_name>
  <!--  -->
  <primitive_test_version>4</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the RBUS APIs rbus_addElement and rbus_removeElement by adding elements in multiple objects</synopsis>
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
    <test_case_id>TC_RBUS_44</test_case_id>
    <test_objective>To Validate the RBUS APIs rbus_addElement and rbus_removeElement by adding or removing elements in multiple objects</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_addElement
rbus_removeElement</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the rbus module
2. open the rbus broker connection using rbus_openBrokerConnection API
3. The rbus_openBrokerConnection should be success
4. In a loop Register 3 different objects using rbus_registerObj API and add multiple elements in each objects
5. Register object and addElement operation should be success
6. Remove all the elements added into the objects using rbus_removeElement API
7. Unregister all three objects using rbus_unregisterObj API, return status should be success
8. Close the rbus broker connection using rbus_closeBrokerConnection API
9. The rbus_closeBrokerConnection should be success
10. Unload the rbus module</automation_approch>
    <expected_output>Should be able to add or remove elements in multiple objects</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_AddElementsWithMultipleObjects</test_script>
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
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_RBUS_AddElementsWithMultipleObjects');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[RBUS LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    dynamic_element_name = 0

    print "\n*************Start of Broker Connection*******************************";
    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
    tdkTestObj.addParameter("operation","openBrokerConnection");
    tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
    tdkTestObj.addParameter("methodName","CloseConnectionBeforeOpen");#Close the connection before open if any

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "RBUS openBrokerConnection Detail is ",details

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS Broker connection ";
        print "EXPECTED RESULT 1: rbus_openBrokerConnection Should be success";
        print "ACTUAL RESULT 1: rbus_openBrokerConnection was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        for obj_count in range(1,4):
            if obj_count == 1:
                obj_name = "tdkb_server.obj1"
                dynamic_element_name = 0;
                element_count = 10;
            elif obj_count == 2:
                obj_name = "tdkb_server.obj2"
                dynamic_element_name = 10;
                element_count = 18;
            else:
                obj_name = "tdkb_server.obj3"
                dynamic_element_name = 18;
                element_count = 30;

            print "\n*************Start of Registering Object-%s *****************************" %obj_count
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","registerObj");
            tdkTestObj.addParameter("objectName",obj_name);
            tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value

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

                print "\n*************Start of Adding Elements in object-%s *****************************" %obj_count
                element_name = "";
                for element in range(dynamic_element_name,element_count):
                    element_name = "Element"+str(element);

                    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                    tdkTestObj.addParameter("operation","addElement");
                    tdkTestObj.addParameter("objectName",obj_name);
                    tdkTestObj.addParameter("methodName",element_name); # methodName will be converted as Element name in stub
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    print "RBUS register Element Detail is ",details

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Adding the element with object, Element_Name is ",element_name;
                        print "EXPECTED RESULT 3: rbus_addElement should be success";
                        print "ACTUAL RESULT 3: rbus_addElement was success";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Adding the element with object, Element_Name is ",element_name;
                        print "EXPECTED RESULT 3: rbus_addElement should be success";
                        print "ACTUAL RESULT 3: rbus_addElement was Failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "*************End of Adding Element in object - %s *******************************" %obj_count
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Register the object with RBUS, Object Name is ",obj_name;
                print "EXPECTED RESULT 2: rbus_registerObj should be success";
                print "ACTUAL RESULT 2: rbus_registerObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
            print "\n*************End of Registering Object %s *****************************" %obj_count

        sleep(30);

        for obj_count in range(1,4):
            if obj_count == 1:
                obj_name = "tdkb_server.obj1"
                dynamic_element_name = 0;
                element_count = 10;
            elif obj_count == 2:
                obj_name = "tdkb_server.obj2"
                dynamic_element_name = 10;
                element_count = 18;
            else:
                obj_name = "tdkb_server.obj3"
                dynamic_element_name = 18;
                element_count = 30;

            print "\n*************Start of RemoveElements in Object %s*****************************" %obj_count
            element_name = "";
            for element in range(dynamic_element_name,element_count):
                element_name = "Element"+str(element);

                tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
                tdkTestObj.addParameter("operation","removeElement");
                tdkTestObj.addParameter("objectName",obj_name);
                tdkTestObj.addParameter("methodName",element_name); # methodName will be converted as Element name in stub

                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "RBUS Remove Element Detail is ",details

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Remove the element with object, Element_Name is ",element_name;
                    print "EXPECTED RESULT 4: rbus_removeElement should be success";
                    print "ACTUAL RESULT 4: rbus_removeElement was success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Remove the element with object, Element_Name is ",element_name;
                    print "EXPECTED RESULT 4: rbus_removeElement should be success";
                    print "ACTUAL RESULT 4: rbus_removeElement was Failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            print "*************End of RemoveElements in Object %s*****************************\n" %obj_count

            print "*************Start of unregistering object- %s*****************************" %obj_count
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","unregisterObj");
            tdkTestObj.addParameter("objectName",obj_name);
            tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value

            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS unregister Obj Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: UnRegister the object with RBUS, Object name is ",obj_name;
                print "EXPECTED RESULT 5: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 5: rbus_unregisterObj was success";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 5: UnRegister the object with RBUS, Object name is ",obj_name;
                print "EXPECTED RESULT 5: rbus_unregisterObj should be success";
                print "ACTUAL RESULT 5: rbus_unregisterObj was Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

            print "*************End of unregistering object - %s*****************************\n" %obj_count

        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","closeBrokerConnection");
        tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
        tdkTestObj.addParameter("methodName","dummy");	 #Dummy Value

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
